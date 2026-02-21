#!/usr/bin/env python3
"""
Visual Plan Analyzer - Construction Plan Sheet Analysis Pipeline

A comprehensive multi-pass extraction pipeline for analyzing construction plan sheets.
Performs sheet layout detection, OCR extraction, line detection, symbol detection,
material zone identification, dimension extraction, and scale calibration.

Author: Foreman OS Document Intelligence Team
License: Proprietary
"""

import os
import sys
import json
import argparse
import re
import warnings
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import traceback

import cv2
import numpy as np
from skimage import filters, feature, img_as_float, img_as_uint
from skimage.morphology import binary_dilation, binary_erosion
from sklearn.cluster import DBSCAN
import logging

# Suppress warnings
warnings.filterwarnings('ignore')
os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

# Optional imports with graceful fallback
try:
    from paddleocr import PaddleOCR
    PADDLE_AVAILABLE = True
except ImportError:
    logger.warning("PaddleOCR not available, will use OpenCV text detection only")
    PADDLE_AVAILABLE = False

try:
    from craft_text_detector import Craft
    CRAFT_AVAILABLE = True
except ImportError:
    logger.warning("CRAFT text detector not available")
    CRAFT_AVAILABLE = False


# =============================================================================
# Data Classes and Enums
# =============================================================================

class ZoneType(Enum):
    """Zone classification enumeration."""
    TITLE_BLOCK = "title_block"
    PLAN = "plan"
    DETAIL = "detail"
    SCHEDULE = "schedule"
    NOTES = "notes"
    LEGEND = "legend"
    MARGIN = "margin"
    GENERAL = "general"


class LineType(Enum):
    """Line classification enumeration."""
    WALL = "wall"
    DIMENSION = "dimension"
    GRID = "grid"
    LEADER = "leader"
    SECTION_CUT = "section_cut"
    HATCH = "hatch"
    UNKNOWN = "unknown"


class SymbolType(Enum):
    """Symbol classification enumeration."""
    DOOR_SWING = "door_swing"
    SECTION_MARKER = "section_marker"
    ELEVATION_MARKER = "elevation_marker"
    EQUIPMENT = "equipment"
    WINDOW = "window"
    FIXTURE = "fixture"
    UNKNOWN = "unknown"


class MaterialType(Enum):
    """Material hatch pattern classification."""
    CONCRETE = "concrete"
    EARTH = "earth"
    INSULATION = "insulation"
    WOOD = "wood"
    STEEL = "steel"
    MASONRY = "masonry"
    WATER = "water"
    UNKNOWN = "unknown"


@dataclass
class TextExtraction:
    """OCR extracted text entry."""
    content: str
    bbox: Tuple[float, float, float, float]  # (x_min, y_min, x_max, y_max)
    confidence: float
    zone_type: Optional[ZoneType] = None
    text_type: Optional[str] = None  # 'room_number', 'dimension', 'elevation', etc.
    rotation: float = 0.0


@dataclass
class LineSegment:
    """Detected line segment."""
    x1: float
    y1: float
    x2: float
    y2: float
    line_type: LineType
    thickness: float
    confidence: float
    associated_text: List[str] = None

    def __post_init__(self):
        if self.associated_text is None:
            self.associated_text = []


@dataclass
class DetectedSymbol:
    """Detected symbol or marker."""
    symbol_type: SymbolType
    bbox: Tuple[float, float, float, float]
    centroid: Tuple[float, float]
    confidence: float
    label: Optional[str] = None
    properties: Dict[str, Any] = None

    def __post_init__(self):
        if self.properties is None:
            self.properties = {}


@dataclass
class MaterialZone:
    """Detected material/hatch pattern zone."""
    material_type: MaterialType
    contour: np.ndarray  # polygon vertices
    area_pixels: float
    area_real: Optional[float] = None  # in square feet
    confidence: float = 0.8
    bbox: Tuple[float, float, float, float] = None


@dataclass
class Dimension:
    """Extracted dimension with associated line."""
    value: str
    unit: str
    numeric_value: Optional[float] = None
    x1: float = 0.0
    y1: float = 0.0
    x2: float = 0.0
    y2: float = 0.0
    confidence: float = 0.8
    orientation: str = 'unknown'  # 'horizontal', 'vertical', 'angled'
    chain_id: Optional[str] = None  # Links to parent dimension chain
    chain_index: Optional[int] = None  # Position within the chain (0-based)
    witness_start: Optional[Tuple[float, float]] = None  # Witness line start point
    witness_end: Optional[Tuple[float, float]] = None  # Witness line end point
    nearest_element_start: Optional[str] = None  # Grid line, wall, etc.
    nearest_element_end: Optional[str] = None


@dataclass
class DimensionChain:
    """A chain of connected dimensions along a common axis."""
    chain_id: str
    orientation: str  # 'horizontal' or 'vertical'
    axis_y: Optional[float] = None  # Y-coordinate for horizontal chains
    axis_x: Optional[float] = None  # X-coordinate for vertical chains
    segments: List[Dimension] = None
    overall_dimension: Optional[Dimension] = None  # The total dimension spanning the chain
    segments_sum_ft: float = 0.0
    overall_ft: float = 0.0
    sum_matches_overall: bool = False
    discrepancy_ft: float = 0.0
    confidence: float = 0.8


@dataclass
class ElevationMarker:
    """Elevation marker from sections, elevations, or site plans."""
    label: str  # "T.O. WALL", "FFE", "T.O. FOOTING"
    elevation_text: str  # "12'-0\"", "856.50'"
    elevation_ft: float
    marker_type: str  # 'level', 'spot', 'grade'
    position: Tuple[float, float] = (0.0, 0.0)
    datum: Optional[str] = None  # Reference datum ("FFE = 0'-0\"")
    sheet: Optional[str] = None
    confidence: float = 0.8


@dataclass
class ZoneMapEntry:
    """Zone map entry."""
    zone_type: ZoneType
    bbox: Tuple[float, float, float, float]
    text_density: float = 0.0
    confidence: float = 0.8


@dataclass
class ScaleCalibration:
    """Scale calibration data."""
    scale_string: str  # e.g., "1/4\" = 1'-0\""
    pixels_per_foot: Optional[float] = None
    scale_factor: Optional[float] = None  # e.g., 1/48 for 1/4" = 1'-0"
    confidence: float = 0.8
    location: Optional[Tuple[float, float]] = None
    calibration_method: str = 'text'  # 'graphic_bar', 'text_scale', 'known_dimension', 'cross_sheet'
    zone_name: Optional[str] = None  # View zone this scale applies to
    zone_bbox: Optional[Tuple[float, float, float, float]] = None


# =============================================================================
# Pass 1: Sheet Layout Detection
# =============================================================================

def detect_sheet_layout(image: np.ndarray, dpi: int = 300) -> Dict[str, Any]:
    """
    Detect outer border, identify zones (title block, plan areas, details, schedules).

    Args:
        image: Input image (BGR)
        dpi: DPI value for scaling calculations

    Returns:
        Dictionary with zone map and detected regions
    """
    logger.info("Pass 1: Sheet Layout Detection")

    height, width = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    edges = cv2.dilate(edges, kernel, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find outer border (largest rectangle)
    largest_area = 0
    outer_border = None
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            area = cv2.contourArea(approx)
            if area > largest_area:
                largest_area = area
                outer_border = cv2.boundingRect(approx)

    zones = []

    # Detect title block: typically in lower-right corner
    # Title blocks have high text density
    if outer_border:
        x, y, w, h = outer_border
        # Title block is roughly 20-30% of width, 20-30% of height, bottom-right
        title_block_x = int(x + 0.7 * w)
        title_block_y = int(y + 0.7 * h)
        title_block_w = int(0.28 * w)
        title_block_h = int(0.28 * h)
        title_bbox = (title_block_x, title_block_y, title_block_x + title_block_w, title_block_y + title_block_h)

        zones.append(ZoneMapEntry(
            zone_type=ZoneType.TITLE_BLOCK,
            bbox=title_bbox,
            confidence=0.85
        ))

        # Main plan area (upper-left to middle)
        plan_bbox = (x + 10, y + 10, int(x + 0.7 * w), int(y + 0.7 * h))
        zones.append(ZoneMapEntry(
            zone_type=ZoneType.PLAN,
            bbox=plan_bbox,
            confidence=0.9
        ))

        # Detail areas (typically top-right and/or bottom-left)
        detail_bbox_tr = (int(x + 0.7 * w), y + 10, int(x + w - 10), int(y + 0.35 * h))
        zones.append(ZoneMapEntry(
            zone_type=ZoneType.DETAIL,
            bbox=detail_bbox_tr,
            confidence=0.75
        ))

        # Notes/legend areas (typically left side or top)
        notes_bbox = (x + 10, int(y + 0.35 * h), int(x + 0.25 * w), int(y + 0.7 * h))
        zones.append(ZoneMapEntry(
            zone_type=ZoneType.NOTES,
            bbox=notes_bbox,
            confidence=0.7
        ))

    return {
        "zones": [asdict(z) for z in zones],
        "outer_border": outer_border,
        "sheet_dimensions": (width, height)
    }


# =============================================================================
# Pass 2: Full OCR Extraction
# =============================================================================

def extract_text_paddle(image: np.ndarray) -> List[TextExtraction]:
    """
    Extract text using PaddleOCR with comprehensive bounding boxes and confidence.

    Args:
        image: Input image (BGR)

    Returns:
        List of TextExtraction objects
    """
    logger.info("Pass 2a: OCR Extraction (PaddleOCR)")

    if not PADDLE_AVAILABLE:
        logger.warning("PaddleOCR not available, skipping Paddle extraction")
        return []

    try:
        ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
        results = ocr.ocr(image, cls=True)

        extractions = []
        for line_idx, line in enumerate(results):
            if line is None:
                continue
            for word_result in line:
                points, (text, confidence) = word_result
                # Convert points to bounding box
                points = np.array(points, dtype=np.float32)
                x_coords = points[:, 0]
                y_coords = points[:, 1]
                bbox = (float(x_coords.min()), float(y_coords.min()),
                       float(x_coords.max()), float(y_coords.max()))

                extraction = TextExtraction(
                    content=text,
                    bbox=bbox,
                    confidence=float(confidence),
                    text_type=classify_text_type(text)
                )
                extractions.append(extraction)

        logger.info(f"Extracted {len(extractions)} text elements via PaddleOCR")
        return extractions

    except Exception as e:
        logger.error(f"PaddleOCR extraction failed: {e}")
        return []


def extract_text_opencv(image: np.ndarray) -> List[TextExtraction]:
    """
    Fallback OCR using OpenCV text detection and Tesseract if available.

    Args:
        image: Input image (BGR)

    Returns:
        List of TextExtraction objects
    """
    logger.info("Pass 2b: OCR Extraction (OpenCV Fallback)")

    extractions = []

    # Try to use CRAFT if available
    if CRAFT_AVAILABLE:
        try:
            craft = Craft(output_dir=None, crop_type="poly", cuda=False)
            prediction_result = craft.detect_text(image)

            if 'boxes' in prediction_result:
                for box_idx, box in enumerate(prediction_result['boxes']):
                    if box is not None:
                        x_coords = [p[0] for p in box]
                        y_coords = [p[1] for p in box]
                        bbox = (min(x_coords), min(y_coords), max(x_coords), max(y_coords))

                        extraction = TextExtraction(
                            content=f"text_{box_idx}",
                            bbox=bbox,
                            confidence=0.6
                        )
                        extractions.append(extraction)

            logger.info(f"Extracted {len(extractions)} text regions via CRAFT")
        except Exception as e:
            logger.warning(f"CRAFT text detection failed: {e}")

    return extractions


def classify_text_type(text: str) -> str:
    """
    Classify text type based on pattern matching.

    Args:
        text: Text string to classify

    Returns:
        Classification string
    """
    text_lower = text.lower().strip()

    # Room number: 3-4 digits
    if re.match(r'^\d{3,4}$', text):
        return 'room_number'

    # Dimension: X'-Y" or X'
    if re.search(r"\d+['\u2019]\s*-?\s*\d*\s*[\"″\u201D]?", text):
        return 'dimension'

    # Elevation: EL followed by number
    if re.match(r'^EL\.?\s*[\d\.\-\+]+', text):
        return 'elevation'

    # Spec reference: section + number (like "A2.1")
    if re.match(r'^[A-Z]+[\d\.]+', text):
        return 'spec_reference'

    # Scale notation
    if re.match(r'^[\d\.\-]*/[\d\.\-]+', text) or re.match(r'^1:[\d]+', text):
        return 'scale'

    # Grid label: single letter or number
    if re.match(r'^[A-Z]$|^[\d]$', text):
        return 'grid_label'

    return 'general_text'


def extract_title_block_text(texts: List[TextExtraction], title_zone: Tuple) -> Dict[str, str]:
    """
    Extract structured data from title block text.

    Args:
        texts: List of extracted text elements
        title_zone: Bounding box of title block

    Returns:
        Dictionary with extracted title block data
    """
    logger.info("Pass 2c: Title Block Extraction")

    title_data = {
        "project_name": None,
        "sheet_number": None,
        "sheet_title": None,
        "scale": None,
        "date": None,
        "revision": None
    }

    if title_zone is None:
        return title_data

    tx_min, ty_min, tx_max, ty_max = title_zone

    # Filter texts in title block
    title_texts = []
    for text in texts:
        bx_min, by_min, bx_max, by_max = text.bbox
        if (bx_min >= tx_min and bx_max <= tx_max and
            by_min >= ty_min and by_max <= ty_max):
            title_texts.append(text)

    # Sort by position
    title_texts.sort(key=lambda t: (t.bbox[1], t.bbox[0]))

    # Try to identify structured fields
    for idx, text in enumerate(title_texts):
        content = text.content.lower()

        if re.search(r'sheet|sheet\s*no', content):
            if idx + 1 < len(title_texts):
                title_data['sheet_number'] = title_texts[idx + 1].content
        elif re.search(r'scale', content):
            if idx + 1 < len(title_texts):
                title_data['scale'] = title_texts[idx + 1].content
        elif re.search(r'date|dated', content):
            if idx + 1 < len(title_texts):
                title_data['date'] = title_texts[idx + 1].content
        elif re.search(r'revision|rev', content):
            if idx + 1 < len(title_texts):
                title_data['revision'] = title_texts[idx + 1].content

    # First few large texts likely project name
    if title_texts:
        title_data['project_name'] = title_texts[0].content

    return title_data


def extract_all_text(image: np.ndarray, zones: List[ZoneMapEntry]) -> List[TextExtraction]:
    """
    Main OCR extraction function combining multiple methods.

    Args:
        image: Input image
        zones: Detected zones from Pass 1

    Returns:
        List of extracted text elements
    """
    logger.info("Pass 2: Full OCR Extraction")

    # Primary: PaddleOCR
    texts = extract_text_paddle(image)

    # Fallback: OpenCV methods
    if not texts:
        texts = extract_text_opencv(image)

    # Assign zone types
    for text in texts:
        for zone in zones:
            zx_min, zy_min, zx_max, zy_max = zone['bbox']
            tx_min, ty_min, tx_max, ty_max = text.bbox
            if (tx_min >= zx_min and tx_max <= zx_max and
                ty_min >= zy_min and ty_max <= zy_max):
                text.zone_type = ZoneType(zone['zone_type'])
                break

    return texts


# =============================================================================
# Pass 3: Line Detection and Classification
# =============================================================================

def detect_and_classify_lines(image: np.ndarray) -> List[LineSegment]:
    """
    Detect and classify lines: walls, dimensions, grids, leaders, section cuts.

    Args:
        image: Input image (BGR)

    Returns:
        List of LineSegment objects
    """
    logger.info("Pass 3: Line Detection and Classification")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # Adaptive thresholding for better edge detection
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)

    # Canny edge detection
    edges = cv2.Canny(threshold, 50, 150)

    # Detect lines using HoughLinesP
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=20, maxLineGap=10)

    line_segments = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            thickness = estimate_line_thickness(gray, x1, y1, x2, y2)

            # Classify line type
            line_type = classify_line(x1, y1, x2, y2, length, thickness, width, height)

            segment = LineSegment(
                x1=float(x1),
                y1=float(y1),
                x2=float(x2),
                y2=float(y2),
                line_type=line_type,
                thickness=float(thickness),
                confidence=0.8
            )
            line_segments.append(segment)

    logger.info(f"Detected and classified {len(line_segments)} line segments")
    return line_segments


def estimate_line_thickness(gray: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Estimate thickness of a line segment.

    Args:
        gray: Grayscale image
        x1, y1, x2, y2: Line endpoints

    Returns:
        Estimated thickness in pixels
    """
    # Simple approach: sample perpendicular to line
    dx = x2 - x1
    dy = y2 - y1
    length = np.sqrt(dx ** 2 + dy ** 2)

    if length < 1:
        return 1.0

    # Perpendicular direction
    px = -dy / length
    py = dx / length

    # Count pixels along perpendicular
    thickness = 1.0
    for offset in range(1, 10):
        x_sample = int(x1 + px * offset)
        y_sample = int(y1 + py * offset)

        if 0 <= x_sample < gray.shape[1] and 0 <= y_sample < gray.shape[0]:
            if gray[y_sample, x_sample] > 128:
                thickness += 1.0
            else:
                break

    return thickness


def classify_line(x1: float, y1: float, x2: float, y2: float, length: float,
                  thickness: float, width: int, height: int) -> LineType:
    """
    Classify a detected line based on characteristics.

    Args:
        x1, y1, x2, y2: Line endpoints
        length: Line length
        thickness: Line thickness
        width, height: Image dimensions

    Returns:
        LineType classification
    """
    # Thick lines (>2px) are likely walls
    if thickness > 2.0:
        return LineType.WALL

    # Long spanning lines (>50% of dimension) are likely grid lines
    max_span = max(width, height)
    if length > max_span * 0.5:
        return LineType.GRID

    # Angled lines are likely leaders
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx > 0 and dy > 0:
        angle = abs(dy / (dx + 1e-6))
        if 0.3 < angle < 3.0:
            return LineType.LEADER

    # Thin lines with moderate length are dimension lines
    if thickness <= 1.0 and 20 < length < 500:
        return LineType.DIMENSION

    # Check for dashed pattern (section cuts)
    # This is a simplified check
    if thickness > 1.5:
        return LineType.SECTION_CUT

    return LineType.UNKNOWN


# =============================================================================
# Pass 4: Symbol Detection
# =============================================================================

def detect_symbols(image: np.ndarray, texts: List[TextExtraction]) -> List[DetectedSymbol]:
    """
    Detect and classify symbols: doors, sections, elevations, equipment, windows.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements (for association)

    Returns:
        List of DetectedSymbol objects
    """
    logger.info("Pass 4: Symbol Detection")

    symbols = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # Detect circles (section markers, elevation markers)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=5, maxRadius=50)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            x, y, r = circle
            bbox = (float(x - r), float(y - r), float(x + r), float(y + r))
            label = find_nearest_text(texts, (float(x), float(y)))

            symbol = DetectedSymbol(
                symbol_type=SymbolType.SECTION_MARKER,
                bbox=bbox,
                centroid=(float(x), float(y)),
                confidence=0.75,
                label=label
            )
            symbols.append(symbol)

    # Detect rectangular equipment/fixtures
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # Rectangle
            x, y, w, h = cv2.boundingRect(approx)
            area = w * h

            # Filter by size: equipment/fixtures typically 20-500 px²
            if 20 < area < 500:
                bbox = (float(x), float(y), float(x + w), float(y + h))
                label = find_nearest_text(texts, (float(x + w / 2), float(y + h / 2)))

                symbol = DetectedSymbol(
                    symbol_type=SymbolType.EQUIPMENT,
                    bbox=bbox,
                    centroid=(float(x + w / 2), float(y + h / 2)),
                    confidence=0.7,
                    label=label
                )
                symbols.append(symbol)

    logger.info(f"Detected {len(symbols)} symbols")
    return symbols


def find_nearest_text(texts: List[TextExtraction], point: Tuple[float, float],
                      max_distance: float = 100.0) -> Optional[str]:
    """
    Find text nearest to a given point.

    Args:
        texts: List of text extractions
        point: (x, y) point
        max_distance: Maximum distance to consider

    Returns:
        Nearest text content or None
    """
    nearest = None
    min_dist = max_distance

    for text in texts:
        tx_min, ty_min, tx_max, ty_max = text.bbox
        text_center = ((tx_min + tx_max) / 2, (ty_min + ty_max) / 2)
        dist = np.sqrt((text_center[0] - point[0]) ** 2 + (text_center[1] - point[1]) ** 2)

        if dist < min_dist:
            min_dist = dist
            nearest = text.content

    return nearest


# =============================================================================
# Pass 5: Material Zone / Hatch Pattern Detection
# =============================================================================

def detect_material_zones(image: np.ndarray) -> List[MaterialZone]:
    """
    Detect and classify material zones based on texture patterns.

    Args:
        image: Input image (BGR)

    Returns:
        List of MaterialZone objects
    """
    logger.info("Pass 5: Material Zone Detection")

    zones = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_float = img_as_float(gray)

    height, width = gray.shape

    # Use Gabor filter banks to detect patterns
    gabor_responses = []
    for frequency in [0.05, 0.1, 0.15]:
        for angle in [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]:
            try:
                real, imag = filters.gabor(gray_float, frequency=frequency, theta=angle)
                response = np.sqrt(real ** 2 + imag ** 2)
                gabor_responses.append(response)
            except Exception as e:
                logger.debug(f"Gabor filter error: {e}")
                continue

    if not gabor_responses:
        logger.warning("No Gabor responses generated")
        return zones

    # Combine responses
    combined_response = np.mean(gabor_responses, axis=0)

    # Threshold to get pattern regions
    threshold = cv2.adaptiveThreshold((combined_response * 255).astype(np.uint8),
                                      255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 15, 2)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area_pixels = cv2.contourArea(contour)

        # Filter by area (avoid noise)
        if area_pixels < 100:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        bbox = (float(x), float(y), float(x + w), float(y + h))

        # Classify material type based on texture response
        material_type = classify_material_pattern(contour, gray, gabor_responses)

        zone = MaterialZone(
            material_type=material_type,
            contour=contour,
            area_pixels=float(area_pixels),
            bbox=bbox,
            confidence=0.7
        )
        zones.append(zone)

    logger.info(f"Detected {len(zones)} material zones")
    return zones


def classify_material_pattern(contour: np.ndarray, gray: np.ndarray,
                              gabor_responses: List[np.ndarray]) -> MaterialType:
    """
    Classify material pattern based on texture analysis.

    Args:
        contour: Contour region
        gray: Grayscale image
        gabor_responses: Gabor filter responses

    Returns:
        MaterialType classification
    """
    # Create mask for contour
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)

    # Calculate LBP (Local Binary Pattern) within region
    try:
        gray_float = img_as_float(gray)
        lbp = feature.local_binary_pattern(gray_float, P=8, R=1, method='uniform')
        lbp_hist, _ = np.histogram(lbp[mask > 0], bins=256, range=(0, 256))
        entropy = -np.sum(lbp_hist / (lbp_hist.sum() + 1e-6) *
                         np.log(lbp_hist / (lbp_hist.sum() + 1e-6) + 1e-6))
    except Exception:
        entropy = 0.5

    # Simple heuristic classification
    if entropy < 0.3:
        return MaterialType.EARTH
    elif entropy < 0.6:
        return MaterialType.CONCRETE
    elif entropy < 1.0:
        return MaterialType.INSULATION
    else:
        return MaterialType.WOOD

    return MaterialType.UNKNOWN


# =============================================================================
# Pass 6: Dimension Extraction (Enhanced — Chaining + Elevation Markers)
# =============================================================================

def extract_dimensions(texts: List[TextExtraction],
                       lines: List[LineSegment],
                       scale_ppf: Optional[float] = None) -> Dict[str, Any]:
    """
    Extract dimensions by pairing dimension text with dimension lines,
    then group into chains and verify sums.

    Also extracts elevation markers and spot elevations.

    Args:
        texts: Extracted text elements
        lines: Detected line segments
        scale_ppf: Pixels per foot from Pass 7 (for measurement verification)

    Returns:
        Dict with keys: dimensions (list), chains (list), elevation_markers (list),
        spot_elevations (list), isolated (list)
    """
    logger.info("Pass 6: Dimension Extraction (Enhanced)")

    result = {
        'dimensions': [],
        'chains': [],
        'elevation_markers': [],
        'spot_elevations': [],
        'isolated': []
    }

    dimension_regex = r"(\d+)['\u2019]\s*-?\s*(\d+)\s*[\"″\u201D]?|(\d+)['\u2019](?!\s*-)|(\d+)\s*[\"″\u201D]"

    # ---- Step 1: Extract all individual dimensions ----
    dimension_texts = [t for t in texts if t.text_type == 'dimension']
    all_dims = []

    for dim_text in dimension_texts:
        match = re.search(dimension_regex, dim_text.content)
        if match:
            if match.group(1) and match.group(2):
                feet = int(match.group(1))
                inches = int(match.group(2))
                numeric_value = feet + inches / 12.0
                unit = "ft-in"
            elif match.group(3):
                numeric_value = float(match.group(3))
                unit = "ft"
            elif match.group(4):
                numeric_value = float(match.group(4))
                unit = "in"
            else:
                continue

            nearest_line = find_nearest_line(dim_text, lines, max_distance=100)

            if nearest_line:
                # Determine orientation
                dx = abs(nearest_line.x2 - nearest_line.x1)
                dy = abs(nearest_line.y2 - nearest_line.y1)
                if dx > dy * 3:
                    orientation = 'horizontal'
                elif dy > dx * 3:
                    orientation = 'vertical'
                else:
                    orientation = 'angled'

                dimension = Dimension(
                    value=dim_text.content,
                    unit=unit,
                    numeric_value=numeric_value,
                    x1=nearest_line.x1,
                    y1=nearest_line.y1,
                    x2=nearest_line.x2,
                    y2=nearest_line.y2,
                    confidence=dim_text.confidence,
                    orientation=orientation
                )
                all_dims.append(dimension)

    result['dimensions'] = all_dims
    logger.info(f"Extracted {len(all_dims)} individual dimensions")

    # ---- Step 2: Group dimensions into chains ----
    chains = build_dimension_chains(all_dims)
    result['chains'] = chains
    logger.info(f"Built {len(chains)} dimension chains")

    # ---- Step 3: Identify isolated dimensions (not in any chain) ----
    chained_ids = set()
    for chain in chains:
        if chain.segments:
            for seg in chain.segments:
                chained_ids.add(id(seg))
    isolated = [d for d in all_dims if id(d) not in chained_ids]
    result['isolated'] = isolated

    # ---- Step 4: Extract elevation markers ----
    elev_markers = extract_elevation_markers(texts)
    result['elevation_markers'] = elev_markers
    logger.info(f"Extracted {len(elev_markers)} elevation markers")

    # ---- Step 5: Extract spot elevations ----
    spot_elevs = extract_spot_elevations(texts)
    result['spot_elevations'] = spot_elevs
    logger.info(f"Extracted {len(spot_elevs)} spot elevations")

    return result


def build_dimension_chains(dimensions: List[Dimension],
                           alignment_tolerance: float = 15.0,
                           gap_tolerance: float = 30.0) -> List[DimensionChain]:
    """
    Group dimensions into chains — sequences of dimensions that share a common
    axis line (same Y for horizontal, same X for vertical).

    A chain is a set of sub-dimensions along one line, often with an overall
    dimension spanning all of them. The sub-dimensions should sum to the overall.

    Args:
        dimensions: All extracted dimensions
        alignment_tolerance: Max pixels between dimension line centers to be "same axis"
        gap_tolerance: Max pixel gap between end of one segment and start of the next

    Returns:
        List of DimensionChain objects with sum verification
    """
    chains = []
    chain_counter = 0

    # Separate by orientation
    h_dims = [d for d in dimensions if d.orientation == 'horizontal']
    v_dims = [d for d in dimensions if d.orientation == 'vertical']

    for orientation, dim_group in [('horizontal', h_dims), ('vertical', v_dims)]:
        if not dim_group:
            continue

        # Sort by axis position (Y for horizontal chains, X for vertical)
        if orientation == 'horizontal':
            dim_group.sort(key=lambda d: (d.y1 + d.y2) / 2)
        else:
            dim_group.sort(key=lambda d: (d.x1 + d.x2) / 2)

        # Cluster by axis position
        clusters = []
        current_cluster = [dim_group[0]]

        for i in range(1, len(dim_group)):
            prev = current_cluster[-1]
            curr = dim_group[i]

            if orientation == 'horizontal':
                prev_axis = (prev.y1 + prev.y2) / 2
                curr_axis = (curr.y1 + curr.y2) / 2
            else:
                prev_axis = (prev.x1 + prev.x2) / 2
                curr_axis = (curr.x1 + curr.x2) / 2

            if abs(curr_axis - prev_axis) <= alignment_tolerance:
                current_cluster.append(curr)
            else:
                clusters.append(current_cluster)
                current_cluster = [curr]

        clusters.append(current_cluster)

        # For each cluster, sort by position along the axis and try to form chains
        for cluster in clusters:
            if len(cluster) < 2:
                continue  # Need at least 2 to form a chain

            # Sort by start position
            if orientation == 'horizontal':
                cluster.sort(key=lambda d: min(d.x1, d.x2))
                axis_val = np.mean([(d.y1 + d.y2) / 2 for d in cluster])
            else:
                cluster.sort(key=lambda d: min(d.y1, d.y2))
                axis_val = np.mean([(d.x1 + d.x2) / 2 for d in cluster])

            # Find the longest dimension (potential overall)
            longest = max(cluster, key=lambda d: d.numeric_value if d.numeric_value else 0)
            segments = [d for d in cluster if d is not longest]

            if not segments:
                continue

            # Build chain
            chain_counter += 1
            chain_id = f"DIM-CHAIN-{chain_counter:03d}"

            # Tag segments with chain info
            for idx, seg in enumerate(segments):
                seg.chain_id = chain_id
                seg.chain_index = idx

            # Sum verification
            seg_sum = sum(s.numeric_value for s in segments if s.numeric_value)
            overall_val = longest.numeric_value if longest.numeric_value else 0
            discrepancy = abs(seg_sum - overall_val)
            sum_matches = discrepancy < 0.1  # Within ~1 inch

            chain = DimensionChain(
                chain_id=chain_id,
                orientation=orientation,
                axis_y=axis_val if orientation == 'horizontal' else None,
                axis_x=axis_val if orientation == 'vertical' else None,
                segments=segments,
                overall_dimension=longest,
                segments_sum_ft=round(seg_sum, 4),
                overall_ft=round(overall_val, 4),
                sum_matches_overall=sum_matches,
                discrepancy_ft=round(discrepancy, 4),
                confidence=0.85 if sum_matches else 0.60
            )
            chains.append(chain)

            if not sum_matches and overall_val > 0:
                logger.warning(
                    f"Chain {chain_id}: segments sum {seg_sum:.2f}' ≠ "
                    f"overall {overall_val:.2f}' (Δ {discrepancy:.2f}')"
                )

    return chains


def extract_elevation_markers(texts: List[TextExtraction]) -> List[ElevationMarker]:
    """
    Extract elevation markers from text.
    Looks for patterns like: EL. 856'-6", T.O. WALL 12'-0", FFE 856.50, +4'-0", etc.
    """
    markers = []

    # Pattern 1: EL. or ELEV. prefix
    elev_regex = r"(?:EL\.?|ELEV\.?)\s*(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?"
    # Pattern 2: Named elevations (T.O. WALL, FFE, T.O. FOOTING, B.O. SLAB, etc.)
    named_regex = r"(T\.?O\.?\s*(?:WALL|STL|SLAB|FTG|PARAPET|ROOF|DECK|CURB)|FFE|FG|B\.?O\.?\s*(?:SLAB|STL|FTG|DECK)|TOP\s*OF\s*\w+|FINISH\s*FLOOR)\s*(?:=\s*)?(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?"
    # Pattern 3: Decimal elevations (856.50, 857.25 — common on civil/site plans)
    decimal_regex = r"(?:EL\.?\s*|ELEV\.?\s*|FFE\s*)?(\d{3,4}\.\d{1,2})['\u2019]?"
    # Pattern 4: Relative elevations (+4'-0", -2'-6")
    relative_regex = r"([+-])(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?"

    for text in texts:
        content = text.content.strip()
        tx, ty = (text.bbox[0] + text.bbox[2]) / 2, (text.bbox[1] + text.bbox[3]) / 2

        # Try named elevations first (most specific)
        match = re.search(named_regex, content, re.IGNORECASE)
        if match:
            label = match.group(1).upper().strip()
            feet = float(match.group(2))
            inches = float(match.group(3)) if match.group(3) else 0
            elev_ft = feet + inches / 12.0
            markers.append(ElevationMarker(
                label=label,
                elevation_text=f"{int(feet)}'-{int(inches)}\"",
                elevation_ft=elev_ft,
                marker_type='level',
                position=(tx, ty),
                confidence=0.85
            ))
            continue

        # Try EL. prefix
        match = re.search(elev_regex, content, re.IGNORECASE)
        if match:
            feet = float(match.group(1))
            inches = float(match.group(2)) if match.group(2) else 0
            elev_ft = feet + inches / 12.0
            markers.append(ElevationMarker(
                label="EL.",
                elevation_text=content,
                elevation_ft=elev_ft,
                marker_type='level',
                position=(tx, ty),
                confidence=0.80
            ))
            continue

        # Try decimal elevations (site plans)
        match = re.search(decimal_regex, content, re.IGNORECASE)
        if match:
            elev_ft = float(match.group(1))
            # Decimal elevations > 100 are likely site elevations (MSL)
            if elev_ft > 100:
                markers.append(ElevationMarker(
                    label="SPOT ELEV",
                    elevation_text=content,
                    elevation_ft=elev_ft,
                    marker_type='spot',
                    position=(tx, ty),
                    confidence=0.75
                ))
            continue

        # Try relative elevations
        match = re.search(relative_regex, content)
        if match:
            sign = 1 if match.group(1) == '+' else -1
            feet = float(match.group(2))
            inches = float(match.group(3)) if match.group(3) else 0
            elev_ft = sign * (feet + inches / 12.0)
            markers.append(ElevationMarker(
                label="RELATIVE",
                elevation_text=content,
                elevation_ft=elev_ft,
                marker_type='level',
                position=(tx, ty),
                datum="FFE = 0'-0\"",
                confidence=0.75
            ))

    return markers


def extract_spot_elevations(texts: List[TextExtraction]) -> List[Dict]:
    """
    Extract spot elevations commonly found on civil/site plans.
    These are typically standalone decimal numbers (e.g., 856.50) with
    an 'x' marker or arrow symbol nearby.

    Returns list of dicts matching the site_grading.spot_elevations schema.
    """
    spots = []

    for text in texts:
        content = text.content.strip()
        tx, ty = (text.bbox[0] + text.bbox[2]) / 2, (text.bbox[1] + text.bbox[3]) / 2

        # Spot elevations are typically 3-4 digit numbers with 1-2 decimal places
        # and may be prefixed with 'x' or have special markers
        match = re.match(r"^[xX×]?\s*(\d{3,4}\.\d{1,2})['\u2019]?\s*$", content)
        if match:
            elev_ft = float(match.group(1))
            # Heuristic: values between 100 and 2000 are likely site elevations
            if 100 < elev_ft < 2000:
                # Determine type from context
                spot_type = 'proposed'  # Default; would need visual context to distinguish
                label = content.strip()

                # Check for FFE indicator
                if 'FFE' in content.upper() or 'FF' in content.upper():
                    spot_type = 'ffe'
                elif 'TC' in content.upper() or 'T/C' in content.upper():
                    spot_type = 'top_of_curb'

                spots.append({
                    'elevation_ft': elev_ft,
                    'position': {'x': tx, 'y': ty},
                    'type': spot_type,
                    'label': label,
                    'confidence': 0.70
                })

    return spots


def find_nearest_line(text: TextExtraction, lines: List[LineSegment],
                      max_distance: float = 100.0) -> Optional[LineSegment]:
    """
    Find line nearest to a text element.

    Args:
        text: Text extraction
        lines: List of line segments
        max_distance: Maximum distance threshold

    Returns:
        Nearest line or None
    """
    tx_min, ty_min, tx_max, ty_max = text.bbox
    text_center = ((tx_min + tx_max) / 2, (ty_min + ty_max) / 2)

    nearest = None
    min_dist = max_distance

    for line in lines:
        if line.line_type != LineType.DIMENSION:
            continue

        # Distance from text center to line segment
        line_center = ((line.x1 + line.x2) / 2, (line.y1 + line.y2) / 2)
        dist = np.sqrt((line_center[0] - text_center[0]) ** 2 +
                      (line_center[1] - text_center[1]) ** 2)

        if dist < min_dist:
            min_dist = dist
            nearest = line

    return nearest


# =============================================================================
# Pass 7: Scale Calibration (Enhanced — Graphic Bar + Text + Multi-Zone + Stretch)
# =============================================================================

def detect_scale(image: np.ndarray, texts: List[TextExtraction],
                 title_zone: Optional[Tuple],
                 lines: Optional[List] = None,
                 zones: Optional[List[Dict]] = None,
                 dpi: int = 300) -> Dict[str, Any]:
    """
    Comprehensive scale calibration using graphic bars, text scales,
    known-dimension fallback, multi-zone mapping, and stretch detection.

    Priority: Graphic bar > Text scale > Known-dimension fallback

    Args:
        image: Input image (BGR)
        texts: Extracted text elements from Pass 2
        title_zone: Bounding box of title block from Pass 1
        lines: Detected lines from Pass 3 (optional, improves graphic bar detection)
        zones: Detected view zones from Pass 1 (optional, enables multi-zone mapping)
        dpi: Image resolution in DPI

    Returns:
        Dict with keys: scales (list), graphic_bars (list), text_scales (list),
        zones (list of zone-scale mappings), stretch_detected (bool),
        h_pixels_per_foot, v_pixels_per_foot, mean_pixels_per_foot,
        calibration_method (str), confidence (float)
    """
    logger.info("Pass 7: Scale Calibration (Enhanced)")

    result = {
        'scales': [],
        'graphic_bars': [],
        'text_scales': [],
        'zones': [],
        'stretch_detected': False,
        'h_pixels_per_foot': None,
        'v_pixels_per_foot': None,
        'mean_pixels_per_foot': None,
        'calibration_method': 'none',
        'confidence': 0.0
    }

    h, w = image.shape[:2]

    # ---- Step 1: Graphic Scale Bar Detection (Highest Priority) ----
    graphic_bars = detect_graphic_scale_bars(image, texts, title_zone, dpi)
    result['graphic_bars'] = graphic_bars

    if graphic_bars:
        best_bar = max(graphic_bars, key=lambda b: b.get('confidence', 0))
        result['calibration_method'] = 'graphic_bar'
        result['confidence'] = best_bar.get('confidence', 0.95)
        result['mean_pixels_per_foot'] = best_bar.get('pixels_per_foot')
        logger.info(f"Graphic bar detected: {best_bar.get('pixels_per_foot', 0):.1f} px/ft")

    # ---- Step 2: Text Scale Notation (Secondary) ----
    text_scales = detect_text_scales(texts)
    result['text_scales'] = text_scales

    if text_scales and not graphic_bars:
        best_text = max(text_scales, key=lambda s: s.confidence)
        ppf = scale_factor_to_ppf(best_text.scale_factor, dpi)
        result['calibration_method'] = 'text_scale'
        result['confidence'] = best_text.confidence
        result['mean_pixels_per_foot'] = ppf
        logger.info(f"Text scale detected: {best_text.scale_string} → {ppf:.1f} px/ft")

    # ---- Step 3: Known-Dimension Fallback ----
    if not graphic_bars and not text_scales:
        known_dim = calibrate_from_known_dimension(texts, lines)
        if known_dim:
            result['calibration_method'] = 'known_dimension'
            result['confidence'] = known_dim.get('confidence', 0.65)
            result['mean_pixels_per_foot'] = known_dim.get('pixels_per_foot')
            logger.info(f"Known-dimension fallback: {known_dim.get('pixels_per_foot', 0):.1f} px/ft")

    # ---- Step 4: Multi-Zone Scale Mapping ----
    if zones and (graphic_bars or text_scales):
        zone_scales = map_zones_to_scales(zones, graphic_bars, text_scales, texts, dpi)
        result['zones'] = zone_scales

    # ---- Step 5: Stretch Detection ----
    if result['mean_pixels_per_foot'] and lines:
        stretch = detect_stretch(texts, lines, result['mean_pixels_per_foot'])
        if stretch:
            result['stretch_detected'] = stretch['detected']
            result['h_pixels_per_foot'] = stretch.get('h_ppf')
            result['v_pixels_per_foot'] = stretch.get('v_ppf')
            if stretch['detected']:
                # Correct mean using geometric mean
                import math
                result['mean_pixels_per_foot'] = math.sqrt(
                    stretch['h_ppf'] * stretch['v_ppf']
                )
                logger.warning(f"Stretch detected! H:{stretch['h_ppf']:.1f} V:{stretch['v_ppf']:.1f}")

    # Build legacy ScaleCalibration list for backward compatibility
    legacy_scales = []
    for bar in graphic_bars:
        legacy_scales.append(ScaleCalibration(
            scale_string=bar.get('label', 'graphic bar'),
            pixels_per_foot=bar.get('pixels_per_foot'),
            scale_factor=bar.get('scale_factor'),
            confidence=bar.get('confidence', 0.95),
            location=bar.get('location')
        ))
    for ts in text_scales:
        legacy_scales.append(ts)
    result['scales'] = legacy_scales

    logger.info(f"Scale calibration complete: method={result['calibration_method']}, "
                f"confidence={result['confidence']:.2f}, "
                f"ppf={result['mean_pixels_per_foot']}")

    return result


def detect_graphic_scale_bars(image: np.ndarray, texts: List[TextExtraction],
                              title_zone: Optional[Tuple],
                              dpi: int = 300) -> List[Dict]:
    """
    Detect graphic scale bars by finding horizontal lines with evenly-spaced
    tick marks and nearby distance labels.

    Returns list of dicts with: pixels_per_foot, pixel_length, real_world_feet,
    tick_count, location, label, confidence
    """
    logger.info("  Detecting graphic scale bars...")

    h, w = image.shape[:2]
    bars = []

    # Convert to grayscale for line detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image.copy()

    # Define search regions (priority order)
    search_regions = []

    # Region 1: Bottom-right quadrant (most common location)
    search_regions.append(('bottom_right', (w // 2, int(h * 0.7), w, h)))

    # Region 2: Title block area (if detected)
    if title_zone:
        tx0, ty0, tx1, ty1 = title_zone
        # Expand slightly above title block
        search_regions.append(('title_block', (
            max(0, tx0 - 50), max(0, ty0 - 100), min(w, tx1 + 50), min(h, ty1 + 50)
        )))

    # Region 3: Bottom center
    search_regions.append(('bottom_center', (w // 4, int(h * 0.8), 3 * w // 4, h)))

    # Region 4: Full bottom strip (wider search)
    search_regions.append(('bottom_strip', (0, int(h * 0.75), w, h)))

    for region_name, (rx0, ry0, rx1, ry1) in search_regions:
        roi = gray[ry0:ry1, rx0:rx1]
        if roi.size == 0:
            continue

        # Edge detection in ROI
        edges = cv2.Canny(roi, 50, 150, apertureSize=3)

        # Detect horizontal line segments using HoughLinesP
        min_line_len = int(50 * dpi / 300)  # Scale with DPI
        max_line_len = int(500 * dpi / 300)
        h_lines = cv2.HoughLinesP(
            edges, rho=1, theta=np.pi / 180, threshold=30,
            minLineLength=min_line_len, maxLineGap=5
        )

        if h_lines is None:
            continue

        for line in h_lines:
            x1, y1, x2, y2 = line[0]

            # Filter: must be nearly horizontal (< 2° slope)
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            if dx < 30 or (dy / max(dx, 1)) > 0.035:
                continue

            line_len = np.sqrt(dx**2 + dy**2)
            if line_len < min_line_len or line_len > max_line_len:
                continue

            # Convert to full-image coordinates
            abs_x1, abs_y1 = x1 + rx0, y1 + ry0
            abs_x2, abs_y2 = x2 + rx0, y2 + ry0
            line_y = (abs_y1 + abs_y2) // 2

            # Look for tick marks: short vertical segments near this line
            ticks = find_tick_marks(gray, abs_x1, abs_x2, line_y, dpi)

            if len(ticks) < 3:
                continue

            # Verify even spacing
            tick_positions = sorted([t[0] for t in ticks])  # X positions
            spacings = [tick_positions[i+1] - tick_positions[i]
                       for i in range(len(tick_positions) - 1)]

            if not spacings:
                continue

            mean_spacing = np.mean(spacings)
            if mean_spacing < 5:
                continue

            cv_spacing = np.std(spacings) / mean_spacing if mean_spacing > 0 else 999
            if cv_spacing > 0.20:  # Allow 20% variation (accounts for OCR-driven tick detection)
                continue

            # Match distance labels to ticks
            labels = match_labels_to_ticks(texts, tick_positions, line_y, rx0, ry0)

            if len(labels) < 2:
                continue

            # Calculate pixels_per_foot from label values
            label_values = sorted(labels, key=lambda l: l['tick_x'])
            first_val = label_values[0]['value']
            last_val = label_values[-1]['value']
            first_x = label_values[0]['tick_x']
            last_x = label_values[-1]['tick_x']

            real_world_span = last_val - first_val
            pixel_span = abs(last_x - first_x)

            if real_world_span <= 0 or pixel_span <= 0:
                continue

            # Determine unit (default to feet)
            unit = detect_scale_unit(texts, line_y)
            if unit == 'inches':
                real_world_feet = real_world_span / 12.0
            elif unit == 'meters':
                real_world_feet = real_world_span * 3.28084
            else:
                real_world_feet = real_world_span

            ppf = pixel_span / real_world_feet

            # Sanity check: ppf should be reasonable for construction drawings
            # At 200 DPI, 1/4" = 1'-0" → ~4.17 px/ft; at 300 DPI → ~6.25 px/ft
            # At 200 DPI, 1" = 20'-0" → ~0.83 px/ft (site plans)
            min_ppf = 0.5 * dpi / 300
            max_ppf = 200 * dpi / 300
            if ppf < min_ppf or ppf > max_ppf:
                continue

            bar_info = {
                'pixels_per_foot': ppf,
                'pixel_length': pixel_span,
                'real_world_feet': real_world_feet,
                'tick_count': len(ticks),
                'label_count': len(labels),
                'unit': unit,
                'location': (abs_x1, line_y),
                'region': region_name,
                'label': f"{real_world_span:.0f} {unit}",
                'confidence': 0.95,
                'scale_factor': 1.0 / (ppf * 12)  # inches on paper per inch real
            }

            bars.append(bar_info)
            logger.info(f"  Found bar in {region_name}: {ppf:.1f} px/ft, "
                       f"{len(ticks)} ticks, {len(labels)} labels")

            # One good bar per region is enough
            break

    # Deduplicate: if multiple regions found the same bar, keep highest confidence
    if len(bars) > 1:
        bars = deduplicate_bars(bars)

    return bars


def find_tick_marks(gray: np.ndarray, x_start: int, x_end: int,
                    line_y: int, dpi: int = 300) -> List[Tuple[int, int]]:
    """
    Find short vertical line segments (tick marks) near a horizontal line.

    Returns list of (x_position, tick_height) tuples.
    """
    ticks = []
    search_band = int(5 * dpi / 300)  # 5px at 300 DPI
    min_tick_h = int(8 * dpi / 300)
    max_tick_h = int(35 * dpi / 300)

    h_img, w_img = gray.shape[:2]
    y_min = max(0, line_y - max_tick_h - search_band)
    y_max = min(h_img, line_y + max_tick_h + search_band)

    if y_min >= y_max or x_start >= x_end:
        return ticks

    # Extract ROI around the line
    roi = gray[y_min:y_max, max(0, x_start):min(w_img, x_end)]
    if roi.size == 0:
        return ticks

    # Vertical edge detection (emphasize vertical lines)
    kernel_v = np.array([[-1, 2, -1]], dtype=np.float32)
    vert_edges = cv2.filter2D(roi, -1, kernel_v.T)
    _, thresh = cv2.threshold(np.abs(vert_edges).astype(np.uint8), 30, 255, cv2.THRESH_BINARY)

    # Find contours that look like vertical ticks
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, cw, ch = cv2.boundingRect(cnt)
        # Tick marks are tall and thin
        if ch >= min_tick_h and ch <= max_tick_h and cw <= int(6 * dpi / 300):
            tick_x = x + cw // 2 + max(0, x_start)  # Convert to full-image coords
            ticks.append((tick_x, ch))

    return ticks


def match_labels_to_ticks(texts: List[TextExtraction], tick_positions: List[int],
                          line_y: int, region_x_offset: int = 0,
                          region_y_offset: int = 0) -> List[Dict]:
    """
    Match OCR text elements to nearby tick positions to get distance labels.

    Returns list of dicts with: tick_x, value, text
    """
    labels = []
    max_x_dist = 30  # Max horizontal distance from tick to label center
    max_y_dist = 40  # Max vertical distance below the line

    for text in texts:
        # Only consider numeric text
        cleaned = text.content.strip().replace("'", "").replace('"', '').replace("ft", "").replace("FT", "")
        try:
            value = float(cleaned)
        except ValueError:
            continue

        # Text center
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        # Check if text is below the line and near a tick
        if ty < line_y or ty > line_y + max_y_dist:
            continue

        # Find nearest tick
        for tick_x in tick_positions:
            if abs(tx - tick_x) < max_x_dist:
                labels.append({
                    'tick_x': tick_x,
                    'value': value,
                    'text': text.content
                })
                break

    return labels


def detect_scale_unit(texts: List[TextExtraction], line_y: int) -> str:
    """
    Detect the unit label near a scale bar (FEET, INCHES, METERS, etc.)
    Returns 'feet', 'inches', or 'meters'. Default: 'feet'.
    """
    for text in texts:
        ty = (text.bbox[1] + text.bbox[3]) / 2
        if abs(ty - line_y) < 60:
            content_lower = text.content.strip().lower()
            if content_lower in ('inches', 'in', 'in.', '"'):
                return 'inches'
            elif content_lower in ('meters', 'm', 'metres'):
                return 'meters'
            elif content_lower in ('feet', 'ft', 'ft.', "'"):
                return 'feet'
    return 'feet'


def deduplicate_bars(bars: List[Dict]) -> List[Dict]:
    """Remove duplicate bar detections (same bar found by multiple regions)."""
    if len(bars) <= 1:
        return bars

    unique = [bars[0]]
    for bar in bars[1:]:
        is_dup = False
        for existing in unique:
            # Same location (within 50px) and similar ppf (within 5%)
            loc_dist = abs(bar['location'][0] - existing['location'][0]) + \
                       abs(bar['location'][1] - existing['location'][1])
            ppf_ratio = bar['pixels_per_foot'] / existing['pixels_per_foot'] \
                if existing['pixels_per_foot'] > 0 else 999
            if loc_dist < 50 and 0.95 < ppf_ratio < 1.05:
                is_dup = True
                # Keep higher confidence
                if bar['confidence'] > existing['confidence']:
                    unique.remove(existing)
                    unique.append(bar)
                break
        if not is_dup:
            unique.append(bar)

    return unique


def detect_text_scales(texts: List[TextExtraction]) -> List[ScaleCalibration]:
    """
    Detect scale from text labels (title block, view labels).
    Enhanced with more patterns and common scale formats.
    """
    scales = []
    seen = set()  # Avoid duplicate scale strings

    # Pattern 1: Explicit scale text elements from Pass 2 classification
    for text in texts:
        if text.text_type == 'scale':
            scale_calib = parse_scale_text(text.content, text.bbox)
            if scale_calib and scale_calib.scale_string not in seen:
                seen.add(scale_calib.scale_string)
                scales.append(scale_calib)

    # Pattern 2: Common scale patterns in any text
    common_scales = [
        ("1/4\" = 1'-0\"", 1/48),
        ("1/4\"=1'-0\"", 1/48),
        ("1/8\" = 1'-0\"", 1/96),
        ("1/8\"=1'-0\"", 1/96),
        ("3/16\" = 1'-0\"", 3/(16*12)),
        ("1/2\" = 1'-0\"", 1/24),
        ("1/2\"=1'-0\"", 1/24),
        ("1\" = 1'-0\"", 1/12),
        ("1\"=1'-0\"", 1/12),
        ("3/4\" = 1'-0\"", 3/(4*12)),
        ("1-1/2\" = 1'-0\"", 1.5/12),
        ("3\" = 1'-0\"", 3/12),
        ("1\" = 10'-0\"", 1/120),
        ("1\" = 20'-0\"", 1/240),
        ("1\" = 30'-0\"", 1/360),
        ("1\" = 40'-0\"", 1/480),
        ("1\" = 50'-0\"", 1/600),
        ("1:48", 1/48),
        ("1:96", 1/96),
        ("1:24", 1/24),
        ("1:12", 1/12),
        ("1:100", 1/100),
        ("1:200", 1/200),
        ("1:50", 1/50),
    ]

    for scale_text, scale_factor in common_scales:
        if scale_text in seen:
            continue
        for text in texts:
            if scale_text.lower().replace(" ", "") in text.content.lower().replace(" ", ""):
                seen.add(scale_text)
                scales.append(ScaleCalibration(
                    scale_string=scale_text,
                    scale_factor=scale_factor,
                    confidence=0.80,
                    location=(text.bbox[0], text.bbox[1])
                ))
                break  # One match per pattern

    return scales


def scale_factor_to_ppf(scale_factor: float, dpi: int) -> float:
    """
    Convert a scale factor to pixels per foot.

    For example: 1/4" = 1'-0" means scale_factor = 1/48
    At 300 DPI: 1/48 * 300 * 12 = 75 px/ft... wait, let me think.

    scale_factor = paper_inches / real_inches
    So 1/4" = 1'-0" means 0.25 paper inches = 12 real inches → scale_factor = 0.25/12 = 1/48

    pixels_per_real_inch = scale_factor * dpi
    pixels_per_real_foot = scale_factor * dpi * 12

    At 300 DPI, 1/4" = 1'-0": (1/48) * 300 * 12 = 75 px/ft
    At 200 DPI, 1/4" = 1'-0": (1/48) * 200 * 12 = 50 px/ft
    """
    return scale_factor * dpi * 12


def calibrate_from_known_dimension(texts: List[TextExtraction],
                                   lines: Optional[List] = None) -> Optional[Dict]:
    """
    Fallback: calibrate from the longest dimension string found on the sheet.
    Find a dimension text, locate its dimension line, measure pixel length.
    """
    # Find dimension texts sorted by real-world value (largest first)
    dim_texts = []
    for text in texts:
        if text.text_type == 'dimension':
            feet_val = parse_dimension_value(text.content)
            if feet_val and feet_val > 1.0:  # Ignore tiny dimensions
                dim_texts.append((text, feet_val))

    dim_texts.sort(key=lambda x: x[1], reverse=True)

    if not dim_texts:
        return None

    # Use the largest dimension
    best_text, best_feet = dim_texts[0]

    # If we have lines from Pass 3, find the dimension line near this text
    if lines:
        dim_line = find_nearest_dimension_line(best_text.bbox, lines)
        if dim_line:
            # Measure line length in pixels
            lx1, ly1, lx2, ly2 = dim_line
            pixel_length = np.sqrt((lx2 - lx1)**2 + (ly2 - ly1)**2)
            if pixel_length > 20:
                ppf = pixel_length / best_feet

                # Cross-check with second-largest dimension if available
                confidence = 0.60
                if len(dim_texts) > 1:
                    second_text, second_feet = dim_texts[1]
                    second_line = find_nearest_dimension_line(second_text.bbox, lines)
                    if second_line:
                        sx1, sy1, sx2, sy2 = second_line
                        second_px = np.sqrt((sx2 - sx1)**2 + (sy2 - sy1)**2)
                        expected_feet = second_px / ppf
                        error = abs(expected_feet - second_feet) / second_feet
                        if error < 0.05:
                            confidence = 0.80  # Excellent cross-check
                        elif error < 0.10:
                            confidence = 0.70  # Acceptable
                        else:
                            confidence = 0.50  # Poor — dimension might be in wrong zone

                return {
                    'pixels_per_foot': ppf,
                    'source_dimension': best_text.content,
                    'source_feet': best_feet,
                    'pixel_length': pixel_length,
                    'confidence': confidence
                }

    # Without lines, use text bbox width as rough proxy (much lower confidence)
    text_width = best_text.bbox[2] - best_text.bbox[0]
    if text_width > 0:
        # Very rough: assume dimension text spans roughly 1/4 of its dimension line
        # This is unreliable — flag as very low confidence
        return {
            'pixels_per_foot': None,  # Can't calculate without line
            'source_dimension': best_text.content,
            'source_feet': best_feet,
            'confidence': 0.30  # Too low to use
        }

    return None


def parse_dimension_value(text: str) -> Optional[float]:
    """
    Parse a dimension string into feet.
    Handles: 25'-0", 132'-8", 12'-6", 4'-0", 75'-0", 10", etc.
    """
    # Feet and inches: 25'-6"
    match = re.search(r"(\d+)['\u2019]\s*-?\s*(\d+)\s*[\"″]?", text)
    if match:
        feet = float(match.group(1))
        inches = float(match.group(2))
        return feet + inches / 12.0

    # Feet only: 25'
    match = re.search(r"(\d+)['\u2019]", text)
    if match:
        return float(match.group(1))

    # Inches only: 10"
    match = re.search(r"^(\d+)\s*[\"″]$", text.strip())
    if match:
        return float(match.group(1)) / 12.0

    return None


def find_nearest_dimension_line(text_bbox: Tuple, lines: List,
                                max_dist: float = 50.0) -> Optional[Tuple]:
    """
    Find the nearest horizontal or vertical dimension line to a text element.
    Dimension lines are thin lines with witness lines at ends.
    """
    tx_center = (text_bbox[0] + text_bbox[2]) / 2
    ty_center = (text_bbox[1] + text_bbox[3]) / 2

    best_line = None
    best_dist = max_dist

    for line_obj in lines:
        # Handle both dict and tuple line formats
        if isinstance(line_obj, dict):
            if line_obj.get('line_type') != 'dimension':
                continue
            coords = line_obj.get('endpoints', line_obj.get('coords'))
            if not coords:
                continue
            lx1, ly1, lx2, ly2 = coords[0][0], coords[0][1], coords[1][0], coords[1][1]
        elif hasattr(line_obj, 'line_type'):
            if line_obj.line_type != 'dimension':
                continue
            lx1, ly1, lx2, ly2 = line_obj.x1, line_obj.y1, line_obj.x2, line_obj.y2
        else:
            continue

        # Distance from text center to line midpoint
        mx, my = (lx1 + lx2) / 2, (ly1 + ly2) / 2
        dist = np.sqrt((tx_center - mx)**2 + (ty_center - my)**2)

        if dist < best_dist:
            best_dist = dist
            best_line = (lx1, ly1, lx2, ly2)

    return best_line


def map_zones_to_scales(zones: List[Dict], graphic_bars: List[Dict],
                        text_scales: List[ScaleCalibration],
                        texts: List[TextExtraction],
                        dpi: int = 300) -> List[Dict]:
    """
    Map each view zone to its calibrated scale.
    Zones come from Pass 1 layout detection.
    """
    zone_scales = []

    for zone in zones:
        zone_type = zone.get('zone_type', 'unknown')
        if zone_type in ('title_block', 'notes'):
            continue

        zbbox = zone.get('bbox', (0, 0, 0, 0))

        # Find scale texts within or near this zone
        zone_scale = None
        for text in texts:
            if text.text_type == 'scale':
                tx = (text.bbox[0] + text.bbox[2]) / 2
                ty = (text.bbox[1] + text.bbox[3]) / 2
                # Check if text is within or just below the zone
                if (zbbox[0] - 50 <= tx <= zbbox[2] + 50 and
                    zbbox[1] - 50 <= ty <= zbbox[3] + 100):
                    parsed = parse_scale_text(text.content, text.bbox)
                    if parsed:
                        zone_scale = {
                            'view_name': zone.get('label', zone_type),
                            'scale_text': parsed.scale_string,
                            'pixels_per_foot': scale_factor_to_ppf(parsed.scale_factor, dpi),
                            'calibration_method': 'text_scale',
                            'zone_bbox': list(zbbox),
                            'confidence': 'medium'
                        }
                        break

        # If no specific scale found, use the sheet's primary scale
        if not zone_scale:
            ppf = None
            method = 'inherited'
            if graphic_bars:
                ppf = graphic_bars[0].get('pixels_per_foot')
                method = 'graphic_bar'
            elif text_scales:
                ppf = scale_factor_to_ppf(text_scales[0].scale_factor, dpi)
                method = 'text_scale'

            if ppf:
                zone_scale = {
                    'view_name': zone.get('label', zone_type),
                    'scale_text': 'inherited from sheet',
                    'pixels_per_foot': ppf,
                    'calibration_method': method,
                    'zone_bbox': list(zbbox),
                    'confidence': 'low'
                }

        if zone_scale:
            zone_scales.append(zone_scale)

    return zone_scales


def detect_stretch(texts: List[TextExtraction], lines: List,
                   reference_ppf: float) -> Optional[Dict]:
    """
    Detect image stretch by comparing horizontal vs vertical scale calibration.
    Uses dimension lines to find H and V measurements independently.
    """
    h_dims = []  # (pixel_length, real_feet)
    v_dims = []

    for text in texts:
        if text.text_type != 'dimension':
            continue

        feet_val = parse_dimension_value(text.content)
        if not feet_val or feet_val < 2.0:
            continue

        dim_line = find_nearest_dimension_line(text.bbox, lines, max_dist=60)
        if not dim_line:
            continue

        lx1, ly1, lx2, ly2 = dim_line
        dx = abs(lx2 - lx1)
        dy = abs(ly2 - ly1)
        pixel_length = np.sqrt(dx**2 + dy**2)

        # Classify as horizontal or vertical
        if dx > dy * 3:  # Horizontal
            h_dims.append((pixel_length, feet_val))
        elif dy > dx * 3:  # Vertical
            v_dims.append((pixel_length, feet_val))

    if not h_dims or not v_dims:
        return None

    # Calculate ppf for each direction using median
    h_ppf_values = [px / ft for px, ft in h_dims]
    v_ppf_values = [px / ft for px, ft in v_dims]

    h_ppf = np.median(h_ppf_values)
    v_ppf = np.median(v_ppf_values)

    stretch_ratio = max(h_ppf, v_ppf) / min(h_ppf, v_ppf) if min(h_ppf, v_ppf) > 0 else 1.0

    return {
        'detected': stretch_ratio > 1.03,
        'h_ppf': float(h_ppf),
        'v_ppf': float(v_ppf),
        'stretch_ratio': float(stretch_ratio),
        'h_sample_count': len(h_dims),
        'v_sample_count': len(v_dims)
    }


def parse_scale_text(text: str, bbox: Tuple) -> Optional[ScaleCalibration]:
    """
    Parse scale notation from text string.
    Handles: 1/4" = 1'-0", 1" = 20'-0", 3/16" = 1'-0", 1-1/2" = 1'-0"

    Args:
        text: Text content
        bbox: Bounding box

    Returns:
        ScaleCalibration or None
    """
    # Pattern 1: Fraction = feet-inches (1/4" = 1'-0")
    match = re.search(
        r"(\d+)/(\d+)[\"′]?\s*=\s*(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?",
        text
    )
    if match:
        numer = float(match.group(1))
        denom = float(match.group(2))
        feet = float(match.group(3))
        inches = float(match.group(4)) if match.group(4) else 0
        feet_total = feet + inches / 12.0
        paper_inches = numer / denom
        scale_factor = paper_inches / (feet_total * 12)  # paper_in / real_in

        return ScaleCalibration(
            scale_string=text.strip(),
            scale_factor=scale_factor,
            confidence=0.85,
            location=bbox[:2]
        )

    # Pattern 2: Mixed number = feet (1-1/2" = 1'-0")
    match = re.search(
        r"(\d+)\s*-\s*(\d+)/(\d+)[\"′]?\s*=\s*(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?",
        text
    )
    if match:
        whole = float(match.group(1))
        numer = float(match.group(2))
        denom = float(match.group(3))
        feet = float(match.group(4))
        inches = float(match.group(5)) if match.group(5) else 0
        feet_total = feet + inches / 12.0
        paper_inches = whole + numer / denom
        scale_factor = paper_inches / (feet_total * 12)

        return ScaleCalibration(
            scale_string=text.strip(),
            scale_factor=scale_factor,
            confidence=0.85,
            location=bbox[:2]
        )

    # Pattern 3: Whole number = feet (1" = 20'-0")
    match = re.search(
        r"(\d+)[\"′]\s*=\s*(\d+)['\u2019]\s*-?\s*(\d*)\s*[\"″]?",
        text
    )
    if match:
        paper_inches = float(match.group(1))
        feet = float(match.group(2))
        inches = float(match.group(3)) if match.group(3) else 0
        feet_total = feet + inches / 12.0
        scale_factor = paper_inches / (feet_total * 12)

        return ScaleCalibration(
            scale_string=text.strip(),
            scale_factor=scale_factor,
            confidence=0.85,
            location=bbox[:2]
        )

    # Pattern 4: Ratio (1:48, 1:100)
    match = re.search(r"1\s*:\s*(\d+)", text)
    if match:
        ratio = float(match.group(1))
        scale_factor = 1.0 / ratio

        return ScaleCalibration(
            scale_string=text.strip(),
            scale_factor=scale_factor,
            confidence=0.75,
            location=bbox[:2]
        )

    return None


# =============================================================================
# Pass 8: Cross-Sheet Reference Detection
# =============================================================================

@dataclass
class CrossSheetReference:
    """A reference from one sheet to a view on another sheet."""
    ref_id: str
    source_sheet: Optional[str] = None  # Set by caller (sheet being processed)
    source_location: Optional[Dict] = None  # Grid ref, zone
    target_sheet: str = ''  # Sheet number referenced (e.g., "A-501")
    target_detail: str = ''  # Detail/section number (e.g., "3")
    callout_type: str = 'unknown'  # section, detail, elevation, interior_elevation, enlarged_plan
    description: str = ''
    position: Tuple[float, float] = (0.0, 0.0)
    has_arrow: bool = False
    confidence: float = 0.8


def detect_cross_sheet_references(image: np.ndarray,
                                   texts: List[TextExtraction],
                                   symbols: Optional[List] = None,
                                   dpi: int = 300) -> Dict[str, Any]:
    """
    Detect cross-sheet references: section cuts, detail callouts,
    elevation markers, enlarged plan references, and schedule references.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements from Pass 2
        symbols: Detected symbols from Pass 4 (optional)
        dpi: Image resolution

    Returns:
        Dict with: callouts (list), schedule_refs (list), spec_refs (list),
        drawing_index_entry (dict)
    """
    logger.info("Pass 8: Cross-Sheet Reference Detection")

    result = {
        'callouts': [],
        'schedule_refs': [],
        'spec_refs': [],
        'drawing_index_entry': None
    }

    ref_counter = [0]  # Mutable counter for closure

    def next_id():
        ref_counter[0] += 1
        return f"XREF-{ref_counter[0]:03d}"

    # ---- Step 1: Detect callout symbols (circles/diamonds with sheet refs) ----
    callout_refs = detect_callout_symbols(image, texts, dpi, next_id)
    result['callouts'] = callout_refs

    # ---- Step 2: Detect schedule references (door marks, window marks, etc.) ----
    sched_refs = detect_schedule_references(texts)
    result['schedule_refs'] = sched_refs

    # ---- Step 3: Detect spec section references ----
    spec_refs = detect_spec_references(texts)
    result['spec_refs'] = spec_refs

    # ---- Step 4: Extract drawing index entry from title block ----
    index_entry = extract_drawing_index_entry(texts)
    result['drawing_index_entry'] = index_entry

    logger.info(f"Detected {len(callout_refs)} callouts, "
                f"{len(sched_refs)} schedule refs, {len(spec_refs)} spec refs")

    return result


def detect_callout_symbols(image: np.ndarray, texts: List[TextExtraction],
                            dpi: int, next_id) -> List[CrossSheetReference]:
    """
    Detect section cut, detail, and elevation callout symbols.
    These are circles (20-60px at 300 DPI) containing text in "number/sheet" format.
    """
    refs = []
    h, w = image.shape[:2]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image.copy()

    # Detect circles using Hough Circle Transform
    min_r = int(10 * dpi / 300)
    max_r = int(35 * dpi / 300)

    # Apply blur to improve circle detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=int(30 * dpi / 300),
        param1=80,
        param2=30,
        minRadius=min_r,
        maxRadius=max_r
    )

    if circles is None:
        # Fall back to text-based detection
        refs.extend(detect_callouts_from_text(texts, next_id))
        return refs

    circles = np.uint16(np.around(circles[0]))

    for cx, cy, r in circles:
        # Find text elements inside or very near this circle
        inner_texts = []
        nearby_texts = []
        search_r = r * 1.5

        for text in texts:
            tx = (text.bbox[0] + text.bbox[2]) / 2
            ty = (text.bbox[1] + text.bbox[3]) / 2
            dist = np.sqrt((tx - cx)**2 + (ty - cy)**2)

            if dist < r * 0.9:
                inner_texts.append(text)
            elif dist < search_r:
                nearby_texts.append(text)

        if not inner_texts and not nearby_texts:
            continue

        # Try to parse sheet reference from inner text
        all_candidates = inner_texts + nearby_texts
        ref = parse_callout_text(all_candidates, cx, cy, next_id)

        if ref:
            # Check for arrow (section cut indicator)
            ref.has_arrow = detect_arrow_near_circle(gray, cx, cy, r, dpi)
            if ref.has_arrow:
                ref.callout_type = 'section'
            elif ref.callout_type == 'unknown':
                ref.callout_type = 'detail'

            refs.append(ref)

    # Also check text-based patterns that may not have detectable circles
    text_refs = detect_callouts_from_text(texts, next_id)
    # Deduplicate: don't add text refs that overlap with circle-detected refs
    for tr in text_refs:
        is_dup = False
        for cr in refs:
            if (tr.target_sheet == cr.target_sheet and
                tr.target_detail == cr.target_detail):
                is_dup = True
                break
        if not is_dup:
            refs.append(tr)

    return refs


def parse_callout_text(texts: List[TextExtraction], cx: float, cy: float,
                        next_id) -> Optional[CrossSheetReference]:
    """
    Parse callout text to extract sheet reference.
    Handles: "3/A-301", "3\nA-301", "3" + "A-301" (separate texts),
    "DETAIL 5/A-501", etc.
    """
    # Combine all text content
    all_content = ' '.join([t.content.strip() for t in texts])

    # Pattern 1: "number / sheet_number" (e.g., "3/A-301", "5 / A-501")
    match = re.search(
        r'(\d{1,3})\s*[/\\]\s*([A-Z])-?(\d{1,3}(?:\.\d)?)',
        all_content, re.IGNORECASE
    )
    if match:
        detail_num = match.group(1)
        disc = match.group(2).upper()
        sheet_num = match.group(3)
        target_sheet = f"{disc}-{sheet_num}"

        return CrossSheetReference(
            ref_id=next_id(),
            target_sheet=target_sheet,
            target_detail=detail_num,
            position=(float(cx), float(cy)),
            confidence=0.90
        )

    # Pattern 2: Stacked text (detail on top, sheet on bottom)
    if len(texts) >= 2:
        # Sort by Y position (top first)
        sorted_texts = sorted(texts, key=lambda t: t.bbox[1])
        top = sorted_texts[0].content.strip()
        bottom = sorted_texts[-1].content.strip()

        # Top should be a number, bottom should be a sheet number
        if re.match(r'^\d{1,3}$', top):
            sheet_match = re.match(r'^([A-Z])-?(\d{1,3}(?:\.\d)?)$', bottom, re.IGNORECASE)
            if sheet_match:
                return CrossSheetReference(
                    ref_id=next_id(),
                    target_sheet=f"{sheet_match.group(1).upper()}-{sheet_match.group(2)}",
                    target_detail=top,
                    position=(float(cx), float(cy)),
                    confidence=0.85
                )

    # Pattern 3: Just a number (might be keyed to a nearby "SIM" or view title)
    for t in texts:
        if re.match(r'^\d{1,2}$', t.content.strip()):
            return CrossSheetReference(
                ref_id=next_id(),
                target_sheet='',  # Unknown — needs cross-sheet resolution
                target_detail=t.content.strip(),
                position=(float(cx), float(cy)),
                confidence=0.50
            )

    return None


def detect_arrow_near_circle(gray: np.ndarray, cx: int, cy: int,
                              r: int, dpi: int) -> bool:
    """
    Detect if there's an arrow extending from a circle (indicating section cut).
    Arrows are thick line segments extending from the circle edge.
    """
    search_dist = int(r * 2.5)

    # Check for significant line segments radiating from circle edge
    # Use a small ROI around the circle
    y_min = max(0, cy - search_dist)
    y_max = min(gray.shape[0], cy + search_dist)
    x_min = max(0, cx - search_dist)
    x_max = min(gray.shape[1], cx + search_dist)

    roi = gray[y_min:y_max, x_min:x_max]
    if roi.size == 0:
        return False

    edges = cv2.Canny(roi, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=20,
                            minLineLength=int(r * 1.2),
                            maxLineGap=5)

    if lines is None:
        return False

    # Look for lines that start near the circle edge and extend outward
    roi_cx, roi_cy = cx - x_min, cy - y_min

    for line in lines:
        lx1, ly1, lx2, ly2 = line[0]

        # Check if one end is near the circle edge
        for px, py in [(lx1, ly1), (lx2, ly2)]:
            dist_to_center = np.sqrt((px - roi_cx)**2 + (py - roi_cy)**2)
            if r * 0.7 < dist_to_center < r * 1.5:
                # Line end is near circle edge — likely an arrow
                return True

    return False


def detect_callouts_from_text(texts: List[TextExtraction],
                               next_id) -> List[CrossSheetReference]:
    """
    Detect cross-sheet references purely from text patterns
    (when circle detection fails or for text-based references).
    """
    refs = []

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        # "SEE DETAIL X/SHEET" or "SEE SHEET X-XXX"
        match = re.search(
            r'SEE\s+(?:DETAIL|SECTION|DWG|SHEET)?\s*(\d{1,3})\s*[/\\]\s*([A-Z])-?(\d{1,3})',
            content, re.IGNORECASE
        )
        if match:
            refs.append(CrossSheetReference(
                ref_id=next_id(),
                target_sheet=f"{match.group(2).upper()}-{match.group(3)}",
                target_detail=match.group(1),
                callout_type='detail',
                description=content,
                position=(tx, ty),
                confidence=0.80
            ))
            continue

        # "SEE ENLARGED PLAN A-102"
        match = re.search(
            r'(?:SEE|REFER TO)\s+.*?([A-Z])-?(\d{1,3}(?:\.\d)?)',
            content, re.IGNORECASE
        )
        if match and len(content) > 10:  # Avoid false positives on short text
            refs.append(CrossSheetReference(
                ref_id=next_id(),
                target_sheet=f"{match.group(1).upper()}-{match.group(2)}",
                target_detail='',
                callout_type='enlarged_plan',
                description=content,
                position=(tx, ty),
                confidence=0.70
            ))

    return refs


def detect_schedule_references(texts: List[TextExtraction]) -> List[Dict]:
    """
    Detect door marks, window marks, equipment tags, and room numbers
    that reference schedules on other sheets.
    """
    refs = []

    for text in texts:
        content = text.content.strip()

        # Door marks: D101, D-101, 101A (in door schedule context)
        if re.match(r'^D-?\d{3}[A-Z]?$', content, re.IGNORECASE):
            refs.append({
                'mark': content,
                'schedule_type': 'door',
                'position': {
                    'x': (text.bbox[0] + text.bbox[2]) / 2,
                    'y': (text.bbox[1] + text.bbox[3]) / 2
                }
            })

        # Window marks: W-1, W-2, W1
        elif re.match(r'^W-?\d{1,3}$', content, re.IGNORECASE):
            refs.append({
                'mark': content,
                'schedule_type': 'window',
                'position': {
                    'x': (text.bbox[0] + text.bbox[2]) / 2,
                    'y': (text.bbox[1] + text.bbox[3]) / 2
                }
            })

        # Equipment tags: RTU-1, AHU-2, EF-1
        elif re.match(r'^(RTU|AHU|EF|MAU|CUH|FCU|VAV|HP|ERV)-?\d{1,3}$', content, re.IGNORECASE):
            refs.append({
                'mark': content,
                'schedule_type': 'equipment',
                'position': {
                    'x': (text.bbox[0] + text.bbox[2]) / 2,
                    'y': (text.bbox[1] + text.bbox[3]) / 2
                }
            })

    return refs


def detect_spec_references(texts: List[TextExtraction]) -> List[Dict]:
    """
    Detect specification section references in drawing notes.
    Format: XX XX XX (CSI MasterFormat)
    """
    refs = []

    for text in texts:
        content = text.content.strip()

        # CSI format: 03 30 00, 09 65 00, etc.
        matches = re.findall(r'\b(\d{2}\s+\d{2}\s+\d{2})\b', content)
        for spec_match in matches:
            refs.append({
                'spec_section': spec_match,
                'context': content[:80],
                'position': {
                    'x': (text.bbox[0] + text.bbox[2]) / 2,
                    'y': (text.bbox[1] + text.bbox[3]) / 2
                }
            })

    return refs


def extract_drawing_index_entry(texts: List[TextExtraction]) -> Optional[Dict]:
    """
    Extract sheet number, title, discipline, and revision from title block text.
    This builds the drawing_index for the cross-reference system.
    """
    entry = {
        'sheet_number': None,
        'title': None,
        'discipline': None,
        'type': None,
        'revision': None,
        'date': None
    }

    for text in texts:
        content = text.content.strip()

        # Sheet number: A-100, S-201, C-103, M-101, E-101, P-101
        if not entry['sheet_number']:
            match = re.match(r'^([ASCMEPLFG])-?(\d{1,3}(?:\.\d)?)$', content, re.IGNORECASE)
            if match:
                disc = match.group(1).upper()
                num = match.group(2)
                entry['sheet_number'] = f"{disc}-{num}"
                entry['discipline'] = disc

                # Infer type from sheet number
                sheet_num = int(re.match(r'(\d)', num).group(1)) if re.match(r'(\d)', num) else 0
                if disc == 'C':
                    entry['type'] = 'site'
                elif sheet_num == 0:
                    entry['type'] = 'cover'
                elif sheet_num == 1:
                    entry['type'] = 'floor_plan'
                elif sheet_num == 2:
                    entry['type'] = 'elevation'
                elif sheet_num == 3:
                    entry['type'] = 'section'
                elif sheet_num >= 5:
                    entry['type'] = 'detail'
                elif sheet_num == 8:
                    entry['type'] = 'schedule'

        # Title (typically all caps, medium-long text)
        if not entry['title'] and text.text_type in ('room_number', 'scale', None):
            if len(content) > 8 and content.isupper() and ' ' in content:
                if any(kw in content for kw in ['PLAN', 'ELEVATION', 'SECTION', 'DETAIL',
                                                  'SCHEDULE', 'FOUNDATION', 'FRAMING',
                                                  'CEILING', 'ROOF', 'SITE', 'GRADING']):
                    entry['title'] = content

        # Revision
        if not entry['revision']:
            rev_match = re.search(r'REV\.?\s*([A-Z0-9]+)', content, re.IGNORECASE)
            if rev_match:
                entry['revision'] = rev_match.group(1)

    if entry['sheet_number']:
        return entry
    return None


# =============================================================================
# Pass 9: Contour Line Detection + Cut/Fill Estimation (Civil/Site Sheets)
# =============================================================================

@dataclass
class ContourLine:
    """A detected contour line with elevation."""
    elevation_ft: float
    line_style: str  # 'solid' (proposed) or 'dashed' (existing)
    contour_type: str  # 'existing' or 'proposed'
    is_index: bool = False  # Index contours are thicker (every 5th or 10th)
    vertices: List[Tuple[float, float]] = None  # Pixel coordinates of the line
    sheet: Optional[str] = None
    confidence: float = 0.7


def detect_contour_lines(image: np.ndarray, texts: List[TextExtraction],
                          scale_ppf: Optional[float] = None,
                          dpi: int = 300) -> Dict[str, Any]:
    """
    Detect contour lines on civil/site plan sheets.

    Contour lines are:
    - Existing: dashed curves with elevation labels (current terrain)
    - Proposed: solid curves with elevation labels (design terrain)
    - Index contours: thicker lines every 5th or 10th interval

    The difference between existing and proposed at any point = cut or fill depth.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements from Pass 2
        scale_ppf: Pixels per foot from Pass 7
        dpi: Image resolution

    Returns:
        Dict with: existing_contours, proposed_contours, contour_interval,
        spot_elevations (civil), drainage_patterns, cut_fill_estimate
    """
    logger.info("Pass 9: Contour Line Detection")

    result = {
        'existing_contours': [],
        'proposed_contours': [],
        'contour_interval_ft': None,
        'drainage_patterns': [],
        'cut_fill_estimate': None
    }

    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image.copy()

    # ---- Step 1: Identify contour elevation labels ----
    contour_labels = extract_contour_labels(texts)

    if not contour_labels:
        logger.info("No contour elevation labels found — may not be a grading sheet")
        return result

    # ---- Step 2: Determine contour interval ----
    interval = determine_contour_interval(contour_labels)
    result['contour_interval_ft'] = interval

    # ---- Step 3: Detect contour line segments ----
    # Separate existing (dashed) from proposed (solid)
    existing, proposed = classify_contour_lines(gray, contour_labels, dpi)
    result['existing_contours'] = existing
    result['proposed_contours'] = proposed

    # ---- Step 4: Estimate cut/fill if both existing and proposed are found ----
    if existing and proposed and scale_ppf:
        estimate = estimate_cut_fill(existing, proposed, scale_ppf, contour_labels)
        result['cut_fill_estimate'] = estimate

    # ---- Step 5: Detect drainage patterns ----
    drainage = detect_drainage_patterns(contour_labels, existing, proposed)
    result['drainage_patterns'] = drainage

    logger.info(f"Detected {len(existing)} existing + {len(proposed)} proposed contours, "
                f"interval={interval}")

    return result


def extract_contour_labels(texts: List[TextExtraction]) -> List[Dict]:
    """
    Extract contour elevation labels from OCR text.
    Contour labels are typically 3-4 digit numbers (800-1200 range for most sites)
    placed along contour lines, sometimes rotated to follow the curve.
    """
    labels = []

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        # Integer elevations: 856, 857, 858, etc.
        if re.match(r'^(\d{3,4})$', content):
            elev = float(content)
            if 100 < elev < 5000:  # Reasonable elevation range
                labels.append({
                    'elevation_ft': elev,
                    'position': (tx, ty),
                    'text': content,
                    'type': 'integer'
                })

        # Decimal elevations: 856.5, 857.0
        elif re.match(r'^(\d{3,4}\.\d{1,2})$', content):
            elev = float(content)
            if 100 < elev < 5000:
                labels.append({
                    'elevation_ft': elev,
                    'position': (tx, ty),
                    'text': content,
                    'type': 'decimal'
                })

    return labels


def determine_contour_interval(labels: List[Dict]) -> Optional[float]:
    """
    Determine the contour interval from the extracted labels.
    Common intervals: 1', 2', 5', 10' (US), 0.5m, 1m, 5m (metric)
    """
    if len(labels) < 3:
        return None

    elevations = sorted(set(l['elevation_ft'] for l in labels))
    if len(elevations) < 3:
        return None

    # Calculate differences between consecutive unique elevations
    diffs = [elevations[i+1] - elevations[i] for i in range(len(elevations) - 1)]

    if not diffs:
        return None

    # The contour interval is the most common difference (mode)
    # Round to nearest common interval
    common_intervals = [0.5, 1.0, 2.0, 5.0, 10.0]
    min_diff = min(diffs)

    best_interval = min(common_intervals, key=lambda ci: abs(ci - min_diff))
    return best_interval


def classify_contour_lines(gray: np.ndarray, labels: List[Dict],
                            dpi: int = 300) -> Tuple[List[Dict], List[Dict]]:
    """
    Classify contour lines as existing (dashed) or proposed (solid).

    Uses line detection near known elevation labels and analyzes
    dash patterns to distinguish existing from proposed.
    """
    existing = []
    proposed = []

    # For each contour label, sample the nearby line pattern
    for label in labels:
        lx, ly = int(label['position'][0]), int(label['position'][1])
        elev = label['elevation_ft']

        # Sample a horizontal strip around the label to detect line style
        search_h = int(20 * dpi / 300)
        search_w = int(80 * dpi / 300)

        y_min = max(0, ly - search_h)
        y_max = min(gray.shape[0], ly + search_h)
        x_min = max(0, lx - search_w)
        x_max = min(gray.shape[1], lx + search_w)

        roi = gray[y_min:y_max, x_min:x_max]
        if roi.size == 0:
            continue

        # Threshold to binary
        _, binary = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Analyze line continuity — dashed lines have gaps
        # Project horizontally to get a 1D signal
        h_proj = np.mean(binary, axis=0)

        # Count transitions (black→white and white→back)
        threshold_val = np.mean(h_proj) * 0.5
        above = h_proj > threshold_val
        transitions = np.sum(np.diff(above.astype(int)) != 0)

        # Many transitions = dashed (existing), few = solid (proposed)
        # Heuristic: > 6 transitions in the search width suggests dashed
        is_dashed = transitions > 6

        contour_info = {
            'elevation_ft': elev,
            'line_style': 'dashed' if is_dashed else 'solid',
            'position': label['position'],
            'label': label['text'],
            'is_index': (elev % 5 == 0),  # Index contours every 5'
            'confidence': 0.70
        }

        if is_dashed:
            existing.append(contour_info)
        else:
            proposed.append(contour_info)

    return existing, proposed


def estimate_cut_fill(existing: List[Dict], proposed: List[Dict],
                       scale_ppf: float, labels: List[Dict]) -> Dict:
    """
    Rough cut/fill estimate based on contour differences.

    For each location where we have both existing and proposed elevations,
    the difference indicates cut (proposed < existing) or fill (proposed > existing).
    """
    # Group contours by nearby positions
    cut_depths = []
    fill_depths = []

    for ex in existing:
        for pr in proposed:
            # Check if contours are at similar positions (within 50px)
            ex_pos = ex['position']
            pr_pos = pr['position']
            dist = np.sqrt((ex_pos[0] - pr_pos[0])**2 + (ex_pos[1] - pr_pos[1])**2)

            if dist < 100:  # Close enough to compare
                diff = pr['elevation_ft'] - ex['elevation_ft']
                if diff < -0.5:
                    cut_depths.append(abs(diff))
                elif diff > 0.5:
                    fill_depths.append(diff)

    estimate = {
        'has_data': bool(cut_depths or fill_depths),
        'cut_locations': len(cut_depths),
        'fill_locations': len(fill_depths),
        'avg_cut_depth_ft': round(np.mean(cut_depths), 1) if cut_depths else 0,
        'max_cut_depth_ft': round(max(cut_depths), 1) if cut_depths else 0,
        'avg_fill_depth_ft': round(np.mean(fill_depths), 1) if fill_depths else 0,
        'max_fill_depth_ft': round(max(fill_depths), 1) if fill_depths else 0,
        'net_operation': 'cut' if len(cut_depths) > len(fill_depths) else 'fill',
        'confidence': 'low',
        'note': 'Rough estimate from contour label proximity — verify with earthwork quantity takeoff'
    }

    return estimate


def detect_drainage_patterns(labels: List[Dict], existing: List[Dict],
                              proposed: List[Dict]) -> List[Dict]:
    """
    Detect drainage flow direction from contour patterns.
    Water flows perpendicular to contours, from high to low.
    """
    patterns = []

    # Use proposed contours (design intent) if available, else existing
    contours = proposed if proposed else existing
    if len(contours) < 3:
        return patterns

    # Sort by elevation
    sorted_contours = sorted(contours, key=lambda c: c['elevation_ft'])

    # Find the general flow direction (from highest cluster to lowest cluster)
    if len(sorted_contours) >= 2:
        high = sorted_contours[-1]
        low = sorted_contours[0]

        dx = low['position'][0] - high['position'][0]
        dy = low['position'][1] - high['position'][1]

        # Classify direction
        if abs(dx) > abs(dy) * 2:
            direction = 'east' if dx > 0 else 'west'
        elif abs(dy) > abs(dx) * 2:
            direction = 'south' if dy > 0 else 'north'
        else:
            if dx > 0 and dy > 0:
                direction = 'southeast'
            elif dx > 0:
                direction = 'northeast'
            elif dy > 0:
                direction = 'southwest'
            else:
                direction = 'northwest'

        patterns.append({
            'direction': direction,
            'high_elevation': high['elevation_ft'],
            'low_elevation': low['elevation_ft'],
            'fall_ft': round(high['elevation_ft'] - low['elevation_ft'], 1),
            'confidence': 0.60
        })

    return patterns


# =============================================================================
# Pass 10: Building Section + Wall Section Extraction
# =============================================================================

@dataclass
class SectionMeasurement:
    """A measurement extracted from a building or wall section."""
    label: str  # e.g., "FFE to T.O. Steel", "GWB thickness"
    value_ft: Optional[float] = None  # Value in feet (for heights)
    value_in: Optional[float] = None  # Value in inches (for layers)
    confidence: str = 'medium'


@dataclass
class WallLayer:
    """A single layer in a wall section assembly."""
    material: str  # e.g., "5/8\" Type X GWB"
    thickness_in: float = 0.0
    position: str = 'unknown'  # exterior_finish, sheathing, air_barrier, insulation, stud_cavity, interior_finish
    r_value: Optional[float] = None
    confidence: float = 0.7


@dataclass
class BuildingSection:
    """Data extracted from a building section cut."""
    section_id: str
    sheet: Optional[str] = None
    section_mark: Optional[str] = None
    cut_line_on_sheet: Optional[str] = None
    cut_location: Optional[str] = None
    scale: Optional[str] = None
    title: Optional[str] = None
    floor_to_floor_ft: float = 0.0
    foundation_depth_ft: float = 0.0
    footing_thickness_in: float = 0.0
    stem_wall_height_ft: float = 0.0
    ridge_height_ft: float = 0.0
    eave_height_ft: float = 0.0
    parapet_height_ft: float = 0.0
    roof_slope: Optional[str] = None  # e.g., "4:12"
    roof_slope_degrees: float = 0.0
    ceiling_height_ft: float = 0.0
    ceiling_type: Optional[str] = None  # ACT, GWB, exposed
    structural_depth_in: float = 0.0
    structural_member: Optional[str] = None  # rafter, truss, joist, beam
    sog_thickness_in: float = 0.0
    measurements: List[SectionMeasurement] = None
    confidence: float = 0.7

    def __post_init__(self):
        if self.measurements is None:
            self.measurements = []


@dataclass
class WallSection:
    """Data extracted from a wall section detail."""
    section_id: str
    sheet: Optional[str] = None
    section_mark: Optional[str] = None
    wall_type: Optional[str] = None
    fire_rating: Optional[str] = None
    total_thickness_in: float = 0.0
    layers: List[WallLayer] = None
    base_condition: Optional[str] = None
    top_condition: Optional[str] = None
    head_detail: Optional[str] = None
    sill_detail: Optional[str] = None
    measurements: List[SectionMeasurement] = None
    confidence: float = 0.7

    def __post_init__(self):
        if self.layers is None:
            self.layers = []
        if self.measurements is None:
            self.measurements = []


def extract_sections(image: np.ndarray, texts: List[TextExtraction],
                     lines: List[LineSegment],
                     dimensions: List[Dimension],
                     elevation_markers: List[Dict] = None,
                     scale_ppf: Optional[float] = None,
                     dpi: int = 300) -> Dict[str, Any]:
    """
    Extract building section and wall section data from section/detail sheets.

    Building sections show full-height cuts through the building (foundation-to-roof).
    Wall sections show enlarged layer-by-layer wall assembly details.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements from Pass 2
        lines: Detected line segments from Pass 3
        dimensions: Extracted dimensions from Pass 6
        elevation_markers: Elevation markers from Pass 6 (optional)
        scale_ppf: Pixels per foot from Pass 7
        dpi: Image resolution

    Returns:
        Dict with: building_sections, wall_sections, roof_slopes, section_count
    """
    logger.info("Pass 10: Building Section + Wall Section Extraction")

    result = {
        'building_sections': [],
        'wall_sections': [],
        'roof_slopes': [],
        'section_count': 0
    }

    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image.copy()

    # ---- Step 1: Detect if this is a section sheet ----
    is_section_sheet = detect_section_sheet_type(texts)
    if not is_section_sheet:
        logger.info("Sheet does not appear to be a section sheet — skipping Pass 10")
        return result

    # ---- Step 2: Extract elevation markers for height calculations ----
    section_elevations = extract_section_elevations(texts, elevation_markers or [])

    # ---- Step 3: Detect roof slope triangles ----
    slopes = detect_roof_slopes(texts, lines, gray, dpi)
    result['roof_slopes'] = slopes

    # ---- Step 4: Detect building sections ----
    building_sects = detect_building_sections(
        texts, dimensions, section_elevations, slopes, scale_ppf, h, w
    )
    result['building_sections'] = [asdict(s) for s in building_sects]

    # ---- Step 5: Detect wall sections ----
    wall_sects = detect_wall_sections(
        image, texts, dimensions, lines, gray, scale_ppf, dpi, h, w
    )
    result['wall_sections'] = [asdict(s) for s in wall_sects]

    result['section_count'] = len(building_sects) + len(wall_sects)

    logger.info(f"Extracted {len(building_sects)} building sections, "
                f"{len(wall_sects)} wall sections, {len(slopes)} roof slopes")

    return result


def detect_section_sheet_type(texts: List[TextExtraction]) -> bool:
    """
    Determine if a sheet contains building or wall sections.
    Checks title block and drawing titles for section-related keywords.
    """
    section_keywords = [
        r'BUILDING\s+SECTION',
        r'WALL\s+SECTION',
        r'CROSS\s+SECTION',
        r'LONGITUDINAL\s+SECTION',
        r'TRANSVERSE\s+SECTION',
        r'TYPICAL\s+WALL',
        r'SECTION\s+DETAIL',
        r'EXTERIOR\s+WALL',
        r'INTERIOR\s+WALL',
        r'PARTITION\s+SECTION',
    ]

    # Also check sheet number patterns: A-300, A-301, A-400, S-300, etc.
    sheet_patterns = [
        r'A-?3\d{2}',  # Architectural section sheets
        r'A-?4\d{2}',  # Architectural detail sheets
        r'A-?5\d{2}',  # Architectural detail sheets
        r'S-?3\d{2}',  # Structural section sheets
    ]

    combined = ' '.join(t.content.upper() for t in texts)

    for pattern in section_keywords:
        if re.search(pattern, combined, re.IGNORECASE):
            return True

    for pattern in sheet_patterns:
        if re.search(pattern, combined, re.IGNORECASE):
            return True

    # Check for elevation marker density — section sheets have many elevation annotations
    elev_count = 0
    for t in texts:
        content = t.content.strip().upper()
        if re.match(r'^(T\.?O\.?\s|B\.?O\.?\s|FFE|FG|FINISH\s+FLOOR|PLATE|RIDGE)', content):
            elev_count += 1

    if elev_count >= 3:
        return True

    return False


def extract_section_elevations(texts: List[TextExtraction],
                                elevation_markers: List[Dict]) -> List[Dict]:
    """
    Extract all elevation annotations from section drawings.
    Returns elevation markers with their pixel positions and values.
    """
    elevations = []

    # First, use pre-extracted elevation markers from Pass 6 if available
    for marker in elevation_markers:
        elevations.append({
            'label': marker.get('label', ''),
            'elevation_ft': marker.get('elevation_ft'),
            'elevation_value': marker.get('value', ''),
            'x': marker.get('x', 0),
            'y': marker.get('y', 0),
            'source': 'pass_6'
        })

    # Supplement with additional section-specific markers from text
    section_elev_patterns = [
        # Named elevation markers: "T.O. STEEL EL. 114'-6\""
        (r"(T\.?O\.?\s+(?:STEEL|WALL|PLATE|FOOTING|SLAB|CONC|PARAPET|RIDGE|MASONRY|JOIST|DECK))"
         r".*?(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?",
         'named'),
        # FFE / FG markers: "FFE = 100'-0\""
        (r"(FFE|FG|FINISH\s+(?:FLOOR|GRADE))\s*[=:]\s*(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?",
         'reference'),
        # Bottom of markers: "B.O. FOOTING EL. 96'-0\""
        (r"(B\.?O\.?\s+(?:FOOTING|SLAB|GRADE\s+BEAM|PIER|WALL))"
         r".*?(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?",
         'named'),
        # Ceiling height: "CLG HT = 10'-0\""
        (r"(CLG\s*(?:HT|HEIGHT)?|CEILING\s*(?:HT|HEIGHT)?)\s*[=:]\s*(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?",
         'ceiling'),
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        for pattern, elev_type in section_elev_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                label = match.group(1).strip()
                feet = float(match.group(2))
                inches_str = match.group(3).strip()
                inches = parse_fraction_inches(inches_str)
                elevation_ft = feet + inches / 12.0

                # Check for duplicates
                is_dup = False
                for existing in elevations:
                    if (existing.get('label', '').upper() == label.upper() and
                            abs(existing.get('elevation_ft', 0) - elevation_ft) < 0.1):
                        is_dup = True
                        break

                if not is_dup:
                    elevations.append({
                        'label': label,
                        'elevation_ft': elevation_ft,
                        'elevation_value': f"{int(feet)}'-{inches_str}\"",
                        'x': tx,
                        'y': ty,
                        'source': 'pass_10',
                        'type': elev_type
                    })

    return elevations


def parse_fraction_inches(inch_str: str) -> float:
    """Parse inch strings that may contain fractions: '6', '6 1/2', '0'."""
    inch_str = inch_str.strip().replace('"', '').replace('″', '')
    if not inch_str or inch_str == '0':
        return 0.0

    # Check for fraction: "6 1/2" or "1/2"
    frac_match = re.match(r'^(\d+)?\s*(\d+)/(\d+)$', inch_str)
    if frac_match:
        whole = float(frac_match.group(1) or 0)
        num = float(frac_match.group(2))
        den = float(frac_match.group(3))
        return whole + num / den if den != 0 else whole

    try:
        return float(inch_str)
    except ValueError:
        return 0.0


def detect_roof_slopes(texts: List[TextExtraction],
                        lines: List[LineSegment],
                        gray: np.ndarray,
                        dpi: int) -> List[Dict]:
    """
    Detect roof slope annotations from slope triangle symbols and text notation.

    Slope triangles are right triangles with rise/run labels (e.g., 4:12).
    Text notations include "4:12", "1/4\":12\"", "MIN 1/4\"/FT".
    """
    slopes = []
    import math

    # Method 1: Text-based slope detection
    slope_patterns = [
        # Standard ratio: "4:12", "4 : 12"
        (r'(\d+(?:\.\d+)?)\s*:\s*12', 'ratio'),
        # Fraction per foot: "1/4\"/FT", "1/2\" PER FOOT"
        (r'(\d+)/(\d+)\s*[\"″]\s*/?\s*(?:FT|FOOT|12[\"″]?)', 'fraction_per_foot'),
        # Roof slope label: "ROOF SLOPE 4:12"
        (r'(?:ROOF|SLOPE|PITCH)\s*(?:[=:])?\s*(\d+(?:\.\d+)?)\s*:\s*12', 'labeled_ratio'),
        # Minimum slope: "MIN 1/4\"/FT"
        (r'MIN\.?\s*(\d+)/(\d+)\s*[\"″]\s*/?\s*(?:FT|FOOT)', 'min_slope'),
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        for pattern, slope_type in slope_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                if slope_type in ('ratio', 'labeled_ratio'):
                    rise = float(match.group(1))
                    run = 12.0
                elif slope_type in ('fraction_per_foot', 'min_slope'):
                    rise = float(match.group(1)) / float(match.group(2))
                    run = 12.0
                else:
                    continue

                degrees = math.degrees(math.atan(rise / run)) if run != 0 else 0
                slope_str = f"{rise}:12" if rise == int(rise) else f"{rise:.2f}:12"

                # Check for duplicate
                is_dup = any(
                    abs(s.get('slope_degrees', 0) - degrees) < 0.5
                    for s in slopes
                )
                if not is_dup:
                    slopes.append({
                        'slope': slope_str,
                        'rise': rise,
                        'run': run,
                        'slope_degrees': round(degrees, 2),
                        'x': tx,
                        'y': ty,
                        'detection_method': 'text_' + slope_type,
                        'is_minimum': slope_type == 'min_slope',
                        'confidence': 0.90
                    })
                break  # Only match first pattern per text

    # Method 2: Visual slope triangle detection
    # Look for small right-angle triangles with two number labels nearby
    visual_slopes = detect_slope_triangles_visual(gray, texts, dpi)
    for vs in visual_slopes:
        # Deduplicate against text-detected slopes
        is_dup = any(
            abs(s.get('slope_degrees', 0) - vs.get('slope_degrees', 0)) < 0.5
            for s in slopes
        )
        if not is_dup:
            slopes.append(vs)

    return slopes


def detect_slope_triangles_visual(gray: np.ndarray,
                                   texts: List[TextExtraction],
                                   dpi: int) -> List[Dict]:
    """
    Detect slope triangle symbols visually using contour analysis.

    Slope triangles are small right triangles (typically 0.3-0.8" on paper)
    with two number labels (rise and run) adjacent to the legs.
    """
    import math
    slopes = []
    h, w = gray.shape[:2]

    # Scale parameters by DPI
    min_tri_px = int(0.25 * dpi)  # ~0.25" minimum triangle leg
    max_tri_px = int(1.0 * dpi)   # ~1.0" maximum triangle leg

    # Threshold and find contours
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < (min_tri_px * min_tri_px * 0.3) or area > (max_tri_px * max_tri_px * 0.7):
            continue

        # Approximate contour to polygon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Must be a triangle (3 vertices)
        if len(approx) != 3:
            continue

        pts = approx.reshape(3, 2)

        # Check for right angle (one angle ~90°)
        has_right_angle = False
        right_vertex_idx = -1
        for i in range(3):
            v1 = pts[(i + 1) % 3] - pts[i]
            v2 = pts[(i + 2) % 3] - pts[i]
            dot = np.dot(v1, v2)
            mag1 = np.linalg.norm(v1)
            mag2 = np.linalg.norm(v2)
            if mag1 == 0 or mag2 == 0:
                continue
            cos_angle = dot / (mag1 * mag2)
            cos_angle = np.clip(cos_angle, -1.0, 1.0)
            angle = math.degrees(math.acos(cos_angle))
            if abs(angle - 90) < 15:  # Within 15° of right angle
                has_right_angle = True
                right_vertex_idx = i
                break

        if not has_right_angle or right_vertex_idx < 0:
            continue

        # Get the two legs from the right-angle vertex
        leg1 = pts[(right_vertex_idx + 1) % 3] - pts[right_vertex_idx]
        leg2 = pts[(right_vertex_idx + 2) % 3] - pts[right_vertex_idx]

        # Classify horizontal and vertical legs
        leg1_angle = abs(math.degrees(math.atan2(leg1[1], leg1[0])))
        leg2_angle = abs(math.degrees(math.atan2(leg2[1], leg2[0])))

        # One leg should be roughly horizontal (0° or 180°), one roughly vertical (90°)
        h_leg = None
        v_leg = None
        if (leg1_angle < 30 or leg1_angle > 150) and 60 < leg2_angle < 120:
            h_leg = leg1
            v_leg = leg2
        elif (leg2_angle < 30 or leg2_angle > 150) and 60 < leg1_angle < 120:
            h_leg = leg2
            v_leg = leg1
        else:
            continue  # Not a standard slope triangle orientation

        h_len = np.linalg.norm(h_leg)
        v_len = np.linalg.norm(v_leg)

        if h_len < min_tri_px or v_len < min_tri_px:
            continue

        # Look for number labels near the triangle
        cx = float(np.mean(pts[:, 0]))
        cy = float(np.mean(pts[:, 1]))
        search_radius = max(h_len, v_len) * 1.5

        nearby_numbers = []
        for t in texts:
            tx = (t.bbox[0] + t.bbox[2]) / 2
            ty = (t.bbox[1] + t.bbox[3]) / 2
            dist = math.sqrt((tx - cx) ** 2 + (ty - cy) ** 2)
            if dist < search_radius:
                num_match = re.match(r'^(\d+(?:\.\d+)?(?:/\d+)?)$', t.content.strip())
                if num_match:
                    nearby_numbers.append({
                        'value': t.content.strip(),
                        'x': tx,
                        'y': ty
                    })

        if len(nearby_numbers) >= 2:
            # Classify which number is rise (near vertical leg) and run (near horizontal leg)
            # The vertical leg midpoint
            v_mid_x = float(pts[right_vertex_idx][0] + v_leg[0] / 2)
            v_mid_y = float(pts[right_vertex_idx][1] + v_leg[1] / 2)
            h_mid_x = float(pts[right_vertex_idx][0] + h_leg[0] / 2)
            h_mid_y = float(pts[right_vertex_idx][1] + h_leg[1] / 2)

            rise_num = None
            run_num = None
            for nn in nearby_numbers:
                dist_v = math.sqrt((nn['x'] - v_mid_x) ** 2 + (nn['y'] - v_mid_y) ** 2)
                dist_h = math.sqrt((nn['x'] - h_mid_x) ** 2 + (nn['y'] - h_mid_y) ** 2)
                val_str = nn['value']
                try:
                    if '/' in val_str:
                        parts = val_str.split('/')
                        val = float(parts[0]) / float(parts[1])
                    else:
                        val = float(val_str)
                except (ValueError, ZeroDivisionError):
                    continue

                if dist_v < dist_h:
                    rise_num = val
                else:
                    run_num = val

            if rise_num is not None and run_num is not None and run_num > 0:
                degrees = math.degrees(math.atan(rise_num / run_num))
                slope_str = f"{rise_num}:{run_num}"
                if run_num == 12:
                    slope_str = f"{rise_num}:12"

                slopes.append({
                    'slope': slope_str,
                    'rise': rise_num,
                    'run': run_num,
                    'slope_degrees': round(degrees, 2),
                    'x': cx,
                    'y': cy,
                    'detection_method': 'visual_triangle',
                    'is_minimum': False,
                    'confidence': 0.85
                })

    return slopes


def detect_building_sections(texts: List[TextExtraction],
                              dimensions: List[Dimension],
                              elevations: List[Dict],
                              slopes: List[Dict],
                              scale_ppf: Optional[float],
                              img_h: int, img_w: int) -> List[BuildingSection]:
    """
    Extract building section data from elevation markers and dimensions.

    Building sections are identified by:
    - Presence of foundation-to-roof elevation markers
    - Section title labels ("BUILDING SECTION", "SECTION 1/A-300")
    - Vertical dimension chains spanning multiple levels
    """
    sections = []
    section_idx = 0

    # Group elevation markers by proximity (different sections may be on same sheet)
    elev_groups = group_elevations_by_section(elevations, img_w)

    for group_idx, elev_group in enumerate(elev_groups):
        section_idx += 1
        sect = BuildingSection(
            section_id=f"BSECT-{section_idx}",
            confidence=0.70
        )

        # Build elevation lookup
        elev_lookup = {}
        for e in elev_group:
            label = e.get('label', '').upper()
            val = e.get('elevation_ft')
            if val is not None:
                elev_lookup[label] = val

        # Extract title and section mark from nearby text
        title_info = find_section_title(texts, elev_group, img_h)
        if title_info:
            sect.title = title_info.get('title')
            sect.section_mark = title_info.get('mark')
            sect.cut_line_on_sheet = title_info.get('cut_from_sheet')
            sect.sheet = title_info.get('sheet')

        # Calculate heights from elevation markers
        ffe = None
        for key in ['FFE', 'FINISH FLOOR', 'T.O. SLAB', 'FIN. FLOOR']:
            if key in elev_lookup:
                ffe = elev_lookup[key]
                break

        # Floor-to-floor / floor-to-structure
        for key in ['T.O. STEEL', 'T.O. WALL', 'T.O. PLATE', 'PLATE', 'PLATE HEIGHT',
                     'T.O. JOIST', 'T.O. DECK']:
            if key in elev_lookup and ffe is not None:
                sect.floor_to_floor_ft = round(elev_lookup[key] - ffe, 2)
                sect.measurements.append(SectionMeasurement(
                    label=f"FFE to {key}",
                    value_ft=sect.floor_to_floor_ft,
                    confidence='high'
                ))
                break

        # Foundation depth
        for key in ['B.O. FOOTING', 'B.O. FTG', 'BOTTOM OF FOOTING']:
            if key in elev_lookup and ffe is not None:
                sect.foundation_depth_ft = round(ffe - elev_lookup[key], 2)
                sect.measurements.append(SectionMeasurement(
                    label=f"FFE to {key}",
                    value_ft=sect.foundation_depth_ft,
                    confidence='high'
                ))
                break

        # Footing thickness
        for top_key in ['T.O. FOOTING', 'T.O. FTG']:
            for bot_key in ['B.O. FOOTING', 'B.O. FTG', 'BOTTOM OF FOOTING']:
                if top_key in elev_lookup and bot_key in elev_lookup:
                    thickness_ft = elev_lookup[top_key] - elev_lookup[bot_key]
                    sect.footing_thickness_in = round(thickness_ft * 12, 1)
                    break

        # Ridge height
        for key in ['RIDGE', 'T.O. RIDGE', 'TOP OF RIDGE']:
            if key in elev_lookup and ffe is not None:
                sect.ridge_height_ft = round(elev_lookup[key] - ffe, 2)
                sect.measurements.append(SectionMeasurement(
                    label=f"FFE to {key}",
                    value_ft=sect.ridge_height_ft,
                    confidence='high'
                ))
                break

        # Eave / parapet height
        for key in ['T.O. WALL', 'T.O. PARAPET', 'EAVE', 'PARAPET']:
            if key in elev_lookup and ffe is not None:
                if 'PARAPET' in key:
                    sect.parapet_height_ft = round(elev_lookup[key] - ffe, 2)
                else:
                    sect.eave_height_ft = round(elev_lookup[key] - ffe, 2)

        # Ceiling height
        for key in ['CLG', 'CEILING', 'CLG HT', 'CEILING HEIGHT']:
            if key in elev_lookup and ffe is not None:
                sect.ceiling_height_ft = round(elev_lookup[key] - ffe, 2)
                break

        # Ceiling type from text
        for text in texts:
            content = text.content.strip().upper()
            if 'ACT' in content or 'ACOUSTIC' in content:
                sect.ceiling_type = 'ACT'
                break
            elif 'GWB' in content or 'GYPSUM' in content or 'DRYWALL' in content:
                sect.ceiling_type = 'GWB'
                break
            elif 'EXPOSED' in content:
                sect.ceiling_type = 'exposed'
                break

        # Roof slope from detected slopes
        if slopes:
            # Use the slope closest to this section's elevation group centroid
            group_cx = np.mean([e.get('x', 0) for e in elev_group]) if elev_group else 0
            closest_slope = min(slopes, key=lambda s: abs(s.get('x', 0) - group_cx))
            sect.roof_slope = closest_slope.get('slope')
            sect.roof_slope_degrees = closest_slope.get('slope_degrees', 0)

        # Structural member from text labels
        structural_keywords = {
            'RAFTER': 'rafter', 'TRUSS': 'truss', 'JOIST': 'joist',
            'BEAM': 'beam', 'PURLIN': 'purlin', 'GIRDER': 'girder',
            'PEMB': 'PEMB rafter', 'BAR JOIST': 'bar joist',
            'OPEN WEB': 'open web joist'
        }
        for text in texts:
            content = text.content.strip().upper()
            for kw, member_name in structural_keywords.items():
                if kw in content:
                    sect.structural_member = member_name
                    # Try to extract depth
                    depth_match = re.search(r'(\d+(?:\.\d+)?)\s*[\"″]?\s*(?:DEEP|DEPTH|DP)?', content)
                    if depth_match:
                        sect.structural_depth_in = float(depth_match.group(1))
                    break
            if sect.structural_member:
                break

        # SOG thickness from text or dimensions
        for text in texts:
            content = text.content.strip().upper()
            sog_match = re.search(r'(\d+(?:\.\d+)?)\s*[\"″]\s*(?:SOG|SLAB|CONC\.?\s*SLAB)', content)
            if sog_match:
                sect.sog_thickness_in = float(sog_match.group(1))
                break

        # Only add section if we got meaningful data
        if (sect.floor_to_floor_ft > 0 or sect.foundation_depth_ft > 0 or
                sect.ridge_height_ft > 0 or sect.roof_slope):
            sect.confidence = 0.80 if len(sect.measurements) >= 2 else 0.65
            sections.append(sect)

    return sections


def group_elevations_by_section(elevations: List[Dict], img_w: int) -> List[List[Dict]]:
    """
    Group elevation markers into separate building sections based on horizontal position.
    On a sheet with multiple sections, they are side by side.
    """
    if not elevations:
        return []

    # If only a few markers, treat as one section
    if len(elevations) <= 4:
        return [elevations]

    # Cluster by x-position
    x_positions = np.array([[e.get('x', 0)] for e in elevations])

    if len(x_positions) < 2:
        return [elevations]

    # Use a gap threshold of 1/4 the image width
    gap_threshold = img_w * 0.25
    sorted_indices = np.argsort(x_positions.flatten())

    groups = [[elevations[sorted_indices[0]]]]
    for i in range(1, len(sorted_indices)):
        curr_x = x_positions[sorted_indices[i]][0]
        prev_x = x_positions[sorted_indices[i - 1]][0]
        if curr_x - prev_x > gap_threshold:
            groups.append([])
        groups[-1].append(elevations[sorted_indices[i]])

    return groups


def find_section_title(texts: List[TextExtraction],
                        elev_group: List[Dict],
                        img_h: int) -> Optional[Dict]:
    """
    Find the section title and mark below or near a building section view.
    Section titles are typically at the bottom of the drawing view.
    """
    if not elev_group:
        return None

    # Get the centroid and bottom of the elevation group
    xs = [e.get('x', 0) for e in elev_group]
    ys = [e.get('y', 0) for e in elev_group]
    cx = np.mean(xs)
    max_y = max(ys)

    # Look for title text below the section (within 15% of image height below the lowest marker)
    search_y_min = max_y
    search_y_max = min(max_y + img_h * 0.15, img_h)
    search_x_min = cx - img_h * 0.25
    search_x_max = cx + img_h * 0.25

    result = {}
    for text in texts:
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        if search_y_min <= ty <= search_y_max and search_x_min <= tx <= search_x_max:
            content = text.content.strip()
            # Section title: "BUILDING SECTION - EAST/WEST"
            if re.search(r'(?:BUILDING|WALL|CROSS|LONGITUDINAL|TRANSVERSE)\s+SECTION', content, re.IGNORECASE):
                result['title'] = content
            # Section mark: "1/A-300" or "A" or "1"
            mark_match = re.match(r'^(\d+|[A-Z])\s*/\s*([A-Z]-?\d{3})', content)
            if mark_match:
                result['mark'] = mark_match.group(1)
                result['cut_from_sheet'] = mark_match.group(2)
            # Sheet number from title block area
            sheet_match = re.match(r'^([A-Z]-?\d{3})', content)
            if sheet_match and 'sheet' not in result:
                result['sheet'] = sheet_match.group(1)

    return result if result else None


def detect_wall_sections(image: np.ndarray,
                          texts: List[TextExtraction],
                          dimensions: List[Dimension],
                          lines: List[LineSegment],
                          gray: np.ndarray,
                          scale_ppf: Optional[float],
                          dpi: int,
                          img_h: int, img_w: int) -> List[WallSection]:
    """
    Extract wall section data showing layer-by-layer assembly.

    Wall sections are identified by:
    - Narrow, tall views with multiple hatched layers side by side
    - Material labels with leader lines pointing to layers
    - Layer dimension callouts (5/8\", 3-5/8\", etc.)
    - Wall type identifiers (Type 1, Type 2, etc.)
    - Fire rating annotations (1-HR, 2-HR)
    """
    wall_sections = []

    # Strategy: Find wall type labels and material callouts, then extract layers
    wall_type_locations = find_wall_type_labels(texts)
    fire_rating_locations = find_fire_rating_labels(texts)
    material_callouts = find_material_callouts(texts)
    layer_dims = find_layer_dimensions(texts)

    # Group material callouts and dimensions by proximity into wall sections
    wall_groups = group_wall_section_elements(
        wall_type_locations, fire_rating_locations,
        material_callouts, layer_dims, img_w, img_h
    )

    for group_idx, group in enumerate(wall_groups):
        ws = WallSection(
            section_id=f"WSECT-{group_idx + 1}",
            wall_type=group.get('wall_type'),
            fire_rating=group.get('fire_rating'),
            confidence=0.70
        )

        # Extract layers from material callouts
        layers = extract_wall_layers(group.get('materials', []),
                                      group.get('layer_dims', []))
        ws.layers = layers

        # Calculate total thickness
        if layers:
            ws.total_thickness_in = round(sum(l.thickness_in for l in layers), 2)

        # Look for total dimension callout
        total_dim = group.get('total_dim')
        if total_dim:
            ws.total_thickness_in = total_dim

        # Extract conditions from text
        conditions = extract_wall_conditions(texts, group)
        ws.base_condition = conditions.get('base')
        ws.top_condition = conditions.get('top')
        ws.head_detail = conditions.get('head')
        ws.sill_detail = conditions.get('sill')

        # Find section title/mark
        title_info = find_section_title(texts, [{'x': group.get('cx', 0), 'y': group.get('cy', 0)}], img_h)
        if title_info:
            ws.section_mark = title_info.get('mark')
            ws.sheet = title_info.get('sheet')

        # Only add if we got at least one layer
        if ws.layers:
            ws.confidence = 0.80 if len(ws.layers) >= 3 else 0.65
            ws.measurements.append(SectionMeasurement(
                label="Total assembly",
                value_in=ws.total_thickness_in,
                confidence='high' if ws.total_thickness_in > 0 else 'low'
            ))
            wall_sections.append(ws)

    return wall_sections


def find_wall_type_labels(texts: List[TextExtraction]) -> List[Dict]:
    """Find wall type labels in the drawing: 'WALL TYPE 4', 'TYPE 2', 'WT-3', etc."""
    results = []
    for text in texts:
        content = text.content.strip()
        match = re.search(r'(?:WALL\s+)?TYPE\s*(\d+[A-Z]?)|WT-?(\d+[A-Z]?)', content, re.IGNORECASE)
        if match:
            wtype = match.group(1) or match.group(2)
            results.append({
                'wall_type': f"Type {wtype}",
                'x': (text.bbox[0] + text.bbox[2]) / 2,
                'y': (text.bbox[1] + text.bbox[3]) / 2
            })
    return results


def find_fire_rating_labels(texts: List[TextExtraction]) -> List[Dict]:
    """Find fire rating labels: '1-HR', '2 HR FIRE', 'UL U305', etc."""
    results = []
    for text in texts:
        content = text.content.strip()
        # Match "1-HR", "2 HR", "1 HOUR"
        match = re.search(r'(\d+)\s*-?\s*(?:HR|HOUR)', content, re.IGNORECASE)
        if match:
            results.append({
                'rating': f"{match.group(1)}-HR",
                'x': (text.bbox[0] + text.bbox[2]) / 2,
                'y': (text.bbox[1] + text.bbox[3]) / 2
            })
        # UL assembly number
        ul_match = re.search(r'UL\s+([A-Z]\d{3})', content, re.IGNORECASE)
        if ul_match:
            results.append({
                'rating': f"UL {ul_match.group(1)}",
                'x': (text.bbox[0] + text.bbox[2]) / 2,
                'y': (text.bbox[1] + text.bbox[3]) / 2
            })
    return results


def find_material_callouts(texts: List[TextExtraction]) -> List[Dict]:
    """
    Find material specification callouts in wall section drawings.
    These are text labels like "5/8\" TYPE X GWB", "R-13 BATT INSULATION", etc.
    """
    results = []
    material_patterns = [
        # GWB / Gypsum board
        (r'(\d+/\d+)\s*[\"″]?\s*(?:TYPE\s+[CX])?\s*(?:GWB|GYPSUM|DRYWALL|SHEETROCK)',
         'gwb', 'interior_finish'),
        # Metal studs
        (r'(\d+[\s-]*\d*/?\d*)\s*[\"″]?\s*(?:\d+\s*GA\.?)?\s*(?:METAL|MTL|STEEL)\s*STUD',
         'metal_stud', 'stud_cavity'),
        # Wood studs
        (r'(\d+)\s*[xX]\s*(\d+)\s*(?:WOOD|WD)\s*STUD',
         'wood_stud', 'stud_cavity'),
        # Insulation - batt
        (r'R-?(\d+)\s*(?:BATT|FIBERGLASS|MINERAL\s*WOOL)',
         'batt_insulation', 'insulation'),
        # Insulation - rigid/foam
        (r'(\d+(?:\.\d+)?)\s*[\"″]?\s*(?:RIGID|FOAM|XPS|EPS|POLYISO|CI)',
         'rigid_insulation', 'insulation'),
        # Sheathing
        (r'(\d+/\d+)\s*[\"″]?\s*(?:PLYWOOD|PLY|OSB|SHEATHING|DENSGLASS)',
         'sheathing', 'sheathing'),
        # Air/weather barrier
        (r'(?:AIR\s*BARRIER|WEATHER\s*BARRIER|WRB|TYVEK|HOUSE\s*WRAP)',
         'air_barrier', 'air_barrier'),
        # Metal panel / siding
        (r'(?:METAL\s*PANEL|MTL\s*PANEL|SIDING|CLADDING)',
         'metal_panel', 'exterior_finish'),
        # Masonry
        (r'(?:CMU|BLOCK|BRICK|MASONRY|STONE\s*VENEER)',
         'masonry', 'exterior_finish'),
        # Vapor barrier
        (r'(?:VAPOR\s*BARRIER|VAPOR\s*RETARDER|VB|6\s*MIL\s*POLY)',
         'vapor_barrier', 'air_barrier'),
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        for pattern, mat_type, position in material_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                # Try to extract thickness from the match
                thickness_in = 0.0
                if mat_type == 'gwb':
                    thickness_in = parse_fraction_inches(match.group(1))
                elif mat_type == 'metal_stud':
                    thickness_in = parse_fraction_inches(match.group(1).replace(' ', ''))
                elif mat_type == 'wood_stud':
                    # 2x4 = 3.5", 2x6 = 5.5"
                    nom_w = int(match.group(1))
                    nom_d = int(match.group(2))
                    thickness_in = nom_d - 0.5  # Nominal to actual
                elif mat_type == 'batt_insulation':
                    r_val = float(match.group(1))
                    # Approximate thickness from R-value (R-3.5/inch for fiberglass)
                    thickness_in = round(r_val / 3.5, 1)
                elif mat_type == 'rigid_insulation':
                    thickness_in = float(match.group(1))
                elif mat_type == 'sheathing':
                    thickness_in = parse_fraction_inches(match.group(1))

                r_value = None
                if mat_type == 'batt_insulation':
                    r_value = float(match.group(1))
                elif mat_type == 'rigid_insulation':
                    # Approximate: R-5/inch for polyiso, R-5/inch XPS
                    r_value = round(thickness_in * 5, 0)

                results.append({
                    'material': content,
                    'material_type': mat_type,
                    'thickness_in': thickness_in,
                    'position': position,
                    'r_value': r_value,
                    'x': tx,
                    'y': ty
                })
                break

    return results


def find_layer_dimensions(texts: List[TextExtraction]) -> List[Dict]:
    """
    Find small dimension callouts typical of wall section layers.
    These are dimension strings like 5/8\", 3-5/8\", 1/2\", etc. that appear
    within or adjacent to wall section details.
    """
    results = []
    # Patterns for layer-scale dimensions (typically < 12")
    layer_dim_pattern = re.compile(
        r'^(\d+(?:\s*-?\s*\d+/\d+)?)\s*[\"″]$'
    )

    for text in texts:
        content = text.content.strip()
        match = layer_dim_pattern.match(content)
        if match:
            val_str = match.group(1).replace(' ', '')
            val_in = parse_fraction_inches(val_str)
            if 0 < val_in <= 12:  # Layer dimensions are typically < 12"
                results.append({
                    'value_in': val_in,
                    'value_str': content,
                    'x': (text.bbox[0] + text.bbox[2]) / 2,
                    'y': (text.bbox[1] + text.bbox[3]) / 2
                })

    return results


def group_wall_section_elements(wall_types: List[Dict],
                                 fire_ratings: List[Dict],
                                 materials: List[Dict],
                                 layer_dims: List[Dict],
                                 img_w: int, img_h: int) -> List[Dict]:
    """
    Group wall section elements (types, ratings, materials, dimensions)
    into distinct wall section views based on spatial proximity.
    """
    if not materials and not wall_types:
        return []

    # Combine all elements with positions
    all_elements = []
    for wt in wall_types:
        all_elements.append({'type': 'wall_type', **wt})
    for fr in fire_ratings:
        all_elements.append({'type': 'fire_rating', **fr})
    for mat in materials:
        all_elements.append({'type': 'material', **mat})
    for ld in layer_dims:
        all_elements.append({'type': 'layer_dim', **ld})

    if not all_elements:
        return []

    # Cluster by x-position (wall sections are arranged horizontally on a sheet)
    x_positions = np.array([[e.get('x', 0)] for e in all_elements])

    # Use gap-based clustering
    gap_threshold = img_w * 0.15  # Wall sections are typically well-separated
    sorted_indices = np.argsort(x_positions.flatten())

    clusters = [[all_elements[sorted_indices[0]]]]
    for i in range(1, len(sorted_indices)):
        curr_x = x_positions[sorted_indices[i]][0]
        prev_x = x_positions[sorted_indices[i - 1]][0]
        if curr_x - prev_x > gap_threshold:
            clusters.append([])
        clusters[-1].append(all_elements[sorted_indices[i]])

    # Build group dictionaries
    groups = []
    for cluster in clusters:
        group = {
            'wall_type': None,
            'fire_rating': None,
            'materials': [],
            'layer_dims': [],
            'total_dim': None,
            'cx': np.mean([e.get('x', 0) for e in cluster]),
            'cy': np.mean([e.get('y', 0) for e in cluster])
        }

        for elem in cluster:
            if elem['type'] == 'wall_type':
                group['wall_type'] = elem.get('wall_type')
            elif elem['type'] == 'fire_rating':
                group['fire_rating'] = elem.get('rating')
            elif elem['type'] == 'material':
                group['materials'].append(elem)
            elif elem['type'] == 'layer_dim':
                group['layer_dims'].append(elem)

        groups.append(group)

    return groups


def extract_wall_layers(materials: List[Dict],
                         layer_dims: List[Dict]) -> List[WallLayer]:
    """
    Build ordered wall layer list from material callouts and dimension values.
    Orders layers from exterior to interior based on x-position.
    """
    layers = []

    if not materials:
        return layers

    # Sort materials by x-position (left to right = exterior to interior typically)
    sorted_mats = sorted(materials, key=lambda m: m.get('x', 0))

    position_order = ['exterior_finish', 'sheathing', 'air_barrier', 'insulation',
                      'stud_cavity', 'interior_finish']

    for mat in sorted_mats:
        layer = WallLayer(
            material=mat.get('material', 'Unknown'),
            thickness_in=mat.get('thickness_in', 0.0),
            position=mat.get('position', 'unknown'),
            r_value=mat.get('r_value'),
            confidence=0.75
        )

        # Try to match with nearby dimension if layer has no thickness
        if layer.thickness_in == 0.0 and layer_dims:
            closest_dim = min(
                layer_dims,
                key=lambda d: abs(d.get('y', 0) - mat.get('y', 0))
            )
            # Only use if reasonably close (within ~1 inch on paper at 300 DPI)
            dist = abs(closest_dim.get('y', 0) - mat.get('y', 0))
            if dist < 300:  # ~1 inch at 300 DPI
                layer.thickness_in = closest_dim.get('value_in', 0.0)

        layers.append(layer)

    return layers


def extract_wall_conditions(texts: List[TextExtraction],
                             group: Dict) -> Dict[str, Optional[str]]:
    """
    Extract base, top, head, and sill conditions from text near a wall section.
    """
    conditions = {
        'base': None,
        'top': None,
        'head': None,
        'sill': None
    }

    cx = group.get('cx', 0)
    cy = group.get('cy', 0)

    for text in texts:
        content = text.content.strip().upper()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        # Only consider text reasonably close to this wall section group
        if abs(tx - cx) > 400:  # ~1.3" at 300 DPI
            continue

        if re.search(r'DEFLECTION\s*TRACK|SLIP\s*TRACK|FIRE\s*SAF', content, re.IGNORECASE):
            conditions['top'] = text.content.strip()
        elif re.search(r'BASE\s*(?:TRIM|COND)|VINYL\s*BASE|RUBBER\s*BASE|SEALANT.*FLOOR', content, re.IGNORECASE):
            conditions['base'] = text.content.strip()
        elif re.search(r'HEAD\s*(?:DETAIL|COND)|AT\s*HEAD', content, re.IGNORECASE):
            conditions['head'] = text.content.strip()
        elif re.search(r'SILL\s*(?:DETAIL|COND)|AT\s*SILL|WINDOW\s*SILL', content, re.IGNORECASE):
            conditions['sill'] = text.content.strip()

    return conditions


# =============================================================================
# Pass 11: RCP (Reflected Ceiling Plan) + MEP System Extraction
# =============================================================================

@dataclass
class CeilingHeightZone:
    """A group of rooms sharing the same ceiling height and type."""
    rooms: List[str]
    ceiling_height_ft: float
    ceiling_type: str  # ACT, GWB, exposed, specialty
    confidence: float = 0.8


@dataclass
class CeilingFixture:
    """A lighting or MEP fixture detected on RCP."""
    tag: str  # Single character or short code (A, B, C, EXIT)
    fixture_type: str  # 2x4_troffer, 2x2_fixture, downlight, exit_sign, etc.
    room: Optional[str] = None
    x: float = 0.0
    y: float = 0.0
    confidence: float = 0.7


@dataclass
class MEPEquipment:
    """MEP equipment tag detected on plan."""
    tag: str  # RTU-1, AHU-2, EF-3, LP-1, etc.
    equipment_type: str  # rooftop_unit, exhaust_fan, panel, etc.
    sheet: Optional[str] = None
    room: Optional[str] = None
    grid_location: Optional[str] = None
    x: float = 0.0
    y: float = 0.0
    confidence: float = 0.8


@dataclass
class DuctSegment:
    """A duct size label detected on mechanical plans."""
    size: str  # "12x8", "10\" RD"
    duct_type: str  # supply, return, exhaust, outside_air
    shape: str  # rectangular, round, flex
    width_in: float = 0.0
    height_in: float = 0.0
    diameter_in: float = 0.0
    x: float = 0.0
    y: float = 0.0
    confidence: float = 0.8


@dataclass
class PipeSegment:
    """A pipe size label detected on plumbing plans."""
    size: str  # "2\"", "4\""
    system: str  # domestic_cold, domestic_hot, sanitary, storm, gas, vent, medical
    material: Optional[str] = None  # copper, CPVC, PVC, cast_iron, SS
    x: float = 0.0
    y: float = 0.0
    confidence: float = 0.8


def extract_rcp_mep(image: np.ndarray, texts: List[TextExtraction],
                     symbols: List[DetectedSymbol] = None,
                     lines: List[LineSegment] = None,
                     scale_ppf: Optional[float] = None,
                     dpi: int = 300) -> Dict[str, Any]:
    """
    Extract RCP ceiling data and MEP system data from plan sheets.

    Detects:
    - Ceiling height zones and ceiling type per room (RCP sheets)
    - Lighting fixture positions and tags (RCP sheets)
    - HVAC diffuser/grille positions (RCP sheets)
    - Duct sizes and routing (M-series sheets)
    - Pipe sizes and systems (P-series sheets)
    - Equipment tags and locations (all MEP sheets)
    - Panel schedule data (E-series sheets)

    Args:
        image: Input image (BGR)
        texts: Extracted text elements from Pass 2
        symbols: Detected symbols from Pass 4 (optional)
        lines: Detected lines from Pass 3 (optional)
        scale_ppf: Pixels per foot from Pass 7
        dpi: Image resolution

    Returns:
        Dict with: sheet_type, ceiling_data, fixtures, equipment, ducts, pipes
    """
    logger.info("Pass 11: RCP + MEP System Extraction")

    result = {
        'sheet_type': 'unknown',
        'ceiling_data': None,
        'fixtures': [],
        'equipment': [],
        'ducts': [],
        'pipes': [],
        'fixture_count': 0,
        'equipment_count': 0,
        'duct_count': 0,
        'pipe_count': 0
    }

    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image.copy()

    # ---- Step 1: Classify sheet type ----
    sheet_type = classify_mep_sheet_type(texts)
    result['sheet_type'] = sheet_type

    if sheet_type == 'unknown':
        logger.info("Sheet does not appear to be RCP or MEP — skipping Pass 11")
        return result

    # ---- Step 2: Extract ceiling data (RCP sheets) ----
    if sheet_type == 'rcp':
        ceiling = extract_ceiling_data(texts, symbols or [], gray, dpi)
        result['ceiling_data'] = ceiling

        fixtures = extract_ceiling_fixtures(texts, symbols or [], gray, dpi)
        result['fixtures'] = [asdict(f) for f in fixtures]
        result['fixture_count'] = len(fixtures)

    # ---- Step 3: Extract equipment tags (all MEP sheets) ----
    equipment = extract_mep_equipment_tags(texts)
    result['equipment'] = [asdict(e) for e in equipment]
    result['equipment_count'] = len(equipment)

    # ---- Step 4: Extract duct sizes (M-series) ----
    if sheet_type in ('mechanical', 'rcp'):
        ducts = extract_duct_sizes(texts)
        result['ducts'] = [asdict(d) for d in ducts]
        result['duct_count'] = len(ducts)

    # ---- Step 5: Extract pipe sizes (P-series) ----
    if sheet_type == 'plumbing':
        pipes = extract_pipe_sizes(texts)
        result['pipes'] = [asdict(p) for p in pipes]
        result['pipe_count'] = len(pipes)

    total = result['fixture_count'] + result['equipment_count'] + result['duct_count'] + result['pipe_count']
    logger.info(f"Sheet type: {sheet_type}, "
                f"fixtures: {result['fixture_count']}, equipment: {result['equipment_count']}, "
                f"ducts: {result['duct_count']}, pipes: {result['pipe_count']}")

    return result


def classify_mep_sheet_type(texts: List[TextExtraction]) -> str:
    """
    Classify a sheet as RCP, mechanical, plumbing, electrical, or unknown.
    Uses sheet number prefix and title block text.
    """
    combined = ' '.join(t.content.upper() for t in texts)

    # RCP detection
    rcp_patterns = [
        r'REFLECTED\s+CEILING',
        r'\bRCP\b',
        r'CEILING\s+PLAN',
    ]
    for p in rcp_patterns:
        if re.search(p, combined):
            return 'rcp'

    # Sheet number-based detection
    sheet_patterns = [
        (r'\b[AM]-?1\d{2}\b.*(?:RCP|CEILING)', 'rcp'),
        (r'\bA-?5\d{2}\b', 'rcp'),
        (r'\bM-?\d{3}\b', 'mechanical'),
        (r'\bP-?\d{3}\b', 'plumbing'),
        (r'\bE-?\d{3}\b', 'electrical'),
        (r'\bFP-?\d{3}\b', 'fire_protection'),
    ]
    for pattern, stype in sheet_patterns:
        if re.search(pattern, combined):
            return stype

    # Keyword-based fallback
    keyword_map = {
        'mechanical': [r'HVAC\s+PLAN', r'MECHANICAL\s+PLAN', r'DUCT\s+LAYOUT', r'DIFFUSER'],
        'plumbing': [r'PLUMBING\s+PLAN', r'PIPING\s+PLAN', r'PLUMBING\s+RISER', r'DRAINAGE'],
        'electrical': [r'ELECTRICAL\s+PLAN', r'POWER\s+PLAN', r'LIGHTING\s+PLAN',
                       r'PANEL\s+SCHEDULE', r'SINGLE\s+LINE'],
    }
    for stype, patterns in keyword_map.items():
        for p in patterns:
            if re.search(p, combined):
                return stype

    return 'unknown'


def extract_ceiling_data(texts: List[TextExtraction],
                          symbols: List[DetectedSymbol],
                          gray: np.ndarray,
                          dpi: int) -> Dict[str, Any]:
    """
    Extract ceiling height zones, ceiling type, grid module, and tile product from RCP.
    """
    ceiling = {
        'grid_type': None,
        'grid_module': None,
        'tile_product': None,
        'height_zones': [],
        'soffits_bulkheads': []
    }

    height_callouts = []
    type_callouts = []

    # ---- Extract height callouts ----
    height_patterns = [
        # "9'-0\" AFF", "10'-0\" A.F.F."
        (r"(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?\s*(?:AFF|A\.?F\.?F\.?)", 'aff'),
        # "CLG @ 10'-0\"", "CLG HT = 9'-6\""
        (r"(?:CLG|CEILING|CL)\s*(?:@|=|HT\s*=?)\s*(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?", 'clg'),
        # "10'-0\" ACT", "9'-0\" GWB"
        (r"(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?\s*(ACT|GWB|GYPSUM|EXPOSED|DRYWALL)", 'typed'),
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        for pattern, ptype in height_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                feet = float(match.group(1))
                inches = parse_fraction_inches(match.group(2))
                height = feet + inches / 12.0

                ctype = None
                if ptype == 'typed':
                    raw_type = match.group(3).upper()
                    if raw_type in ('ACT', 'ACOUSTIC'):
                        ctype = 'ACT'
                    elif raw_type in ('GWB', 'GYPSUM', 'DRYWALL'):
                        ctype = 'GWB'
                    elif raw_type == 'EXPOSED':
                        ctype = 'exposed'

                height_callouts.append({
                    'height_ft': round(height, 2),
                    'ceiling_type': ctype,
                    'x': tx,
                    'y': ty,
                    'room': None  # Will be matched later
                })
                break

    # ---- Detect ceiling type from text if not already found ----
    for text in texts:
        content = text.content.strip().upper()
        if re.search(r'\bACT\b|ACOUSTIC\s+CEILING\s+TILE', content):
            type_callouts.append({'type': 'ACT', 'x': (text.bbox[0] + text.bbox[2]) / 2,
                                  'y': (text.bbox[1] + text.bbox[3]) / 2})
        elif re.search(r'\bGWB\b|GYPSUM\s+BOARD\s+CEILING|DRYWALL\s+CEILING', content):
            type_callouts.append({'type': 'GWB', 'x': (text.bbox[0] + text.bbox[2]) / 2,
                                  'y': (text.bbox[1] + text.bbox[3]) / 2})

    # ---- Detect grid module ----
    for text in texts:
        content = text.content.strip()
        grid_match = re.search(r'(\d+)\s*[\"″x×]\s*(\d+)\s*[\"″]?\s*(?:GRID|MODULE|ACT)', content, re.IGNORECASE)
        if grid_match:
            w_val = grid_match.group(1)
            h_val = grid_match.group(2)
            ceiling['grid_module'] = f"{w_val}\" x {h_val}\""
            ceiling['grid_type'] = f"{int(int(w_val)/12)}x{int(int(h_val)/12)}" if int(w_val) >= 12 else f"{w_val}x{h_val}"
            break

    # ---- Detect tile product ----
    tile_keywords = ['ARMSTRONG', 'USG', 'CERTAINTEED', 'ROCKFON', 'MINERAL FIBER',
                     'FINE FISSURED', 'SECOND LOOK', 'ULTIMA', 'RADAR']
    for text in texts:
        content = text.content.strip()
        for kw in tile_keywords:
            if kw.upper() in content.upper():
                ceiling['tile_product'] = content
                break
        if ceiling['tile_product']:
            break

    # ---- Group height callouts into zones ----
    # Group by unique (height, type) pairs
    zone_map = {}
    for hc in height_callouts:
        key = (hc['height_ft'], hc.get('ceiling_type'))
        if key not in zone_map:
            zone_map[key] = {
                'rooms': [],
                'ceiling_height_ft': hc['height_ft'],
                'ceiling_type': hc.get('ceiling_type') or 'unknown'
            }
        if hc.get('room'):
            zone_map[key]['rooms'].append(hc['room'])

    ceiling['height_zones'] = list(zone_map.values())

    # ---- Detect soffits/bulkheads ----
    for text in texts:
        content = text.content.strip()
        if re.search(r'SOFFIT|BULKHEAD|FUR\s*DOWN|DROP\s*CEIL', content, re.IGNORECASE):
            ceiling['soffits_bulkheads'].append({
                'description': content,
                'x': (text.bbox[0] + text.bbox[2]) / 2,
                'y': (text.bbox[1] + text.bbox[3]) / 2
            })

    return ceiling


def extract_ceiling_fixtures(texts: List[TextExtraction],
                              symbols: List[DetectedSymbol],
                              gray: np.ndarray,
                              dpi: int) -> List[CeilingFixture]:
    """
    Extract lighting fixture positions and tags from RCP.
    Fixtures are identified by single-character tags near geometric symbols.
    """
    fixtures = []
    seen_positions = set()

    # Method 1: Find fixture tags from text — single uppercase letters or short codes
    fixture_tag_pattern = re.compile(r'^([A-Z][A-Z0-9]?)$')

    # Collect all potential fixture tags
    tag_candidates = []
    for text in texts:
        content = text.content.strip()
        if fixture_tag_pattern.match(content) and content not in ('N', 'S', 'E', 'W', 'UP', 'DN'):
            tx = (text.bbox[0] + text.bbox[2]) / 2
            ty = (text.bbox[1] + text.bbox[3]) / 2
            tag_candidates.append({
                'tag': content,
                'x': tx,
                'y': ty
            })

    # Method 2: Look for EXIT signs
    for text in texts:
        content = text.content.strip().upper()
        if 'EXIT' in content:
            tx = (text.bbox[0] + text.bbox[2]) / 2
            ty = (text.bbox[1] + text.bbox[3]) / 2
            pos_key = (round(tx / 20) * 20, round(ty / 20) * 20)
            if pos_key not in seen_positions:
                seen_positions.add(pos_key)
                fixtures.append(CeilingFixture(
                    tag='EXIT',
                    fixture_type='exit_sign',
                    x=tx, y=ty,
                    confidence=0.90
                ))

    # Method 3: Classify tags based on frequency and position patterns
    # Tags that appear multiple times in a regular pattern are likely fixtures
    tag_counts = {}
    for tc in tag_candidates:
        tag_counts[tc['tag']] = tag_counts.get(tc['tag'], 0) + 1

    # Tags appearing 2+ times are likely fixture tags (not one-off labels)
    fixture_tags = {tag for tag, count in tag_counts.items() if count >= 2}

    for tc in tag_candidates:
        if tc['tag'] in fixture_tags:
            pos_key = (round(tc['x'] / 20) * 20, round(tc['y'] / 20) * 20)
            if pos_key not in seen_positions:
                seen_positions.add(pos_key)
                # Classify fixture type by common conventions
                ftype = classify_fixture_type(tc['tag'])
                fixtures.append(CeilingFixture(
                    tag=tc['tag'],
                    fixture_type=ftype,
                    x=tc['x'], y=tc['y'],
                    confidence=0.75
                ))

    return fixtures


def classify_fixture_type(tag: str) -> str:
    """Classify fixture type by tag convention (heuristic)."""
    # Common conventions (vary by project, but these are typical)
    if tag in ('A', 'B'):
        return '2x4_recessed_troffer'
    elif tag in ('C', 'D'):
        return '2x2_recessed_fixture'
    elif tag in ('E', 'F'):
        return 'recessed_downlight'
    elif tag in ('G', 'H'):
        return 'surface_pendant'
    elif tag in ('J', 'K'):
        return 'wall_sconce'
    elif tag == 'EXIT':
        return 'exit_sign'
    else:
        return 'unknown_fixture'


def extract_mep_equipment_tags(texts: List[TextExtraction]) -> List[MEPEquipment]:
    """
    Extract MEP equipment tags from plan sheets.
    Tags follow pattern: 2-4 uppercase letters + optional hyphen + number.
    """
    equipment = []
    seen_tags = set()

    equipment_patterns = {
        r'(RTU-?\d+)': 'rooftop_unit',
        r'(AHU-?\d+)': 'air_handling_unit',
        r'(EF-?\d+)': 'exhaust_fan',
        r'(SF-?\d+)': 'supply_fan',
        r'(VRF-?\d+)': 'vrf_unit',
        r'(ERV-?\d+)': 'energy_recovery_ventilator',
        r'(HP-?\d+)': 'heat_pump',
        r'(FCU-?\d+)': 'fan_coil_unit',
        r'(VAV-?\d+)': 'vav_box',
        r'(WH-?\d+)': 'water_heater',
        r'(HWH-?\d+)': 'hot_water_heater',
        r'(P-?\d+)': 'pump',
        r'(CP-?\d+)': 'circulation_pump',
        r'(GT-?\d+)': 'grease_trap',
        r'(BFP-?\d+)': 'backflow_preventer',
        r'(LP-?\d+[A-Z]?)': 'lighting_panel',
        r'(DP-?\d*[A-Z]?)': 'distribution_panel',
        r'(MDP-?\d*[A-Z]?)': 'main_distribution_panel',
        r'(XFMR-?\d+)': 'transformer',
        r'(ATS-?\d+)': 'automatic_transfer_switch',
        r'(GEN-?\d+)': 'generator',
    }

    for text in texts:
        content = text.content.strip().upper()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        for pattern, etype in equipment_patterns.items():
            match = re.search(pattern, content)
            if match:
                tag = match.group(1)
                if tag not in seen_tags:
                    seen_tags.add(tag)
                    equipment.append(MEPEquipment(
                        tag=tag,
                        equipment_type=etype,
                        x=tx, y=ty,
                        confidence=0.85
                    ))

    return equipment


def extract_duct_sizes(texts: List[TextExtraction]) -> List[DuctSegment]:
    """
    Extract duct size labels from mechanical plans.
    Rectangular: WxH (e.g., 12x8)
    Round: diameter (e.g., 10\" RD, Ø8\")
    """
    ducts = []
    seen_positions = set()

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        # Rectangular duct: "12x8", "24 x 12", "12X8"
        rect_match = re.match(r'^(\d+)\s*[xX×]\s*(\d+)\s*[\"″]?$', content)
        if rect_match:
            w_val = float(rect_match.group(1))
            h_val = float(rect_match.group(2))
            # Must be reasonable duct sizes (4" to 60")
            if 4 <= w_val <= 60 and 4 <= h_val <= 60:
                pos_key = (round(tx / 30) * 30, round(ty / 30) * 30)
                if pos_key not in seen_positions:
                    seen_positions.add(pos_key)
                    ducts.append(DuctSegment(
                        size=f"{int(w_val)}x{int(h_val)}",
                        duct_type='unknown',
                        shape='rectangular',
                        width_in=w_val,
                        height_in=h_val,
                        x=tx, y=ty,
                        confidence=0.85
                    ))
                continue

        # Round duct: "10\" RD", "Ø8\"", "8\" FLEX", "10 RD"
        round_match = re.match(
            r'^[Øø]?\s*(\d+)\s*[\"″]?\s*(?:RD|ROUND|FLEX|DIA|Ø)?$',
            content, re.IGNORECASE
        )
        if round_match:
            dia = float(round_match.group(1))
            if 4 <= dia <= 36:  # Reasonable round duct range
                pos_key = (round(tx / 30) * 30, round(ty / 30) * 30)
                if pos_key not in seen_positions:
                    seen_positions.add(pos_key)
                    shape = 'flex' if 'FLEX' in content.upper() else 'round'
                    ducts.append(DuctSegment(
                        size=f"{int(dia)}\" {'FLEX' if shape == 'flex' else 'RD'}",
                        duct_type='unknown',
                        shape=shape,
                        diameter_in=dia,
                        x=tx, y=ty,
                        confidence=0.80
                    ))

    # Try to classify duct type from nearby text (SA, RA, EA, OA labels)
    duct_type_patterns = {
        r'\bSA\b|SUPPLY\s*AIR': 'supply',
        r'\bRA\b|RETURN\s*AIR': 'return',
        r'\bEA\b|EXHAUST\s*AIR': 'exhaust',
        r'\bOA\b|OUTSIDE\s*AIR|FRESH\s*AIR': 'outside_air',
    }

    for duct in ducts:
        for text in texts:
            tx = (text.bbox[0] + text.bbox[2]) / 2
            ty = (text.bbox[1] + text.bbox[3]) / 2
            dist = ((tx - duct.x) ** 2 + (ty - duct.y) ** 2) ** 0.5
            if dist < 200:  # ~0.67" at 300 DPI
                content = text.content.strip().upper()
                for pattern, dtype in duct_type_patterns.items():
                    if re.search(pattern, content):
                        duct.duct_type = dtype
                        break
            if duct.duct_type != 'unknown':
                break

    return ducts


def extract_pipe_sizes(texts: List[TextExtraction]) -> List[PipeSegment]:
    """
    Extract pipe size labels from plumbing plans.
    Format: size + system abbreviation (e.g., "2\" CW", "4\" SAN")
    """
    pipes = []
    seen_positions = set()

    # System abbreviation mapping
    system_map = {
        'CW': 'domestic_cold', 'DCW': 'domestic_cold', 'CWS': 'domestic_cold',
        'HW': 'domestic_hot', 'DHW': 'domestic_hot', 'HWS': 'domestic_hot',
        'HWR': 'domestic_hot_return',
        'SAN': 'sanitary', 'S': 'sanitary', 'SS': 'sanitary',
        'SD': 'storm', 'ST': 'storm', 'STORM': 'storm', 'RD': 'storm',
        'G': 'gas', 'NG': 'gas', 'GAS': 'gas',
        'V': 'vent', 'VTR': 'vent', 'VENT': 'vent',
        'O2': 'medical_oxygen', 'VAC': 'medical_vacuum',
        'N2O': 'medical_nitrous', 'MG': 'medical_gas',
        'CO2': 'medical_co2', 'N2': 'medical_nitrogen',
        'CWR': 'chilled_water_return', 'CHWS': 'chilled_water_supply',
    }

    abbrev_list = '|'.join(sorted(system_map.keys(), key=len, reverse=True))

    # Pattern: size + system (e.g., "2\" CW", "4\" SAN", "3/4\" HW")
    pipe_pattern = re.compile(
        rf'^(\d+(?:/\d+)?)\s*[\"″]?\s*({abbrev_list})$',
        re.IGNORECASE
    )

    # Also match: system + size (e.g., "CW 2\"", "SAN 4\"")
    pipe_pattern_rev = re.compile(
        rf'^({abbrev_list})\s*(\d+(?:/\d+)?)\s*[\"″]?$',
        re.IGNORECASE
    )

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2

        match = pipe_pattern.match(content)
        match_rev = pipe_pattern_rev.match(content) if not match else None

        if match:
            size_str = match.group(1)
            abbrev = match.group(2).upper()
        elif match_rev:
            abbrev = match_rev.group(1).upper()
            size_str = match_rev.group(2)
        else:
            continue

        system = system_map.get(abbrev, 'unknown')

        pos_key = (round(tx / 30) * 30, round(ty / 30) * 30)
        if pos_key not in seen_positions:
            seen_positions.add(pos_key)
            pipes.append(PipeSegment(
                size=f"{size_str}\"",
                system=system,
                x=tx, y=ty,
                confidence=0.85
            ))

    # Try to detect pipe material from nearby text
    material_patterns = {
        r'\bCOPPER\b|TYPE\s*[LMK]': 'copper',
        r'\bCPVC\b': 'CPVC',
        r'\bPVC\b': 'PVC',
        r'\bCAST\s*IRON\b|CI\b': 'cast_iron',
        r'\bSS\b|STAINLESS': 'stainless_steel',
        r'\bHDPE\b': 'HDPE',
        r'\bDUCTILE\s*IRON\b|DI\b': 'ductile_iron',
    }

    for pipe in pipes:
        for text in texts:
            tx = (text.bbox[0] + text.bbox[2]) / 2
            ty = (text.bbox[1] + text.bbox[3]) / 2
            dist = ((tx - pipe.x) ** 2 + (ty - pipe.y) ** 2) ** 0.5
            if dist < 300:  # ~1" at 300 DPI
                content = text.content.strip().upper()
                for pattern, material in material_patterns.items():
                    if re.search(pattern, content):
                        pipe.material = material
                        break
            if pipe.material:
                break

    return pipes


# =============================================================================
# Pass 12: Exterior Elevation + Accessibility Extraction
# =============================================================================

@dataclass
class ElevationMaterial:
    """A material zone on an exterior elevation."""
    zone: str  # primary_cladding, accent, base, trim, roof
    material: str  # Metal panels, CMU, brick, etc.
    color: Optional[str] = None
    mfg_code: Optional[str] = None
    height_ft: float = 0.0  # For base/accent zones
    confidence: float = 0.7


@dataclass
class ElevationOpening:
    """A window or door position on an exterior elevation."""
    mark: str  # W-101, 101, etc.
    opening_type: str  # window, door, storefront
    sill_height_ft: float = 0.0
    head_height_ft: float = 0.0
    width_ft: float = 0.0
    x: float = 0.0
    y: float = 0.0
    confidence: float = 0.7


@dataclass
class AccessibilityItem:
    """An accessibility feature detected on plans."""
    item_type: str  # route, restroom, ramp, signage, parking, counter
    location: Optional[str] = None
    room: Optional[str] = None
    compliant: bool = True
    details: Dict[str, Any] = None
    x: float = 0.0
    y: float = 0.0
    confidence: float = 0.7

    def __post_init__(self):
        if self.details is None:
            self.details = {}


def extract_elevations_accessibility(image: np.ndarray,
                                      texts: List[TextExtraction],
                                      lines: List[LineSegment] = None,
                                      dimensions: List[Dimension] = None,
                                      scale_ppf: Optional[float] = None,
                                      dpi: int = 300) -> Dict[str, Any]:
    """
    Extract exterior elevation data and accessibility annotations.

    Elevation sheets: material zones, window/door positions, grade line, heights.
    Floor plans: accessible routes, ADA restroom clearances, ramps, signage.

    Args:
        image: Input image (BGR)
        texts: Extracted text elements from Pass 2
        lines: Detected line segments from Pass 3 (optional)
        dimensions: Extracted dimensions from Pass 6 (optional)
        scale_ppf: Pixels per foot from Pass 7
        dpi: Image resolution

    Returns:
        Dict with: sheet_type, elevation_data, accessibility_items
    """
    logger.info("Pass 12: Exterior Elevation + Accessibility Extraction")

    result = {
        'sheet_type': 'unknown',
        'elevation_data': None,
        'accessibility_items': [],
        'elevation_count': 0,
        'accessibility_count': 0
    }

    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image.copy()

    # ---- Step 1: Detect if this is an elevation sheet ----
    is_elevation = detect_elevation_sheet(texts)
    if is_elevation:
        result['sheet_type'] = 'elevation'
        elev_data = extract_elevation_data(texts, lines or [], dimensions or [], scale_ppf, h, w)
        result['elevation_data'] = elev_data
        result['elevation_count'] = len(elev_data) if isinstance(elev_data, list) else 1

    # ---- Step 2: Extract accessibility data (any plan sheet) ----
    access_items = extract_accessibility_data(texts, dimensions or [], scale_ppf)
    result['accessibility_items'] = [asdict(a) for a in access_items]
    result['accessibility_count'] = len(access_items)

    logger.info(f"Elevation sheet: {is_elevation}, "
                f"elevations: {result['elevation_count']}, "
                f"accessibility items: {result['accessibility_count']}")

    return result


def detect_elevation_sheet(texts: List[TextExtraction]) -> bool:
    """Detect if this sheet contains exterior elevations."""
    combined = ' '.join(t.content.upper() for t in texts)

    elevation_patterns = [
        r'(?:NORTH|SOUTH|EAST|WEST|FRONT|REAR|LEFT|RIGHT)\s+ELEVATION',
        r'EXTERIOR\s+ELEVATION',
        r'BUILDING\s+ELEVATION',
    ]
    for p in elevation_patterns:
        if re.search(p, combined):
            return True

    # Sheet number: A-200 series
    if re.search(r'\bA-?2\d{2}\b', combined):
        return True

    return False


def extract_elevation_data(texts: List[TextExtraction],
                            lines: List[LineSegment],
                            dimensions: List[Dimension],
                            scale_ppf: Optional[float],
                            img_h: int, img_w: int) -> List[Dict]:
    """
    Extract material zones, openings, and heights from exterior elevation views.
    A sheet may contain multiple elevation views (N, S, E, W).
    """
    elevations = []

    # Find elevation face labels
    face_locations = find_elevation_faces(texts, img_h, img_w)

    if not face_locations:
        # Try a single unnamed elevation
        face_locations = [{'face': 'Unknown', 'cx': img_w / 2, 'cy': img_h / 2}]

    for face_info in face_locations:
        elev = {
            'face': face_info['face'],
            'materials': [],
            'grade_line_elevation_ft': None,
            'window_positions': [],
            'door_positions': [],
            'measurements': []
        }

        cx = face_info.get('cx', img_w / 2)
        cy = face_info.get('cy', img_h / 2)

        # Extract materials from nearby text
        materials = extract_elevation_materials(texts, cx, cy, img_w)
        elev['materials'] = [asdict(m) for m in materials]

        # Extract grade line
        grade_elev = find_grade_line_elevation(texts, cx, cy)
        elev['grade_line_elevation_ft'] = grade_elev

        # Extract window/door positions
        openings = extract_elevation_openings(texts, cx, cy, img_w)
        for op in openings:
            if op.opening_type == 'window':
                elev['window_positions'].append(asdict(op))
            else:
                elev['door_positions'].append(asdict(op))

        # Extract height measurements
        heights = extract_elevation_heights(texts, dimensions, cx, cy, img_w)
        elev['measurements'] = heights

        elevations.append(elev)

    return elevations


def find_elevation_faces(texts: List[TextExtraction],
                          img_h: int, img_w: int) -> List[Dict]:
    """Find elevation face labels (NORTH, SOUTH, EAST, WEST) and their positions."""
    faces = []
    face_pattern = re.compile(
        r'(NORTH|SOUTH|EAST|WEST|FRONT|REAR|LEFT|RIGHT)\s+ELEV',
        re.IGNORECASE
    )

    for text in texts:
        match = face_pattern.search(text.content.strip())
        if match:
            direction = match.group(1).upper()
            # Map aliases
            if direction == 'FRONT':
                direction = 'SOUTH'  # Convention varies, but front is commonly south
            elif direction == 'REAR':
                direction = 'NORTH'

            tx = (text.bbox[0] + text.bbox[2]) / 2
            ty = (text.bbox[1] + text.bbox[3]) / 2

            faces.append({
                'face': direction,
                'cx': tx,
                'cy': ty - img_h * 0.2  # Title is usually below the view
            })

    return faces


def extract_elevation_materials(texts: List[TextExtraction],
                                 cx: float, cy: float,
                                 img_w: int) -> List[ElevationMaterial]:
    """Extract material zone labels from elevation view text."""
    materials = []
    search_radius = img_w * 0.4

    material_patterns = [
        # Metal panels
        (r'(?:METAL|MTL)\s+PANEL', 'Metal panels', 'primary_cladding'),
        (r'STANDING\s+SEAM', 'Standing seam metal', 'roof'),
        # Masonry
        (r'(?:SPLIT[\s-]*FACE\s+)?CMU', 'CMU', 'primary_cladding'),
        (r'BRICK', 'Brick', 'primary_cladding'),
        (r'STONE\s+VENEER', 'Stone veneer', 'accent'),
        # Other
        (r'STUCCO|EIFS', 'EIFS/Stucco', 'primary_cladding'),
        (r'(?:LAP|BOARD)\s+(?:SIDING|&\s*BATTEN)', 'Siding', 'primary_cladding'),
        (r'FIBER\s+CEMENT', 'Fiber cement', 'primary_cladding'),
        # Trim/fascia
        (r'(?:ALUMINUM|ALUM\.?|MTL)\s+(?:TRIM|FASCIA|COPING)', 'Aluminum trim', 'trim'),
        (r'SOFFIT', 'Soffit', 'trim'),
        # Roof
        (r'(?:ASPHALT|ARCH)\s+SHINGLE', 'Asphalt shingles', 'roof'),
        (r'TPO|EPDM|MEMBRANE', 'Roofing membrane', 'roof'),
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        dist = ((tx - cx) ** 2 + (ty - cy) ** 2) ** 0.5

        if dist > search_radius:
            continue

        for pattern, material_name, zone in material_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                # Try to extract color
                color = extract_color_from_text(content)
                mfg = extract_mfg_code(content)

                materials.append(ElevationMaterial(
                    zone=zone,
                    material=material_name,
                    color=color,
                    mfg_code=mfg,
                    confidence=0.80
                ))
                break

    return materials


def extract_color_from_text(text: str) -> Optional[str]:
    """Extract color/finish description from material callout text."""
    color_patterns = [
        r'((?:CHAMPAGNE|TAN|BEIGE|BRONZE|WHITE|BLACK|GRAY|GREY|CHARCOAL|'
        r'CREAM|IVORY|SAND|STONE|SLATE|PEWTER|SILVER|DARK\s+BRONZE|'
        r'WARM\s+GRAY|COOL\s+GRAY|BONE|ALMOND|TAUPE)\s*(?:TAN|FINISH)?)',
        r'(?:COLOR|FINISH|CLR)\s*[:#=]\s*([^\n,]+)',
    ]
    for pattern in color_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def extract_mfg_code(text: str) -> Optional[str]:
    """Extract manufacturer code from material callout."""
    mfg_patterns = [
        r'(?:NUCOR|KINGSPAN|CENTRIA|MBCI|BERRIDGE)\s+(?:COLOR\s+)?(?:CODE\s+)?(\S+)',
        r'(?:SW|SHERWIN)\s*(\d{4})',
        r'(?:COLOR|CLR)\s*#?\s*(\d+[\w-]*)',
    ]
    for pattern in mfg_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0).strip()
    return None


def find_grade_line_elevation(texts: List[TextExtraction],
                               cx: float, cy: float) -> Optional[float]:
    """Find the finished grade elevation from elevation view text."""
    grade_patterns = [
        r'(?:F\.?G\.?|FIN\.?\s*GRADE|GRADE|FINISH\s+GRADE)\s*[=:@]\s*(\d+)[\'.-]\s*(\d+(?:\s*\d*/\d+)?)[\"″]?',
        r'(?:EL\.?\s*)?(\d{3})\s*[\'.-]\s*(\d+)[\"″]?\s*(?:F\.?G\.?|GRADE)',
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        dist = abs(tx - cx)
        if dist > 800:  # Reasonable proximity
            continue

        for pattern in grade_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                feet = float(match.group(1))
                inches = parse_fraction_inches(match.group(2))
                return round(feet + inches / 12.0, 2)

    return None


def extract_elevation_openings(texts: List[TextExtraction],
                                cx: float, cy: float,
                                img_w: int) -> List[ElevationOpening]:
    """Extract window and door mark positions from elevation views."""
    openings = []
    seen_marks = set()
    search_radius = img_w * 0.4

    # Window marks: W-101, W101, WN-1, etc.
    window_pattern = re.compile(r'^(W[ND]?-?\d+[A-Z]?)$', re.IGNORECASE)
    # Door marks: 101, D-101, DR-1, etc.
    door_pattern = re.compile(r'^(D[R]?-?\d+[A-Z]?|\d{3}[A-Z]?)$', re.IGNORECASE)
    # Storefront: SF-1, GL-1, etc.
    storefront_pattern = re.compile(r'^(SF-?\d+|GL-?\d+|STOREFRONT)$', re.IGNORECASE)

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        dist = ((tx - cx) ** 2 + (ty - cy) ** 2) ** 0.5

        if dist > search_radius:
            continue

        mark = None
        otype = None

        if window_pattern.match(content):
            mark = content.upper()
            otype = 'window'
        elif storefront_pattern.match(content):
            mark = content.upper()
            otype = 'storefront'
        elif door_pattern.match(content):
            mark = content.upper()
            otype = 'door'

        if mark and mark not in seen_marks:
            seen_marks.add(mark)
            openings.append(ElevationOpening(
                mark=mark,
                opening_type=otype,
                x=tx, y=ty,
                confidence=0.80
            ))

    return openings


def extract_elevation_heights(texts: List[TextExtraction],
                               dimensions: List[Dimension],
                               cx: float, cy: float,
                               img_w: int) -> List[Dict]:
    """Extract height measurements from elevation views."""
    heights = []
    seen_labels = set()

    height_patterns = [
        (r'(?:GRADE|FG)\s+TO\s+(?:EAVE|T\.?O\.?\s*WALL)', 'Grade to eave'),
        (r'(?:GRADE|FG)\s+TO\s+(?:RIDGE|T\.?O\.?\s*RIDGE)', 'Grade to ridge'),
        (r'(?:GRADE|FG)\s+TO\s+(?:PARAPET|T\.?O\.?\s*PARAPET)', 'Grade to parapet'),
        (r'(?:FLOOR|FFE)\s+TO\s+(?:FLOOR|CEILING|CLG)', 'Floor to floor'),
        (r'(?:T\.?O\.?\s*(?:WALL|STEEL|PLATE|PARAPET|RIDGE))', None),  # Named elevation
    ]

    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        dist = abs(tx - cx)

        if dist > img_w * 0.35:
            continue

        for pattern, default_label in height_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                label = default_label or match.group(0).strip()
                if label in seen_labels:
                    continue

                # Look for an associated dimension value
                dim_match = re.search(r"(\d+)['\-][\s-]*(\d+(?:\s*\d*/\d+)?)[\"″]?", content)
                if dim_match:
                    feet = float(dim_match.group(1))
                    inches = parse_fraction_inches(dim_match.group(2))
                    value_ft = round(feet + inches / 12.0, 2)

                    seen_labels.add(label)
                    heights.append({
                        'label': label,
                        'value_ft': value_ft,
                        'confidence': 'high'
                    })

    return heights


def extract_accessibility_data(texts: List[TextExtraction],
                                dimensions: List[Dimension],
                                scale_ppf: Optional[float]) -> List[AccessibilityItem]:
    """
    Extract accessibility annotations from floor plans and site plans.
    Includes: accessible routes, ADA restroom clearances, ramps, signage, parking, counters.
    """
    items = []

    # ---- 1. Accessible route annotations ----
    route_patterns = [
        r'ACCESSIBLE\s+ROUTE',
        r'PATH\s+OF\s+TRAVEL',
        r'BARRIER[\s-]FREE\s+ROUTE',
    ]
    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        for pattern in route_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                items.append(AccessibilityItem(
                    item_type='route',
                    location=content,
                    x=tx, y=ty,
                    details={'description': content},
                    confidence=0.85
                ))
                break

    # ---- 2. ADA restroom annotations ----
    ada_restroom_patterns = [
        (r'(?:60|1524)\s*[\"″mm]*\s*(?:TURNING|TURN)\s*(?:RADIUS|CIRCLE|DIAM)', 'turning_radius'),
        (r'18\s*[\"″]\s*(?:TO\s+)?(?:CL|CENTERLINE|C/?L)', 'wc_centerline'),
        (r'(?:GRAB\s+BAR|GB)\s*(?:\d+[\"″])?', 'grab_bar'),
        (r'(?:CLEAR\s+FLOOR|CLR\s+FLR)\s*(?:SPACE)?.*?30\s*[\"″x×]\s*48', 'clear_floor'),
    ]
    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        for pattern, ada_type in ada_restroom_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                items.append(AccessibilityItem(
                    item_type='restroom',
                    location=content,
                    x=tx, y=ty,
                    details={'ada_feature': ada_type, 'description': content},
                    confidence=0.85
                ))
                break

    # ---- 3. Ramp annotations ----
    ramp_patterns = [
        (r'(?:ADA\s+)?RAMP', 'ramp'),
        (r'(?:SLOPE|GRADE)\s*[=:]\s*1\s*:\s*(\d+)', 'slope'),
        (r'(\d+(?:\.\d+)?)\s*%\s*(?:MAX|SLOPE)', 'slope_pct'),
    ]
    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        for pattern, ramp_type in ramp_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                details = {'description': content}
                if ramp_type == 'slope' and match.lastindex:
                    run = float(match.group(1))
                    details['slope'] = f"1:{int(run)}"
                    details['compliant'] = run >= 12
                elif ramp_type == 'slope_pct' and match.lastindex:
                    pct = float(match.group(1))
                    details['slope_pct'] = pct
                    details['compliant'] = pct <= 8.33

                items.append(AccessibilityItem(
                    item_type='ramp',
                    location=content,
                    x=tx, y=ty,
                    details=details,
                    confidence=0.80
                ))
                break

    # ---- 4. Signage annotations ----
    signage_patterns = [
        r'BRAILLE|TACTILE\s+SIGN',
        r'(?:ROOM|DOOR)\s+SIGN',
        r'(?:ADA|ACCESSIBLE)\s+SIGN',
    ]
    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        for pattern in signage_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                # Try to extract mounting height
                height_match = re.search(r'(\d+)\s*[\"″]\s*(?:AFF|A\.?F\.?F\.?)', content)
                details = {'description': content}
                if height_match:
                    details['mounting_height_in'] = int(height_match.group(1))

                items.append(AccessibilityItem(
                    item_type='signage',
                    location=content,
                    x=tx, y=ty,
                    details=details,
                    confidence=0.85
                ))
                break

    # ---- 5. Accessible parking annotations ----
    parking_patterns = [
        r'(?:VAN\s+)?ACCESSIBLE\s+(?:PARKING|STALL|SPACE)',
        r'(?:HC|HANDICAP|ISA)\s+(?:PARKING|STALL|SPACE)',
        r'ACCESS\s+AISLE',
    ]
    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        for pattern in parking_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                details = {'description': content}
                details['van_accessible'] = bool(re.search(r'VAN', content, re.IGNORECASE))

                items.append(AccessibilityItem(
                    item_type='parking',
                    location=content,
                    x=tx, y=ty,
                    details=details,
                    confidence=0.85
                ))
                break

    # ---- 6. Counter height annotations ----
    counter_patterns = [
        r'(?:ADA|ACCESSIBLE)\s+COUNTER',
        r'(?:TRANSACTION|SERVICE)\s+COUNTER.*?(\d+)\s*[\"″]',
        r'(?:KNEE|CLEAR)\s+(?:SPACE|CLEARANCE).*?(\d+)\s*[\"″]',
    ]
    for text in texts:
        content = text.content.strip()
        tx = (text.bbox[0] + text.bbox[2]) / 2
        ty = (text.bbox[1] + text.bbox[3]) / 2
        for pattern in counter_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                details = {'description': content}
                if match.lastindex:
                    details['height_in'] = int(match.group(1))

                items.append(AccessibilityItem(
                    item_type='counter',
                    location=content,
                    x=tx, y=ty,
                    details=details,
                    confidence=0.80
                ))
                break

    return items


# =============================================================================
# Pass 13: Hatch Pattern Refinement + Keynote Extraction
# =============================================================================

@dataclass
class RefinedHatch:
    """Refined material zone with hatch angle/density analysis."""
    zone_index: int  # Index into Pass 5 material_zones
    hatch_angles_deg: List[float]  # Dominant line angles
    hatch_spacing_px: float  # Average inter-line spacing in pixels
    hatch_density_lpi: float  # Lines per inch (from scale calibration)
    hatch_pattern: str  # ANSI/standard code
    refined_material: str  # Refined material type
    context: str  # "section_cut" or "plan_view"
    material_label: str  # Adjacent text label, if found
    legend_match: bool  # Whether matched to a legend entry
    confidence: float


@dataclass
class KeynoteCallout:
    """A keynote bubble callout on a drawing sheet."""
    keynote_number: str
    bubble_center: Tuple[float, float]
    bubble_radius: float
    leader_endpoint: Optional[Tuple[float, float]]
    points_to_element: Optional[str]
    points_to_type: Optional[str]


@dataclass
class KeynoteScheduleEntry:
    """An entry in a keynote schedule table."""
    number: str
    description: str
    spec_section: Optional[str]
    sheet_source: str


@dataclass
class GeneralNote:
    """A numbered general note from a notes block."""
    note_number: str
    text: str
    category: str  # dimensions, materials, installation, code, coordination, general
    spec_refs: List[str]


def extract_hatch_keynotes(image: np.ndarray,
                           texts: List[TextExtraction],
                           material_zones: List[Dict],
                           lines: Optional[List] = None,
                           symbols: Optional[List] = None,
                           scale_ppf: Optional[float] = None,
                           zones: Optional[List[Dict]] = None,
                           dpi: int = 300) -> Dict[str, Any]:
    """
    Pass 13: Refine material zone hatch classification and extract keynotes.

    Args:
        image: Input image (BGR)
        texts: OCR text extractions from Pass 2
        material_zones: Pass 5 material zone results (list of dicts)
        lines: Line segments from Pass 3
        symbols: Symbol detections from Pass 4
        scale_ppf: Pixels per foot from Pass 7
        zones: Sheet layout zones from Pass 1
        dpi: Image DPI

    Returns:
        Dict with refined_zones, keynotes, general_notes
    """
    logger.info("Pass 13: Hatch Refinement + Keynote Extraction")

    result = {
        'refined_zones': [],
        'refined_count': 0,
        'keynote_callouts': [],
        'keynote_schedule': [],
        'general_notes': [],
        'keynote_count': 0,
        'general_note_count': 0
    }

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # --- Part A: Hatch Refinement ---
    refined = refine_hatch_zones(gray, material_zones, texts, scale_ppf, dpi)
    result['refined_zones'] = [asdict(r) for r in refined]
    result['refined_count'] = len(refined)

    # --- Part B: Keynote Extraction ---
    callouts = detect_keynote_bubbles(image, gray, texts, lines, symbols)
    result['keynote_callouts'] = [asdict(c) for c in callouts]
    result['keynote_count'] = len(callouts)

    schedule = extract_keynote_schedule(texts, zones)
    result['keynote_schedule'] = [asdict(s) for s in schedule]

    # --- Part C: General Notes ---
    notes = extract_general_notes(texts, zones)
    result['general_notes'] = [asdict(n) for n in notes]
    result['general_note_count'] = len(notes)

    logger.info(f"Pass 13 complete: {len(refined)} refined zones, "
                f"{len(callouts)} keynotes, {len(schedule)} schedule entries, "
                f"{len(notes)} general notes")
    return result


def refine_hatch_zones(gray: np.ndarray,
                       material_zones: List[Dict],
                       texts: List[TextExtraction],
                       scale_ppf: Optional[float],
                       dpi: int) -> List[RefinedHatch]:
    """
    Refine Pass 5 material zones using Hough line analysis within each zone.
    """
    refined = []
    height, width = gray.shape

    for idx, zone in enumerate(material_zones):
        bbox = zone.get('bbox', [0, 0, 0, 0])
        if len(bbox) != 4:
            continue

        x1, y1, x2, y2 = [int(v) for v in bbox]
        # Clamp to image bounds
        x1 = max(0, min(x1, width - 1))
        y1 = max(0, min(y1, height - 1))
        x2 = max(x1 + 1, min(x2, width))
        y2 = max(y1 + 1, min(y2, height))

        if (x2 - x1) < 10 or (y2 - y1) < 10:
            continue

        # Extract zone ROI
        roi = gray[y1:y2, x1:x2]

        # Detect lines within zone
        angles, spacing_px = analyze_hatch_lines(roi)

        # Classify pattern from angles
        pattern, material = classify_hatch_from_angles(angles)

        # Calculate density (lines per inch)
        density_lpi = 0.0
        if spacing_px > 0 and scale_ppf and scale_ppf > 0:
            spacing_ft = spacing_px / scale_ppf
            spacing_in = spacing_ft * 12.0
            if spacing_in > 0:
                density_lpi = 1.0 / spacing_in
        elif spacing_px > 0:
            # Fallback: use DPI
            spacing_in = spacing_px / (dpi / 1.0)
            if spacing_in > 0:
                density_lpi = 1.0 / spacing_in

        # Determine context (section vs plan view)
        context = determine_hatch_context(zone)

        # Find adjacent material label
        label = find_adjacent_label(x1, y1, x2, y2, texts)

        # If label found, use it to refine material type
        if label:
            label_material = material_from_label(label)
            if label_material:
                material = label_material

        # Override original classification if we have a confident refined one
        orig_material = zone.get('material_type', 'unknown')
        if material == 'unknown':
            material = orig_material

        confidence = 0.8
        if label:
            confidence = 0.9
        if len(angles) == 0:
            confidence = 0.5

        rh = RefinedHatch(
            zone_index=idx,
            hatch_angles_deg=angles,
            hatch_spacing_px=spacing_px,
            hatch_density_lpi=round(density_lpi, 1),
            hatch_pattern=pattern,
            refined_material=material,
            context=context,
            material_label=label or '',
            legend_match=False,  # Legend matching requires sheet-specific legend detection
            confidence=confidence
        )
        refined.append(rh)

    return refined


def analyze_hatch_lines(roi: np.ndarray) -> Tuple[List[float], float]:
    """
    Analyze line angles and spacing within a hatch zone ROI.

    Returns:
        Tuple of (dominant_angles_deg, average_spacing_px)
    """
    if roi.size == 0:
        return [], 0.0

    # Edge detection
    edges = cv2.Canny(roi, 50, 150)

    # Hough line detection
    lines_p = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=15,
                               minLineLength=15, maxLineGap=5)

    if lines_p is None or len(lines_p) == 0:
        return [], 0.0

    # Calculate angles of all detected lines
    all_angles = []
    for line in lines_p:
        x1, y1, x2, y2 = line[0]
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) < 1 and abs(dy) < 1:
            continue
        angle_rad = np.arctan2(abs(dy), abs(dx))
        angle_deg = np.degrees(angle_rad)
        # Normalize to 0-180 range
        angle_deg = angle_deg % 180
        all_angles.append(angle_deg)

    if not all_angles:
        return [], 0.0

    # Build histogram with 5-degree bins
    bins = np.arange(0, 185, 5)
    hist, edges_h = np.histogram(all_angles, bins=bins)

    # Find dominant angles (peaks with >15% of lines)
    threshold_count = len(all_angles) * 0.15
    dominant = []
    for i, count in enumerate(hist):
        if count >= threshold_count:
            center_angle = (edges_h[i] + edges_h[i + 1]) / 2
            dominant.append(round(center_angle, 1))

    # Calculate average spacing between parallel lines
    spacing = calculate_line_spacing(lines_p, dominant[0] if dominant else 45.0)

    return dominant, spacing


def calculate_line_spacing(lines_p: np.ndarray, dominant_angle: float) -> float:
    """
    Calculate average perpendicular spacing between parallel lines.
    """
    if lines_p is None or len(lines_p) < 2:
        return 0.0

    # Project line midpoints onto the perpendicular axis
    perp_angle_rad = np.radians(dominant_angle + 90)
    perp_cos = np.cos(perp_angle_rad)
    perp_sin = np.sin(perp_angle_rad)

    projections = []
    for line in lines_p:
        x1, y1, x2, y2 = line[0]
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        proj = mx * perp_cos + my * perp_sin
        projections.append(proj)

    if len(projections) < 2:
        return 0.0

    projections.sort()
    spacings = []
    for i in range(1, len(projections)):
        s = projections[i] - projections[i - 1]
        if s > 2:  # Minimum meaningful spacing
            spacings.append(s)

    if spacings:
        return float(np.median(spacings))
    return 0.0


def classify_hatch_from_angles(angles: List[float]) -> Tuple[str, str]:
    """
    Classify hatch pattern and material from dominant line angles.

    Returns:
        Tuple of (pattern_code, material_type)
    """
    if not angles:
        return 'UNKNOWN', 'unknown'

    has_45 = any(abs(a - 45) < 10 for a in angles)
    has_135 = any(abs(a - 135) < 10 for a in angles)
    has_0 = any(a < 10 or a > 170 for a in angles)
    has_90 = any(abs(a - 90) < 10 for a in angles)

    # Cross-hatch: 45° + 135° = concrete
    if has_45 and has_135:
        return 'AR-CONC', 'concrete'

    # Single diagonal 45° = steel (section cut)
    if has_45 and not has_135:
        return 'ANSI31', 'steel'

    # Single diagonal 135° = also steel
    if has_135 and not has_45:
        return 'ANSI31', 'steel'

    # Horizontal + vertical grid = wood end-grain
    if has_0 and has_90:
        return 'WOOD-XS', 'wood'

    # Horizontal or vertical only = wood with-grain
    if has_0 and not has_90:
        return 'ANSI37', 'wood'
    if has_90 and not has_0:
        return 'ANSI37', 'wood'

    # No dominant pattern = earth/stipple
    if len(angles) > 2:
        return 'EARTH', 'earth'

    return 'UNKNOWN', 'unknown'


def determine_hatch_context(zone: Dict) -> str:
    """Determine if a hatch zone is in a section cut or plan view context."""
    # Use sheet type hints if available in zone data
    sheet = zone.get('sheet', '')
    sheet_upper = sheet.upper()

    # Section sheets
    if any(s in sheet_upper for s in ['A-3', 'A-4', 'A-5', 'S-3', 'S-4', 'S-5']):
        return 'section_cut'
    # Plan view sheets
    if any(s in sheet_upper for s in ['A-1', 'A-2', 'C-', 'S-1', 'S-2']):
        return 'plan_view'
    return 'unknown'


def find_adjacent_label(x1: int, y1: int, x2: int, y2: int,
                        texts: List[TextExtraction],
                        search_radius: int = 50) -> Optional[str]:
    """Find text labels adjacent to a material zone boundary."""
    material_keywords = [
        'CONCRETE', 'CONC', 'EARTH', 'FILL', 'GRAVEL', 'INSULATION',
        'INSUL', 'RIGID', 'BATT', 'STEEL', 'WOOD', 'MASONRY', 'CMU',
        'BRICK', 'STONE', 'METAL', 'GWB', 'GYPSUM', 'PLYWOOD', 'OSB',
        'SAND', 'VAPOR', 'AIR BARRIER', 'SHEATHING', 'STUD', 'FOAM'
    ]

    best_label = None
    best_dist = search_radius + 1

    for text in texts:
        tx = text.x
        ty = text.y
        content = text.text.upper().strip()

        # Check if text contains a material keyword
        has_keyword = any(kw in content for kw in material_keywords)
        if not has_keyword:
            continue

        # Calculate distance from text to zone boundary
        # Use minimum distance to any edge
        dx = max(x1 - tx, 0, tx - x2)
        dy = max(y1 - ty, 0, ty - y2)
        dist = np.sqrt(dx ** 2 + dy ** 2)

        if dist < best_dist:
            best_dist = dist
            best_label = text.text.strip()

    return best_label


def material_from_label(label: str) -> Optional[str]:
    """Map a text label to a material type string."""
    label_upper = label.upper()
    mappings = [
        (['CONCRETE', 'CONC', '4000 PSI', '3000 PSI'], 'concrete'),
        (['EARTH', 'FILL', 'BACKFILL', 'NATIVE'], 'earth'),
        (['GRAVEL', 'AGGREGATE', 'CRUSHED', '#57', '#2'], 'gravel'),
        (['INSULATION', 'INSUL', 'RIGID', 'BATT', 'R-', 'FOAM', 'XPS', 'EPS'], 'insulation'),
        (['STEEL', 'METAL', 'MTL'], 'steel'),
        (['WOOD', 'TIMBER', 'PLYWOOD', 'OSB', 'LVL', 'LUMBER'], 'wood'),
        (['MASONRY', 'CMU', 'BRICK', 'BLOCK'], 'masonry'),
        (['GYPSUM', 'GWB', 'DRYWALL', 'GYPS'], 'gypsum'),
        (['SAND', 'BEDDING'], 'sand'),
    ]
    for keywords, mat_type in mappings:
        if any(kw in label_upper for kw in keywords):
            return mat_type
    return None


def detect_keynote_bubbles(image: np.ndarray,
                           gray: np.ndarray,
                           texts: List[TextExtraction],
                           lines: Optional[List] = None,
                           symbols: Optional[List] = None) -> List[KeynoteCallout]:
    """
    Detect keynote bubble callouts on the drawing.
    Keynotes are small circles/diamonds containing numbers with leader lines.
    """
    callouts = []
    height, width = gray.shape

    # Detect small circles using HoughCircles
    blurred = cv2.GaussianBlur(gray, (5, 5), 1)
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=20,
        param1=100,
        param2=30,
        minRadius=6,
        maxRadius=25
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype(int)

        for cx, cy, r in circles:
            # Check if circle contains a number (keynote ID)
            number = find_number_in_region(
                texts, cx - r, cy - r, cx + r, cy + r
            )

            if number is None:
                continue

            # Filter out door/window marks (typically larger circles or different patterns)
            if len(number) > 2:
                continue  # Keynotes are typically 1-2 digit numbers
            if not number.isdigit():
                continue

            # Find leader line endpoint
            leader_end = find_leader_endpoint(cx, cy, r, lines)

            # Determine what the leader points to
            element_type = None
            element_id = None
            if leader_end and symbols:
                element_type, element_id = find_pointed_element(
                    leader_end, symbols, texts
                )

            callout = KeynoteCallout(
                keynote_number=number,
                bubble_center=(float(cx), float(cy)),
                bubble_radius=float(r),
                leader_endpoint=leader_end,
                points_to_element=element_id,
                points_to_type=element_type
            )
            callouts.append(callout)

    logger.info(f"Detected {len(callouts)} keynote callouts")
    return callouts


def find_number_in_region(texts: List[TextExtraction],
                          x1: float, y1: float,
                          x2: float, y2: float) -> Optional[str]:
    """Find a numeric text element within a bounding region."""
    for text in texts:
        if x1 <= text.x <= x2 and y1 <= text.y <= y2:
            content = text.text.strip()
            # Check for 1-2 digit number
            if content.isdigit() and 1 <= len(content) <= 2:
                return content
    return None


def find_leader_endpoint(cx: int, cy: int, radius: int,
                         lines: Optional[List],
                         search_radius: int = 15) -> Optional[Tuple[float, float]]:
    """
    Find the endpoint of a leader line originating near a keynote bubble.
    """
    if not lines:
        return None

    best_endpoint = None
    best_dist = search_radius + 1

    for line_obj in lines:
        # Handle both Line dataclass and dict
        if hasattr(line_obj, 'x1'):
            lx1, ly1 = line_obj.x1, line_obj.y1
            lx2, ly2 = line_obj.x2, line_obj.y2
        elif isinstance(line_obj, dict):
            lx1 = line_obj.get('x1', 0)
            ly1 = line_obj.get('y1', 0)
            lx2 = line_obj.get('x2', 0)
            ly2 = line_obj.get('y2', 0)
        else:
            continue

        # Check if either endpoint is near the bubble boundary
        for px, py, ex, ey in [(lx1, ly1, lx2, ly2), (lx2, ly2, lx1, ly1)]:
            dist_to_bubble = np.sqrt((px - cx) ** 2 + (py - cy) ** 2)
            # Line starts near the bubble boundary (within search_radius of circumference)
            if abs(dist_to_bubble - radius) < search_radius:
                # The other endpoint is the leader target
                dist_away = np.sqrt((ex - cx) ** 2 + (ey - cy) ** 2)
                if dist_away > radius * 2:  # Must point away from bubble
                    if dist_to_bubble < best_dist:
                        best_dist = dist_to_bubble
                        best_endpoint = (float(ex), float(ey))

    return best_endpoint


def find_pointed_element(leader_end: Tuple[float, float],
                         symbols: List,
                         texts: List[TextExtraction],
                         search_radius: int = 30) -> Tuple[Optional[str], Optional[str]]:
    """
    Determine what element a keynote leader line points to.
    """
    ex, ey = leader_end

    # Check symbols first
    for sym in symbols:
        if hasattr(sym, 'x'):
            sx, sy = sym.x, sym.y
            sym_type = getattr(sym, 'symbol_type', None)
            sym_name = str(sym_type.value) if sym_type else 'unknown'
        elif isinstance(sym, dict):
            sx = sym.get('x', 0)
            sy = sym.get('y', 0)
            sym_name = sym.get('symbol_type', 'unknown')
        else:
            continue

        dist = np.sqrt((sx - ex) ** 2 + (sy - ey) ** 2)
        if dist < search_radius:
            return sym_name, f"symbol_at_{int(sx)}_{int(sy)}"

    # Check nearby text for element identification
    for text in texts:
        dist = np.sqrt((text.x - ex) ** 2 + (text.y - ey) ** 2)
        if dist < search_radius:
            content = text.text.strip().upper()
            if any(kw in content for kw in ['WALL', 'TYPE', 'PARTITION']):
                return 'wall', content
            if any(kw in content for kw in ['DOOR', 'DR']):
                return 'door', content
            if any(kw in content for kw in ['WINDOW', 'WIN', 'W-']):
                return 'window', content

    return None, None


def extract_keynote_schedule(texts: List[TextExtraction],
                             zones: Optional[List[Dict]] = None) -> List[KeynoteScheduleEntry]:
    """
    Extract keynote schedule entries from the notes/schedule zone of the sheet.
    """
    schedule = []

    # Find text elements that look like keynote schedule entries
    # Pattern: number at start of line followed by description text
    # First, sort texts by y position (top to bottom), then x (left to right)
    sorted_texts = sorted(texts, key=lambda t: (t.y, t.x))

    # Look for sequences: number text followed by description text at similar y
    i = 0
    while i < len(sorted_texts):
        text = sorted_texts[i]
        content = text.text.strip()

        # Check if this is a keynote number (1-99, standalone)
        if content.isdigit() and 1 <= int(content) <= 99:
            # Look for description text at approximately the same y position
            desc_parts = []
            number = content
            j = i + 1

            while j < len(sorted_texts):
                next_text = sorted_texts[j]
                # Same line (within 10px vertically) and to the right
                if (abs(next_text.y - text.y) < 10 and
                        next_text.x > text.x):
                    desc_parts.append(next_text.text.strip())
                    j += 1
                else:
                    break

            if desc_parts:
                description = ' '.join(desc_parts)

                # Check for spec section reference in description
                spec_ref = extract_spec_ref(description)

                entry = KeynoteScheduleEntry(
                    number=number,
                    description=description,
                    spec_section=spec_ref,
                    sheet_source=''  # Filled by caller
                )
                schedule.append(entry)

                i = j
                continue

        i += 1

    logger.info(f"Extracted {len(schedule)} keynote schedule entries")
    return schedule


def extract_spec_ref(text: str) -> Optional[str]:
    """Extract a CSI spec section reference from text (e.g., '09 29 00')."""
    # Standard CSI format: XX XX XX (six digits in three pairs)
    match = re.search(r'\b(\d{2})\s*(\d{2})\s*(\d{2})\b', text)
    if match:
        return f"{match.group(1)} {match.group(2)} {match.group(3)}"

    # Alternative format: "Section XXXXXX"
    match = re.search(r'[Ss]ection\s+(\d{6})', text)
    if match:
        s = match.group(1)
        return f"{s[:2]} {s[2:4]} {s[4:6]}"

    return None


def extract_general_notes(texts: List[TextExtraction],
                          zones: Optional[List[Dict]] = None) -> List[GeneralNote]:
    """
    Extract numbered general notes from the notes zone of the sheet.
    """
    notes = []

    # Sort texts by position to reconstruct note blocks
    sorted_texts = sorted(texts, key=lambda t: (t.y, t.x))

    # Pattern: numbered note start (1., 2., A., B., etc.)
    note_pattern = re.compile(r'^(\d+|[A-Z])[\.\)]\s*(.+)', re.IGNORECASE)

    current_number = None
    current_text_parts = []

    for text in sorted_texts:
        content = text.text.strip()
        if not content:
            continue

        match = note_pattern.match(content)
        if match:
            # Save previous note
            if current_number is not None and current_text_parts:
                full_text = ' '.join(current_text_parts)
                category = classify_note_category(full_text)
                spec_refs = find_all_spec_refs(full_text)
                notes.append(GeneralNote(
                    note_number=current_number,
                    text=full_text,
                    category=category,
                    spec_refs=spec_refs
                ))

            # Start new note
            current_number = match.group(1)
            current_text_parts = [match.group(2)]
        elif current_number is not None:
            # Continuation of current note (heuristic: similar x position or indented)
            current_text_parts.append(content)

    # Don't forget last note
    if current_number is not None and current_text_parts:
        full_text = ' '.join(current_text_parts)
        category = classify_note_category(full_text)
        spec_refs = find_all_spec_refs(full_text)
        notes.append(GeneralNote(
            note_number=current_number,
            text=full_text,
            category=category,
            spec_refs=spec_refs
        ))

    logger.info(f"Extracted {len(notes)} general notes")
    return notes


def classify_note_category(text: str) -> str:
    """Classify a general note into a category based on content keywords."""
    text_upper = text.upper()

    categories = [
        ('dimensions', ['DIMENSION', 'MEASURE', 'FACE OF STUD', 'CENTERLINE',
                        'C/L', 'U.N.O', 'UNLESS NOTED']),
        ('materials', ['MATERIAL', 'PROVIDE', 'FURNISH', 'TYPE X', 'GWB',
                       'CONCRETE', 'STEEL', 'MASONRY']),
        ('installation', ['INSTALL', 'APPLY', 'MOUNT', 'FASTEN', 'ATTACH',
                          'SECURE', 'ANCHOR']),
        ('code', ['CODE', 'ADA', 'FIRE', 'EGRESS', 'RATED', 'ACCESSIBLE',
                  'NFPA', 'IBC', 'SMOKE']),
        ('coordination', ['COORDINATE', 'VERIFY', 'FIELD VERIFY', 'CONFIRM',
                          'CONTRACTOR', 'RESPONSIBLE', 'PRIOR TO']),
    ]

    for category, keywords in categories:
        if any(kw in text_upper for kw in keywords):
            return category

    return 'general'


def find_all_spec_refs(text: str) -> List[str]:
    """Find all CSI spec section references in text."""
    refs = []

    # Standard format: XX XX XX
    for match in re.finditer(r'\b(\d{2})\s+(\d{2})\s+(\d{2})\b', text):
        refs.append(f"{match.group(1)} {match.group(2)} {match.group(3)}")

    # Compact format: XXXXXX after "Section" or "Spec"
    for match in re.finditer(r'[Ss](?:ection|pec)\s+(\d{6})', text):
        s = match.group(1)
        ref = f"{s[:2]} {s[2:4]} {s[4:6]}"
        if ref not in refs:
            refs.append(ref)

    # Division reference: "Division XX" or "Div XX"
    for match in re.finditer(r'[Dd]iv(?:ision)?\s+(\d{1,2})', text):
        div = match.group(1).zfill(2)
        ref = f"{div} 00 00"
        if ref not in refs:
            refs.append(ref)

    return refs


# =============================================================================
# Main Pipeline and Visualization
# =============================================================================

def create_annotated_image(image: np.ndarray, result: Dict[str, Any]) -> np.ndarray:
    """
    Create annotated image with overlays from all passes.

    Args:
        image: Original image
        result: Pipeline result dictionary

    Returns:
        Annotated image
    """
    logger.info("Creating annotated image")

    annotated = image.copy()

    # Draw zones from Pass 1
    for zone in result.get('pass_1', {}).get('zones', []):
        x_min, y_min, x_max, y_max = zone['bbox']
        color = (0, 255, 0)  # Green
        cv2.rectangle(annotated, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 2)
        cv2.putText(annotated, zone['zone_type'], (int(x_min), int(y_min) - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Draw text bboxes from Pass 2
    for text in result.get('pass_2', {}).get('texts', [])[:50]:  # Limit for clarity
        x_min, y_min, x_max, y_max = text['bbox']
        color = (255, 0, 0)  # Blue
        cv2.rectangle(annotated, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, 1)

    # Draw lines from Pass 3
    for line in result.get('pass_3', {}).get('lines', [])[:100]:
        color_map = {
            'wall': (0, 0, 255),
            'dimension': (255, 255, 0),
            'grid': (255, 0, 255),
            'leader': (0, 255, 255),
            'section_cut': (128, 0, 255),
        }
        color = color_map.get(line['line_type'], (128, 128, 128))
        cv2.line(annotated, (int(line['x1']), int(line['y1'])),
                (int(line['x2']), int(line['y2'])), color, 1)

    # Draw symbols from Pass 4
    for symbol in result.get('pass_4', {}).get('symbols', []):
        x_min, y_min, x_max, y_max = symbol['bbox']
        cx, cy = symbol['centroid']
        cv2.circle(annotated, (int(cx), int(cy)), 5, (0, 165, 255), -1)  # Orange
        if symbol['label']:
            cv2.putText(annotated, symbol['label'], (int(x_min), int(y_min) - 5),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 165, 255), 1)

    return annotated


def run_pipeline(image_path: str, dpi: int = 300,
                 passes: Optional[List[int]] = None,
                 annotate_output: Optional[str] = None) -> Dict[str, Any]:
    """
    Main pipeline execution.

    Args:
        image_path: Path to input image
        dpi: DPI value
        passes: List of passes to run (default: all)
        annotate_output: Optional output path for annotated image

    Returns:
        Dictionary with all extraction results
    """
    logger.info(f"Starting visual plan analysis pipeline on {image_path}")

    if passes is None:
        passes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    image = cv2.imread(image_path)
    if image is None:
        logger.error(f"Failed to load image: {image_path}")
        return {"error": f"Failed to load image: {image_path}"}

    result = {
        "image_path": image_path,
        "image_shape": image.shape,
        "dpi": dpi,
        "passes_executed": passes
    }

    try:
        # Pass 1: Sheet Layout Detection
        if 1 in passes:
            pass_1_result = detect_sheet_layout(image, dpi)
            result['pass_1'] = pass_1_result
            zones = [ZoneMapEntry(**z) for z in pass_1_result['zones']]
            title_zone = zones[0].bbox if zones else None
        else:
            zones = []
            title_zone = None

        # Pass 2: OCR Extraction
        if 2 in passes:
            texts = extract_all_text(image, zones)
            title_block = extract_title_block_text(texts, title_zone) if title_zone else {}
            result['pass_2'] = {
                "texts": [asdict(t) for t in texts],
                "title_block": title_block,
                "text_count": len(texts)
            }
        else:
            texts = []

        # Pass 3: Line Detection
        if 3 in passes:
            lines = detect_and_classify_lines(image)
            result['pass_3'] = {
                "lines": [asdict(l) for l in lines],
                "line_count": len(lines)
            }
        else:
            lines = []

        # Pass 4: Symbol Detection
        if 4 in passes:
            symbols = detect_symbols(image, texts)
            result['pass_4'] = {
                "symbols": [asdict(s) for s in symbols],
                "symbol_count": len(symbols)
            }

        # Pass 5: Material Zones
        if 5 in passes:
            materials = detect_material_zones(image)
            result['pass_5'] = {
                "material_zones": [
                    {
                        "material_type": m.material_type.value,
                        "area_pixels": m.area_pixels,
                        "bbox": m.bbox,
                        "confidence": m.confidence
                    } for m in materials
                ],
                "material_count": len(materials)
            }

        # Pass 6: Dimension Extraction (Enhanced with chaining + elevations)
        if 6 in passes:
            dim_result = extract_dimensions(texts, lines)
            result['pass_6'] = {
                "dimensions": [asdict(d) for d in dim_result.get('dimensions', [])],
                "dimension_count": len(dim_result.get('dimensions', [])),
                "chains": [asdict(c) for c in dim_result.get('chains', [])],
                "chain_count": len(dim_result.get('chains', [])),
                "isolated": [asdict(d) for d in dim_result.get('isolated', [])],
                "isolated_count": len(dim_result.get('isolated', [])),
                "elevation_markers": [asdict(m) for m in dim_result.get('elevation_markers', [])],
                "elevation_marker_count": len(dim_result.get('elevation_markers', [])),
                "spot_elevations": dim_result.get('spot_elevations', []),
                "spot_elevation_count": len(dim_result.get('spot_elevations', []))
            }

        # Pass 7: Scale Calibration (Enhanced)
        if 7 in passes:
            # Collect zones from Pass 1 for multi-zone mapping
            pass1_zones = result.get('pass_1', {}).get('zones', [])
            scale_result = detect_scale(
                image, texts, title_zone,
                lines=lines if lines else None,
                zones=pass1_zones if pass1_zones else None,
                dpi=dpi
            )
            # Store enhanced result
            result['pass_7'] = {
                "scales": [asdict(s) for s in scale_result.get('scales', [])],
                "scale_count": len(scale_result.get('scales', [])),
                "graphic_bars": scale_result.get('graphic_bars', []),
                "text_scales": [asdict(s) for s in scale_result.get('text_scales', [])],
                "zones": scale_result.get('zones', []),
                "stretch_detected": scale_result.get('stretch_detected', False),
                "h_pixels_per_foot": scale_result.get('h_pixels_per_foot'),
                "v_pixels_per_foot": scale_result.get('v_pixels_per_foot'),
                "mean_pixels_per_foot": scale_result.get('mean_pixels_per_foot'),
                "calibration_method": scale_result.get('calibration_method', 'none'),
                "confidence": scale_result.get('confidence', 0.0)
            }

        # Pass 8: Cross-Sheet Reference Detection
        if 8 in passes:
            xref_result = detect_cross_sheet_references(
                image, texts,
                symbols=result.get('pass_4', {}).get('symbols', []),
                dpi=dpi
            )
            result['pass_8'] = {
                "callouts": [asdict(c) for c in xref_result.get('callouts', [])],
                "callout_count": len(xref_result.get('callouts', [])),
                "schedule_refs": xref_result.get('schedule_refs', []),
                "schedule_ref_count": len(xref_result.get('schedule_refs', [])),
                "spec_refs": xref_result.get('spec_refs', []),
                "spec_ref_count": len(xref_result.get('spec_refs', [])),
                "drawing_index_entry": xref_result.get('drawing_index_entry')
            }

        # Pass 9: Contour Line Detection (Civil/Site sheets only)
        if 9 in passes:
            # Get scale from Pass 7 if available
            p7_ppf = result.get('pass_7', {}).get('mean_pixels_per_foot')
            contour_result = detect_contour_lines(image, texts, scale_ppf=p7_ppf, dpi=dpi)
            result['pass_9'] = {
                "existing_contours": contour_result.get('existing_contours', []),
                "existing_count": len(contour_result.get('existing_contours', [])),
                "proposed_contours": contour_result.get('proposed_contours', []),
                "proposed_count": len(contour_result.get('proposed_contours', [])),
                "contour_interval_ft": contour_result.get('contour_interval_ft'),
                "drainage_patterns": contour_result.get('drainage_patterns', []),
                "cut_fill_estimate": contour_result.get('cut_fill_estimate')
            }

        # Pass 10: Building Section + Wall Section Extraction
        if 10 in passes:
            # Get dimensions from Pass 6
            p6_dims = []
            p6_elev_markers = []
            if 'pass_6' in result:
                p6_data = result['pass_6']
                # Reconstruct Dimension objects from dicts
                for d in p6_data.get('dimensions', []):
                    p6_dims.append(Dimension(**{k: v for k, v in d.items()
                                                if k in Dimension.__dataclass_fields__}))
                p6_elev_markers = p6_data.get('elevation_markers', [])

            # Get scale from Pass 7
            p7_ppf = result.get('pass_7', {}).get('mean_pixels_per_foot')

            section_result = extract_sections(
                image, texts, lines,
                dimensions=p6_dims,
                elevation_markers=p6_elev_markers,
                scale_ppf=p7_ppf,
                dpi=dpi
            )
            result['pass_10'] = {
                "building_sections": section_result.get('building_sections', []),
                "building_section_count": len(section_result.get('building_sections', [])),
                "wall_sections": section_result.get('wall_sections', []),
                "wall_section_count": len(section_result.get('wall_sections', [])),
                "roof_slopes": section_result.get('roof_slopes', []),
                "section_count": section_result.get('section_count', 0)
            }

        # Pass 11: RCP + MEP System Extraction
        if 11 in passes:
            # Get scale from Pass 7
            p7_ppf = result.get('pass_7', {}).get('mean_pixels_per_foot')

            rcp_mep_result = extract_rcp_mep(
                image, texts,
                symbols=result.get('pass_4', {}).get('symbols', []),
                lines=lines,
                scale_ppf=p7_ppf,
                dpi=dpi
            )
            result['pass_11'] = {
                "sheet_type": rcp_mep_result.get('sheet_type', 'unknown'),
                "ceiling_data": rcp_mep_result.get('ceiling_data'),
                "fixtures": rcp_mep_result.get('fixtures', []),
                "fixture_count": rcp_mep_result.get('fixture_count', 0),
                "equipment": rcp_mep_result.get('equipment', []),
                "equipment_count": rcp_mep_result.get('equipment_count', 0),
                "ducts": rcp_mep_result.get('ducts', []),
                "duct_count": rcp_mep_result.get('duct_count', 0),
                "pipes": rcp_mep_result.get('pipes', []),
                "pipe_count": rcp_mep_result.get('pipe_count', 0)
            }

        # Pass 12: Exterior Elevation + Accessibility Extraction
        if 12 in passes:
            # Get dimensions from Pass 6
            p6_dims = []
            if 'pass_6' in result:
                for d in result['pass_6'].get('dimensions', []):
                    p6_dims.append(Dimension(**{k: v for k, v in d.items()
                                                if k in Dimension.__dataclass_fields__}))

            p7_ppf = result.get('pass_7', {}).get('mean_pixels_per_foot')

            elev_access_result = extract_elevations_accessibility(
                image, texts,
                lines=lines,
                dimensions=p6_dims,
                scale_ppf=p7_ppf,
                dpi=dpi
            )
            result['pass_12'] = {
                "sheet_type": elev_access_result.get('sheet_type', 'unknown'),
                "elevation_data": elev_access_result.get('elevation_data'),
                "elevation_count": elev_access_result.get('elevation_count', 0),
                "accessibility_items": elev_access_result.get('accessibility_items', []),
                "accessibility_count": elev_access_result.get('accessibility_count', 0)
            }

        # Pass 13: Hatch Refinement + Keynote Extraction
        if 13 in passes:
            # Get material zones from Pass 5
            p5_zones = result.get('pass_5', {}).get('material_zones', [])

            # Get scale from Pass 7
            p7_ppf = result.get('pass_7', {}).get('mean_pixels_per_foot')

            # Get layout zones from Pass 1
            p1_zones = result.get('pass_1', {}).get('zones', [])

            # Get symbols from Pass 4
            p4_syms = result.get('pass_4', {}).get('symbols', [])

            hatch_keynote_result = extract_hatch_keynotes(
                image, texts,
                material_zones=p5_zones,
                lines=lines,
                symbols=p4_syms,
                scale_ppf=p7_ppf,
                zones=p1_zones,
                dpi=dpi
            )
            result['pass_13'] = {
                "refined_zones": hatch_keynote_result.get('refined_zones', []),
                "refined_count": hatch_keynote_result.get('refined_count', 0),
                "keynote_callouts": hatch_keynote_result.get('keynote_callouts', []),
                "keynote_schedule": hatch_keynote_result.get('keynote_schedule', []),
                "keynote_count": hatch_keynote_result.get('keynote_count', 0),
                "general_notes": hatch_keynote_result.get('general_notes', []),
                "general_note_count": hatch_keynote_result.get('general_note_count', 0)
            }

        # Create annotated image if requested
        if annotate_output:
            annotated = create_annotated_image(image, result)
            cv2.imwrite(annotate_output, annotated)
            logger.info(f"Annotated image saved to {annotate_output}")
            result['annotated_image_path'] = annotate_output

    except Exception as e:
        logger.error(f"Pipeline error: {e}")
        logger.error(traceback.format_exc())
        result['error'] = str(e)

    logger.info("Pipeline execution complete")
    return result


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Visual Plan Analyzer - Construction Plan Sheet Analysis Pipeline"
    )
    parser.add_argument('input', help='Input image path')
    parser.add_argument('--output', help='Output JSON path', default=None)
    parser.add_argument('--passes', help='Comma-separated pass numbers (default: 1-13)',
                       default='1,2,3,4,5,6,7,8,9,10,11,12,13')
    parser.add_argument('--dpi', type=int, help='Image DPI (default: 300)', default=300)
    parser.add_argument('--annotate', help='Output annotated image path', default=None)
    parser.add_argument('--summary', action='store_true', help='Print summary to stdout')

    args = parser.parse_args()

    # Parse passes
    try:
        passes = [int(p.strip()) for p in args.passes.split(',')]
    except ValueError:
        logger.error("Invalid pass specification")
        sys.exit(1)

    # Run pipeline
    result = run_pipeline(args.input, dpi=args.dpi, passes=passes,
                         annotate_output=args.annotate)

    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2, default=str)
        logger.info(f"Results saved to {args.output}")
    else:
        # Output to stdout as JSON
        print(json.dumps(result, indent=2, default=str))

    # Print summary if requested
    if args.summary:
        print("\n=== Summary ===", file=sys.stderr)
        if 'error' in result:
            print(f"Error: {result['error']}", file=sys.stderr)
        else:
            for pass_num in passes:
                key = f'pass_{pass_num}'
                if key in result:
                    count_key = None
                    if pass_num == 2:
                        count_key = 'text_count'
                    elif pass_num == 3:
                        count_key = 'line_count'
                    elif pass_num == 4:
                        count_key = 'symbol_count'
                    elif pass_num == 5:
                        count_key = 'material_count'
                    elif pass_num == 6:
                        count_key = 'dimension_count'
                    elif pass_num == 7:
                        count_key = 'scale_count'
                    elif pass_num == 8:
                        count_key = 'callout_count'
                    elif pass_num == 9:
                        count_key = 'existing_count'
                    elif pass_num == 10:
                        count_key = 'section_count'
                    elif pass_num == 11:
                        count_key = 'fixture_count'
                    elif pass_num == 12:
                        count_key = 'accessibility_count'
                    elif pass_num == 13:
                        count_key = 'keynote_count'

                    if count_key:
                        print(f"Pass {pass_num}: {result[key].get(count_key, 0)} items", file=sys.stderr)


if __name__ == '__main__':
    main()
