#!/usr/bin/env python3
"""
parse_dxf.py — DXF Spatial Extraction Pipeline for Construction Document Intelligence

Extracts structured spatial data from .dxf files:
- Block inserts with attributes (doors, rooms, equipment)
- Hatch entities with material type mapping and area calculation
- Closed polylines with area/perimeter calculation
- Dimension entities with measured values
- Text/MText entities with locations
- Layer-based discipline grouping

Usage:
    python3 parse_dxf.py <input.dxf> [--output output.json] [--layers A-WALL,S-FNDN]
                                      [--blocks-only] [--hatches-only] [--summary]
                                      [--merge-with config.json]
"""

import argparse
import json
import math
import os
import sys
from datetime import datetime

try:
    import ezdxf
    from ezdxf.entities import Insert, Hatch, LWPolyline, Polyline, Dimension, Text, MText, Line, Arc, Circle
except ImportError:
    print("ERROR: ezdxf library not installed. Run: pip install ezdxf --break-system-packages")
    sys.exit(1)


# ── Hatch Pattern → Material Mapping ──────────────────────────────────────────

HATCH_MATERIAL_MAP = {
    "AR-CONC": "concrete",
    "AR-SAND": "sand_gravel",
    "ANSI31": "steel_section",
    "ANSI32": "steel_surface",
    "ANSI37": "cast_iron",
    "BRICK": "masonry",
    "EARTH": "earth_fill",
    "GRAVEL": "aggregate_base",
    "INSUL": "insulation",
    "AR-RSHKE": "wood_shingle",
    "MUDST": "clay_soil",
    "CROSS": "ceramic_tile",
    "DOTS": "VCT_resilient",
    "HONEY": "tile",
    "SACNCR": "concrete_block",
    "SOLID": "solid_fill",
}

# ── Layer Prefix → Discipline Mapping ─────────────────────────────────────────

LAYER_DISCIPLINE_MAP = {
    "A-": "architectural",
    "S-": "structural",
    "M-": "mechanical",
    "E-": "electrical",
    "P-": "plumbing",
    "F-": "fire_protection",
    "C-": "civil",
    "L-": "landscape",
    "G-": "general",
    "I-": "interior",
}

# ── Drawing Unit Constants ────────────────────────────────────────────────────

INSUNITS_MAP = {
    0: ("unitless", 1.0),
    1: ("inches", 1.0),
    2: ("feet", 12.0),
    3: ("miles", 63360.0),
    4: ("millimeters", 0.03937),
    5: ("centimeters", 0.3937),
    6: ("meters", 39.3701),
}


def get_discipline(layer_name: str) -> str:
    """Map a layer name to a construction discipline."""
    upper = layer_name.upper()
    for prefix, discipline in LAYER_DISCIPLINE_MAP.items():
        if upper.startswith(prefix):
            return discipline
    return "other"


def shoelace_area(vertices: list) -> float:
    """Calculate area of a simple polygon using the shoelace formula.

    Args:
        vertices: List of (x, y) tuples

    Returns:
        Absolute area in square drawing units
    """
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0


def polyline_perimeter(vertices: list, closed: bool = True) -> float:
    """Calculate perimeter of a polyline.

    Args:
        vertices: List of (x, y) tuples
        closed: Whether to include closing segment

    Returns:
        Total perimeter length in drawing units
    """
    if len(vertices) < 2:
        return 0.0
    total = 0.0
    n = len(vertices)
    limit = n if closed else n - 1
    for i in range(limit):
        j = (i + 1) % n
        dx = vertices[j][0] - vertices[i][0]
        dy = vertices[j][1] - vertices[i][1]
        total += math.sqrt(dx * dx + dy * dy)
    return total


def convert_to_inches(value: float, units_factor: float) -> float:
    """Convert a drawing-unit value to inches."""
    return value * units_factor


def sq_inches_to_sq_feet(sq_inches: float) -> float:
    """Convert square inches to square feet."""
    return sq_inches / 144.0


def inches_to_feet(inches: float) -> float:
    """Convert inches to linear feet."""
    return inches / 12.0


def extract_blocks(msp, layer_filter=None) -> list:
    """Extract all block inserts with attributes from modelspace.

    Returns list of dicts with block name, position, attributes, layer, rotation.
    """
    blocks = []
    for entity in msp.query("INSERT"):
        layer = entity.dxf.layer
        if layer_filter and not any(layer.upper().startswith(f.upper()) for f in layer_filter):
            continue

        block_data = {
            "block_name": entity.dxf.name,
            "layer": layer,
            "discipline": get_discipline(layer),
            "insertion_point": {
                "x": round(entity.dxf.insert.x, 4),
                "y": round(entity.dxf.insert.y, 4),
                "z": round(entity.dxf.insert.z, 4) if hasattr(entity.dxf, 'insert') and entity.dxf.insert.z else 0.0
            },
            "rotation": round(entity.dxf.rotation, 2) if hasattr(entity.dxf, 'rotation') else 0.0,
            "scale": {
                "x": round(entity.dxf.xscale, 4) if hasattr(entity.dxf, 'xscale') else 1.0,
                "y": round(entity.dxf.yscale, 4) if hasattr(entity.dxf, 'yscale') else 1.0,
            },
            "attributes": {}
        }

        # Extract attribute values
        if entity.attribs:
            for attrib in entity.attribs:
                tag = attrib.dxf.tag
                value = attrib.dxf.text
                if tag and value:
                    block_data["attributes"][tag] = value

        blocks.append(block_data)

    return blocks


def classify_block(block_data: dict) -> str:
    """Classify a block insert by its type based on name and attributes."""
    name = block_data["block_name"].upper()
    attrs = {k.upper(): v for k, v in block_data["attributes"].items()}

    # Door blocks
    if any(kw in name for kw in ["DOOR", "DR-", "D-TAG", "DR_"]):
        return "door"
    if "DOOR_NO" in attrs or "DOOR_NUM" in attrs or "DR_NO" in attrs:
        return "door"

    # Room tag blocks
    if any(kw in name for kw in ["ROOM", "RM-", "RM_TAG", "ROOM_TAG"]):
        return "room_tag"
    if "ROOM_NO" in attrs or "ROOM_NAME" in attrs or "RM_NO" in attrs:
        return "room_tag"

    # Equipment blocks
    if any(kw in name for kw in ["EQUIP", "EQ-", "EQ_TAG"]):
        return "equipment"
    if "EQUIP_TAG" in attrs or "EQUIPMENT" in attrs:
        return "equipment"

    # Plumbing fixture blocks
    if any(kw in name for kw in ["WC", "LAV", "SINK", "SHOWER", "FIXT"]):
        return "plumbing_fixture"
    if "FIXT_TAG" in attrs:
        return "plumbing_fixture"

    # Light fixture blocks
    if any(kw in name for kw in ["LIGHT", "LT-", "LT_TAG", "FIXTURE"]):
        return "light_fixture"

    # Electrical blocks
    if any(kw in name for kw in ["RECEP", "OUTLET", "SWITCH", "PANEL"]):
        return "electrical"

    # Sprinkler blocks
    if any(kw in name for kw in ["SPRK", "SPRINKLER", "SPRNK"]):
        return "sprinkler"

    # Fire alarm blocks
    if any(kw in name for kw in ["FA-", "PULL", "SMOKE", "HORN", "STROBE"]):
        return "fire_alarm"

    return "other"


def extract_hatches(msp, units_factor: float, layer_filter=None) -> list:
    """Extract all hatch entities with pattern, material, boundary, and area.

    Returns list of dicts with hatch data and calculated areas.
    """
    hatches = []
    for entity in msp.query("HATCH"):
        layer = entity.dxf.layer
        if layer_filter and not any(layer.upper().startswith(f.upper()) for f in layer_filter):
            continue

        pattern = entity.dxf.pattern_name if hasattr(entity.dxf, 'pattern_name') else "SOLID"
        material = HATCH_MATERIAL_MAP.get(pattern.upper(), f"unknown ({pattern})")

        # Calculate area from boundary paths
        total_area_sq_units = 0.0
        boundaries = []

        try:
            for path in entity.paths:
                vertices = []
                if hasattr(path, 'vertices'):
                    # PolylinePath
                    for v in path.vertices:
                        vertices.append((v[0], v[1]))
                elif hasattr(path, 'edges'):
                    # EdgePath — approximate from edges
                    for edge in path.edges:
                        if hasattr(edge, 'start'):
                            vertices.append((edge.start[0], edge.start[1]))

                if len(vertices) >= 3:
                    area_sq_units = shoelace_area(vertices)
                    total_area_sq_units += area_sq_units
                    boundaries.append({
                        "vertex_count": len(vertices),
                        "area_sq_units": round(area_sq_units, 2)
                    })
        except Exception:
            # Some hatch boundaries are complex — skip silently
            pass

        # Convert area to square feet
        area_sq_inches = total_area_sq_units * (units_factor ** 2)
        area_sf = sq_inches_to_sq_feet(area_sq_inches)

        hatch_data = {
            "layer": layer,
            "discipline": get_discipline(layer),
            "pattern": pattern,
            "material": material,
            "area_sf": round(area_sf, 1),
            "boundary_count": len(boundaries),
            "boundaries": boundaries
        }

        hatches.append(hatch_data)

    return hatches


def extract_polylines(msp, units_factor: float, layer_filter=None) -> list:
    """Extract closed polylines with area and perimeter calculations.

    Returns list of dicts with polyline data.
    """
    polylines = []

    for entity in msp.query("LWPOLYLINE"):
        layer = entity.dxf.layer
        if layer_filter and not any(layer.upper().startswith(f.upper()) for f in layer_filter):
            continue

        if not entity.closed:
            continue

        vertices = [(p[0], p[1]) for p in entity.get_points(format="xy")]
        if len(vertices) < 3:
            continue

        area_sq_units = shoelace_area(vertices)
        perim_units = polyline_perimeter(vertices, closed=True)

        area_sq_inches = area_sq_units * (units_factor ** 2)
        perim_inches = perim_units * units_factor

        polylines.append({
            "layer": layer,
            "discipline": get_discipline(layer),
            "vertices": len(vertices),
            "area_sf": round(sq_inches_to_sq_feet(area_sq_inches), 1),
            "perimeter_lf": round(inches_to_feet(perim_inches), 1),
            "centroid": {
                "x": round(sum(v[0] for v in vertices) / len(vertices), 2),
                "y": round(sum(v[1] for v in vertices) / len(vertices), 2)
            }
        })

    return polylines


def extract_dimensions(msp, units_factor: float, layer_filter=None) -> list:
    """Extract dimension entities with measured values and reference points.

    Returns list of dicts with dimension data.
    """
    dimensions = []

    for entity in msp.query("DIMENSION"):
        layer = entity.dxf.layer
        if layer_filter and not any(layer.upper().startswith(f.upper()) for f in layer_filter):
            continue

        dim_data = {
            "layer": layer,
            "discipline": get_discipline(layer),
            "text": entity.dxf.text if hasattr(entity.dxf, 'text') and entity.dxf.text else "<measured>",
            "type": "linear",
        }

        # Try to get definition points
        try:
            if hasattr(entity.dxf, 'defpoint'):
                dim_data["defpoint1"] = {
                    "x": round(entity.dxf.defpoint.x, 4),
                    "y": round(entity.dxf.defpoint.y, 4)
                }
            if hasattr(entity.dxf, 'defpoint2'):
                dim_data["defpoint2"] = {
                    "x": round(entity.dxf.defpoint2.x, 4),
                    "y": round(entity.dxf.defpoint2.y, 4)
                }
        except Exception:
            pass

        # Flag overridden dimensions (text != empty means override)
        if dim_data["text"] and dim_data["text"] != "<measured>":
            dim_data["overridden"] = True
        else:
            dim_data["overridden"] = False
            # Try to get the actual measured value
            try:
                actual = entity.dxf.actual_measurement
                dim_data["measured_value_inches"] = round(actual * units_factor, 4)
                dim_data["measured_value_display"] = format_dimension(actual * units_factor)
            except Exception:
                pass

        dimensions.append(dim_data)

    return dimensions


def format_dimension(inches: float) -> str:
    """Format a dimension in inches as feet-inches string."""
    if inches < 0:
        inches = abs(inches)
    feet = int(inches // 12)
    remaining = inches % 12
    whole_inches = int(remaining)
    frac = remaining - whole_inches

    # Simple fraction approximation
    if frac < 0.0625:
        frac_str = ""
    elif frac < 0.1875:
        frac_str = " 1/8"
    elif frac < 0.3125:
        frac_str = " 1/4"
    elif frac < 0.4375:
        frac_str = " 3/8"
    elif frac < 0.5625:
        frac_str = " 1/2"
    elif frac < 0.6875:
        frac_str = " 5/8"
    elif frac < 0.8125:
        frac_str = " 3/4"
    elif frac < 0.9375:
        frac_str = " 7/8"
    else:
        whole_inches += 1
        frac_str = ""

    if feet > 0:
        return f"{feet}'-{whole_inches}{frac_str}\""
    else:
        return f"{whole_inches}{frac_str}\""


def extract_text(msp, layer_filter=None) -> list:
    """Extract all TEXT and MTEXT entities.

    Returns list of dicts with text content and location.
    """
    texts = []

    for entity in msp.query("TEXT MTEXT"):
        layer = entity.dxf.layer
        if layer_filter and not any(layer.upper().startswith(f.upper()) for f in layer_filter):
            continue

        content = ""
        if hasattr(entity, 'plain_text'):
            content = entity.plain_text()
        elif hasattr(entity.dxf, 'text'):
            content = entity.dxf.text

        if not content or not content.strip():
            continue

        insert = entity.dxf.insert if hasattr(entity.dxf, 'insert') else None

        text_data = {
            "content": content.strip(),
            "layer": layer,
            "discipline": get_discipline(layer),
            "height": round(entity.dxf.height, 2) if hasattr(entity.dxf, 'height') else 0,
            "rotation": round(entity.dxf.rotation, 2) if hasattr(entity.dxf, 'rotation') else 0,
        }

        if insert:
            text_data["position"] = {
                "x": round(insert.x, 2),
                "y": round(insert.y, 2)
            }

        texts.append(text_data)

    return texts


def get_drawing_units(doc) -> tuple:
    """Get drawing units from DXF header.

    Returns (unit_name, conversion_factor_to_inches)
    """
    try:
        insunits = doc.header.get("$INSUNITS", 0)
        return INSUNITS_MAP.get(insunits, ("unitless", 1.0))
    except Exception:
        return ("unitless", 1.0)


def aggregate_materials(hatches: list) -> dict:
    """Aggregate hatch areas by material type.

    Returns dict mapping material → total SF
    """
    materials = {}
    for h in hatches:
        mat = h["material"]
        if mat not in materials:
            materials[mat] = {"total_sf": 0.0, "hatch_count": 0}
        materials[mat]["total_sf"] += h["area_sf"]
        materials[mat]["hatch_count"] += 1

    # Round totals
    for mat in materials:
        materials[mat]["total_sf"] = round(materials[mat]["total_sf"], 1)

    return materials


def aggregate_blocks_by_type(blocks: list) -> dict:
    """Aggregate blocks by classification type.

    Returns dict mapping type → count and list
    """
    by_type = {}
    for b in blocks:
        btype = classify_block(b)
        if btype not in by_type:
            by_type[btype] = {"count": 0, "items": []}
        by_type[btype]["count"] += 1
        by_type[btype]["items"].append(b)
    return by_type


def layer_summary(msp) -> dict:
    """Summarize entities by layer.

    Returns dict mapping layer → entity count
    """
    layers = {}
    for entity in msp:
        layer = entity.dxf.layer if hasattr(entity.dxf, 'layer') else "0"
        if layer not in layers:
            layers[layer] = {"count": 0, "discipline": get_discipline(layer)}
        layers[layer]["count"] += 1
    return layers


def main():
    parser = argparse.ArgumentParser(
        description="Extract spatial data from DXF files for construction document intelligence"
    )
    parser.add_argument("input", help="Path to .dxf file")
    parser.add_argument("--output", "-o", help="Output JSON file path (default: stdout)")
    parser.add_argument("--layers", help="Comma-separated layer prefixes to filter (e.g., A-,S-)")
    parser.add_argument("--blocks-only", action="store_true", help="Extract only block inserts")
    parser.add_argument("--hatches-only", action="store_true", help="Extract only hatch entities")
    parser.add_argument("--summary", action="store_true", help="Output summary only")
    parser.add_argument("--merge-with", help="Path to existing config JSON to merge results into")

    args = parser.parse_args()

    # Validate input
    if not os.path.exists(args.input):
        print(f"ERROR: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if not args.input.lower().endswith(".dxf"):
        print(f"ERROR: Expected .dxf file, got: {args.input}", file=sys.stderr)
        print("For .dwg files, convert to .dxf first (ask architect for DXF export).", file=sys.stderr)
        sys.exit(1)

    # Parse layer filter
    layer_filter = None
    if args.layers:
        layer_filter = [l.strip() for l in args.layers.split(",")]

    # Open DXF
    try:
        doc = ezdxf.readfile(args.input)
    except ezdxf.DXFStructureError as e:
        print(f"ERROR: Invalid DXF file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Could not open DXF: {e}", file=sys.stderr)
        sys.exit(1)

    msp = doc.modelspace()
    unit_name, units_factor = get_drawing_units(doc)

    # Build output
    result = {
        "dxf_extraction": {
            "source_file": os.path.basename(args.input),
            "file_size_bytes": os.path.getsize(args.input),
            "extracted_date": datetime.now().isoformat(),
            "dxf_version": doc.dxfversion,
            "drawing_units": unit_name,
            "units_factor_to_inches": units_factor,
        }
    }

    # Layer summary (always included)
    layers = layer_summary(msp)
    result["dxf_extraction"]["layers"] = layers
    result["dxf_extraction"]["layer_count"] = len(layers)
    total_entities = sum(l["count"] for l in layers.values())
    result["dxf_extraction"]["total_entities"] = total_entities

    # Discipline summary
    disciplines = {}
    for layer_name, layer_data in layers.items():
        disc = layer_data["discipline"]
        if disc not in disciplines:
            disciplines[disc] = {"layers": 0, "entities": 0}
        disciplines[disc]["layers"] += 1
        disciplines[disc]["entities"] += layer_data["count"]
    result["dxf_extraction"]["disciplines"] = disciplines

    if args.summary:
        # Summary mode — just layer/discipline stats
        pass
    elif args.blocks_only:
        # Blocks only
        blocks = extract_blocks(msp, layer_filter)
        result["dxf_extraction"]["blocks"] = aggregate_blocks_by_type(blocks)
    elif args.hatches_only:
        # Hatches only
        hatches = extract_hatches(msp, units_factor, layer_filter)
        result["dxf_extraction"]["hatches"] = hatches
        result["dxf_extraction"]["material_areas"] = aggregate_materials(hatches)
    else:
        # Full extraction
        print(f"Processing {total_entities} entities across {len(layers)} layers...", file=sys.stderr)

        blocks = extract_blocks(msp, layer_filter)
        result["dxf_extraction"]["blocks"] = aggregate_blocks_by_type(blocks)
        print(f"  Blocks: {len(blocks)} inserts extracted", file=sys.stderr)

        hatches = extract_hatches(msp, units_factor, layer_filter)
        result["dxf_extraction"]["hatches_summary"] = {
            "count": len(hatches),
            "material_areas": aggregate_materials(hatches)
        }
        print(f"  Hatches: {len(hatches)} entities, {len(result['dxf_extraction']['hatches_summary']['material_areas'])} material types", file=sys.stderr)

        polylines = extract_polylines(msp, units_factor, layer_filter)
        result["dxf_extraction"]["closed_polylines"] = {
            "count": len(polylines),
            "items": polylines[:100]  # Limit to first 100 for readability
        }
        print(f"  Polylines: {len(polylines)} closed polylines", file=sys.stderr)

        dimensions = extract_dimensions(msp, units_factor, layer_filter)
        result["dxf_extraction"]["dimensions"] = {
            "count": len(dimensions),
            "items": dimensions[:200]  # Limit for readability
        }
        print(f"  Dimensions: {len(dimensions)} extracted", file=sys.stderr)

        texts = extract_text(msp, layer_filter)
        result["dxf_extraction"]["text"] = {
            "count": len(texts),
            "items": texts[:500]  # Limit for readability
        }
        print(f"  Text: {len(texts)} entities", file=sys.stderr)

    # Merge with existing config if requested
    if args.merge_with and os.path.exists(args.merge_with):
        try:
            with open(args.merge_with, "r") as f:
                existing = json.load(f)
            existing["dxf_extraction"] = result["dxf_extraction"]
            result = existing
            print(f"Merged DXF data into {args.merge_with}", file=sys.stderr)
        except Exception as e:
            print(f"WARNING: Could not merge with {args.merge_with}: {e}", file=sys.stderr)

    # Output
    output_json = json.dumps(result, indent=2, default=str)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output_json)


if __name__ == "__main__":
    main()
