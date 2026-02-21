# document-annotation — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the document-annotation skill.



## Output Formats

### Annotated PDF (Primary Format)

The primary output format is annotated PDF, produced using Python PDF libraries for programmatic markup.

**Technology Stack**:
- **PyMuPDF (fitz)**: Primary library for reading source PDFs, extracting page geometry, and applying annotations. PyMuPDF provides direct access to PDF page content, coordinate transformation, and annotation insertion.
- **reportlab**: Secondary library for generating complex annotation overlays (tables, formatted text blocks, charts) as separate PDF pages that are merged with the source document.
- **Pillow (PIL)**: For image manipulation when annotating photos (resize, composite, draw operations).

**PDF Annotation Process**:
1. Open source PDF with `fitz.open()`
2. Get page dimensions and rotation: `page.rect`, `page.rotation`
3. Calculate annotation coordinates in PDF user space (origin at lower-left, 72 points per inch)
4. Create annotation shapes:
   - `page.draw_rect()` for rectangles, zones, text backgrounds
   - `page.draw_circle()` for callout bubbles, control points
   - `page.draw_line()` for leader lines, dimension lines, arrows
   - `page.draw_polyline()` for revision clouds (series of arcs)
   - `page.insert_text()` for text annotations
   - `page.insert_image()` for symbol placement from pre-rendered symbol library
5. Set annotation properties: color, line width, fill, opacity, layer (OCG)
6. Save with `doc.save()` preserving original content with annotations overlaid

**Coordinate System Handling**:
- Construction drawings are often at non-standard scales (1/4" = 1'-0", 1/8" = 1'-0", etc.)
- The annotation system works in PDF points (1 point = 1/72 inch) regardless of drawing scale
- Location references from annotation records are converted to PDF coordinates using the page's coordinate mapping
- Grid intersections, room centers, and element locations are mapped to PDF coordinates before annotation placement

### Annotated Images

Photo documentation annotations use image manipulation to produce marked-up photos.

**Image Annotation Process**:
1. Open source image with Pillow
2. Calculate overlay positions based on image dimensions
3. Draw annotation elements:
   - Circles, arrows, rectangles using `ImageDraw`
   - Text with background using `ImageDraw.text()` with measured text bounding box
   - Semi-transparent overlays using alpha compositing
4. Composite all annotation layers onto the source image
5. Save as PNG (lossless for quality) or JPEG (compressed for distribution)

**Image Output Specifications**:
- Resolution: maintain source resolution, minimum 150 DPI for print, 72 DPI for screen
- Format: PNG for markup with transparency, JPEG for distribution
- Maximum dimension: 4096px on longest side for distribution (larger for archival)
- Text rendering: anti-aliased, minimum 14pt equivalent at output resolution

### HTML Annotated Views

For dashboard integration and web-based viewing, annotations can be rendered as HTML/SVG overlays.

**HTML Annotation Output**:
- Source document rendered as background image (rasterized from PDF or original photo)
- Annotations rendered as SVG overlay elements positioned absolutely
- Interactive elements: hover tooltips showing annotation details, click to navigate to source data
- Responsive scaling: annotations maintain relative position as the view scales
- Layer toggles: checkbox controls to show/hide annotation layers
- Print-friendly: CSS print media query produces clean printable output

---



## Annotation Data Model

All annotations are tracked through a structured data model stored in `annotation-log.json`. Each annotation is a discrete record linked to its source document, location, and associated project data.

### Schema

```json
{
  "annotations": [
    {
      "annotation_id": "ANN-001",
      "document_ref": "A-101",
      "document_path": "plans/architectural/A-101_Floor_Plan_Level_1.pdf",
      "sheet_number": "A-101",
      "sheet_title": "First Floor Plan",
      "annotation_type": "revision_cloud",
      "location": {
        "page": 1,
        "x": 324.5,
        "y": 512.0,
        "width": 180.0,
        "height": 120.0,
        "grid_ref": "C-4",
        "level": "Level 1",
        "room": "Room 105",
        "description": "Corridor ceiling area between grids C-D and 3-4"
      },
      "content": {
        "text": "Duct routing revised per RFI-042 response. See ASI-007.",
        "symbols": ["revision_delta"],
        "revision_number": "R3",
        "markup_elements": [
          {
            "type": "cloud",
            "points": [[300, 490], [350, 480], [420, 490], [450, 520], [440, 580], [380, 600], [310, 590], [290, 540]],
            "arc_radius": 10
          },
          {
            "type": "text",
            "position": [460, 500],
            "value": "RFI-042: Duct rerouted above beam",
            "font_size": 10
          },
          {
            "type": "leader_line",
            "from": [456, 510],
            "to": [420, 530]
          }
        ]
      },
      "discipline": "mechanical",
      "color": "#008000",
      "line_weight": "heavy",
      "layer": "RFI_REFERENCES",
      "created_by": "John Smith, Superintendent",
      "created_date": "2024-11-15",
      "modified_date": "2024-11-15",
      "linked_items": {
        "rfi": "RFI-042",
        "asi": "ASI-007",
        "clash_id": "CLH-MEP-STR-0042",
        "punch_item": null,
        "daily_report": "DR-2024-11-15",
        "spec_section": "23 31 13"
      },
      "status": "active",
      "version_history": [
        {
          "version": 1,
          "date": "2024-11-15",
          "action": "created",
          "by": "John Smith",
          "notes": "Initial RFI markup for duct rerouting at C-4"
        }
      ]
    }
  ],
  "annotation_sets": [
    {
      "set_id": "ASET-001",
      "name": "Level 1 MEP Coordination Markup",
      "description": "Complete MEP coordination markup for Level 1 distribution to mechanical and electrical foremen",
      "created_date": "2024-11-15",
      "created_by": "John Smith, Superintendent",
      "source_documents": ["A-101", "M-101", "E-101"],
      "annotation_ids": ["ANN-001", "ANN-002", "ANN-003", "ANN-004"],
      "output_format": "annotated_pdf",
      "output_path": "markups/Level1_MEP_Coordination_2024-11-15.pdf",
      "distribution": ["Tom Brown (Mechanical Foreman)", "Sarah Davis (Electrical Foreman)"],
      "status": "distributed"
    }
  ],
  "symbol_library": {
    "revision_delta": {
      "type": "triangle",
      "size": 16,
      "fill": false,
      "label_position": "center"
    },
    "hold_point": {
      "type": "diamond",
      "size": 20,
      "fill": true,
      "fill_color": "#FF0000",
      "label_position": "right"
    },
    "deficiency": {
      "type": "cross",
      "size": 14,
      "color": "#FF0000",
      "line_weight": 2
    },
    "verified": {
      "type": "checkmark",
      "size": 14,
      "color": "#008000",
      "line_weight": 2
    },
    "callout_bubble": {
      "type": "circle",
      "size": 20,
      "fill": true,
      "fill_color": "#FFFFFF",
      "border_color": "#000000",
      "label_position": "center"
    },
    "direction_arrow": {
      "type": "arrow",
      "size": 24,
      "fill": true,
      "head_style": "closed"
    },
    "section_cut": {
      "type": "section_arrow",
      "size": 24,
      "fill": true,
      "label_position": "tail"
    },
    "match_line": {
      "type": "dashed_line",
      "dash_pattern": [10, 5],
      "line_weight": 1.5,
      "label_position": "center"
    },
    "detail_bubble": {
      "type": "circle_with_line",
      "size": 24,
      "fill": false,
      "label_position": "center",
      "reference_position": "bottom"
    }
  },
  "layer_definitions": [
    {
      "layer_name": "RFI_REFERENCES",
      "display_name": "RFI References",
      "default_color": "#FF00FF",
      "default_visibility": true,
      "description": "RFI markup including question area clouds, RFI numbers, and cross-references"
    },
    {
      "layer_name": "FIELD_NOTES",
      "display_name": "Field Notes",
      "default_color": "#0000FF",
      "default_visibility": true,
      "description": "Superintendent field notes, observations, and measurements"
    },
    {
      "layer_name": "QC_MARKS",
      "display_name": "Quality Control",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Quality control inspection marks, verification stamps, deficiency flags"
    },
    {
      "layer_name": "SAFETY_ZONES",
      "display_name": "Safety Zones",
      "default_color": "#FF8C00",
      "default_visibility": true,
      "description": "Safety barricade lines, exclusion zones, fall protection boundaries"
    },
    {
      "layer_name": "WORK_AREAS",
      "display_name": "Work Areas",
      "default_color": "#008000",
      "default_visibility": true,
      "description": "Work zone boundaries, trade access routes, staging areas"
    },
    {
      "layer_name": "PUNCH_ITEMS",
      "display_name": "Punch List Items",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Punch list callouts, deficiency markers, numbered references"
    },
    {
      "layer_name": "AS_BUILT",
      "display_name": "As-Built Redlines",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "As-built redlines showing field deviations from design"
    },
    {
      "layer_name": "DIMENSIONS",
      "display_name": "Field Dimensions",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Field-verified dimensions, deviation callouts, measurement annotations"
    },
    {
      "layer_name": "REVISIONS",
      "display_name": "Revisions",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Revision clouds, delta symbols, change descriptions"
    },
    {
      "layer_name": "HOLD_POINTS",
      "display_name": "Hold Points",
      "default_color": "#FF0000",
      "default_visibility": true,
      "description": "Inspection hold points, QC stop points, witness test locations"
    }
  ],
  "project_color_overrides": {}
}
```

### Annotation Record Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `annotation_id` | string | Yes | Unique identifier (ANN-###) |
| `document_ref` | string | Yes | Sheet number or document identifier of the source document |
| `document_path` | string | Yes | File path to the source document |
| `sheet_number` | string | No | Drawing sheet number (e.g., A-101, M-201) |
| `sheet_title` | string | No | Drawing sheet title |
| `annotation_type` | enum | Yes | Type: revision_cloud, text_note, comment, label, callout, symbol, dimension, zone_boundary, photo_markup, redline |
| `location` | object | Yes | Position data: page, x, y, width, height, grid_ref, level, room, description |
| `content` | object | Yes | Annotation content: text, symbols, revision_number, markup_elements array |
| `discipline` | enum | Yes | Discipline: architectural, structural, mechanical, electrical, plumbing, fire_protection, civil, safety, general |
| `color` | string | Yes | Hex color code for the annotation |
| `line_weight` | enum | Yes | Line weight: heavy (2pt), medium (1pt), light (0.5pt) |
| `layer` | string | Yes | Annotation layer name |
| `created_by` | string | Yes | Name and role of the annotation creator |
| `created_date` | string | Yes | ISO date of creation |
| `modified_date` | string | No | ISO date of last modification |
| `linked_items` | object | No | Cross-references: rfi, asi, clash_id, punch_item, daily_report, spec_section |
| `status` | enum | Yes | Status: active, superseded, voided, archived |
| `version_history` | array | Yes | Array of version records tracking annotation changes |

### Annotation Set Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `set_id` | string | Yes | Unique identifier (ASET-###) |
| `name` | string | Yes | Descriptive name for the annotation set |
| `description` | string | No | Detailed description of the annotation set purpose |
| `created_date` | string | Yes | ISO date of creation |
| `created_by` | string | Yes | Name and role of the set creator |
| `source_documents` | array | Yes | List of source document references included in the set |
| `annotation_ids` | array | Yes | List of annotation IDs included in the set |
| `output_format` | enum | Yes | Output format: annotated_pdf, annotated_image, html_view |
| `output_path` | string | No | File path to the generated output |
| `distribution` | array | No | List of recipients for the annotated document |
| `status` | enum | Yes | Status: draft, generated, distributed, archived |

### Status Lifecycle

**Annotation Status**:

| Status | Definition |
|---|---|
| `active` | Current, valid annotation displayed on output documents |
| `superseded` | Replaced by a newer annotation (e.g., revised RFI response, updated punch item) |
| `voided` | Annotation was created in error or is no longer applicable |
| `archived` | Annotation is historical record, retained but no longer displayed by default |

**Annotation Set Status**:

| Status | Definition |
|---|---|
| `draft` | Set defined but output not yet generated |
| `generated` | Output document produced, not yet distributed |
| `distributed` | Output document distributed to recipients |
| `archived` | Set is historical record, output may be superseded |

---



## Annotation Workflow Patterns

### Pattern 1: Weekly Trade Distribution Package

**Frequency**: Weekly, aligned with look-ahead planning cycle

**Process**:
1. Pull current look-ahead activities by trade from schedule data
2. For each trade with active work in the coming week:
   a. Select the relevant plan sheets covering their work areas
   b. Generate work area boundary annotations (WORK_AREAS layer)
   c. Add hold zone annotations for pending RFIs, inspections (HOLD_POINTS layer)
   d. Add field notes relevant to the trade (FIELD_NOTES layer)
   e. Compile into an annotation set
   f. Generate annotated PDF output
   g. Distribute to trade foreman

### Pattern 2: RFI Submission Package

**Trigger**: RFI preparation (integrates with rfi-preparer skill)

**Process**:
1. Identify the drawing sheet(s) referenced by the RFI
2. Generate revision cloud around the question area (RFI_REFERENCES layer)
3. Add RFI number label with leader line
4. Add dimension callouts for relevant measurements
5. Add spec section reference annotation
6. If field photos exist, generate annotated photo with callouts
7. Compile into annotation set
8. Generate annotated PDF package for RFI attachment

### Pattern 3: Punch List Walkthrough Documentation

**Trigger**: Punch list walkthrough (integrates with punch-list skill)

**Process**:
1. For each punch list item captured during the walkthrough:
   a. Annotate the field photo with deficiency callout, description, and location stamp
   b. Place callout marker on the relevant plan sheet at the item location
   c. Number callouts sequentially matching the punch list numbering
2. Generate annotated plan sheet with all punch items shown spatially
3. Generate annotated photo package with all deficiency photos marked up
4. Compile into annotation set for distribution to responsible trades

### Pattern 4: As-Built Documentation

**Trigger**: Work completion verification, pre-cover inspection, closeout documentation

**Process**:
1. Collect field-verified dimensions and routing data
2. For each deviation from design:
   a. Place redline annotation showing actual condition
   b. Add dimension callout with actual vs. design values
   c. Add deviation note explaining the change
3. Place verification stamps at locations confirmed as matching design
4. Generate annotated as-built drawing for record
5. Log all deviations in the field verification tracking system

---



## Integration

The document-annotation skill connects with other ForemanOS skills to provide comprehensive document management:

### document-intelligence
- Receives extracted data (room numbers, equipment tags, spec requirements, hold points) for auto-generated annotations
- Consumes document classification and coordinate mapping for accurate annotation placement
- Uses extracted spec section data to produce annotated field spec sheets
- Leverages schedule data for annotated timeline views and milestone highlights

### rfi-preparer
- Produces annotated drawing markups for RFI submission packages
- Generates revision cloud and question area highlighting referenced by RFI content
- Creates annotated photo attachments for field condition documentation
- Maintains cross-reference between annotation records and RFI log entries

### punch-list
- Produces annotated photos with deficiency callouts, descriptions, and location stamps
- Generates annotated plan sheets showing punch item locations spatially
- Creates numbered callout overlays matching punch list item numbering
- Supports before/after photo comparison annotation for punch item resolution

### daily-report-format
- Provides annotated plan references for daily report work area documentation
- Generates annotated site photos for daily report photo logs
- Creates quick-markup plan sheets showing today's active work areas
- Supplies annotation records for daily report activity logging

### drawing-control
- Tracks revision markup on controlled drawings through annotation version history
- Maintains annotation layer state across drawing revisions (carry forward or archive)
- Links revision cloud annotations to drawing revision log entries
- Ensures as-built markup annotations are preserved through the revision process

### bim-coordination
- Consumes clash report data to auto-generate clash location markups on plan sheets
- Places deviation markers from model-to-field verification records
- Produces annotated plans showing scan results and out-of-tolerance conditions
- Generates coordination markup showing multi-discipline conflict areas

## Integration with Document Intelligence

The document-annotation skill leverages data extracted by the document-intelligence skill to auto-generate annotations. This eliminates manual placement of common annotations and ensures consistency.

### Auto-Generated Annotations from Extracted Data

**Room Number Placement**
- Document-intelligence extracts room numbers, names, and approximate locations from floor plans
- Annotation skill places room number labels at extracted coordinates on plan sheets
- Labels formatted as circled or boxed room numbers with room name below
- Useful for producing marked-up plans for trades that reference room numbers (finishes, electrical, low-voltage)

**Hold Point Locations**
- Document-intelligence extracts inspection and hold point requirements from spec sections
- Annotation skill places diamond symbols at corresponding locations on plan sheets
- Each hold point labeled with the inspection type and spec reference
- Produces a "hold point plan" showing all required inspections spatially

**Equipment Tag Placement**
- Document-intelligence extracts equipment schedules with tag numbers and locations
- Annotation skill places equipment tags at plan locations
- Tags formatted as hexagonal or rectangular labels with equipment designation
- Cross-references to submittal log entries and O&M manual references

**Spec Requirement Overlays**
- Document-intelligence extracts key requirements per area (concrete strength by pour area, fire rating by zone, finish schedule by room)
- Annotation skill produces annotated plans with requirements shown at their applicable locations
- Example: Floor plan with concrete strength noted in each pour area ("4000 PSI", "5000 PSI HIGH-EARLY")

### Annotated Spec Summaries

Produce trade-specific "field spec sheets" by combining extracted spec data with annotation formatting:

1. **Extract** key requirements from full spec section using document-intelligence
2. **Filter** requirements by trade applicability
3. **Format** as annotated document with highlighted critical items, plain-language notes, and visual callouts
4. **Cross-reference** with plan sheet locations and approved submittals
5. **Output** as annotated PDF ready for field distribution

**Example output**: A two-page "Concrete Field Spec Sheet" containing:
- Mix design requirements (extracted from 03 30 00) with critical values highlighted in yellow
- Placement requirements (slump, temperature, vibration) with hold points marked
- Curing requirements with timeline graphic and weather restrictions flagged in orange
- Testing requirements (cylinders, slump tests) with frequency table
- Approved ready-mix suppliers from submittal log
- Reference to specific pour area on plan with callout to spec requirements

### Annotated Schedule Overlays

Generate annotated schedule views by combining schedule data with visual markup:

**Critical Path Highlighting**
- Critical path activities highlighted in red on the bar chart or network diagram
- Near-critical activities (< 5 days float) highlighted in orange
- Float values annotated on each activity bar
- Milestone diamonds enlarged and labeled with dates

**Weather-Sensitive Activity Flags**
- Activities sensitive to weather conditions flagged with weather symbol
- Temperature restrictions (concrete pours, coatings, roofing) noted with threshold values
- Rain-sensitive activities (earthwork, exterior finishes) noted with restriction description
- Seasonal considerations annotated on the timeline

**Upcoming Milestone Highlights**
- Activities due within the look-ahead period highlighted with colored border
- Predecessor completion status shown with green (complete) or red (incomplete) indicators
- Resource requirements annotated on upcoming activities
- Material delivery dates cross-referenced from procurement log

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


