# PEMB (Pre-Engineered Metal Building) - Deep Extraction Guide

Extract comprehensive, field-actionable data from PEMB design documents, reaction drawings, erection manuals, and accessory details. PEMB documents come from the building manufacturer (Nucor, BlueScope, Metallic Building Co., VP Buildings, etc.) and contain critical information that differs significantly from conventional construction drawings.

---

## Extraction Priority Matrix

| Priority | Data Type | Use Case | Completeness Target |
|----------|-----------|----------|-------------------|
| **CRITICAL** | Column reactions (vertical, horizontal, moment) | Foundation design verification, anchor bolt checks | 100% by grid |
| **CRITICAL** | Anchor bolt layout (size, embedment, projection, template) | Foundation placement, bolt setting QC | 100% every column |
| **CRITICAL** | Building envelope (width, length, eave, ridge, slope) | Overall building verification | 100% |
| **HIGH** | Primary framing (rafter type, column type, moment frames) | Erection sequencing, crane planning | 100% |
| **HIGH** | Erection sequence and bracing requirements | Safety, erection planning | 100% |
| **HIGH** | Connection details (moment, pinned, base plate) | Field bolt-up, torque requirements | 100% for unique types |
| **HIGH** | Secondary framing (purlins, girts, spacing, gauge) | Material verification, installation QC | 100% |
| **MEDIUM** | Accessories (gutters, downspouts, trim, louvers) | Procurement, installation tracking | 100% if present |
| **MEDIUM** | Panel and insulation systems | Enclosure tracking, thermal verification | 100% if present |
| **LOW** | Shipping and piece mark lists | Delivery verification | Extract if provided |

---

## BUILDING ENVELOPE

### Overall Dimensions

**ALWAYS EXTRACT**:
- **Width**: Clear span or multi-span (e.g., "80'-0\" clear span")
- **Length**: Total building length and bay count
- **Bay spacing**: Each bay dimension (e.g., "5 bays @ 25'-0\" = 125'-0\"")
- **Eave height**: Height to underside of rafter at column line (e.g., "20'-0\" eave")
- **Roof slope**: Pitch (e.g., "1:12", "0.5:12", "1/4\" per foot")
- **Ridge height**: Calculated or stated peak height
- **Endwall type**: Each endwall — post-and-beam, rigid frame, bearing frame, or open
- **Sidewall type**: Each sidewall — rigid frame, bearing, lean-to connection

**Output format**:
```json
{
  "building_envelope": {
    "width": "80'-0\" clear span",
    "length": "125'-0\" (5 bays @ 25'-0\")",
    "eave_height": "20'-0\"",
    "roof_slope": "1:12",
    "ridge_height": "23'-4\"",
    "bays": [
      {"bay": 1, "width": "25'-0\"", "from_grid": "1", "to_grid": "2"},
      {"bay": 2, "width": "25'-0\"", "from_grid": "2", "to_grid": "3"},
      {"bay": 3, "width": "25'-0\"", "from_grid": "3", "to_grid": "4"},
      {"bay": 4, "width": "25'-0\"", "from_grid": "4", "to_grid": "5"},
      {"bay": 5, "width": "25'-0\"", "from_grid": "5", "to_grid": "6"}
    ],
    "endwall_left": "Post-and-beam (Grid 1)",
    "endwall_right": "Post-and-beam (Grid 6)",
    "sidewall_left": "Rigid frame (Grid A)",
    "sidewall_right": "Rigid frame (Grid H)"
  }
}
```

### Building Extensions and Appendages

- **Canopies**: Width, projection, height, location (grid reference)
- **Lean-tos**: Width, eave height, connection type, location
- **Mezzanines**: Bay locations, clear height above/below, load capacity (PSF)
- **Fascia/parapet**: Height above eave, locations

---

## COLUMN REACTIONS

### Reaction Drawing Extraction

PEMB reaction drawings are the most critical document for foundation design. They provide the loads that the building structure delivers to the foundation at each column location.

**EXTRACT FOR EVERY COLUMN**:

| Data Point | Unit | Example |
|-----------|------|---------|
| Grid location | Grid ID | "Grid A-3" |
| Column type | Description | "Rigid frame interior" |
| Vertical reaction (gravity, max) | kips | "45.2 kips down" |
| Vertical reaction (uplift, min) | kips | "12.8 kips up" |
| Horizontal reaction (at base) | kips | "8.5 kips" |
| Moment at base | ft-kips | "0 (pinned)" or "35.2 ft-kips" |
| Wind uplift (MWFRS) | kips | "18.3 kips up" |
| Seismic shear (if applicable) | kips | "6.2 kips" |
| Collateral load included | PSF | "5 PSF" |
| Live load | PSF | "20 PSF roof" |

**Load combinations to look for**:
- Dead + Live (gravity)
- Dead + Wind (uplift critical)
- Dead + Snow (if applicable)
- Dead + Seismic (if in seismic zone)
- ASD vs. LRFD (note which basis)

**Output format**:
```json
{
  "column_reactions": [
    {
      "grid": "A-1",
      "column_type": "Endwall corner",
      "vertical_down_max": "12.5 kips",
      "vertical_up_max": "6.2 kips",
      "horizontal": "3.1 kips",
      "moment": "0 (pinned)",
      "load_basis": "ASD",
      "notes": "Endwall post, non-moment frame"
    },
    {
      "grid": "A-3",
      "column_type": "Rigid frame exterior",
      "vertical_down_max": "45.2 kips",
      "vertical_up_max": "12.8 kips",
      "horizontal": "8.5 kips",
      "moment": "0 (pinned base)",
      "load_basis": "ASD",
      "notes": "Sidewall rigid frame column"
    }
  ],
  "design_loads": {
    "roof_live": "20 PSF",
    "collateral": "5 PSF",
    "wind_speed": "115 mph (ASCE 7-22)",
    "exposure": "C",
    "snow": "15 PSF ground",
    "seismic": "SDS = 0.15, SD1 = 0.08"
  }
}
```

### Reaction Summary Table

Many PEMB manufacturers provide a tabular reaction summary. If present, extract the entire table:
- All column grid locations
- All load cases (gravity, wind left, wind right, wind end, seismic)
- Maximum and minimum values per column
- Design code reference (IBC, ASCE 7 edition)

---

## PRIMARY FRAMING

### Rigid Frames

**EXTRACT**:
- **Frame type**: Clear span, multi-span, single slope, lean-to
- **Frame locations**: Which grid lines are rigid frames (e.g., "Grids 2, 3, 4, 5")
- **Rafter profile**: Tapered, straight, built-up depth range (e.g., "24\" at knee, 12\" at ridge")
- **Column profile**: Tapered or straight, depth range (e.g., "12\" at base, 24\" at knee")
- **Flange/web thickness**: If specified (e.g., "3/8\" web, 5/8\" flange")
- **Steel grade**: ASTM A572 Gr. 50 (typical for PEMB)
- **Splice locations**: Number and approximate location of field splices per frame
- **Knee connection**: Bolted moment connection details
- **Base connection**: Pinned or fixed, number of anchor bolts

### Endwall Framing

**EXTRACT**:
- **Endwall columns**: Post-and-beam posts at each grid intersection
- **Endwall rafters**: Typically lighter than interior rigid frames
- **Endwall headers**: Over openings (doors, windows)
- **Endwall bracing**: X-bracing, portal frame, or wind column
- **Wind columns**: If separate from building columns (location, size)

### Bracing

**EXTRACT ALL BRACING LOCATIONS AND TYPES**:
- **Roof bracing**: X-bracing bays, location (typically end bays)
- **Sidewall bracing**: X-bracing, portal frame, or wind bent locations
- **Endwall bracing**: Type and location
- **Flange bracing**: Purlin-to-rafter or girt-to-column connections
- **Temporary erection bracing**: If specified in erection manual

**Output format**:
```json
{
  "bracing": {
    "roof_bracing": [
      {"bays": "1-2", "type": "X-brace rod", "size": "3/4\" dia rod"},
      {"bays": "5-6", "type": "X-brace rod", "size": "3/4\" dia rod"}
    ],
    "sidewall_bracing": [
      {"bay": "1-2", "side": "A", "type": "X-brace rod"},
      {"bay": "5-6", "side": "A", "type": "X-brace rod"},
      {"bay": "1-2", "side": "H", "type": "Portal frame"},
      {"bay": "5-6", "side": "H", "type": "Portal frame"}
    ],
    "endwall_bracing": [
      {"grid": "1", "type": "X-brace", "between": "D-E"},
      {"grid": "6", "type": "X-brace", "between": "D-E"}
    ]
  }
}
```

---

## SECONDARY FRAMING

### Purlins (Roof)

**EXTRACT**:
- **Type**: C-section, Z-section (most common in PEMB)
- **Size designation**: e.g., "10Z2.5" (10\" deep Z, 2.5\" flange)
- **Gauge**: e.g., "14 ga" (0.075\")
- **Spacing**: Varies by zone — extract all zones:
  - Standard spacing (e.g., "5'-0\" o.c.")
  - Reduced spacing at eave (e.g., "3'-6\" o.c. first 2 purlins")
  - Reduced spacing at ridge (if any)
- **Lap lengths**: At supports (e.g., "4'-0\" lap over interior supports")
- **Sag rods/angles**: Rows of sag rods, spacing between rows
- **Peak channel/closure**: Type and size at ridge

### Girts (Wall)

**EXTRACT**:
- **Type**: C-section, Z-section
- **Size designation**: e.g., "8Z2.25"
- **Gauge**: e.g., "16 ga"
- **Spacing**: Standard and reduced near base/eave:
  - Standard (e.g., "5'-6\" o.c.")
  - First girt height from floor (e.g., "6\" above base angle")
  - Reduced spacing zones
- **Base angle**: Size, attachment method
- **Eave strut**: Size, connection to rafter/column

### Endwall Girts and Purlins

- **Endwall girts**: Often different from sidewall girts (lighter, different spacing)
- **Endwall purlins**: May match interior or be lighter

---

## ANCHOR BOLT LAYOUT

### Per-Column Anchor Bolt Details

**EXTRACT FOR EVERY COLUMN BASE**:

| Data Point | Example |
|-----------|---------|
| Grid location | "A-3" |
| Number of bolts | 4 |
| Bolt diameter | 3/4\" |
| Bolt length (embedment) | 24\" |
| Bolt projection above concrete | 4\" |
| Bolt circle or pattern | 2-bolt inline, 4-bolt square, 6-bolt rectangle |
| Bolt spacing (along frame) | 8\" |
| Bolt spacing (across frame) | 5\" |
| Edge distance (min) | 4\" |
| Base plate size | 12\" × 10\" × 3/4\" |
| Grout thickness | 1\" (typical) |
| Bolt grade | ASTM F1554 Gr. 36 (or 55, 105) |
| Nut and washer | Heavy hex, hardened washer |
| Template required? | Yes/No |
| Template dimensions | If different from bolt pattern |
| Leveling nut required? | Yes/No |

**CRITICAL QC NOTES**:
- Anchor bolt placement tolerance: typically ±1/8\" for PEMB
- Bolt projection must allow for grout pad + base plate + leveling nut + top nut
- Template dimensions must be verified against the actual base plate

**Output format**:
```json
{
  "anchor_bolts": [
    {
      "grid": "A-3",
      "quantity": 4,
      "diameter": "3/4\"",
      "grade": "F1554 Gr. 36",
      "embedment": "24\"",
      "projection": "4\"",
      "pattern": "4-bolt rectangle",
      "spacing_along": "8\"",
      "spacing_across": "5\"",
      "edge_distance_min": "4\"",
      "base_plate": "12\" × 10\" × 3/4\"",
      "leveling_nuts": true,
      "template_dims": "14\" × 12\""
    }
  ],
  "placement_tolerance": "±1/8\"",
  "grout_thickness": "1\" non-shrink grout"
}
```

---

## ERECTION SEQUENCE

### Manufacturer's Erection Manual

If an erection manual or erection plan is provided, extract:

**Sequence Steps**:
1. **Mobilization**: Crane requirements (type, capacity, reach)
2. **Column erection order**: Which columns first, temporary bracing requirements
3. **Rafter/beam erection**: Order, connection sequence, safety cables
4. **Bracing installation**: When bracing must be installed relative to framing
5. **Secondary framing**: Purlins and girts after primary is braced
6. **Sheeting/panels**: Panel installation direction and sequence
7. **Trim and accessories**: After panels

**CRITICAL SAFETY ITEMS**:
- **Minimum bracing before releasing crane**: Number of bays that must be braced
- **Safety cable requirements**: When and where required
- **Temporary shoring**: Any temporary supports during erection
- **Wind speed limits**: Maximum wind for erection operations (typically 25-30 mph)
- **Fall protection**: Tie-off points, safety requirements during erection
- **Column plumb tolerance**: Typically H/500 for PEMB columns

**Crane Requirements**:
- **Type**: Crawler, RT, truck crane
- **Minimum capacity**: Tons at maximum radius needed
- **Maximum reach**: For furthest pick from crane position
- **Heaviest pick**: Weight of heaviest single piece
- **Crane pad requirements**: Ground bearing pressure, size, location
- **Multiple crane lifts**: If tandem lifts are required

**Output format**:
```json
{
  "erection_sequence": {
    "crane": {
      "type": "RT crane",
      "min_capacity": "40 ton",
      "max_reach": "60'-0\"",
      "heaviest_pick": "4,200 lbs (interior rigid frame)",
      "crane_pad": "20' × 20', 3000 PSF bearing"
    },
    "sequence": [
      {"step": 1, "description": "Set columns at Grid 3 (center bay)", "bracing": "Temporary guy cables"},
      {"step": 2, "description": "Set rafter at Grid 3", "bracing": "Pin at knee, bolt at ridge"},
      {"step": 3, "description": "Set columns/rafter at Grid 4", "bracing": "X-bracing bay 3-4"},
      {"step": 4, "description": "Install purlins bay 3-4", "bracing": "Flange braces to purlins"},
      {"step": 5, "description": "Proceed outward to Grids 2 and 5", "bracing": "Continue bracing pattern"},
      {"step": 6, "description": "Set endwall framing Grids 1 and 6", "bracing": "Endwall bracing"},
      {"step": 7, "description": "Complete secondary framing (girts, eave struts)", "bracing": "Full system"},
      {"step": 8, "description": "Install roof panels (start ridge, work to eave)", "bracing": "Diaphragm develops"},
      {"step": 9, "description": "Install wall panels (top to bottom)", "bracing": "Remove temp bracing after panels"},
      {"step": 10, "description": "Trim, gutters, downspouts", "bracing": "N/A"}
    ],
    "safety": {
      "min_braced_bays_before_crane_release": 2,
      "safety_cables": "Required on all purlins until roof panels installed",
      "wind_limit": "25 mph sustained, 35 mph gusts — stop erection",
      "fall_protection": "100% tie-off above 6', retractable lanyards on columns",
      "column_plumb_tolerance": "H/500"
    }
  }
}
```

---

## CONNECTION DETAILS

### Moment Connections (Knee)

- **Connection type**: Bolted end-plate, bolted flange plate
- **Bolt size and grade**: e.g., "3/4\" A325-N" or "7/8\" A325-SC"
- **Bolt count**: Number per flange, number per web
- **Torque requirement**: Per AISC or manufacturer specification
- **End plate thickness**: If end-plate connection
- **Stiffener requirements**: At knee or splice
- **Snug-tight vs. fully tensioned**: Verify requirement

### Ridge Connections

- **Connection type**: Bolted splice plate, bolted end-plate
- **Bolt pattern**: Quantity, size, arrangement
- **Splice plate thickness**: If splice connection
- **Erection bolts vs. final bolts**: Temporary connection during erection?

### Base Plate Connections

- **Connection type**: Pinned (typical) or moment (fixed base)
- **Base plate dimensions**: Width × length × thickness
- **Weld or bolt to column**: Shop-welded base plate (typical)
- **Grout**: Non-shrink grout thickness and type
- **Leveling method**: Leveling nuts, shims, or wedges

### Bolting Requirements Summary

**EXTRACT BOLT TORQUE TABLE IF PROVIDED**:

| Bolt Size | Grade | Snug | Full Tension (Turn-of-Nut) | Full Tension (TC Bolt) |
|----------|-------|------|---------------------------|----------------------|
| 3/4\" | A325 | Snug tight | 1/3 turn past snug | Use TC indicator |
| 7/8\" | A325 | Snug tight | 1/3 turn past snug | Use TC indicator |

---

## WALL AND ROOF PANELS

### Roof Panels

**EXTRACT**:
- **Panel type**: Standing seam, through-fastened, concealed clip
- **Profile**: Manufacturer and profile name (e.g., "Nucor NuRib", "Butler MR-24")
- **Gauge**: e.g., "26 ga Galvalume"
- **Coverage width**: Net coverage per panel (e.g., "36\" cover")
- **Panel color**: Finish color code/name
- **Fastening**: Clip type, spacing, screw pattern
- **Thermal spacer blocks**: Between purlins and panels (if insulated)

### Wall Panels

**EXTRACT**:
- **Panel type**: Through-fastened, concealed fastener, insulated metal panel (IMP)
- **Profile**: Manufacturer and name
- **Gauge**: e.g., "26 ga"
- **Coverage width**: Net coverage
- **Panel color**: Exterior and interior (if different)
- **Fastening**: Screw pattern, type, spacing
- **Liner panel**: If double-skin system — liner gauge, profile, color
- **Wainscot**: If different panel at base — height, type, color

### Insulation System

**EXTRACT**:
- **Roof insulation**: Type (fiberglass, rigid board), R-value, thickness, facing
- **Wall insulation**: Type, R-value, thickness, facing
- **Vapor barrier**: Type, location (warm side), perm rating
- **Thermal breaks/spacer blocks**: Size, material, locations
- **Condensation gutter**: If required, location

**Output format**:
```json
{
  "panel_system": {
    "roof": {
      "type": "Standing seam",
      "profile": "NuRib SSR",
      "gauge": "26 ga Galvalume",
      "color": "Polar White",
      "coverage": "24\" net",
      "insulation": "R-25 fiberglass batt (8\" thick), faced"
    },
    "wall": {
      "type": "Through-fastened",
      "profile": "PBR panel",
      "gauge": "26 ga",
      "color": "Burnished Slate",
      "coverage": "36\" net",
      "insulation": "R-13 fiberglass batt (3.5\" thick), faced",
      "liner": "26 ga flat liner, White"
    },
    "wainscot": {
      "type": "PBR panel",
      "gauge": "26 ga",
      "color": "Charcoal Gray",
      "height": "4'-0\" from base"
    }
  }
}
```

---

## ACCESSORIES

### Gutters and Downspouts

- **Gutter type**: Box, half-round, eave
- **Gutter size**: Width and depth (e.g., "6\" × 4\" box gutter")
- **Gutter material/gauge**: e.g., "24 ga Galvalume"
- **Gutter color**: Match roof or wall?
- **Downspout size**: e.g., "4\" × 3\" rectangular"
- **Downspout locations**: Grid references or spacing (e.g., "one per bay, Grid A side")
- **Downspout material/gauge**: e.g., "26 ga"

### Trim

- **Ridge cap**: Profile, color, gauge
- **Eave trim**: Type, color
- **Rake trim**: Type, color
- **Corner trim**: Inside/outside, color
- **Base trim/angle**: Size, attachment
- **Door/window trim**: Jamb and head trim profiles

### Openings

**EXTRACT ALL BUILDING OPENINGS**:

| Data Point | Example |
|-----------|---------|
| Opening type | Overhead door, walk door, window, louver |
| Size | 12'-0\" × 14'-0\" |
| Location | Grid A, Bay 2-3 |
| Header/jamb framing | Hot-rolled W or cold-formed header |
| Sill height | 0\" (floor level) or elevated |
| Door manufacturer/model | If specified by PEMB supplier |
| Hardware | Locks, closers, panic hardware |
| Fire rating | If required |
| Wind load | For overhead doors |

### Ventilation

- **Ridge vents**: Type (continuous, individual), size, length, NFA
- **Louvers**: Size, location, NFA (net free area)
- **Exhaust fans**: Size, location, curb requirements
- **Gravity ventilators**: Type, throat size, location

---

## PIECE MARKS AND SHIPPING

### Piece Mark System

PEMB manufacturers assign unique piece marks to every shipped component. If a piece mark list or shipping list is provided:

- **Primary framing**: RF-1, RF-2 (rigid frame columns/rafters by grid)
- **Secondary**: P-1, P-2 (purlins), G-1, G-2 (girts)
- **Bracing**: BR-1, XB-1 (bracing rods/angles)
- **Accessories**: T-1 (trim), DS-1 (downspout), etc.

### Delivery Verification

If a shipping manifest is provided, cross-reference:
- Total piece count vs. received count
- Missing or damaged pieces (critical for erection schedule)
- Priority pieces (columns and first-bay framing needed first)

---

## DESIGN CODES AND LOADS

### Building Code Information

**EXTRACT**:
- **Building code**: IBC edition (e.g., "2021 IBC")
- **Wind design**: ASCE 7 edition, wind speed, exposure category, risk category
- **Seismic design**: Seismic design category, SDS, SD1
- **Snow load**: Ground snow load, roof snow load (if different)
- **Collateral load**: PSF allowance for MEP, sprinklers, lighting
- **Live load**: Roof live load (typically 20 PSF reducible)
- **Deflection limits**: Roof (L/240 typical), wall (H/120 typical)

---

## CROSS-REFERENCING PEMB DATA

PEMB documents should be cross-referenced with:

1. **Foundation drawings** (structural): Verify anchor bolt patterns match PEMB reactions
2. **Structural specifications** (Div 05, 13): Verify steel grades, bolt specs, erection tolerances
3. **Building specifications** (Div 13 34 19): PEMB-specific spec section requirements
4. **Schedule**: PEMB delivery and erection milestones
5. **Geotechnical report**: Foundation bearing vs. PEMB column reactions
6. **Concrete drawings**: Pier/footing sizes vs. PEMB anchor bolt edge distances

**Common Conflicts to Flag**:
- Anchor bolt pattern on foundation drawing doesn't match PEMB reaction drawing
- Column reaction exceeds foundation capacity
- Anchor bolt edge distance too small for pier size
- Eave height on architectural drawings doesn't match PEMB eave height
- Door opening framing doesn't accommodate specified overhead door
- Insulation R-value in PEMB package doesn't match spec requirement

---

## PEMB-SPECIFIC QC CHECKPOINTS

During extraction, flag these common PEMB quality issues:

### Before Foundation Pour
- [ ] Anchor bolt templates match PEMB reaction drawings (not just foundation drawings)
- [ ] Bolt projections account for grout pad + base plate + leveling nut
- [ ] Pier sizes provide adequate edge distance for anchor bolts
- [ ] Foundation elevations allow for grout pad and base plate

### During Erection
- [ ] Column plumb within H/500
- [ ] Knee bolt torque verified (especially moment connections)
- [ ] Bracing installed before proceeding to next bay
- [ ] Safety cables installed on purlins before sheeting
- [ ] Wind speed monitored — stop at limit

### During Enclosure
- [ ] Panel overlap direction correct (away from prevailing weather)
- [ ] Sealant at laps and penetrations
- [ ] Insulation vapor barrier on warm side
- [ ] Thermal breaks at girt/purlin-to-panel contact
- [ ] Trim sealed at joints

---

## Notes

- PEMB documents may arrive in separate packages: reactions first, then erection drawings, then accessory details. Extract each as received and update the project intelligence incrementally.
- Nucor (the manufacturer for this project) typically provides: reaction sheet, anchor bolt plan, framing plans, connection details, panel layout, trim details, and an erection manual. Each may be a separate PDF.
- Always verify that PEMB reaction loads match what the structural engineer designed the foundations for. Discrepancies are one of the most common coordination issues on PEMB projects.
