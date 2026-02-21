#!/usr/bin/env python3
"""
Multi-source calculation bridge for construction quantities.

Integrates assembly chains (from sheet_xref.py) with extracted data from
DXF, visual, takeoff, and text sources to calculate derived quantities
and flag discrepancies.
"""

import json
import math
import re
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


class SourcePriority(Enum):
    """Source priority order for quantity resolution."""
    DXF = 1
    VISUAL = 2
    TAKEOFF = 3
    TEXT = 4


@dataclass
class QuantityResult:
    """Result of a quantity calculation with multi-source validation."""
    element: str
    element_type: str
    value: float
    unit: str
    source: str
    source_sheets: List[str] = field(default_factory=list)
    confidence: float = 0.8
    validated_by: List[str] = field(default_factory=list)
    discrepancy: bool = False
    discrepancy_details: str = ""


@dataclass
class DiscrepancyRecord:
    """Record of a discrepancy between sources."""
    element: str
    field: str
    sources: Dict[str, float]
    variance_pct: float
    resolution_status: str = "unresolved"
    resolution_notes: str = ""


class DimensionParser:
    """Parse construction dimensions from text."""

    @staticmethod
    def parse_dimension(text: str) -> Optional[float]:
        """
        Parse dimension string to decimal feet.

        Supports: "4'-6\"", "2'-0\"", "10 ft", "120 inches", "12.5"
        Returns None if parsing fails.
        """
        if not text or not isinstance(text, str):
            return None

        text = text.strip()

        # Format: 4'-6"
        match = re.match(r"(\d+)'(?:(\d+))?\"?", text)
        if match:
            feet = int(match.group(1))
            inches = int(match.group(2)) if match.group(2) else 0
            return feet + inches / 12.0

        # Format: 10 ft or 10ft
        match = re.search(r"(\d+(?:\.\d+)?)\s*(?:ft|feet)", text)
        if match:
            return float(match.group(1))

        # Format: 120 inches
        match = re.search(r"(\d+(?:\.\d+)?)\s*(?:in|inches)", text)
        if match:
            return float(match.group(1)) / 12.0

        # Decimal feet
        try:
            return float(text)
        except ValueError:
            return None

    @staticmethod
    def cubic_feet_to_cubic_yards(cubic_feet: float) -> float:
        """Convert cubic feet to cubic yards."""
        return cubic_feet / 27.0

    @staticmethod
    def square_inches_to_square_feet(square_inches: float) -> float:
        """Convert square inches to square feet."""
        return square_inches / 144.0


class WasteFactorCalculator:
    """Apply waste factors to quantities based on element type."""

    WASTE_FACTORS = {
        "footing": 0.10,
        "sog": 0.03,
        "grade_beam": 0.05,
        "pier": 0.05,
        "wall": 0.05,
        "curb": 0.05,
        "concrete": 0.05,
    }

    @staticmethod
    def apply_waste_factor(qty: float, element_type: str) -> float:
        """Apply appropriate waste factor to quantity."""
        factor = WasteFactorCalculator.WASTE_FACTORS.get(
            element_type.lower(), 0.0
        )
        return qty * (1.0 + factor)


class PolygonCalculator:
    """Calculate properties of polygons (area, perimeter)."""

    @staticmethod
    def shoelace_area(vertices: List[Tuple[float, float]]) -> float:
        """
        Calculate area of polygon using shoelace formula.

        vertices: List of (x, y) tuples in order
        Returns: Area in square units
        """
        if len(vertices) < 3:
            return 0.0

        n = len(vertices)
        area = 0.0
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            area += x1 * y2 - x2 * y1

        return abs(area) / 2.0

    @staticmethod
    def polyline_perimeter(vertices: List[Tuple[float, float]]) -> float:
        """Calculate perimeter of polyline."""
        if len(vertices) < 2:
            return 0.0

        perimeter = 0.0
        n = len(vertices)
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            perimeter += distance

        return perimeter


class ConcreteCalculator:
    """Calculate concrete quantities for various elements."""

    def __init__(self):
        self.parser = DimensionParser()
        self.waste = WasteFactorCalculator()

    def calculate_footing(
        self,
        length: float,
        width: float,
        depth: float,
        count: int = 1,
    ) -> float:
        """Calculate footing volume in cubic yards."""
        cf = length * width * depth * count
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "footing")

    def calculate_sog(self, area: float, thickness: float) -> float:
        """Calculate slab-on-grade volume in cubic yards."""
        cf = area * thickness
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "sog")

    def calculate_grade_beam(
        self, length: float, width: float, depth: float
    ) -> float:
        """Calculate grade beam volume in cubic yards."""
        cf = length * width * depth
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "grade_beam")

    def calculate_pier_circular(self, radius: float, depth: float) -> float:
        """Calculate circular pier volume in cubic yards."""
        cf = math.pi * (radius ** 2) * depth
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "pier")

    def calculate_pier_rectangular(
        self, length: float, width: float, depth: float
    ) -> float:
        """Calculate rectangular pier volume in cubic yards."""
        cf = length * width * depth
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "pier")

    def calculate_wall(
        self, length: float, height: float, thickness: float
    ) -> float:
        """Calculate concrete wall volume in cubic yards."""
        cf = length * height * thickness
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "wall")

    def calculate_curb(
        self, length: float, width: float, height: float
    ) -> float:
        """Calculate curb volume in cubic yards."""
        cf = length * width * height
        cy = self.parser.cubic_feet_to_cubic_yards(cf)
        return self.waste.apply_waste_factor(cy, "curb")


class AreaCalculator:
    """Calculate room and material areas."""

    def __init__(self):
        self.polygon = PolygonCalculator()

    def calculate_room_area(
        self, vertices: Optional[List[Tuple[float, float]]] = None,
        pixel_count: Optional[float] = None,
        pixels_per_sf: float = 1.0,
    ) -> float:
        """
        Calculate room area in square feet.

        Use vertices (from DXF polylines) or pixel_count (from visual).
        """
        if vertices:
            return self.polygon.shoelace_area(vertices)
        elif pixel_count is not None and pixels_per_sf > 0:
            return pixel_count / pixels_per_sf
        return 0.0

    def calculate_room_perimeter(
        self, vertices: List[Tuple[float, float]]
    ) -> float:
        """Calculate room perimeter from vertices."""
        return self.polygon.polyline_perimeter(vertices)

    def calculate_wall_area(self, perimeter: float, height: float) -> float:
        """Calculate wall area = perimeter × height."""
        return perimeter * height

    def aggregate_flooring(
        self, room_areas: Dict[str, float], finish_schedule: Dict[str, str]
    ) -> Dict[str, float]:
        """
        Aggregate flooring by type.

        finish_schedule maps room_id → floor type
        Returns: Dict[floor_type → total_sf]
        """
        by_type = {}
        for room_id, area in room_areas.items():
            floor_type = finish_schedule.get(room_id, "unknown")
            if floor_type not in by_type:
                by_type[floor_type] = 0.0
            by_type[floor_type] += area
        return by_type


class LinearCalculator:
    """Calculate linear quantities."""

    def __init__(self):
        self.polygon = PolygonCalculator()

    def calculate_wall_lengths(
        self, polylines: Dict[str, List[Tuple[float, float]]]
    ) -> Dict[str, float]:
        """Calculate wall length by type from polylines."""
        lengths = {}
        for wall_type, vertices in polylines.items():
            lengths[wall_type] = self.polygon.polyline_perimeter(vertices)
        return lengths

    def aggregate_pipe_runs(
        self, pipe_data: List[Dict[str, Any]]
    ) -> Dict[str, float]:
        """
        Aggregate pipe runs by size, avoiding double-counting.

        pipe_data: List of {"size": "2\"", "length": 50, "sheet": "A2.1"}
        Returns: Dict[size → total_lf]
        """
        by_size = {}
        seen_pipes = set()

        for pipe in pipe_data:
            size = pipe.get("size", "unknown")
            length = pipe.get("length", 0.0)
            sheet = pipe.get("sheet", "")

            key = (size, sheet)
            if key not in seen_pipes:
                if size not in by_size:
                    by_size[size] = 0.0
                by_size[size] += length
                seen_pipes.add(key)

        return by_size

    def calculate_base_trim(self, perimeter: float) -> float:
        """Calculate base trim LF (= room perimeter)."""
        return perimeter


class CountCalculator:
    """Calculate element counts with anti-double-counting."""

    @staticmethod
    def count_symbols(
        visual_detections: List[Dict[str, Any]],
        sheets_overlapping: Dict[str, List[str]],
    ) -> Dict[str, int]:
        """
        Count symbols with anti-double-counting.

        visual_detections: List of {"symbol": "door_swing", "sheet": "A2.1"}
        sheets_overlapping: Dict["A2.1"] = ["A2.2", ...] (sheets that overlap)
        Returns: Dict[symbol → count]
        """
        by_symbol = {}
        counted = set()

        for detection in visual_detections:
            symbol = detection.get("symbol", "unknown")
            sheet = detection.get("sheet", "")
            position = detection.get("position", (0, 0))

            # Create unique key avoiding double-counts
            key = (symbol, sheet, tuple(position))
            if key not in counted:
                if symbol not in by_symbol:
                    by_symbol[symbol] = 0
                by_symbol[symbol] += 1
                counted.add(key)

        return by_symbol

    @staticmethod
    def compare_to_schedule(
        visual_counts: Dict[str, int],
        schedule_counts: Dict[str, int],
    ) -> Dict[str, Dict[str, Any]]:
        """
        Compare visual counts to schedule counts.

        Returns: Dict[element → {"visual": ..., "schedule": ..., "discrepancy": bool}]
        """
        result = {}
        all_keys = set(visual_counts.keys()) | set(schedule_counts.keys())

        for key in all_keys:
            v_count = visual_counts.get(key, 0)
            s_count = schedule_counts.get(key, 0)
            discrepancy = v_count != s_count

            result[key] = {
                "visual": v_count,
                "schedule": s_count,
                "discrepancy": discrepancy,
            }

        return result


class AggregateCalculator:
    """Roll up quantities by CSI division."""

    @staticmethod
    def aggregate_by_division(quantities: List[QuantityResult]) -> Dict[str, Dict[str, Any]]:
        """Aggregate quantities by CSI division."""
        divisions = {
            "03": {"name": "Concrete", "items": {}},
            "08": {"name": "Doors/Windows", "items": {}},
            "09": {"name": "Finishes", "items": {}},
            "22": {"name": "Plumbing", "items": {}},
            "26": {"name": "Electrical", "items": {}},
        }

        for qty in quantities:
            element_type = qty.element_type.lower()

            if "concrete" in element_type or "footing" in element_type:
                div = divisions.setdefault("03", {})["items"]
                if "total_cy" not in div:
                    div["total_cy"] = 0.0
                div["total_cy"] += qty.value
            elif "door" in element_type:
                div = divisions.setdefault("08", {})["items"]
                if "doors" not in div:
                    div["doors"] = 0
                div["doors"] += int(qty.value)
            elif "flooring" in element_type or "gwb" in element_type:
                div = divisions.setdefault("09", {})["items"]
                if qty.unit == "sf":
                    if f"{element_type}_sf" not in div:
                        div[f"{element_type}_sf"] = 0.0
                    div[f"{element_type}_sf"] += qty.value
            elif "pipe" in element_type:
                div = divisions.setdefault("22", {})["items"]
                size = element_type.split("_")[-1]
                key = f"pipe_{size}_lf"
                if key not in div:
                    div[key] = 0.0
                div[key] += qty.value
            elif "outlet" in element_type or "switch" in element_type:
                div = divisions.setdefault("26", {})["items"]
                if f"{element_type}_count" not in div:
                    div[f"{element_type}_count"] = 0
                div[f"{element_type}_count"] += int(qty.value)

        return divisions


class DiscrepancyTracker:
    """Track and report discrepancies between sources."""

    def __init__(self):
        self.records: List[DiscrepancyRecord] = []

    def log_comparison(
        self,
        element: str,
        field: str,
        sources: Dict[str, float],
        variance_threshold_pct: float = 10.0,
    ) -> bool:
        """
        Log a comparison between sources.

        Returns: True if discrepancy detected (variance > threshold)
        """
        if len(sources) < 2:
            return False

        values = list(sources.values())
        max_val = max(values)
        min_val = min(values)

        if min_val == 0 and max_val > 0:
            variance_pct = 100.0
        elif max_val == 0:
            variance_pct = 0.0
        else:
            variance_pct = ((max_val - min_val) / max_val) * 100.0

        if variance_pct > variance_threshold_pct:
            record = DiscrepancyRecord(
                element=element,
                field=field,
                sources=sources.copy(),
                variance_pct=variance_pct,
            )
            self.records.append(record)
            return True

        return False

    def resolve_discrepancy(
        self, element: str, field: str, resolution_status: str,
        resolution_notes: str = ""
    ) -> None:
        """Mark a discrepancy as resolved."""
        for record in self.records:
            if record.element == element and record.field == field:
                record.resolution_status = resolution_status
                record.resolution_notes = resolution_notes
                break

    def generate_report(self) -> Dict[str, Any]:
        """Generate discrepancy report."""
        unresolved = [r for r in self.records if r.resolution_status == "unresolved"]
        resolved = [r for r in self.records if r.resolution_status != "unresolved"]

        return {
            "total_discrepancies": len(self.records),
            "unresolved": len(unresolved),
            "resolved": len(resolved),
            "details": [asdict(r) for r in self.records],
        }


class CalcBridge:
    """Main orchestrator for multi-source calculation."""

    def __init__(self):
        self.concrete_calc = ConcreteCalculator()
        self.area_calc = AreaCalculator()
        self.linear_calc = LinearCalculator()
        self.count_calc = CountCalculator()
        self.aggregate_calc = AggregateCalculator()
        self.discrepancy_tracker = DiscrepancyTracker()
        self.parser = DimensionParser()

        self.dxf_data = {}
        self.visual_data = {}
        self.takeoff_data = {}
        self.text_data = {}
        self.assembly_chains = {}
        self.results: List[QuantityResult] = []

    def load_extraction_data(
        self,
        dxf_json: Optional[str],
        visual_json: Optional[str],
        takeoff_json: Optional[str],
        text_json: Optional[str],
    ) -> None:
        """Load extracted data from all sources."""
        if dxf_json and Path(dxf_json).exists():
            with open(dxf_json) as f:
                self.dxf_data = json.load(f)
        if visual_json and Path(visual_json).exists():
            with open(visual_json) as f:
                self.visual_data = json.load(f)
        if takeoff_json and Path(takeoff_json).exists():
            with open(takeoff_json) as f:
                self.takeoff_data = json.load(f)
        if text_json and Path(text_json).exists():
            with open(text_json) as f:
                self.text_data = json.load(f)

    def load_assembly_chains(self, xref_json: str) -> None:
        """Load cross-reference chains from sheet_xref.py output."""
        if Path(xref_json).exists():
            with open(xref_json) as f:
                self.assembly_chains = json.load(f)

    def _resolve_value(
        self, element: str, field: str
    ) -> Tuple[Optional[float], str, List[str]]:
        """
        Resolve value across sources by priority.

        Returns: (value, source_name, [validated_by_sources])
        """
        sources_data = {}

        if element in self.dxf_data and field in self.dxf_data[element]:
            sources_data["DXF"] = self.dxf_data[element][field]
        if element in self.visual_data and field in self.visual_data[element]:
            sources_data["VISUAL"] = self.visual_data[element][field]
        if element in self.takeoff_data and field in self.takeoff_data[element]:
            sources_data["TAKEOFF"] = self.takeoff_data[element][field]
        if element in self.text_data and field in self.text_data[element]:
            sources_data["TEXT"] = self.text_data[element][field]

        if not sources_data:
            return None, "", []

        # Sort by priority
        priority_order = ["DXF", "VISUAL", "TAKEOFF", "TEXT"]
        sorted_sources = sorted(
            sources_data.items(),
            key=lambda x: priority_order.index(x[0])
        )

        primary_source, primary_value = sorted_sources[0]
        validated_by = []

        # Check other sources for validation
        for source, value in sorted_sources[1:]:
            if primary_value and value:
                variance = abs(primary_value - value) / primary_value
                if variance <= 0.10:
                    validated_by.append(source)
                else:
                    self.discrepancy_tracker.log_comparison(
                        element, field, {primary_source: primary_value, source: value}
                    )

        return primary_value, primary_source, validated_by

    def calculate_element(self, element_id: str) -> Optional[QuantityResult]:
        """Calculate quantity for a single element."""
        value, source, validated_by = self._resolve_value(element_id, "quantity")

        if value is None:
            return None

        element_type = self.dxf_data.get(element_id, {}).get("type", "unknown")
        unit = self.dxf_data.get(element_id, {}).get("unit", "")
        sheets = self.dxf_data.get(element_id, {}).get("sheets", [])

        result = QuantityResult(
            element=element_id,
            element_type=element_type,
            value=value,
            unit=unit,
            source=source,
            source_sheets=sheets,
            validated_by=validated_by,
            discrepancy=len(validated_by) < 1 and len(element_id) > 0,
        )

        return result

    def calculate_all(self) -> List[QuantityResult]:
        """Run all calculators and collect results."""
        all_elements = set()
        for data in [self.dxf_data, self.visual_data, self.takeoff_data, self.text_data]:
            all_elements.update(data.keys())

        self.results = []
        for element in all_elements:
            result = self.calculate_element(element)
            if result:
                self.results.append(result)

        return self.results

    def to_config_json(self) -> Dict[str, Any]:
        """Export results in config schema format."""
        return {
            "quantities": [asdict(r) for r in self.results],
            "divisions": self.aggregate_calc.aggregate_by_division(self.results),
            "discrepancies": self.discrepancy_tracker.generate_report(),
        }

    def from_config_json(self, data: Dict[str, Any]) -> None:
        """Load existing quantities for incremental updates."""
        if "quantities" in data:
            for qty_dict in data["quantities"]:
                self.results.append(QuantityResult(**qty_dict))

    def generate_summary(self) -> str:
        """Generate summary report."""
        lines = [
            "=" * 60,
            "CONSTRUCTION QUANTITY SUMMARY",
            "=" * 60,
            f"Total Elements: {len(self.results)}",
            f"Total Discrepancies: {len(self.discrepancy_tracker.records)}",
            "",
            "DIVISIONS:",
        ]

        divisions = self.aggregate_calc.aggregate_by_division(self.results)
        for div_code, div_data in sorted(divisions.items()):
            if div_data.get("items"):
                lines.append(f"\n{div_code}: {div_data.get('name', 'Unknown')}")
                for key, value in div_data["items"].items():
                    lines.append(f"  {key}: {value}")

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)


def main():
    """CLI interface."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Multi-source construction quantity calculator"
    )
    parser.add_argument("--xref", help="Path to xref.json from sheet_xref.py")
    parser.add_argument("--dxf", help="Path to DXF extraction JSON")
    parser.add_argument("--visual", help="Path to visual extraction JSON")
    parser.add_argument("--takeoff", help="Path to takeoff JSON")
    parser.add_argument("--text", help="Path to text extraction JSON")
    parser.add_argument("--output", help="Output quantities JSON file")
    parser.add_argument("--summary", action="store_true", help="Print summary")
    parser.add_argument("--element", help="Calculate single element")
    parser.add_argument("--discrepancies-only", action="store_true",
                        help="Only show discrepancies")

    args = parser.parse_args()

    bridge = CalcBridge()
    bridge.load_extraction_data(args.dxf, args.visual, args.takeoff, args.text)

    if args.xref:
        bridge.load_assembly_chains(args.xref)

    if args.element:
        result = bridge.calculate_element(args.element)
        if result:
            print(json.dumps(asdict(result), indent=2))
    else:
        bridge.calculate_all()

        if args.summary:
            print(bridge.generate_summary())

        if args.discrepancies_only:
            report = bridge.discrepancy_tracker.generate_report()
            print(json.dumps(report, indent=2))
        elif args.output:
            output = bridge.to_config_json()
            with open(args.output, "w") as f:
                json.dump(output, f, indent=2)
            print(f"Output written to {args.output}")


if __name__ == "__main__":
    main()
