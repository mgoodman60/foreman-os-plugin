# Visual Plan Analysis — Extraction Reference

Extract construction intelligence from plan sheet images using computer vision and OCR. This is the visual complement to text-based extraction (Phase 5) and DXF spatial extraction (Phase 6), capturing the 80% of plan data communicated through drawings rather than text.

---

## Pipeline Overview

The visual analysis pipeline (`visual_plan_analyzer.py`) runs 13 sequential passes on a plan sheet image (PNG, 300 DPI recommended):

| Pass | Name | Extracts | Feeds Into |
|------|------|----------|------------|
| 1 | Sheet Layout Detection | Zone map (title block, plan area, details, notes, schedules) | All subsequent passes (zone-aware) |
| 2 | Full OCR Extraction | All text with position, angle, type classification, zone | Pass 6 (dimension text), Pass 7 (scale text) |
| 3 | Line Detection & Classification | Walls, dimension lines, grid lines, leaders, section cuts | Pass 6 (dimension lines) |
| 4 | Symbol Detection | Doors, windows, electrical, plumbing, markers | Cross-ref with schedules |
| 5 | Material Zone Detection | Hatch patterns → material types with areas | Cross-ref with finish schedule |
| 6 | Dimension Extraction | Paired dimension values + line segments | Quantity intelligence |
| 7 | Scale Calibration | Graphic bar detection + text scale + multi-zone mapping + stretch detection | ALL measurement passes, area calculations |
| 8 | Cross-Sheet References | Section cuts, detail callouts, elevation markers, schedule refs, spec refs | Assembly chains, drawing index, quantity intelligence |
| 9 | Contour Detection | Existing/proposed contour lines, elevation labels, cut/fill estimation | Site grading, earthwork quantities, drainage patterns |
| 10 | Section Extraction | Building sections, wall sections, roof slopes | Height verification, assembly takeoffs |
| 11 | RCP + MEP Extraction | Ceiling data, fixtures, equipment tags, duct/pipe sizes | MEP coordination, ceiling finish tracking |
| 12 | Elevation + Accessibility | Exterior material zones, openings, ADA compliance items | Rendering, envelope takeoff, code compliance |
| 13 | Hatch Refinement + Keynotes | Refined material classification, keynote schedules, general notes | Improved material zones, spec-to-drawing linking |

### Processing Time (CPU, 300 DPI ~3000×4000px)

| Pass | Time | Notes |
|------|------|-------|
| 1 | 2-3 sec | OpenCV contours |
| 2 | 5-7 sec | PaddleOCR + CRAFT, CPU-bound |
| 3 | <1 sec | Hough transform |
| 4 | 3-5 sec | Template matching + filtering |
| 5 | 3-5 sec | Texture analysis |
| 6 | 1-2 sec | Post-processing of Pass 2+3 |
| 7 | 2-4 sec | Scale bar detection + text parse + zone mapping |
| 8 | 1-3 sec | Circle detection + text pattern matching |
| 9 | 2-4 sec | Contour label extraction + dash pattern analysis |
| 10 | 2-4 sec | Section sheet analysis: layer detection + elevation reading |
| 11 | 2-4 sec | RCP ceiling zones + MEP system labels + equipment tags |
| 12 | 2-3 sec | Elevation material zones + accessibility annotations |
| 13 | 2-4 sec | Hatch angle/density refinement + keynote bubble + general notes |
| **Total** | **~28-47 sec** | **Per sheet** |

A 50-sheet plan set processes in approximately 15-25 minutes.

---

## Running the Pipeline

```bash
# Full pipeline
python3 visual_plan_analyzer.py sheet.png --output result.json --dpi 300

# With annotated overlay image
python3 visual_plan_analyzer.py sheet.png --output result.json --annotate annotated.png

# Specific passes only
python3 visual_plan_analyzer.py sheet.png --passes 1,2,6,7

# Summary statistics
python3 visual_plan_analyzer.py sheet.png --summary
```

### Input Requirements

- **Format**: PNG (recommended), JPG, TIFF
- **Resolution**: 300 DPI recommended (200 DPI minimum, 600 DPI maximum for performance)
- **Source**: PDF plan sheets converted to PNG using `pdf_to_images.py` from the construction-takeoff skill
- **Color**: Color or grayscale — pipeline converts to grayscale internally for line/symbol detection

### Converting PDFs to Images

```bash
python3 /mnt/.skills/skills/construction-takeoff/pdf_to_images.py plans.pdf --dpi 300 --output-dir ./sheet_images/
```

---

## Text Type Classification (Pass 2)

After OCR extracts all text, each text element is classified by content pattern:

| Text Type | Pattern | Example | Use |
|-----------|---------|---------|-----|
| Room number | 3-4 digits, in plan area | "101", "201A" | Room schedule cross-ref |
| Dimension | X'-Y" format | "25'-0\"", "12'-6\"" | Measurement data |
| Elevation | EL. or +/- prefix | "EL. 100'-0\"", "+4'-0\"" | Vertical positioning |
| Spec reference | XX XX XX format | "09 65 00", "03 30 00" | Spec cross-ref |
| Scale notation | Fraction = feet | "1/4\" = 1'-0\"" | Calibration |
| Grid label | Single letter or number at plan edge | "A", "1", "C.5" | Grid system |
| Sheet number | X-NNN format | "A-101", "S-201" | Sheet identification |
| Door/window mark | Letter + number | "D101", "W-3" | Schedule cross-ref |

---

## Line Type Classification (Pass 3)

Lines are classified by visual characteristics:

| Type | Thickness | Length | Pattern | Association |
|------|-----------|--------|---------|-------------|
| Wall | >2px at 300 DPI | Moderate | Solid | Form closed/near-closed rectangles |
| Dimension line | 1px thin | Moderate | Solid | Text nearby (dimension value), witness lines at ends |
| Grid line | 1px thin | Long (>50% sheet) | Dash-dot or solid | Grid labels at endpoints |
| Leader line | 1px thin | Short | Solid | 45°-60° angle, connects text to element |
| Section cut | >2px thick | Long | Heavy dashed | Section markers at endpoints |
| Hidden line | 1px thin | Variable | Short dashes | Below-slab elements, future work |

---

## Symbol Reference Library (Pass 4)

### Architectural Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Door swing | Arc + line at wall opening | Single, double, pocket, sliding |
| Window | Parallel lines with breaks in wall | Casement, sliding, fixed, awning |
| Stair arrow | Arrow with "UP" or "DN" text | Direction of travel |
| North arrow | Decorated arrow, usually circled | Plan orientation |
| Room tag | Circle or rectangle with number | Room identification |

### Section and Detail Markers

| Symbol | Visual | Description |
|--------|--------|-------------|
| Section cut | Circle with number/letter, arrow pointing | References section view on another sheet |
| Elevation marker | Circle with number/letter, no arrow | References elevation view |
| Detail callout | Circle or diamond with number/sheet | References enlarged detail |
| Revision cloud | Irregular wavy closed curve | Marks revised areas |
| Grid bubble | Circle at end of grid line | Grid identification |

### Electrical Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Duplex outlet | Circle with 2 lines | Standard receptacle |
| GFCI outlet | Circle with "GFI" text | Ground-fault outlet |
| 220V outlet | Circle with "220" or specific mark | High-voltage outlet |
| Single-pole switch | "S" in circle or at wall | Light switch |
| 3-way switch | "S3" mark | Multi-location switch |
| Junction box | Square or octagon | Electrical junction |
| Light fixture | Various shapes (circle, rectangle, line) | Ceiling or wall-mounted |

### Plumbing Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Water closet | Elongated oval/rectangle at wall | Toilet |
| Lavatory | Small oval/rectangle at wall | Sink |
| Floor drain | Circle with cross | Floor drain |
| Cleanout | Circle with "CO" | Access cleanout |
| Hose bib | Triangle at wall | Outdoor faucet |

### Fire Protection Symbols

| Symbol | Visual | Description |
|--------|--------|-------------|
| Sprinkler head | Circle with cross or dot | Pendent, upright, or sidewall |
| Pull station | Square with "PS" | Manual fire alarm pull |
| Horn/strobe | "HS" or bell symbol | Notification appliance |
| Fire extinguisher | "FE" or cabinet symbol | Extinguisher location |
| FDC | Double connection symbol | Fire department connection |

---

## Hatch Pattern Reference (Pass 5)

### Standard Construction Hatching Conventions

| Visual Pattern | Material | Standard | Use On |
|---------------|----------|----------|--------|
| Diagonal lines (45°, single direction) | Steel (section cut) | ANSI31 | Structural sections |
| Diagonal crosshatch (two directions, 45°/135°) | Concrete | AR-CONC | Foundation/slab sections |
| Random dots/stipple | Earth fill | EARTH | Embankments, backfill |
| Zigzag/wavy parallel lines | Insulation | INSUL | Wall/roof insulation |
| Offset rectangles (brick pattern) | Masonry | BRICK | Brick/CMU walls |
| Small dots in grid | Sand/gravel | AR-SAND | Base course, drainage |
| Solid light gray fill | VCT or generic flooring | DOTS | Floor plans |
| X-pattern grid | Ceramic tile | CROSS | Bathrooms, kitchens |
| No fill (white) | May be carpet or unfinished | — | Floor plans |

### Texture Analysis Method

The pipeline uses two complementary texture analysis techniques:

1. **Gabor Filters**: Detect repeating directional patterns at multiple frequencies (0.05, 0.1, 0.15) and orientations (0°, 45°, 90°, 135°). Strong response indicates hatching with known direction.

2. **Local Binary Patterns (LBP)**: Classify texture type based on local pixel neighborhoods. Different materials produce distinct LBP histograms.

### Material Zone Confidence

| Confidence | Criteria |
|-----------|----------|
| HIGH (>0.8) | Pattern matches finish schedule legend on the sheet |
| MEDIUM (0.5-0.8) | Standard hatching convention match |
| LOW (<0.5) | Ambiguous pattern, multiple possible materials |

---

## Accuracy Expectations

| Extraction Type | Visual Accuracy | DXF Accuracy | Notes |
|----------------|----------------|--------------|-------|
| Room areas | ±5-10% | Exact | Visual from pixel counting at calibrated scale |
| Material areas | ±5-10% | Exact | Visual from hatch zone boundaries |
| Door/window counts | 90-95% | 100% | May miss doors at unusual angles |
| Electrical fixture counts | 80-90% | 100% | Small symbols harder to detect |
| Plumbing fixture counts | 85-95% | 100% | Distinctive shapes help detection |
| Grid line spacing | ±1-2% | Exact | From OCR'd dimension values |
| Dimension values | 95-99% (OCR) | Exact | OCR accuracy depends on print quality |
| Dimension chain verification | 90-95% | N/A | Sum-check catches OCR errors; discrepancy > 1" flags for review |
| Elevation markers | 90-95% | N/A | Named elevations (T.O. WALL, FFE) more reliable than bare numbers |
| Spot elevations (civil) | 85-90% | N/A | Decimal elevation OCR; existing vs proposed classification needs visual context |
| Scale detection (graphic bar) | 98%+ | N/A | Graphic bar survives PDF resizing — most reliable |
| Scale detection (text) | 90-95% | N/A | Text scale assumes nominal print size — may be wrong on resized PDFs |
| Scale detection (known-dim fallback) | 80-90% | N/A | Depends on dimension OCR accuracy and line measurement |
| Multi-zone scale mapping | 90-95% | N/A | Requires correct zone boundary detection from Pass 1 |
| Stretch detection | 95%+ | N/A | Comparing H vs V pixels_per_foot — very reliable when 2+ dimensions available |
| Title block text | 98%+ | N/A | Large, clean text — high OCR confidence |
| Contour elevation labels | 90-95% | N/A | 3-4 digit integers along contour lines; rotated text may reduce accuracy |
| Existing vs proposed classification | 75-85% | N/A | Dash pattern analysis; heavily depends on print quality and line weight |
| Cut/fill estimation | 60-70% | N/A | Rough estimate from contour proximity — always verify with formal earthwork takeoff |
| Drainage direction | 80-85% | N/A | Based on elevation gradient between contour clusters |
| Building section heights | 90-95% | N/A | Elevation markers + dimension strings in section views |
| Roof slope detection | 95%+ | N/A | Slope triangle symbols are distinctive and well-labeled |
| Wall layer identification | 80-90% | N/A | Depends on section detail scale; 3"=1'-0" or larger yields best results |
| Wall layer thickness | 85-90% | N/A | Dimension strings within wall sections; small text may reduce OCR accuracy |
| Fire rating from sections | 90-95% | N/A | Text labels on section drawings; distinctive "HR" or "MIN" patterns |
| Ceiling height zones (RCP) | 90-95% | N/A | Height callouts are large, clear text; zone grouping depends on room boundary detection |
| Ceiling type classification | 95%+ | N/A | ACT grid pattern is visually distinctive; GWB vs exposed easy to distinguish |
| Lighting fixture tags (RCP) | 85-90% | N/A | Symbol + tag recognition; dense fixture layouts may merge adjacent symbols |
| HVAC diffuser tags (RCP) | 80-90% | N/A | Diffuser symbols are smaller; supply vs return classification from symbol shape |
| Duct size labels | 90-95% | N/A | Text labels on duct runs; rectangular (WxH) and round (dia) formats |
| Pipe size labels | 85-90% | N/A | Smaller text than duct labels; system abbreviation + size (e.g., "2\" CW") |
| Equipment tags (MEP) | 95%+ | N/A | Equipment tags are typically large, distinctive text with leader lines |
| Panel schedule data | 85-90% | N/A | Table OCR from schedule sheets; dense columns may reduce accuracy |
| Elevation face identification | 98%+ | N/A | Title text clearly states North/South/East/West |
| Elevation material zones | 80-85% | N/A | Material boundary detection from hatch + color changes; labels improve accuracy |
| Window/door positions on elevation | 90-95% | N/A | Mark labels + opening outlines; dense fenestration may merge |
| Grade line detection | 90-95% | N/A | Distinctive line with earth hatch below |
| Accessibility route width | 85-90% | N/A | Dimension strings along corridors/routes; requires scale calibration |
| ADA clearance annotations | 80-90% | N/A | Turning radius circles and clearance dimensions; symbol-based |
| Signage location markers | 85-90% | N/A | "BRAILLE" or tactile symbol tags on plans |
| Hatch angle classification | 90-95% | Exact | Hough line analysis within zone; standard AIA angles (45°, 90°) detected reliably |
| Hatch density (lines/inch) | 85-90% | N/A | Pixel spacing at calibrated scale; noisy scans reduce accuracy |
| Material legend matching | 95%+ | N/A | OCR legend text + visual pattern comparison; very reliable when legend present |
| Section-cut vs plan-view context | 90-95% | N/A | Sheet type from Pass 10/12 classification; ambiguous on mixed sheets |
| Keynote bubble detection | 90-95% | N/A | Circle/diamond contour + interior number; small keynotes (<8px) may be missed |
| Keynote schedule extraction | 95%+ | N/A | Table OCR from notes zone; clean tabular format yields high accuracy |
| General note extraction | 90-95% | N/A | Numbered text blocks in notes zone; run-on notes may mis-segment |
| Spec section references in notes | 95%+ | N/A | "XX XX XX" six-digit CSI format is highly distinctive |

**When DXF data is available (Phase 6), it always takes priority over visual analysis for spatial data.** Visual analysis provides fallback when DXF is unavailable and supplements DXF with information DXF doesn't carry (symbol identification, material zone classification from hatching).

---

## Integration with Text-Based Extraction

Visual analysis supplements existing text-based extraction:

| Data | Text Extraction | Visual Adds |
|------|----------------|-------------|
| Room schedule | Table from plan notes | Room locations on floor plan, measured areas |
| Door schedule | Table from plan notes | Door locations, swing directions, count verification |
| Finish schedule | Table from plan notes | Actual material zone boundaries, area calculation |
| Equipment schedule | Table from plan notes | Equipment locations on plan, symbol verification |
| Grid system | Grid labels from notes | Grid line positions, spacing measurement |
| Dimensions | Limited from notes | All dimensioned measurements on drawings |
| General notes | Direct text extraction | Callout locations linked to plan elements |

### Cross-Reference Checks

After visual extraction, compare against text-based data:

1. **Door count**: Visual door swings vs. door schedule count → flag if different
2. **Room count**: Visual room tags vs. room schedule count → flag missing rooms
3. **Equipment count**: Visual equipment symbols vs. equipment schedule → flag discrepancies
4. **Material areas**: Visual hatch zones vs. finish schedule room assignments → verify coverage
5. **Dimension chains**: Sub-dimensions sum vs. overall dimension → flag discrepancies > 1"
6. **Elevation consistency**: Section elevation markers vs. detail elevation markers → flag conflicts

---

## Dimension String Chaining (Pass 6 Enhanced)

Dimension chains are the primary built-in cross-check for measurement accuracy. Construction drawings arrange dimensions in "strings" where sub-dimensions along a common line sum to an overall dimension.

### How Chaining Works

```
Overall:  |←————————————— 132'-8" ——————————————→|
Sub-dims: |← 31'-4" →|← 29'-0" →|← 29'-0" →|← 29'-0" →|← 14'-4" →|
          Grid 1     Grid 2     Grid 3     Grid 4     Grid 5     Grid 6
```

The pipeline:
1. **Groups dimensions by axis** — dimensions sharing the same Y-coordinate (horizontal) or X-coordinate (vertical) within 15px tolerance
2. **Identifies the overall dimension** — the longest value in each group (typically offset further from the drawing)
3. **Sums sub-dimensions** and compares to the overall
4. **Flags discrepancies** > 1" (0.083 ft)

### Chain Verification Rules

| Result | Action |
|--------|--------|
| Sum matches overall (±1") | Chain verified — high confidence |
| Sum within 6" of overall | Likely OCR error on one segment — flag for review |
| Sum differs by > 6" | Possible missing segment or major OCR error — flag prominently |
| No overall dimension found | Segments-only chain — sum provides total but unverified |

### What Chains Feed

Verified dimension chains are critical inputs for:
- **Quantitative intelligence**: Room perimeters, wall lengths, building footprint
- **Assembly chains**: Cross-sheet verification (plan dimensions vs. section dimensions)
- **Estimating**: Linear footage for walls, partitions, base trim, crown molding
- **Schedule validation**: Verifying building dimensions match structural grid

---

## Elevation and Spot Elevation Extraction (Pass 6 Enhanced)

### Elevation Markers

Elevation markers appear on **building sections, wall sections, and exterior elevations**. They anchor vertical measurements.

| Marker Type | Pattern | Example | Found On |
|------------|---------|---------|----------|
| Named level | Label + elevation | "T.O. WALL 12'-0\"" | Building sections |
| Relative | +/- from datum | "+4'-0\"" | Sections, details |
| Absolute (MSL) | "EL." prefix + large number | "EL. 856'-6\"" | Site plans, foundations |
| FFE | Finished floor elevation | "FFE 856.50'" | Plans, sections |

### Spot Elevations

Spot elevations appear on **civil/site plans** as standalone decimal numbers (e.g., 856.50) at specific points on the site:

| Type | Visual Indicator | Use |
|------|-----------------|-----|
| Existing | Parentheses "(856.50)" or dashed | Current grade — used for cut/fill calculations |
| Proposed | Bold or standard text "856.50" | Design grade — what will be built |
| FFE | Boxed or labeled "FFE" | Building finished floor level |
| Top of Curb | Labeled "TC" or "T/C" | Curb and gutter elevations |

### Elevation Cross-Checks

After extraction, verify consistency:
1. **FFE on plan vs. FFE on sections** → must match
2. **T.O. WALL on sections vs. wall height dimensions** → must be consistent
3. **Spot elevations at building perimeter vs. FFE** → difference = slab step or ramp
4. **Existing vs. proposed spot elevations at same point** → difference = cut or fill depth

---

## Cross-Sheet Reference Detection (Pass 8)

Cross-sheet references are the connective tissue of a construction plan set. They link views across sheets to form a navigable graph. Building this index is essential for assembly chains, quantity verification, and multi-sheet calculations.

### Reference Types and Visual Patterns

| Type | Visual Pattern | Text Format | Example |
|------|---------------|-------------|---------|
| **Section Cut** | Circle with arrow → | `number / sheet` | "3 / A-301" (Section 3 on sheet A-301) |
| **Detail Callout** | Circle or diamond | `detail / sheet` | "5 / A-501" (Detail 5 on sheet A-501) |
| **Elevation Marker** | Circle, no arrow | `number / sheet` | "1 / A-201" (Elevation 1 on sheet A-201) |
| **Interior Elevation** | Triangle or diamond | `letter / sheet` | "A / A-401" |
| **Enlarged Plan** | Dashed boundary box | `sheet reference in title` | "SEE A-102 FOR ENLARGED PLAN" |
| **Wall Type Tag** | Hexagon or rectangle | `type code` | "2A" → links to wall type schedule |
| **Door/Window Mark** | Circle or tag | `mark number` | "D101" → links to door schedule |
| **Spec Reference** | Text in notes | `XX XX XX` format | "SEE SECTION 03 30 00" |

### Detection Algorithm (Python Pipeline — Pass 8)

```
1. CALLOUT SYMBOL DETECTION
   - Find circles 20-60px diameter (at 300 DPI) with text inside
   - Find diamonds/hexagons 25-70px wide with text inside
   - Filter: must contain text matching "number/sheet" or "letter/sheet" pattern
   - Arrow detection: check for line segment extending from circle edge (section vs elevation)

2. TEXT PARSING
   - Inside the symbol: parse "3/A-301" or "3" (top) / "A-301" (bottom)
   - Some markers use horizontal divider line: number above, sheet below
   - Some use just a number (detail number) with sheet in nearby text
   - Handle variations: "3/A301", "3 / A-301", "3\nA-301", "③/A-301"

3. REFERENCE CLASSIFICATION
   - Has arrow → Section Cut
   - No arrow, circle → Elevation Marker
   - Diamond shape → Detail Callout
   - Triangle/arrow → Interior Elevation
   - Dashed boundary → Enlarged Plan Reference

4. CONTEXT LINKAGE
   - For each reference, note what it's near: grid intersection, room, element
   - Section cuts: note the cut line direction and what it passes through
   - Details: note what's being detailed (wall, footing, connection)

5. INDEX ASSEMBLY (across all processed sheets)
   - Build adjacency graph: sheet → [references_to_sheets]
   - Verify bidirectional: if A-100 calls out detail on A-501, A-501's title should reference A-100
   - Flag orphan references (target sheet not in drawing index)
   - Flag unreferenced sheets (no other sheet points to them)
```

### Common Callout Formats by Discipline

| Discipline | Typical Callout Style | Sheet Numbering |
|-----------|----------------------|-----------------|
| Architectural | Circle with divider line | A-101, A-201, A-501 |
| Structural | Circle, sometimes with tail | S-101, S-201, S-501 |
| Mechanical | Circle or hexagon | M-101, M-201 |
| Electrical | Circle or diamond | E-101, E-201 |
| Plumbing | Circle | P-101, P-201 |
| Civil | Circle, often with arrow for profiles | C-101, C-201 |

### Cross-Reference Validation

After building the index:

| Check | What It Catches |
|-------|----------------|
| Target sheet exists in drawing index | Missing sheets, typos in sheet numbers |
| Bidirectional references (A calls B, B references A) | One-way links that break navigation |
| Section numbers unique per target sheet | Duplicate section numbers on same sheet |
| Detail numbers sequential | Skipped details that may indicate missing content |
| All plan sheet rooms appear in finish schedule | Rooms not covered by finish specifications |
| All door marks have schedule entries | Doors missing from hardware coordination |

### Storage Format

Cross-references go into `plans-spatial.json` under `sheet_cross_references.detail_callouts`:

```json
{
  "id": "XREF-001",
  "source_sheet": "A-100",
  "source_location": {"grid": "C-3", "zone": "plan_area"},
  "target_sheet": "A-501",
  "target_detail": "3",
  "callout_type": "section",
  "description": "Building section at Grid 3",
  "linked_elements": ["grid_3", "wall_type_2A"]
}
```

The drawing index goes into `sheet_cross_references.drawing_index`:

```json
{
  "sheet_number": "A-100",
  "title": "FLOOR PLAN",
  "discipline": "A",
  "type": "floor_plan",
  "revision": "0",
  "date": "01/22/2026"
}
```

---

## Contour Line Detection (Pass 9 — Civil/Site Sheets)

Contour lines on grading plans represent terrain elevation. Detecting and classifying them enables earthwork estimation, drainage analysis, and cut/fill volume calculation.

### Contour Line Conventions

| Line Type | Style | Weight | Meaning |
|-----------|-------|--------|---------|
| Existing contour | Dashed | Light | Current terrain before construction |
| Proposed contour | Solid | Medium | Design terrain after construction |
| Existing index contour | Dashed | Heavy | Every 5th or 10th existing contour (always labeled) |
| Proposed index contour | Solid | Heavy | Every 5th or 10th proposed contour (always labeled) |

### Detection Method

The pipeline detects contours through their elevation labels rather than tracing the curves themselves (curve tracing at typical scan resolution is unreliable):

1. **Label extraction**: Find 3-4 digit integers (e.g., 856, 857, 858) that aren't part of other text patterns
2. **Interval determination**: Calculate spacing between unique elevation values → contour interval (1', 2', 5')
3. **Dash pattern analysis**: For each label, sample the nearby line and count intensity transitions — many transitions = dashed (existing), few = solid (proposed)
4. **Index contour identification**: Elevations divisible by 5 (or 10) are flagged as index contours

### Cut/Fill Estimation

When both existing and proposed contour labels are found near the same location:
- **Proposed < Existing** → CUT (excavation needed)
- **Proposed > Existing** → FILL (material import needed)
- The depth difference gives approximate cut/fill depth at that point

This is a **rough estimate only** — formal earthwork takeoff requires grid method or average-end-area calculations from the actual contour geometry. The estimate is useful for:
- Quick validation against SWPPP cut/fill volumes
- Identifying predominant operation (net cut vs. net fill)
- Flagging areas of deep cut that may encounter rock or groundwater

### Drainage Pattern Detection

Water flows perpendicular to contour lines, from high elevation to low. The pipeline detects overall drainage direction from the elevation gradient across the sheet. This is validated against:
- Storm sewer pipe directions (from civil-deep-extraction)
- SWPPP receiving water identification
- Site grading arrow annotations

### MOSC Project Specifics

For the MOSC project (Climate Zone 4A, 0.56 acre site):
- Expected contour interval: 1' or 2'
- Building pad approximate elevation: ~856' (from geotech boring logs)
- Receiving water: Unnamed Tributary to Triplett Creek
- SWPPP total earthwork: ~2,000 CY
- Contour data should cross-check against geotech soil profile (fill 0-3.5', native clay 3.5'-15')

---

## Claude Vision Validation (Post-Pipeline)

After the automated pipeline runs, Claude reviews the annotated images within the Cowork session using native multimodal capability. This is the **primary validation method** and runs automatically whenever plan sheets are processed through `/process-docs` or `/set-project`.

### How It Works

1. **Pipeline runs** → produces structured JSON + annotated plan image with colored overlays
2. **Claude reads JSON** results and **views annotated images** (native Cowork vision — no external API needed)
3. **Claude validates** extraction quality:
   - Room identification: correct numbers, complete count, locations match plan
   - Door/window counts: visual door swings match detected count, no missed openings
   - Symbol accuracy: electrical outlets vs. data ports, plumbing fixture types
   - Material zones: hatch patterns correctly classified (concrete vs. VCT vs. tile)
   - Line classification: walls vs. grid lines vs. dimension lines
   - Title block data: project name, sheet number, date, revision
4. **Claude corrects** the extraction JSON in-place for any misidentifications
5. **Low-confidence items** get special attention — Claude crops and zooms sub-images for closer inspection

### Validation Priority Order

Focus validation effort where errors have the most impact:

| Priority | Check | Why |
|----------|-------|-----|
| 1 | Room count matches schedule | Missing rooms = missed progress tracking |
| 2 | Door count matches schedule | Procurement and hardware coordination |
| 3 | Equipment symbols correctly identified | Wrong equipment type = wrong spec section |
| 4 | Grid lines and labels | Spatial reference for all field reporting |
| 5 | Dimension values | Quantity verification, material ordering |
| 6 | Material zone classification | Finish schedule validation |
| 7 | Electrical/plumbing fixture counts | Trade coordination, circuit loading |

### Superintendent Participation

The superintendent can participate in validation during Cowork sessions:

- **Correct misidentifications**: "That's not an outlet, that's a data port" → Claude updates extraction JSON
- **Add project-specific context**: "The hatching in those rooms is polished concrete, not VCT" → Claude reclassifies
- **Confirm ambiguous symbols**: "Those circles in the corridor are smoke detectors" → Claude adds to symbol map
- **Flag missing items**: "There should be 6 RTUs on the roof plan" → Claude re-examines

All superintendent corrections are logged and applied to improve future extractions on the same project.

### When to Use Claude Vision Validation

- **Always**: During `/set-project` and `/process-docs` for plan sheet PDFs
- **Per-sheet**: Claude validates each sheet after pipeline processing (automatic)
- **On-demand**: User asks "verify the floor plan extraction" → Claude re-examines
- **After corrections**: Re-validate after superintendent provides corrections

### Annotated Image Overlay Colors

The pipeline generates annotated images with these overlay colors for Claude to review:

| Color | Meaning |
|-------|---------|
| Green | Walls (thick lines) |
| Blue | Grid lines |
| Red | Dimension lines |
| Yellow text boxes | OCR-detected text with classification |
| Orange circles | Detected symbols |
| Semi-transparent fills | Material zones by type |

---

## Optional: Gemini 2.5 Pro Batch Validation

For bulk processing of large plan sets (100+ sheets) where interactive Cowork review is impractical, the pipeline supports automated validation using Google's Gemini 2.5 Pro vision model. This is **optional** — Claude Vision validation (above) is the default and preferred method.

### When to Use Gemini Batch Validation

- Initial project setup with 100+ plan sheets
- Overnight processing of full plan sets
- Bulk re-extraction after pipeline improvements
- Projects where superintendent isn't available for interactive review

### Setup

1. **Install**: `pip install google-genai --break-system-packages`
2. **Get API key**: From [Google AI Studio](https://aistudio.google.com/) (included with Gemini Pro subscription)
3. **Store key** in `AI - Project Brain/gemini-config.json`:
   ```json
   {
     "api_key": "YOUR_GEMINI_API_KEY",
     "model": "gemini-2.5-pro",
     "batch_size": 5,
     "max_retries": 3
   }
   ```

### Batch Validation Workflow

1. **Run automated pipeline** on all sheets → produces JSON + annotated PNGs
2. **Group sheets by discipline** (A-sheets together, S-sheets together, etc.)
3. **Send annotated images to Gemini** in batches of 5-10 sheets per API call
4. **Prompt Gemini** with extraction JSON + annotated image:
   - "Review this floor plan extraction. Verify room count, door count, and equipment identification."
   - "Check these dimension values against what you see on the plan."
   - "Confirm material zone classifications match the hatching patterns."
5. **Gemini returns corrections** as structured JSON (same schema as pipeline output)
6. **Apply corrections** to extraction results
7. **Generate validation summary** with correction counts by type

### Cost Estimate

- Gemini 2.5 Pro: ~$0.002-0.005 per plan sheet (image + text input/output)
- 50-sheet plan set: ~$0.10-0.25 total
- 200-sheet plan set: ~$0.40-1.00 total

### Limitations

- Requires internet access and valid API key
- API rate limits may slow processing of very large sets
- Gemini may not catch project-specific symbol conventions
- Claude Vision + superintendent review catches more nuanced errors
- Not suitable for confidential/classified projects (data leaves local machine)

---

## Scale Calibration — Detailed Methodology (Pass 7)

Scale calibration is the foundation of ALL measurement extraction. Without a calibrated pixels-per-foot value, room areas, dimension verification, material quantities, and distance calculations are impossible. **Pass 7 MUST succeed before any measurement data from the sheet is trusted.**

### Priority Order

| Priority | Method | Confidence | When to Use |
|----------|--------|------------|-------------|
| 1 | **Graphic scale bar** | HIGH (0.95) | Always preferred — survives PDF resizing, scanning, reprinting |
| 2 | **Text scale notation** | MEDIUM (0.80) | When no graphic bar — assumes nominal sheet size |
| 3 | **Known-dimension calibration** | LOW (0.65) | When neither bar nor text found — uses longest readable dimension |
| 4 | **Cross-sheet inference** | LOW (0.60) | Same discipline sheets often share scale — borrow from calibrated sibling |

### Graphic Scale Bar Detection (Enhanced Pass 7)

#### Visual Characteristics

Graphic scale bars appear as one of three common styles:

**Open Bar (most common on architectural plans):**
```
|----|----|----|----|
0    4'   8'  12'  16'
```
- Horizontal line with perpendicular tick marks at even intervals
- Distance labels below ticks, increasing left to right
- May have "GRAPHIC SCALE" label above or below

**Filled Bar (common on civil/site plans):**
```
█░░░█░░░█░░░█░░░█
0   10   20   30   40
         FEET
```
- Alternating filled and unfilled rectangular segments
- Each segment represents a fixed distance
- Often includes unit label ("FEET", "METERS")

**Ladder Bar (common on detail sheets):**
```
┌──┬──┬──┬──┬──┐
│  │  │  │  │  │
└──┴──┴──┴──┴──┘
0  1  2  3  4  5
      INCHES
```
- Enclosed rectangular segments
- Common for larger-scale details (1" = 1'-0" and above)

**Subdivided First Segment:**
Many bars have the first segment subdivided into finer increments:
```
|·|·|·|·|----|----|----|
0  1  2  3  4'   8'  12'  16'
```
- The fine ticks between 0 and the first major tick represent sub-units
- This provides higher precision for small measurements

#### Detection Algorithm (Python Pipeline)

```
1. CANDIDATE LINE DETECTION
   - Find horizontal line segments between 50px and 500px long (at 200-300 DPI)
   - Filter: slope < 2° from horizontal
   - Filter: not in plan area interior (scale bars are at sheet edges, near title block, or below views)

2. TICK MARK DETECTION
   - For each candidate line, search perpendicular (±5px of the line Y-coordinate)
   - Find short vertical line segments (10-30px tall) that intersect or are within 5px of the candidate
   - Require minimum 3 ticks
   - Calculate tick spacing: distance between consecutive ticks in pixels
   - Verify even spacing: coefficient of variation of tick spacing < 0.15 (15%)

3. LABEL MATCHING
   - Search OCR text elements within 40px below the tick positions
   - Match text to nearest tick by X-coordinate proximity
   - Parse numeric values: integers, decimals, feet-inch notation
   - Verify monotonically increasing values left to right
   - Extract unit label if present ("FEET", "FT", "INCHES", "IN", "METERS", "M")

4. CALIBRATION CALCULATION
   - bar_pixel_length = distance between first and last tick (in pixels)
   - bar_real_length = value at last tick minus value at first tick (in real units)
   - Convert to feet if units are inches or meters
   - pixels_per_foot = bar_pixel_length / bar_real_length_in_feet

5. FILLED BAR VARIANT
   - If no tick marks found, look for alternating light/dark segments along the candidate line
   - Segment boundaries become the "ticks"
   - Same label matching and calibration calculation applies

6. VALIDATION
   - Cross-check: if text scale also found on same sheet, compare calculated pixels_per_foot
   - Acceptable tolerance: ±5% between graphic bar and text scale
   - If > 5% divergence: graphic bar wins (text scale assumes nominal print size)
   - Flag divergence in output for superintendent review
```

#### Common Scale Bar Locations

Search these areas in priority order:
1. **Bottom-right of sheet** (adjacent to or inside title block) — most common
2. **Below each plan view** (especially when multiple views on one sheet)
3. **Bottom-center of sheet** (common on civil/site plans)
4. **Right side margin** (some firms place it vertically — rotate detection 90°)

### Multi-Scale Zone Mapping

A single sheet often contains multiple views at different scales. Each view MUST be calibrated independently.

#### How to Identify Zones

1. **View titles**: Look for OCR text matching patterns like "FLOOR PLAN", "ENLARGED PLAN", "DETAIL A", "SECTION 1", followed by a scale notation
2. **Boundary lines**: Thick border lines or break lines separate views
3. **Scale labels below views**: "SCALE: 1/4\" = 1'-0\""
4. **Separate graphic bars**: Some sheets have multiple graphic bars, one per view

#### Common Multi-Scale Combinations

| Sheet Type | Main View Scale | Secondary Views |
|-----------|----------------|-----------------|
| Floor Plan (A-101) | 1/4" = 1'-0" | Enlarged restroom 1/2", wall sections 1" |
| Site Plan (C-101) | 1" = 20'-0" | Enlarged entrance 1" = 10'-0" |
| Foundation (S-101) | 1/4" = 1'-0" | Footing details 3/4", pier details 1" |
| Details (A-501) | varies | Multiple details at 1", 1-1/2", 3" |
| Ceiling Plan (A-102) | 1/4" = 1'-0" | Enlarged ceiling details 1/2" |
| Elevations (A-201) | 1/4" = 1'-0" | Wall section callouts at 1" |
| MEP Plans (M-101, E-101) | 1/4" = 1'-0" | Usually single-scale matching architectural |

#### Zone-Scale Storage Format

```json
"zones": [
  {
    "view_name": "FLOOR PLAN",
    "scale_text": "1/4\" = 1'-0\"",
    "pixels_per_foot": 62.4,
    "calibration_method": "graphic_bar",
    "zone_bbox": [120, 80, 2800, 3200],
    "confidence": "high"
  },
  {
    "view_name": "ENLARGED RESTROOM",
    "scale_text": "1/2\" = 1'-0\"",
    "pixels_per_foot": 124.8,
    "calibration_method": "text_scale",
    "zone_bbox": [2850, 80, 3600, 1200],
    "confidence": "medium"
  }
]
```

### Known-Dimension Calibration Fallback

When no graphic bar or text scale is found:

1. **Find the longest dimension string** on the sheet (largest real-world value)
2. **Locate its dimension line** — the thin line with witness lines at each end
3. **Measure the dimension line** in pixels (center of witness line to center of witness line)
4. **Calculate**: `pixels_per_foot = pixel_length / (dimension_value_in_feet)`
5. **Cross-check**: Pick a SECOND dimension on the same view and verify:
   - Measure its line in pixels
   - Calculate expected real-world value using the calibration
   - Compare to its OCR text value
   - If within ±5%: calibration is good → confidence "medium"
   - If within ±10%: acceptable → confidence "low"
   - If > 10%: calibration failed → do not use

### Stretch Detection (Double Calibration)

Scanned documents and some PDF exports produce images with different X and Y scaling. This is invisible to the eye but ruins area calculations.

**Detection method:**
1. Find a clearly horizontal dimension and calculate `h_ppf` (horizontal pixels per foot)
2. Find a clearly vertical dimension and calculate `v_ppf` (vertical pixels per foot)
3. Compare: `stretch_ratio = max(h_ppf, v_ppf) / min(h_ppf, v_ppf)`
4. If `stretch_ratio > 1.03` (3% difference): stretch detected

**Correction:**
- For horizontal measurements: use `h_ppf`
- For vertical measurements: use `v_ppf`
- For area calculations: use `area_ppf² = h_ppf × v_ppf` (geometric product, not mean squared)
- Record `"stretch_detected": true` and both values in the scale data

**Common stretch sources:**
- Flatbed scanning of printed sheets (feed direction stretches 2-5%)
- PDF resizing without "preserve aspect ratio"
- Screen capture from PDF viewers at non-standard zoom

### Scale Calibration Failure Protocol

If all calibration methods fail for a sheet:

1. **Record failure**: `"calibration_method": "none"`, `"confidence": "failed"`
2. **Flag for review**: Add to extraction report as needing manual scale confirmation
3. **Continue text extraction**: Room names, door marks, general notes, title block data — all still valid
4. **DO NOT extract measurements**: No areas, no distances, no quantities from this sheet
5. **Cross-sheet fallback**: If sibling sheets of the same discipline ARE calibrated, note the expected scale for superintendent confirmation

---

## Building Section and Wall Section Extraction — Detailed Methodology

### Sheet Identification

Section sheets are identified by:
- **Sheet number prefix**: A-300 series (architectural building sections), A-400/A-500 (wall sections/details), S-300 (structural sections)
- **Drawing index classification**: "BUILDING SECTIONS", "WALL SECTIONS", "SECTIONS AND DETAILS"
- **Title block content**: Keywords "SECTION", "BUILDING SECTION", "WALL SECTION"
- **Visual characteristics**: Vertical drawings with elevation markers, hatched material layers, grade lines

### Building Section Detection Algorithm

Building sections are full-height cuts through the building showing foundation-to-roof:

1. **Identify the grade line**: Horizontal line with earth hatch (diagonal lines) below and building above. The grade line establishes the reference for foundation depth.

2. **Read elevation markers**: Building sections always have elevation markers on at least one side:
   - T.O. FOOTING, B.O. FOOTING (foundation)
   - T.O. SLAB, FFE (finished floor)
   - T.O. WALL, PLATE HEIGHT (wall top)
   - T.O. STEEL, T.O. STRUCTURE (structural support)
   - RIDGE, T.O. RIDGE (roof peak)
   - Grade, FG, FINISH GRADE (ground level)

3. **Calculate key heights by subtraction**:
   - `floor_to_floor = T.O. STRUCTURE - FFE` (or T.O. WALL - FFE for single story)
   - `foundation_depth = FFE - B.O. FOOTING` (or FG - B.O. FOOTING for depth below grade)
   - `ridge_height = RIDGE - FFE`
   - `eave_height = T.O. WALL - FFE`
   - `ceiling_height = CEILING - FFE`

4. **Detect roof slope**: Look for slope triangle symbols — small right triangles with rise and run labeled (e.g., "4" on vertical, "12" on horizontal = 4:12 slope). Common locations: along the top chord of the roof structure. Convert to degrees: `degrees = atan(rise/run) × 180/π`.

5. **Identify structural members**: Text labels within the section identifying structural elements (purlins, rafters, joists, trusses, beams, columns) with their depth dimensions.

6. **Read dimension strings**: Vertical dimension chains along the sides of the section giving heights between levels. These confirm the elevation marker math.

### Wall Section Detection Algorithm

Wall sections are enlarged views showing layer-by-layer construction:

1. **Identify wall section boundaries**: Wall sections are typically drawn at 1-1/2"=1'-0" or 3"=1'-0" scale. They show a narrow vertical strip with distinct material hatching for each layer.

2. **Detect material layers by hatch pattern**:

| Hatch Pattern | Material | Typical Position |
|---------------|----------|-----------------|
| Diagonal lines (45°) | GWB / Gypsum board | Interior/exterior finish |
| Small dots / stipple | Concrete / CMU | Structure |
| Crossed diagonal lines | Insulation (batt) | Stud cavity |
| Wavy lines | Insulation (rigid/foam) | Sheathing/cavity |
| Empty rectangle with studs | Metal/wood studs | Structural frame |
| Dense parallel lines | Plywood / sheathing | Substrate |
| Brick pattern | Masonry veneer | Exterior |
| Irregular random | Earth / fill | Below grade |

3. **Read layer dimensions**: Each layer typically has a dimension callout. Scan for dimension strings positioned within or adjacent to each hatched zone. Common formats:
   - `5/8"` (GWB)
   - `3-5/8"` (stud depth)
   - `R-13` or `R-19` (insulation R-value, implies thickness)
   - `1/2"` (sheathing)
   - Full dimension strings: `5/8" TYPE X GWB`

4. **Read material labels**: Text labels pointing to each layer with leader lines. These provide the full specification: `5/8" TYPE X GWB ON 3-5/8" 20GA METAL STUDS @ 16" O.C.`

5. **Identify wall type**: Match to wall type schedule via:
   - Explicit label on the section (e.g., "WALL TYPE 4")
   - Matching the layer composition against the wall type legend
   - Cross-referencing with plan annotations showing wall types

6. **Detect fire rating annotations**: Look for:
   - Text containing "HR" preceded by a number (e.g., "1-HR", "2 HR")
   - UL assembly numbers (e.g., "UL U305", "UL U411")
   - Fire rating symbols (hour-glass or fire symbols in some drawing standards)

7. **Read connection conditions**:
   - **Base**: How wall meets floor — sealant joints, base trim, moisture barrier
   - **Top**: How wall meets structure — deflection track, fire safing, acoustic sealant
   - **Head/sill/jamb**: Window and door frame conditions if shown in the section

### Slope Triangle Detection

Slope triangles are standardized symbols used to denote roof pitch:

```
    |\
    | \
  4 |  \
    |   \
    |____\
      12
```

Detection method:
1. Find right-angle triangle shapes (three connected lines forming ~90° corner)
2. Read the two numbers: vertical side = rise, horizontal side = run
3. Standard ratios: 1/4:12, 1/2:12, 1:12, 2:12, 3:12, 4:12, 6:12, 8:12, 12:12
4. Convert: `slope_degrees = math.degrees(math.atan(rise / run))`
5. For flat roofs: may show "1/4\"/FT" or "MIN 1/4\"/FT" instead of triangle

### Wall Assembly Validation Rules

After extracting wall layers, run these checks:

| Check | Rule | Action on Failure |
|-------|------|-------------------|
| Layer sum vs total | Sum of layer thicknesses should equal total wall thickness ±0.25" | Flag discrepancy, use total from dimension |
| Fire-rated GWB | 1-HR walls require min 5/8" Type X GWB on each side | Flag if Type X not specified |
| Insulation presence | Exterior walls must have insulation layer | Flag if missing |
| Stud depth vs insulation | Insulation thickness should not exceed stud cavity depth | Flag if batt exceeds cavity |
| Vapor barrier | Exterior walls in cold climates should show vapor barrier | Note if missing |
| Air barrier | Exterior walls should show air/weather barrier | Note if missing |

### Section Data Consumers

Section extraction data feeds these downstream systems:

- **Estimating**: Wall assembly layers → material takeoff (GWB SF, insulation SF, stud LF)
- **Scheduling**: Foundation depth → excavation duration; wall complexity → framing duration
- **Quality Management**: Fire ratings → inspection checklists; layer specs → pre-install verification
- **Rendering**: Heights, slopes, material finishes → 3D visualization parameters
- **Field Reference**: Assembly details → quick-reference for trade crews

---

## RCP and MEP System Extraction — Detailed Methodology

### RCP Sheet Detection

Reflected Ceiling Plans are identified by:
- **Sheet number patterns**: `A-102`, `A-5xx`, `RCP-xxx`, or suffix `-RCP`
- **Title block text**: "Reflected Ceiling Plan", "RCP", "Ceiling Plan"
- **Visual characteristics**: Dashed grid lines (reflected view), ceiling height callouts in rooms, lighting fixture symbols without floor furniture

### Ceiling Height Zone Detection

Ceiling heights appear as room-level callouts. The detection approach:

1. **Find height callout text**: Patterns include:
   - `9'-0" AFF` (above finished floor)
   - `CLG @ 10'-0"` or `CLG HT = 10'-0"`
   - `10'-0" ACT` (height + ceiling type)
   - `GWB @ 8'-6"` (type + height)

2. **Associate callout with room**: Match height callout position to room boundary from Pass 1 zone detection or from room labels.

3. **Group rooms into height zones**: Rooms with the same ceiling height and type form a zone.

4. **Detect transitions**: Where ceiling height changes within a single room (soffits, bulkheads, stepped ceilings), record as a `height_transition` element.

### Ceiling Type Classification

| Visual Signal | Classification | Confidence |
|--------------|---------------|------------|
| Regular grid pattern (2×2 or 2×4 modules) | ACT (acoustic ceiling tile) | 95% |
| Smooth surface with no grid | GWB (gypsum board ceiling) | 85% |
| Text label "ACT" or "ACOUSTIC" | ACT | 98% |
| Text label "GWB" or "DRYWALL" | GWB | 98% |
| Text label "EXPOSED" or no ceiling shown | Exposed structure | 90% |
| Grid with irregular spacing or linear pattern | Specialty (wood slat, metal panel) | 75% |

### Lighting Fixture Symbol Library

Common fixture symbols found on RCPs:

| Symbol Shape | Typical Tag | Description |
|-------------|-------------|-------------|
| Rectangle (2×4 outline) | A, B | 2×4 recessed troffer |
| Rectangle (2×2 outline) | C, D | 2×2 recessed fixture |
| Small circle (4-6" dia) | E, F | Recessed downlight (LED can) |
| Circle with lines radiating | G | Surface/pendant mount decorative |
| Rectangle with "X" | H | Emergency/exit fixture |
| Small square with arrow | J | Wall-mounted sconce |
| Triangle or "EXIT" text | EXIT | Exit sign (LED/battery backup) |

Detection method:
1. Find small geometric shapes (rectangles, circles) that repeat in a regular pattern
2. Look for single-character tags adjacent to each symbol (within ~0.5" on paper)
3. Cross-reference tag characters to lighting fixture schedule if available
4. Count fixtures per room by spatial association with room boundaries

### MEP Sheet Detection

MEP sheets are identified by discipline prefix:
- **M-series**: Mechanical (HVAC) — duct layouts, equipment, diffuser locations
- **P-series**: Plumbing — pipe routing, fixture connections, riser diagrams
- **E-series**: Electrical — panel locations, circuiting, receptacle/switch layouts
- **FP-series**: Fire protection — sprinkler layouts (reference only from RCP)

### Duct Size Label Detection

Duct size labels appear along duct routing lines:

| Format | Example | Interpretation |
|--------|---------|---------------|
| W×H | `12x8` | Rectangular duct, 12" wide × 8" high |
| Diameter (round) | `10" RD` or `Ø10"` | Round duct, 10" diameter |
| Diameter (flex) | `8" FLEX` | Flexible round duct, 8" diameter |

Detection: Find text matching `\d+\s*[xX×]\s*\d+` (rectangular) or `\d+\s*[\"″]?\s*(?:RD|ROUND|FLEX|Ø)` (round) along detected line segments.

### Pipe Size Label Detection

Pipe labels combine system abbreviation + size:

| System | Abbreviations | Example Label |
|--------|--------------|---------------|
| Domestic cold water | CW, DCW, CWS | `2" CW` |
| Domestic hot water | HW, DHW, HWS, HWR | `3/4" HW` |
| Sanitary sewer | SAN, S, SS | `4" SAN` |
| Storm drain | SD, ST, STORM | `6" SD` |
| Natural gas | G, NG, GAS | `1" G` |
| Medical gas | MG, O2, VAC, N2O | `1/2" O2` |
| Vent | V, VTR | `2" V` |

Detection: Find text matching `\d+(?:/\d+)?\s*[\"″]?\s*(?:CW|HW|SAN|SD|G|NG|V|...)` near line segments on P-series sheets.

### Equipment Tag Detection

MEP equipment tags are distinctive: uppercase letters + numbers, typically with leader lines pointing to equipment symbols.

| Pattern | Equipment Type | Example |
|---------|---------------|---------|
| RTU-# | Rooftop unit | RTU-1, RTU-2 |
| AHU-# | Air handling unit | AHU-1 |
| EF-# | Exhaust fan | EF-1, EF-2 |
| VRF-# | Variable refrigerant flow | VRF-1 |
| ERV-# | Energy recovery ventilator | ERV-1 |
| WH-# | Water heater | WH-1 |
| P-# | Pump | P-1, P-2 |
| LP-#, DP-# | Lighting/distribution panel | LP-1, DP-A |

Detection: Find text matching `[A-Z]{2,4}-?\d+` with leader lines or inside equipment symbol outlines. Cross-reference to equipment schedules for capacity data.

### Panel Schedule Table Extraction

Panel schedules are dense tables on E-series sheets. Extraction approach:

1. **Identify table boundaries**: Find the rectangular grid pattern of the schedule
2. **Read header row**: Panel name, voltage, phase, main breaker size
3. **Read circuit rows**: Circuit number, description, breaker size, load (VA or watts)
4. **Sum loads**: Calculate total connected load and compare to panel capacity
5. **Map circuits to rooms**: Parse circuit descriptions for room numbers/names

### RCP + MEP Data Consumers

| Consumer | Data Used | Purpose |
|----------|-----------|---------|
| Estimating/Takeoff | Fixture counts, duct LF, pipe LF | Material quantities |
| Quality Management | Equipment tags, panel schedules | Inspection checklists |
| Scheduling | Equipment list, system complexity | MEP rough-in/trim durations |
| Commissioning | Equipment tags, panel schedules | Startup/TAB checklists |
| Daily Reports | Active MEP work by system | Progress tracking |
| Rendering | Ceiling type, fixture layout | Interior visualization |

---

## Exterior Elevation and Accessibility Extraction — Detailed Methodology

### Elevation Sheet Detection

Exterior elevation sheets are identified by:
- **Sheet number**: A-200 series (A-200, A-201, A-202, etc.)
- **Title block text**: "NORTH ELEVATION", "SOUTH ELEVATION", "EXTERIOR ELEVATIONS"
- **Visual characteristics**: Full-height side view of building with grade line, material hatching, window/door outlines
- **Orientation labels**: N, S, E, W or full cardinal direction words

### Elevation Face Classification

Each elevation drawing shows one face of the building. Identification:

1. **Title text**: Usually states the direction explicitly — "NORTH ELEVATION", "SOUTH ELEV."
2. **Orientation relative to plan**: If plan North arrow is known, cross-reference section cut marks on plan
3. **Multiple elevations per sheet**: Some sheets show 2-4 elevations; each has its own title and scale

### Material Zone Detection on Elevations

Exterior elevations show material zones as hatched or patterned areas:

| Visual Signal | Material | Common Color/Texture |
|--------------|----------|---------------------|
| Diagonal hatch (45°) with dots | Concrete / CMU | Gray, textured |
| Running bond pattern | Brick masonry | Red, tan, gray |
| Irregular stone pattern | Stone veneer | Earth tones |
| Vertical ribs / parallel lines | Metal panel (ribbed) | Metallic colors |
| Clean rectangles with reveals | Metal panel (flat) | Solid colors |
| Wood grain pattern | Wood siding / board-and-batten | Natural/stain |
| Stipple dots | Stucco / EIFS | Light colors |

Detection approach:
1. Identify the building outline on the elevation (the closed polygon above grade line)
2. Segment the building area into zones by hatch pattern change or boundary lines
3. Read material labels with leader lines pointing to each zone
4. Extract color/finish from text callouts (e.g., "CHAMPAGNE TAN METAL PANELS")

### Grade Line Detection

The grade line is the boundary between building and earth:
- **Visual**: Horizontal or gently sloping line with earth hatch (diagonal lines) or stipple below
- **Label**: Often marked "F.G." (finished grade) or "GRADE" with an elevation value
- **Significance**: Establishes the reference for all height measurements on the elevation

### Window and Door Positions on Elevation

Windows and doors appear as openings in the elevation wall surface:
- **Windows**: Rectangular openings with mark labels (W-101, etc.), sill and head heights
- **Doors**: Rectangular openings at grade or near-grade level, with mark labels
- **Storefronts**: Large glazed areas with mullion patterns, marked by section
- **Detection**: Find mark labels near rectangular openings; cross-reference to schedules

### Accessibility Extraction from Floor Plans

Accessibility data is typically annotated on architectural floor plans rather than separate sheets:

**1. Accessible Route Detection:**
- Routes marked with dashed lines or special line type labeled "ACCESSIBLE ROUTE"
- Corridor width dimensions (must be ≥44" for corridors, ≥36" for passages)
- Door maneuvering clearances shown as dashed rectangles at doors
- Level changes noted with ramp symbols or elevator locations

**2. ADA Restroom Clearance Detection:**
- 60" diameter turning circle shown as dashed circle in accessible restrooms
- WC centerline dimension (18" from side wall)
- Clear floor space rectangles (30"×48") at fixtures
- Grab bar symbols (42" side bar, 36" rear bar)

**3. Ramp Detection:**
- Ramp symbols: parallel lines with slope notation (1:12, 8.33%)
- Landing rectangles at top, bottom, and direction changes (60"×60" min)
- Handrail symbols on both sides
- Text: "RAMP", "1:12 MAX", "ADA RAMP"

**4. Signage Location Detection:**
- Text labels: "BRAILLE", "TACTILE SIGN", "ROOM SIGNAGE"
- Symbol: Small rectangle with dots (representing Braille)
- Mounting height notes: "60\" AFF", "48\"-60\" AFF"
- Location: Latch side of door, 6" from frame

**5. Accessible Parking Detection (Site Plans):**
- Standard accessible stalls: 8' wide + 5' access aisle, ISA symbol
- Van accessible: 8' wide + 8' aisle (or 11' + 5'), "VAN ACCESSIBLE" sign
- Slope annotation: max 2% in any direction
- Sign symbol: ISA wheelchair symbol on post

### Accessibility Compliance Validation Rules

| Check | Code Requirement | Action on Failure |
|-------|-----------------|-------------------|
| Corridor width | ≥44" (≥36" for short passages) | Flag as ADA violation |
| Door width | ≥32" clear opening (≥36" for accessible) | Flag |
| Turning radius | 60" circle in accessible restrooms | Flag |
| WC centerline | 18" from side wall | Flag |
| Ramp slope | ≤1:12 (8.33%) | Flag |
| Ramp width | ≥36" between handrails | Flag |
| Landing size | ≥60"×60" at top/bottom | Flag |
| Handrail height | 34"-38" AFF | Flag |
| Signage height | 48"-60" AFF, latch side | Flag |
| Accessible parking | Per IBC Table 1106.1 | Flag count deficiency |
| Counter height | ≤36" (service), ≤34" (transaction) | Flag |

### Data Consumers for Elevation + Accessibility

| Consumer | Data Used | Purpose |
|----------|-----------|---------|
| Rendering | Material zones, colors, fenestration | Exterior 3D visualization |
| Estimating | Material areas by zone, fenestration count | Cladding/glazing takeoff |
| Quality Management | ADA clearances, grab bar locations | Pre-pour/pre-frame inspection |
| Scheduling | Cladding zones, fenestration count | Envelope sequence planning |
| Safety | Accessible routes, ramp locations | Site safety plan |
| Commissioning | ADA compliance items | Closeout checklist |

---

## Hatch Pattern Refinement and Keynote Extraction — Detailed Methodology

### Hatch Refinement Algorithm (Pass 13A)

Pass 13 refines Pass 5 material zones using standard construction hatch pattern classification:

**Step 1 — Hatch Line Angle Measurement:**
For each material zone from Pass 5, extract the region of interest and run Hough Line Transform within the zone boundary:
1. Mask the zone using its contour polygon
2. Apply Canny edge detection within the mask
3. Run HoughLinesP with `minLineLength=20`, `maxLineGap=5`
4. Calculate the angle of each detected line segment
5. Build a histogram of angles (binned to 5° increments)
6. Identify dominant angles (peaks with >15% of total line segments)

**Step 2 — Standard Pattern Classification Table:**

| Dominant Angles | Pattern Name | ANSI Code | Material | Notes |
|----------------|-------------|-----------|----------|-------|
| 45° only | Single diagonal | ANSI31 | Steel (section cut) | Most common section cut pattern |
| 45° + 135° | Cross-hatch | AR-CONC | Concrete | Double diagonal = concrete standard |
| 0° or 90° only | Horizontal/vertical | ANSI37 | Wood (with-grain) | Parallel to grain direction |
| 0° + 90° | Grid cross-hatch | — | Wood (end-grain) | Cross-section of timber |
| No dominant angle | Random/stipple | EARTH | Earth/fill | Dots detected by low line count + texture variance |
| ~30° wavy | Wavy lines | INSUL | Insulation | Low-frequency oscillation pattern |
| 45° very dense | Dense diagonal | AR-SAND | Sand/gravel | Same angle as ANSI31 but spacing <0.05" |
| Brick-like | Running bond | BRICK | Masonry | Alternating offset horizontal lines with verticals |

**Step 3 — Hatch Density Measurement:**
1. Count the number of Hough lines detected within the zone
2. Measure the perpendicular spacing between adjacent parallel lines
3. Convert pixel spacing to inches using Pass 7 scale calibration
4. Calculate lines per inch (LPI) = 1 / spacing_inches
5. Use LPI to disambiguate similar patterns (concrete ~4-8 LPI, earth fill ~1-3 LPI, sand >10 LPI)

**Step 4 — Legend Cross-Reference:**
1. In Pass 1 zone detection, identify material legend blocks (usually in the corner or margin of the sheet)
2. OCR the legend text to get material name → visual pattern swatch pairs
3. For each Pass 5 zone, compare its angle/density signature against each legend swatch
4. If match found, override the Pass 5 classification with the legend's material name and set `legend_match: true`

**Step 5 — Adjacent Label Association:**
1. For each material zone boundary, search within 50px radius for OCR text elements
2. Check if any nearby text matches material keywords (CONCRETE, EARTH, GRAVEL, INSULATION, STEEL, WOOD, MASONRY, CMU, RIGID, BATT)
3. Also check for leader lines (Pass 3) that terminate within the zone — follow leader back to its text label
4. If found, set `material_label` field on the zone

### Keynote Extraction Algorithm (Pass 13B)

**Step 1 — Keynote Bubble Detection:**
Keynote bubbles are small geometric shapes (circles, diamonds, hexagons) containing a number, connected by leader lines to drawing elements.

1. Detect small circular contours (radius 8-25px at 300 DPI) using HoughCircles
2. Also detect small diamond/hexagonal shapes using contour approximation (4-6 vertices, aspect ratio ~1:1)
3. For each candidate shape, check if it contains exactly one OCR text element that is a number (1-99) or alphanumeric code
4. Filter out door/window marks (these are larger and have different text patterns like "101", "W-1")
5. For each confirmed keynote bubble, trace leader lines:
   - Find lines (from Pass 3) that start within 10px of the bubble boundary
   - Follow the line to its opposite endpoint = `leader_endpoint`
   - Record the endpoint position for element-linking

**Step 2 — Keynote Schedule Table Extraction:**
1. Look in the notes/schedule zones (from Pass 1) for tables with columns: Number | Description
2. Tables with two columns where Column 1 is short numbers (1-99) and Column 2 is descriptive text are keynote schedules
3. Extract each row as a keynote entry: `number`, `description`
4. Scan `description` text for spec section references using pattern: `\d{2}\s?\d{2}\s?\d{2}` (CSI six-digit format)
5. Also check for alternate formats: "Section XXX", "Spec XXX", "Division XX"

**Step 3 — General Note Block Extraction:**
1. Identify general note blocks in the notes zone from Pass 1
2. Parse numbered entries using pattern: `^\s*(\d+|[A-Z])[\.\)]\s*(.+)` (number/letter followed by period or paren)
3. For multi-line notes, continue capturing until the next numbered entry
4. Classify each note by category:
   - **dimensions**: Contains "dimension", "measurement", "face of stud", "centerline"
   - **materials**: Contains material names or spec section references
   - **installation**: Contains "install", "provide", "apply", "furnish"
   - **code**: Contains "code", "ADA", "fire", "egress", "rated"
   - **coordination**: Contains "coordinate", "verify", "field verify", "confirm"
   - **general**: Default category

**Step 4 — Note-to-Element Linking:**
For each keynote callout on the drawing:
1. Get the `leader_endpoint` position
2. Search for the nearest detected element from other passes:
   - Walls (Pass 3 wall lines) within 30px
   - Doors/windows (Pass 4 symbols) within 30px
   - Material zones (Pass 5) containing the endpoint
   - Equipment (Pass 11) within 30px
3. Record the nearest element type and ID as `points_to`

### Data Consumers for Hatch Refinement + Keynotes

| Consumer | Data Used | Purpose |
|----------|-----------|---------|
| Estimating | Refined material zones with accurate types | Material quantity takeoffs |
| Quality Management | Keynote descriptions, spec references | Inspection checklist generation |
| Submittal Intelligence | Spec section refs from keynotes/notes | Submittal compliance cross-check |
| Rendering Generator | Accurate material types from refined hatches | Photorealistic material mapping |
| Field Reference | General notes by category | Quick-lookup of construction requirements |
| Drawing Control | Keynote schedule completeness | Drawing QA/QC |
| Document Intelligence | Spec refs from notes | Enriching the spec reference index |

---

## Fallback Strategy

When visual analysis components fail:

| Component | Fallback | Impact |
|-----------|----------|--------|
| PaddleOCR unavailable | CRAFT text detection + basic OCR | Reduced text recognition accuracy |
| CRAFT unavailable | PaddleOCR only | May miss angled text |
| Both OCR unavailable | OpenCV text detection (limited) | Significantly reduced text extraction |
| scikit-image unavailable | Skip Pass 5 (material zones) | No hatch pattern detection |
| Low-resolution image (<200 DPI) | Upscale with interpolation | Reduced accuracy across all passes |
| Complex/busy sheet | Claude Vision validation catches misses | Human-in-the-loop correction |

The pipeline is designed to degrade gracefully — each pass runs independently and handles missing upstream data.
