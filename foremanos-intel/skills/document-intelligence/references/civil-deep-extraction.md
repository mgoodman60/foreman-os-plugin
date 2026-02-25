# Civil & Site - Deep Extraction Guide

Extract exact values for utilities, grading, and paving from civil/site drawings.

## Storm Drainage - Extract Pipe Data

For each pipe run:
- **Material**: RCP, HDPE, PVC, CMP
- **Diameter**: 12", 18", 24", 30"
- **Length**: Station to station
- **Slope**: % (e.g., "0.50%", "1.00%")
- **Invert IN**: Elevation at upstream structure
- **Invert OUT**: Elevation at downstream structure
- **Rim**: Manhole/inlet rim elevation

**Example**:
```
SD-1 to SD-2: 12" RCP, 50' long, 1.0% slope
  At SD-1: Inv OUT = 844.50', Rim = 856.20'
  At SD-2: Inv IN = 844.00', Rim = 855.80'
```

## Grading - Extract Spot Elevations

- **FFE**: Finished Floor Elevation (e.g., "856.50'")
- **Building corners**: Proposed grades
- **Entries**: Entrance elevations
- **Parking**: High/low points
- **Slopes**: %, direction of drainage

**Example**:
```
FFE = 856.50'
NW corner = 855.00' (proposed)
SE corner = 854.20' (proposed)
Main entry = 856.30'
Parking slope = 2% toward storm drains
```

## Paving Sections

**Asphalt**:
- Binder course thickness (e.g., "2.5\" binder")
- Surface course thickness (e.g., "1.5\" surface")
- Total asphalt thickness

**Aggregate Base**:
- Material (e.g., "#57 stone", "21-A")
- Thickness (e.g., "6\" compacted")
- Compaction (e.g., "98% modified proctor")

**Subgrade**:
- Compaction (e.g., "95% modified proctor")

**Example**:
```
Asphalt Pavement Section:
- 1.5" surface course (Type S5 mix)
- 2.5" binder course (Type I-2 mix)
- 6" aggregate base (#57 stone, 98% compaction)
- Subgrade (95% modified proctor)
Total thickness: 10" (4" asphalt + 6" base)
```

## Sanitary Sewer System

**Pipe Materials & Selection**:
- **PVC SDR-35**: Most common for 4"–8" laterals and building sewers. Lightweight, corrosion-resistant, quick to install. Check for ASTM D3034 rating.
- **DIP (Ductile Iron Pipe)**: Larger mains (8"–24"+), high-pressure zones, corrosive soil conditions. Heavier but extremely durable.
- **HDPE (High-Density Polyethylene)**: Trenchless applications, areas with settling. Flexible, good for difficult access. Less common than PVC for gravity systems.

**Pipe Sizes by Use**:
- **4" lateral**: From cleanout/building to main line. Minimum for residential.
- **6" building sewer**: From building to property line or main. Standard residential size.
- **8"+ main**: Collector lines, trunk sewers. Size depends on flow calculations shown on plan.

**Slope Requirements** (critical for function):
- **4" pipe**: 1/4" per foot minimum (2.08% slope). Steeper is acceptable.
- **6" pipe and larger**: 1/8" per foot minimum (1.04% slope). Main lines often 0.5%–1.0%.
- **Note**: Insufficient slope causes solids backup; excessive slope (>5%) causes scouring. Always confirm slope on profile.

**Invert Elevations** (marked on plan and profile):
- **Invert IN**: Water surface elevation entering a structure (manhole, catch basin). Read from upstream pipe.
- **Invert OUT**: Water surface elevation leaving a structure. Read from downstream pipe.
- **Structure depth**: Rim elevation minus invert OUT = depth to flow line.
- **Example**: MH-3 Rim 852.50', Invert IN 844.75', Invert OUT 844.50' (0.25' drop through structure).

**Manhole Details**:
- **Rim elevation**: Top of casting, used for surface survey tie-in. Mark clearly during excavation.
- **Shelf**: Sloped benching inside manhole where pipes enter. Directs incoming flow toward outgoing pipe.
- **Channel**: Formed concrete chute at base from inlet to outlet pipe. Guides solids, prevents dead zones.
- **Drop manhole**: Used where incoming pipe is >2' higher than outgoing. Includes internal drop pipe or baffle to dissipate energy.
- **Diameter**: Typically 4' for access; check plans for special sizes (3' or 6' for high-flow lines).

**Cleanout Locations & Spacing**:
- **Maximum spacing**: 100'–150' apart (check local code; some jurisdictions specify 75'). Prevents blockage sections.
- **Installed at**: Changes in grade, alignment, pipe size, or elevation. Always before the main line.
- **Type**: Wye fittings with caps above grade, or plugged tees inside structures.
- **Access**: Marked on final survey; must be accessible for cleaning equipment (jetting, rodding).

**Service Connections**:
- **Tap location**: Marked on main line, typically 3 o'clock position for gravity flow. Confirm on profile/plan.
- **Saddle type**: Cast iron or PVC clamp saddle (4"–6" lateral) or direct tee in main line (if already exposed during construction).
- **Backfill**: Density critical around new taps. Use sand/gravel, compact in lifts. Do not pile backfill against fresh concrete.
- **Lateral slope**: Same rules as mains (1/4" per foot for 4", 1/8" for 6"+). Slope must run toward main.

**Grease Traps & Interceptors**:
- **Grease trap**: Small device (residential kitchen, single sink). Typically 20–40 gallons. Requires regular pumping (monthly–quarterly).
- **Grease interceptor**: Large tank (commercial kitchen, food service). 500+ gallons. Two-chamber design; inlet → grease rise zone → outlet. Allows solids and grease to separate.
- **Sizing**: Based on waste water volume and retention time. Plans show size, location, and cleanout access.
- **Piping**: Inlet from sinks/drains, outlet to sanitary main. Trap prevents sewer gases backing up into building.
- **Maintenance note**: Pumping schedule is critical; full traps back up into kitchen, causing code violations and stoppages.

**Lift Stations** (when gravity flow fails):
- **Why needed**: When property is below main line grade or topography doesn't allow downhill flow.
- **Components**: Wet well (sump), pump(s), discharge line, check valve, control panel.
- **Discharge**: Forces sewage uphill through dedicated force main (typically smaller diameter, higher pressure pipe).
- **Material**: Force main is usually DIP or PVC Schedule 40 (higher PSI rating than sanitary pipe). Slopes are not relevant; elevation change is what matters.
- **Power/controls**: Electrical, alarm system if pump fails. Critical for 24/7 operation.
- **On drawing**: Shown as "LS-1" with elevation of wet well invert, pump capacity (GPM), discharge size.

**Testing Before Acceptance**:
- **Mandrel test**: Rubber plug pulled through pipe to verify no obstructions, root intrusion, or collapsed sections. Required for gravity sewers.
- **Air test** (low-pressure or bleed-off test): 0.5 PSI sustained for 10 minutes with no visible bubbles. Detects cracks, loose joints. More common in regions with groundwater.
- **TV inspection (CCTV)**: High-definition camera pulled through line. Documents joint condition, offset, cracks, I&I sources. Usually required for larger mains or problem areas.
- **Acceptance**: All three may be required before final sign-off. Confirm with local authority having jurisdiction.

---

## Domestic Water System

**Pipe Materials & Selection**:
- **DIP (Ductile Iron Pipe)**: Standard for mains (2"–24"), very durable in most soils. Heavier but corrosion-resistant. Check mill certifications.
- **PVC C900 (High-Pressure PVC)**: Smaller services (3/4"–2"), lighter weight, fast installation. Suitable for lower-pressure zones. C900 = 200 PSI rated.
- **Copper**: Older systems, some commercial. Corrosive in acidic soils; tubing (soft copper) used for service lines.
- **HDPE**: Trenchless (boring, directional drilling), corrosive soil conditions. Growing in use; verify local acceptance and certification.

**Meter Location & Size**:
- **Meter sets**: Typically 3/4" or 1" diameter. Size determines available household flow rate.
- **Location**: Shown on plot plan, usually near property line or inside building vault/basement. Affects service line routing.
- **Pressure check**: Meter size and supply line size must match; undersized meter restricts flow and increases pressure drop.
- **Note**: Fire service often separate from domestic meter; check if dual service required.

**Backflow Preventer Type & Location**:
- **RPZ (Reduced Pressure Zone)**: More robust, required in many jurisdictions for medical facilities, commercial kitchens, irrigation. Larger footprint, annual testing required.
- **DCVA (Double Check Valve Assembly)**: Simpler, smaller, suitable for low-hazard connections. Less frequent testing (every 5 years in some codes).
- **Location**: Usually at property line or inside building near meter. Plan shows exact location.
- **Why required**: Prevents contamination from flowing back into public water system (cross-connection protection).

**Fire Service Connection**:
- **Separate tap**: Dedicated line from main to FDC (Fire Department Connection) on building exterior. Typically 2"–4" line.
- **PIV (Post Indicator Valve)**: Gate valve on fire line with visible handle, shows open/closed status. Located near building or at property line.
- **FDC location**: Marked on plan; must be accessible to fire truck (within 50' of street, clear of obstructions). Typically on frontage nearest hydrant or main supply.
- **Check valve in FDC**: Allows one-way flow from FD truck; prevents backflow into city main.

**Hydrant Locations & Spacing**:
- **Spacing**: Typically 300'–500' apart (check local fire code). Ensures adequate coverage for fire flow.
- **Location on drawing**: Marked as "FH" with elevation note. Plan shows distance from building, street, intersections.
- **Bury depth**: Below frost line. Outlet nozzles at standard height (~2.5' above grade).
- **Flow requirements**: Plan notes required GPM for fire protection. Depends on building size, hazard classification.

**Thrust Blocks & Restraints**:
- **Why needed**: Water pressure pushing through fittings (tees, elbows, bends) creates lateral force. Concrete thrust block resists this.
- **Sizing**: By pressure (PSI) and pipe diameter. Plan should show block dimensions or designer calculates based on pressure @ fitting.
- **Location**: At every change of direction in line. Blocks are cast concrete, often placed before backfill.
- **Common mistake**: Forgetting thrust blocks at tees leading to fire line; fitting can shift under pressure, breaking seals.

**Valve Locations - Isolation & Control**:
- **Gate valve**: Primary shutoff valves on main line and branches. Allow full bore flow. Typically at: main entry to property, branches to zones, fire line.
- **Butterfly valve**: Used on larger mains (6"+) due to lighter weight and smaller footprint. Not suitable for small lines.
- **Valve boxes**: Show location above-grade, marked "WV" or similar. Depth noted (for operation depth, e.g., 3' below surface).
- **Spacing**: Typically one main line valve per 200'–300'. More frequent in commercial/industrial properties.

**Depth of Bury**:
- **Below frost line**: Protects pipe from freezing. Varies by region (Minnesota ~4', Southern US ~1'–2'). Check local code.
- **Clearance**: Typically 3'–4' minimum under roadways, 2'–3' under landscaping.
- **Mark on drawing**: Profile sections show depth at key points (road crossing, building approach, etc.).

**Pressure Testing Requirements**:
- **Test pressure**: Typically 150 PSI for 2 hours (or as specified in construction documents). Confirms no leaks.
- **Method**: Isolate section with plugs/valves, pressurize with water from pump or tank, watch gauge for drop.
- **Acceptance**: Zero leakage allowed. Any weeping joint fails test and must be re-done.
- **Time**: Leaks often appear in first 15 minutes; longer duration confirms joints have set if recently installed.

**Chlorination & Bacteriological Testing Before Use**:
- **Chlorination**: Disinfects new pipe to kill any bacteria introduced during construction. Dosage ~50 mg/L. Pipe sits for 24+ hours.
- **Flush out**: After chlorination, flush at high velocity to remove chlorinated water and any debris. Continue until water runs clear.
- **Bacteriological samples**: Collected after flushing. Must pass coliform testing (zero CFU per 100 mL per health dept rules).
- **Documentation**: Chain of custody for samples; lab results filed with health dept before final system approval.

---

## Site Utilities Coordination

**Minimum Horizontal Separations**:
- **Water from sewer**: 10'–15' minimum depending on jurisdiction. Separation reduces risk of contamination if sewer breaks.
- **Water from gas**: 3'–5' minimum (check local gas utility rules). Gas is often on opposite side of street from water.
- **Electrical ductbank from sewer**: 5'–10' minimum. Distance reduces moisture/flooding risk to electrical system.
- **Telecom from other utilities**: Typically 3'–5' depending on code. Fiber cables prefer lower ground stresses.
- **Note**: These are MINIMUMS. Plan layout often provides more separation for ease of installation and maintenance.

**Minimum Vertical Clearances at Crossings**:
- **Water OVER sewer**: 18" minimum vertical clearance (measured from outside diameter of sewer to inside of water pipe). Water on top protects it if sewer ruptures.
- **Electrical/telecom under sewer**: 12"–18" clearance. Cables protected from sewer infiltration.
- **Concrete encasement or steel casing**: Where vertical clearance cannot be maintained. Casing protects both utilities; requires special handling during installation.
- **Profile drawing**: Shows elevation of each utility at crossing; verify clearances before excavation.

**Crossing Protection Requirements**:
- **Concrete encasement**: 6" of concrete surrounds pipe/cable. Protects from external loads, abrasion, corrosion. More expensive but permanent.
- **Steel casing**: Larger diameter steel pipe serves as protective sleeve around utility. Utility pulls through casing; annular space may be sealed with grout or left open for future cable pulling.
- **Procedure**: Install casing first (often via boring), then pull utility through. If utility in casing, it can be replaced without re-excavating.
- **Cost/effort**: Casing significantly increases utility line cost; only used where crossing unavoidable and clearance inadequate.

**Conflicts with Other Trades**:
- **Electrical ductbank**: Usually 4"–6" concrete-encased runs in trenches. Marked on electrical drawings, not always on civil plans.
- **Gas lines**: Marked separately on utility coordination plan. Cannot be directionally bored like water/sewer; must be laid open.
- **Telecom / fiber**: Often installed last; may occupy same trench as others if protective covering (PVC conduit, duct spacer) used.
- **Power cable**: Sometimes installed in same trench as water/sewer if adequate separation and protection provided.

**How to Identify Conflicts from Plan Overlays**:
- **Same elevation (depth)**: If water shown at 3' deep and sewer at 2.5' deep in same trench area, they cross or run parallel too close. Red flag.
- **Same horizontal corridor**: Multiple utilities in narrow street or lot. Review profile at multiple cross-sections to confirm clearances.
- **Overlapping bends**: If sewer elbow and water tee are within 10' horizontally, check vertical separation on profile.
- **Trench annotation**: Plans note "shared utility trench" or "common corridor." These require special detail showing protective spacing/covering.
- **Conflict matrix**: Comprehensive designs include a conflict resolution table showing each crossing/parallel run and how it's handled.

**Utility Easement Requirements**:
- **Sewer easement**: Typically 10'–15' wide, centered on sewer line. Landowner cannot build structures, plant large trees, or alter grading over easement.
- **Water easement**: Similar width. Allows city/utility access for maintenance, repairs.
- **Combined easement**: On some properties, sewer + water under one easement. Reduces easement count but requires coordination with utility locations.
- **Recorded on deed**: Easements are legal documents, filed with property records. Do not assume easement exists; check survey and deed.
- **Impact**: Easement restricts future improvements; site plan must respect easement lines to avoid conflicts.

**Existing Utility Locations** (Critical step):
- **Call 811 (or local "call before you dig")**: Mark all existing utilities (water, sewer, gas, electric, telecom, fiber) before any ground disturbance. Marks are valid ~30 days.
- **Document marks**: Spray paint or flags show location. Cross-check with plan; if discrepancy, investigate before digging.
- **Conflicts with design**: If marked utility is not shown on plan or is in wrong location, notify designer and utility owner immediately.
- **Deep utilities**: Some utilities may be deeper than surface marks indicate. Vacuum excavation or careful hand digging near marked locations.

---

## Utility Tie-In Points

**Connection to City Main**:
- **Tap location**: Marked on plan at street or main line location. Tap size shown (e.g., "2" tap," "4" tap").
- **Permit & tap fee**: City/utility typically controls main taps. Separate permit and inspection often required. Contractor must schedule with utility.
- **Tap procedure**: Main is live; utility crews perform tap under pressure (wet tap) or shut main down (dry tap). Coordination essential to avoid service interruptions to neighbors.
- **Service line from tap**: Size and routing shown on plan from tap to property or building meter.

**Connection to Existing Site Utilities During Phased Construction**:
- **Phased sites**: Early buildings connect to temporary mains; later phases tie in as work expands.
- **Coordination plan**: Shows which building uses which temporary line during phase 1, where future connections occur for phase 2.
- **Sized for ultimate demand**: Temporary lines often sized for full build-out to avoid re-piping later.
- **Flexibility**: Design allows new structures to branch off existing lines without disrupting operating systems.

**Bypass / Temporary Connections During Construction**:
- **Bypass required if**: Construction work interrupts existing utilities serving occupied buildings or concurrent work.
- **Temporary water line**: Hose, pump, or temporary PVC line supplies adjacent buildings during tie-in work. Must be clearly marked and protected from damage.
- **Temporary sewer**: Bypass line (sometimes hose) diverts flows around work zone to prevent backups. Risk of overflow if not sized adequately.
- **Duration**: Bypass is temporary (hours to days). Must be removed and final connection tested before permanent operation.
- **Pressure/flow**: Temporary lines often smaller diameter; verify they can handle required flow. High-pressure water lines may need booster pump.

**Shutdown Coordination Requirements**:
- **Notice**: Utilities being shut down require advance notice to building operators, tenants, fire department (if fire service affected).
- **Duration**: Minimize shutdown time. Plan work sequence to reduce flow disruption.
- **Valve isolation**: Use existing valves to isolate work zone. Confirm valve function before relying on it.
- **Emergency contact**: On-site supervisor and utility liaison communicate throughout work. If problem occurs, know who to contact immediately.
- **Backflow/siphoning risk**: After shutdown, check for reverse flow into work area before crew entry. Especially critical for sewer work.

**As-Built Documentation Requirements for Utility Connections**:
- **Measured elevations**: Rim elevations, invert in/out at each connection. Compare to design and note discrepancies.
- **Distances & bearings**: Horizontal location of main line tap, distance from property line or reference point.
- **Material & size confirmation**: Verify what was actually installed matches construction documents.
- **Test results**: Pressure tests, flow tests, bacteriological samples (water) filed and attached to as-builts.
- **Photos**: Show connection details, valve locations, cleanout positions before backfill.
- **Record drawing**: Marked-up plan showing all utilities as actually built. Filed with city, developer, and owner.
- **Survey**: Final survey ties utilities to property monuments and structures. Critical for future maintenance access.

---

## Extraction Data Table Format

For each utility run identified on drawings, extract data into a standardized table. This structure works for all utility types (storm, sanitary, water, fire, gas, electrical ductbank, telecom).

**Standard Extraction Table**:
```
| Utility | From | To | Size | Material | Slope | Invert In | Invert Out | Rim/Cover | Length | Notes |
|---------|------|-----|------|----------|-------|-----------|-----------|-----------|--------|-------|
| Sanitary | Building | MH-1 | 4" | PVC SDR-35 | 1/4"/ft | 853.20 | 853.10 | 859.40 | 65 ft | Drop @ MH-1 |
| Storm | MH-3 | SD-2 | 18" | RCP | 0.75% | 843.50 | 843.47 | 851.20 | 145 ft | Type II RCP |
| Water | Main tap | Building | 2" | DIP | N/A | N/A | N/A | 848.50 | 220 ft | Bury 4' deep |
| Fire | Water main | FDC | 4" | DIP | N/A | N/A | N/A | 847.00 | 180 ft | PIV at property line |
| Gas | Street main | Building | 1.5" | PE | N/A | N/A | N/A | 835.00 | 210 ft | 3' deep, regulator at meter |
| Electrical | Transformer | Building | 4" conduit | PVC ductbank | N/A | N/A | 849.50 | 849.00 | 160 ft | 3' deep, 10 runs |
| Telecom | Street cabinet | Building | 1" duct | HDPE conduit | N/A | N/A | N/A | 848.50 | 175 ft | 2' deep |
```

**Notes column includes**:
- Special structures (drop manholes, cleanouts, access points)
- Protection method (casing, encasement) at crossings
- Depth of bury at key points
- Connection details (tap type, valve info, FDC access)
- Test results if available (pressure, mandrel, CCTV)

---

## Storage in plans-spatial.json

Store all extracted utility data under a `site_utilities` section. Each utility type gets its own array for easy querying and schedule coordination.

**JSON Structure**:
```json
{
  "site_utilities": {
    "storm": [
      {
        "id": "SD-1",
        "from": "Inlet corner NE parking",
        "to": "MH-3",
        "size_inches": 18,
        "material": "RCP Type II",
        "slope_pct": 0.75,
        "invert_in": 843.50,
        "invert_out": 843.47,
        "rim_elevation": 851.20,
        "length_ft": 145,
        "depth_at_start": 8.2,
        "depth_at_end": 7.73,
        "testing": "Mandrel pass, TV inspection complete",
        "notes": "Outlet to existing detention basin"
      }
    ],
    "sanitary": [
      {
        "id": "SAN-1",
        "from": "Building lateral cleanout",
        "to": "MH-2",
        "size_inches": 4,
        "material": "PVC SDR-35",
        "slope_pct": 2.08,
        "invert_in": 853.20,
        "invert_out": 853.10,
        "rim_elevation": 859.40,
        "length_ft": 65,
        "depth_at_start": 6.2,
        "depth_at_end": 6.3,
        "cleanout_spacing_ft": 65,
        "testing": "Air test passed 0.5 PSI x 10 min",
        "notes": "Separate grease trap discharge upstream of this line"
      },
      {
        "id": "SAN-MAIN-1",
        "from": "MH-2",
        "to": "Main tap",
        "size_inches": 8,
        "material": "DIP",
        "slope_pct": 1.0,
        "invert_in": 852.50,
        "invert_out": 852.30,
        "rim_elevation": 858.80,
        "length_ft": 320,
        "depth_at_start": 6.3,
        "depth_at_end": 6.5,
        "cleanout_spacing_ft": 150,
        "testing": "Air test passed, TV inspection OK",
        "notes": "Crosses water main at sta. 180 ft; 18\" clearance confirmed"
      }
    ],
    "water": [
      {
        "id": "W-SERVICE",
        "from": "City main @ tap",
        "to": "Building meter",
        "size_inches": 2,
        "material": "DIP",
        "pressure_rating_psi": 200,
        "bury_depth_ft": 4.0,
        "length_ft": 220,
        "meter_location": "Building basement NE corner",
        "meter_size": "1 inch",
        "backflow_type": "DCVA",
        "backflow_location": "At meter",
        "testing": "Pressure test 150 PSI x 2 hrs passed; chlorinated, bacteriological OK",
        "notes": "Bury below 4' frost line; thrust block @ 45 deg bend sta. 90 ft"
      },
      {
        "id": "W-FIRE",
        "from": "City main",
        "to": "FDC Building face",
        "size_inches": 4,
        "material": "DIP",
        "pressure_rating_psi": 200,
        "bury_depth_ft": 3.5,
        "length_ft": 180,
        "piv_location": "Property line, near west corner",
        "fdc_location": "Building S face, 40 ft from street",
        "flow_requirement_gpm": 1000,
        "testing": "Pressure test 150 PSI x 2 hrs passed",
        "notes": "PIV in valve box, check valve in FDC; separate from domestic service"
      }
    ],
    "fire": [
      {
        "id": "FIRE-HYD-1",
        "location": "Street frontage W side, 50 ft from corner",
        "elevation": 846.50,
        "bury_depth_ft": 4.0,
        "distance_to_building_ft": 280,
        "flow_rating_gpm": 1500,
        "spacing_to_next_hydrant_ft": 350,
        "notes": "Accessible for fire truck; clear 15 ft radius around hydrant"
      },
      {
        "id": "FIRE-HYD-2",
        "location": "Street frontage E side, 150 ft from corner",
        "elevation": 846.70,
        "bury_depth_ft": 4.0,
        "distance_to_building_ft": 220,
        "flow_rating_gpm": 1500,
        "spacing_to_next_hydrant_ft": 350,
        "notes": "Accessible from street; clear radius confirmed"
      }
    ],
    "gas": [
      {
        "id": "GAS-1",
        "from": "Street regulator",
        "to": "Building meter",
        "size_inches": 1.5,
        "material": "PE (polyethylene)",
        "bury_depth_ft": 3.0,
        "length_ft": 210,
        "pressure_psi": 10,
        "regulator_location": "At street, before service line",
        "meter_location": "Building west wall, exterior",
        "testing": "Pressure test passed; no leaks detected",
        "notes": "Call utility for connection; 10 ft min from sewer per code"
      }
    ],
    "electrical_ductbank": [
      {
        "id": "ELEC-DUC-1",
        "from": "Transformer pad corner",
        "to": "Building electrical room",
        "duct_size_inches": 4,
        "material": "PVC ductbank",
        "number_of_runs": 10,
        "bury_depth_ft": 3.0,
        "length_ft": 160,
        "protection": "6 in concrete encasement entire length",
        "crossing_info": "Crosses sanitary main @ sta. 95 ft, 10 ft horizontal sep",
        "notes": "Ductbank slope 1% toward building for drainage; pull rope in place"
      }
    ],
    "telecom": [
      {
        "id": "TELECOM-1",
        "from": "Street cabinet",
        "to": "Building demarcation point",
        "duct_size_inches": 1,
        "material": "HDPE conduit",
        "bury_depth_ft": 2.0,
        "length_ft": 175,
        "number_of_cables": 4,
        "slack_percentage": 10,
        "notes": "HDPE conduit; 2' deep standard. Coordinate timing with utility; fiber sensitive to tension during pull."
      }
    ]
  }
}
```

**Data entry notes**:
- **Elevations**: Record to 0.01' (nearest inch). Use same datum as rest of site.
- **Slopes**: Gravity systems use slope %; forced systems (fire, gas, electrical) show "N/A" for slope.
- **Depth**: Measured from rim/surface to pipe/duct centerline or top of ductbank. Verify during excavation.
- **Testing**: Note pass/fail, date, inspector. Attach test reports to record documents.
- **Conflicts**: Cross-reference in "notes" column (e.g., "crosses sewer main, 18\" clearance confirmed").
- **Incomplete data**: If detail not shown on plan (e.g., material not specified), flag in notes ("Material TBD, confirm with utility") and follow up before construction.

---

## Grading and Earthwork Data (from Visual Pipeline Pass 9)

The visual pipeline (Pass 9) extracts contour and grading data from civil/site sheets and stores it in `plans-spatial.json → site_grading`. When processing civil documents, cross-reference this data:

**Available from `site_grading`:**
- `contours.existing` — Existing terrain contour elevations and line styles
- `contours.proposed` — Proposed (design) terrain contour elevations
- `contours.contour_interval_ft` — Spacing between contour lines (1', 2', 5')
- `spot_elevations` — Point elevations (FFE, grade, top-of-curb) from Pass 6
- `cut_fill_volumes` — Rough cut/fill estimate from contour comparison
- `drainage_patterns` — Overall drainage flow direction and fall

**Cross-checks to perform:**
1. Spot elevations at utility inverts should be consistent with utility invert elevations extracted in Storm Drainage / Sanitary sections
2. Building FFE from spot elevations should match structural FFE from foundation plans
3. Cut/fill estimate should be consistent with SWPPP earthwork volumes
4. Drainage direction should be consistent with storm sewer flow direction
5. Contour interval should match the interval noted in the civil legend/notes

---

## Field Verification Checklist

Before final grading and backfill, verify:
- [ ] All utility lines exposed, depths measured against elevations.
- [ ] Slopes confirmed for gravity systems (storm, sanitary, water lateral runs).
- [ ] Invert elevations match design; any variance noted and documented.
- [ ] Cleanouts and access points located and marked for final survey.
- [ ] Crossing clearances verified (horizontal and vertical).
- [ ] Test results received and filed (pressure, mandrel, TV inspection, bacteriological).
- [ ] As-built plan updated with measured locations, elevations, materials.
- [ ] All easements and utility markings (811 calls, paint marks) cleared or preserved.
- [ ] Utility companies signed off on their work; final inspection letters filed.
- [ ] Site utilities JSON updated and cross-checked against as-builts.
