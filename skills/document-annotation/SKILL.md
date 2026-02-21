---
name: document-annotation
description: >
  Construction document annotation and markup system for superintendents. Produce redline markups, revision clouds, text annotations, symbol placement, color-coded discipline markups, and layered annotation management on plans, specs, photos, and RFIs. Generate annotated PDFs using PyMuPDF/fitz and reportlab, annotated images for photo documentation, and HTML annotated views for dashboard integration. Integrates with document-intelligence, rfi-preparer, punch-list, daily-report-format, and drawing-control. Triggers: "annotate", "markup", "redline", "cloud", "mark up plans", "annotate drawing", "redline drawing", "photo markup", "punch list photo", "annotate spec", "spec markup", "RFI markup", "as-built markup", "callout", "dimension callout", "field note on drawing", "highlight on plan", "revision cloud", "annotation layer", "color-coded markup".
version: 1.0.0
---

# Document Annotation Skill

## Overview

The **document-annotation** skill provides programmatic construction document markup and annotation capabilities for superintendents and field managers. This skill does not replace Bluebeam Revu or PlanGrid for interactive markup sessions -- it provides **automated, data-driven annotation** that turns extracted project data into marked-up documents ready for field distribution, RFI submission, punch list documentation, and as-built recording.

Construction documents are only useful when the right information reaches the right trade at the right time. A 200-page spec book is useless to the plumber who needs three paragraphs about fixture rough-in requirements. A full set of architectural plans means nothing to the electrician who needs to know which rooms have dedicated circuits. This skill bridges that gap by producing annotated, trade-specific document extracts that put actionable information directly on the drawings, specs, and photos that field crews actually use.

**Core capabilities**:
- Redline and revision cloud markup on PDF plan sheets
- Text annotation with callouts, labels, leaders, and notes
- Symbol placement using standard construction markup conventions
- Color-coded markup by discipline following industry convention
- Layer-based annotation management for organizing markup by type
- Annotated document production for trade distribution
- Photo markup with deficiency callouts for punch list and QC
- RFI drawing markup with highlighted question areas
- As-built redline markup with field-verified dimensions and deviations
- Auto-generated annotations from document-intelligence extracted data
- Structured annotation records with full traceability

**Critical distinction**: This skill produces output documents. It takes source documents (plans, specs, photos) and produces annotated versions with markup applied. The annotations are data-driven -- they come from project data, field observations, RFI content, punch list items, and extracted document intelligence, not from freehand drawing.

### Why Programmatic Annotation Matters

**Traditional markup workflow**:
- Open drawing in Bluebeam or PlanGrid
- Manually draw clouds, add text, place symbols
- Save and distribute
- No structured data behind the markup -- it is a picture of annotations

**Data-driven annotation workflow**:
- Annotation records created from project data (RFIs, punch items, field notes, extracted specs)
- Markup generated programmatically with consistent formatting
- Every annotation linked to source data (RFI number, punch item ID, spec section)
- Annotations queryable, filterable, and trackable
- Bulk annotation production for trade-specific document packages

This skill enables the superintendent to produce professional, consistent, traceable document markup at scale -- not one drawing at a time, but entire packages of annotated documents for distribution.

---

## PDF Markup Capabilities

### Redline and Cloud Markup

Redline markup is the fundamental language of construction document revision. This skill supports programmatic generation of all standard redline markup types.

**Revision Clouds**
- Freeform cloud outlines drawn around areas of change or concern
- Cloud arc radius configurable (default: 0.15" arc segments for standard revision cloud appearance)
- Cloud line weight: heavy (2pt) for revision clouds, per AIA convention
- Cloud color follows discipline color coding (see Color Conventions below)
- Interior of cloud may be left clear or filled with semi-transparent wash (10-15% opacity)
- Revision clouds are the primary markup for identifying areas affected by a design change, ASI, or field deviation

**Redline Annotations**
- Strikethrough lines for deleted elements (single diagonal or X through deleted item)
- Addition lines for new elements (drawn in revision color with delta symbol)
- Dimension callouts showing field-verified measurements vs. design dimensions
- Leader lines connecting annotations to specific locations on the drawing
- Section cuts and detail references pointing to supplementary information

**Implementation**: PDF markup is generated using PyMuPDF (fitz) for reading and modifying existing PDFs, and reportlab for generating new annotation overlays. The workflow:
1. Open source PDF with PyMuPDF
2. Calculate page dimensions and coordinate system
3. Generate annotation shapes (clouds, lines, text, symbols) as PDF drawing operations
4. Apply annotations as overlay on the source page
5. Save annotated PDF with annotations on a separate layer when possible

### Text Annotations

Text annotations place readable information directly on drawings at specific locations. All text follows construction document conventions for readability at typical reproduction scales.

**Note Annotations**
- Freestanding text blocks placed at specified coordinates
- Font: sans-serif (Helvetica/Arial) for markup text, matching typical construction document conventions
- Size hierarchy: 12pt for primary notes, 10pt for secondary, 8pt for reference text
- Background: optional white or yellow rectangle behind text for readability over complex drawings
- Border: optional thin black border around text block

**Comment Annotations**
- Text with leader line pointing to a specific location on the drawing
- Leader line terminates with arrowhead at the target location
- Text block positioned to avoid overlapping existing drawing content
- Comment format: "[PREFIX] Comment text" where prefix is the annotation type (e.g., "RFI-042:", "PUNCH:", "NOTE:")

**Label Annotations**
- Short text labels placed directly at or adjacent to elements
- Used for room numbers, equipment tags, grid references, elevation callouts
- Typically 8-10pt bold text with optional circle, rectangle, or hexagon enclosure
- Label placement follows drafting convention: above and to the right of the labeled element when space permits

**Callout Annotations**
- Numbered or lettered callouts with corresponding legend
- Callout marker: circled number or letter placed on the drawing
- Legend block: numbered list of callout descriptions placed in margin or title block area
- Used for punch list items, inspection points, deficiency locations

### Symbol Placement

Standard construction markup symbols communicate specific meanings without text. This skill places symbols programmatically at specified coordinates.

| Symbol | Name | Meaning | Usage |
|---|---|---|---|
| Triangle (delta) | Revision triangle | Marks a revision or change | Placed next to revised elements with revision number inside |
| Cloud outline | Revision cloud | Encloses area of change | Drawn around the affected area on the drawing |
| Arrow (straight) | Direction arrow | Indicates direction of flow, access, or reference | Placed on plans for traffic flow, pipe flow, access routes |
| Arrow (curved) | Rotation arrow | Indicates rotation or turning direction | Equipment orientation, door swing direction |
| Circle with crosshairs | Control point | Survey or layout control point | Placed at survey control locations |
| Diamond | Hold point | Inspection or quality hold point | Placed at locations requiring inspection before proceeding |
| Flag | Flag/attention | Calls attention to a specific item | General attention marker for important notes |
| X (cross) | Deficiency | Marks a deficient condition | Placed on photos or plans at deficiency locations |
| Checkmark | Verified/approved | Marks verified or approved condition | Placed on items that pass inspection |
| Circle with number | Callout bubble | Numbered reference to legend | Sequential numbering for punch list, inspection items |
| Dashed rectangle | Zone boundary | Defines a work zone or area | Drawn around work areas, hold zones, safety zones |
| Hatched area | Restricted zone | Indicates restricted or no-access area | Drawn over areas with access restrictions |

### Color-Coded Markup by Discipline

Industry convention assigns specific colors to discipline-specific markup. Consistent color coding allows field crews to immediately identify which trade a markup applies to.

| Discipline | Primary Color | RGB Value | Hex Code | Usage |
|---|---|---|---|---|
| Architectural | Black | (0, 0, 0) | #000000 | Architectural markups, general notes, dimensions |
| Structural | Red | (255, 0, 0) | #FF0000 | Structural markups, beam/column modifications, load paths |
| Mechanical (HVAC) | Green | (0, 128, 0) | #008000 | Ductwork routing, equipment placement, diffuser locations |
| Electrical | Blue | (0, 0, 255) | #0000FF | Conduit routing, panel locations, device placement |
| Plumbing | Purple | (128, 0, 128) | #800080 | Pipe routing, fixture locations, drain lines |
| Fire Protection | Red-Dashed | (255, 0, 0) dashed | #FF0000 | Sprinkler routing, head locations, FDC, standpipes |
| Civil/Site | Brown | (139, 90, 43) | #8B5A2B | Grading, utilities, paving, site features |
| Safety | Orange | (255, 140, 0) | #FF8C00 | Safety zones, barricades, fall protection, exclusion areas |
| General/Multi-trade | Magenta | (255, 0, 255) | #FF00FF | Multi-discipline coordination, general field notes |
| Owner/Design team | Cyan | (0, 200, 200) | #00C8C8 | Owner comments, design team responses, ASI markups |

**Fire protection distinction**: Fire protection uses the same red as structural but with a dashed line pattern to differentiate. When both structural and fire protection markups appear on the same sheet, the dash pattern provides clear visual separation.

**Discipline color override**: Project-specific color conventions may differ. The annotation system allows color override per project through the project configuration.

### Layer Management

Annotations are organized into layers that can be toggled, filtered, and managed independently. Layer management enables multiple annotation types to coexist on a single document without visual clutter.

**Standard Annotation Layers**:

| Layer Name | Content | Default Visibility |
|---|---|---|
| `RFI_REFERENCES` | RFI markup -- highlighted question areas, RFI numbers, cross-references | Visible |
| `FIELD_NOTES` | Superintendent field notes, observations, measurements | Visible |
| `QC_MARKS` | Quality control inspection marks, verification stamps, deficiency flags | Visible |
| `SAFETY_ZONES` | Safety barricade lines, exclusion zones, fall protection boundaries | Visible |
| `WORK_AREAS` | Work zone boundaries, trade access routes, staging areas | Visible |
| `DIMENSIONS` | Field-verified dimensions, deviation callouts, measurement annotations | Visible |
| `REVISIONS` | Revision clouds, delta symbols, change descriptions | Visible |
| `PUNCH_ITEMS` | Punch list callouts, deficiency markers, numbered references | Visible |
| `AS_BUILT` | As-built redlines showing field deviations from design | Visible |
| `HOLD_POINTS` | Inspection hold points, QC stop points, witness test locations | Visible |
| `TRADE_SPECIFIC` | Trade-specific annotations filtered by discipline color | Visible |
| `REFERENCE` | Background reference annotations, spec section references, code citations | Hidden by default |

**Layer naming convention**: `[TYPE]_[SUBTYPE]` using uppercase with underscores. Custom layers follow the same pattern (e.g., `SAFETY_FALL_PROTECTION`, `QC_CONCRETE_PLACEMENT`).

**PDF layer implementation**: When the output PDF supports Optional Content Groups (OCG), annotations are placed on named layers that can be toggled in PDF viewers (Adobe Acrobat, Bluebeam Revu). When OCG is not supported, layers are flattened but visually distinguished by color and line style.

---

## Annotated Document Production

### Plan Markup for Trade Distribution

The most common annotation task is marking up a plan sheet with trade-specific information for field distribution. This produces a document that a foreman can hand to a crew with all relevant information visible on the drawing.

**Work Area Markup**
- Dashed rectangle or cloud outline defining the active work zone for the day/week
- Zone label with work description (e.g., "ZONE 3A -- MEP ROUGH-IN THIS WEEK")
- Color-coded by responsible trade
- Access route arrows showing crew entry/exit paths
- Material staging area marked with hatching

**Hold Zone Markup**
- Solid red boundary line around areas where work must stop
- "HOLD" label with reason (e.g., "HOLD -- PENDING RFI-042 RESPONSE")
- Diamond hold point symbols at specific hold locations
- Reference to the RFI, inspection, or coordination item causing the hold

**Sequence Markup**
- Numbered zones showing installation sequence (1, 2, 3...)
- Directional arrows showing work flow direction
- Phase boundaries with date labels
- Predecessor/successor notes between zones

**Trade-Specific Plan Package**
For each trade receiving a marked-up plan:
1. Start with the relevant discipline sheet (mechanical plan for HVAC, electrical plan for electrical, etc.)
2. Add work area boundaries for the current look-ahead period
3. Mark hold zones and restricted areas
4. Add field notes relevant to that trade
5. Highlight RFI areas affecting that trade's work
6. Add spec references for critical requirements
7. Include callouts for coordination points with other trades

### Spec Section Annotation

Specification books are dense legal documents. Field crews need the critical requirements extracted and highlighted, not the full 50-page section. This capability produces annotated spec extracts.

**Spec Highlighting**
- Key requirements highlighted with colored background (yellow for critical, green for informational)
- Margin annotations explaining requirements in plain language
- Cross-references to plan sheet locations where the requirement applies
- Submittal references linked to approved submittals for specified products

**Trade Field Spec Sheet**
A one-to-three page annotated extract from the full spec section containing:
- Section header with spec section number, title, and revision date
- Critical requirements extracted and highlighted (strengths, tolerances, materials, methods)
- Testing and inspection requirements with hold points marked
- Approved products/manufacturers from submittal log
- Weather restrictions and environmental requirements
- Quality control requirements and acceptance criteria
- Relevant code references (ACI, AISC, NEC, UPC, NFPA)
- Superintendent notes and project-specific clarifications

**Implementation**: The document-intelligence skill extracts spec data; this skill formats it into annotated field-ready documents. The extraction provides structured data; the annotation provides visual presentation.

### RFI Drawing Markup

When preparing an RFI, the referenced drawing must be marked up to clearly identify the question area and provide context to the reviewer.

**RFI Markup Elements**
1. **Question Area Cloud** -- Revision cloud around the area in question, colored magenta for RFI markup
2. **RFI Reference Label** -- "RFI-[NUMBER]" label placed adjacent to the cloud with leader line
3. **Dimension Callouts** -- Key dimensions relevant to the question, highlighted in red
4. **Section References** -- Arrows pointing to relevant detail/section views
5. **Conflict Indication** -- If the RFI is about a conflict, both conflicting elements highlighted with contrasting colors
6. **Spec Reference** -- Annotation noting the relevant spec section number
7. **Photo Reference** -- If field photos exist, annotation noting "SEE ATTACHED PHOTO [X]"
8. **Proposed Solution** -- If the superintendent has a proposed resolution, it is sketched/annotated in green with "PROPOSED" label

**RFI Markup Package**
The complete RFI markup package includes:
- Annotated plan sheet (primary affected sheet)
- Annotated detail/section views (if applicable)
- Annotated photos (if field conditions are relevant)
- Annotation legend explaining all markup symbols used

### Punch List Photo Markup

Photo documentation of deficiencies requires clear annotation to communicate exactly what the problem is and where it is located.

**Photo Annotation Elements**
- **Deficiency Callout**: Circled number at the deficiency location with leader line to description
- **Description Box**: Text box with deficiency description, responsible trade, and punch item ID
- **Directional Arrows**: Arrows pointing to the specific deficient element
- **Measurement Overlay**: Dimension lines showing measured values vs. required values
- **Reference Overlay**: Spec section or drawing reference for the applicable standard
- **Before/After Comparison**: Side-by-side layout with "BEFORE" and "AFTER" labels, deficiency marks on the "before" image, acceptance marks on the "after" image
- **Location Stamp**: Text overlay with location information (building, floor, room, grid)

**Photo Markup Standards**
- Callout numbers correspond to the punch list item numbering
- Arrow colors match the responsible discipline color
- Description text is minimum 14pt for readability on mobile devices
- Location stamp is placed in the lower-left corner of the photo
- Date/time stamp placed in the lower-right corner
- White semi-transparent background behind all text overlays (80% opacity)

### As-Built Drawing Markup

As-built markup records the actual field conditions that differ from the design documents. These markups become part of the permanent project record and are used for closeout documentation.

**As-Built Markup Elements**
- **Dimension Redlines**: Actual field-measured dimensions shown in red, replacing or supplementing design dimensions
- **Routing Changes**: Revised pipe, conduit, or duct routing shown with colored lines matching the discipline
- **Elevation Changes**: Actual elevations annotated at key points (invert elevations, top-of-steel, finish floor)
- **Location Shifts**: Arrows showing the direction and distance of element displacement from design location
- **Deletion Marks**: X through elements that were not installed or were removed
- **Addition Marks**: New elements drawn in red with delta symbol and "ADDED" label
- **Deviation Notes**: Text annotations explaining why the field condition differs from design
- **Verification Stamps**: Checkmark with date and initials at locations verified by field measurement

**As-Built Color Convention**
- Red: All as-built changes and deviations
- Green: Verified as-installed matching design (confirmation markup)
- Blue: Information annotations (notes, references, explanations)
- Original drawing content remains in its original color (typically black)

**As-Built Accuracy Requirements**
- Horizontal dimensions: verified to +/- 1/4" for MEP, +/- 1/2" for structural
- Vertical dimensions: verified to +/- 1/4" for all systems
- Routing changes: drawn to approximate scale showing general path, with key dimensions noted
- All as-built markups must include the date of field verification and the verifier's initials

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
