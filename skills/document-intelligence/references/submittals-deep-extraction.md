# Submittals - Deep Extraction Guide

Extract comprehensive, field-actionable data from submittal packages — the product data, shop drawings, mix designs, and cut sheets that subcontractors and suppliers submit for approval. These documents contain the actual products and materials that will be installed, making them critical for procurement tracking, field verification, quality control, and **visual rendering accuracy**.

---

## Extraction Priority Matrix

| Priority | Submittal Type | Use Case | Completeness Target |
|----------|---------------|----------|-------------------|
| **CRITICAL** | Concrete mix designs | Placement verification, weather protocols, testing | 100% — all mixes |
| **CRITICAL** | Structural steel shop drawings | Erection, connection verification, piece marks | 100% — all connections |
| **HIGH** | Door hardware submittals | Procurement, keying, ADA compliance | 100% — all hardware sets |
| **HIGH** | MEP equipment submittals | Startup, commissioning, O&M | 100% — all major equipment |
| **HIGH** | Fire-rated assemblies | Code compliance, inspection requirements | 100% if present |
| **HIGH** | [RENDERING] Exterior panel/cladding submittals | Color, profile, finish accuracy for rendering | 100% if present |
| **HIGH** | [RENDERING] Casework/millwork shop drawings | Cabinet layout, finish, hardware for visualization | 100% if present |
| **MEDIUM** | [RENDERING] Finish material submittals | Installation verification, color approval, floor-to-ceiling rendering | 100% if present |
| **MEDIUM** | [RENDERING] Lighting fixture submittals | Fixture type, appearance, mounting for interior visualization | 100% if present |
| **MEDIUM** | [RENDERING] Window/glazing submittals | Frame finish, glass appearance, mullion details | 100% if present |
| **MEDIUM** | Waterproofing/roofing submittals | Warranty, installation requirements | 100% if present |
| **LOW** | Miscellaneous product data | General reference | Key specs only |

---

## CONCRETE MIX DESIGNS

### Document Identification

**Signals this is a concrete mix design**:
- Lab or ready-mix producer letterhead (Wells Concrete, Cemstone, local batch plants)
- Table with mix proportions (cement, aggregates, water, admixtures)
- Mix ID or mix number designation
- Design strength (f'c) and W/C ratio prominently displayed
- ASTM references for materials
- May include trial batch test results

### Extraction Targets

**EXTRACT FOR EVERY MIX DESIGN**:

| Data Point | Unit | Example |
|-----------|------|---------|
| Mix ID / designation | Text | "Mix #4000-A-45" |
| Design strength (f'c) | PSI | "4,000 PSI at 28 days" |
| W/C ratio (maximum) | Ratio | "0.45" |
| Slump (target ± tolerance) | Inches | "4\" ± 1\"" |
| Air content (target ± tolerance) | Percent | "5.5% ± 1.5%" |
| Unit weight | PCF | "145 PCF" |
| Cement type | ASTM C150 | "Type I/II" |
| Cement content | Lbs/CY | "564 lbs/CY" |
| Fly ash or pozzolan | Lbs/CY, % replacement | "141 lbs/CY (20% replacement)" |
| Coarse aggregate | Size, source, ASTM | "#57 limestone, ASTM C33" |
| Fine aggregate | Source, FM, ASTM | "Natural sand, FM 2.8, ASTM C33" |
| Water | Lbs/CY | "267 lbs/CY" |
| Admixtures (each) | Name, dosage | |
| — Water reducer | oz/cwt | "HRWR: 6 oz/cwt" |
| — Air entraining | oz/cwt | "AE: 1.5 oz/cwt" |
| — Retarder | oz/cwt | "Retarder: 3 oz/cwt" |
| — Accelerator | oz/cwt | "Accelerator: 20 oz/cwt (cold weather)" |
| — Fiber reinforcement | lbs/CY | "Synthetic fiber: 1.5 lbs/CY" |
| Max aggregate size | Inches | "3/4\"" |
| Intended use | Element type | "Slab on grade" |

### Weather-Related Mix Variations

Look for cold/hot weather mix modifications:
- **Cold weather mix**: Higher cement content, accelerator, no retarder, possibly heated water
- **Hot weather mix**: Retarder, ice replacement for water, lower cement content
- **Self-consolidating concrete (SCC)**: For congested reinforcement areas

### Spec Compliance Check

Cross-reference extracted mix data against project specifications (Div 03 30 00):
- f'c meets or exceeds spec requirement
- W/C ratio is at or below spec maximum
- Air content range matches spec (especially for exterior/freeze-thaw exposure)
- Aggregate size compatible with rebar spacing and cover
- Cement type matches spec
- Admixtures are approved types

**Output format**:
```json
{
  "concrete_mixes": [
    {
      "mix_id": "4000-A-45",
      "producer": "Wells Concrete",
      "design_strength": "4,000 PSI at 28 days",
      "wc_ratio": "0.45 max",
      "slump": "4\" ± 1\"",
      "air_content": "5.5% ± 1.5%",
      "cement": {"type": "I/II", "content": "564 lbs/CY"},
      "fly_ash": {"type": "Class F", "content": "141 lbs/CY", "replacement": "20%"},
      "coarse_agg": "#57 limestone, ASTM C33",
      "fine_agg": "Natural sand, FM 2.8",
      "water": "267 lbs/CY",
      "admixtures": [
        {"type": "HRWR", "product": "Sika ViscoCrete", "dosage": "6 oz/cwt"},
        {"type": "Air entraining", "product": "Sika Aer", "dosage": "1.5 oz/cwt"}
      ],
      "max_agg_size": "3/4\"",
      "intended_use": "Slab on grade",
      "spec_section": "03 30 00",
      "spec_compliant": true,
      "notes": "Normal weight concrete for interior SOG"
    }
  ]
}
```

---

## DOOR HARDWARE SUBMITTALS

### Document Identification

**Signals this is a door hardware submittal**:
- Hardware distributor or manufacturer letterhead
- Hardware group/set numbers (HW-1, HW-2, etc.)
- Product cut sheets with images and specifications
- Keying schedule or cylinder chart
- References to Div 08 71 00 (Door Hardware) spec section
- Multiple manufacturers represented (lock, closer, hinges, etc.)

### Hardware Set Extraction

**EXTRACT FOR EVERY HARDWARE SET**:

| Data Point | Example |
|-----------|---------|
| Hardware set number | "HW-1" |
| Set description | "Standard interior passage" |
| Doors assigned to this set | "101, 102, 103, 107, 108" |
| Door type reference | "A" (from door schedule) |

**FOR EACH ITEM IN THE SET**:

| Data Point | Example |
|-----------|---------|
| Item description | "Lockset" |
| Manufacturer | "Schlage" |
| Series/model | "ND Series, ND53PD" |
| Function | "Entrance/office" |
| Finish | "626 (Satin Chrome)" |
| Fire rating | "UL 3-hour" |
| ADA compliant | Yes — lever handle |
| Quantity per set | 1 |
| Handing | "LH/LHR" or "Field reversible" |

### Common Hardware Items to Extract

- **Hinges**: Manufacturer, size (4-1/2\" × 4-1/2\"), weight, material, finish, quantity per door, fire-rated
- **Locksets/levers**: Manufacturer, series, function (passage, privacy, classroom, storeroom, entrance), finish, cylinder type
- **Closers**: Manufacturer, model, size/force, mount type (regular, parallel, top jamb), hold-open, fire-rated
- **Exit devices**: Manufacturer, model, type (rim, SVR, CVR, mortise), fire-rated, dogging
- **Door stops/holders**: Type (wall, floor, overhead), magnetic hold-open (fire-rated), finish
- **Kick/mop/push/pull plates**: Size, material, finish
- **Thresholds**: Type (saddle, offset, thermal), material, width, ADA compliance
- **Weatherstripping**: Type (perimeter, sweep, astragal), material
- **Silencers**: Quantity per frame (3 for single, 4 for pair)
- **Viewers/peepholes**: If required
- **Overhead stops**: If specified

### Finish Code Cross-Reference [RENDERING]

Extract and map finish codes to visual descriptions for rendering accuracy:

| Finish Code | Description | Visual Appearance | Notes |
|-------------|-------------|-------------------|-------|
| 626 | Satin Chrome | Brushed silver-gray, matte | Most common; subtle grain visible |
| 652 | Satin Chrome Plated | Lighter silver, smooth | Thinner plating than 626 |
| US26D | Satin Chrome | Brushed silver-gray, matte | Equivalent to 626 |
| US32D | Satin Stainless Steel | Warm silver, brushed | More corrosion-resistant; coastal use |
| 613 | Oil Rubbed Bronze | Dark brown-black, aged patina | High-touch areas show wear pattern |
| US10B | Oil Rubbed Bronze | Dark brown-black | ANSI equivalent |
| US3 | Polished Brass | Bright gold, lustrous | Requires maintenance; yellows over time |
| 622 | Flat Black | Pure black, non-reflective | Modern aesthetic; can show fingerprints |
| 630 | Satin Stainless Steel | Warm brushed silver | Healthcare/institutional standard |
| US4 | Oil Rubbed Bronze | Dark finish | Heavier patina than 613 |

### Hardware Finish Consistency Check [RENDERING]

When extracting multiple hardware sets, flag mixed finishes:

**Example notation**:
```
NOTE: Mixed finishes detected
- HW-1 (Passage doors, rooms 101-108): 626 Satin Chrome
- HW-2 (Restroom doors, rooms 102R-105R): 622 Flat Black
- HW-3 (Exterior entries): 630 Satin Stainless Steel

RECOMMENDATION: For rendering, use 626 Satin Chrome as predominant finish
(appears on 60% of door hardware)
```

### Keying Schedule

**EXTRACT**:
- **Key system**: Master key, grand master, construction master
- **Keying groups**: Which doors are keyed alike
- **Master key levels**: Number of levels, key hierarchy
- **Construction keying**: Temporary construction master that gets voided
- **Key quantities**: Per cylinder/per group
- **Restricted keyway**: If proprietary keyway is specified

### ADA Compliance Summary

For each hardware set, note:
- Lever handles (not knobs) — required for accessible doors
- Closer force: max 5 lbs (exterior) / 5 lbs (interior) opening force
- Threshold height: max 1/2\" (1/4\" vertical, 1/2\" beveled)
- Hardware mounting height: 34\" to 48\" AFF
- Automatic opener: If specified for accessible entries

**Output format**:
```json
{
  "hardware_sets": [
    {
      "set_number": "HW-1",
      "description": "Standard interior passage",
      "doors": ["101", "102", "103", "107", "108"],
      "finish_code": "626",
      "finish_description": "Satin Chrome (brushed silver-gray)",
      "items": [
        {
          "item": "Hinges",
          "manufacturer": "Hager",
          "model": "BB1279",
          "size": "4-1/2\" × 4-1/2\"",
          "finish": "652 (Satin Chrome)",
          "quantity": 3,
          "fire_rated": "UL 3-hour"
        },
        {
          "item": "Lockset",
          "manufacturer": "Schlage",
          "model": "ND53PD",
          "function": "Entrance",
          "finish": "626",
          "finish_visual": "Brushed silver-gray",
          "ada_compliant": true,
          "fire_rated": true
        },
        {
          "item": "Closer",
          "manufacturer": "LCN",
          "model": "4041-DEL",
          "mount": "Regular arm",
          "size": "1-4",
          "fire_rated": true,
          "ada_force": "5 lbs max"
        }
      ]
    }
  ],
  "keying": {
    "system": "Master key with construction master",
    "levels": 2,
    "groups": [
      {"group": "KA-1", "doors": ["101", "102", "103"], "description": "Office suite"},
      {"group": "KA-2", "doors": ["201", "202"], "description": "Admin"}
    ]
  },
  "rendering_summary": {
    "predominant_finish": "626 Satin Chrome",
    "mixed_finishes": false
  }
}
```

---

## STRUCTURAL STEEL SHOP DRAWINGS

### Document Identification

**Signals this is a structural steel shop drawing**:
- Steel fabricator letterhead or title block
- Piece marks (B-1, C-2, W-3, etc.)
- Member sizes (W12×26, HSS6×6×3/8, L4×4×1/4)
- Connection details with bolt patterns
- Erection plans with piece mark callouts
- Bill of materials with weights
- Approval stamps (engineer of record review)

### Piece Mark Extraction

**EXTRACT FOR EVERY PIECE MARK**:

| Data Point | Example |
|-----------|---------|
| Piece mark | "B-3" |
| Member size | "W12×26" |
| Length | "28'-6\"" |
| Steel grade | "A992 Gr. 50" |
| Weight | "742 lbs" |
| Quantity | 4 |
| Location | "Grids B-C, Bays 2-5" |
| Camber | "3/4\" (if required)" |
| Finish | "Shop prime" or "HDG" |
| Shop connections | "Shear tab welded each end" |
| Field connections | "3 - 3/4\" A325-N bolts each end" |

### Connection Details

**EXTRACT FOR EACH UNIQUE CONNECTION TYPE**:
- **Connection ID**: Reference number on shop drawing
- **Type**: Shear (simple), moment (rigid), brace
- **Bolts**: Size, grade, quantity, pattern, snug-tight or fully tensioned
- **Welds**: Type (fillet, CJP, PJP), size, length, electrode
- **Plates**: Shear tabs, gussets, stiffeners — size, thickness, grade
- **Bearing**: Beam bearing length on support
- **Cope/block**: If beam is coped, dimensions
- **Special**: Slotted holes, finger-tight, field-weld symbols

### Erection Plan Data

- **Erection sequence**: If shown (bay-by-bay, floor-by-floor)
- **Erection aids**: Temporary bracing, shoring
- **Field welding**: Locations requiring field welding vs. all-bolted
- **Anchor bolt plan**: If included (cross-reference with PEMB anchor bolts)

### Bill of Materials

If a bill of materials is provided:
- **Total tonnage**: Sum of all pieces
- **Piece count**: Total number of individual pieces
- **Heaviest piece**: Weight and mark
- **Longest piece**: Length and mark (shipping constraint)
- **Material grades**: Summary of all grades used

---

## MEP SUBMITTALS

### HVAC Equipment

**EXTRACT FOR EACH UNIT**:

| Data Point | Example |
|-----------|---------|
| Equipment tag | "RTU-1" |
| Manufacturer | "Carrier" |
| Model number | "48XC-N14090" |
| Type | "Rooftop unit" |
| Cooling capacity | "10 tons / 120 MBH" |
| Heating capacity | "150 MBH gas" |
| Airflow | "4,000 CFM" |
| Electrical | "208/3/60" |
| MCA/MOP | "MCA 45A / MOP 60A" |
| Refrigerant | "R-410A" |
| Weight | "1,850 lbs operating" |
| Dimensions | "100\" L × 44\" W × 42\" H" |
| Curb size | "96\" × 40\" (14\" high)" |
| Controls | "BACnet, factory controller" |
| Warranty | "5-yr compressor, 1-yr parts" |
| Efficiency | "SEER 14.0 / EER 11.0" |
| Sound level | "72 dBA at 5 feet" |

### Electrical Equipment

**EXTRACT FOR EACH PANEL/SWITCHBOARD**:

| Data Point | Example |
|-----------|---------|
| Equipment tag | "MDP" |
| Manufacturer | "Square D" |
| Type | "Main distribution panel" |
| Voltage | "208Y/120V, 3-phase" |
| Amperage | "400A main breaker" |
| Bus rating | "400A" |
| Enclosure | "NEMA 1 (indoor)" |
| AIC rating | "22 kAIC" |
| Spaces | "30 spaces, 42 circuits" |
| Dimensions | "60\" H × 20\" W × 6\" D" |
| Feed from | "Utility transformer" |
| Metering | "Revenue meter, CT cabinet" |

### Plumbing Fixtures [RENDERING ENHANCED]

**EXTRACT FOR EACH FIXTURE TYPE**:

| Data Point | Example |
|-----------|---------|
| Fixture tag | "WC-1" |
| Type | "Water closet" |
| Manufacturer | "Kohler" |
| Model | "K-4325" |
| Mount | "Floor mount" |
| Flush | "1.28 GPF" |
| ADA compliant | Yes — 17\" seat height |
| Supply | "1\" cold" |
| Waste | "4\" sanitary" |
| Carrier | "Josam 18000 (if wall mount)" |
| Color | "White" |
| Faucet finish | "Polished chrome" |
| Faucet style | "Single-handle, gooseneck" |
| Grab bar finish | "Satin stainless steel" |
| Soap/dispenser finish | "Satin stainless steel" |

**Plumbing fixture visual attributes**:
- **Fixture color**: "White" (standard), "Bone", "Biscuit", "Bisque", "Black"
- **Faucet finish options**: "Polished chrome" (bright, reflective), "Brushed nickel" (matte silver), "Matte black" (modern), "Oil-rubbed bronze" (aged)
- **Faucet style**: Single-handle (modern), double-handle (traditional), gooseneck (accessible), sensor (hands-free)
- **Accessory finishes**: Grab bars, towel bars, soap dispensers, paper holders
  - Common finish standards: "Satin stainless steel" (healthcare), "Bright chrome" (standard), "Matte black" (contemporary)

### Fire Protection Equipment

**EXTRACT**:
- **Sprinkler heads**: Manufacturer, model, K-factor, temperature rating, coverage area, finish
- **Fire alarm panel**: Manufacturer, model, zones, capacity
- **Standpipe**: Class, size, hose connections
- **FDC**: Location, size, type (Siamese, Storz)
- **Extinguishers**: Type, size, locations, cabinet spec

---

## FINISH MATERIAL SUBMITTALS

### Flooring [RENDERING ENHANCED]

**EXTRACT FOR EACH FLOORING PRODUCT**:

| Data Point | Example |
|-----------|---------|
| Product type | "LVT (Luxury Vinyl Tile)" |
| Manufacturer | "Armstrong" |
| Product name | "Rigid Core Pro" |
| Color/pattern name | "Warm Oak" |
| Color number | "PR-W411" |
| Size | "6\" × 48\" plank" |
| Thickness/gauge | "8 mm" |
| Wear layer | "20 mil" |
| Slip resistance (DCOF) | ">0.42 (wet areas)" |
| Fire rating | "ASTM E648 Class I" |
| Adhesive recommended | "Pressure-sensitive or click-lock" |
| Grout color (if tile) | "Mapei Keracolor U, Charcoal" |
| Transition material | "T-molding, oak-finish aluminum" |
| Spec section | "09 65 19" |
| Visual description [RENDERING] | "Warm natural oak-look plank with subtle grain" |

**Flooring visual extraction for rendering**:
- **Exact color description**: "Cool White 51911" not just "white"
- **Pattern/format**: Plank width (3\", 6\", 9\"), tile size (12\"×12\", 24\"×24\"), grout line width
- **Manufacturer's visual marketing**: Capture the aesthetic description from product brochure
- **Grout color**: For tile products — "Polyblend #381 Bright White" or specific color name/number
- **Transition materials**: Type and finish at floor changes (T-molding, reducer, threshold)
- **Surface texture**: "Embossed wood-grain", "Smooth", "Textured hand-scraped"

### Paint and Coatings [RENDERING ENHANCED]

**EXTRACT FOR EACH PRODUCT**:

| Data Point | Example |
|-----------|---------|
| Product type | "Interior latex paint" |
| Manufacturer | "Sherwin-Williams" |
| Product name | "ProMar 200 Zero VOC" |
| Color name | "Repose Gray" |
| Color code | "SW 7015" |
| Sheen | "Eggshell" |
| Coverage | "400 SF/gal" |
| VOC content | "0 g/L" |
| Number of coats | 2 |
| Substrate/application | "Drywall walls, living areas" |
| Primer required | "SW 7015 tinted primer" |
| Primer sheen | "Eggshell" |
| Spec section | "09 91 00" |
| Room locations [RENDERING] | "Bedrooms, common areas, corridors" |
| Exterior/interior | "Interior" |
| Visual appearance [RENDERING] | "Neutral warm gray, subdued, contemporary" |

**Enhanced paint color schedule extraction**:
- **Full color specification**: Manufacturer code AND name (e.g., "SW 7015 Repose Gray" not just "gray")
- **Sheen specification**: Eggshell, semi-gloss, flat, satin — each has distinct appearance
- **Substrate mapping**: Which color goes on walls vs. ceilings vs. doors vs. trim
- **Room-by-room schedule**: "Master bedrooms: SW 7015 Repose Gray eggshell", "Bathrooms: SW 7005 Pure White semi-gloss"
- **Color chip/fan deck reference**: If pages referenced, note location in submittal
- **Primer color note**: Tinted or white primer affects appearance during construction phases
- **Exterior colors**: Separate section — "Building body: SW Urbane Bronze, Trim: SW Dover White"

**Paint color visual reference table**:
- **Warm grays**: SW 7015 (Repose Gray), SW 7008 (Urbane Bronze) — appear slightly tan
- **Cool whites**: SW 7005 (Pure White), SW 7006 (Extra White) — appear slightly blue-tinted
- **Warm beiges**: SW 7032 (Warm Stone), SW 7014 (Downing Stone) — appear natural, earthy
- **Soft blues**: SW 6204 (Agreeable Gray), SW 9180 (Tricorn Black lighter) — appear calm
- **Accent colors**: Note if any high-saturation colors specified for feature walls

### Ceiling [RENDERING ENHANCED]

**EXTRACT**:

| Data Point | Example |
|-----------|---------|
| Type | "ACT (Acoustical Ceiling Tile)" |
| Manufacturer | "Armstrong" |
| Product | "Fine Fissured" |
| Model | "#1728" |
| Size | "2' × 2'" |
| Color | "White" |
| NRC | "0.75" |
| CAC | "35" |
| Light reflectance (LR) | "0.87" |
| Edge detail | "Tegular" |
| Grid system | "15/16\" exposed tee" |
| Grid color [RENDERING] | "White" |
| Fire rating | "UL Design A" |
| Mounting method | "Suspended from structure" |
| Spec section | "09 51 00" |
| Visual description [RENDERING] | "White ceiling tile with subtle random fissure texture, sits below grid creating shadow line" |

**Ceiling visual extraction for rendering**:
- **Tile product with appearance**: "Armstrong Fine Fissured #1728 — white, subtle random fissure texture"
- **Grid system color**: "Armstrong Prelude XL, White" or "Chicago Metallic 200, Silver"
- **Edge detail visual description**:
  - "Tegular edge — tile sits below grid, shadow line visible, modern appearance"
  - "Square edge — tile flush with grid, minimal shadow, seamless look"
- **Reflectance**: LR value affects brightness perception (0.87 = bright white, 0.70 = off-white)
- **Texture**: "Fine fissured" (subtle), "Rough fissured" (pronounced texture), "Smooth" (minimal texture)

---

## CASEWORK AND MILLWORK SHOP DRAWINGS [NEW SECTION - RENDERING]

### Document Identification

**Signals this is a casework/millwork submittal**:
- Cabinet manufacturer or millwork shop letterhead
- Elevation drawings of cabinet runs showing door/drawer layout
- Section details showing construction method (frame-and-panel, etc.)
- Material and finish schedules
- Hardware specifications and cut sheets
- Reference to Div 12 35 00 (Casework) or 06 41 00 (Architectural Woodwork)
- Specification callouts for edge banding, finish color, door style

### Extraction Targets

**EXTRACT FOR EACH CASEWORK ELEVATION/RUN**:

| Data Point | Example |
|-----------|---------|
| Location | "Room 107 - Nurse Station" |
| Wall location | "North wall, opposite entry" |
| Configuration | "Base + upper with countertop" |
| Overall width | "8'-0\"" |
| Base height | "34-1/2\"" |
| Upper height | "30\"" |
| Depth | "24\" standard" |
| Door style | "Flat panel (slab)" |
| Door material | "Thermofoil MDF" |
| Door color/finish | "White" |
| Drawer fronts | "Match doors - White flat panel" |
| Hardware - pull type | "Bar pull, 6\" center" |
| Hardware - finish [RENDERING] | "Brushed nickel" |
| Hardware - manufacturer | "Hafele" |
| Countertop material | "Solid surface" |
| Countertop color [RENDERING] | "Arctic White" |
| Countertop edge profile | "Eased, 1/2\" radius" |
| Backsplash material | "Solid surface" |
| Backsplash height | "4\"" |
| Backsplash color [RENDERING] | "Match countertop" |
| Interior finish | "White melamine" |
| Special features | "3 pull-out shelves, trash enclosure, glass insert upper left" |

**Casework material and finish specifications**:
- **Door material types**:
  - Thermofoil (vinyl wrap, durable, healthcare-friendly)
  - Wood veneer (natural appearance, requires sealing)
  - Painted MDF (flat finish, cleanable)
  - HPL/Formica (high-pressure laminate, stain-resistant)
- **Door color options**: "White", "Natural Maple", "Warm Gray TFL", "Natural Oak"
- **Drawer fronts**: Same material/finish as doors or specification alternative
- **Hardware pull styles**: Bar pull (6\" or 8\" center), cup pull, knob, recessed
- **Hardware finishes**: Brushed nickel, satin stainless steel, polished chrome, matte black
- **Countertop surfaces**: Solid surface (Corian), laminate (Formica), quartz, granite, stainless steel
- **Countertop edges**: Eased (smooth curve), ogee (decorative curve), beveled, square
- **Interior linings**: Melamine (white, almond, maple), veneer, painted plywood
- **Specialty items**: Lazy Susan (corner cabinets), pull-out shelves, tray dividers, trash pull-outs, spice racks

#### Casework Rendering Output Format [RENDERING]

```json
{
  "casework": [
    {
      "location": "Room 107 - Nurse Station",
      "wall": "North wall",
      "type": "Base + upper with countertop",
      "dimensions": {
        "width": "8'-0\"",
        "base_height": "34-1/2\"",
        "upper_height": "30\"",
        "depth": "24\""
      },
      "door_style": "Flat panel (slab)",
      "door_material": "Thermofoil MDF",
      "door_color": "White",
      "door_color_visual": "Bright white, matte finish, minimal texture",
      "drawer_configuration": "2 large drawers, 1 small drawer upper",
      "hardware": {
        "type": "Bar pull, 6\" center",
        "manufacturer": "Hafele",
        "model": "HF-1245",
        "finish": "Brushed nickel",
        "finish_visual": "Matte silver, warm tone"
      },
      "countertop": {
        "material": "Solid surface",
        "color": "Arctic White",
        "color_visual": "Bright white, non-porous, uniform appearance",
        "edge": "Eased, 1/2\" radius",
        "length": "8'-0\""
      },
      "backsplash": {
        "material": "Solid surface",
        "height": "4\"",
        "color": "Match countertop - Arctic White"
      },
      "interior": "White melamine",
      "special_items": ["Pull-out trash enclosure", "3 adjustable shelves"],
      "rendering_priority": true,
      "color_summary": {
        "predominant_color": "White",
        "accent_color": "Brushed nickel hardware"
      }
    }
  ]
}
```

---

## EXTERIOR PANEL AND CLADDING SUBMITTALS [NEW SECTION - RENDERING]

### Document Identification

**Signals this is an exterior panel submittal**:
- Metal building system (PEMB) shop drawings from manufacturer (Nucor, BlueScope, Chief)
- Panel manufacturer product data (MBCI, Metl-Span, VP Buildings)
- Color charts or actual color chip sheets
- Panel profile cross-section details with dimensions
- Trim detail drawings showing fascia, gutters, flashing
- Wainscot or base material specifications (if applicable)
- Wind and rain load ratings

### Extraction Targets

**WALL PANELS**:

| Data Point | Example |
|-----------|---------|
| Profile type | "PBR (Purlin Bearing Rib)" |
| Profile name [RENDERING] | "Standing seam appearance with horizontal ribs" |
| Color name [RENDERING] | "Champagne Metallic" |
| Color code | "Nucor Color Code CM" |
| Gauge | "26 ga" |
| Manufacturer | "Nucor Building Systems" |
| Panel weight | "1.8 lbs/SF" |
| Fastening | "Seam fastening, 24\" OC" |
| Wind rating | "Up to 145 mph" |
| R-value | "None (metal only)" |

**ROOF PANELS**:

| Data Point | Example |
|-----------|---------|
| Profile type | "Standing seam" |
| Profile name [RENDERING] | "Vertical ribs, concealed fastening, smooth appearance" |
| Color name [RENDERING] | "Charcoal Gray" |
| Color code | "Nucor Code CG" |
| Gauge | "26 ga" |
| Seam type | "Double-lock standing seam" |
| Insulation (if part of panel) | "Polyiso, 2\", R-13" |
| Wind rating | "Up to 160 mph" |

**TRIM AND FASCIA**:

| Data Point | Example |
|-----------|---------|
| Trim color [RENDERING] | "Dark Bronze" |
| Trim color code | "Nucor Code DB" |
| Material | "Metal" |
| Gauge | "26 ga" |
| Items included | "Fascia, soffit, rake trim, corner trim" |

**WAINSCOT/BASE (if specified)**:

| Data Point | Example |
|-----------|---------|
| Material | "Split-face CMU" |
| Color | "Warm gray" |
| Height | "4'-0\"" |
| Mortar color | "Gray" |

**GUTTERS AND DOWNSPOUTS**:

| Data Point | Example |
|-----------|---------|
| Material | "Aluminum" |
| Color [RENDERING] | "Match trim - Dark Bronze" |
| Size | "6\" gutter, 3\" downspout" |
| Fastening | "Concealed hangers, 24\" OC" |

#### Exterior Cladding Rendering Output Format [RENDERING]

```json
{
  "exterior_cladding": {
    "wall_panels": {
      "profile": "PBR (Purlin Bearing Rib)",
      "profile_visual": "Horizontal ribs, slight shadowing, industrial appearance",
      "color_name": "Champagne Metallic",
      "color_code": "CM",
      "color_visual": "Soft metallic gold-tan, warm undertone, subtle sheen",
      "manufacturer": "Nucor Building Systems",
      "gauge": "26 ga",
      "coverage": "9,980 SF building exterior"
    },
    "roof_panels": {
      "profile": "Standing seam",
      "profile_visual": "Vertical ribs, concealed fastening, smooth clean lines",
      "color_name": "Charcoal Gray",
      "color_code": "CG",
      "color_visual": "Dark warm gray, metallic finish, minimal sheen",
      "gauge": "26 ga",
      "coverage": "Entire roof"
    },
    "trim_fascia": {
      "color_name": "Dark Bronze",
      "color_code": "DB",
      "color_visual": "Rich dark brown, metallic, matches roof panel darkness",
      "items": ["Fascia", "Soffit", "Rake trim", "Corner trim"]
    },
    "wainscot": {
      "material": "Split-face CMU",
      "color": "Warm gray",
      "color_visual": "Natural concrete gray with textured face",
      "height": "4'-0\"",
      "location": "Base of building at entry areas"
    },
    "gutters_downspouts": {
      "material": "Aluminum",
      "color": "Match trim - Dark Bronze",
      "size": "6\" gutter, 3\" downspout"
    },
    "overall_rendering_summary": {
      "exterior_color_scheme": "Champagne Metallic walls, Charcoal Gray roof, Dark Bronze trim",
      "visual_impression": "Modern, cohesive, warm metallic palette with dark accents",
      "dominant_color": "Champagne Metallic (75% of visible area)"
    }
  }
}
```

---

## LIGHTING FIXTURE SUBMITTALS [NEW SECTION - RENDERING]

### Document Identification

**Signals this is a lighting fixture submittal**:
- Lighting manufacturer cut sheets (Lithonia, Acuity, Cooper, Philips, Sylvania, etc.)
- Fixture type cross-reference schedule matching fixture marks (A, B, C, etc.) to electrical plans
- Photometric data and IES files (technical performance data)
- Physical dimensions and mounting details
- Color temperature and CRI specifications
- Fixture appearance photos or detailed drawings

### Extraction Targets

**EXTRACT FOR EACH FIXTURE TYPE**:

| Data Point | Example |
|-----------|---------|
| Fixture type mark | "A" |
| Fixture description [RENDERING] | "2x2 LED Flat Panel Troffer" |
| Manufacturer | "Lithonia Lighting" |
| Model number | "CPX 2x2 ALO7" |
| Housing material [RENDERING] | "Steel" |
| Housing color [RENDERING] | "White" |
| Lens/diffuser type [RENDERING] | "Flat frosted acrylic" |
| Lens/diffuser appearance [RENDERING] | "Smooth frosted surface, soft light diffusion" |
| Mounting type | "Recessed in ACT grid" |
| Trim ring color [RENDERING] | "White" |
| Lamp type | "LED integrated" |
| Wattage | "32W" |
| Lumen output | "3,600 lm" |
| Color temperature | "4000K (neutral white)" |
| CRI (Color Rendering) | "90+" |
| Voltage | "120/277V" |
| Dimmable | "0-10V" |
| Quantity on project | "42 fixtures" |

**SPECIFIC FIXTURE TYPES - EXTRACTION DETAILS**:

**Recessed Fixtures**:
- Trim ring finish (white, brushed nickel, black, bronze)
- Baffle color (white, black, mirror)
- Aperture size (4\", 6\", 8\")
- Trim ring depth (shallow, standard, deep)

**Pendant/Decorative Fixtures**:
- Shade/bowl material and color
- Suspension type (cord, chain, rod, track)
- Suspension finish
- Overall appearance photo
- Shade opacity (transparent, translucent, opaque)

**Linear Strip Fixtures**:
- Length (2', 4', custom)
- Width (narrow, standard, wide)
- Surface mount color
- Lens/diffuser appearance

**Wall Sconces**:
- Backplate finish and color
- Shade material and color
- Overall dimensions
- Appearance (traditional, contemporary, minimalist)

**Exterior Fixtures**:
- Wall pack appearance (sealed housing)
- Color and finish
- Bollard or pole light style
- Mounting height

**Emergency/Exit Fixtures**:
- Exit sign style (traditional block letters or modern design)
- Sign color (red lettering, green lettering)
- Housing color (white, black, stainless)
- Mounting (wall, ceiling)

#### Lighting Fixture Rendering Output Format [RENDERING]

```json
{
  "lighting_fixtures": [
    {
      "type_mark": "A",
      "description": "2x2 LED Flat Panel Troffer",
      "appearance_summary": "Flush white 2x2 panel, even diffused light, minimal profile, modern appearance",
      "manufacturer": "Lithonia Lighting",
      "model": "CPX 2x2 ALO7",
      "housing_color": "White",
      "housing_material": "Steel",
      "lens_diffuser": "Flat frosted acrylic",
      "lens_appearance": "Smooth frosted, soft light spread, bright white appearance",
      "trim_ring_color": "White",
      "mounting": "Recessed in 2x2 ACT grid",
      "lamp_type": "LED integrated",
      "color_temperature": "4000K (neutral white)",
      "lumen_output": "3,600 lm",
      "quantity": 42,
      "rendering_appearance": "Clean white recessed panel, subtle square outline in ceiling plane"
    },
    {
      "type_mark": "B",
      "description": "6-inch LED Downlight Recessed",
      "appearance_summary": "Compact round recessed fixture with black trim, tight beam pattern",
      "manufacturer": "Acuity Brands",
      "model": "ARL-6",
      "housing_color": "Black",
      "baffle_color": "Black",
      "aperture": "6\"",
      "trim_ring_finish": "Matte black",
      "mounting": "Recessed in drywall",
      "color_temperature": "3000K (warm white)",
      "lumen_output": "700 lm",
      "quantity": 18,
      "rendering_appearance": "Small round dark spot on ceiling, warm-toned light output"
    },
    {
      "type_mark": "C",
      "description": "Linear LED Strip - Undercabinet",
      "appearance_summary": "Thin linear light source under cabinetry, white plastic housing",
      "manufacturer": "Philips Hue",
      "model": "LCL102",
      "housing_color": "White",
      "housing_width": "1.5\" wide, ultra-thin profile",
      "mounting": "Under-cabinet surface mount",
      "color_temperature": "4000K",
      "lumen_output": "600 lm per 4 feet",
      "quantity": 8,
      "location": "Kitchen undercabinet lighting",
      "rendering_appearance": "Subtle light strip under cabinet, creates accent light on countertop"
    }
  ],
  "lighting_rendering_summary": {
    "predominant_fixture_type": "Recessed 2x2 LED panels",
    "color_temperature_standard": "4000K (neutral white)",
    "overall_lighting_style": "Modern, LED-based, clean recessed appearance",
    "visual_impact": "Even, bright ceiling illumination with minimal fixture visibility"
  }
}
```

---

## WINDOW AND GLAZING SUBMITTALS [NEW SECTION - RENDERING]

### Document Identification

**Signals this is a window/glazing submittal**:
- Window manufacturer specification sheets (Andersen, Pella, Traco, Schüco, etc.)
- Glazing product data sheets (glass type, coatings, spacer type)
- Detailed drawings showing frame/mullion profiles
- Color and finish charts
- Hardware specification sheets (locks, operators, handles)
- Performance data (U-factor, SHGC, air leakage)

### Extraction Targets

**WINDOW FRAMES**:

| Data Point | Example |
|-----------|---------|
| Frame material | "Aluminum" |
| Frame finish [RENDERING] | "Dark bronze anodized" |
| Anodize type | "Class I (high-durability)" |
| Mullion width (sightline) [RENDERING] | "2.5\" (narrow modern profile)" |
| Mullion color [RENDERING] | "Matches frame - Dark bronze" |
| Sill finish [RENDERING] | "Sloped, dark bronze" |

**GLAZING (GLASS)**:

| Data Point | Example |
|-----------|---------|
| Glass type | "Low-E insulating unit" |
| Outer pane appearance [RENDERING] | "Clear" |
| Inner pane appearance [RENDERING] | "Clear" |
| Tint [RENDERING] | "None (clear glass)" |
| Coating [RENDERING] | "Low-E coating on inner surface (clear, not reflective)" |
| Spacer bar [RENDERING] | "Black warm-edge spacer visible at perimeter" |
| Spacer visual [RENDERING] | "Thin dark line at glass edge, modern appearance" |
| U-factor | "0.28 (high efficiency)" |
| SHGC | "0.23 (solar control)" |
| VT (Visible Transmittance) | "0.65" |

**HARDWARE**:

| Data Point | Example |
|-----------|---------|
| Lock handle finish [RENDERING] | "Brushed silver" |
| Lock handle style | "Contemporary lever" |
| Operator type | "Casement crank" |
| Operator finish [RENDERING] | "Brushed nickel" |

#### Window and Glazing Rendering Output Format [RENDERING]

```json
{
  "windows_glazing": {
    "frame_system": {
      "material": "Aluminum",
      "finish": "Dark bronze anodized",
      "finish_visual": "Rich dark brown-black, subtle metallic sheen, warm tone",
      "anodize_durability": "Class I (5-10 year warranty)"
    },
    "mullion_profile": {
      "width": "2.5\" (sightline)",
      "profile_style": "Modern narrow profile, minimal visual interruption",
      "color": "Dark bronze (matches frame)",
      "visual_impact": "Fine lines dividing glass, dark color recedes behind glass"
    },
    "glazing": {
      "type": "Low-E insulating unit",
      "outer_pane": "Clear",
      "inner_pane": "Clear",
      "tint": "None (clear)",
      "coating": "Low-E (transparent, slight blue-gray tint when viewed at angle)",
      "spacer": {
        "type": "Black warm-edge spacer",
        "appearance": "Thin black line visible around glass perimeter",
        "visual_effect": "Modern appearance, hidden edge vs traditional aluminum spacer"
      }
    },
    "overall_rendering_appearance": "Clear glass windows with dark bronze frames and mullions, modern appearance, black spacer bars visible at edges, high visibility",
    "rendering_priority": true
  }
}
```

---

## SPEC COMPLIANCE VERIFICATION

When extracting submittal data, always cross-reference against the project specifications:

### Compliance Checklist

For each submittal, verify:
- [ ] Manufacturer is listed as acceptable in spec section
- [ ] Product meets or exceeds specified performance criteria
- [ ] Fire rating matches spec requirement
- [ ] ADA compliance confirmed where required
- [ ] Color/finish matches spec or approved selection
- [ ] Warranty meets or exceeds spec duration
- [ ] Required certifications/test reports included
- [ ] Installation instructions included (if required by spec)
- [ ] Substitution request filed (if different from spec basis-of-design)

### Common Submittal Deficiencies

Flag these during extraction:
- **Missing test reports**: Product data without ASTM test documentation
- **Wrong spec section**: Submittal references incorrect CSI section
- **Incomplete data**: Cut sheet doesn't show all required performance data
- **Substitution without request**: Product differs from spec basis-of-design without formal substitution
- **Expired certifications**: Test reports or listings past expiration
- **Missing fire rating**: Fire-rated assembly without UL listing documentation
- **Missing ADA documentation**: Accessible product without compliance certification
- **[RENDERING] Color mismatch**: Submitted finish color differs from approved rendering color selection

---

## OUTPUT STRUCTURE

Structure all submittal extractions for project-data storage:

```json
{
  "submittals_extracted": {
    "document": {
      "filename": "03300-1_Concrete_Mix_Designs.pdf",
      "type": "submittal_package",
      "category": "concrete_mix_design",
      "spec_section": "03 30 00",
      "submittal_number": "03300-1",
      "submitted_by": "Wells Concrete",
      "date_received": "2026-01-15"
    },
    "extracted_data": { },
    "spec_compliance": {
      "compliant": true,
      "deficiencies": [],
      "notes": "All mixes meet or exceed spec requirements"
    },
    "coverage": {
      "populated": ["mix_id", "strength", "wc_ratio", "slump", "air", "materials"],
      "missing": ["trial_batch_results"],
      "low_confidence": []
    }
  },
  "visual_rendering_data": {
    "exterior": {
      "wall_color": "Champagne Metallic metal panels, warm gold-tan",
      "roof_color": "Charcoal Gray standing seam, dark warm gray",
      "trim_color": "Dark Bronze, rich dark brown",
      "base_material": "Split-face CMU, warm gray, 4'-0\" height",
      "window_frames": "Dark bronze anodized aluminum, modern narrow mullion",
      "window_glass": "Clear with low-E, black warm-edge spacer visible",
      "entry_doors": "Aluminum storefront, dark bronze frames",
      "wall_area_coverage": "9,980 SF"
    },
    "interior": {
      "predominant_wall_color": "SW 7015 Repose Gray, eggshell finish",
      "secondary_wall_colors": ["SW 7005 Pure White (bathrooms)", "SW 7032 Warm Stone (common areas)"],
      "predominant_floor": "Armstrong LVT, Warm Oak plank, 6\" × 48\", subtle grain texture",
      "floor_grout": "Not applicable (LVT flooring)",
      "ceiling": "Armstrong Fine Fissured #1728, white ACT 2x2 grid, tegular edge",
      "ceiling_appearance": "Subtle random fissure texture, sits below grid creating shadow line",
      "casework": "White thermofoil flat panel cabinets, brushed nickel bar pulls (6\" center)",
      "countertops": "White solid surface, eased edge, 8'-0\" length at nurse station",
      "backsplash": "Match countertop - white solid surface, 4\" height",
      "hardware_finish": "626 Satin Chrome (brushed silver-gray) — predominant on passage doors",
      "lighting_style": "Recessed 2x2 LED flat panels (type A) + 6\" LED downlights (type B), 4000K neutral white",
      "lighting_appearance": "Modern, clean, flush ceiling fixtures, minimal visual profile",
      "plumbing_fixtures": "White porcelain, polished chrome faucets, single-handle gooseneck style",
      "grab_bar_finish": "Satin stainless steel, contemporary matte silver",
      "accessible_entry": "Aluminum storefront, glass doors, dark bronze frames",
      "overall_interior_aesthetic": "Modern healthcare, clean lines, neutral warm color palette, healthcare-grade finishes",
      "key_rendering_colors": ["SW 7015 Repose Gray (walls)", "White (casework, fixtures)", "Brushed nickel (hardware)", "4000K LED lighting"]
    }
  }
}
```

---

## INTEGRATION WITH RENDERING SYSTEM

### Why Submittals Are Critical for Accurate Rendering

Submittal documents provide the most authoritative visual and material data because they contain:

1. **Actual products being installed** — not design intent or basis-of-design approximations
2. **Manufacturer images and colors** — exact appearance from product photography
3. **Color codes and finishes** — precise visual specifications (e.g., "626 Satin Chrome" not just "chrome")
4. **Texture and material details** — surface finish, sheen, pattern information
5. **Dimensions and proportions** — accurate size for modeling (ceiling heights, cabinet widths, etc.)
6. **Material alternatives** — approved substitutions that may differ from original design

### How Extracted Submittal Data Improves Rendering Quality

- **Exterior cladding**: Metal panel colors and profiles directly influence building appearance perception
- **Window frames and glazing**: Frame finish and mullion width dramatically affect facade appearance
- **Interior finishes**: Paint colors, flooring patterns, ceiling texture create spatial atmosphere
- **Casework and built-ins**: Cabinet colors, hardware finishes, countertop materials determine room character
- **Lighting fixtures**: Fixture type, color temperature, and mounting method affect interior brightness perception
- **Hardware finishes**: Door locks, hinges, pulls appear repeatedly throughout building and unify aesthetic
- **Plumbing fixtures and accessories**: Color and finish of bathroom/kitchen fixtures affect cleanliness perception (important in healthcare)

### Data Flow: Submittals → Project Database → Rendering Engine

1. **Extraction phase**: Extract visual attributes from submittals (colors, finishes, materials, dimensions)
2. **Storage phase**: Store data in `visual_rendering_data` JSON structure with exact color names/codes
3. **Rendering phase**: Rendering engine queries project database for visual data
4. **Application phase**: Rendering engine applies extracted colors, materials, textures to 3D model
5. **Quality check**: Compare rendered output to submittal images and actual product samples

### Accuracy Advantages Over Design Documents

- **Design documents** may show approximate colors; submittals show actual product
- **Design documents** may specify "white" casework; submittals specify exact finish (thermofoil, flat panel, white)
- **Design documents** may show generic fixtures; submittals specify exact model with appearance photos
- **Submittals** capture approved substitutions that design documents don't reflect

---

## Notes

- Submittals may arrive as compiled packages (multiple products in one PDF) or individual product data sheets. Handle both formats.
- Some submittals require resubmission after "Revise and Resubmit" action. Track revision numbers and dates.
- Shop drawings (structural steel, miscellaneous metals, HVAC ductwork, casework) require engineer-of-record or architect review stamps. Note stamp status during extraction.
- For healthcare/senior care projects, pay special attention to: antimicrobial finishes, cleanability ratings, grab bar load ratings, nurse call compatibility, infection control compliance, and ADA accessibility requirements.
- [RENDERING] tagged sections are specifically prioritized for rendering system integration and should be extracted with high completeness.
- Color and finish data is time-sensitive — if submittal includes physical samples or color chips, note approval dates and cross-reference with approved color selection documentation.
- When multiple hardware finishes or paint colors appear on project, always extract "predominant" finish for rendering defaults while noting all variations for specification accuracy.
