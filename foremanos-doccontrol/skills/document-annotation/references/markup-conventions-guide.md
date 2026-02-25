# Construction Document Markup Conventions
## Industry-Standard Markup Practices for Field Documentation

---

## 1. STANDARD CONSTRUCTION MARKUP SYMBOLS

### Revision and Change Symbols

These symbols communicate changes, revisions, and modifications to construction documents. They are recognized across all trades and disciplines.

| Symbol | Name | Description | When to Use |
|---|---|---|---|
| **Triangle with number** | Revision Delta | Equilateral triangle containing the revision number (1, 2, 3...) | Place adjacent to any element changed in the current revision. The number inside corresponds to the revision log in the title block. |
| **Irregular cloud outline** | Revision Cloud | Freeform cloud drawn around the area affected by the revision | Enclose the entire area affected by a change. The cloud makes the changed zone immediately visible when scanning a drawing. |
| **Triangle with arrow** | Revision Delta with Leader | Delta symbol with a leader line pointing to the specific changed element | Use when the revision affects a small element that needs a precise pointer rather than a cloud. |
| **Cloud with delta** | Revision Cloud with Delta | Cloud around the area plus delta symbol at the cloud perimeter | Full revision markup: cloud defines the area, delta provides the revision number reference. Standard AIA/CSI practice. |
| **Diagonal line through text** | Strikethrough | Single diagonal line through text or dimension being deleted | Mark text, dimensions, or notes being removed in the revision. The original text must remain readable beneath the strikethrough. |

### Direction and Reference Symbols

| Symbol | Name | Description | When to Use |
|---|---|---|---|
| **Straight arrow** | Direction Arrow | Arrow showing direction of flow, movement, or reference | Pipe flow direction, traffic flow, material handling routes, access paths. Arrow points in the direction of movement. |
| **Arrow with tail flags** | North Arrow | Arrow indicating geographic north | Must appear on every plan sheet. Supplement with construction north if different from true north. |
| **Circle with line and arrows** | Section Cut | Circle split horizontally; top half shows section ID, bottom shows drawing number. Arrows point in viewing direction. | Place on plan to indicate where a section cut is taken. Arrows point toward the side the viewer is looking at. |
| **Circle with number over number** | Detail Bubble | Circle split horizontally; top number is detail ID, bottom is sheet number | Reference to a detail drawing. Place at the location on the plan where the detail condition occurs. |
| **Dashed line with label** | Match Line | Dashed line across the drawing with sheet references on each side | Indicates where one drawing ends and the adjacent drawing continues. Labels show the adjacent sheet numbers. |
| **Zigzag line** | Break Line | Zigzag or wavy line indicating the drawing is not continuous | Used when an element is too long to show at scale. The break indicates omitted length. |

### Inspection and Quality Symbols

| Symbol | Name | Description | When to Use |
|---|---|---|---|
| **Diamond** | Hold Point | Solid or outlined diamond shape | Marks locations where work must stop for required inspection. Place at the physical location on the plan. |
| **Circle with X** | Deficiency Mark | Circle with X through it, or standalone X | Marks locations with deficient work. Used on punch lists and QC walkthrough drawings. |
| **Checkmark** | Verification Mark | Standard checkmark symbol | Marks locations where work has been inspected and approved. Often paired with date and initials. |
| **Star** | Attention/Flag | Five-pointed star or asterisk | Calls special attention to an item. Used for high-priority notes, critical dimensions, or unusual conditions. |
| **Circle with number** | Callout Bubble | Numbered circle with optional leader line | Sequential reference to a legend, punch list, or note table. Number corresponds to the item in the list. |

---

## 2. COLOR CONVENTIONS BY DISCIPLINE

### Primary Discipline Colors

Color coding is the fastest way to identify which trade or discipline a markup belongs to. These conventions are widely used across the US commercial construction industry, though some projects may adopt variations.

| Discipline | Color | Hex Code | RGB | Line Style | Rationale |
|---|---|---|---|---|---|
| **Architectural** | Black | #000000 | (0, 0, 0) | Solid | Matches the base drawing color; architectural is the primary discipline on arch sheets |
| **Structural** | Red | #FF0000 | (255, 0, 0) | Solid | High visibility; structural changes are critical and must not be missed |
| **Mechanical (HVAC)** | Green | #008000 | (0, 128, 0) | Solid | Industry convention; green for mechanical systems |
| **Electrical** | Blue | #0000FF | (0, 0, 255) | Solid | Industry convention; blue for electrical systems |
| **Plumbing** | Purple | #800080 | (128, 0, 128) | Solid | Distinguishes plumbing from mechanical and electrical |
| **Fire Protection** | Red | #FF0000 | (255, 0, 0) | Dashed | Same red as structural but dashed to differentiate; red signals life safety |
| **Civil/Sitework** | Brown | #8B5A2B | (139, 90, 43) | Solid | Earth tones for site and civil work |
| **Landscaping** | Dark Green | #006400 | (0, 100, 0) | Solid | Darker green distinguishes from mechanical green |
| **Safety** | Orange | #FF8C00 | (255, 140, 0) | Solid | OSHA orange; immediately recognized as safety-related |
| **Telecommunications** | Light Blue | #4169E1 | (65, 105, 225) | Solid | Lighter blue distinguishes from power electrical |
| **Owner/Design** | Cyan | #00C8C8 | (0, 200, 200) | Solid | Neutral color for non-trade-specific markup |

### Secondary and Special-Purpose Colors

| Purpose | Color | Hex Code | Usage |
|---|---|---|---|
| **RFI Markup** | Magenta | #FF00FF | Designates markup specifically related to RFI questions and responses |
| **As-Built Changes** | Red | #FF0000 | All as-built deviations from design shown in red regardless of discipline |
| **As-Built Verified** | Green | #008000 | Elements verified as matching design intent |
| **As-Built Information** | Blue | #0000FF | Informational notes on as-built drawings |
| **Demolition** | Gray | #808080 | Elements to be demolished or removed |
| **Existing to Remain** | Light Gray | #C0C0C0 | Existing elements that are not part of the current scope |
| **Proposed** | Dashed (any color) | varies | Proposed solutions or alternatives shown with dashed lines in the applicable discipline color |

### Multi-Discipline Conflict Resolution

When markups from multiple disciplines appear on the same sheet, follow this visibility priority:
1. **Safety** (orange) -- always visible, never obscured
2. **Structural** (red, solid) -- structural changes are critical path
3. **Fire Protection** (red, dashed) -- life safety systems
4. **Mechanical** (green) -- typically the largest MEP system spatially
5. **Electrical** (blue) -- often routed around mechanical
6. **Plumbing** (purple) -- smaller footprint, higher priority routing
7. **Architectural** (black) -- base information

When two markups overlap, offset the lower-priority markup slightly or add a discipline label to distinguish.

---

## 3. LINE WEIGHT CONVENTIONS

### Standard Line Weights for Markup

Line weight communicates the significance and type of markup. Heavier lines draw attention; lighter lines provide supporting information.

| Weight | Points | Pixels (screen) | Usage |
|---|---|---|---|
| **Heavy** | 2.0 pt | 3 px | Revision clouds, zone boundaries, as-built redlines, safety barriers |
| **Medium** | 1.0 pt | 2 px | Dimension lines, leader lines, section cuts, general markup |
| **Light** | 0.5 pt | 1 px | Reference lines, hatching, grid references, background annotations |
| **Extra Heavy** | 3.0 pt | 4 px | Safety exclusion zones, critical hold boundaries (use sparingly) |

### Line Style Conventions

| Style | Pattern | Usage |
|---|---|---|
| **Solid** | Continuous | Primary markup, confirmed elements, installed conditions |
| **Dashed** | Long dash (10pt dash, 5pt gap) | Proposed elements, future work, hidden/above elements |
| **Dotted** | Short dash (2pt dash, 2pt gap) | Reference lines, alignment indicators, projection lines |
| **Chain** | Long-short-long (10-2-4-2) | Property lines, centerlines, match lines |
| **Cloud** | Continuous arc segments | Revision areas, change boundaries |

---

## 4. CLOUD MARKUP RULES

### Revision Cloud Standards

Revision clouds are the most commonly used markup element. Proper cloud construction ensures readability and professional appearance.

**Arc Specifications**
- Arc radius: 0.10" to 0.20" (3mm to 5mm) per arc segment at full scale
- Arc direction: Arcs curve outward (convex side faces away from the enclosed area)
- Arc consistency: All arcs in a single cloud should be approximately the same radius
- Cloud closure: The cloud must fully close; no gaps in the perimeter
- Minimum size: Cloud must be large enough to clearly identify the enclosed area; minimum 1" x 1" at full scale

**Revision Cloud Types**

| Type | Line Weight | Color | Purpose |
|---|---|---|---|
| **Design Revision** | Heavy (2pt) | Red | Encloses area changed by a design revision (ASI, SK, bulletin) |
| **RFI Reference** | Heavy (2pt) | Magenta | Encloses area referenced by an RFI question |
| **Field Deviation** | Heavy (2pt) | Red | Encloses area where field conditions differ from design |
| **Hold Zone** | Extra Heavy (3pt) | Red | Encloses area where work must stop pending resolution |
| **Coordination** | Medium (1pt) | Varies by discipline | Encloses area requiring multi-trade coordination |
| **Information** | Light (0.5pt) | Blue | Encloses area for reference or informational purposes |

**Cloud Interior Treatment**
- Revision clouds: Interior left clear (no fill)
- Hold zones: Interior filled with semi-transparent red (10% opacity) or hatched with diagonal lines
- Safety zones: Interior filled with semi-transparent orange (10% opacity) or cross-hatched
- Work areas: Interior filled with semi-transparent discipline color (5-10% opacity)

---

## 5. TEXT ANNOTATION STANDARDS

### Font Specifications

| Element | Font Family | Size | Weight | Case |
|---|---|---|---|---|
| **Primary note** | Helvetica / Arial | 12pt | Regular | Sentence case |
| **Secondary note** | Helvetica / Arial | 10pt | Regular | Sentence case |
| **Reference text** | Helvetica / Arial | 8pt | Regular | Sentence case |
| **Label** | Helvetica / Arial | 10pt | Bold | UPPERCASE |
| **Title** | Helvetica / Arial | 14pt | Bold | UPPERCASE |
| **Dimension text** | Helvetica / Arial | 10pt | Regular | Standard notation |
| **Callout number** | Helvetica / Arial | 12pt | Bold | Numeric |

### Callout Format Standards

**Leader Line Callouts**
- Leader line starts at the annotation text block and terminates at the target location with an arrowhead
- Leader line should have one bend maximum (horizontal-to-angled or angled-to-horizontal)
- Arrowhead: closed triangle, 8pt length, pointing at the target element
- Text block placed in clear area away from dense drawing content
- Leader line minimum length: 0.5" from text block to target (avoid cramped leaders)

**Text Block Formatting**
- White or light yellow background rectangle behind text (90% opacity for readability)
- 2pt padding between text and background edge
- Optional 0.5pt black border around background rectangle
- Text aligned left within the block
- Multiple lines allowed; keep to 3 lines maximum per annotation

**Prefix Conventions**
- `NOTE:` -- General field note or observation
- `RFI-###:` -- RFI-related annotation
- `PUNCH #:` -- Punch list item annotation
- `HOLD:` -- Hold point or stop work annotation
- `VERIFY:` -- Item requiring field verification
- `ASI-###:` -- Architect's Supplemental Instruction markup
- `CO-###:` -- Change order related markup
- `COORD:` -- Coordination markup between trades

---

## 6. PHOTO MARKUP CONVENTIONS

### Deficiency Photo Markup

Field photos documenting deficiencies require clear, consistent annotation so that trades can identify the problem and location without additional explanation.

**Required Elements on Every Deficiency Photo**
1. **Deficiency Marker**: Red circle or arrow pointing to the deficient condition
2. **Item Number**: Circled number corresponding to the punch list or deficiency log
3. **Description**: Text box with brief description of the deficiency (2 lines maximum)
4. **Location Stamp**: Lower-left corner text showing Building, Level, Room/Area, Grid Reference
5. **Date Stamp**: Lower-right corner text showing date and time of photo capture
6. **Responsible Trade**: Color-coded banner or text indicating the responsible trade

**Annotation Placement Rules**
- Markers and arrows must point directly at the deficiency, not at adjacent elements
- Text boxes placed in areas of the photo with minimal visual information (sky, floor, wall surfaces)
- No annotation should obscure the deficiency itself
- Multiple deficiencies in one photo: number each with leader lines, avoid crossing leaders
- Minimum text size: 14pt equivalent at output resolution (readable on phone screen)

**Measurement Overlays**
- Dimension lines drawn between reference points with measurement value at midpoint
- Actual measurement shown in red; required measurement shown in blue (parenthetical)
- Example: `3'-2" (REQ: 3'-0")` showing 2" deviation from requirement
- Use white background behind dimension text for readability

### Before/After Photo Pairs

| Element | "Before" Photo | "After" Photo |
|---|---|---|
| **Header label** | "BEFORE" in red banner, top-left | "AFTER" in green banner, top-left |
| **Deficiency marks** | Red X, arrows, callouts on deficiency | Green checkmark at corrected location |
| **Item reference** | Punch item number and description | Same punch item number, "CORRECTED" |
| **Date stamp** | Date of deficiency identification | Date of correction verification |
| **Layout** | Left side of comparison | Right side of comparison |

### Progress Photo Markup

Progress photos benefit from annotations showing what has been completed and what is upcoming:
- Green shading over completed work areas
- Yellow shading over in-progress work areas
- Red shading over areas not yet started
- Annotation labels for each area with activity description and completion percentage
- Directional arrows showing work progression sequence

---

## 7. DIGITAL MARKUP TOOL GUIDANCE

### Bluebeam Revu Conventions

Bluebeam Revu is the industry-standard PDF markup tool for construction. When producing programmatic annotations that will be viewed or supplemented in Bluebeam, follow these conventions:

**Layer Naming**
- Use the Bluebeam layer naming convention: `[Discipline]-[Type]` (e.g., "Mechanical-RFI", "Structural-AsBuilt")
- Annotations placed on named layers are toggleable in Bluebeam's Layers panel

**Markup Properties**
- Line colors: use Bluebeam's default palette colors for consistency with manual markups
- Cloud markup: Bluebeam's default cloud arc radius is 0.1875"; match this for visual consistency
- Text markup: Bluebeam defaults to 12pt Arial; match for consistency
- Callout markup: Bluebeam uses a rounded-rectangle callout box with leader; match this style

**Studio Sessions**
- Annotations produced by this skill should be compatible with Bluebeam Studio Session workflows
- Use standard PDF annotation types (not proprietary Bluebeam-only markup) for maximum compatibility
- Test output PDFs in Bluebeam to verify annotation visibility and layer assignment

### PlanGrid / Autodesk Build Conventions

PlanGrid (now part of Autodesk Build) uses a simplified markup system:

**Markup Types Supported**
- Pen tool (freehand), text, arrow, shape (rectangle, circle, cloud), photo link, measurement
- Markups stored per-sheet and linked to document version
- Markups visible on mobile devices (iPad, phone) in the field

**Compatibility Considerations**
- PlanGrid does not support PDF layers; all annotations appear on a single markup layer
- PlanGrid stores markups as overlays, not embedded in the PDF
- For PlanGrid compatibility, produce annotation overlays as separate PNG images with transparency

### Procore Markup Conventions

Procore's drawing markup system:

**Markup Features**
- Pen, text, shape, arrow, cloud, measurement, photo pin
- Markups linked to Procore observations, RFIs, and punch items
- Drawing versions tracked; markups can carry forward to new revisions

**Integration Notes**
- Procore allows PDF upload with embedded annotations
- For best results, flatten annotations into the PDF before uploading to Procore
- Procore observation pins can reference annotated drawing locations

---

## 8. INDUSTRY-STANDARD MARKUP ABBREVIATIONS

### Common Abbreviations Used in Markup Annotations

| Abbreviation | Meaning | Context |
|---|---|---|
| **NIC** | Not In Contract | Scope exclusion markup |
| **NTS** | Not To Scale | Sketch or detail markup |
| **TYP** | Typical | Applies to all similar conditions |
| **SIM** | Similar | Similar to the referenced condition |
| **EQ** | Equal | Equal spacing or equal dimension |
| **UNO** | Unless Noted Otherwise | Default condition with exceptions |
| **VIF** | Verify In Field | Requires field measurement |
| **EJ** | Expansion Joint | Joint location markup |
| **CJ** | Control Joint | Joint location markup |
| **CLR** | Clear / Clearance | Clearance dimension |
| **ABV** | Above | Elevation reference |
| **BLW** | Below | Elevation reference |
| **FF** | Finish Floor | Elevation datum |
| **TOS** | Top Of Steel | Elevation datum |
| **TOC** | Top Of Concrete | Elevation datum |
| **TOW** | Top Of Wall | Elevation datum |
| **BOD** | Bottom Of Deck | Elevation datum |
| **INV** | Invert | Pipe invert elevation |
| **CL** | Centerline | Alignment reference |
| **GL** | Grid Line | Grid reference |
| **EL** | Elevation | Elevation dimension |
| **DIM** | Dimension | Dimensional markup |
| **REF** | Reference | Cross-reference |
| **REV** | Revision | Revision markup |
| **ASI** | Architect's Supplemental Instruction | Design change reference |
| **SK** | Sketch | Design sketch reference |
| **PR** | Proposal Request | Cost-related change reference |
| **CO** | Change Order | Approved change reference |
| **CCD** | Construction Change Directive | Directed change reference |
| **RFI** | Request For Information | Information request reference |
| **SUB** | Submittal | Submittal reference |

### Dimension Notation Conventions

| Format | Meaning | Example |
|---|---|---|
| `12'-6"` | Feet and inches | Standard architectural dimension |
| `12.5'` | Decimal feet | Civil/survey notation |
| `150.00"` | Decimal inches | Machine/precision notation |
| `+/-` | Plus or minus tolerance | `12'-6" +/- 1/4"` |
| `(field)` | Field-measured value | `12'-6 1/4" (field)` vs. `12'-6" (design)` |
| `HOLD` | Dimension to be confirmed | `HOLD 12'-6" -- VIF` |

### Status Annotations

| Annotation | Meaning | Color |
|---|---|---|
| **APPROVED** | Work inspected and accepted | Green |
| **REJECTED** | Work inspected and not accepted | Red |
| **HOLD** | Work must stop, pending resolution | Red with yellow background |
| **PENDING** | Awaiting inspection or decision | Orange |
| **VERIFY** | Requires field verification | Blue |
| **REVISED** | Element has been revised | Red with revision delta |
| **DEMOLISHED** | Element has been removed | Gray with strikethrough |
| **EXISTING** | Existing condition, not new work | Light gray |
| **PROPOSED** | Proposed but not yet approved | Dashed lines in discipline color |
| **AS-BUILT** | Field-verified actual condition | Red with checkmark |
