# quantitative-intelligence — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the quantitative-intelligence skill.



## Sheet Cross-Reference Index

### What Gets Indexed

The cross-reference index captures every connection between sheets in the plan set:

| Reference Type | Example | Data Captured |
|---------------|---------|---------------|
| **Detail callout** | Circle with "3/A5.2" on floor plan | Source sheet, target sheet, target detail number, location (grid), linked elements |
| **Section cut** | Heavy dashed line with "A/A4.1" marker | Source sheet, target sheet, cut direction, elements crossed |
| **Interior elevation** | Triangle with "1/A6.1" | Source sheet, target sheet, viewing direction, room referenced |
| **Enlarged plan** | Dashed rectangle with "A3.1" ref | Source sheet, target sheet, area enclosed, scale change |
| **Schedule reference** | Door mark "D101" on plan → door schedule on A8.1 | Plan sheet, schedule sheet, item mark, item count on each |
| **Spec callout** | "09 65 00" text on plan or note | Sheet, spec section, context, all sheets it applies to |
| **General notes** | "SEE STRUCTURAL GENERAL NOTES S1.0" | Source sheet, target sheet, scope of applicability |
| **Wall type** | Wall type tag "2A" → wall type schedule | Plan sheet, schedule/legend sheet, wall type, all occurrences |

### Building the Index

The index is built automatically during document processing:

1. **During text extraction** (Phase 5): Parse sheet references from OCR'd text (patterns like "A5.2", "DETAIL 3/A5.2", "SEE SHEET S1.0")
2. **During visual analysis** (Phase 7): Detect detail callout bubbles, section markers, elevation markers as symbols, read their text content
3. **During DXF extraction** (Phase 6): Extract block attributes that contain sheet references
4. **Cross-validate**: Compare the index against the drawing index (sheet list) to flag references to missing sheets

### Spec Section Cross-References

When new spec sections are added via `/process-docs`:

1. Scan the new spec sections for plan sheet references (e.g., "See Sheet S2.1 for footing layout")
2. Add these to `sheet_cross_references.spec_references` — linking spec section → plan sheet
3. Scan for CSI division callouts that reference work types already in the quantity database
4. If a new spec section provides a value (e.g., concrete strength) that's also extracted from plans, cross-verify and flag discrepancies

### Using the Index

When calculating quantities or answering questions about specific elements:

1. **Look up the element** in the cross-reference index
2. **Follow assembly chains** to gather all related data from connected sheets
3. **Aggregate** dimensions, specs, and details from all linked sheets
4. **Calculate** derived quantities using the complete picture

**Example — "How much concrete for Footing F1?"**

```
Assembly Chain CHAIN-001: Footing F1 at Grid C-3
├── S2.1 (Foundation Plan): Location at C-3, plan dimensions 4'-0" x 8'-0"
├── S5.1 (Structural Details): Detail 3 — section shows depth 2'-0", rebar #5@12" E.W.
├── S1.0 (Structural Notes): 4,000 PSI concrete, #5 bars Grade 60
└── Spec 03 30 00: w/c ratio 0.45, slump 4"±1", air 5.5%±1.5%

Calculation:
  Volume = 4.0' × 8.0' × 2.0' = 64 CF = 2.37 CY
  Add 10% waste: 2.61 CY
  Concrete: 4,000 PSI per S1.0 / Spec 03 30 00
  Rebar: #5@12" E.W. per S5.1 Detail 3
```

---



## Multi-Source Completeness Checklist

For critical elements, make sure you've pulled data from ALL relevant sheets. If any source is missing, the calculation may be incomplete.

### Concrete Element (Footing, SOG, Wall, Column)

| Data Needed | Source Sheet | ✓ |
|------------|-------------|---|
| Plan dimensions (L × W) | Foundation/floor plan (S-100s) | |
| Depth/thickness | Structural detail (S-400s/500s) | |
| Reinforcing | Structural detail + structural notes (S-001) | |
| Concrete strength (f'c) | Structural general notes (S-001) | |
| Mix design details | Spec Section 03 30 00 | |
| Weather thresholds | Spec Section 03 30 00 | |
| Curing requirements | Spec Section 03 30 00 | |
| Testing frequency | Spec Section 03 30 00 + Div 01 QC | |
| Location (grid reference) | Foundation plan | |
| Elevation (TOF, BOF) | Foundation plan or grading plan | |
| Count (how many similar) | Foundation plan (count "TYP" instances) | |

### Pipe Run (Storm, Sanitary, Water, Fire)

| Data Needed | Source Sheet | ✓ |
|------------|-------------|---|
| Plan routing and length | Plumbing/civil plan (P/C-100s) | |
| Pipe size | Plan view labels | |
| Pipe material | Spec or plan notes | |
| Slope | Profile view or plan notes | |
| Invert elevations | Profile view | |
| Rim/structure elevations | Profile view or plan view | |
| Fitting count | Plan view (count elbows, tees, etc.) | |
| Hanger/support spacing | Spec or detail | |
| Insulation requirements | Spec (if applicable) | |
| Penetration locations | Plan view (through walls, floors) | |
| Sleeve requirements | Structural or architectural details | |

### Room Finishes

| Data Needed | Source Sheet | ✓ |
|------------|-------------|---|
| Room area (SF) | Floor plan (measured) | |
| Room perimeter (LF) | Floor plan (measured) | |
| Ceiling height | RCP or building section | |
| Floor material | Finish schedule (A-500s) | |
| Wall material/paint | Finish schedule | |
| Base type and height | Finish schedule | |
| Ceiling type | Finish schedule + RCP | |
| Door count and type | Door schedule (cross-ref room) | |
| Window count (if any) | Window schedule (cross-ref room) | |
| Light fixtures | RCP + lighting schedule | |
| HVAC diffusers | RCP + mechanical schedule | |
| Electrical devices | Electrical plan + panel schedule | |

### Site Work

| Data Needed | Source Sheet | ✓ |
|------------|-------------|---|
| Existing grades | Topo/survey (C-100 series, dashed contours) | |
| Proposed grades | Grading plan (C-200 series, solid contours) | |
| FFE | Architectural floor plan | |
| Pad elevation | Grading plan | |
| Paving section (thickness) | Paving detail (C-400/500s) | |
| Curb type and location | Site plan + curb detail | |
| Storm pipe routing | Utility plan + profile | |
| Sanitary pipe routing | Utility plan + profile | |
| Water service | Utility plan | |
| Erosion control limits | SWPPP/erosion control plan | |
| Tree protection | Landscape plan or civil notes | |
| Construction entrance | Erosion control plan | |

---



## Estimate-to-Field Quantity Reconciliation

Connect extracted plan quantities to estimating knowledge so the superintendent can manage costs in the field, not just geometry. Every quantity extracted by the assembly chain system should be traceable to a cost code, comparable against the bid estimate, convertible to an order quantity, and usable for pay application verification.

### CSI Cost Code Mapping

Every extracted quantity maps to a CSI MasterFormat cost code. This enables budget tracking, pay application line items, and trade-specific scope analysis.

#### Standard Mappings — Structural and Sitework

| Extracted Item | Unit | CSI Code | CSI Title |
|---------------|------|----------|-----------|
| Cast-in-place concrete (foundations) | CY | 03 30 00 | Cast-in-Place Concrete |
| Cast-in-place concrete (SOG) | CY | 03 30 00 | Cast-in-Place Concrete |
| Cast-in-place concrete (walls) | CY | 03 30 00 | Cast-in-Place Concrete |
| Reinforcing steel (rebar) | TON | 03 20 00 | Concrete Reinforcing |
| Formwork (foundations) | SFCA | 03 10 00 | Concrete Forming and Accessories |
| Formwork (walls) | SFCA | 03 10 00 | Concrete Forming and Accessories |
| Structural steel | TON | 05 12 00 | Structural Steel Framing |
| Miscellaneous metals | LBS | 05 50 00 | Metal Fabrications |
| Anchor bolts | EA | 05 50 00 | Metal Fabrications |
| Earthwork (cut) | CY | 31 23 16 | Excavation |
| Earthwork (fill) | CY | 31 23 23 | Fill |
| Aggregate base | TON | 31 25 00 | Erosion and Sedimentation Controls |
| Asphalt paving | TON | 32 12 16 | Asphalt Paving |
| Concrete paving | SF | 32 13 13 | Concrete Paving |

#### Standard Mappings — Architectural and Finishes

| Extracted Item | Unit | CSI Code | CSI Title |
|---------------|------|----------|-----------|
| CMU (block) | SF | 04 22 00 | Concrete Unit Masonry |
| Brick veneer | SF | 04 21 13 | Brick Masonry |
| Metal stud framing | LF | 09 22 16 | Non-Structural Metal Framing |
| Gypsum wallboard (GWB) | SF | 09 29 00 | Gypsum Board |
| Acoustical ceiling tile (ACT) | SF | 09 51 00 | Acoustical Ceilings |
| VCT flooring | SF | 09 65 16 | Resilient Tile Flooring |
| Carpet tile | SF | 09 68 13 | Tile Carpeting |
| Ceramic tile | SF | 09 30 00 | Tiling |
| Paint | SF | 09 91 00 | Painting |
| Vinyl base | LF | 09 65 13 | Resilient Base and Accessories |
| Hollow metal doors/frames | EA | 08 11 13 | Hollow Metal Doors and Frames |
| Wood doors | EA | 08 14 00 | Wood Doors |
| Hardware sets | EA | 08 71 00 | Door Hardware |
| Aluminum storefront | SF | 08 41 13 | Aluminum-Framed Entrances and Storefronts |

#### Standard Mappings — Mechanical, Electrical, Plumbing

| Extracted Item | Unit | CSI Code | CSI Title |
|---------------|------|----------|-----------|
| Plumbing fixtures | EA | 22 40 00 | Plumbing Fixtures |
| Domestic water piping | LF | 22 11 16 | Domestic Water Piping |
| Sanitary waste piping | LF | 22 13 16 | Sanitary Waste and Vent Piping |
| HVAC ductwork | LBS | 23 31 13 | Metal Ducts |
| Diffusers/registers | EA | 23 37 13 | Diffusers, Registers, and Grilles |
| RTU/AHU | EA | 23 74 00 | Packaged Outdoor HVAC Equipment |
| Electrical panelboards | EA | 26 24 16 | Panelboards |
| Duplex receptacles | EA | 26 27 26 | Wiring Devices |
| Light fixtures | EA | 26 51 00 | Interior Lighting |
| Fire sprinkler heads | EA | 21 13 13 | Wet-Pipe Sprinkler Systems |
| Fire alarm devices | EA | 28 31 00 | Fire Detection and Alarm |

#### Cost Code Hierarchy

CSI codes follow a strict hierarchy that enables roll-up reporting:

```
Division (2 digits)     03          — Concrete (all concrete work)
  Section (4 digits)    03 30       — Cast-in-Place Concrete
    Subsection (6 dig)  03 30 00    — Cast-in-Place Concrete (general)
      Item              03 30 00.10 — Footing F1 at Grid C-3 (project-specific)
```

When mapping extracted quantities, assign at the 6-digit level minimum. Project-specific item codes (the .10, .20, etc.) are assigned by the project estimator and should be matched to the bid breakdown if available.

#### Auto-Classification Rules

When an assembly chain produces a quantity, classify it automatically:

1. **Concrete assemblies** — Any chain that calculates volume in CY from formed elements routes to 03 30 00. If rebar is included in the chain, split: concrete volume to 03 30 00, rebar weight to 03 20 00, formwork area to 03 10 00.
2. **Masonry assemblies** — Any chain involving CMU block counts or masonry wall SF routes to 04 22 00. Reinforcing grout in CMU stays in 04 22 00 (not 03 30 00).
3. **Room finish assemblies** — Parse the finish schedule material column: VCT to 09 65 16, carpet to 09 68 13, ceramic tile to 09 30 00, paint to 09 91 00, ACT ceiling to 09 51 00.
4. **MEP assemblies** — Classify by system: pipe runs by pipe type (domestic water vs. sanitary vs. storm), ductwork to 23 31 13, electrical devices by type to appropriate 26 XX XX code.

### Plan-to-Estimate Quantity Comparison

The most valuable use of extracted quantities is comparing them against the bid estimate to catch scope changes before they become cost problems.

#### Reconciliation Workflow

```
Step 1: Extract plan quantity (from assembly chain)
Step 2: Look up bid quantity (from estimate, if available in project docs)
Step 3: Calculate delta = (plan qty - bid qty) / bid qty × 100%
Step 4: Classify impact using tolerance thresholds
Step 5: Recommend action based on classification
```

#### Tolerance Thresholds and Actions

| Delta Range | Classification | Action | Who Needs to Know |
|------------|---------------|--------|-------------------|
| ≤ 5% | **Within Estimate** | No action — normal measurement variance | Log only |
| 5% – 10% | **Monitor** | Note in quantity log, review at next OAC meeting | Superintendent + PM |
| 10% – 20% | **Investigate** | Compare plan revision dates, check for ASIs or addenda that explain the change | PM + estimator |
| > 20% | **Flag for Re-Pricing** | Likely scope change — initiate change order process | PM + estimator + owner |
| Negative (plan < bid) | **Potential Credit** | Verify reduction is real, not a measurement error; if confirmed, may need to issue credit CO | PM + estimator |

#### Trade-Level Scope Tracking

Roll up plan-vs-estimate deltas by CSI division to see which trades are growing or shrinking:

```
Division 03 — Concrete:     Plan 485 CY vs Bid 460 CY = +5.4% [MONITOR]
Division 04 — Masonry:      Plan 8,200 SF vs Bid 8,400 SF = -2.4% [WITHIN]
Division 09 — Finishes:     Plan 22,800 SF vs Bid 19,500 SF = +16.9% [INVESTIGATE]
Division 22 — Plumbing:     Plan 62 fixtures vs Bid 58 fixtures = +6.9% [MONITOR]
Division 26 — Electrical:   Plan 285 devices vs Bid 240 devices = +18.8% [INVESTIGATE]
```

When multiple divisions trend upward simultaneously, this often indicates an addendum or revision that added scope. Check the revision block on the plans against the bid set revision date.

### Material Procurement Quantities

Extracted quantities tell you how much material goes into the building. Order quantities account for waste, packaging, and practical field considerations.

#### Order Quantity Formula

```
Order Quantity = (Extracted Plan Quantity × Waste Factor) rounded up to packaging unit
```

#### Standard Waste Factors by Material

| Material | Waste Factor | Reason | Packaging Round-Up |
|----------|-------------|--------|-------------------|
| Concrete (formed) | +5–7% | Over-vibration, spillage, pump line cleanup | Nearest 0.5 CY (truck increment) |
| Concrete (SOG/flatwork) | +3–5% | Grade variance, bulkheads | Nearest 0.5 CY |
| Rebar | +3–5% | Lap splices, cut waste, bent bar waste | Nearest bundle (varies by bar size) |
| CMU block | +3–5% | Cutting, breakage, corners | Nearest cube (90 for 8" standard) |
| Lumber (framing) | +7–10% | Crown cull, cutting waste, damaged pieces | Nearest unit (per piece) |
| Plywood/OSB sheathing | +5–8% | Cutting waste at edges and openings | Nearest sheet (4x8) |
| Gypsum wallboard | +10–12% | Cutouts for openings, damaged sheets, butt joints | Nearest sheet (4x8 or 4x12) |
| Paint | +10–15% | Touch-up, multiple coats, surface texture variation | Nearest gallon or 5-gallon bucket |
| Roofing membrane | +5–8% | Side laps, end laps, edge trim waste | Nearest roll |
| Ceramic/porcelain tile | +10–15% | Cuts at walls, pattern waste, breakage | Nearest box (varies by tile size) |
| Carpet tile | +5–8% | Pattern matching, cuts at walls, attic stock | Nearest carton (typically 48 SF) |
| VCT | +5–8% | Cuts at walls, pattern alignment, breakage | Nearest carton (typically 45 SF) |
| ACT ceiling tile | +5–8% | Border cuts, damaged tiles, attic stock | Nearest carton (varies) |
| Insulation (batt) | +3–5% | Compression at framing, cutting waste | Nearest bag/roll |
| Insulation (rigid board) | +5–8% | Cutting waste at corners and penetrations | Nearest sheet (4x8) |
| Ductwork | +5–8% | Fittings waste, field adjustments | Nearest LF or EA |
| Piping (copper/PVC) | +5–8% | Fittings allowance, cut waste | Nearest 10 LF or 20 LF stick |
| Conduit | +5–8% | Bends, cut waste | Nearest 10 LF stick |
| Wire/cable | +10–12% | Homeruns, slack loops, termination waste | Nearest 250 LF or 1000 LF spool |

#### Procurement Example

```
Assembly Chain: SOG Area B
  Extracted plan area: 4,800 SF
  Slab thickness: 6" (from structural notes)
  Concrete volume: 4,800 × 0.5 / 27 = 88.9 CY
  Waste factor: +5% → 88.9 × 1.05 = 93.3 CY
  Truck round-up: 94 CY (nearest 0.5 CY = 94.0)
  Truck count at 10 CY/truck: 10 trucks (9.4 → round up)

  WWF 6×6-W1.4×W1.4: 4,800 SF + 10% lap allowance = 5,280 SF
  Roll round-up: 5,280 / 750 SF per roll = 7.04 → 8 rolls

  Vapor barrier (10 mil): 4,800 SF + 10% lap = 5,280 SF
  Roll round-up: 5,280 / 600 SF per roll = 8.8 → 9 rolls
```

#### Lead Time Awareness

When extracted quantities are large or involve specialty items, flag lead time concerns:

| Material | Typical Lead Time | Flag Threshold |
|----------|------------------|----------------|
| Ready-mix concrete | 24–48 hours (standard mixes) | >100 CY single pour (need pump + staging plan) |
| Structural steel | 8–12 weeks (fabrication) | All structural steel (always long lead) |
| Rebar (fabricated) | 2–4 weeks | >5 TON total or custom bent shapes |
| Hollow metal frames | 4–6 weeks | >20 frames or custom sizes |
| Aluminum storefront | 8–12 weeks | All storefront/curtain wall |
| Rooftop HVAC units | 10–16 weeks | All RTUs/AHUs |
| Electrical switchgear | 12–20 weeks | Main distribution and large panels |
| Elevator | 16–24 weeks | All elevators |
| Fire sprinkler fabrication | 4–6 weeks | All sprinkler systems (after approved drawings) |
| Specialty tile/stone | 6–12 weeks | Imported or custom materials |

**Decision rule**: If extracted quantity triggers a flag threshold AND the schedule shows that trade starting within 2× the lead time window, issue a procurement alert to the superintendent.

### Pay Application Verification

Use extracted quantities as an independent check on monthly pay applications. The superintendent's job is to verify that the percent complete claimed on a pay application reflects reality in the field.

#### Quantity-in-Place Method

The most reliable way to verify progress is to measure what is actually installed and compare it to the total extracted quantity:

```
% Complete = Installed Quantity / Total Extracted Quantity × 100

Example — Concrete Foundations:
  Total extracted: 42.3 CY (from assembly chains, all footings + grade beams)
  Installed to date: Footings F1–F4 poured = 9.5 CY (measured from pour tickets)
  % Complete = 9.5 / 42.3 = 22.5%

  Contractor claimed: 25% → Delta = 2.5% → ACCEPTABLE (within 5% tolerance)
```

#### Unit Price Verification

Compare the unit price on the schedule of values against the contract unit price:

| Check | Formula | Flag If |
|-------|---------|---------|
| Unit price match | SOV unit price vs. contract unit price | Difference > $0.01 |
| Line item math | Claimed qty × unit price = claimed amount | Does not equal |
| Total check | Sum of line items = total contract amount | Does not equal |
| Retainage | Earned amount × retainage % = retainage withheld | Does not equal |

#### Earned Value Calculation

```
Earned Value = Installed Quantity × Contract Unit Price

Example — CMU Masonry:
  Contract: 8,400 SF CMU × $18.50/SF = $155,400 (schedule of values line item)
  Installed this period: 1,200 SF
  Installed to date: 4,800 SF
  Earned this period: 1,200 × $18.50 = $22,200
  Earned to date: 4,800 × $18.50 = $88,800
  % Complete: 4,800 / 8,400 = 57.1%
```

#### Unusual Progress Flags

Flag pay application line items that show suspicious progress jumps:

| Condition | Flag Level | Action |
|-----------|-----------|--------|
| Single period jump > 15% on items > $50,000 | **WARNING** | Verify with field observation — was that much work actually done? |
| Item goes from < 20% to > 80% in one period | **ALERT** | Almost certainly incorrect — request backup documentation |
| Item at 100% but work visibly incomplete | **REJECT** | Do not approve — require revised pay app |
| Item decreasing (negative progress) | **INVESTIGATE** | May indicate prior over-billing being corrected |
| Multiple items all at same round % (e.g., all 50%) | **SUSPICIOUS** | Suggests contractor estimated rather than measured |
| Stored material claimed > 30% of line item | **VERIFY** | Confirm material is on-site, properly stored, and matches specs |

---



## Assembly Chain Cost Awareness

Extend the assembly chain system with cost intelligence so the superintendent can understand the dollar impact of every quantity, flag high-value assemblies for enhanced QC, calculate change order impacts quickly, and track budget performance at the assembly level.

### Unit Cost Attachment

For each assembly chain, attach approximate unit cost ranges to transform quantities into cost estimates. Use ranges rather than point estimates because material and labor costs are market-dependent and vary by region, season, and project conditions.

#### Structural Assembly Cost Example

```
Assembly Chain CHAIN-001: Footing F1 at Grid C-3
├── Concrete: 2.37 CY × $180–220/CY    = $427–$521 (material only)
├── Rebar: 0.18 TON × $1,400–1,800/TON  = $252–$324 (material + placement)
├── Formwork: 56 SFCA × $8–12/SFCA      = $448–$672 (form + strip)
├── Excavation: 3.2 CY × $15–25/CY      = $48–$80
└── Backfill: 1.8 CY × $12–20/CY        = $22–$36
    ─────────────────────────────────────────────────
    Total Assembly Cost (material):         $1,197–$1,633
    Labor factor (typically 1.0–1.5× material for concrete): +$1,197–$2,450
    Estimated Installed Cost:               $2,394–$4,083
```

#### Architectural Finish Assembly Cost Example

```
Assembly Chain CHAIN-047: Room 201 — Office (320 SF)
├── VCT Flooring: 320 SF × $3.50–5.00/SF     = $1,120–$1,600
├── Vinyl Base: 72 LF × $2.00–3.50/LF        = $144–$252
├── GWB Walls: 864 SF × $3.00–4.50/SF         = $2,592–$3,888
├── Paint (2 coats): 864 SF × $1.50–2.50/SF   = $1,296–$2,160
├── ACT Ceiling: 320 SF × $3.50–5.50/SF       = $1,120–$1,760
├── HM Door/Frame: 1 EA × $800–1,200/EA       = $800–$1,200
└── Hardware Set: 1 EA × $350–600/EA           = $350–$600
    ─────────────────────────────────────────────────
    Estimated Installed Cost (this room):       $7,422–$11,460
```

#### Unit Cost Reference Ranges

These ranges represent typical installed costs (material + labor) for common assemblies. Actual costs depend on project location, market conditions, complexity, and access:

| Assembly Type | Unit | Low Range | Mid Range | High Range | Notes |
|--------------|------|-----------|-----------|------------|-------|
| CIP concrete (foundations) | CY | $350 | $500 | $750 | Includes form, place, finish, strip |
| CIP concrete (SOG) | SF | $6 | $9 | $14 | Includes prep, place, finish |
| CIP concrete (walls) | SF | $25 | $35 | $50 | Includes form both sides, place, strip |
| Rebar (placed) | TON | $1,800 | $2,400 | $3,200 | Includes cut, bend, place, tie |
| CMU wall (grouted + reinforced) | SF | $14 | $20 | $28 | Includes block, grout, rebar, labor |
| Structural steel (erected) | TON | $4,500 | $6,000 | $8,500 | Includes fabrication, erection, connections |
| Metal stud + GWB (one side) | SF | $5 | $8 | $12 | Includes stud, board, tape, finish |
| Metal stud + GWB (both sides) | SF | $9 | $14 | $20 | Includes stud, both sides board, finish |
| ACT ceiling | SF | $4 | $6 | $9 | Includes grid and tile |
| VCT flooring | SF | $3 | $5 | $7 | Includes adhesive and installation |
| Carpet tile | SF | $4 | $6 | $10 | Includes adhesive and installation |
| Ceramic tile (floor) | SF | $10 | $16 | $25 | Includes setting material and grout |
| Ceramic tile (wall) | SF | $12 | $20 | $30 | Includes backer board, setting, grout |
| Paint (2 coats, walls) | SF | $1.25 | $2.00 | $3.00 | Includes primer and 2 finish coats |
| HM door + frame + hardware | EA | $1,500 | $2,200 | $3,500 | Complete opening |
| Aluminum storefront | SF | $40 | $65 | $90 | Includes frame, glass, hardware |
| Ductwork (rectangular) | LB | $6 | $10 | $15 | Fabricated and installed |
| Copper pipe (3/4"–2") | LF | $18 | $28 | $45 | Installed with fittings |
| PVC DWV pipe (2"–4") | LF | $12 | $18 | $28 | Installed with fittings |
| EMT conduit (3/4"–1") | LF | $8 | $14 | $22 | Installed with fittings and wire |
| Duplex receptacle | EA | $120 | $180 | $250 | Installed with box, whip, device |
| Light fixture (2x4 LED) | EA | $250 | $400 | $600 | Installed with whip and connection |
| Sprinkler head (pendant) | EA | $80 | $130 | $200 | Installed with drop and head |

### High-Cost Assembly Flagging

Not all assemblies warrant the same level of QC attention. Flag assemblies that represent significant cost or risk so the superintendent can allocate inspection time where it matters most.

#### Cost-Based Flags

| Condition | Flag Type | Superintendent Action |
|-----------|----------|----------------------|
| Assembly installed cost > $10,000 | **HIGH-VALUE** | Enhanced inspection: verify dimensions before pour/cover, witness critical operations |
| Assembly installed cost > $50,000 | **CRITICAL-VALUE** | Pre-work meeting with trade foreman, inspect at each phase, photo documentation |
| Assembly installed cost > $100,000 | **MAJOR-VALUE** | Dedicated QC plan, third-party inspection consideration, daily progress tracking |

#### Specialty Material Flags (Automatic, Regardless of Cost)

These materials get flagged automatically because they have high rework costs, are difficult to repair, or require specialized skills:

| Material/Assembly | Flag Reason | Extra QC Steps |
|------------------|-------------|----------------|
| Architectural concrete (exposed) | Cannot repair cosmetically — must be right the first time | Review form liner, verify release agent, witness pour, inspect immediately at strip |
| Curtain wall / aluminum storefront | Long lead replacement, precision fit required | Check opening dimensions before order, inspect anchors before install |
| Terrazzo flooring | Expensive material, skilled labor, cannot easily patch | Verify substrate flatness, witness pour/grind, protect during other work |
| Epoxy flooring | Surface prep critical, fails if moisture present | Verify moisture test results, check substrate prep, temperature during install |
| Waterproofing (below grade) | Buried and inaccessible after backfill | Inspect every joint, flood test before backfill, photo document |
| Structural steel connections | Structural integrity, cannot easily re-do | Verify bolt torque or weld inspection, check plumbness |
| Fire-rated assemblies | Life safety, code compliance, inspection required | Verify UL assembly matches drawings, inspect penetration seals, document |
| Medical gas piping | Life safety, specialized testing required | Witness pressure test, verify brazer certification |

#### Critical Path + Cost Combined Flag

When an assembly is both high-cost AND on the critical path, it gets a combined flag:

```
⚠ CRITICAL PATH + HIGH VALUE: SOG Pour Area B
  Cost: ~$85,000 (156 CY concrete + WWF + VB + finishing)
  Schedule: 3-day activity on critical path, Day 45–47
  Delay impact: Every day of delay = 1 day to project completion
  Action: Pre-pour meeting required, pump truck confirmed, concrete plant notified,
          finishing crew sized for full area, weather window confirmed 72 hours out
```

### Change Impact Calculation

When a plan revision changes a dimension, spec, or quantity, trace through the assembly chain to estimate cost impact. This gives the superintendent immediate ammunition for change order discussions.

#### Dimension Change Impact

When a physical dimension changes, the cost impact ripples through the assembly:

```
CHANGE: Footing F1 depth increased from 2'-0" to 2'-6" (per ASI-004)

Assembly Chain CHAIN-001: Footing F1 at Grid C-3
  Original: 4.0' × 8.0' × 2.0' = 64 CF = 2.37 CY
  Revised:  4.0' × 8.0' × 2.5' = 80 CF = 2.96 CY
  Delta:    +0.59 CY concrete

  Cost Impact Breakdown:
  ├── Concrete: +0.59 CY × $200/CY (mid-range)   = +$118
  ├── Rebar: additional bottom mat area = same, but +2 vertical bars
  │   +0.04 TON × $2,400/TON                       = +$96
  ├── Formwork: +6" depth × 24 LF perimeter = +12 SFCA
  │   +12 SFCA × $10/SFCA                          = +$120
  ├── Excavation: +0.59 CY × $20/CY                = +$12
  └── Backfill: net change minimal                  = $0
      ──────────────────────────────────────────────
      Estimated Change Impact (this footing):        +$346

  If "TYP" for 6 similar footings:                  +$2,076
```

#### Specification Change Impact

When a material spec changes without a dimension change:

```
CHANGE: Concrete strength increased from 3,000 PSI to 4,000 PSI (per RFI-007)

  Affected assemblies: All SOG pours (Areas A, B, C)
  Total quantity: 312 CY (unchanged)

  Cost Impact:
  ├── 3,000 PSI concrete: ~$135/CY (material delivered)
  ├── 4,000 PSI concrete: ~$145/CY (material delivered)
  ├── Unit price delta: +$10/CY
  └── Total impact: 312 CY × $10/CY = +$3,120

  Additional considerations:
  ├── Testing frequency may increase (higher strength = more cylinders)
  │   Estimated: +8 sets × $45/set = +$360
  └── Curing requirements may be stricter (longer wet cure)
      Estimated: +$500 (additional labor for curing compound/blankets)
      ──────────────────────────────────────────────
      Total Estimated Change Impact:                 +$3,980
```

#### Change Impact Formatting for Change Order Support

Present change impacts in a format ready for change order documentation:

```
CHANGE ORDER REQUEST — ASI-004: Increased Foundation Depths

Line Item 1: Footing Type F1 (6 EA)
  Added concrete:    +3.54 CY × $500/CY installed    = $1,770.00
  Added rebar:       +0.24 TON × $2,400/TON installed = $576.00
  Added formwork:    +72 SFCA × $10/SFCA installed     = $720.00
  Added excavation:  +3.54 CY × $20/CY                = $70.80
                                           Subtotal:   $3,136.80

Line Item 2: Footing Type F2 (4 EA)
  Added concrete:    +2.96 CY × $500/CY installed    = $1,480.00
  Added rebar:       +0.20 TON × $2,400/TON installed = $480.00
  Added formwork:    +48 SFCA × $10/SFCA installed     = $480.00
  Added excavation:  +2.96 CY × $20/CY                = $59.20
                                           Subtotal:   $2,499.20

                               Direct Cost Total:      $5,636.00
                               Overhead (10%):          $563.60
                               Profit (10%):            $619.96
                               CHANGE ORDER TOTAL:      $6,819.56
```

#### Additive vs. Credit Calculations

Changes can increase or decrease scope. Track both:

| Change Type | Calculation | Format |
|------------|-------------|--------|
| **Additive** (more work) | New qty − original qty = added qty × unit price = ADD | Positive dollar amount |
| **Credit** (less work) | Original qty − new qty = deleted qty × unit price = CREDIT | Negative dollar amount (shown in parentheses) |
| **Substitution** (different spec) | (New unit price − old unit price) × quantity = NET | Can be add or credit |
| **Net change** | Sum of all adds and credits per CSI code = NET IMPACT | Show both gross and net |

### Budget Tracking Integration

Connect assembly-level cost awareness to overall project budget tracking so the superintendent has early warning when costs diverge from the estimate.

#### Assembly Cost to Budget Line Item Flow

```
Assembly Chain (CHAIN-001)
  └── Calculated cost: $2,394–$4,083
       └── CSI Code: 03 30 00 (concrete) + 03 20 00 (rebar) + 03 10 00 (formwork)
            └── Budget line items: 03 30 00 = $186,000 (total concrete budget)
                 └── Forecast: Budget ± approved COs ± pending COs = projected final cost
```

#### Budget Performance Tracking by Assembly Type

Track actual unit costs against estimated unit costs as work is completed:

| Assembly Type | Estimated Unit Cost | Actual Unit Cost | Variance | Status |
|--------------|--------------------|--------------------|----------|--------|
| Footings (CIP concrete) | $480/CY installed | $510/CY installed | +6.3% | MONITOR |
| SOG (6" w/ WWF) | $8.50/SF | $8.20/SF | -3.5% | WITHIN |
| CMU walls (grouted) | $19.00/SF | $22.50/SF | +18.4% | INVESTIGATE |
| GWB partitions | $12.00/SF | $11.75/SF | -2.1% | WITHIN |
| ACT ceilings | $5.50/SF | $5.50/SF | 0% | WITHIN |
| VCT flooring | $4.25/SF | — | — | NOT STARTED |

#### Early Warning Triggers

| Condition | Alert Level | Action |
|-----------|------------|--------|
| Actual unit cost exceeds estimate by > 10% | **WARNING** | Investigate cause — was it a one-time issue or a trend? Review remaining work for same assembly type |
| Actual unit cost exceeds estimate by > 20% | **ESCALATE** | Notify PM immediately — may need budget revision or value engineering for remaining work |
| 3+ consecutive assemblies of same type over estimate | **TREND** | Systemic issue — the estimate may have been too low for this trade, or site conditions are driving up costs |
| Total committed + forecast exceeds budget by > 5% | **BUDGET ALERT** | Comprehensive review needed — identify offsets or request contingency release |
| Change orders consuming contingency > 50% with < 50% complete | **CONTINGENCY ALERT** | Project is trending over budget — escalate to owner and explore cost-saving measures |

#### Forecast Update Workflow

When new actual cost data comes in (from pay applications, purchase orders, or field reports):

```
Step 1: Record actual cost for completed assembly
Step 2: Calculate actual unit cost = total cost / quantity installed
Step 3: Compare to estimated unit cost → flag if > 10% variance
Step 4: Update forecast for remaining assemblies of same type:
        Remaining cost = remaining qty × actual unit cost (if trend) or estimated (if one-time issue)
Step 5: Roll up to division level → update project forecast
Step 6: Compare forecast to budget + approved COs → report variance
```

---



## Resources

### references/
- **sheet_xref.py** — Sheet cross-reference index builder. Parses extraction results to build drawing index, detail callouts, schedule references, spec references, and assembly chains. Outputs to config JSON.
- **calc_bridge.py** — Multi-source calculation engine. Takes assembly chains + extracted data from DXF, visual, takeoff, and text sources. Calculates derived quantities (volumes, areas, counts). Flags discrepancies. Outputs to config JSON quantities section.

### External Dependencies
- **parse_dxf.py** (Phase 6) — DXF spatial extraction for exact coordinates and areas
- **visual_plan_analyzer.py** (Phase 7) — Visual extraction for OCR, symbols, material zones
- **construction-takeoff skill** (Anthropic built-in) — Scale-calibrated measurements from plan images
- **project-data skill** — Config read/write for storing quantities in project intelligence

## Spatial Clash Detection — Multi-Discipline Coordination

Construction documents are drawn by different disciplines (Architecture, Structural, Mechanical, Electrical, Plumbing, Fire Protection) working on the same building. Each discipline draws their systems on **separate sheets but in the same physical space**. Conflicts happen when two systems try to occupy the same location.

### How 2D Clash Detection Works

Since we're working from 2D drawings (not 3D BIM), clash detection is done by **comparing elevation data across disciplines** at the same plan location:

1. **Identify shared spaces** — Areas where multiple disciplines have systems (above ceilings, in mechanical rooms, in walls, at floor penetrations)
2. **Extract elevation data** from each discipline at those locations
3. **Compare** — If two elements occupy the same horizontal location AND the same elevation range, there's a potential clash

### What to Compare

| Discipline A | Discipline B | Potential Clash | How to Check |
|-------------|-------------|----------------|-------------|
| **Mechanical ductwork** | **Structural beams** | Duct routing conflicts with beam depth | Compare duct bottom elevation vs beam bottom elevation at crossing points |
| **Plumbing waste pipe** | **Electrical conduit** | Both running at same elevation in ceiling | Compare pipe centerline elevation vs conduit elevation at crossings |
| **Plumbing waste pipe** | **Structural beam** | Pipe penetrating beam (not allowed without engineer approval) | Check if pipe elevation passes through beam depth at crossing |
| **HVAC diffuser** | **Light fixture** | Both trying to occupy same ceiling grid location | Compare RCP locations — diffusers and fixtures should not overlap |
| **Sprinkler main** | **Ductwork** | Fire protection main conflicts with duct routing | Compare elevations at crossing points |
| **Electrical panel** | **Door swing** | Panel blocked by door opening | Check door swing arc vs panel face clearance (36" clear required) |
| **Equipment clearance** | **Wall/column** | Maintenance access blocked | Check equipment service clearance envelope vs nearby obstructions |

### Elevation Data Sources by Discipline

To do clash detection, you need elevation data. Here's where to find it:

| Element | Where Elevation Is Shown |
|---------|------------------------|
| **Structural beams** | Structural framing plan (TOS = Top of Steel), building sections |
| **Ductwork** | Mechanical plan (duct sizes shown, bottom of duct noted or derivable from ceiling height minus duct depth) |
| **Piping** | Plumbing plan (inverts and pipe size give you the full profile), riser diagrams |
| **Conduit** | Electrical plan (usually follows ceiling space — elevation rarely noted explicitly, assume just below structure) |
| **Sprinkler mains** | Fire protection plan (elevation noted or derivable from ceiling type and required clearance) |
| **Ceiling plane** | RCP (ceiling height noted by room) |

### Clearance Rules

When systems cross, minimum clearances apply:

| Crossing | Minimum Clearance |
|----------|------------------|
| Duct below beam | 1" minimum (but consider insulation) |
| Pipe below beam | Pipe OD + hangers + 1" |
| Sprinkler below duct | 1-3" below duct bottom (per NFPA) |
| Anything above ceiling | Must fit between structure bottom and ceiling grid top (typically 12"-36" of plenum space) |
| Mechanical equipment | 36" service clearance on access side |
| Electrical panels | 36" clear in front (NEC), 30" wide |

### How to Report Clashes

When a potential clash is detected, report it with:

```
POTENTIAL CLASH: Plumbing vs Structural at Grid C-3
- 4" waste pipe at elevation 112'-6" (from P-101, heading east)
- W12x26 beam bottom at elevation 112'-4" (from S-201, running N-S)
- Conflict: Pipe centerline is 2" ABOVE beam bottom
- Impact: Pipe would penetrate beam web — requires structural engineer review
- Resolution options: (1) Reroute pipe below beam, (2) Core drill with sleeve (needs SE approval)
```

### Practical Coordination Sequence

When processing a full plan set:

1. **Extract structural framework first** — beam locations, sizes, bottom elevations (this is the "ceiling" that everything else must fit under)
2. **Extract mechanical ductwork** — main trunk lines, sizes, routing (these are the biggest elements in the ceiling space)
3. **Extract plumbing** — waste and supply lines, sizes, elevations where noted
4. **Extract fire protection** — mains and branch lines
5. **Extract electrical** — conduit runs (typically smallest, most flexible)
6. **Compare at every crossing point** — any location where two disciplines cross paths on the plan
7. **Check plenum depth** — at every point, verify that ALL systems fit between the structural bottom and the ceiling plane

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


