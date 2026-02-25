# DXF/DWG Spatial Extraction Guide

Extract precise spatial data from CAD drawings (.dxf and .dwg files) that PDF-based extraction cannot capture: exact coordinates, layer organization, block attributes, dimensions, polyline geometry, and hatch areas. This guide covers the extraction pipeline, layer mapping, entity parsing, and integration with existing project intelligence.

---

## Why DXF Extraction Matters

When plans are exported to PDF, they become flat images. Claude can read text labels and visually interpret symbols, but spatial relationships are approximate. A .dxf file retains the actual geometry:

- **Coordinates**: Every wall, column line, and footing outline has exact X/Y/Z coordinates drawn at full scale
- **Layers**: AutoCAD layers (A-WALL, A-DOOR, S-FNDN, E-POWER) can be isolated for targeted extraction
- **Block attributes**: Door tags, room tags, and equipment tags are structured key-value data (DOOR_NO=101, SIZE=3'-0" x 7'-0", RATING=90-min)
- **Dimensions**: Every dimension string has the measured value plus the two points it spans — no scale calibration needed
- **Polylines**: Room boundaries, building footprints, and paving areas are closed polylines with exact vertices — areas can be calculated mathematically
- **Hatches**: Material zones (concrete, VCT, carpet, insulation) are hatched areas with exact boundaries and calculated square footages

---

## Supported File Types

### .dxf (Drawing Exchange Format)
- **Direct support**: Parsed natively using the `ezdxf` Python library (v1.4.3+)
- **Versions supported**: R12 through R2018
- **How to obtain**: Architect exports from AutoCAD (File → Save As → DXF), Revit (Export → CAD Formats → DXF), or any other CAD application

### .dwg (Native AutoCAD)
- **Requires conversion**: .dwg → .dxf using ODA File Converter (Open Design Alliance)
- **Current status**: ODA File Converter is NOT available on ARM64 Linux — only x86_64 builds exist
- **Workaround**: Ask the architect to export .dxf alongside PDF when issuing drawings. In AutoCAD this is one extra click in the publish routine. Most architects will accommodate this request — phrase it as: "Can you include DXF exports with the next drawing issue? We're building digital project intelligence and the DXF gives us exact geometry for quantity verification."

### .ifc (Industry Foundation Classes) — FUTURE
- **Not yet implemented** — documented for future reference
- **Library**: `ifcopenshell` Python library can parse .ifc files
- **Extracts**: Building elements (walls, doors, windows, slabs), spatial structure (floors, rooms, zones), material properties, quantities
- **When to implement**: When an architect/engineer uses Revit and exports IFC for a project
- **Advantage over DXF**: IFC carries semantic meaning (a wall knows it's a wall, with material, fire rating, and structural properties) whereas DXF just has geometry on layers

---

## Layer Mapping

Standard AutoCAD layer naming conventions follow the AIA CAD Layer Guidelines (US National CAD Standard). Map layer prefixes to construction disciplines:

### Architectural Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| A-WALL | Wall lines | Wall geometry, thickness, types, fire ratings |
| A-WALL-FIRE | Fire-rated walls | Fire rating boundaries, assembly types |
| A-DOOR | Door blocks | Door number, size, type, swing direction, rating |
| A-GLAZ | Windows/glazing | Window blocks with type, size, glazing spec |
| A-FLOR | Floor patterns/finishes | Finish boundaries, material hatches, room areas |
| A-FLOR-PATT | Floor hatch patterns | Material identification (VCT, carpet, tile, concrete) |
| A-CLNG | Ceiling elements | Ceiling grid, heights, types, soffits |
| A-FURN | Casework/built-ins | Cabinets, counters, built-in elements |
| A-EQPM | Equipment | Kitchen, laundry, specialty equipment |
| A-AREA | Area calculations | Room boundaries with area tags |
| A-ANNO | Annotations | Room tags, labels, notes |
| A-DIMS | Dimensions | Architectural dimensions |
| A-SYMB | Symbols | Section marks, detail marks, north arrows |

### Structural Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| S-COLS | Columns | Column centers, sizes, grid intersections |
| S-FNDN | Foundations | Footing outlines, pier locations, grade beams |
| S-BEAM | Beams | Beam lines, sizes, elevations |
| S-FRAM | Framing | Joist/rafter layout, bracing |
| S-SLAB | Slabs | Slab edges, thickening, construction joints |
| S-WALL | Structural walls | Shear walls, retaining walls |
| S-GRID | Grid lines | Column grid system (numbered/lettered) |
| S-DIMS | Dimensions | Structural dimensions |
| S-RBAR | Reinforcing | Rebar callouts, sections |

### Mechanical/HVAC Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| M-DUCT | Ductwork | Duct runs, sizes, routing |
| M-PIPR | Piping (refrigerant) | Refrigerant lines |
| M-EQPM | Equipment | RTUs, AHUs, unit heaters, exhaust fans |
| M-DIFF | Diffusers/grilles | Supply/return/exhaust locations |
| M-CTRL | Controls | Thermostats, sensors |
| M-DIMS | Dimensions | Mechanical dimensions |

### Electrical Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| E-POWR | Power | Receptacles, disconnects, panels |
| E-LITE | Lighting | Light fixtures, types, circuits |
| E-SWCH | Switches | Switch locations, types |
| E-DATA | Data/telecom | Data outlets, telecom |
| E-FIRE | Fire alarm | Pull stations, detectors, horns, strobes |
| E-SECY | Security | Card readers, cameras, motion sensors |
| E-DIMS | Dimensions | Electrical dimensions |

### Plumbing Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| P-FIXT | Fixtures | Toilets, sinks, showers, locations |
| P-PIPE | Piping | Pipe runs, sizes (domestic) |
| P-SANR | Sanitary | Sanitary waste, vents |
| P-STRM | Storm | Storm drains, roof drains |
| P-EQPM | Equipment | Water heaters, pumps |
| P-DIMS | Dimensions | Plumbing dimensions |

### Fire Protection Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| F-SPRN | Sprinklers | Head locations, types, coverage |
| F-PIPE | Piping | Main/branch, sizes |
| F-EQPM | Equipment | FDC, riser, valve locations |

### Civil Layers

| Layer Prefix | Content | Extract |
|-------------|---------|---------|
| C-TOPO | Topography | Contour lines, spot elevations |
| C-ROAD | Roads/paving | Pavement edges, curbs |
| C-PKNG | Parking | Stall outlines, counts |
| C-STRM | Storm drainage | Pipe runs, inlets, manholes |
| C-WATR | Water | Water main, service, hydrants |
| C-SANR | Sanitary sewer | Sewer main, laterals, manholes |
| C-BLDG | Building footprint | Foundation/building outline |
| C-DIMS | Dimensions | Civil dimensions |

---

## Entity Extraction Rules

### Block Inserts (INSERT entities)

Block inserts are the richest data source in DXF files. Each insert represents a symbol placed on the drawing with structured attribute data.

**For each block insert, extract**:
- **Block name**: Identifies the symbol type (DOOR, ROOM_TAG, EQUIPMENT_TAG, etc.)
- **Insertion point**: X/Y coordinates (exact location on plan)
- **All attribute key-value pairs**: The structured data attached to the symbol
- **Rotation angle**: Which way the symbol faces (critical for door swings)
- **Scale factors**: Usually 1:1 if drawn at full scale
- **Layer**: Which layer the insert is on

**Common block types and their attributes**:

| Block Name Pattern | Type | Expected Attributes |
|-------------------|------|-------------------|
| DOOR, DR, D-TAG | Door | DOOR_NO, SIZE, TYPE, RATING, HARDWARE_GROUP |
| ROOM, RM, RM-TAG | Room tag | ROOM_NO, ROOM_NAME, AREA, DEPARTMENT |
| EQUIP, EQ-TAG | Equipment | EQUIP_TAG, TYPE, MODEL, CAPACITY |
| WC, LAV, SINK | Plumbing fixture | FIXT_TAG, TYPE, MODEL |
| LIGHT, LT-TAG | Light fixture | FIXTURE_TYPE, WATTAGE, CIRCUIT |
| RECEP, OUTLET | Receptacle | CIRCUIT, TYPE (duplex, GFCI, etc.) |
| PANEL | Electrical panel | PANEL_NAME, VOLTAGE, AMPERAGE |
| SPRK, SPRINKLER | Sprinkler head | HEAD_TYPE, K_FACTOR, TEMP_RATING |

### Hatch Entities

Hatches identify material types visually. Each HATCH entity has a pattern name, boundary, and layer.

**Standard hatch pattern to material mapping**:

| Pattern Name | Material | Typical Use |
|-------------|----------|-------------|
| AR-CONC | Concrete | Foundation sections, slab sections, walls |
| AR-SAND | Sand/gravel | Fill material, base course |
| ANSI31 | Steel (section cut) | Steel beam/column sections |
| ANSI32 | Steel (surface) | Steel plates, brackets |
| ANSI37 | Cast iron | Pipe sections, grates |
| BRICK | Masonry/brick | Brick walls, veneers |
| EARTH | Earth fill | Embankments, backfill zones |
| GRAVEL | Aggregate base | Under slab, parking base |
| INSUL | Insulation | Wall cavities, roof insulation |
| AR-RSHKE | Wood shingles | Roofing (if wood) |
| MUDST | Mud/clay | Foundation bearing soils |
| CROSS | Tile/ceramic | Tile floors, shower walls |
| DOTS | VCT/resilient | Vinyl composition tile, sheet vinyl |
| SOLID (colored) | Various | Color-coded material zones |

**For each hatch, extract**:
- Pattern name → material type (using mapping above)
- Boundary vertices → calculate area (SF)
- Layer → discipline context
- Color → may indicate material subtype

**Aggregate hatch areas by material type and layer** to produce totals:
```json
{
  "material_areas": {
    "concrete": {"total_sf": 4250, "locations": ["footings", "SOG", "walls"]},
    "VCT": {"total_sf": 2800, "rooms": ["101", "102", "103", "107"]},
    "carpet_tile": {"total_sf": 1200, "rooms": ["104", "105"]},
    "ceramic_tile": {"total_sf": 450, "rooms": ["WC-1", "WC-2", "shower"]},
    "insulation": {"total_sf": 6500, "type": "wall_cavity"},
    "earth_fill": {"total_sf": 1800, "location": "backfill"}
  }
}
```

### Closed Polylines (LWPOLYLINE, POLYLINE)

Closed polylines define boundaries — rooms, building footprint, paving areas, landscape zones.

**For each closed polyline, extract**:
- All vertices (X/Y coordinates)
- Calculated area (SF) using the shoelace formula
- Calculated perimeter (LF)
- Layer (identifies what the boundary represents)
- Associated text/tags nearby (room numbers, area labels)

**Area calculation**: Use the shoelace formula for simple polygons. For polylines with arc segments (bulge factors), integrate the arc area contribution.

### Dimension Entities (DIMENSION)

Dimensions contain precise measurements with their reference points.

**For each dimension, extract**:
- **Measured value**: The dimension text (e.g., "25'-0\"")
- **Definition points**: The two points being measured between
- **Dimension type**: Linear, aligned, angular, radial, ordinate
- **Layer**: Context (architectural, structural, civil)
- **Override flag**: If the dimension text has been manually overridden (less reliable)

### Text and MText Entities

All text on the drawing contains potential intelligence.

**For each text entity, extract**:
- **Content**: The actual text string
- **Insertion point**: X/Y location on drawing
- **Layer**: Context
- **Height**: Text height (larger = more important — titles, notes headers)
- **Rotation**: Angle (rotated text is common for dimensions, labels)

**Priority text to identify**:
- Title block information (project name, number, date, revision)
- General notes (numbered paragraphs — usually critical requirements)
- Room names and numbers
- Equipment tags
- Grid labels
- Revision descriptions

### Line and Arc Entities

Lines and arcs form the geometric framework.

**Extract selectively** (there are thousands of lines — focus on):
- Lines on grid layers (S-GRID): Column grid spacing
- Lines on wall layers (A-WALL): Wall layout geometry
- Lines on slab layers (S-SLAB): Slab edges, joints
- Arcs on curb layers (C-ROAD): Curb radii

---

## Extraction Pipeline

### Overview

The extraction pipeline is implemented in `parse_dxf.py` and follows this sequence:

```
Input (.dxf) → ezdxf parser → Entity enumeration → Layer grouping →
  Block extraction → Hatch extraction → Geometry extraction →
  Dimension extraction → Text extraction → JSON output
```

### Running the Pipeline

```bash
python3 parse_dxf.py /path/to/drawing.dxf --output /path/to/output.json
```

**Options**:
- `--layers LAYER1,LAYER2`: Filter to specific layers only
- `--blocks-only`: Extract only block inserts with attributes
- `--hatches-only`: Extract only hatch entities with areas
- `--summary`: Output a summary instead of full extraction
- `--merge-with CONFIG.json`: Merge DXF data into existing project intelligence

### Pipeline Steps

1. **Open DXF**: Load with ezdxf, get modelspace entities
2. **Enumerate layers**: List all layers with entity counts per layer
3. **Classify by discipline**: Group layers by prefix (A-, S-, M-, E-, P-, F-, C-)
4. **Extract blocks**: All INSERT entities with attributes
5. **Extract hatches**: All HATCH entities with pattern, boundary, area
6. **Extract polylines**: All closed LWPOLYLINE/POLYLINE with area/perimeter
7. **Extract dimensions**: All DIMENSION entities with values and points
8. **Extract text**: All TEXT/MTEXT entities with content and location
9. **Aggregate**: Material areas, room areas, equipment counts
10. **Output**: Structured JSON matching project intelligence schema

---

## .dwg Conversion

### Current Status

The ODA File Converter (the standard tool for .dwg → .dxf conversion) is **not available on ARM64 Linux**. Only x86_64 builds exist.

### Workaround

Ask the architect to export .dxf alongside PDF:

> "Can you include DXF exports with the next drawing issue? We're building digital project intelligence and the DXF gives us exact geometry for quantity verification."

In AutoCAD, this is one extra click in the publish routine. Most architects will accommodate the request.

### Future: If ODA Becomes Available

If ODA File Converter becomes available (e.g., on x86_64 system), the `convert_dwg.py` wrapper script handles:
1. Accept .dwg file path
2. Run ODA to convert .dwg → .dxf in temp directory
3. Feed .dxf into parse_dxf.py
4. Clean up temp files
5. Return structured JSON

---

## Integration with Project Intelligence

### DXF Data Priority

When both PDF-extracted and DXF-extracted data exist for the same drawing, **DXF data takes priority** because it contains exact geometry:

| Data Type | PDF Extraction | DXF Extraction | Priority |
|-----------|---------------|----------------|----------|
| Room areas | Estimated from scale | Exact from polyline | **DXF** |
| Door locations | Visual position | Exact coordinates | **DXF** |
| Door attributes | OCR from schedule table | Block attribute data | **DXF** |
| Grid spacing | Dimension text reading | Dimension entity + points | **DXF** |
| Material areas | Not available from PDF | Exact from hatch boundaries | **DXF only** |
| Wall lengths | Not available from PDF | Exact from polyline perimeter | **DXF only** |
| Equipment counts | Visual counting from PDF | Block insert count by type | **DXF** |
| General notes | Text extraction from PDF | Text entity extraction | **Equivalent** |

### Cross-Reference with PDF Extraction

After DXF extraction, compare against existing PDF-based data:

1. **Room schedule**: Match DXF room tags (block attributes) against PDF-extracted room schedule. Flag any rooms in DXF not in PDF schedule (or vice versa).
2. **Door schedule**: Match DXF door blocks against PDF door schedule. Verify counts and attributes match.
3. **Equipment**: Match DXF equipment blocks against PDF equipment schedules.
4. **Dimensions**: Verify DXF dimension values match PDF-read dimensions for spot checks.

### Output Schema

DXF extraction output merges into the project intelligence config:

```json
{
  "dxf_extraction": {
    "source_file": "A-100_Floor_Plan.dxf",
    "extracted_date": "2026-02-17",
    "layers_found": 45,
    "entities_processed": 12500,
    "disciplines": {
      "architectural": {"layers": 15, "entities": 6200},
      "structural": {"layers": 8, "entities": 2100},
      "mechanical": {"layers": 7, "entities": 1800},
      "electrical": {"layers": 9, "entities": 1500},
      "plumbing": {"layers": 4, "entities": 600},
      "civil": {"layers": 2, "entities": 300}
    },
    "blocks": {
      "doors": [...],
      "rooms": [...],
      "equipment": [...],
      "fixtures": [...]
    },
    "material_areas": {
      "concrete": {"total_sf": 4250},
      "VCT": {"total_sf": 2800},
      "carpet": {"total_sf": 1200}
    },
    "room_areas": [...],
    "dimensions": [...],
    "grid_lines": {...}
  }
}
```

---

## Notes

- Not all DXF files are created equal. Some architects freeze layers before exporting, hide entities, or use XREFs (external references) that don't embed. If extraction seems incomplete, ask for a "bind all XREFs and thaw all layers" export.
- DXF file sizes can be very large (50-200 MB for a full plan set). Parse selectively by layer when possible.
- Drawing units matter. Most architectural drawings use inches or feet. Civil drawings often use feet or survey feet. The parse_dxf.py script auto-detects units from the DXF header ($INSUNITS variable).
- Some DXF files use proxy entities or custom objects from third-party AutoCAD plugins. These are skipped during extraction with a warning.
