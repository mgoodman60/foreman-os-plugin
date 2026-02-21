# Construction Surveying Guide
## Superintendent's Reference — Layout Verification, Grade Control, and Survey Management

---

## 1. BENCHMARK ESTABLISHMENT AND MAINTENANCE

### What Benchmarks Are
A benchmark (BM) is a permanent reference point with a known, fixed elevation. All vertical measurements on the project are derived from benchmarks. If your benchmark is wrong, every elevation on the project is wrong.

### Primary Benchmark
- **Established by a registered/licensed surveyor** — Tied to NAVD88 (North American Vertical Datum of 1988) or local project datum as specified in contract documents
- **Located off-site or at project perimeter** — Must be outside the construction disturbance zone
- **Permanent monument** — Brass disk in concrete, iron rod, or existing structure (top of hydrant, manhole rim, etc.)
- **Elevation certified** — Surveyor provides written certification with datum reference, date, accuracy

### Secondary Benchmarks (Project Control Points)
- **Set by surveyor from primary benchmark** — Minimum 2 secondary benchmarks on-site, 3 preferred
- **Located for daily use** — Visible from most work areas, on stable ground, accessible for instrument setup
- **Protected from construction damage** — Offset from traffic, flagged, and marked clearly. Photograph location and reference to permanent features.
- **Typical markers:** Rebar with cap driven to stable depth, PK nail in pavement, chiseled "X" on concrete, hub and tack

### Benchmark Protection
1. Flag with lath and ribbon — bright colors, visible from 100+ feet
2. Install protective barrier if near traffic (T-posts and ribbon, concrete-filled tire around hub)
3. Photograph location with reference to two permanent features (building corner, utility pole, etc.)
4. Add to site logistics plan — mark on drawings distributed to all trades
5. Include in subcontractor orientation — "Do not disturb survey points"

### Verification Schedule
| Trigger | Action |
|---------|--------|
| Monthly (minimum) | Level loop between all benchmarks. All should match within ±0.01 foot. |
| After nearby excavation | Check benchmarks within 50 feet of excavation. Settlement or displacement possible. |
| After grading operations | Verify benchmarks near graded areas. Equipment traffic can shift hubs. |
| After blasting within 500 feet | Check ALL benchmarks on-site. Vibration can shift monuments. |
| After heavy rain/flooding | Check benchmarks near drainage areas. Erosion or soil movement possible. |
| When survey data doesn't match | STOP work. Check benchmarks first — most field errors trace back to benchmark issues. |

### Benchmark Documentation Log
For each benchmark, record:
- **BM designation** (BM-1, BM-2, etc.)
- **Elevation** (to 0.001 foot)
- **Datum reference** (NAVD88, local, assumed)
- **Date set**
- **Set by** (surveyor name, company, license number)
- **Location description** (with reference distances to two permanent features)
- **Photograph** (date-stamped)
- **Verification dates and results** (running log)

---

## 2. CONTROL POINT NETWORK

### Primary Control
- **Established by licensed surveyor** — Horizontal (X, Y) and vertical (Z) coordinates
- **Minimum 3 points** — Visible from all areas of the project. 3 is minimum; 4-6 preferred for large sites.
- **Tied to project coordinate system** — State Plane, local grid, or assumed coordinates per contract
- **Monumented** — Permanent markers with clear identification (tagged rebar, brass disk, PK nail)
- **Documentation** — Survey report with coordinates, datum, date, accuracy statement, adjustment method

### Secondary Control
- **Set by field crew from primary control** — Used for daily layout operations
- **Closer to work areas** — Reduces instrument setup time and line-of-sight issues
- **Spacing:** 200-500 feet typical for building projects, closer for complex structures, wider for site/earthwork

### Grid vs. Bearing Systems
- **Grid system (State Plane)** — Large sites, projects tied to public infrastructure. Grid north differs from true north by a convergence angle.
- **Assumed bearing system** — Common on building projects. Baseline established, all bearings referenced to it. Simpler but not tied to external reference.
- **Know which system your project uses** — Mixing grid and bearing coordinates is a common and costly error

### Control Point Verification
- **Close the loop** — Survey from Point A to B to C and back to A. Closure error must be within tolerance.
- **Building projects:** Closure within 1/10,000 minimum (1 foot error per 10,000 feet of traverse)
- **Site/earthwork:** Closure within 1/5,000 acceptable for most grading work
- **Interior/precision work:** Closure within 1/20,000 or better for elevator shafts, curtain wall, tolerance-critical work

### Re-establishment Procedure When Control Point Is Disturbed
1. **STOP layout operations** — Do not use remaining points until verified
2. **Notify surveyor immediately** — Request emergency re-establishment
3. **Verify remaining points** — Surveyor checks undisturbed points against each other
4. **Re-set disturbed point** — Surveyor establishes new point from verified control
5. **Verify recent work** — Any layout done since last verification of the disturbed point must be field-checked
6. **Document** — Record what happened, when discovered, what was re-checked, any corrections made

---

## 3. SURVEY EQUIPMENT OVERVIEW

### Equipment Comparison

| Equipment | Measures | Typical Accuracy | Best For | Limitations |
|-----------|----------|-----------------|----------|-------------|
| Total station | Angles + distances | ±2mm + 2ppm | Building layout, staking, as-builts | Requires line of sight, 2-person operation (unless robotic) |
| Robotic total station | Angles + distances | ±2mm + 2ppm | One-person layout, tracking | Expensive, complex, still needs line of sight |
| Auto/optical level | Elevation only | ±1.5mm per km | Grade checks, benchmark transfer | No horizontal measurement, requires rod person |
| Digital level | Elevation only | ±0.3mm per km | Precision elevation, floor flatness | More expensive than optical, same limitations |
| Rotary laser level | Elevation (plane) | ±1/16" at 100' | Interior ceiling grids, form checks | Limited range, no documentation, general reference only |
| GPS/RTK | 3D position | ±1" horiz, ±2" vert | Large site layout, earthwork, topo | Requires satellite visibility (no indoor, limited urban canyon), less precise vertically |
| Pipe laser | Line and grade | ±1/16" at 200' | Pipe installation, tunnel alignment | Single alignment only |

### Task-to-Equipment Guide

| Task | Best Equipment | Notes |
|------|---------------|-------|
| Building corner layout | Total station or robotic | From primary control, check diagonals |
| Foundation form check | Total station + optical level | Horizontal position + elevation |
| Column anchor bolt layout | Total station | Precision layout from control |
| Floor elevation check | Optical level or digital level | Level loop from benchmark |
| Rough grading | GPS/RTK | Fast, covers large areas |
| Fine grading | GPS/RTK or optical level | Level for final verification |
| Interior wall layout | Total station or robotic | From interior control points |
| Pipe invert layout | Pipe laser + optical level | Laser for line, level for grade verification |
| Ceiling grid layout | Rotary laser | Quick reference, verify with level |
| As-built underground | Total station | Before backfill, precise location required |

---

## 4. LAYOUT PROCEDURES

### Building Layout from Control
1. **Set up total station on control point** — Level instrument, enter station coordinates
2. **Backsight to second control point** — Verify angle and distance match known values (within ±0.01' distance, ±5" angle)
3. **Calculate and stake building corners** — Turn angles and measure distances from control to each corner
4. **Check diagonals** — Measure corner-to-corner diagonals. Opposite diagonals should match within ±1/4" for building layout. If diagonals don't match, a corner is wrong.
5. **Establish offset stakes** — Set stakes 5-10 feet from building lines, outside excavation/foundation zone
6. **Reference offset stakes** — Mark each stake with distance and direction to building line (e.g., "5.00' N to N building line")

### Foundation Layout
1. **Batter boards** — Set 4-6 feet outside footing lines, at elevation allowing string line at top-of-footing or top-of-wall
2. **String lines** — Stretch between batter boards to mark center of footing, edge of footing, edge of wall
3. **Verify layout** — Check all dimensions against foundation plan, check diagonals, check elevations
4. **Mark forms** — Transfer string line locations to form work with keel/lumber crayon
5. **Pier/column locations** — Mark center point on forms, verify offset from building lines matches plans

### Interior Layout
1. **Establish interior control** — Transfer at least 2 control points inside the structure (through openings, with instrument)
2. **Snap chalk lines** — From established control, snap lines for:
   - Partition wall faces (specify which face — stud side or finish side)
   - Door/window openings (mark header height on adjacent walls)
   - Plumbing rough-in centerlines
   - Electrical panel locations
3. **Verify dimensions** — Spot-check room dimensions, corridor widths, door locations against plans
4. **Mark elevations** — Shoot finish floor elevation at multiple points, mark reference elevation (typically 4'-0" above FF) on columns/walls for MEP coordination

### Column Layout for Steel
1. **Establish column grid lines** — Snap chalk lines on foundation for column centerlines in both directions
2. **Anchor bolt template** — Use manufacturer's template, align to grid intersections, verify bolt spacing, edge distances, and pattern orientation
3. **Embed plate placement** — Set plates level to design elevation ±1/8" using shim stacks or leveling nuts
4. **Mark centerlines on forms** — Permanent marks on form edges at grid intersections for verification after pour
5. **Pre-pour verification** — Check all anchor bolt locations against erection drawings BEFORE concrete placement. Moving anchor bolts after concrete = expensive, delays steel erection.

---

## 5. STAKING PROCEDURES

### Offset Stakes
- **Purpose:** Mark positions outside the construction disturbance area so work reference is not destroyed during construction
- **Typical offset:** 5-10 feet from edge of work (footing edge, curb line, pipe trench)
- **Marking:** Lath or hub with tack, labeled with:
  - Station or grid reference
  - Offset distance and direction to work point
  - Cut or fill to design elevation (if applicable)

### Grade Stakes

| Stake Marking | Meaning | Example |
|---------------|---------|---------|
| C 2.5 | Cut 2.5 feet | Existing ground is 2.5' above design grade |
| F 1.0 | Fill 1.0 foot | Existing ground is 1.0' below design grade |
| Grade | On grade | Existing matches design (within tolerance) |
| FS 102.50 | Finish surface elevation | Design elevation at this point is 102.50 |

- **Color coding** (common convention):
  - **Red/pink flagging** — Property/boundary lines
  - **Blue flagging** — Water lines
  - **Green flagging** — Sewer lines
  - **Orange flagging** — Communication/cable
  - **Yellow flagging** — Gas lines
  - **White flagging** — Proposed excavation

### Slope Stakes
- Mark the **catch point** — where the designed slope intersects existing ground
- Labeled with slope ratio (e.g., 2:1, 3:1) and offset from centerline
- Set at top and bottom of designed slopes
- Critical for earthwork pay quantity calculations — get these right

### Blue Tops
- **Grade-set stakes driven flush with finished grade** — Top of stake = design elevation
- Used for fine grading verification, typically on 25-50 foot grid
- Grading contractor grades between blue tops, superintendent spot-checks with level
- Faster than checking every point with instrument — visual reference for equipment operator

### Documentation
- **Survey field book** — Date, crew, equipment, weather, points set, point descriptions
- **Staking request log** — Date requested, area/scope, date completed, surveyor name
- **Staking completion log** — Date staked, area, point list, verification method, superintendent signature

---

## 6. ELEVATION VERIFICATION

### When to Verify Elevations
- **Before every concrete placement** — Forms set to correct elevation? Embeds at correct depth?
- **Before compaction approval** — Subgrade/base course at design elevation?
- **Before pipe installation** — Trench bottom at correct invert elevation?
- **After grading operations** — Finished surface within tolerance?
- **Before structural steel erection** — Bearing elevations correct?
- **At floor-to-floor transitions** — Elevator shaft, stair landings, slab steps

### Cut/Fill Calculation
**Design Elevation - Existing Elevation = Cut or Fill**
- Positive result = CUT (existing ground is higher than design, remove material)
- Negative result = FILL (existing ground is lower than design, add material)
- Example: Design = 100.00, Existing = 102.50, Difference = -2.50 = Cut 2.50 feet

### Grade Tolerance by Application

| Application | Tolerance | Notes |
|-------------|-----------|-------|
| Rough earthwork | ±0.10 foot (±1-1/4") | Bulk cut/fill, stockpile areas |
| Building pad/subgrade | ±0.05 foot (±5/8") | Before aggregate base or slab |
| Aggregate base course | ±0.05 foot (±5/8") | Verify after compaction |
| Concrete forms (slab on grade) | ±1/4" | Check at pour strips, edges, interior |
| Concrete forms (elevated deck) | ±1/4" | Check soffit and top of form |
| Fine grading (landscape) | ±0.05 foot (±5/8") | Verify positive drainage |
| Fine grading (pavement) | ±0.02 foot (±1/4") | Critical for drainage, flatness |
| Structural steel bearing | ±1/8" | Per AISC tolerances |
| Elevator shaft | ±1/4" per floor | Cumulative tolerance critical |
| Floor flatness (FF/FL) | Per spec (FF25/FL20 min typical) | F-number system, check with floor profiler |

### Level Loop Procedure (How to Shoot Grade)
1. **Set up level** — Midway between benchmark and point to check (minimize error)
2. **Backsight (BS)** — Read rod on benchmark. Record reading.
3. **Height of Instrument (HI)** = Benchmark Elevation + Backsight Reading
4. **Foresight (FS)** — Read rod on point to check. Record reading.
5. **Point Elevation** = HI - Foresight Reading
6. **ALWAYS close back to benchmark** — Final foresight on BM must reproduce known elevation within ±0.01' for building work, ±0.05' for earthwork. If it doesn't close, the loop has an error — do NOT use the data.

### Level Loop Example
- BM-1 Elevation = 100.000'
- BS on BM-1 = 5.230' --> HI = 105.230'
- FS on Point A = 3.120' --> Point A Elevation = 102.110'
- FS on Point B = 6.450' --> Point B Elevation = 98.780'
- Close FS on BM-1 = 5.230' --> Check: 105.230 - 5.230 = 100.000' (Closes. Data is good.)

---

## 7. SUPERINTENDENT'S SURVEY RESPONSIBILITIES

### Your Role: Verify and Manage (You Don't Survey)
You are not a surveyor. You manage the survey process, verify results, and ensure layout supports the construction schedule. A superintendent who tries to do their own layout invites liability, errors, and re-work.

### Ordering Surveys — Lead Time
| Survey Type | Typical Lead Time | Notes |
|-------------|------------------|-------|
| Initial site control | 2-4 weeks | Schedule during mobilization planning |
| Building layout | 48-72 hours | After rough grade complete, before foundations |
| Foundation verification | 24-48 hours | Before concrete placement |
| As-built underground | Same day | MUST be before backfill — schedule with dig crew |
| Floor elevation check | 24-48 hours | Before and after concrete placement |
| Property line verification | 1-2 weeks | Registered surveyor required |
| Topographic survey | 1-2 weeks | For pay quantity verification, earthwork |

### When to Request a Survey
- Before foundation concrete placement (verify forms)
- After grading operations (verify grades, calculate quantities)
- After utility installation and before backfill (as-built — CRITICAL)
- When layout appears incorrect or dimensions don't work
- At control point verification intervals (monthly minimum)
- Before structural steel erection (bearing elevations)
- When owner/architect requests field verification
- When a dispute arises about dimensions or locations

### Checking Survey Work (Superintendent Spot-Checks)
You don't need a surveyor's instrument to catch major errors:
1. **Tape check** — Measure between staked points with steel tape. Compare to plan dimensions. Should match within ±1/4" for building layout.
2. **Diagonal check** — Measure diagonals of rectangular layouts. Should be equal within ±1/4". Unequal diagonals = layout is not square.
3. **Visual alignment** — Sight along staked lines. Points should align visually. Obvious bows or offsets indicate an error.
4. **Dimension chain** — Add up individual room/bay dimensions from layout. Total should match overall building dimension on plans.
5. **Common sense check** — Do the staked points make sense with site features, adjacent structures, property lines? Does the building "fit" on the site as shown on the site plan?

### Resolving Survey Conflicts
When field measurements don't match plans:
1. **STOP work in the affected area** — Do not proceed until resolved
2. **Document the discrepancy** — Measure and record what you found vs. what the plans show
3. **Notify the engineer/architect** — RFI or phone call, depending on urgency
4. **Request resolution before proceeding** — Get written direction (ASI, RFI response, revised drawing)
5. **NEVER adjust the structure to fit incorrect survey** — Fix the survey, not the building
6. **NEVER adjust the survey to fit incorrect plans** — Get the plans corrected

### Common Surveyor-Superintendent Coordination Issues
- **Wrong datum** — Surveyor using different benchmark than plans reference. Verify datum before any work begins.
- **Plan vs. field conflict** — Dimensions on plan don't match what fits on site. Usually a plan error — get it resolved via RFI.
- **Grid vs. bearing confusion** — Surveyor using State Plane, plans use project grid (or vice versa). Confirm coordinate system at project start.
- **Dimension to what?** — Face of concrete, centerline of wall, face of finish? Clarify dimensioning basis with architect before layout.

---

## 8. COMMON SURVEYING ERRORS

### Sources of Error and Field Corrections

| Error Source | Magnitude | Prevention |
|--------------|-----------|------------|
| Wrong benchmark | Unlimited — everything off | Verify BM designation and elevation before every setup |
| Instrument not level | Increases with distance | Check bubble before and during readings, re-level if bumped |
| Temperature effect on steel tape | 1/8" per 100' per 15degF change from 68degF standard | Use tension handle (apply standard pull), apply temperature correction for precision work |
| Transposing numbers | Common — costly | Read back all numbers, double-check field book entries |
| Reading rod incorrectly | 0.01-1.0 foot | Rod person verifies reading, use digital level for critical work |
| Atmospheric refraction | Significant on long sights over hot surfaces | Keep sight distances short (<300'), avoid sights over pavement in afternoon heat |
| Rod not plumb | Increases with elevation read | Use rod level (bulls-eye level on rod), rock rod and read lowest value |
| Settlement of instrument | Progressive through survey | Re-check backsight periodically, close loops frequently |
| Sag in steel tape | 0.01-0.03' per 100' | Support tape at intervals, or apply sag correction |
| Wind deflection of rod | Variable | Shield rod from wind, wait for lulls on windy days |

### Field Correction Best Practices
1. **Always take redundant measurements** — Measure everything twice, from different setups if possible
2. **Close all loops** — Return to starting benchmark or control point. Closure error reveals problems.
3. **Check against known dimensions** — Measure building features shown on plans (bay spacing, column grid dimensions) as independent verification
4. **Reject outliers** — If one measurement disagrees with several others, re-measure it — do not average an error into your data
5. **Document everything** — Field book entries with date, crew, conditions, equipment serial number. If it is not written down, it did not happen.

### Red Flags That Survey Work May Be Wrong
- Dimensions don't add up (individual bays/rooms don't total to overall dimension)
- Building doesn't "fit" on site as expected from site plan
- Diagonals of rectangular layout are not equal
- Elevation check doesn't close back to benchmark
- Adjacent structure alignment appears off
- Subcontractor reports dimensions don't match their shop drawings
- Surveyor seems rushed, doesn't close loops, doesn't check work

---

## 9. AS-BUILT SURVEY REQUIREMENTS

### What Needs As-Built Survey
| Item | Priority | Timing |
|------|----------|--------|
| Sanitary sewer (pipe and manholes) | CRITICAL | Before backfill — same day as installation |
| Storm drain (pipe, inlets, manholes) | CRITICAL | Before backfill — same day as installation |
| Domestic water lines | CRITICAL | Before backfill — same day as installation |
| Fire water lines | CRITICAL | Before backfill — same day as installation |
| Gas lines | CRITICAL | Before backfill — same day as installation |
| Electrical ductbank | CRITICAL | Before backfill — same day as installation |
| Communication conduit | HIGH | Before backfill |
| Foundation actual locations | HIGH | After form strip, before backfill |
| Floor elevations (each level) | HIGH | After concrete cure, before framing |
| Structural member locations | MODERATE | When tolerance questions arise |
| Site grading final surfaces | HIGH | After fine grading, before paving/landscape |
| Curb and gutter | MODERATE | After placement |
| Paving finished grades | MODERATE | After paving |

### As-Built Survey Content (What Gets Recorded)
For each as-built feature:
- **Actual coordinates** (X, Y) — Horizontal location of key points (pipe ends, manholes, bends, tees, valves)
- **Actual elevations** (Z) — Invert elevations for pipes, rim elevations for manholes, top of foundation, finished floor
- **Pipe material, size, type** — Verify against plans and mark any deviations
- **Date of installation** — For record and warranty tracking
- **Surveyor name and certification** — Licensed surveyor for formal as-builts

### Underground As-Built Timing — CRITICAL
**Underground as-builts MUST be completed before backfill.**
- Once buried, survey requires excavation to verify — expensive and disruptive
- Schedule surveyor concurrent with underground crews
- Field superintendent coordinates: "Do not backfill until surveyor completes as-built shots"
- If surveyor is delayed, protect the trench (barricade, cover) — do NOT backfill to maintain schedule
- Some jurisdictions and inspectors will not approve underground installations without as-built survey documentation

### As-Built vs. Record Drawing
- **As-built survey** — Field-measured actual locations and elevations by a surveyor. Factual data.
- **Record drawing** — Contract drawing marked up with actual conditions, changes, deviations. Prepared by contractor, reviewed by engineer. Based on as-built survey data plus field notes.
- The superintendent is responsible for providing accurate field information for record drawings. As-built surveys provide the precise data underlying those markups.

### As-Built Documentation Package
Maintain a running file:
1. As-built survey data sheets (from surveyor)
2. Surveyor's signed and sealed plat/map (for underground utilities)
3. Photographs of utilities before backfill (with reference measurements visible)
4. Deviation log (where actual differs from plan — note RFI/ASI numbers authorizing changes)
5. Inspector sign-off sheets (jurisdictional inspections tied to as-built data)

---

## QUICK REFERENCE — SUPERINTENDENT'S SURVEY CHECKLIST

**Project Start:**
- [ ] Confirm datum (horizontal and vertical) matches contract documents
- [ ] Verify primary benchmark location, elevation, and datum tie
- [ ] Confirm coordinate system (State Plane, local grid, assumed)
- [ ] Establish minimum 3 secondary benchmarks on-site
- [ ] Photograph and log all benchmark/control point locations
- [ ] Distribute control point locations to all subcontractors

**Weekly/Ongoing:**
- [ ] Protect survey control points from construction damage
- [ ] Schedule survey support 48-72 hours in advance
- [ ] Spot-check layout with tape, diagonal, and visual methods
- [ ] Coordinate as-built surveys with underground installation schedule

**Monthly:**
- [ ] Verify benchmarks against each other (level loop)
- [ ] Review survey request/completion log — any outstanding items?
- [ ] Update as-built documentation file

**Before Concrete/Backfill:**
- [ ] Confirm layout survey is complete and verified
- [ ] Confirm elevation checks are within tolerance
- [ ] Confirm as-built survey is complete (underground only)
- [ ] Resolve any survey discrepancies BEFORE placing concrete or backfilling
