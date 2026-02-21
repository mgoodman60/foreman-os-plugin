# Construction Document Conventions — How Drawings Actually Work

**A practical guide for AI systems parsing construction PDFs.** This reference teaches the visual grammar, navigation system, and calculation methods that every superintendent and project engineer knows intuitively. Read this BEFORE attempting to extract data from construction drawings.

---

## Why This Matters

Construction documents are not just "documents with text." They are a **coordinated visual communication system** with strict conventions developed over 150+ years. Understanding these conventions lets you:

- **Navigate a 200-page set in seconds** instead of reading page by page
- **Follow cross-references** between drawings to build complete data
- **Derive quantities** from dimensions even when they aren't explicitly stated
- **Recognize what you're looking at** based on line types, symbols, and layout
- **Know where to find specific information** based on sheet numbering alone

---

## 1. Sheet Numbering — Your Navigation System

### The NCS Standard Format

Sheet numbers follow the pattern: **[Discipline][Sheet Type]-[Sequence]**

#### Discipline Designators (First Letter)

| Letter | Discipline | What You'll Find |
|--------|-----------|-----------------|
| **G** | General | Cover sheet, code analysis, life safety plans, abbreviation legends |
| **C** | Civil/Site | Site plan, grading, utilities, paving, landscaping |
| **L** | Landscape | Planting plans, irrigation, hardscape details |
| **A** | Architectural | Floor plans, elevations, sections, interior details, schedules |
| **S** | Structural | Foundation plans, framing plans, structural details |
| **M** | Mechanical | HVAC plans, ductwork, equipment schedules |
| **P** | Plumbing | Piping plans, fixture schedules, riser diagrams |
| **E** | Electrical | Power plans, lighting plans, panel schedules |
| **FP** | Fire Protection | Sprinkler layouts, riser diagrams, FDC locations |

#### Sheet Type Ranges (Second Digit Group)

Within each discipline, sheet types progress from general → specific → details → schedules:

| Range | Type | Examples |
|-------|------|---------|
| **-001 to -009** | General (notes, symbols, legends) | A-001 = Architectural Notes & Symbols |
| **-100 to -199** | Plans (floor plans, site plans) | A-101 = First Floor Plan, A-102 = Second Floor Plan |
| **-200 to -299** | Elevations | A-201 = Exterior Elevations |
| **-300 to -399** | Sections & wall sections | A-301 = Building Sections |
| **-400 to -499** | Details (enlarged) | A-401 = Interior Details |
| **-500 to -599** | Schedules | A-501 = Door/Window/Finish Schedules |
| **-600 to -699** | Reflected ceiling plans | A-601 = RCP First Floor |

### Practical Navigation Strategy

**To find specific information, go directly to the right sheet type:**

| You Need | Go To | Sheet Range |
|----------|-------|-------------|
| Room layout and dimensions | Floor plans | A-100s |
| Door sizes, types, hardware | Door schedule | A-500s |
| Finish materials by room | Finish schedule | A-500s |
| Concrete specs, rebar | Structural general notes | S-001 |
| Foundation layout | Structural foundation plan | S-100s |
| HVAC equipment | Mechanical schedule | M-500s |
| Electrical panel info | Electrical panel schedule | E-500s |
| Site utilities | Civil plans | C-100s |
| Building sections | Architectural sections | A-300s |

**CRITICAL**: Always start with the **sheet index** (usually on G-001 or the cover sheet). This lists every sheet in the set with its number and title. Build your navigation map from this index.

---

## 2. The Cross-Reference System — How Drawings Link Together

Construction drawings are not standalone pages. They form a **web of cross-references** where every drawing points to related drawings. Understanding this system is how you trace an element through multiple views to get complete information.

### Section Cut Markers

**What they look like:** A bold line drawn across a plan with a circle at one or both ends.

**How to read them:**
```
    ┌───┐
    │ A │  ← Section identifier (letter or number)
    ├───┤
    │301│  ← Sheet number where this section is drawn
    └───┘
      │
══════╪══════  ← Cut line (heavy line through the plan)
      │
      ▼        ← Arrow shows the direction you're looking
```

**Example:** A section marker labeled "A / A-301" on the first floor plan means: "Look at sheet A-301 to see Section A — a vertical slice through the building at this location, looking in the direction the arrow points."

**Why it matters for extraction:** When you see a section cut through a wall or foundation on a plan, the *section view* on the referenced sheet will show the internal assembly — wall thickness, insulation, structural framing, material layers. You need BOTH views to fully understand the construction.

### Detail Callout Markers

**What they look like:** A circle (or circle-with-tail) placed at a specific spot on a drawing.

**How to read them:**
```
    ┌───┐
    │ 3 │  ← Detail number
    ├───┤
    │401│  ← Sheet number where the detail is drawn
    └───┘
```

**Example:** A callout "3 / A-401" on a building section means: "Look at sheet A-401, find Detail 3, for an enlarged view of this connection/assembly."

**Why it matters:** Details are drawn at **larger scale** (½" = 1'-0" or 1" = 1'-0" vs ¼" = 1'-0" for plans). They show fasteners, sealants, flashing, material layers, and dimensions that are too small to show on the plan. This is where you find the specific construction information.

### Elevation Markers

**What they look like:** A circle with an arrow pointing toward a building face.

**How to read them:**
```
    ┌───┐
    │ 1 │  ← Elevation identifier
    ├───┤
    │201│  ← Sheet where elevation is drawn
    └───┘
  ───►       ← Arrow points toward the face being shown
```

### Assembly Chains — Following an Element Across Multiple Sheets

A single building element may appear on 3-5 different sheets:

**Example — Footing F1:**
1. **S-101** (Foundation Plan): Shows footing location in plan, dimensions, grid references
2. **S-301** (Foundation Section): Shows footing cross-section, depth, relationship to wall above
3. **S-501** (Foundation Details): Shows rebar placement, concrete cover, dowel details
4. **S-001** (Structural Notes): Shows concrete strength (PSI), rebar grade, curing requirements
5. **Spec Section 03 30 00**: Shows detailed concrete mix requirements, testing, weather thresholds

**To calculate the full material quantity for Footing F1, you need data from ALL of these sources.** The plan gives you the linear footage, the section gives you the cross-section dimensions, the details give you the rebar, and the notes/specs give you the concrete requirements.

---

## 3. Drawing Types and Their Relationships

### Plan Views — Looking Down

A floor plan is a **horizontal slice** through the building, typically cut at about 4 feet above the floor. Everything below the cut shows as solid lines. Everything above shows as dashed lines (like cabinets mounted on the wall above, or beams overhead).

**What plan views show:** Room layout, wall locations, door swings, window locations, fixtures, equipment, dimensions, room tags, door tags, grid lines.

**What plan views DON'T show:** Wall assembly details, heights of elements, material layers, structural depth, items concealed in walls/ceilings.

### Reflected Ceiling Plans (RCPs) — Looking Up

**CRITICAL — Currently missing from extraction rules.**

An RCP shows the ceiling as if you're looking UP at it from the floor (or as if a mirror on the floor reflected the ceiling back at you). The orientation matches the floor plan — left is still left, right is still right.

**What RCPs show:**
- Ceiling material and finish (ACT grid, drywall, exposed structure)
- Ceiling heights (especially height changes and soffits)
- Light fixture locations and types (referenced to lighting schedule)
- HVAC diffuser and return air locations
- Sprinkler head locations
- Smoke detector locations
- Speaker and AV equipment locations

**Why RCPs matter:** They are the **primary coordination document** for MEP trades. If you need to know what's happening above the ceiling — ductwork routing, lighting layout, sprinkler coverage — the RCP is where you look.

**Sheet numbering:** Typically A-601, A-602 (Architectural RCPs) or sometimes on the MEP sheets.

### Sections — Vertical Slices

A building section is a **vertical slice** through the building. It reveals what's hidden inside walls, floors, and roofs.

**Line weight convention in sections:**
- **Heaviest lines:** Elements cut by the section plane (the wall/floor/roof you're slicing through)
- **Medium lines:** Elements visible beyond the cut (things you can see looking past the slice)
- **Light lines:** Distant background elements

**What sections show:** Floor-to-floor heights, wall assembly layers, structural depth, foundation-to-roof relationship, ceiling heights, material thicknesses, insulation locations.

### Details — Enlarged Views

Details zoom into a specific area at a larger scale. A connection that's 2 inches on a plan becomes 6 inches on a detail, making it possible to show every layer, fastener, and dimension.

**Common detail scales:** ½" = 1'-0", ¾" = 1'-0", 1" = 1'-0", 1½" = 1'-0", or full size.

**Key plan:** Many detail sheets include a small "key plan" — a miniature floor plan showing exactly where each detail is located. This helps you understand the context.

---

## 4. Scale — How to Derive Measurements

### The Scale Hierarchy

1. **Written dimensions ALWAYS take priority** over scaled measurements
2. **Graphic scale bar** is more reliable than noted scale (prints may be reproduced at different sizes)
3. **Noted scale** (in title block) is the intended scale but may not match the actual print

### Common Drawing Scales

| Drawing Type | Typical Scale | What 1 Inch Represents |
|-------------|--------------|----------------------|
| Site plan | 1" = 20' to 1" = 60' | 20-60 feet |
| Floor plan | ¼" = 1'-0" | 4 feet |
| Floor plan (large buildings) | ⅛" = 1'-0" | 8 feet |
| Elevations | ¼" = 1'-0" | 4 feet |
| Building sections | ¼" = 1'-0" or ⅜" = 1'-0" | 4 or 2.67 feet |
| Wall sections | ¾" = 1'-0" or 1" = 1'-0" | 1.33 or 1 foot |
| Details | 1½" = 1'-0" or 3" = 1'-0" | 8 or 4 inches |
| Full-size details | Full size (1:1) | 1 inch |

### How to Verify Scale from a PDF

Since Claude is reading PDFs (not paper prints), scale verification works like this:

1. **Find the graphic scale bar** on the sheet (a ruler-like bar with distance markings)
2. **Measure the scale bar in pixels** — for example, the bar shows "0 to 10 feet" and measures 400 pixels
3. **Calculate pixels per foot:** 400 pixels ÷ 10 feet = 40 pixels/foot
4. **Use this ratio** to measure other distances on the same sheet

**Backup method:** If no scale bar is present, find a known dimension:
- Standard door = 3'-0" wide (most common)
- Standard ceiling height = 9'-0" or 10'-0"
- CMU block = 8" × 16" face
- Grid spacing is often dimensioned

### When NOT to Scale

- **"NTS" (Not To Scale)** on a drawing means do not measure from it
- **Sketches and diagrams** with no scale noted
- **Drawings that have been enlarged or reduced** — check the scale bar first
- **Details showing "typical" conditions** that may not be drawn to exact proportions

---

## 5. Quantity Calculations from Drawings

### The Fundamental Formulas

Claude should be able to take dimensions extracted from drawings and **automatically calculate** material quantities. These are the core formulas every estimator uses:

#### Concrete (Cubic Yards)

```
CY = (Length ft × Width ft × Thickness ft) ÷ 27
```

**By element type:**

| Element | How to Calculate | Waste Factor |
|---------|-----------------|-------------|
| Slab on grade | Length × Width × Thickness ÷ 27 | +5% |
| Spread footing | Length × Width × Depth ÷ 27 | +5% |
| Continuous footing | Cross-section area × Linear feet ÷ 27 | +5% |
| Foundation wall | Length × Height × Thickness ÷ 27 | +5% |
| Column | π × r² × Height ÷ 27 (round) or L × W × H ÷ 27 (square) | +5% |
| Elevated slab | Length × Width × Thickness ÷ 27 | +8% (formwork losses) |
| Sloped slab | L × W × [(min thickness + max thickness) ÷ 2] ÷ 27 | +8% |

**Quick reference:** 1 CY covers 81 SF at 4" thick, 54 SF at 6" thick, 27 SF at 12" thick.

#### Earthwork (Cubic Yards)

```
CY = (Length ft × Width ft × Depth ft) ÷ 27
```

**Compaction factors:**
- Bank (in-ground) to Loose (in truck): multiply by 1.25-1.30
- Bank to Compacted (in fill): multiply by 0.85-0.90
- Loose to Compacted: multiply by 0.70-0.75

**Shrinkage allowance:** Add 15% (multiply by 1.15) for compacted fill volumes to account for shrinkage during compaction.

**Trapezoidal excavation:** CY = ½ × (Top width + Bottom width) × Depth × Length ÷ 27

#### Drywall / Sheathing (Sheets or SF)

```
Sheets = (Wall perimeter LF × Wall height) ÷ 32 SF per 4×8 sheet
```

- Add 10-15% for waste (cuts, corners, openings)
- Subtract openings larger than 4×4 (small openings don't save material due to cutting waste)
- For ceilings: Length × Width ÷ 32

#### Masonry (Blocks or Bricks)

```
CMU blocks = Wall SF ÷ 0.89 SF per block (standard 8×16 CMU)
Bricks = Wall SF × 6.75 bricks per SF (standard modular brick with 3/8" mortar joint)
```

- Add 5% for waste/breakage
- Subtract 50% of opening areas (you still need blocks for headers and jambs)

#### Paint / Coatings (SF)

```
Wall SF = Wall perimeter LF × Wall height − Door/window openings SF
Ceiling SF = Room length × Room width
Total SF = Wall SF + Ceiling SF (if painting both)
```

- Coverage rate per gallon varies by product (typically 350-400 SF/gallon for first coat)
- Two coats = double the paint quantity

#### Flooring (SF)

```
Room SF = Length × Width (for rectangular rooms)
```

- VCT/LVT: Add 10% waste for cuts
- Carpet: Add 10-15% waste (depends on seam layout and pattern match)
- Tile: Add 10-15% waste for cuts (more waste for diagonal patterns or small tiles)

#### Linear Items (Pipe, Conduit, Wire)

```
Total LF = Sum of all horizontal runs + Sum of all vertical drops + Fitting allowances
```

- Add 10-15% for fittings, bends, and connections
- For wire/cable: add length for drops from ceiling to devices + service loops
- Measure from **centerline** of pipe runs, not edge to edge

#### Rebar

```
Weight (lbs) = Total LF × Weight per LF (by bar size)
```

| Bar Size | Weight per LF | Common Use |
|----------|--------------|------------|
| #3 | 0.376 lbs/ft | Stirrups, ties |
| #4 | 0.668 lbs/ft | Slabs, light walls |
| #5 | 1.043 lbs/ft | Footings, walls |
| #6 | 1.502 lbs/ft | Foundations, beams |
| #7 | 2.044 lbs/ft | Heavy foundations |
| #8 | 2.670 lbs/ft | Columns, heavy beams |

- Add lap splice lengths (typically 24"-48" per splice depending on bar size)
- Add development lengths at bends and hooks
- Standard rebar comes in 20' or 40' lengths — calculate number of splices needed

### Breaking Complex Shapes Into Simple Ones

When rooms or areas are not rectangular:

1. Divide the irregular shape into **rectangles and triangles**
2. Calculate each sub-area separately
3. Sum all sub-areas
4. For L-shaped rooms: split into two rectangles
5. For rooms with angled walls: rectangle + triangle
6. For curved walls: approximate with multiple straight segments

### The "Typical" Multiplier

When drawings say **"TYP"** (typical), it means this condition repeats:

- "30'-0" TYP" between grid lines = every bay is 30 feet
- 6 bays × 30' = 180' total building length
- A footing detail marked "TYP" applies to all similar footings

**"SIM"** (similar) means close but check for differences.
**"EQ"** (equal) means equally spaced — total length ÷ number of spaces = spacing.
**"NTS"** (not to scale) means don't measure from the drawing.
**"UNO"** (unless noted otherwise) means this is the default but exceptions exist.

---

## 6. Common Construction Abbreviations on Drawings

These abbreviations appear constantly on construction documents. Claude must recognize them to correctly interpret notes, schedules, and dimensions:

### Dimensional
- **O.C.** = On Center (spacing measured center-to-center)
- **CLR** = Clear (unobstructed dimension)
- **NOM** = Nominal (named size, not actual — a 2×4 is actually 1½" × 3½")
- **MAX / MIN** = Maximum / Minimum
- **±** = Plus or minus (tolerance)
- **EQ** = Equal spacing
- **TYP** = Typical (this condition repeats)
- **SIM** = Similar
- **NTS** = Not to scale
- **UNO** = Unless noted otherwise

### Elevation & Location
- **FFE** = Finished Floor Elevation
- **TOS** = Top of Steel
- **TOW** = Top of Wall
- **TOC** = Top of Concrete (or Top of Curb)
- **BOS** = Bottom of Slab (or Bottom of Steel)
- **BOF** = Bottom of Footing
- **FG** = Finish Grade
- **EG** = Existing Grade
- **AFF** = Above Finished Floor
- **BFF** = Below Finished Floor
- **CL / ℄** = Centerline

### Materials
- **CONC** = Concrete
- **CMU** = Concrete Masonry Unit (block)
- **GWB** = Gypsum Wallboard (drywall)
- **ACT** = Acoustic Ceiling Tile
- **VCT** = Vinyl Composition Tile
- **LVT** = Luxury Vinyl Tile
- **FRP** = Fiberglass Reinforced Panel
- **HM** = Hollow Metal (steel door/frame)
- **WD** = Wood
- **AL** = Aluminum
- **STL** = Steel
- **SST** = Stainless Steel
- **GI** = Galvanized Iron
- **WWF** = Welded Wire Fabric (mesh reinforcing)
- **RCP** = Reinforced Concrete Pipe (in civil) OR Reflected Ceiling Plan (in architectural)

### Structural
- **PSI** = Pounds per Square Inch (concrete strength)
- **PSF** = Pounds per Square Foot (loading)
- **KSI** = Kips per Square Inch (steel stress)
- **w/c** = Water-to-cement ratio
- **f'c** = Specified compressive strength of concrete
- **fy** = Yield strength of reinforcing steel

---

## 7. Line Types — What Different Lines Mean

Understanding line conventions helps Claude interpret what a drawing is showing, especially in visual analysis:

### Solid Lines (Continuous)

| Weight | Meaning |
|--------|---------|
| **Heavy** | Section cut plane, building outline, major structural elements |
| **Medium** | Visible object edges, wall outlines, equipment outlines |
| **Light** | Dimension lines, leader lines, hatching, minor details |

### Dashed Lines

| Pattern | Meaning |
|---------|---------|
| **Short dashes** | Hidden/concealed elements (behind or above the cut plane) |
| **Long dashes** | Overhead elements shown on floor plans (beams, soffits) |
| **Dash-dot-dash** | Centerlines, axes of symmetry, grid lines |
| **Dash-dot-dot-dash** | Property lines, boundary lines |
| **Long-short-long** | Phantom/reference lines (elements from other drawings shown for context) |

### Special Lines

| Line | Meaning |
|------|---------|
| **Zigzag or wavy break** | Drawing is broken — middle section omitted for space |
| **Crossed diagonal hatching** | Demolished/removed work |
| **Cloud border** | Revision — this area was changed since last issue |
| **Heavy with arrows** | Section cut line (follow to find the section view) |

---

## 8. Hatch Patterns — Material Identification

In section views and details, materials are shown with standard fill patterns:

| Pattern | Material |
|---------|----------|
| **Diagonal lines (45°)** | Earth/soil (in section) |
| **Stipple (dots)** | Concrete |
| **Cross-hatch (X pattern)** | Steel or metal |
| **Wavy lines** | Insulation (batt) |
| **Diagonal with dots** | Sand or gravel |
| **Brick pattern** | Masonry/brick |
| **Parallel lines (close)** | Wood (end grain) |
| **Random circles** | Gravel/aggregate |
| **Solid black** | Steel (in small sections) or rubber/waterproofing |
| **Honeycomb** | Concrete masonry (CMU) |

**Why this matters:** In a wall section, hatch patterns tell you the material layers even if text labels are missing. This is critical for visual plan analysis when OCR may not capture all labels.

---

## 9. Efficient PDF Processing Strategy

### How to Navigate a Construction PDF Set

**Do NOT read page by page.** Instead:

1. **Find the sheet index** (G-001 or cover page) — build your map of what's in the set
2. **Read the Notes & Symbols sheet** (G-002 or discipline-specific -001 sheets) — learn the project's specific abbreviations, keynote system, and symbol legend
3. **Go directly to the sheets you need** based on the index and discipline designators
4. **Follow cross-references** from general → specific (plan → section → detail)
5. **Read schedules last** — they compile information from multiple plan sheets

### Processing Priority for Maximum Intelligence

| Order | Sheet Type | Why First |
|-------|-----------|-----------|
| 1 | Sheet index + cover | Builds the navigation map |
| 2 | Notes & symbols | Learns the drawing's "vocabulary" |
| 3 | Architectural floor plans (A-100s) | Establishes spatial framework — grids, rooms, layout |
| 4 | Structural foundation/framing (S-100s) | Adds structural grid, foundation layout |
| 5 | Architectural schedules (A-500s) | Door/window/finish data keyed to plan tags |
| 6 | Structural general notes (S-001) | Concrete specs, rebar, steel — critical field data |
| 7 | MEP plans (M/E/P-100s) | Equipment locations, system layouts |
| 8 | Sections and details (A-300s, A-400s) | Assembly details, material layers, connections |
| 9 | Civil/site plans (C-100s) | Site layout, utilities, grading |
| 10 | RCPs (A-600s) | Ceiling coordination, lighting, HVAC diffusers |

### What PDF Text Extraction Actually Produces

**Expect imperfect text from construction PDFs.** CAD-exported PDFs have specific quirks:

- **SHX fonts** (common in AutoCAD) render as line segments, NOT as selectable text. OCR or vision is required.
- **Text placement** in the PDF may not match visual layout — a room tag in the center of a room may appear at random coordinates in the text stream
- **Tables** (schedules) may extract as scrambled text rather than structured rows/columns
- **Dimensions** may extract without their associated dimension lines, losing context
- **Rotated text** (common in title blocks and along dimension lines) may not extract correctly
- **Symbols** (section markers, detail callouts, grid bubbles) are graphics, not text

**Implication:** For plan sheets, always supplement text extraction with **visual analysis** (Pass 4). Text extraction alone will miss a significant portion of construction drawing content.

---

## 10. Multi-Discipline Coordination

### How Drawing Sets Layer Together

Every MEP discipline (Mechanical, Electrical, Plumbing) uses the **architectural floor plan as a background**. They draw their systems ON TOP of the architectural layout. This means:

- Wall locations come from Architectural
- Column locations come from Structural
- Duct routing, equipment placement come from Mechanical
- Lighting, power, panels come from Electrical
- Piping, fixtures come from Plumbing

### Cross-Discipline References

| On This Sheet | You'll See References To |
|--------------|------------------------|
| Architectural plans | "See S-101 for foundation," "See M-101 for duct routing" |
| Structural plans | "Arch. background for reference only" |
| Mechanical plans | "Coordinate diffuser locations with RCP on A-601" |
| Electrical plans | "Panel LP-1, see panel schedule E-501" |
| Plumbing plans | "Fixture schedule P-501," "Coordinate with structural for floor penetrations" |

### The RCP as Coordination Hub

The Reflected Ceiling Plan is where Architectural, Mechanical, Electrical, and Fire Protection all converge:

- **Architect** sets ceiling type, heights, soffits
- **Mechanical** places diffusers and return grilles
- **Electrical** places light fixtures (keyed to lighting schedule)
- **Fire Protection** places sprinkler heads
- **Low Voltage** places speakers, smoke detectors, security devices

When any of these conflict (light fixture where a duct needs to go), it's caught on the RCP.

---

## 11. Elevation Datums and Benchmarks

### How Vertical Measurements Work

Construction drawings use **elevation datums** — fixed reference points for all vertical measurements. These are essential for calculating cut/fill, slab thickness, wall heights, and equipment placement.

**Common elevation abbreviations:**

| Abbreviation | Meaning | Used For |
|-------------|---------|----------|
| **FFE** | Finished Floor Elevation | Building floor level (the number one reference point) |
| **TOS** | Top of Steel | Steel beam/column elevations |
| **TOC** | Top of Concrete | Slab surface, curb top |
| **BOF** | Bottom of Footing | Footing excavation depth |
| **TOF** | Top of Footing | Footing surface (where walls bear) |
| **BOS** | Bottom of Slab/Steel | Underside of structure |
| **TOW** | Top of Wall | Wall height reference |
| **FG** | Finish Grade | Final ground surface |
| **EG** | Existing Grade | Current ground surface before work |
| **INV** | Invert | Inside bottom of pipe |
| **RIM** | Rim Elevation | Top of manhole/structure |

### Calculating from Datums

**Example — Foundation wall height:**
- FFE (Finished Floor) = 856.50'
- BOF (Bottom of Footing) = 852.00'
- Height = 856.50 - 852.00 = 4.50 feet (4'-6")

**Example — Earthwork cut depth:**
- EG (Existing Grade) = 858.00'
- BOF (Bottom of Footing) = 852.00'
- Cut depth = 858.00 - 852.00 = 6.00 feet

**Example — Slab thickness verification:**
- TOC (Top of Concrete slab) = 856.50'
- BOS (Bottom of Slab) = 856.17'
- Thickness = 856.50 - 856.17 = 0.33 feet = 4 inches ✓

---

## 12. Reading Dimension Strings

### Dimension Anatomy

A dimension on a drawing consists of:
1. **Extension lines** — thin lines extending from the object outward
2. **Dimension line** — thin line between extension lines with arrows/ticks at each end
3. **Dimension value** — the measurement text, placed above or centered on the dimension line

### Dimension String Chains

Dimensions are typically arranged in **chains** (strings):

```
|←— 12'-0" —→|←— 30'-0" —→|←— 30'-0" —→|←— 12'-0" —→|
|             |             |             |             |
|←————————————————— 84'-0" ————————————————————————→|
Grid 1       Grid 2       Grid 3       Grid 4       Grid 5
```

- **Inner string** = individual bay dimensions
- **Outer string** = overall dimension (should equal the sum of inner dimensions)
- **If they don't match**, there's an error on the drawings — flag it

### Reference Dimensions

Dimensions shown in **(parentheses)** or marked **"REF"** are reference dimensions — for information only, not for construction. They're derived from other dimensions and are there as a convenience. If a reference dimension conflicts with the primary dimensions, the primary dimensions govern.

### Dimension Priority Rules

1. **Written dimensions** take priority over scaling
2. **Specific dimensions** take priority over general notes
3. **Larger-scale drawing** dimensions take priority over smaller-scale
4. **Detail dimensions** take priority over plan dimensions
5. **Addendum/revision dimensions** take priority over original issue

---

## 13. Contour Lines, Grading Plans, and Site Work Calculations

### How Contour Lines Work

Contour lines are continuous lines connecting points of **equal elevation** above a fixed datum (typically sea level or a project benchmark). They are the primary way civil drawings represent three-dimensional terrain on a two-dimensional sheet.

**Key rules:**
- **Contour interval** = the vertical distance between adjacent contour lines (constant across the plan). Common intervals: 1' or 2' for small sites, 5' for large sites
- **Index contours** = every 5th contour is drawn **heavier/bolder** and labeled with its elevation (e.g., 850, 855, 860)
- **Intermediate contours** = the 4 lighter lines between index contours (unlabeled — calculate their elevation from the interval)
- **Closer spacing = steeper slope** — contour lines bunched together mean the ground is steep
- **Wider spacing = flatter ground** — contour lines spread apart mean gradual slope
- **V-shapes pointing uphill** = a valley or swale (water flows through the V)
- **V-shapes pointing downhill** = a ridge (water flows away from the V)
- **Closed contour circles** = hilltop or depression (look for hachure marks pointing inward = depression)

### Existing vs. Proposed Grade

This is one of the most critical distinctions on a grading plan:

| Feature | Existing (Before Work) | Proposed (After Work) |
|---------|----------------------|---------------------|
| **Contour lines** | Dashed or light lines | Solid or bold lines |
| **Spot elevations** | Marked with "×" or "(EG)" or in parentheses | Marked with "+" or "FG" or without parentheses |
| **Label convention** | "EG 856.00" or "(856.00)" | "FG 856.50" or "856.50" |

**To determine cut or fill at any point:**
```
Cut/Fill = Proposed Elevation − Existing Elevation
```
- **Positive result** = FILL needed (add soil to raise the grade)
- **Negative result** = CUT needed (remove soil to lower the grade)

### Spot Elevations

Spot elevations are specific elevation values at specific points, more precise than contour lines:

| Symbol | Meaning |
|--------|---------|
| **× 856.32** | Existing spot elevation |
| **+ 856.50** | Proposed/finished spot elevation |
| **FFE 856.50** | Finished Floor Elevation (building floor level) |
| **TC 857.20** | Top of Curb |
| **BC 856.70** | Bottom of Curb (flowline) |
| **TW 860.00** | Top of Wall |
| **INV 844.50** | Invert (inside bottom of pipe) |
| **RIM 856.20** | Rim elevation (top of manhole/structure) |
| **PAD 856.00** | Pad elevation (compacted subgrade below slab — typically 6-8" below FFE) |

**Priority rule:** When a contour line and a spot elevation appear to conflict, **trust the spot elevation** — it's more precise.

### Calculating Slope

```
Slope (%) = (Rise ÷ Run) × 100
```

- **Rise** = vertical change in elevation (feet)
- **Run** = horizontal distance (feet)

**Common slope requirements:**
| Surface | Typical Slope | Code Requirement |
|---------|--------------|-----------------|
| Parking lots | 1-5% | Min 1% for drainage |
| Sidewalks | 0.5-2% cross-slope | ADA max 2% cross-slope |
| ADA ramps | 5-8.33% | ADA max 8.33% (1:12) |
| Building perimeter | 2-5% away from building | Min 2% away for 10' (IRC) |
| Swales | 1-4% longitudinal | Per civil engineer |
| Storm pipe | 0.5-2% | Per civil design |

**Water flow direction:** Water flows **perpendicular to contour lines**, from high elevation to low. This tells you exactly where drainage goes on the site.

### Earthwork Volume Calculation Methods

There are three practical methods for calculating cut/fill volumes from grading plans. Claude should understand all three:

#### Method 1: Grid Method (Most Common for Building Pads)

1. **Overlay a grid** on the grading plan (typically 25' × 25' or 50' × 50' squares)
2. **At each grid intersection**, determine:
   - Existing elevation (from existing contours or survey)
   - Proposed elevation (from proposed contours or spot elevations)
   - Cut/fill depth = Proposed − Existing
3. **For each grid cell**, average the cut/fill depths at the four corners:
```
Average depth = (Corner1 + Corner2 + Corner3 + Corner4) ÷ 4
Cell volume (CF) = Average depth × Cell area (SF)
Cell volume (CY) = Cell volume (CF) ÷ 27
```
4. **Sum all CUT cells** and **sum all FILL cells** separately
5. **Apply shrinkage factor** to fill: multiply fill volume by 1.15 (15% shrinkage from compaction)

#### Method 2: Average End Area (Best for Linear Projects — Roads, Trenches)

1. **Cut cross-sections** perpendicular to the centerline at regular intervals (25', 50', or 100')
2. **Calculate the cut/fill AREA** of each cross-section (in SF)
3. **Average adjacent section areas** and multiply by the distance between them:
```
Volume between sections (CF) = [(Area₁ + Area₂) ÷ 2] × Distance between sections
Volume (CY) = Volume (CF) ÷ 27
```
4. **Sum all segment volumes** for total

**Special case:** If one end area is zero (e.g., where cut transitions to fill), use the pyramid formula:
```
Volume = (1/3) × Area × Distance
```

#### Method 3: Contour Area Method (Good for Irregular Sites)

1. **Measure the area enclosed** between each pair of existing and proposed contour lines at the same elevation
2. **Average adjacent contour areas** and multiply by the contour interval:
```
Volume between contours (CF) = [(Area_lower + Area_upper) ÷ 2] × Contour interval
Volume (CY) = Volume (CF) ÷ 27
```
3. **Sum all volumes** — separate cut from fill

### Earthwork Adjustment Factors

Raw calculated volumes must be adjusted for real-world conditions:

| Factor | Multiplier | When to Apply |
|--------|-----------|---------------|
| **Swell** (bank → loose) | × 1.25 to 1.30 | Calculating truck loads for hauling |
| **Shrinkage** (bank → compacted) | × 0.85 to 0.90 | Calculating how much bank material produces compacted fill |
| **Compaction loss** | Add 15% to fill quantities | Ordering fill material |
| **Topsoil strip** (typically 6") | Separate quantity | Strip and stockpile before grading |
| **Over-excavation** | Add 1' width each side of footings | Foundation excavation |
| **Trench width** | Footing width + 2' working room | Continuous footing trenches |

### Site Work Quantities to Extract from Civil Drawings

| Quantity | Where to Find It | How to Calculate |
|----------|-----------------|-----------------|
| **Cut volume (CY)** | Grading plan (existing vs. proposed contours) | Grid or end area method |
| **Fill volume (CY)** | Grading plan | Grid or end area method + 15% shrinkage |
| **Topsoil strip (CY)** | Grading plan limits | Disturbed area SF × 0.5' ÷ 27 |
| **Subgrade prep (SF)** | Building footprint + paving areas | Measure from plans |
| **Aggregate base (CY)** | Paving sections (detail) | Paved area SF × base thickness ÷ 27 |
| **Asphalt (TONS)** | Paving sections | Area SF × thickness × 145 lbs/CF ÷ 2000 |
| **Curb & gutter (LF)** | Site plan | Measure perimeter of paved areas |
| **Sidewalk (SF)** | Site plan | Measure area of walks |
| **Storm pipe (LF by size)** | Utility plan | Measure each run, note pipe size |
| **Manholes/catch basins (EA)** | Utility plan | Count each structure |
| **Silt fence (LF)** | Erosion control plan | Measure perimeter of disturbed area |
| **Rock check dams (EA)** | Erosion control plan | Count each dam |
| **Seeding/mulching (SF or ACRE)** | Erosion control plan | Measure disturbed area |
| **Retaining walls (SF of face)** | Grading/wall plans | Length × exposed height |

### Reading Utility Profiles

Civil drawings often include **profile views** (longitudinal sections) of pipes. These show:

```
        Ground surface (existing and proposed)
     ___/‾‾‾\___/‾‾‾‾\___
    /                      \
---•---------•---------•---  ← Pipe profile (with slope)
  MH-1     MH-2     MH-3

  Station:  0+00    1+50    3+00
  Rim:     856.20   855.80  855.00
  Inv In:          844.00   843.25
  Inv Out: 844.50   843.50  842.50
  Pipe:    12" RCP  12" RCP
  Slope:   1.0%     0.5%
  Length:   150'     150'
```

**Key data to extract from profiles:**
- Station (distance along the pipe run)
- Rim elevations (top of manholes)
- Invert elevations IN and OUT (inside bottom of pipe at each structure)
- Pipe size, material, and slope
- Cover depth (Rim − Invert − Pipe diameter = cover)
- Trench depth at each point

---

## Summary — What Claude Should Do Differently

With this knowledge, Claude should:

1. **Navigate by sheet index first**, not read pages sequentially
2. **Follow cross-references** (section cuts → sections, detail callouts → details) to build complete element data
3. **Recognize that plan text extraction is imperfect** and supplement with vision analysis
4. **Calculate quantities automatically** from extracted dimensions using the formulas above
5. **Understand "TYP" and multipliers** to extrapolate from one instance to all similar instances
6. **Use hatch patterns** to identify materials when text labels are missing
7. **Check RCPs** for MEP coordination data (currently being missed entirely)
8. **Verify dimensions** by cross-checking dimension string totals
9. **Use elevation datums** to calculate vertical dimensions (heights, depths, cut/fill)
10. **Trace assembly chains** across multiple sheets to get complete element data
