# Specifications - Deep Extraction Guide

Extract specific, measurable values from construction specifications. Focus on requirements that affect field operations, quality control, compliance, and visual rendering.

---

## Extraction Priority

| Priority | Data | Purpose |
|----------|------|---------|
| **CRITICAL** | Weather thresholds (temp, wind, moisture) | Work stoppage decisions |
| **CRITICAL** | Testing frequencies with numbers | Schedule inspections |
| **CRITICAL** | Hold points vs. witness points | Work flow control |
| **HIGH** | Material specs with exact values (PSI, grades, R-values) | Procurement and verification |
| **HIGH** | Tolerances with numerical limits | Quality acceptance criteria |
| **HIGH** | Visual/aesthetic data (colors, finishes, materials) [RENDERING] | Rendering pipeline, 3D visualization |
| **MEDIUM** | Submittal requirements | Procurement timeline |
| **MEDIUM** | Warranty periods | Closeout tracking |

---

## Division 01 - General Requirements

### Section 01 31 00 - Project Management
- Coordination meeting schedule (weekly, biweekly)
- Required attendees
- Pre-installation meeting requirements (which systems)

### Section 01 33 00 - Submittal Procedures
- Format (paper, electronic, portal)
- Number of copies
- Review time allowed (e.g., "14 calendar days")
- Resubmittal procedures
- Closeout submittal requirements

### Section 01 45 00 - Quality Control
- Testing agency requirements
- Special inspection scope by CSI division
- Mock-up requirements (which assemblies)
- Manufacturer field rep requirements

### Section 01 50 00 - Temporary Facilities
**CRITICAL - Extract exact values**:
- **Working hours**: "7:00 AM - 5:00 PM, Monday-Friday"
- **Overtime**: Prior approval required? Allowed days?
- **Noise limits**: "85 dBA at property line", restricted hours
- **Dust control**: Methods required
- **Temporary utilities**: Who provides (power, water, sanitary)
- **Fencing**: Height, type, gate locations

### Section 01 77 00 - Closeout
- Warranty duration by system
- Training requirements (owner staff)
- As-built requirements

---

## Division 02 - Existing Conditions

### Section 02 41 00 - Demolition
- Salvage requirements (protect and return)
- Hazardous materials (asbestos, lead)
- Shoring/bracing requirements

---

## Division 03 - Concrete

### Section 03 30 00 - Cast-in-Place Concrete

**CRITICAL - Extract ALL specific numerical values**:

#### Mix Designs
For each mix (list separately: footings, walls, SOG, elevated, columns):
- **Design strength**: _____ PSI at 28 days
- **Max W/C ratio**: e.g., "0.45"
- **Slump**: "4 inches ± 1 inch"
- **Air content**: "5.5% ± 1.5%"
- **Max aggregate size**: "3/4 inch"
- **Admixtures**: Types (water reducer Type F, accelerator, air entrainment)

#### Weather Requirements
- **Cold weather threshold**: "Below 40°F"
- **Cold weather protection**:
  - Min concrete temp at placement: "50°F"
  - Min ambient temp: "40°F"
  - Protection method: "Insulated blankets"
  - Duration: "Maintain 50°F for 72 hours"
- **Hot weather threshold**: "Above 90°F"
- **Hot weather measures**:
  - Max concrete temp: "90°F"
  - Mitigation: "Ice in mix, cool aggregates, night placement if >95°F"

#### Curing
- **Method**: Wet burlap, curing compound, waterproof sheet
- **Duration by element**:
  - Slabs: "7 days minimum"
  - Walls: "3 days minimum"
  - Columns: "3 days minimum"

#### Testing
- **Cylinder frequency**: "1 set per 50 CY or per day, whichever is more"
- **Cylinders per set**: "4 cylinders (for 7-day, 28-day, spares)"
- **Cylinder size**: "4x8 inch" or "6x12 inch"
- **Break schedule**: "7-day (optional), 28-day (required)"
- **Slump testing**: "Every load" or "Every 50 CY"

#### Tolerances
- **Slab flatness/levelness**: "FF 35 / FL 25 minimum"
- **Slab thickness**: "± 1/4 inch"
- **Elevation**: "± 1/4 inch"

**Example extraction**:
```
Footings: 3,000 PSI, w/c 0.50 max, slump 4"±1"
Walls: 3,500 PSI, w/c 0.48 max, slump 4"±1"
SOG: 4,000 PSI, w/c 0.45 max, slump 4"±1", air 5.5%±1.5%

Cold: <40°F, maintain 50°F for 72 hours, insulated blankets
Hot: >90°F, ice in mix, cool aggregates, night pour if >95°F

Cure: 7 days wet for slabs, 3 days for walls/columns
Test: 1 set per 50 CY or per day (4 cylinders), break at 7 and 28 days
Tolerance: FF 35/FL 25, thickness ±1/4"
```

---

## Division 04 - Masonry

### Section 04 20 00 - Unit Masonry
- **CMU strength**: _____ PSI
- **Grout**: Fine/coarse, _____ PSI, grouted cells (all vs. bond beams only)
- **Mortar type**: Type N, S, or M (where used)
- **Reinforcing**: Bond beam spacing, vertical rebar spacing, sizes
- **Control joints**: "Maximum 25 feet o.c. or at openings"
- **Cold weather**: "Below 40°F: heat mortar, protect work"
- **Hot weather**: "Above 90°F: shade materials, fog mist"

---

## Division 05 - Metals

### Section 05 12 00 - Structural Steel
- **Steel grades**: Already in structural notes, but confirm here
- **Bolted connections**: Torque values by size, snug vs. fully tensioned
- **Welded connections**: Inspection % (e.g., "100% visual, 10% UT on moment connections")
- **Fireproofing thickness**: By rating (1-hr, 2-hr, 3-hr)

---

## Division 06 - Wood

### Section 06 10 00 - Rough Carpentry
- **Lumber grades**: Studs (Stud grade), joists (No. 2 or better)
- **Treated lumber**: Ground contact vs. above-ground rating
- **Engineered lumber**: LVL, I-joist load ratings
- **Moisture content**: "Maximum 19%" or "Maximum 15% for finish"

---

## Division 07 - Thermal & Moisture

### Section 07 21 00 - Thermal Insulation
- **Batt insulation**: R-value, thickness, kraft-faced/unfaced
- **Rigid insulation**: Type (polyiso, EPS, XPS), R-value, thickness
- **Spray foam**: Open-cell vs. closed-cell, R-value per inch

### Section 07 50 00 - Membrane Roofing
- **Membrane type**: TPO, EPDM, PVC, built-up, mod bit
- **Membrane thickness**: "60 mil TPO"
- **Insulation**: Type, thickness, R-value
- **Roof slope**: "1/4 inch per foot minimum"
- **Warranty**: "20-year NDL manufacturer warranty"

### Section 07 60 00 - Flashing and Sheet Metal [RENDERING]
- **Material**: Aluminum, galvanized steel, stainless, copper
- **Finish**: Mill finish, painted, anodized
- **Color**: Specific finish code (e.g., "Champagne Metallic", "Burnished Slate")

### Section 07 41 00 - Roof Panels [RENDERING]
- **Material and profile**: Standing seam, metal, membrane type
- **Color code**: Manufacturer color designation (e.g., "Kynar 500, Polar White")
- **Panel width**: Rib spacing, coverage width
- **Fastening**: Clips, seams, mechanical attachment

### Section 07 42 00 - Wall Panels [RENDERING]
- **Exterior wall panel color**: Metal panel color name/code (e.g., "Champagne Metallic", "Burnished Slate")
- **Panel profile**: Rib spacing, panel width, flat vs. corrugated
- **Profile depth and type**: 7/8" corrugated, 1.5" standing seam, etc.
- **Installation method**: Vertical, horizontal, diagonal

### Section 07 90 00 - Joint Sealants
- **Sealant types** by location: Silicone, polyurethane, polysulfide
- **Joint width and depth**
- **Backer rod** sizing
- **Sealant color** [RENDERING]: Where visible (e.g., "Bronze" or "White" silicone at windows)

---

## Division 08 - Openings [RENDERING]

This division contains critical visual specification data for rendering and 3D visualization.

### Section 08 11 00 - Hollow Metal Doors and Frames [RENDERING]

Extract for each door type:
- **Standard finish**: Factory prime, powder coat, galvanized, painted
- **Color**: If specified (e.g., "Paint to match wall color SW 7006", "Stainless steel")
- **Frame profile**: Standard, double rabbet, wraparound
- **Gauge/thickness**: 20 ga., 18 ga., 16 ga.
- **Fire-rated assemblies**: If required, rating (1-hr, 1.5-hr, 2-hr)
- **Hardware finish**: See Section 08 71 00

**Example extraction**:
```
Corridor Doors (HM): 18 ga. prime finish, paint to SW 7006 Extra White
Patient Room Doors (HM): 20 ga., primed, paint to SW 7015 Repose Gray
Exterior Doors (HM): 16 ga., galvanized with aluminum threshold
```

### Section 08 14 00 - Wood Doors [RENDERING]

Extract for each door type:
- **Species**: If stained (oak, maple, cherry, walnut, hickory)
- **Stain color**: If specified (e.g., "Golden Oak", "Cherry", "Natural")
- **Paint color**: If painted (cross-reference paint schedule)
- **Panel style**: Flush, raised panel, glass lite (single/multiple), solid panel
- **Glass type**: Clear, tempered, frosted, tinted
- **Fire-rated**: Rating if required

**Example extraction**:
```
Entrance Door: Solid wood, Cherry species, Natural Cherry stain
Interior Wood Doors: Flush door, primed, paint to schedule (varies by room)
Conference Room: Raised panel, Natural finish, with clear glass lites
```

### Section 08 41 00 - Aluminum Entrances and Storefronts [RENDERING]

Extract for each entrance/storefront system:
- **Finish**: Clear anodized, dark bronze anodized, painted, powder coat
- **Color code**: Manufacturer color designation (e.g., "Satin Anodized", "Duranodic 312")
- **Frame color**: If painted, specific color code
- **Mullion profile**: Width (1.75", 2.5", 3"), depth, material
- **Glass type**: Clear, tinted (bronze, gray, green), low-E appearance
- **Glazing appearance**: Single-pane vs. insulated unit appearance

**Example extraction**:
```
Main Entrance: Aluminum storefront, clear anodized finish
- Mullion: 2.5" width, satin-finish aluminum
- Glass: 1" insulated units, clear/clear, low-E coating (slight blue tint)
Exterior glazing: Tinted gray, 1" insulated low-E
```

### Section 08 51 00 - Aluminum Windows [RENDERING]

Extract for each window type:
- **Frame finish/color**: Same as storefronts typically (clear anodized, bronze, painted)
- **Color code**: Specific manufacturer designation
- **Glass type appearance**: Clear, tinted (bronze, gray, green), low-E appearance
- **Spacer bar color**: Black, silver (visible in insulated glass units)
- **Frame depth**: Typical depth for architectural appearance
- **Operating style**: Fixed, casement, double-hung, awning, sliding

**Example extraction**:
```
Patient Room Windows: Aluminum frame, clear anodized, 1" insulated units
- Glass: Clear/clear, low-E (minimal visible coating)
- Spacers: Black aluminum spacers (visible in perimeter)
Corridor Windows: Same frame, clear glass, fixed operation
```

### Section 08 71 00 - Door Hardware [RENDERING]

Extract standard finish and consistency:
- **Standard finish**: 626 (Satin Chrome), 652 (Satin Chrome Plated), US26D (Satin Stainless), 625 (Polished Chrome), etc.
- **Finish consistency**: All hardware same finish, or varied by area?
- **Hardware style**: Modern, traditional, commercial-grade, accessible
- **Specialty finishes**: Antimicrobial copper, decorative, matte black, brushed nickel
- **Key functions**: Locks, closers, hinges, exit devices, coordinators, holders

**Example extraction**:
```
Standard Finish: 626 (Satin Chrome) for all interior doors
Exterior Doors: 652 (Satin Chrome Plated) stainless hardware
Accessible Doors: ADA-compliant lever handles, satin stainless
All Hardware: Heavy-duty commercial grade, synchronized finish
```

---

## Division 09 - Finishes [RENDERING]

This division contains the majority of visual specification data critical to rendering accuracy.

### Section 09 20 00 - Plaster and Gypsum Board Systems

#### Section 09 29 00 - Gypsum Board [RENDERING - EXPANDED]

**Material specifications**:
- **GWB thickness**: 1/2", 5/8"
- **GWB type**: Regular, Type X (fire-rated), abuse-resistant (Type C), moisture-resistant (Type A)
- **Fire ratings**: 1-hour, 2-hour assemblies by wall type
- **Finish level descriptions**:
  - Level 4 = smooth for paint, ready for eggshell or higher sheen
  - Level 5 = skim coat finish, ready for gloss or semi-gloss
- **Abuse-resistant locations**: Corridors, common areas, high-traffic zones (specify which rooms)
- **Joint compound**: All-purpose, lightweight, setting-type
- **Tape type**: Paper or mesh (affects appearance of finished joints)

**Example extraction**:
```
All interior walls: 5/8" Type X GWB, Level 4 finish
Patient rooms: 5/8" abuse-resistant Type C, Level 4
Corridor walls: 5/8" Type X with corner bead protection
Ceilings: 1/2" regular GWB, Level 4 finish
```

### Section 09 30 00 - Tiling [RENDERING - NEW]

Extract by room type and location:

#### Floor Tile
- **Size**: 12"x12", 18"x18", 24"x24", other
- **Material**: Ceramic, porcelain, glass, stone
- **Color**: Specific product name and color (e.g., "Daltile Colour Collection, Sand")
- **Finish**: Matte, gloss, textured, slip-resistant rating
- **Grout type**: Unsanded, sanded, epoxy
- **Grout color**: White, gray, charcoal, colored

#### Wall Tile
- **Size**: 4"x4", 6"x6", 8"x10", subway 3"x6", other
- **Material**: Ceramic, porcelain, glass, stone
- **Color**: Specific product (e.g., "Emser Subway, Bright White")
- **Pattern**: Subway (running bond), stack bond, running bond, herringbone
- **Finish**: Matte, gloss, textured
- **Grout color**: White, gray, contrasting color

#### Trim and Accent Pieces
- **Bullnose edges**: On perimeter walls, shelves
- **Cove base**: If specified at wall/floor junction
- **Accent tile**: Decorative patterns, contrasting colors
- **Specialty pieces**: Chair rail tile, borders, listels

**Example extraction**:
```
Restroom Floors: Porcelain, 12"x12", Daltile Colour Sand, matte finish
- Grout: Sanded, gray, 1/8" joint
Restroom Walls (lower): Ceramic subway 3"x6", white, running bond
- Grout: Unsanded white, 1/4" joint
Accent band: Daltile decorative trim, gray with pattern
```

### Section 09 51 00 - Acoustical Ceilings [RENDERING - EXPANDED]

**Specifications for visual accuracy**:
- **Tile product/color**: Manufacturer and specific product (e.g., "Armstrong Fine Fissured #1728, White", "USG Radar, Paintable White")
- **Product line**: Specify exact product series/line for accurate appearance
- **Color**: White, off-white, cream, textured white, other
- **Grid color**: White, silver, black, galvanized
- **Grid type**: Exposed 15/16", concealed, linear (T-bar appearance)
- **Suspension system**: Exposed, concealed (affects ceiling appearance)
- **Edge detail**: Tegular (offset edge), square-edge, reveal-edge (shadow effect)
- **Acoustical rating**: NRC (Noise Reduction Coefficient) value
- **Seismic bracing**: If in seismic zone (affects visible bracing)

**Example extraction**:
```
Standard Ceilings: Armstrong Sahara, Fine Fissured, Bright White
- Grid: White 15/16" exposed T-bar
- Edge: Tegular (1/2" drop from grid)
- NRC: 0.70

Open Areas: USG Radar, paintable surface, white
- Grid: Silver concealed system
- Edge: Square edge (flush appearance)
```

### Section 09 65 00 - Resilient Flooring [RENDERING - NEW]

Extract by room type and location:

#### Vinyl Composition Tile (VCT)
- **Manufacturer**: Armstrong, Mannington, Tarkett, Congoleum
- **Product line**: Specific product series
- **Color name and number**: (e.g., "Armstrong Excelon Imperial Texture, Cinnamon")
- **Tile size**: 12"x12" typical, other sizes
- **Pattern/texture**: Solid, speckled, wood-look, stone-look
- **Finish**: Glossy, matte, honed
- **Grout width**: 1/8", 3/16", 1/4"

#### Luxury Vinyl Tile / Luxury Vinyl Plank (LVT/LVP)
- **Manufacturer**: Shaw, Mohawk, Tarkett, Waterproof LVT brands
- **Product line and name**: (e.g., "Shaw Floorte Pro, Aged Hickory")
- **Color/pattern**: Wood-look (species), stone-look, tile-look
- **Plank/tile size**: 7"x48" (LVP), 6"x36", 5"x48", tile sizes
- **Finish**: Matte, satin, gloss, textured
- **Wear layer**: mil thickness (affects durability/appearance)

#### Sheet Vinyl
- **Manufacturer and product**: Mannington, Armstrong, Tarkett, Johnsonite
- **Color and pattern**: Solid color, wood-look, stone-look, custom pattern
- **Width availability**: 6', 12' (affects seaming)
- **Finish**: Glossy, semi-gloss, matte
- **Wear layer**: mil thickness

#### Rubber Flooring
- **Material**: Natural rubber, synthetic, recycled
- **Color**: Specify solid or pattern (e.g., "Charcoal", "Tan Speckle")
- **Texture**: Smooth, studded, wave, custom
- **Tile size**: 12"x12", 18"x18", 24"x24"
- **Thickness**: 3/8", 1/2", 5/8"

**Example extraction**:
```
Corridors: Armstrong Excelon Imperial, Cinnamon, 12"x12" VCT
Patient Rooms: Shaw Floorte Pro LVT, Aged Hickory, 7"x48" planks
Restrooms: Sheet vinyl, Tarkett Harmonious, stone pattern, glossy finish
Specialized Areas: Rubber tile, charcoal, studded, 12"x12"
```

### Section 09 91 00 - Painting [RENDERING - EXPANDED - MOST CRITICAL]

This is the **MOST IMPORTANT section for rendering data**. Extract comprehensively by room type and surface.

#### Paint Manufacturer and Product Line
- **Manufacturer**: Sherwin-Williams, Benjamin Moore, PPG, Behr, Valspar
- **Product line**: Duration, Emerald, Cashmere (SW); Aura, Regal (BM); ProClassic, Exterior (PPG)

#### Color Schedule by Room Type [RENDERING - CRITICAL]

**Create a comprehensive color schedule**:

| Room Type | Surface | Paint Color | Code | Manufacturer | Sheen | Notes |
|-----------|---------|-------------|------|--------------|-------|-------|
| Bedrooms | Walls | Repose Gray | SW 7015 | Sherwin-Williams | Eggshell | All patient/resident rooms |
| Bedrooms | Ceiling | Ceiling White | SW 7050 | Sherwin-Williams | Flat | Standard ceiling |
| Bedrooms | Trim/Door | Extra White | SW 7006 | Sherwin-Williams | Semi-gloss | Door frames, baseboards |
| Corridors | Walls | Extra White | SW 7006 | Sherwin-Williams | Semi-gloss | High-traffic washable |
| Corridors | Ceiling | Ceiling White | SW 7050 | Sherwin-Williams | Flat | 9' height |
| Restrooms | Walls (lower) | Pure White | SW 7005 | Sherwin-Williams | Semi-gloss | Below tile, cleanable |
| Restrooms | Walls (upper) | Pure White | SW 7005 | Sherwin-Williams | Eggshell | Above tile or full wall |
| Common Areas | Walls | Accessible Beige | SW 7036 | Sherwin-Williams | Eggshell | Warm, inviting spaces |
| Offices | Walls | Administrative Gray | SW 7076 | Sherwin-Williams | Eggshell | Professional appearance |
| Mechanical | Walls | Utility Gray | SW 7015 | Sherwin-Williams | Semi-gloss | Washable for equipment |

#### Accent Walls [RENDERING]
- **Location**: Specify room or area
- **Color**: Different from primary room color
- **Reason**: Wayfinding, design accent, emphasis

#### Ceiling Paint [RENDERING]
- **Color**: Usually flat white (Sherwin-Williams 7050 Ceiling White), but may vary
- **Sheen**: Flat (common), eggshell (softer gloss reduction)
- **Product**: May differ from wall paint due to flatness requirement

#### Door and Frame Paint [RENDERING]
- **Color**: Trim color from schedule, or match wall
- **Difference from wall**: If doors are darker or lighter than walls
- **Interior vs. exterior**: Exterior doors may be different from interior

#### Accent or Highlight Colors [RENDERING]
- **Location**: Feature wall, wainscot, accent stripe
- **Color code and manufacturer**
- **Purpose**: Wayfinding, branding, visual interest

#### Special Finishes [RENDERING]
- **Anti-microbial paint**: Restrooms, healthcare areas (specify product)
- **Moisture-resistant**: Bathrooms, kitchens, high-humidity zones
- **Blackboard/marker board paint**: If any areas specified

#### Surface Preparation Requirements (extract if affecting appearance)
- **Primer type**: Oil-based, latex, specialty (shellac for stains)
- **Existing surface prep**: Power wash, TSP, sanding, patching
- **Blocking**: Any primers for bleed-through prevention

**Example comprehensive extraction**:
```
PAINT SPECIFICATION SUMMARY

Manufacturer: Sherwin-Williams Duration (exterior), Emerald (interior)

BEDROOMS/PATIENT ROOMS:
- Walls: SW 7015 Repose Gray, eggshell finish
- Ceiling: SW 7050 Ceiling White, flat
- Trim/Doors: SW 7006 Extra White, semi-gloss
- Notes: Soft, calming color for patient areas

CORRIDORS (high-traffic):
- Walls: SW 7006 Extra White, semi-gloss (scrubbable)
- Ceiling: SW 7050 Ceiling White, flat
- Trim: Same as walls
- Notes: Semi-gloss for durability, cleanability

RESTROOMS:
- Lower walls (below tile): SW 7005 Pure White, semi-gloss
- Upper walls (or full if no tile): SW 7005 Pure White, eggshell
- Ceiling: SW 7050 Ceiling White, flat
- Notes: Bright, clean appearance, moisture-resistant primer

COMMON AREAS (dining, lounge):
- Walls: SW 7036 Accessible Beige, eggshell finish
- Ceiling: SW 7050 Ceiling White, flat
- Trim: SW 7006 Extra White, semi-gloss
- Notes: Warm, inviting color palette

OFFICES/ADMINISTRATION:
- Walls: SW 7076 Administrative Gray, eggshell
- Ceiling: SW 7050 Ceiling White, flat
- Trim: SW 7006 Extra White, semi-gloss
- Notes: Professional appearance

MECHANICAL ROOMS:
- Walls: SW 7015 Repose Gray, semi-gloss
- Notes: Utility finish, scrubbable for equipment access

EXTERIOR:
- Main Exterior: Duration Exterior, Burnished Slate (color code TBD)
- Trim/Fascia: Duration, Urbane Bronze (color code TBD)
- Priming: All substrate per manufacturer
```

---

## Division 10 - Specialties [RENDERING]

### Section 10 21 00 - Toilet Compartments [RENDERING]

**Visual specifications**:
- **Material**: Powder-coated steel, solid plastic (phenolic), laminate, stainless steel
- **Color**: Gray, cream, black, white, stainless, custom laminate color
- **Finish**: Matte, satin (stainless), gloss powder coat
- **Appearance**: Sleek modern vs. traditional, texture vs. smooth
- **Door style**: In-swing, out-swing, bi-fold, pocket
- **Urinal screen material**: If applicable (stainless, powder coat, plastic)

**Example extraction**:
```
Toilet Compartments: Solid phenolic, dove gray color, satin finish
- Configuration: Floor-mounted, in-swing doors
- Accessories: Satin stainless steel hardware
```

### Section 10 28 00 - Toilet Accessories [RENDERING]

**Extract finish and style for all items**:
- **Standard finish**: Satin stainless steel, bright chrome, matte black, powder-coated white
- **Style**: Modern, traditional, commercial-heavy
- **Mounting**: Surface-mount, recessed, semi-recessed
- **Items to specify**:
  - Soap dispensers
  - Paper towel dispensers
  - Toilet paper holders
  - Grab bars
  - Mirrors
  - Shelves/utility shelves
  - Hooks
  - Waste receptacles

**Example extraction**:
```
Restroom Accessories: Satin stainless steel finish, all items
- Soap dispenser: Recessed, auto-sensor
- Paper towel: Recessed dispenser
- Toilet paper: Surface-mount, stainless hardware
- Grab bars: 1.25" diameter, satin stainless
- Mirror: Recessed, stainless frame
- Waste: Stainless steel pedal-activated
```

### Section 10 26 00 - Wall and Corner Guards [RENDERING]

**Visual specifications**:
- **Material**: Stainless steel, vinyl, rubber, aluminum
- **Color**: Match wall (paint), natural stainless, contrasting color for visibility
- **Profile**: Corner guards, crash rails, handrails
- **Height**: Standard 48", or custom height
- **Style**: Modern minimalist, substantial profile

**Example extraction**:
```
Corner Guards: Stainless steel, satin finish, 48" height
- Locations: All interior corners of corridors
- Crash rails: 6" x 48", satin stainless at nursing stations
Handrails: 1.25" stainless tube, satin finish, ADA-compliant
```

### Section 10 44 00 - Fire Protection Specialties [RENDERING]

**Visual specifications**:
- **Extinguisher cabinet**: Recessed, semi-recessed, surface-mounted
- **Cabinet finish**: Painted white, stainless steel, glass door (transparent)
- **Color**: White enamel, brushed stainless, polished stainless
- **Door style**: Swing, sliding, hinged glass
- **Location signage**: If applicable (visibility requirements)

**Example extraction**:
```
Fire Extinguisher Cabinets: Semi-recessed, white enamel finish
- Door: Hinged acrylic/glass door (transparent)
- Frame: White powder-coated steel
- Signage: Red band or label as required
```

---

## Division 12 - Furnishings [RENDERING]

### Section 12 35 00 - Casework [RENDERING]

**Extract for all cabinet locations** (kitchens, nurse stations, storage, etc.):

#### Cabinet Construction
- **Type**: Frameless (European) vs. face-frame (traditional)
- **Material**: Thermofoil-wrapped, wood veneer, painted MDF, plastic laminate (HPL), solid wood
- **Manufacturing**: Stock vs. semi-custom vs. fully custom

#### Door Style [RENDERING - CRITICAL]
- **Style**: Shaker, flat panel, raised panel, slab, glass-front, open shelving
- **Appearance**: Modern minimal, transitional, traditional

#### Color and Finish [RENDERING - CRITICAL]
- **Finish type**: Painted (specify color), wood stain (specify species/color), laminate (specify color/pattern)
- **Specific color/product**:
  - Painted example: "White Shaker, high-gloss painted MDF"
  - Stain example: "Natural Maple, hand-rubbed finish"
  - Laminate example: "Warm Gray HPL laminate, matte finish"

#### Hardware [RENDERING]
- **Pull style**: Bar pull, cup pull, knob, ring pull, finger pull
- **Finish**: Brushed nickel, polished chrome, matte black, stainless steel, bronze
- **Style**: Modern, traditional, decorative

#### Interior Finish
- **Backing**: Open or finished back
- **Interior material**: Melamine (color), veneer, painted
- **Shelving**: Adjustable or fixed
- **Interior color**: White melamine, natural, stained to match exterior

**Example extraction**:
```
Nurse Station Casework:
- Cabinet type: Frameless, European style
- Material: Painted MDF, White Shaker doors
- Color: Bright white, semi-gloss paint
- Hardware: Brushed nickel bar pulls, 128mm centers
- Interior: White melamine backing
- Countertop: See Section 12 36 00

Resident Storage Casework:
- Cabinet type: Face-frame traditional
- Material: Wood veneer over plywood
- Door style: Raised panel, natural finish
- Color: Natural Maple, hand-rubbed
- Hardware: Oil-rubbed bronze knobs, 96mm centers
- Interior: Natural wood backing
```

### Section 12 36 00 - Countertops [RENDERING]

**Extract for all countertop locations**:

#### Countertop Material [RENDERING - CRITICAL]
- **Type**: Solid surface (Corian), engineered quartz (Cambria, Silestone, Caesarstone), laminate, butcher block, stainless steel, tile
- **Manufacturer and product**: Brand and specific product line

#### Color and Pattern [RENDERING - CRITICAL]
- **Color name**: Specific product color code
- **Pattern description**: Solid, veined, speckled, wood-look, stone-look
- **Example**: "Cambria Brittanica Warm, white with warm gray veining"
- **Match/coordination**: If countertop color relates to cabinet color

#### Edge Profile [RENDERING]
- **Profile style**: Square, eased/rounded, bullnose, ogee, beveled
- **Visual impact**: Defines countertop appearance from side view

#### Backsplash (if specified) [RENDERING]
- **Material**: Tile (see Section 09 30 00), laminate, solid surface, stainless, glass
- **Height**: 4", 6", full height to cabinets
- **Color/pattern**: Coordinate with countertop and tile specifications
- **Finish**: Matte, gloss, textured

**Example extraction**:
```
Nurse Station Countertop:
- Material: Engineered quartz, Cambria
- Product: Brittanica Warm, white with gray veining
- Edge: Eased/rounded profile
- Backsplash: Subway tile (white ceramic, 3"x6"), grout 1/4" light gray
- Thickness: 1.25" (2-piece or solid)

Resident Kitchen Area Countertop:
- Material: Solid surface, Corian
- Color: Almond, solid color
- Edge: Bullnose profile
- Backsplash: 6" height, same Corian, integrated appearance
```

---

## Division 14 - Conveying Systems

### Section 14 21 00 - Elevators
- **Capacity**: Passenger load (e.g., 3500 lbs, 2500 lbs)
- **Speed**: Feet per minute (fpm)
- **Doors**: Manual swing, automatic sliding (affects appearance)
- **Interior finish** [RENDERING]: Stainless steel, vinyl wall panels, mirror, painted steel
- **Floor finish** [RENDERING]: Stainless steel, ceramic tile, rubber

---

## Hold Points vs. Witness Points

**CRITICAL DISTINCTION**:

**Hold Points** - Work MUST STOP until inspection passes:
- Pre-placement inspection (rebar, formwork, embeds before concrete)
- Subgrade inspection (compaction before SOG)
- Rough-in inspections (MEP before drywall)
- Structural connections (before fireproofing)

**Witness Points** - Inspector should be present, but work can proceed:
- Concrete placement (inspector may witness but doesn't stop pour)
- Compaction testing (ongoing, not blocking)
- Certain weld inspections (can proceed if inspector unavailable)

**Extract both types with clear labels**.

---

## Testing Frequencies

**Always extract with specific numbers**:

Examples:
- Concrete cylinders: "1 set per 50 CY or per day, whichever is more"
- Compaction: "1 test per 2,500 SF per lift" or "1 test per 500 CY fill"
- Structural steel: "Visual inspect 100% connections, UT 10% of moment connections"
- Fireproofing: "Thickness test every 5,000 SF per rated assembly"
- Masonry: "1 prism per 5,000 SF wall area"

---

## Tolerances with Numbers

Extract all numerical tolerance limits:

Examples:
- Concrete slab flatness: "FF 35 / FL 25 minimum"
- Slab thickness: "± 1/4 inch"
- Masonry plumb: "± 1/4 inch in 10 feet"
- Steel erection plumb: "± 1:500"
- Door/window elevation: "± 1/8 inch"
- Casework plumb and level: "± 1/8 inch in 10 feet"
- Paint coverage: "Wet mil thickness per manufacturer" or "Dry mil after curing"

---

## Output Structure

```json
{
  "spec_sections": [
    {
      "division": "03",
      "section": "03 30 00",
      "title": "Cast-in-Place Concrete",
      "key_req": "4000 PSI, w/c 0.45 max, slump 4\"±1\"",
      "weather_thresholds": {
        "cold_weather_min_temp": "40°F",
        "cold_weather_protection": "Maintain 50°F for 72 hours",
        "hot_weather_max_temp": "90°F",
        "hot_weather_measures": "Ice in mix, night pour if >95°F"
      },
      "testing": {
        "frequency": "1 set per 50 CY or per day",
        "type": "4 cylinders (4x8 inch)",
        "breaks": "7-day and 28-day"
      },
      "hold_points": [
        "Pre-placement inspection of rebar, formwork, embeds",
        "Subgrade/vapor barrier inspection before SOG"
      ],
      "witness_points": [
        "Concrete placement (optional witness)"
      ],
      "tolerances": {
        "slump": "4\" ± 1\"",
        "air_content": "5.5% ± 1.5%",
        "floor_flatness": "FF 35 / FL 25"
      }
    }
  ],
  "visual_specifications": {
    "exterior_colors": {
      "wall_panels": {
        "color_name": "Champagne Metallic",
        "color_code": "NUC-002",
        "manufacturer": "Nucor",
        "profile": "7/8\" corrugated",
        "panel_width": "36\" coverage width"
      },
      "roof_color": {
        "color_name": "Polar White",
        "color_code": "KYN-PW-500",
        "membrane_type": "60 mil TPO"
      },
      "trim_fascia": {
        "color_name": "Burnished Slate",
        "color_code": "DUR-BS",
        "material": "Galvanized steel"
      }
    },
    "paint_schedule": [
      {
        "room_type": "Bedrooms",
        "surface": "Walls",
        "color_code": "SW 7015",
        "color_name": "Repose Gray",
        "manufacturer": "Sherwin-Williams",
        "product_line": "Emerald",
        "sheen": "Eggshell",
        "notes": "All patient/resident rooms"
      },
      {
        "room_type": "Corridors",
        "surface": "Walls",
        "color_code": "SW 7006",
        "color_name": "Extra White",
        "manufacturer": "Sherwin-Williams",
        "product_line": "Duration",
        "sheen": "Semi-gloss",
        "notes": "High-traffic, scrubbable"
      },
      {
        "room_type": "All Areas",
        "surface": "Ceilings",
        "color_code": "SW 7050",
        "color_name": "Ceiling White",
        "manufacturer": "Sherwin-Williams",
        "product_line": "Emerald",
        "sheen": "Flat",
        "notes": "Standard ceiling finish"
      }
    ],
    "hardware_finishes": {
      "standard_finish": "626 (Satin Chrome)",
      "exterior_finish": "652 (Satin Chrome Plated)",
      "accessible_doors": "US26D (Satin Stainless)",
      "finish_consistency": "All hardware synchronized"
    },
    "casework_specs": {
      "nurse_station": {
        "door_style": "Shaker",
        "material": "Painted MDF",
        "color_name": "White",
        "color_code": "N/A",
        "hardware_finish": "Brushed Nickel",
        "interior_finish": "White melamine",
        "countertop": "Engineered quartz, Cambria Brittanica Warm"
      }
    },
    "flooring_colors": [
      {
        "room_type": "Corridors",
        "product": "Armstrong Excelon Imperial Texture",
        "color_name": "Cinnamon",
        "color_code": "EXC-CIN-12",
        "material": "Vinyl Composition Tile",
        "size": "12\" x 12\""
      },
      {
        "room_type": "Patient Rooms",
        "product": "Shaw Floorte Pro",
        "color_name": "Aged Hickory",
        "color_code": "SHP-AH-7x48",
        "material": "Luxury Vinyl Plank",
        "size": "7\" x 48\""
      }
    ],
    "door_specifications": {
      "hollow_metal_doors": {
        "standard_finish": "Prime",
        "paint_color": "SW 7006 Extra White",
        "frame_profile": "Standard",
        "gauge": "20 ga."
      },
      "aluminum_storefronts": {
        "finish": "Clear Anodized",
        "color_code": "Clear",
        "mullion_width": "2.5\"",
        "glass_type": "1\" insulated, clear/clear, low-E"
      }
    },
    "accessory_finishes": {
      "toilet_compartments": "Solid phenolic, dove gray, satin",
      "grab_bars": "Satin stainless steel, 1.25\" diameter",
      "dispensers": "Satin stainless steel, recessed",
      "corner_guards": "Stainless steel, satin finish"
    }
  }
}
```

---

## Integration with Daily Reports

Spec data enables rendering and field documentation:

### Visual Data Integration
- **Color verification**: "Wall paint applied: SW 7015 Repose Gray, compared to spec match sample"
- **Material confirmation**: "Casework installed: White Shaker doors, brushed nickel hardware per spec"
- **Finish inspection**: "Paint sheen verified: Semi-gloss on corridor trim per specification"
- **Hardware consistency**: "All door hardware: 626 Satin Chrome finish, synchronized across facility"

### Field Compliance Documentation
- **Photo comparison**: Take photos during installation, compare to color/finish specifications
- **Sample retention**: Keep paint chips, hardware samples, material swatches on file for final verification
- **Punch list accuracy**: "Bedroom paint SW 7015 - verify color match before final acceptance"

### Rendering System Integration
- **Accurate 3D visualization**: Color codes and material specifications feed directly to rendering pipeline
- **Photo-realistic rendering**: Hardware finishes, paint sheens, and panel colors ensure rendered images match built environment
- **Wayfinding visualization**: Paint schedule color coding supports digital wayfinding applications
- **Material tracking**: Rendering system can track which materials have been approved vs. still pending submittal review

---

## MEP Systems - Visual Specifications [RENDERING]

### HVAC
- **Duct insulation**: R-value, thickness (affects visible duct appearance when exposed)
- **Equipment finish** [RENDERING]: Painted metal, stainless steel, powder coat color
- **Color coding**: If ducts or equipment color-coded (e.g., blue for cool supply)

### Electrical
- **Conduit color**: Gray, black, colored (if color-coded by system)
- **Panel finish**: Stainless steel, powder coat, painted (if exposed)
- **LED fixture finish** [RENDERING]: Satin chrome, brushed nickel, white, black, brass

### Plumbing
- **Visible pipe finish**: Copper (natural patina or polished), stainless steel, painted
- **Pipe color coding**: If required (hot = red, cold = blue, etc.)

---

## Commands Available for Reference

/log, /morning-brief, /daily-report, /dashboard, /look-ahead, /submittal-review, /prepare-rfi, /weekly-report, /material-tracker, /set-project, /update, /process-docs, /meeting-notes, /inspections, /change-order, /punch-list, /pay-app, /delay, /closeout, /safety

---

## Summary: Visual Data Priority for Rendering

When extracting specifications, prioritize visual/aesthetic data in this order:

1. **Paint schedule** (colors by room type, manufacturer, sheen)
2. **Exterior colors** (wall panels, roof, trim)
3. **Flooring colors and materials** (all room types)
4. **Hardware finishes** (door hardware, accessories)
5. **Casework colors and door styles** (cabinets, built-ins)
6. **Tile specifications** (color, finish, grout color)
7. **Ceiling specifications** (product, color, grid color, edge detail)
8. **Door and frame colors** (hollow metal, wood, aluminum)
9. **Accessory finishes** (grab bars, dispensers, compartments)
10. **Window/glass specifications** (frame finish, glass tint, appearance)

This data directly supports rendering accuracy, photo-realistic visualization, and field verification photography.

---

## Cross-Discipline Conflict Detection Rules

Construction documents are authored by multiple design firms (architect, structural engineer, MEP engineer, civil engineer, landscape architect) across extended timelines. Conflicts between disciplines are common and expected. This section defines the methodology for detecting, classifying, and routing conflicts during specification and plan extraction.

### Value Comparison Methodology

#### Step 1: Extract with Full Context
Every numerical value extracted from specifications must carry:
- **Value**: The number with units (e.g., "4,000 PSI")
- **Context**: What the value describes (e.g., "footing concrete design strength at 28 days")
- **Source**: Exact location (e.g., "Spec 03 30 00, para 2.1.A.3")
- **Source type**: specification | plan_note | schedule_table | detail_callout | general_note
- **Revision**: Document revision level (e.g., "Rev 2, dated 2026-01-15")

#### Step 2: Build Comparison Pairs
After extraction, build comparison pairs for the same parameter from different sources:

```json
{
  "comparison_pair": {
    "parameter": "footing_concrete_strength",
    "value_a": {
      "value": "4,000 PSI",
      "source": "Spec 03 30 00, para 2.1.A",
      "source_type": "specification",
      "revision": "Rev 2"
    },
    "value_b": {
      "value": "3,500 PSI",
      "source": "Sheet S-001, General Note 4",
      "source_type": "plan_note",
      "revision": "Rev 3"
    },
    "match": false,
    "variance": "14.3%",
    "severity": "CRITICAL"
  }
}
```

#### Step 3: Unit Normalization
Before comparing, normalize units:
- Pressure: PSI, kPa, MPa (convert all to PSI for comparison)
- Length: feet-inches, decimal feet, inches, mm (convert to inches)
- Temperature: Fahrenheit, Celsius (convert to Fahrenheit)
- Area: SF, SY, SM (convert to SF)
- Volume: CY, CF, CM (convert to CY)
- Weight: lbs, kips, tons, kg (convert to lbs)
- Slope: percent, ratio (e.g., 1/4"/ft = 2.08% -- convert to percent)

### Common Conflict Patterns by Discipline Pair

#### Architectural vs. Structural

| Parameter | Arch Source | Struct Source | Conflict Example |
|-----------|-----------|-------------|-----------------|
| Slab thickness | Floor plan note "6\" SOG" | Structural detail "5\" SOG" | 1" discrepancy affects finish floor height |
| Opening sizes | Elevation shows 8'-0" wide opening | Structural plan shows 7'-6" clear span | Beam sizing affected |
| Floor elevation | Architectural FFE = 100.00' | Structural top-of-slab = 99.50' | 6" difference may be intentional (finish thickness) or error |
| Wall thickness | Architectural plan dims show 6" wall | Structural detail shows 8" CMU wall | Affects room dimensions |
| Column locations | Architectural plan shows column at grid intersection | Structural plan shows column offset 6" from grid | Finish wall alignment affected |
| Floor-to-floor height | Architectural section shows 12'-0" floor-to-floor | Structural framing shows 11'-6" clear below steel | Verify clearance for MEP routing |
| Expansion joints | Architectural plan shows joint at grid 5 | Structural plan shows joint at grid 4 | Must align -- structural governs |

#### Architectural vs. MEP

| Parameter | Arch Source | MEP Source | Conflict Example |
|-----------|-----------|-----------|-----------------|
| Ceiling height | RCP shows 9'-0" ACT ceiling | Ductwork routing requires 14" above ceiling | Available plenum space conflict |
| Wall chases | Architectural plan shows 4" chase wall | Plumbing riser requires 6" minimum chase | Wall must be widened |
| Floor penetrations | Architectural plan shows no penetration | Mechanical riser schedule shows 12" pipe through floor | Coordination needed |
| Room size | Architectural plan shows 10'x12' mech room | Equipment schedule shows unit requires 12'x14' clearance | Room undersized for equipment |
| Door clearance | Door schedule shows 3'-0" door to mech room | Equipment is 42" wide, requires 48" clear for maintenance | Door too narrow for equipment replacement |
| Electrical panel location | Room layout shows casework on wall | Electrical plan shows panel on same wall section | Physical conflict |
| Light fixture vs. diffuser | RCP shows light fixture at grid intersection | Mechanical RCP overlay shows diffuser at same location | Ceiling device conflict |

#### Specification vs. Plan Notes

| Parameter | Spec Source | Plan Source | Typical Resolution |
|-----------|-----------|-----------|-------------------|
| Concrete strength | Spec 03 30 00: "4,000 PSI" | Structural notes: "3,500 PSI" | RFI to structural engineer; use higher value pending resolution |
| Rebar cover | Spec 03 30 00: "3\" cover for footings" | Structural detail: "2\" cover shown" | More restrictive (3") controls |
| Curing duration | Spec 03 30 00: "7 days wet cure" | Structural note: "72 hours minimum" | Spec governs (7 days > 72 hours) |
| Compaction | Spec 31 23 00: "95% Standard Proctor" | Civil note: "98% Modified Proctor" | Different test methods -- RFI to clarify which applies |
| Paint sheen | Spec 09 91 00: "semi-gloss corridors" | Finish schedule: "eggshell corridors" | Spec governs unless finish schedule is more recent |
| Testing frequency | Spec 03 30 00: "1 set per 50 CY" | Plan note: "1 set per 100 CY" | More frequent (1/50 CY) controls |

#### Specification vs. Specification (Cross-Division)

| Div A | Div B | Conflict Type | Example |
|-------|-------|--------------|---------|
| Div 03 (Concrete) | Div 31 (Earthwork) | Foundation concrete strength | Div 03 says "3,000 PSI footings" but Div 31 references "4,000 PSI foundation concrete" |
| Div 07 (Roofing) | Div 22 (Plumbing) | Roof penetration requirements | Div 07 requires "factory curb with 8\" minimum height" but Div 22 roof drain detail shows 4" curb |
| Div 08 (Openings) | Div 09 (Finishes) | Door/frame paint | Div 08 says "factory prime coat only" but Div 09 paint schedule omits HM doors from field painting scope |
| Div 09 (Finishes) | Div 12 (Furnishings) | Casework finish | Div 09 shows "paint SW 7006" for casework but Div 12 specifies "HPL laminate, white" for same cabinets |
| Div 23 (HVAC) | Div 26 (Electrical) | Equipment electrical | Div 23 RTU schedule shows "208V/3ph/60A" but Div 26 panel schedule has 50A breaker for same unit |
| Div 03 (Concrete) | Div 07 (Waterproofing) | Below-grade waterproofing | Div 03 says "damproofing" for foundation walls but Div 07 specifies "full waterproofing membrane" |
| Div 05 (Metals) | Div 07 (Fireproofing) | Fireproofing thickness | Div 05 steel notes say "1\" spray fireproofing" but Div 07 says "1.5\" for 2-hour rating" |

### Conflict Classification Rules

**CRITICAL -- Safety/Structural** (Stop work, issue RFI immediately):
- Any disagreement in structural load-carrying parameters: concrete strength, rebar size/grade, steel member sizes, anchor bolt specifications, bearing capacity
- Fire rating discrepancies: rated assembly specifications that disagree between disciplines
- Seismic detailing conflicts: lateral system details that differ between structural and architectural
- Life safety system conflicts: fire alarm, sprinkler, smoke control specifications that disagree
- Means of egress conflicts: exit width, door size, corridor width discrepancies

**MAJOR -- Performance** (Flag for resolution before procurement/installation):
- Energy code compliance parameters: insulation R-values, window U-values/SHGC, air barrier continuity
- Waterproofing/moisture control: membrane type, thickness, coverage conflicts
- Acoustic performance: STC ratings, NRC values that disagree between acoustic consultant and architect
- HVAC capacity: Equipment sizing that conflicts between mechanical engineer's schedule and spec
- Electrical sizing: Panel amperage, wire sizing, conduit sizing that disagrees between plans and spec

**MINOR -- Aesthetic/Cosmetic** (Resolve before installation, do not delay other work):
- Paint color/sheen disagreements
- Hardware finish conflicts (626 vs. 625, brushed vs. polished)
- Ceiling tile product specification vs. what appears on finish schedule
- Grout color, trim profile, accessory finish conflicts
- Carpet/flooring product where spec and schedule reference different products from same manufacturer line

### Resolution Priority Rules

When a conflict is detected, apply these rules to determine which source controls:

1. **Addenda and ASIs supersede original documents**: If an addendum changes a value, the addendum controls even if the original spec or plan still shows the old value.

2. **More recent revision controls**: If Plan Rev 3 (dated 2/10/2026) says "4,000 PSI" and Spec Rev 1 (dated 6/15/2025) says "3,500 PSI", the more recent document likely reflects the design intent -- but RFI is still recommended.

3. **Specification governs over plan notes** (general rule): The spec is the detailed written requirement; plan notes are summaries. If they conflict, spec typically controls -- UNLESS the plan note is more restrictive.

4. **Most restrictive value controls for safety items**: When both values are arguably valid, use the more conservative (higher strength, more cover, thicker section, tighter tolerance) pending RFI resolution.

5. **Numerical specificity beats general language**: "4,000 PSI at 28 days per ASTM C39" beats "high-strength concrete per spec." The more specific value controls.

6. **Design professional of record clarifies their discipline**: Structural conflicts go to the structural engineer. Architectural conflicts go to the architect. MEP conflicts go to the MEP engineer. Do not have the wrong discipline resolve another discipline's conflict.

### Conflict Detection Output Format

```json
{
  "cross_discipline_conflicts": [
    {
      "conflict_id": "XDC-001",
      "disciplines": ["structural", "specification"],
      "parameter": "Footing concrete design strength",
      "values": [
        {"value": "4,000 PSI", "source": "Spec 03 30 00, para 2.1.A", "discipline": "specification"},
        {"value": "3,500 PSI", "source": "Sheet S-001, General Note 4", "discipline": "structural"}
      ],
      "severity": "CRITICAL",
      "category": "structural_capacity",
      "resolution_rule": "RFI to structural engineer. Use 4,000 PSI (more restrictive) pending response.",
      "affects": ["Concrete mix design submittal", "Footing placement", "Cost (higher strength = higher cost)"],
      "rfi_needed": true
    }
  ]
}
```

---

## Spec-to-Submittal Validation

When the submittal extraction pipeline (submittals-deep-extraction.md) has processed submitted product data, this section defines how to automatically compare that data against specification requirements to determine compliance.

### Validation Framework

For each specification requirement, extract a testable criterion and compare it against the corresponding submittal data:

```
Spec Requirement: "Concrete mix design: 4,000 PSI at 28 days"
  Criterion: compressive_strength >= 4,000 PSI
  Submittal Data: "Proposed mix: 4,200 PSI at 28 days"
  Result: 4,200 >= 4,000 --> PASS
```

### Comparison Methodology

#### Numerical Requirements (Greater Than / Less Than)

These requirements have a clear pass/fail threshold:

| Requirement Type | Operator | Example Spec | Example Submittal | Result |
|-----------------|----------|-------------|-------------------|--------|
| Minimum strength | >= | "4,000 PSI min" | "4,200 PSI" | PASS (exceeds min) |
| Maximum w/c ratio | <= | "0.45 max" | "0.42" | PASS (below max) |
| Minimum R-value | >= | "R-25 minimum" | "R-21" | FAIL (below min) |
| Maximum U-value | <= | "U-0.30 max" | "U-0.28" | PASS (below max) |
| Minimum thickness | >= | "60 mil min" | "60 mil" | PASS (meets min) |
| Maximum absorption | <= | "0.5% max" | "0.3%" | PASS (below max) |

#### Range Requirements (Within Tolerance)

These requirements have an acceptable range:

| Requirement Type | Range | Example Spec | Example Submittal | Result |
|-----------------|-------|-------------|-------------------|--------|
| Slump | Within +/- | "4\" +/- 1\"" | "4.5\"" | PASS (within 3-5 range) |
| Air content | Within +/- | "5.5% +/- 1.5%" | "7.5%" | FAIL (exceeds 7.0% max) |
| Dimension tolerance | Within +/- | "36\" +/- 1/4\"" | "36-1/8\"" | PASS (within range) |
| Color match | Delta E | "Delta E < 1.0" | "Delta E = 0.8" | PASS (within tolerance) |

#### Exact Match Requirements

These requirements must match exactly or meet a categorical specification:

| Requirement Type | Match Type | Example Spec | Example Submittal | Result |
|-----------------|-----------|-------------|-------------------|--------|
| ASTM standard | Exact | "ASTM A615 Grade 60" | "ASTM A615 Grade 60" | PASS |
| Fire rating | Minimum | "2-hour fire rating" | "3-hour fire rating" | PASS (exceeds) |
| Material type | Category | "Type X gypsum board" | "Type C gypsum board" | REVIEW (Type C exceeds Type X, but verify intent) |
| Color | Exact | "SW 7006 Extra White" | "SW 7006 Extra White" | PASS |
| Manufacturer | Listed | "Armstrong or approved equal" | "USG" | REVIEW ("or equal" requires architect approval) |

### Pass/Fail Criteria by Requirement Type

**Automatic PASS**:
- Submitted value meets or exceeds minimum requirement
- Submitted value meets or is below maximum requirement
- Submitted value is within specified tolerance range
- Submitted product matches specified manufacturer and product exactly

**Automatic FAIL**:
- Submitted value is below minimum requirement
- Submitted value exceeds maximum requirement
- Submitted value is outside tolerance range
- Submitted product does not meet specified ASTM/UL/FM standard
- Required fire rating not met by submitted assembly

**Requires Review** (cannot auto-determine):
- "Or approved equal" substitutions -- architect must evaluate equivalency
- "Match existing" -- requires field sample comparison
- Performance specifications with multiple criteria (e.g., "meets AAMA 2604" -- must verify all sub-criteria)
- Proprietary specifications where only one product is acceptable
- Color matching where subjective judgment is required

### "Or Equal" and Substitution Handling

When specifications allow "or equal" products:

1. **Extract the basis-of-design product**: The named product in the spec (e.g., "Armstrong Sahara or approved equal")
2. **Identify the key performance criteria**: The characteristics that define equivalency
   - For ACT: NRC, CAC, fire rating, edge detail, size, light reflectance
   - For doors: fire rating, gauge, sound rating, abuse resistance, warranty
   - For paint: VOC content, coverage rate, sheen, washability, warranty
3. **Compare submitted product against all criteria**:
   ```
   Basis of design: Armstrong Sahara 2x2
     NRC: 0.70  |  CAC: 35  |  Fire: Class A  |  Edge: Tegular  |  LR: 0.83

   Submitted equal: USG Radar 2x2
     NRC: 0.70  |  CAC: 35  |  Fire: Class A  |  Edge: Tegular  |  LR: 0.82

   Comparison: All criteria met or within 2%. RECOMMEND APPROVAL.
   Note: LR 0.82 vs 0.83 -- negligible difference. Architect to confirm.
   ```
4. **Flag for architect review**: Even if all criteria are met, substitutions require architect's written approval.

### Substitution Request Documentation

When a submitted product does not match the spec but a substitution is proposed:
- **Product proposed**: Full manufacturer, model, product line
- **Reason for substitution**: Cost savings, lead time, availability, improved performance
- **Comparison matrix**: Side-by-side of spec requirements vs. proposed product
- **Impact assessment**: Does the substitution affect other trades, aesthetics, warranty, maintenance?
- **Required approvals**: Architect, engineer of record, owner (as applicable)

### Submittal Compliance Tracking

Track the compliance status of every specification requirement across all submittals:

```json
{
  "submittal_compliance": [
    {
      "spec_section": "03 30 00",
      "spec_title": "Cast-in-Place Concrete",
      "submittal_number": "SUB-003",
      "submittal_status": "approved",
      "requirements_checked": 12,
      "requirements_passed": 11,
      "requirements_failed": 0,
      "requirements_review": 1,
      "review_items": [
        {
          "requirement": "Fly ash content not to exceed 25%",
          "submitted_value": "20% fly ash",
          "result": "REVIEW -- verify mix design performance data supports 20% replacement",
          "resolved": false
        }
      ],
      "overall_compliance": "CONDITIONAL PASS -- pending fly ash verification"
    },
    {
      "spec_section": "09 51 00",
      "spec_title": "Acoustical Ceilings",
      "submittal_number": "SUB-015",
      "submittal_status": "returned_for_revision",
      "requirements_checked": 8,
      "requirements_passed": 6,
      "requirements_failed": 2,
      "requirements_review": 0,
      "failed_items": [
        {
          "requirement": "NRC 0.70 minimum",
          "submitted_value": "NRC 0.55",
          "result": "FAIL -- submitted product does not meet minimum acoustical performance",
          "action": "Resubmit with product meeting NRC >= 0.70"
        },
        {
          "requirement": "Edge detail: Tegular",
          "submitted_value": "Square edge",
          "result": "FAIL -- wrong edge profile. Tegular required for design intent.",
          "action": "Resubmit with tegular edge product"
        }
      ],
      "overall_compliance": "FAIL -- resubmittal required"
    }
  ]
}
```

### Integration with Conflict Detection

Spec-to-submittal validation feeds into the broader conflict detection workflow:
- If a submittal is approved but the approved product conflicts with a plan note or another spec section, flag as a cross-discipline conflict
- If a submittal is rejected, check whether the rejection creates a schedule impact (long-lead items, procurement delays)
- If an "or equal" substitution is approved, update the project intelligence to reflect the approved product (not the original spec product) for downstream tracking

### Validation Automation Rules

When processing submittals alongside specifications:
1. **Match submittal to spec section**: Use CSI division/section numbers to pair submittals with spec requirements
2. **Extract testable criteria from spec**: Convert prose requirements into numerical comparisons
3. **Extract product data from submittal**: Pull performance values, ratings, certifications from product data sheets
4. **Run comparison**: Apply pass/fail criteria per the rules above
5. **Generate compliance report**: Summary with pass/fail/review counts and specific items requiring action
6. **Flag schedule impacts**: If a submittal fails and needs resubmission, flag the impact on procurement lead time and installation schedule
7. **Update project intelligence**: Store compliance status in project config for dashboard display and morning brief alerts
