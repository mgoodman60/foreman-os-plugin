# BIM Field Guide for Superintendents
## Practical BIM for Field Operations

---

## 1. MODEL VIEWER QUICK REFERENCE

### Navigation Controls by Platform

Use these controls to navigate 3D models on your desktop or tablet. All platforms support mouse/trackpad and touch input.

#### Navisworks Freedom (Desktop)

| Action | Mouse | Keyboard Shortcut |
|---|---|---|
| Orbit (rotate view) | Middle-click + drag | Shift + Middle-click |
| Pan (move view) | Middle-click + drag (in pan mode) | Ctrl + Middle-click |
| Zoom | Scroll wheel | + / - keys |
| Zoom to selection | Double-click on element | F key (zoom extents) |
| Section plane | ViewCube > Enable Sectioning | S key (toggle) |
| Measure (point-to-point) | Review tab > Measure > Point to Point | Ctrl + M |
| Select element | Left-click | Esc to deselect |
| Hide selected | Right-click > Hide Selected | H key |
| Unhide all | Right-click > Unhide All | Ctrl + Shift + H |
| Saved viewpoints | Viewpoints panel > double-click | -- |
| Redline markup | Review tab > Redline > select tool | -- |

**Tip**: Use the ViewCube in the upper-right corner to quickly orient to standard views (Top, Front, Right, etc.). Click a face, edge, or corner to snap to that view.

#### Autodesk Docs / BIM 360 (Browser/Mobile)

| Action | Mouse (Browser) | Touch (Tablet/Phone) |
|---|---|---|
| Orbit | Left-click + drag | One finger drag |
| Pan | Right-click + drag or Middle-click + drag | Two finger drag |
| Zoom | Scroll wheel | Pinch in/out |
| Section plane | Section Analysis tool in toolbar | Same (toolbar) |
| Measure | Measure tool in toolbar | Same (toolbar) |
| Select element | Left-click | Tap |
| Properties | Click element > Properties panel | Tap > Properties |
| Markup | Markup tool in toolbar | Same (toolbar) |
| Issues | Issues panel > Pin to location | Same (panel) |
| Model browser | Model browser panel (tree view) | Same (panel) |

**Tip**: Use the "Explode" slider to pull model elements apart and see what is hidden behind other elements. Useful for checking MEP routing in congested areas.

#### Procore BIM (Browser/Mobile)

| Action | Mouse (Browser) | Touch (Tablet/Phone) |
|---|---|---|
| Orbit | Left-click + drag | One finger drag |
| Pan | Right-click + drag | Two finger drag |
| Zoom | Scroll wheel | Pinch in/out |
| Section plane | Section tool in BIM toolbar | Same (toolbar) |
| Measure | Measure tool in BIM toolbar | Same (toolbar) |
| Select element | Left-click | Tap |
| View properties | Click element > info panel | Tap > info panel |
| Create observation | Link to Procore observation workflow | Same |
| Create RFI | Link to Procore RFI workflow | Same |
| Filter by trade | Discipline filter in model browser | Same |

**Tip**: Procore BIM links directly to Procore observations, RFIs, and submittals. You can create an RFI directly from a model viewpoint, which automatically attaches the 3D view.

### General Navigation Tips

- **Start with a plan view** (top-down) to orient yourself, then orbit to 3D
- **Use section planes** to cut through the model and see internal routing
- **Hide disciplines** you are not reviewing to reduce visual clutter
- **Save viewpoints** for important locations you need to revisit
- **Take screenshots** of model views for use in meetings, RFIs, and daily reports
- **Download models for offline use** before going to areas with no connectivity

---

## 2. CLASH REPORT READING GUIDE

### Navisworks Clash Detective Report Format

A typical Navisworks Clash Detective HTML report contains the following for each clash:

```
CLASH REPORT HEADER
-------------------
Test Name:        MEP vs Structural - Level 3
Date Run:         2024-11-15
Tolerance:        0.01 ft (hard clash)
Total Clashes:    142
New:              23
Active:           30
Reviewed:         36
Resolved:         48
Approved:         5

INDIVIDUAL CLASH ENTRY
----------------------
Clash ID:         CLH-MEP-STR-0042
Status:           Active
Date Found:       2024-11-08
Grid Location:    Between C-D / 3-4, Level 3
Elevation:        +38'-6" to +39'-2"

Element 1:        12" Supply Duct (Mechanical)
                  Model: MEP_Combined_v2.4.nwc
                  Layer: HVAC-Supply-Main

Element 2:        W16x40 Steel Beam (Structural)
                  Model: Structural_v2.4.nwc
                  Layer: S-Steel-Beams

Clash Point:      X: 145.32, Y: 87.65, Z: 38.92
Distance:         -0.42 ft (penetration into beam)

Image:            [Viewpoint screenshot showing clash]

Assigned To:      Mechanical Contractor
Description:      12" supply duct passes through W16x40 beam
                  web at grid C-4. Duct must be rerouted above
                  or below beam, or beam penetration sleeve required.
```

### How to Read the Report Efficiently

1. **Start with the summary** -- Total clashes, status breakdown, trend vs. last report
2. **Sort by grid location** -- Focus on areas where your trades are working this week/next week
3. **Sort by status** -- Review "New" clashes first, then "Active" with approaching deadlines
4. **Check assigned party** -- Are your trades responsible? Follow up on their resolution progress
5. **Review images** -- The viewpoint screenshots show exactly where the clash occurs in 3D

### Clash Priority Matrix

Use this matrix to prioritize clash resolution when multiple clashes compete for attention:

| Priority | Category | Definition | Resolution Timeline |
|---|---|---|---|
| **P1 -- Critical** | Safety/Code | Clash violates life safety code (fire separation, egress, electrical clearance) | Resolve before any work proceeds in the area |
| **P2 -- High** | Code Compliance | Clash violates building code but is not life safety (accessibility, energy, plumbing code) | Resolve within 1 week or before trade mobilizes |
| **P3 -- Medium** | Constructability | Clash creates a constructability problem (cannot physically install as modeled) | Resolve before trade reaches the area per schedule |
| **P4 -- Low** | Coordination | Clash is a coordination issue (can be resolved with minor routing adjustment) | Resolve at next coordination meeting |
| **P5 -- Cosmetic** | Aesthetic | Clash affects appearance but not function (ceiling grid alignment, finish conflicts) | Resolve before finishes begin in the area |

### Priority Decision Flow

1. Does it violate life safety code? --> **P1 Critical**
2. Does it violate any code? --> **P2 High**
3. Can it be physically built as modeled? If no --> **P3 Medium**
4. Does it require design input (RFI)? --> **P3 Medium** minimum
5. Can trades resolve it with minor field adjustment? --> **P4 Low**
6. Is it only an appearance issue? --> **P5 Cosmetic**

---

## 3. FIELD MEASUREMENT FOR BIM VERIFICATION

### What to Measure

When verifying installed work against the BIM model, focus on these critical dimensions:

**Ceiling Heights (Above Ceiling MEP)**
- Measure from finished floor to bottom of lowest MEP element
- Compare to model: is there enough ceiling plenum space?
- Check at multiple points along a corridor -- MEP routing changes elevation
- Critical dimension: minimum ceiling height after MEP installation

**Rough Openings**
- Measure width and height of framed openings
- Compare to model: does the opening match the door/window schedule?
- Check diagonal to verify square (difference should be < 1/8" for doors)
- Measure sill height for windows

**Sleeve Locations**
- Measure from nearest grid line or wall to center of sleeve
- Measure elevation from finished floor to center of sleeve
- Verify sleeve diameter against specified pipe/duct size (with clearance)
- Check both sides of penetration (sleeves must align through walls/floors)

**Penetration Offsets**
- Measure from column grid to center of penetration
- Measure from floor to center of penetration
- Verify required clearances from structural elements (per structural engineer requirements)
- Document actual offset vs. modeled offset

### How to Report Field Measurements

Always reference your measurements to fixed project control points:

**Reference Grid System**
- Measure from the nearest column grid intersection (e.g., "24" west of grid line C, 36" north of grid line 4")
- Use the same grid system as the model (verify grid naming matches)
- If grid lines are not accessible, measure from established survey control points

**Elevation Datum**
- Always reference the project elevation datum (e.g., "12'-6" above FFE Level 3")
- Verify your measurement instrument is calibrated to the project datum
- Note whether you are measuring to top, bottom, or center of element

**Measured vs. Modeled Comparison Format**

| Item | Grid Ref | Modeled | Measured | Deviation | Within Tol? |
|---|---|---|---|---|---|
| 12" supply duct CL | C-4, L3 | 12'-6" AFF | 12'-2" AFF | 4" low | No (+/- 1/4") |
| 4" conduit CL | B-3, L2 | 6'-0" from grid B | 6'-1" from grid B | 1" east | Yes (+/- 2") |
| Door opening width | D-5, L1 | 3'-0" | 2'-11-3/4" | 1/4" narrow | Yes (+/- 1/4") |
| Sleeve CL elevation | A-2, L3 | 9'-4" AFF | 9'-3-1/2" AFF | 1/2" low | No (+/- 1/4") |

**Tools for Field Measurement**
- Laser distance meter (Leica DISTO, Bosch GLM): +/- 1/16" accuracy, fast single measurements
- Digital level: elevation checks with high accuracy
- Total station: survey-grade positioning for layout verification
- Tape measure: quick checks, not for tolerance verification on precision elements

---

## 4. COMMON MODEL ISSUES

These are the most frequent problems superintendents encounter when comparing BIM models to field conditions. Knowing these patterns helps you identify issues faster.

### Model Not Georeferenced Correctly
- **Symptom**: Model coordinates do not match survey control points in the field
- **Impact**: Layout from model data lands in the wrong location
- **Detection**: Compare model coordinates at known survey points to field survey
- **Resolution**: BIM team must adjust model to match project control survey; do not adjust field layout to match an incorrectly georeferenced model

### Elements Modeled at Wrong Elevation
- **Symptom**: Ductwork, piping, or conduit shown at one elevation in model but different elevation in the field based on structural constraints
- **Impact**: Trades install at model elevation and conflict with structure or other trades
- **Detection**: Check key MEP elevations at structural intersections before installation begins
- **Resolution**: RFI if elevation was specified incorrectly; coordination fix if model was not updated after a design change

### Ductwork Modeled Without Insulation Clearance
- **Symptom**: Duct centerline and size are correct, but no space for insulation thickness
- **Impact**: Insulated duct conflicts with adjacent elements; ceiling height reduced
- **Detection**: Add insulation thickness to duct dimensions when reviewing model (e.g., 12" duct with 2" insulation = 16" total)
- **Resolution**: Request BIM team model insulation as a separate layer, or manually account for insulation in coordination reviews

### Structural Connections Missing from Model
- **Symptom**: Steel members shown as clean intersections without gusset plates, connection angles, stiffeners, or bolts
- **Impact**: Connection hardware occupies space that is not shown -- creates conflicts with MEP routing near connections
- **Detection**: Review model at steel connections; if connections are LOD 200-300, assume 6-12" additional hardware in each direction
- **Resolution**: Request structural model at LOD 350 minimum for coordination; verify connection geometry from shop drawings

### Pipe Slopes Not Modeled
- **Symptom**: Gravity drain piping shown level in the model
- **Impact**: Actual installed pipe at required slope (1/8" to 1/4" per foot) occupies more vertical space downstream; conflicts emerge where model shows clearance
- **Detection**: Check waste and vent piping in the model for proper slope indication; calculate actual low-point elevation based on run length
- **Resolution**: Insist that gravity drain piping be modeled with actual slopes; use a slope calculation to verify clearance at the low end of each run

### Hangers and Supports Not Modeled
- **Symptom**: MEP elements float in space with no visible supports
- **Impact**: Hanger rods, trapeze supports, strut channels occupy space between the element and the structure above; may conflict with other elements
- **Detection**: When reviewing tight ceiling spaces, add 2-6" above ducts/pipes for hanger clearance
- **Resolution**: Request LOD 350 modeling with supports, or apply standard hanger allowances during coordination

### Ceiling Grid Not Coordinated with MEP
- **Symptom**: Reflected ceiling plan and MEP model do not align -- sprinkler heads, diffusers, light fixtures, and speakers are not centered in ceiling tiles
- **Impact**: Poor aesthetics, potential code violations (sprinkler coverage), rework
- **Detection**: Overlay reflected ceiling plan with MEP model; check device locations vs. ceiling grid
- **Resolution**: Coordination meeting with all ceiling trades (HVAC, electrical, fire protection, architectural) to finalize ceiling device layout

---

## 5. BIM COORDINATION MEETING CHECKLIST

### Pre-Meeting Preparation (Superintendent)

- [ ] Review current clash report -- note new clashes in your work areas
- [ ] Check status of previously assigned action items
- [ ] Walk the active coordination areas -- note any field conditions affecting the model
- [ ] Review the 3-week look-ahead -- identify upcoming areas needing coordination priority
- [ ] Gather field deviation logs from the past week
- [ ] Confirm model version matches the version being discussed

### Meeting Agenda Template

**BIM Coordination Meeting**
**Date**: ___________  **Time**: ___________  **Location**: ___________

| # | Topic | Duration | Lead |
|---|---|---|---|
| 1 | Model updates since last meeting (new uploads, version changes) | 5 min | BIM Manager |
| 2 | New clash report review (summary, trends, new critical items) | 5 min | BIM Manager |
| 3 | Previously assigned clash resolution -- status check | 10 min | All trades |
| 4 | Walk-through of priority clashes by area (3D model on screen) | 20 min | BIM Manager + Super |
| 5 | Upcoming work areas needing pre-clash review | 5 min | Superintendent |
| 6 | RFI status for design-related clashes | 5 min | Project Engineer |
| 7 | Field deviation report -- items affecting model accuracy | 5 min | Superintendent |
| 8 | Action items, assignments, due dates | 5 min | All |

**Total Duration**: 60 minutes

### Post-Meeting Actions (Superintendent)

- [ ] Distribute meeting minutes with action items within 24 hours
- [ ] Update bim-log.json coordination_meetings entry
- [ ] Follow up with trade foremen on their assigned clash resolutions
- [ ] Schedule any required field walks to resolve spatial conflicts
- [ ] Update look-ahead planner with coordination dependencies
- [ ] Submit RFIs identified during the meeting

---

## 6. LOD QUICK REFERENCE TABLE

### LOD by Discipline -- What You See at Each Level

#### Architectural Elements

| LOD | Walls | Doors | Windows | Ceilings | Floors |
|---|---|---|---|---|---|
| 100 | Outline only | Not shown | Not shown | Not shown | Outline only |
| 200 | Generic thickness | Generic swing | Generic opening | Generic height | Generic assembly |
| 300 | Specific assembly | Specific type/size | Specific type/size | Specific type/height | Specific assembly |
| 350 | Framing, GWB layers | Hardware, frame | Frame, sill, hardware | Grid, suspension | Layers, transitions |
| 400 | Stud layout, fasteners | Exact hardware | Exact glazing detail | Tile layout | Substrate, adhesive |
| 500 | As-built verified | As-built verified | As-built verified | As-built verified | As-built verified |

#### Structural Elements

| LOD | Columns | Beams | Slabs | Foundations | Connections |
|---|---|---|---|---|---|
| 100 | Vertical line | Horizontal line | Flat plane | Not shown | Not shown |
| 200 | Generic shape | Generic shape | Generic depth | Generic outline | Not shown |
| 300 | Specific member | Specific member | Specific depth/rebar zones | Specific dims | Generic |
| 350 | Stiffeners, plates | Copes, holes | Embeds, rebar | Anchor bolts, dowels | Plates, bolts |
| 400 | Erection aids | Camber, shims | Pour joints, rebar detail | Waterproofing | Weld details |
| 500 | As-built verified | As-built verified | As-built verified | As-built verified | As-built verified |

#### MEP Elements

| LOD | Ductwork | Piping | Conduit/Cable Tray | Equipment | Fixtures |
|---|---|---|---|---|---|
| 100 | Schematic line | Schematic line | Not shown | Placeholder block | Not shown |
| 200 | Generic size/route | Generic size/route | Generic route | Generic dims | Generic location |
| 300 | Specific size/fittings | Specific size/fittings | Specific sizes | Manufacturer dims | Specific type |
| 350 | Hangers, insulation | Hangers, insulation, valves | Supports, boxes | Connections, clearances | Rough-in dims |
| 400 | Fabrication spools | Fabrication spools | Pull boxes, detail | Vibration isolation | Carrier detail |
| 500 | As-built verified | As-built verified | As-built verified | As-built verified | As-built verified |

### Quick LOD Identification in the Field

When reviewing a model, quickly determine the LOD by asking:
- **Can I see connections and supports?** If yes: LOD 350+
- **Can I see specific manufacturer dimensions?** If yes: LOD 300+
- **Is everything generic shapes?** LOD 200
- **Just boxes and lines?** LOD 100

---

## 7. AR/MIXED REALITY FIELD TOOLS

### Current Tools for Field Overlay

| Tool | Platform | BIM Formats | Key Feature | Cost |
|---|---|---|---|---|
| Dalux BIM Viewer | iOS, Android | IFC, RVT, NWD | AR overlay, QA checklists | Subscription |
| Trimble Connect | iOS, Android, HoloLens | IFC, SKP, DWG | AR + mixed reality | Subscription |
| OpenSpace | iOS, Android (360 camera) | IFC integration | 360 capture + BIM compare | Subscription |
| HoloBuilder | iOS, Android (360 camera) | IFC integration | Job walk capture + overlay | Subscription |
| Resolve | HoloLens, iOS | RVT, NWD, IFC | Full-scale holographic BIM | Enterprise |
| XYZ Reality HoloSite | HoloLens | RVT, IFC | Real-time layout verification | Enterprise |

### Setup Requirements for AR Field Use

1. **Model preparation**: Export model to IFC or supported format; optimize for mobile (reduce unnecessary detail)
2. **Coordinate calibration**: Establish at least 3 known reference points visible to both the device and marked in the model
3. **Device requirements**: Modern smartphone/tablet with LiDAR sensor preferred (iPad Pro, iPhone Pro); older devices work but with lower accuracy
4. **Lighting**: Camera-based AR requires adequate lighting; does not work in dark spaces without supplemental light
5. **Connectivity**: Download model for offline use before going to field; real-time streaming requires strong WiFi or cellular

### Accuracy Considerations

| Method | Typical Accuracy | Best For |
|---|---|---|
| Phone/tablet AR (no LiDAR) | +/- 2-4" | Visual conflict check, general routing verification |
| Phone/tablet AR (with LiDAR) | +/- 1-2" | Rough-in verification, ceiling plenum review |
| HoloLens mixed reality | +/- 1/2-1" | Detailed coordination, layout verification |
| Dedicated AR layout (HoloSite) | +/- 1/4" | Precision layout, tolerance verification |

**Bottom line**: Use mobile AR for "does this look right?" checks and dedicated hardware for "is this within tolerance?" verification.

---

## 8. SCAN-TO-BIM VERIFICATION CHECKLIST

### Pre-Scan Preparation

- [ ] Define scan scope: what areas, what elements, what tolerances
- [ ] Confirm model version is current (as-designed or last coordinated version)
- [ ] Coordinate scan timing: ensure work in the area is complete and accessible
- [ ] Establish survey control: minimum 3 control points visible to scanner and tied to project coordinates
- [ ] Clear obstructions: remove temporary items that would clutter the scan (trash, scaffolding if possible, stored materials)
- [ ] Notify trades: scanning crew needs unobstructed access; no active work in scan zone during capture
- [ ] Confirm deliverable requirements: point cloud format, deviation map, as-built overlay
- [ ] Check environmental conditions: dust, rain, or extreme temperatures can affect scan quality

### Scanner Placement (Terrestrial)

- [ ] Plan scan positions to cover all surfaces of interest with adequate overlap
- [ ] Typical spacing: 30-50 feet between positions for interior scans
- [ ] Ensure line of sight from each position to at least 2 control targets
- [ ] Place targets (checkerboard or sphere) at control points before scanning
- [ ] Capture reference photos from each scan position for registration verification
- [ ] Minimum of 3 scan positions per room/area for full coverage

### Registration Quality Check

After the scanning crew registers (aligns) the individual scans:

- [ ] Registration error should be < 1/4" (6mm) for MEP verification scans
- [ ] Check control point residuals: each point should align within 1/8" of known coordinates
- [ ] Visually inspect registered point cloud for "ghosting" (misaligned duplicate surfaces)
- [ ] Verify coordinate system matches the project BIM coordinate system
- [ ] Confirm elevation datum alignment (check a known floor elevation)

### Deviation Analysis Review

When reviewing the scan-to-BIM deviation report:

- [ ] Understand the color scale: typically blue (within tolerance) to red (exceeds tolerance)
- [ ] Focus on areas where deviations exceed specified tolerances
- [ ] Distinguish between real deviations and scan artifacts (temporary items, people, noise)
- [ ] Check elements flagged as missing: are they not installed yet, or actually missing?
- [ ] Verify critical dimensions: ceiling heights, clearances, rough opening sizes
- [ ] Cross-reference deviations with clash report: does a field deviation create a new clash?

### Deliverable Review Checklist

- [ ] Point cloud file received in specified format (E57, RCP, LAS)
- [ ] Point cloud is georeferenced to project coordinate system
- [ ] Deviation map/report received (PDF or HTML)
- [ ] Deviation map includes element-by-element analysis for specified tolerances
- [ ] As-built overlay file received (NWD or IFC) for viewing alongside the model
- [ ] Cross-sections provided at specified locations (if requested)
- [ ] Summary statistics: total elements checked, percentage within tolerance, maximum deviation
- [ ] Recommendations for out-of-tolerance items included in report
- [ ] All deliverables linked/filed in project CDE (Autodesk Docs, Procore, etc.)
