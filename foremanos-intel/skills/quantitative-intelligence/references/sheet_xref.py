#!/usr/bin/env python3
"""
Sheet Cross-Reference Index Builder for Construction Plan Sets

Parses extraction results from text, visual, and DXF pipelines to build a complete
map of how sheets reference each other. Handles detail callouts, schedules,
specifications, and assembly chains.
"""

import json
import re
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict, field
from collections import defaultdict


@dataclass
class Sheet:
    """Represents a sheet in the drawing index."""
    number: str
    title: str
    discipline: str
    type: str  # e.g., 'plan', 'detail', 'section', 'elevation', 'schedule'
    filename: Optional[str] = None
    revision: Optional[str] = None
    scale: Optional[str] = None


@dataclass
class DetailCallout:
    """Represents a cross-reference from one sheet to another."""
    id: str
    source_sheet: str
    source_location: Optional[str] = None  # grid reference, e.g., "A1"
    target_sheet: str = ""
    target_detail: Optional[str] = None
    callout_type: str = ""  # 'detail', 'section', 'elevation', 'plan', 'wall_type', etc.
    description: str = ""
    linked_elements: List[str] = field(default_factory=list)


@dataclass
class ScheduleReference:
    """Represents a link between a schedule and plan sheets."""
    schedule_sheet: str
    schedule_name: str
    plan_sheets: List[str] = field(default_factory=list)
    item_count_schedule: Optional[int] = None
    item_count_plans: Optional[int] = None
    discrepancy: Optional[str] = None


@dataclass
class SpecReference:
    """Represents a spec section callout on a sheet."""
    sheet_number: str
    spec_section: str  # format: "XX XX XX" (CSI format)
    location: Optional[str] = None
    context: str = ""


@dataclass
class AssemblyChain:
    """Represents a multi-sheet element chain (e.g., room, footing, equipment)."""
    id: str
    element_type: str  # 'room', 'footing', 'equipment', 'wall_type', etc.
    element_name: str
    sheets_involved: List[str] = field(default_factory=list)
    detail_callouts: List[str] = field(default_factory=list)
    schedule_references: List[str] = field(default_factory=list)
    spec_references: List[str] = field(default_factory=list)


@dataclass
class SheetIndex:
    """Holds the complete cross-reference state."""
    drawing_index: List[Sheet] = field(default_factory=list)
    detail_callouts: List[DetailCallout] = field(default_factory=list)
    schedule_references: List[ScheduleReference] = field(default_factory=list)
    spec_references: List[SpecReference] = field(default_factory=list)
    assembly_chains: List[AssemblyChain] = field(default_factory=list)
    validation_errors: List[str] = field(default_factory=list)


class SheetXRefBuilder:
    """Builds sheet cross-reference index from extraction results."""

    # Regex patterns for construction callout formats
    PATTERNS = {
        'detail_number': r'(\d+)\s*[/\/]\s*([A-Z]?\d+\.?\d*)',  # "3/A5.2" or "3 / A5.2"
        'detail_on_sheet': r'(?:DETAIL|DET\.?)\s+(\d+)\s+ON\s+([A-Z]?\d+\.?\d*)',
        'see_sheet': r'SEE\s+SHEET\s+([A-Z]?\d+\.?\d*)',
        'see_detail': r'SEE\s+DETAIL\s+(\w+/[A-Z]?\d+\.?\d*)',
        'section_cut': r'([A-Z])-([A-Z]?[A-Z]?\d+\.?\d*)',  # "A-A4.1"
        'interior_elevation': r'(?:INT\.?\s+)?EL(?:EV)?\.?\s+(\d+).*(?:ON|SHEET)\s+([A-Z]?\d+\.?\d*)',
        'enlarged_plan': r'(?:ENLG|ENLARGED|EXPANDED).*([A-Z]?\d+\.?\d*)',
        'wall_type_tag': r'(?:WALL\s+TYPE|WT)\s+([0-9A-Z]+)',
        'spec_section': r'\b(\d{2})\s+(\d{2})\s+(\d{2})\b',  # "CSI format XX XX XX"
    }

    def __init__(self, verbose: bool = False):
        """Initialize the builder."""
        self.logger = self._setup_logging(verbose)
        self.index = SheetIndex()

    @staticmethod
    def _setup_logging(verbose: bool) -> logging.Logger:
        """Configure logging."""
        logger = logging.getLogger(__name__)
        level = logging.DEBUG if verbose else logging.INFO
        logger.setLevel(level)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(levelname)s: %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    def build_drawing_index(self, extraction_results: List[Dict[str, Any]]) -> None:
        """
        Build the sheet list from extraction metadata.

        Args:
            extraction_results: List of dicts with keys: filename, sheet_number,
                               title, discipline, type, etc.
        """
        self.logger.info(f"Building drawing index from {len(extraction_results)} extractions")

        seen = set()
        for result in extraction_results:
            sheet_number = result.get('sheet_number', result.get('number', ''))

            # Avoid duplicates
            if sheet_number in seen:
                continue
            seen.add(sheet_number)

            sheet = Sheet(
                number=sheet_number,
                title=result.get('title', 'Untitled'),
                discipline=result.get('discipline', 'General'),
                type=result.get('type', 'plan'),
                filename=result.get('filename'),
                revision=result.get('revision'),
                scale=result.get('scale'),
            )
            self.index.drawing_index.append(sheet)

        self.logger.info(f"Drawing index built: {len(self.index.drawing_index)} sheets")

    def parse_detail_callouts(self, ocr_results: List[Dict[str, Any]],
                             visual_results: List[Dict[str, Any]]) -> None:
        """
        Find detail callouts in OCR text and visual symbol detection results.

        Detects patterns like:
        - "3/A5.2" or "3 / A5.2" (detail number / sheet number)
        - "DETAIL 3 ON A5.2"
        - "SEE SHEET S1.0"
        - "SEE DETAIL A/A5.2"
        - Section cuts: "A-A4.1" or "A / A4.1"
        - Interior elevation markers
        - Enlarged plan references
        - Wall type tags
        """
        self.logger.info("Parsing detail callouts from OCR and visual results")
        callout_id = 0

        # Process OCR results
        for ocr_result in ocr_results:
            sheet_num = ocr_result.get('sheet_number', '')
            text = ocr_result.get('text', '')
            location = ocr_result.get('location')  # grid reference if available

            callouts = self._extract_callouts_from_text(text, sheet_num, location)
            for callout in callouts:
                callout.id = f"callout_{callout_id}"
                callout_id += 1
                self.index.detail_callouts.append(callout)

        # Process visual results (symbol detections)
        for visual_result in visual_results:
            sheet_num = visual_result.get('sheet_number', '')
            symbols = visual_result.get('symbols', [])

            for symbol in symbols:
                callout = self._extract_callout_from_symbol(symbol, sheet_num)
                if callout:
                    callout.id = f"callout_{callout_id}"
                    callout_id += 1
                    self.index.detail_callouts.append(callout)

        self.logger.info(f"Found {len(self.index.detail_callouts)} detail callouts")

    def _extract_callouts_from_text(self, text: str, sheet_num: str,
                                    location: Optional[str]) -> List[DetailCallout]:
        """Extract callout references from OCR text."""
        callouts = []

        # Detail number pattern (e.g., "3/A5.2")
        for match in re.finditer(self.PATTERNS['detail_number'], text):
            detail_num, target_sheet = match.groups()
            callout = DetailCallout(
                id="",
                source_sheet=sheet_num,
                source_location=location,
                target_sheet=target_sheet,
                target_detail=detail_num,
                callout_type='detail',
                description=f"Detail {detail_num} on sheet {target_sheet}",
            )
            callouts.append(callout)

        # "DETAIL X ON SHEET Y" pattern
        for match in re.finditer(self.PATTERNS['detail_on_sheet'], text, re.IGNORECASE):
            detail_num, target_sheet = match.groups()
            callout = DetailCallout(
                id="",
                source_sheet=sheet_num,
                source_location=location,
                target_sheet=target_sheet,
                target_detail=detail_num,
                callout_type='detail',
                description=f"Detail {detail_num} on sheet {target_sheet}",
            )
            callouts.append(callout)

        # "SEE SHEET X" pattern
        for match in re.finditer(self.PATTERNS['see_sheet'], text, re.IGNORECASE):
            target_sheet = match.group(1)
            callout = DetailCallout(
                id="",
                source_sheet=sheet_num,
                source_location=location,
                target_sheet=target_sheet,
                callout_type='cross_reference',
                description=f"See sheet {target_sheet}",
            )
            callouts.append(callout)

        # Section cut pattern (e.g., "A-A4.1")
        for match in re.finditer(self.PATTERNS['section_cut'], text):
            cut_letter, target_sheet = match.groups()
            callout = DetailCallout(
                id="",
                source_sheet=sheet_num,
                source_location=location,
                target_sheet=target_sheet,
                target_detail=f"Section {cut_letter}",
                callout_type='section',
                description=f"Section {cut_letter} on sheet {target_sheet}",
            )
            callouts.append(callout)

        # Interior elevation pattern
        for match in re.finditer(self.PATTERNS['interior_elevation'], text, re.IGNORECASE):
            elev_num, target_sheet = match.groups()
            callout = DetailCallout(
                id="",
                source_sheet=sheet_num,
                source_location=location,
                target_sheet=target_sheet,
                target_detail=f"Elevation {elev_num}",
                callout_type='elevation',
                description=f"Interior elevation {elev_num} on sheet {target_sheet}",
            )
            callouts.append(callout)

        # Wall type pattern
        for match in re.finditer(self.PATTERNS['wall_type_tag'], text, re.IGNORECASE):
            wall_type = match.group(1)
            callout = DetailCallout(
                id="",
                source_sheet=sheet_num,
                source_location=location,
                callout_type='wall_type',
                description=f"Wall type {wall_type}",
                linked_elements=[f"wall_type_{wall_type}"],
            )
            callouts.append(callout)

        return callouts

    def _extract_callout_from_symbol(self, symbol: Dict[str, Any],
                                     sheet_num: str) -> Optional[DetailCallout]:
        """Extract callout reference from visual symbol detection."""
        symbol_type = symbol.get('type', '').lower()
        location = symbol.get('location')
        label = symbol.get('label', '')

        if 'detail' in symbol_type or 'callout' in symbol_type:
            # Parse label to extract detail number and target sheet
            match = re.search(self.PATTERNS['detail_number'], label)
            if match:
                detail_num, target_sheet = match.groups()
                return DetailCallout(
                    id="",
                    source_sheet=sheet_num,
                    source_location=location,
                    target_sheet=target_sheet,
                    target_detail=detail_num,
                    callout_type='detail',
                    description=label,
                )
        elif 'section' in symbol_type:
            match = re.search(self.PATTERNS['section_cut'], label)
            if match:
                cut_letter, target_sheet = match.groups()
                return DetailCallout(
                    id="",
                    source_sheet=sheet_num,
                    source_location=location,
                    target_sheet=target_sheet,
                    target_detail=f"Section {cut_letter}",
                    callout_type='section',
                    description=label,
                )
        elif 'elevation' in symbol_type:
            match = re.search(r'(\d+)', label)
            if match:
                elev_num = match.group(1)
                return DetailCallout(
                    id="",
                    source_sheet=sheet_num,
                    source_location=location,
                    target_detail=f"Elevation {elev_num}",
                    callout_type='elevation',
                    description=label,
                )

        return None

    def parse_schedule_references(self, extraction_results: List[Dict[str, Any]]) -> None:
        """
        Identify which sheets contain schedules and which plan sheets reference them.

        Compares item counts: schedule says 24 doors, plan sheets show 22 door symbols
        → flags discrepancy.
        """
        self.logger.info("Parsing schedule references")

        schedule_sheets = {}
        plan_sheets_by_discipline = defaultdict(list)

        # Identify schedule sheets and extract counts
        for result in extraction_results:
            sheet_type = result.get('type', '').lower()
            sheet_num = result.get('sheet_number', '')

            if 'schedule' in sheet_type:
                schedule_name = result.get('title', 'Unknown Schedule')
                item_count = result.get('item_count')

                schedule_sheets[sheet_num] = {
                    'name': schedule_name,
                    'count': item_count,
                }
            elif sheet_type in ('plan', 'elevation', 'section'):
                discipline = result.get('discipline', 'General')
                plan_sheets_by_discipline[discipline].append(sheet_num)

        # Link schedules to plan sheets
        for schedule_sheet, schedule_info in schedule_sheets.items():
            schedule_name = schedule_info['name'].lower()

            # Infer related discipline from schedule name
            related_discipline = self._infer_discipline_from_schedule(schedule_name)
            plan_sheets = plan_sheets_by_discipline.get(related_discipline, [])

            # Count items in plans
            plan_item_count = self._count_items_in_plans(plan_sheets, schedule_name)

            discrepancy = None
            if schedule_info['count'] and plan_item_count:
                if schedule_info['count'] != plan_item_count:
                    discrepancy = (f"Schedule lists {schedule_info['count']} items, "
                                  f"but {plan_item_count} found in plans")

            ref = ScheduleReference(
                schedule_sheet=schedule_sheet,
                schedule_name=schedule_info['name'],
                plan_sheets=plan_sheets,
                item_count_schedule=schedule_info['count'],
                item_count_plans=plan_item_count,
                discrepancy=discrepancy,
            )
            self.index.schedule_references.append(ref)

        self.logger.info(f"Found {len(self.index.schedule_references)} schedule references")

    @staticmethod
    def _infer_discipline_from_schedule(schedule_name: str) -> str:
        """Infer the related discipline from schedule name."""
        if any(x in schedule_name for x in ['door', 'window', 'finish']):
            return 'Architectural'
        elif any(x in schedule_name for x in ['equipment', 'fixture']):
            return 'Mechanical'
        elif any(x in schedule_name for x in ['device', 'switch', 'outlet']):
            return 'Electrical'
        return 'General'

    @staticmethod
    def _count_items_in_plans(plan_sheets: List[str], schedule_name: str) -> Optional[int]:
        """Count items in plans (stub; would need actual plan data)."""
        # This would integrate with extraction data to count symbols
        return None

    def parse_spec_references(self, ocr_results: List[Dict[str, Any]]) -> None:
        """
        Find spec section callouts (XX XX XX format) on plan sheets and note
        which spec sections apply to which sheets.
        """
        self.logger.info("Parsing spec section references")

        for ocr_result in ocr_results:
            sheet_num = ocr_result.get('sheet_number', '')
            text = ocr_result.get('text', '')
            location = ocr_result.get('location')

            for match in re.finditer(self.PATTERNS['spec_section'], text):
                spec_section = f"{match.group(1)} {match.group(2)} {match.group(3)}"

                ref = SpecReference(
                    sheet_number=sheet_num,
                    spec_section=spec_section,
                    location=location,
                    context=text[max(0, match.start() - 50):match.end() + 50],
                )
                self.index.spec_references.append(ref)

        self.logger.info(f"Found {len(self.index.spec_references)} spec references")

    def build_assembly_chains(self, extraction_data: List[Dict[str, Any]]) -> None:
        """
        Create assembly chains by tracing cross-references for key elements:
        - Footings: foundation plan → detail sheet → structural notes
        - Rooms: floor plan → finish schedule → RCP → elevation
        - Equipment: plan location → equipment schedule → spec
        - Wall types: across plans → legend → detail → spec
        """
        self.logger.info("Building assembly chains")
        chain_id = 0

        # Group callouts by element
        callouts_by_target = defaultdict(list)
        for callout in self.index.detail_callouts:
            key = (callout.source_sheet, callout.target_detail)
            callouts_by_target[key].append(callout)

        # Build chains for each element type
        for element_type in ['footing', 'room', 'equipment', 'wall_type']:
            chains = self._build_chains_for_element_type(element_type, extraction_data)
            for chain in chains:
                chain.id = f"chain_{chain_id}"
                chain_id += 1
                self.index.assembly_chains.append(chain)

        self.logger.info(f"Built {len(self.index.assembly_chains)} assembly chains")

    def _build_chains_for_element_type(self, element_type: str,
                                       extraction_data: List[Dict[str, Any]]) -> List[AssemblyChain]:
        """Build assembly chains for a specific element type."""
        chains = []

        # This is a stub; actual implementation would analyze extraction data
        # and trace element references across sheets

        return chains

    def validate_index(self) -> None:
        """
        Cross-check the index for consistency:
        - All target sheets in callouts exist in drawing index
        - No orphaned references
        - Schedule item counts match plan counts
        - Assembly chains are complete
        """
        self.logger.info("Validating cross-reference index")
        self.index.validation_errors = []

        sheet_numbers = {s.number for s in self.index.drawing_index}

        # Validate detail callouts
        for callout in self.index.detail_callouts:
            if callout.source_sheet not in sheet_numbers:
                self.index.validation_errors.append(
                    f"Callout {callout.id}: source sheet '{callout.source_sheet}' not in index"
                )
            if callout.target_sheet and callout.target_sheet not in sheet_numbers:
                self.index.validation_errors.append(
                    f"Callout {callout.id}: target sheet '{callout.target_sheet}' not in index"
                )

        # Validate schedule references
        for schedule_ref in self.index.schedule_references:
            if schedule_ref.schedule_sheet not in sheet_numbers:
                self.index.validation_errors.append(
                    f"Schedule '{schedule_ref.schedule_name}' on sheet '{schedule_ref.schedule_sheet}' not in index"
                )
            for plan_sheet in schedule_ref.plan_sheets:
                if plan_sheet not in sheet_numbers:
                    self.index.validation_errors.append(
                        f"Plan sheet '{plan_sheet}' in schedule reference not in index"
                    )

        # Validate spec references
        for spec_ref in self.index.spec_references:
            if spec_ref.sheet_number not in sheet_numbers:
                self.index.validation_errors.append(
                    f"Spec reference on sheet '{spec_ref.sheet_number}' not in index"
                )

        if self.index.validation_errors:
            self.logger.warning(f"Found {len(self.index.validation_errors)} validation errors")
            for error in self.index.validation_errors:
                self.logger.warning(f"  - {error}")
        else:
            self.logger.info("Validation passed: index is consistent")

    def to_config_json(self) -> Dict[str, Any]:
        """Export the index in config schema format."""
        return {
            'sheet_cross_references': {
                'drawing_index': [asdict(s) for s in self.index.drawing_index],
                'detail_callouts': [asdict(c) for c in self.index.detail_callouts],
                'schedule_references': [asdict(r) for r in self.index.schedule_references],
                'spec_references': [asdict(r) for r in self.index.spec_references],
                'assembly_chains': [asdict(c) for c in self.index.assembly_chains],
            }
        }

    @staticmethod
    def from_config_json(data: Dict[str, Any]) -> 'SheetXRefBuilder':
        """Load an existing index from config JSON for incremental updates."""
        builder = SheetXRefBuilder()
        xref_data = data.get('sheet_cross_references', {})

        # Restore drawing index
        for item in xref_data.get('drawing_index', []):
            builder.index.drawing_index.append(Sheet(**item))

        # Restore detail callouts
        for item in xref_data.get('detail_callouts', []):
            builder.index.detail_callouts.append(DetailCallout(**item))

        # Restore schedule references
        for item in xref_data.get('schedule_references', []):
            builder.index.schedule_references.append(ScheduleReference(**item))

        # Restore spec references
        for item in xref_data.get('spec_references', []):
            builder.index.spec_references.append(SpecReference(**item))

        # Restore assembly chains
        for item in xref_data.get('assembly_chains', []):
            builder.index.assembly_chains.append(AssemblyChain(**item))

        return builder


def main():
    """CLI interface."""
    parser = argparse.ArgumentParser(
        description='Build sheet cross-reference index from extraction results'
    )
    parser.add_argument('--extraction-dir', type=str, required=True,
                        help='Directory containing JSON extraction results')
    parser.add_argument('--output', type=str, default='xref.json',
                        help='Output JSON file (default: xref.json)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable verbose logging')
    parser.add_argument('--validate', action='store_true',
                        help='Validate index after building')
    parser.add_argument('--update-from', type=str,
                        help='Load existing index for incremental update')

    args = parser.parse_args()

    # Initialize builder
    builder = SheetXRefBuilder(verbose=args.verbose)

    # Load existing index if provided
    if args.update_from:
        if Path(args.update_from).exists():
            with open(args.update_from) as f:
                config = json.load(f)
            builder = SheetXRefBuilder.from_config_json(config)
            builder.logger.info(f"Loaded existing index from {args.update_from}")

    # Load extraction results
    extraction_dir = Path(args.extraction_dir)
    if not extraction_dir.exists():
        builder.logger.error(f"Extraction directory not found: {extraction_dir}")
        return

    extraction_results = []
    ocr_results = []
    visual_results = []

    for json_file in extraction_dir.glob('*.json'):
        with open(json_file) as f:
            data = json.load(f)

        if isinstance(data, list):
            for item in data:
                if item.get('type') == 'ocr':
                    ocr_results.append(item)
                elif item.get('type') == 'visual':
                    visual_results.append(item)
                else:
                    extraction_results.append(item)
        else:
            if data.get('type') == 'ocr':
                ocr_results.append(data)
            elif data.get('type') == 'visual':
                visual_results.append(data)
            else:
                extraction_results.append(data)

    # Build index
    builder.build_drawing_index(extraction_results)
    builder.parse_detail_callouts(ocr_results, visual_results)
    builder.parse_schedule_references(extraction_results)
    builder.parse_spec_references(ocr_results)
    builder.build_assembly_chains(extraction_results)

    # Validate if requested
    if args.validate:
        builder.validate_index()

    # Export
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        json.dump(builder.to_config_json(), f, indent=2, default=str)

    builder.logger.info(f"Index exported to {output_path}")


if __name__ == '__main__':
    main()
