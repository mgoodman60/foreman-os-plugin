# Construction Quantity Calculation Reference

Formulas and methods for deriving quantities from plan extraction data. Used in Pass 6 of the page-by-page extraction pipeline.

---

## 1. Concrete Quantities (CY)

### Spread Footings
```
Volume = Length × Width × Depth
CY = Volume (CF) ÷ 27
```
- Typical depths: 12", 18", 24", 36"
- Include pedestal/pier extensions above footing if shown
- Count from foundation plan — each footing mark = 1 unit

### Continuous/Strip Footings
```
Volume = Perimeter Length × Width × Depth
CY = Volume (CF) ÷ 27
```
- Measure centerline perimeter from foundation plan
- Account for steps in footing elevation (each step = separate segment)

### Slab on Grade
```
Area (SF) × Thickness (inches) ÷ 12 ÷ 27 = CY
```
- Standard thicknesses: 4", 5", 6", 8"
- Deduct footing areas from slab area
- Add for thickened edges (perimeter and under load-bearing walls)
- Thickened edge: (Thickened depth − slab depth) × width × perimeter length

### Grade Beams
```
Volume = Length × Width × Depth
CY per beam = L × W × D ÷ 27
```
- Measure centerline length between column centers
- Typical sizes: 12"×24", 16"×30", 18"×36"

### Concrete Walls
```
Volume = Length × Height × Thickness
CY = Volume (CF) ÷ 27
```
- Deduct openings > 4 SF
- Include pilasters as separate calculations

### Waste Factor
- Footings: +5% waste
- Slabs: +3-5% waste
- Walls: +5% waste
- Piers/columns: +8% waste

---

## 2. Reinforcing Steel (Rebar)

### Weight per Linear Foot
| Bar Size | Diameter (in) | Weight (lb/ft) | Area (sq in) |
|----------|--------------|----------------|--------------|
| #3       | 0.375        | 0.376          | 0.11         |
| #4       | 0.500        | 0.668          | 0.20         |
| #5       | 0.625        | 1.043          | 0.31         |
| #6       | 0.750        | 1.502          | 0.44         |
| #7       | 0.875        | 2.044          | 0.60         |
| #8       | 1.000        | 2.670          | 0.79         |
| #9       | 1.128        | 3.400          | 1.00         |
| #10      | 1.270        | 4.303          | 1.27         |

### Bar Count from Spacing
```
Number of bars = (Length ÷ Spacing) + 1
```
- Round up to next whole number
- Apply to each direction (longitudinal and transverse)

### Total Rebar Weight
```
Total bars × average length × weight/ft = total lbs
Total lbs ÷ 2000 = tons
```
- Add 10% for laps and waste
- Lap splice length: typically 40 × bar diameter (verify spec)

### Welded Wire Reinforcement (WWR)
```
Area (SF) × weight per SF = total lbs
```
- 6×6-W1.4×W1.4: 0.029 lb/SF
- 6×6-W2.0×W2.0: 0.041 lb/SF
- 6×6-W2.9×W2.9: 0.058 lb/SF
- Add 10% for laps

---

## 3. Earthwork

### Trench Excavation
```
Volume = Length × Width × Depth
CY = Volume (CF) ÷ 27
```
- Width = pipe OD + 12" each side (minimum) or as specified
- Depth = invert elevation − ground elevation + cover depth
- Swell factor: multiply bank CY × 1.25 (typical for clay/silt)

### Building Excavation
```
Volume = (Building footprint + 3' each side) × average depth
CY = Volume (CF) ÷ 27
```
- Overdig: typically 2'-3' beyond footing edge for forming
- Swell factors by soil type:
  - Sand/gravel: 1.12
  - Common earth: 1.25
  - Clay: 1.30
  - Rock: 1.50

### Backfill
```
Backfill CY = Excavation CY − (concrete volume + structure volume in ground)
```
- Compacted fill factor: multiply loose CY × 0.85-0.90
- Import/export = backfill needed − excavation available (adjusted for compaction)

### Subgrade Preparation
```
Area = Building footprint + paving areas
Depth = specified subgrade treatment depth (typically 6"-12")
CY = Area × Depth ÷ 27
```

---

## 4. Drywall & Metal Framing

### Drywall SF
```
Wall drywall SF = Wall length × Wall height − Openings
```
- Openings: doors (width × height) + windows (width × height)
- Only deduct openings > 4 SF (standard estimating practice)
- Count BOTH sides of interior walls
- One side only for exterior sheathing

### Grouping by Wall Type
```
For each wall type:
  Total LF of that type × ceiling height × 2 sides = Gross SF
  − (door count × avg door SF) − (window count × avg window SF) = Net SF
```
- Standard door opening: 3'×7' = 21 SF
- Standard window opening: varies, use schedule dimensions

### Metal Stud Framing
```
Studs = (Wall LF × 12 ÷ spacing) + 1
Track = Wall LF × 2 (top and bottom)
```
- Standard spacing: 16" OC or 24" OC
- Add 10% waste for studs
- Headers over openings: 2× stud length + 12" each end

### Fire-Rated Assemblies
- Track separately by rating (1-hr, 2-hr)
- Note UL assembly number
- Additional layers of drywall per rating requirements

---

## 5. Flooring

### Flooring SF by Type
```
For each finish type in finish schedule:
  Sum room areas where that finish is specified = Total SF
```
- Group rooms by floor finish type from finish schedule
- Add 5-10% waste depending on material:
  - Carpet tile: +5%
  - Sheet vinyl/VCT: +10%
  - Ceramic tile: +10-15%
  - LVP/LVT: +7%
  - Epoxy: +5%

### Tile
```
Field tile SF = Room area − perimeter border width area
Border/accent LF = Room perimeter
```
- Setting materials: thin-set at ~50 SF/bag, grout at ~25 SF/bag

---

## 6. Painting

### Wall Paint SF
```
Wall paint SF = Room perimeter × ceiling height − unpainted surfaces − openings
```
- Unpainted: tile walls, FRP panels, exposed concrete/CMU (if not painted)
- Two coats standard: multiply SF × 2 for coverage calculations

### Ceiling Paint SF
```
Ceiling paint SF = Sum of room areas with painted ceilings (from finish schedule)
```
- ACT (Acoustic Ceiling Tile) ceilings: NOT painted
- GWB ceilings: painted
- Exposed structure: painted if specified

### Coverage Rates
- Latex wall paint: 350-400 SF/gallon per coat
- Primer: 300-350 SF/gallon
- Ceiling paint: 350-400 SF/gallon per coat

---

## 7. Roofing

### Roof Area
```
Plan area × slope factor = Actual roof area
```

### Slope Factors
| Pitch    | Rise/Run | Factor |
|----------|----------|--------|
| Flat     | 0:12     | 1.000  |
| 1/4:12   | 0.25:12  | 1.000  |
| 1/2:12   | 0.5:12   | 1.001  |
| 1:12     | 1:12     | 1.003  |
| 2:12     | 2:12     | 1.014  |
| 3:12     | 3:12     | 1.031  |
| 4:12     | 4:12     | 1.054  |
| 5:12     | 5:12     | 1.083  |
| 6:12     | 6:12     | 1.118  |

### PEMB Metal Roof
- Standing seam panels: width coverage varies (12", 16", 18")
- Panel LF = roof length (perpendicular to ridge)
- Number of panels = roof width ÷ panel coverage width
- Ridge cap LF = building length
- Eave trim LF = building perimeter
- Gutter LF = eave length

### Insulation
```
Insulation SF = Roof area (typically same as plan area for blanket insulation)
```

---

## 8. Code Compliance Calculations

### Occupant Load
```
Occupant Load = Floor Area (SF) ÷ Occupant Load Factor
```

| Use Group | Load Factor (SF/person) |
|-----------|------------------------|
| Assembly (concentrated) | 7 net |
| Assembly (unconcentrated) | 15 net |
| Business | 150 gross |
| Educational | 20 net |
| Institutional (outpatient) | 240 gross |
| Day Care | 35 net |
| Mercantile (ground floor) | 60 gross |
| Storage | 300 gross |
| Kitchens | 200 gross |
| Exercise rooms | 50 gross |

### Egress Width
```
Required egress width = Occupant Load × 0.2 inches/person (doors, corridors)
Required stair width = Occupant Load × 0.3 inches/person
Minimum door width: 32" clear
Minimum corridor width: 44" (>50 occupants), 36" (<50 occupants)
```

### Maximum Travel Distance (IBC Table 1017.2)
| Occupancy | Unsprinklered | Sprinklered |
|-----------|--------------|-------------|
| B (Business) | 200 ft | 300 ft |
| E (Educational/Day Care) | 200 ft | 250 ft |
| I-2 (Institutional) | 150 ft | 200 ft |

### Plumbing Fixture Requirements (IPC Table 403.1)
| Facility Type | WC (M/F) | Lavatory (M/F) | Drinking Fountain |
|---------------|----------|----------------|-------------------|
| Business (per 25) | 1/1 | 1/1 | 1 per 100 |
| Assembly (per 75 M, 40 F) | 1/1 | 1/1 | 1 per 100 |
| Day Care (per 15) | 1/1 | 1/1 | 1 per 100 |
| Medical Office (per 25) | 1/1 | 1/1 | 1 per 100 |

### Fire-Rated Assembly Requirements
| Separation | Rating Required |
|------------|----------------|
| Occupancy separation (E/B) | 1 hour (Table 508.4) |
| Corridor walls (E) | 1 hour (unsprinklered), 0 hour (sprinklered) |
| Corridor walls (I) | 1 hour (regardless) |
| Shaft enclosures | 1 hour (2 stories or less) |

---

## 9. MEP Sizing Rules

### HVAC Ventilation (ASHRAE 62.1)
```
Required CFM = (Rp × occupants) + (Ra × area)
```
- Rp (per person): Office=5, Classroom=10, Healthcare=7.5, Reception=7.5
- Ra (per SF): Office=0.06, Classroom=0.12, Healthcare=0.06, Reception=0.06

### Duct Sizing (rough estimate)
```
Duct area (sq in) = CFM ÷ velocity (FPM)
```
- Main trunk: 800-1200 FPM
- Branch ducts: 600-800 FPM
- Final runs: 400-600 FPM

### Electrical Load
```
General lighting: 3.5 VA/SF (office), 2.0 VA/SF (healthcare)
Receptacle load: 1.0 VA/SF (general), 5.0 VA/SF (medical)
```
- Panel capacity = total connected load × demand factor (typically 0.65-0.80)
- Service size = total demand ÷ voltage

### Plumbing Pipe Sizing (fixture units)
| Fixture | FU (Cold) | FU (Hot) | FU (Waste) |
|---------|-----------|----------|------------|
| Water Closet (flush valve) | 10 | 0 | 4 |
| Water Closet (tank) | 2.2 | 0 | 4 |
| Lavatory | 1 | 1 | 1 |
| Kitchen Sink | 1.5 | 1.5 | 2 |
| Mop Sink | 1.5 | 1.5 | 3 |

---

## 10. Site/Paving

### Asphalt Paving
```
Tons = Area (SF) × Thickness (inches) × 110 lbs/CF ÷ (12 × 2000)
Simplified: Tons ≈ Area (SY) × Thickness (inches) × 0.055
```
- Base course: typically 2"-3" thickness
- Surface course: typically 1.5"-2" thickness
- Tack coat: 0.05-0.10 gal/SY

### Aggregate Base
```
CY = Area (SF) × Depth (inches) ÷ 12 ÷ 27
Tons = CY × 1.4 (typical for crusite/DGA)
```
- Typical base depth: 6"-8" for parking, 8"-12" for drives

### Concrete Sidewalk
```
CY = Length × Width × Thickness ÷ 27
```
- Standard: 4" thick, 5' wide
- ADA ramps: 6" thick, per detail

### Curb and Gutter
```
CY = LF × cross-section area (from detail) ÷ 27
```
- Typical 24" combined curb/gutter: ~0.055 CY/LF
- Typical 6" vertical curb: ~0.025 CY/LF

### Stormwater (Rational Method)
```
Q (CFS) = C × I × A
Q (GPM) = Q (CFS) × 448.8
```
- C (runoff coefficient): Roof=0.95, Asphalt=0.85, Concrete=0.90, Grass=0.30
- I (rainfall intensity): per local IDF curves (inches/hour)
- A (drainage area): acres

### Parking Count
```
Required spaces = Building SF ÷ parking ratio
```
- Medical office: 1 per 200 SF (typical)
- Day care: 1 per 8 occupants + 1 per employee (typical)
- ADA spaces: per IBC Table 1106.1
  - 1-25 total: 1 accessible
  - 26-50 total: 2 accessible
  - 51-75 total: 3 accessible

---

## Usage Notes

- All calculations should reference plan-extracted dimensions, NOT assumed values
- Flag calculations where input data is incomplete or unclear
- Round CY up to nearest 0.5 CY for ordering purposes
- Always note waste factors applied
- Cross-reference calculated quantities against any bid/estimate quantities in project data
- Report confidence level: HIGH (all dims from plans), MEDIUM (some assumed), LOW (heavily estimated)
