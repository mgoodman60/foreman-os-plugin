# Cross-Trade Coordination Reference
**Foreman OS Plugin | Practical Field Reference for Multi-Spatial Coordination**

---

## Introduction
Construction involves 8–15 trades working in the same space simultaneously. Coordination failures are the #1 source of rework, delays, and disputes. This guide covers the high-conflict coordination zones: above-ceiling, underground utilities, walls, slab penetrations, equipment supports, and pre-installation planning. You'll learn the coordination drawing process, trade sequencing hierarchy, and how to avoid the expensive mistakes that demolition crews fix months later.

---

## 1. ABOVE-CEILING COORDINATION
*The #1 coordination problem in commercial construction*

### Why Above-Ceiling is a Battleground
The space between the structural slab and the ceiling grid is where mechanical, electrical, plumbing, and fire protection systems compete for vertical space. The typical commercial ceiling is 9–12 feet above finished floor. The structural slab-to-slab height is typically 14 feet. That leaves 2–3 feet of space to stack HVAC ductwork, sprinkler mains, waste pipes, electrical conduit/cable tray, and all their associated hangers.

**The Problem:** If one trade (e.g., HVAC) installs its ductwork in the "wrong" location early, everything else downstream has to shift or relocate. By the time electrical discovers the conflict, ductwork is already installed and difficult to move.

### The Standard Above-Ceiling Stack (Bottom to Top)
This hierarchy is not arbitrary; it's based on gravity and system requirements:

1. **Plumbing Waste/Vent** (LOWEST)
   - Gravity-dependent (must slope downward to drain)
   - Largest diameter pipes (3"–4" waste lines, 2" vents)
   - Most rigid installation (cannot be compressed or rerouted significantly)
   - Location: Lowest priority to position but MUST slope correctly

2. **Water Supply / Fire Main**
   - Pressurized (can route in any direction if fittings support)
   - Smaller diameter (1"–2" typical water lines, 1–2" fire main)
   - Flexible routing (can use elbows, transitions)
   - Location: Above waste lines, but below HVAC typically

3. **HVAC Ductwork**
   - Large diameter (can be 18"×18" or larger for main trunks)
   - Relatively rigid (ductwork does not compress)
   - Can be routed over or under other systems with 1–2" clearance
   - Location: Mid-level; often the "controller" of above-ceiling layout

4. **Electrical Conduit/Cable Tray**
   - Small diameter (1/2"–2" conduit; cable trays are "ribbon" thin)
   - Very flexible (can be routed around obstacles easily)
   - Cannot cross plumbing waste (code violation—sanitary gases risk)
   - Location: Above HVAC typically, but flexible routing allows it to navigate

5. **Sprinkler Branch Lines / Hangers** (UPPER LEVEL)
   - Small diameter (1/2"–3/4" branch lines)
   - Flexible routing (can navigate around obstacles)
   - Typically supported by hangers from structure
   - Location: Often the highest system, suspended from structure

6. **Light Fixtures, Registers, Grilles** (CEILING PLANE)
   - At or just above ceiling grid
   - Require accessible openings in ceiling
   - Potential conflicts with everything above (all systems must avoid light fixture locations)

### Minimum Clearance Requirements

| System Pair | Minimum Clearance | Reason | Code |
|------------|------------------|--------|------|
| Ductwork to ductwork | 1" minimum | Thermal expansion, vibration isolation | SMACNA, ASHRAE |
| Electrical conduit over water line | 12" horizontal separation OR 12" vertical above | Cross-contamination prevention (electrical above) | NEC 300.3, local amendments |
| Electrical under plumbing waste | FORBIDDEN | Sanitary gas release risk, fire hazard | NEC 300.3, IRC |
| Sprinkler branch to electrical | 1" | Fire protection priority; minimize electrical exposure to water |  NEC, NFPA |
| Any system to structure | Minimum 6" for insulation/hangers; 12" for thermal considerations | Thermal bridging, vibration, maintenance access | Structural, MEP specs |
| Below structural slab | Maintain minimum headroom per code (typically 7'–7'6" minimum ceiling height in finished spaces) | Code-required clear height for occupants | IBC/IRC |

### Coordination Drawing (The Tool to Prevent Conflicts)
A coordination drawing is an overlay of all MEP trades on a structural reflected ceiling plan. It shows every system route and identifies conflicts BEFORE installation.

**Typical Coordination Drawing Process:**

1. **Base Drawing Preparation** (GC or MEP Coordinator)
   - Start with structural reflected ceiling plan (shows beam locations, support points)
   - Add architectural ceiling grid (if applicable)
   - Mark column lines, bracing points, any structural obstructions
   - Identify critical zones: mechanical rooms, electrical rooms, plumbing chases

2. **Individual Trade Routing** (Each Trade Submits)
   - **HVAC**: Ductwork centerline for all mains, branches; hanger points; access doors for filters
   - **Plumbing**: Waste/vent routing with slope indicators; water line routing; clean-out access points
   - **Electrical**: Conduit runs; cable tray; disconnect locations; equipment pad locations
   - **Fire Protection**: Sprinkler main routing; branch line coverage diagram; alarm device locations
   - Scales: Typically 1/4" = 1' or 1/2" = 1' (large enough to show details)

3. **Overlay & Conflict Identification** (MEP Coordinator or Architect)
   - Combine all trade drawings on single sheet (color-coded by trade)
   - Mark every conflict: X marks where systems overlap or violate clearance
   - Note severity: "critical" (one system must move), "minor" (re-route easily)
   - List conflicts on schedule: "Conflict #1: HVAC ductwork conflicts electrical cable tray at Grid 3-C. Resolution: Electrical to shift north 2 feet."

4. **Resolution & Sign-Off** (All Trades + GC)
   - **HVAC**: "Accept electrical shift; ductwork remains as shown."
   - **Electrical**: "Accept northern shift; relocate conduit run."
   - **Plumbing**: "No impact to waste line; maintain water line as shown."
   - All trades sign coordination drawing (commitment to follow the plan)
   - Revisions tracked with date, revision marker

5. **Field Verification** (GC Superintendent)
   - Post coordination drawing on job site (job shack, in field)
   - Pre-installation conference: superintendent walks trades through their routes per coordination drawing
   - Mark routes on structure with chalk or tape (physical reference)
   - Enforce adherence: "You're 1 foot off the coordination drawing—stop and verify with MEP coordinator before continuing."

### "First In Wins" Problem (How Conflicts Happen)

**Typical Scenario:**
- Day 1: HVAC contractor installs ductwork (no coordination drawing yet). Duct placed where it was convenient that day.
- Day 5: Electrical contractor arrives, ready to install conduit. Finds ductwork blocking planned route.
- Day 8: Plumber arrives, ready to install waste lines. Both HVAC and electrical are already in place, leaving no good route.
- Day 12: Project manager blames all three trades. Reality: No coordination drawing, no pre-planning.

**Prevention:**
- Require coordination drawing BEFORE any trade starts rough-in
- Don't allow any trade to begin until all trades agree
- Enforce the drawing during installation (superintendent's job)

### Resolution Hierarchy (When Conflicts Can't be Avoided)
Sometimes you can't fit everything in the available space. The question is: Who moves?

| Priority | System | Reason |
|----------|--------|--------|
| **1st (NO MOVE)** | Plumbing Waste/Vent | Gravity-dependent; moving requires code review; most expensive to relocate |
| **2nd (AVOID IF POSSIBLE)** | Water Supply / Fire Main | Pressurized; routing flexibility limited by pressure drop; moving requires engineer calc |
| **3rd (CAN MOVE)** | HVAC Ductwork | Large but flexible; moving affects ductwork layout, pressure drop; re-calc but doable |
| **4th (MOVES LAST)** | Electrical Conduit | Most flexible; can be routed above, below, around; minimal code impact; easiest to move |

**Field Example:** HVAC duct conflicts with fire sprinkler main. Neither wants to move. Electrical conduit can easily shift to accommodate HVAC. Electrical moves; HVAC and water stay put.

### Inspection Hold Points
- **Before Rough-In Starts**: Coordination drawing approved by all trades and signed
- **During Rough-In**: Superintendent verifies trades are following coordination drawing (random spot-checks at 3–5 locations per day)
- **Before Drywall/Ceiling Close-Up**: All systems in place per coordination drawing, no conflicts visible, penetrations identified and cleared

---

## 2. UNDERGROUND UTILITY COORDINATION
*Getting utility stacking and crossing correct before excavation*

### Typical Utility Trench Layout (Plan View)
A typical commercial building requires 4–6 separate utilities. The size and spacing rules vary by local code, but this is standard:

```
BUILDING FACE
┌─────────────────────────────────┐
│     BUILDING ENTRY              │
│     (Utilities approach here)    │
└─────────────────────────────────┘

UTILITY TRENCH LAYOUT (Typical):
─────────────────────────────────────────────────────
Fire Service Line (1–2" dia)        ← 10 feet from building
─────────────────────────────────────────────────────
Domestic Water Line (1–2" dia)      ← 8 feet from building
─────────────────────────────────────────────────────
Gas Line (if applicable)             ← Separate trench or 6 feet from water (must check local utility code)
─────────────────────────────────────────────────────
Sanitary Sewer (4–6" dia)            ← 10–12 feet below water line (elevation separation)
─────────────────────────────────────────────────────
Storm Sewer or Drainage              ← Separate trench or parallel, 6–10 feet away
─────────────────────────────────────────────────────
Electrical Duct Bank (4–6 PVC ducts, concrete encased)  ← Separate trench, minimum 3 feet away from water
─────────────────────────────────────────────────────
Telecom/Data Conduit                 ← Separate trench or shared with electrical (check utility rules)
─────────────────────────────────────────────────────
```

### Vertical Stacking (Cross-Section View)
When utilities MUST cross or run in same trench, vertical separation is critical:

```
UTILITY TRENCH CROSS-SECTION (Vertical Stacking):

GRADE ═════════════════════════════════════════════════
      ↓
     12"   Warning Tape (yellow, "UTILITIES BELOW")
            ╔════════════════════════════════════╗
            ║ Water Supply (Domestic) (1–2")     ║ ← HIGHEST in stack
            ╚════════════════════════════════════╝

     24"   ╔════════════════════════════════════╗
            ║ Gas Line (if applicable) (1–2")    ║ ← 12" below water min. (code-dependent)
            ╚════════════════════════════════════╝

     24"   ╔════════════════════════════════════╗
            ║ Fire Service Line (1–2")           ║ ← Separate or parallel (12" separation)
            ╚════════════════════════════════════╝

     36"   ╔════════════════════════════════════╗
            ║ Electrical Duct Bank (concrete)    ║ ← LOWEST OR SEPARATE
            ╚════════════════════════════════════╝

     48"+  ╔════════════════════════════════════╗
            ║ Sanitary Sewer (4–6")              ║ ← BELOW GRADE (deep trench)
            ║ (10'–12' minimum below water)      ║
            ╚════════════════════════════════════╝
```

**Why This Order?**
- **Water Supply on Top**: Most likely to fail or leak; needs easy access for repair
- **Gas in Middle**: Buoyancy concern if in high water table; must not be above water (safety)
- **Electrical Lowest or Separate**: Prevent water contact; ground/burial concerns
- **Sewer Deep**: Gravity flow requires depth; freezing concerns in cold climates require depth below frost line

### Critical Separation Distances (Code Requirements)
| Utility Pair | Minimum Horizontal | Minimum Vertical | Notes |
|-------------|-------------------|-----------------|-------|
| **Water to Sewer** | 10 feet | 12 inches (water ABOVE sewer) | Prevent contamination if sewer leaks |
| **Water to Gas** | 1–3 feet (local code varies) | 12 inches | Gas isolation for safety |
| **Electrical to Water** | 3 feet OR 12" vertical above | 12 inches above | Prevent electrical hazard |
| **Electrical to Sewer** | 6–10 feet | N/A (usually separate) | Ground protection |
| **Gas to Sewer** | 3–6 feet (local code) | 12 inches min | Safety isolation |
| **Fire Service to Domestic Water** | 1 foot minimum | Can share trench | Same supply source; separation acceptable if marked |

**CRITICAL:** Check your LOCAL code. Some jurisdictions have different requirements. The city/county standards override these generics.

### Utility Crossing Procedure
When utilities MUST cross (cannot maintain separation):

1. **Ductwork/Sleeve Installation**
   - The non-dominant utility is sleeved through the other
   - Example: Electrical conduit sleeves through/over sewer line (electrical has smallest cross-section)
   - Sleeve material: PVC for most cases; concrete encasing if required by utility
   - Sleeve length: Minimum 3 feet on each side of crossing point (6 feet total minimum)

2. **Vertical Separation at Crossing**
   - Water supply crosses ABOVE sewer (elevation difference: minimum 1 foot vertical rise at crossing point)
   - Electrical crosses ABOVE water if possible
   - Sewer is lowest point

3. **Marking & Documentation**
   - Install permanent marker at surface above crossing (post, paint mark, or GPS tag)
   - Document crossing location on "record drawing" (as-built utility plan)
   - Verify crossing in survey/mark-out before backfill

### Pre-Excavation Utility Locate (The 811 Call)
**Required by law before ANY excavation:**

1. **Call 811** (Dig Safe, or your local equivalent)
   - Provide address, utility type (building water/sewer/gas/electric)
   - Utility companies mark existing utilities with spray paint (typically 5–7 days response)
   - Marks show approximate location; your survey/pothole verifies exact location

2. **Pothole Verification** (Hand-dig BEFORE excavation equipment)
   - Use shovels (not heavy equipment) to expose utilities at mark locations
   - Identify: Water line, sewer line, gas line, electrical, telecom
   - Note depth, condition, direction of run
   - Take photos for site record

3. **If Existing Utility Found NOT Where Expected**
   - Stop excavation
   - Call utility company to re-mark
   - Wait for confirmation before proceeding
   - Document unexpected location in site photos/reports

### Material Storage Near Utilities
- Water/sewer/gas/electrical lines are active utilities (not to be buried or damaged)
- Maintain clear zone above marked utilities: 3-foot radius minimum
- No material storage, equipment placement, or excavation in clear zone
- Exception: planned trenching per design; non-disturbance otherwise

### Inspection Hold Points
- **Before Excavation Begins**: 811 call made, existing utilities marked, pothole verification complete, record showing utilities is posted on site
- **During Trench Excavation**: GC superintendent verifies trench depth matches plan, utilities appear at expected elevations, no utility damage (call utility company immediately if damage suspected)
- **Before Backfill**: All new utilities installed, tested (water pressure test, electrical continuity, sewer smoke test), all crossings documented and marked
- **Final Backfill**: Trench compacted properly (compaction test to 95% standard for utility trenches), surface restored per plan

---

## 3. WALL COORDINATION
*Getting MEP and structural requirements right BEFORE drywall closes the wall*

### Stud Wall Roughing (The Critical Pre-Drywall Work)
Once drywall is hung, moving anything behind it is exponentially more expensive. The pre-drywall period is when all electrical boxes, plumbing rough-in, blocking for future equipment, and fire-rated assembly details must be finalized.

### Typical Wall Build-up (Bottom to Top)
```
INSIDE FACE (room interior)
═════════════════════════════════════════════════════
   Drywall (5/8" typ)                    ← FINISH FACE
═════════════════════════════════════════════════════
   Insulation (3.5" fiberglass, R-13)    ← THERMAL/ACOUSTIC
═════════════════════════════════════════════════════
   Vapor Barrier (if required)           ← VAPOR CONTROL
═════════════════════════════════════════════════════
   Stud Framing (2×4 or 2×6 studs)       ← STRUCTURE
                                         (with MEP rough-in inside)
═════════════════════════════════════════════════════
   Sheathing (plywood, OSB, or gypsum)   ← OUTSIDE FACE STRUCTURE
═════════════════════════════════════════════════════
   House Wrap (if exterior)              ← WATER/AIR BARRIER
═════════════════════════════════════════════════════
OUTSIDE FACE (weather / exterior)
```

### Pre-Drywall MEP Coordination Meeting (CRITICAL)
**This meeting happens AFTER framing is complete, BEFORE insulation/drywall.**

Attendees: GC Superintendent, Electrical Foreman, Plumbing Foreman, Mechanical (if ductwork in walls), Architect, Structural Engineer (if modifications needed)

**Agenda Items:**

1. **Electrical Box Locations**
   - Identify all receptacle, switch, and device box locations from architectural drawings
   - Verify heights (per ADA: receptacles 15"–48" floor to center, switches 48"–54" floor to center)
   - Coordinate with casework/equipment drawings (TV mounts, cash registers, equipment controls)
   - Mark locations on wall studs with tape/paint BEFORE insulation/drywall

2. **Backing & Blocking Requirements**
   - Grab bars in bathrooms/wet areas (solid blocking behind bar location)
   - TV mounts, equipment supports (blocking must support full load; typical: 200–300 lbs for wall-mount equipment)
   - Future equipment mounts (coordinate with mechanical/electrical equipment location drawings)
   - Verify stud spacing accommodates backing (typical: 16" on center; blocking fits between studs)

3. **Plumbing Penetrations & Access**
   - Hot water line routing through walls (requires insulation for thermal control; coordinate location)
   - Supply/waste penetrations: Verify 2"×4" studs are adequate; oversized studs (2"×6" or 2"×8") may be needed for large pipes
   - Shutoff valve locations (should be accessible, not buried in walls)
   - Access panels for future cleanouts

4. **Fire-Rated Wall Details**
   - Penetrations in rated walls require firestopping (inspection point)
   - All electrical, plumbing, and ductwork penetrations noted on floor plan
   - Firestopping responsibility assigned (typically MEP trade responsible for their penetrations)
   - Sample firestop detail posted on site (shows sealant type, material thickness)

5. **Rated Wall Continuity**
   - Wall must extend from deck-to-deck (or deck-to-structure above), NOT just to ceiling grid
   - Coordinate framing: studs, blocking, head detail all shown on framing plan
   - Verify ceiling/soffit systems don't violate wall rating (gaps allow fire spread)

### Plumbing Walls (Oversized Studs for Waste Lines)
Standard 2"×4" studs are too narrow for 3"–4" waste pipes. Typical solutions:

| Stud Size | Pipe Diameter | Use Case | Notes |
|-----------|---------------|----------|-------|
| 2×4 (3.5" interior) | ≤2" supply/vent | Secondary walls, branch lines | Typical residential |
| 2×6 (5.5" interior) | 3–4" waste main | Main waste stacks, primary plumbing wall | Commercial typical |
| 2×8 (7.25" interior) | 4–6" waste main + vent | Multiple stacks, large buildings | High-rise typical |
| Staggered studs (offset) | Large pipes in both walls | Back-to-back bathroom walls | Creative solution; verify with engineer |
| Soffit/Chase (drop ceiling) | Large pipes | Running pipes above regular ceiling | More expensive; avoids oversized studs |

**Coordination:** Plumbing contractor provides rough-in drawing showing pipe locations and sizes. Framing contractor sizes studs accordingly. This must be coordinated BEFORE framing begins (not after).

### Electrical Box Coordination
Standard electrical boxes are shallow (1.5" deep). If insulation, blocking, or other items occupy wall cavity, boxes may not fit or may not be flush with future drywall.

| Box Type | Depth | Use | Coordination Note |
|----------|-------|-----|-------------------|
| Shallow box (1.5") | 1.5" | Standard 2×4 wall (3.5" cavity) | Normal residential |
| Old work / remodel box (varies) | 1.75–2.5" | Retrofit (retrofit not typical in new construction) | N/A |
| Deep box (2.5–3") | 2.5–3" | Walls with blocking/backing, or for extra conductors | Requires deeper box; framer must accommodate |

**Typical Issue:** Framer installs blocking for grab bar in bathroom, reducing cavity space. Electrician's standard shallow box no longer fits. Solution: Use deep boxes, or relocate blocking. This must be coordinated at pre-drywall meeting.

### Inspection Hold Points
- **After Framing, Before Insulation**: All electrical boxes located and installed, all blocking/backing installed, plumbing rough-in complete, all locations marked for verification
- **After Insulation, Before Drywall**: Verify insulation does not cover/block electrical boxes, verify backing is still in place and correct, all penetrations identified
- **Before Drywall Finish**: Sample firestop details reviewed and approved (if fire-rated wall)

---

## 4. SLAB PENETRATIONS & EMBEDS
*Getting it right before concrete cures — moving concrete is exponentially more expensive*

### Why Slab Embeds Matter
A 4-foot horizontal relocation of a slab penetration BEFORE the pour:
- Cost: ~$50 (move the sleeve/form)
- Time impact: Minimal

A 4-foot relocation AFTER the concrete cures:
- Cost: $1,500–3,000 (core drilling, epoxy repair, testing)
- Time impact: 1–2 weeks (waiting for coring service, cure time)
- Quality impact: Cored hole creates stress concentration; weakens slab

**Lesson:** Pre-pour coordination is non-negotiable.

### Embed Schedule (The Master List)
An "embed schedule" is a table that lists EVERY item that goes through a slab:

| Item # | System | Description | Qty | Size | Location (Grid) | Elevation | Tolerance | Notes |
|--------|--------|-------------|-----|------|-----------------|-----------|-----------|-------|
| E-1 | Structural | Column Base Anchor Bolts | 8 | 1.5" dia | A-1 | +0.0" | ±1/8" | Embedded during pour |
| E-2 | Mechanical | Equipment Pad (400-lb AHU support) | 1 | 4'×8' platform | C-4 | +0.0" | ±1" | Four 2"×4" timbers |
| E-3 | Plumbing | Drain Sleeve (4" PVC) | 2 | 4" dia | D-5, F-6 | +0.0" | ±1" | Sleeved penetrations |
| E-4 | Electrical | Duct Bank (4×2" PVC conduits) | 1 | 8" wide×10" tall | B-3 | +0.0" | ±1" | Concrete encased |
| E-5 | Fire Protection | Drain Plug Sleeve | 1 | 1.5" dia | H-8 | +0.0" | ±1" | Sprinkler drain |
| E-6 | Plumbing | Cleanout Access (4" waste) | 1 | 4" dia | A-8 | +0.0" | ±1/2" | Install frame/cover after pour |

**Key Detail:** Embed schedule is created collaboratively by:
- **Structural Engineer**: Foundation anchors, equipment pads for heavy loads, critical structural embeds
- **MEP Designers**: Mechanical (equipment pads, duct sleeves), Plumbing (drain/supply sleeves), Electrical (duct banks, grounding), Fire Protection (drain plugs, anchor points)
- **GC**: Final list, locations verified in field, tolerances realistic

### Sleeve Schedule (Every Pipe, Conduit, and Duct Through a Slab)
Similar to embed schedule but focused on sleeves (protective tubes through penetrations):

| Item # | System | Description | Size | Type | Location | Notes |
|--------|--------|-------------|------|------|----------|-------|
| S-1 | Plumbing | Water Supply Sleeve | 2" dia | PVC SCH 40 | A-3 | Concrete encased; set at slab face |
| S-2 | Plumbing | Waste Sleeve | 4" dia | PVC SCH 40 | B-5 | Sloped; seal within 5' of building |
| S-3 | Electrical | Electrical Conduit | 2" dia | Steel | C-4 | Concrete encased |
| S-4 | Mechanical | Ductwork Sleeve | 14"×14" | Steel or aluminum | D-2 | Duct transitions to rigid sleeve |
| S-5 | Fire Protection | Sprinkler Riser | 1.5" dia | Steel | E-6 | Threaded; concrete encased |

**Difference from Embeds:** Sleeves are TEMPORARY conduits that later carry permanent systems through penetrations. Embeds are items that STAY in concrete.

### Pre-Pour Coordination Meeting for Slabs (CRITICAL)
**Timing:** 2–3 days BEFORE scheduled pour

**Required Attendees:** GC Superintendent, Structural Concrete Foreman, Structural Engineer, MEP Subcontractors (Mechanical, Electrical, Plumbing, Fire), Architect, Site Inspector

**Meeting Output:**
1. **Physical Walk-Down of Slab Area**
   - Walk the deck/area to be poured with marked plan
   - Point to each embed/sleeve location: "Drain goes here," "Electrical duct bank here"
   - Verify clearances: Are embeds 3+ feet from column centerlines? Are they clear of rebar patterns?
   - Identify any last-minute location changes (MEP contractor wants to shift something)

2. **Tolerance Discussion**
   - Structural: "Column anchors are ±1/8" — cannot move"
   - Equipment Pads: "AHU pad is ±1" — do not over-tighten tolerance"
   - MEP: "Drains are ±1", electrical ducts are ±1""
   - Agree on who sets up embeds (typically concrete contractor under GC direction)

3. **Last-Minute Verification**
   - Confirm all materials are on-site: sleeves, anchors, forms
   - Confirm contractor crews ready to place embeds during pour
   - Review weather forecast: rain delays the pour? Affects embed setup timeline?

4. **Hold Point Signature**
   - GC gets written confirmation from each trade: "Yes, embeds match our drawing, ready for pour"
   - Document in meeting minutes (timestamp, attendees, approvals)

### Common Embed/Sleeve Mistakes (and Prevention)

| Mistake | Consequence | Prevention |
|---------|-------------|-----------|
| **Embed in wrong location** (off grid by 2 feet) | Requires coring after pour; expensive, delays system installation | Walk the deck before pour with marked plan; superintendent confirms location verbally |
| **Sleeve too short or installed at wrong height** | Pipe sticks out of slab; doesn't seat properly; requires grinding or epoxy | Verify sleeve length matches slab thickness; set elevation at slab form face |
| **No sleeve** (pipe runs directly through concrete) | Concrete bonds to pipe; difficult to remove/replace; cannot be relocated | Specification: All penetrations require protective sleeves; enforce during placement |
| **Rebar protruding into sleeve** | Blocks pipe insertion; requires re-pouring or grinding | Mark rebar around sleeves; bend rebar away from sleeve during setting; inspect before pour |
| **Concrete over sleeve** (sleeve not high enough) | Pipe buried; cannot access; requires coring | Sleeves must be set above final slab surface by minimum 1/2"; check height before pour authorization |
| **Multiple embeds too close together** (less than 1 foot apart) | Reduces concrete between penetrations; creates stress concentration; risk of cracking | Plan embed locations with minimum 1-foot separation; if unavoidable, engineer must review |
| **Utility trench sleeves not sealed** (within 5' of building) | Water intrusion around sleeve; foundation settling/damage | Seal all utility sleeves within 5 feet of building with flowable fill or caulk within 24 hours after pour |

### Embed Installation (GC Role During Placement)
During the concrete pour:

1. **Verify Embed Staging** (1 hour before pour)
   - All sleeves, anchors, pads staged at slab location
   - Labeling clear (ID number matches embed schedule)
   - No debris in sleeves or on embed surfaces

2. **Position Embeds During/After Pour** (During pour)
   - As concrete rises, position embeds at correct elevation
   - Verify depth: structural anchors must be at design depth (typically 2–3 feet embedded)
   - Check vertical alignment: anchors must be vertical (not tilted)

3. **Protect During Curing** (After pour)
   - All sleeve openings capped/covered (prevent debris, prevent concrete from dripping in)
   - Anchor bolts exposed (not buried in concrete); verify visibility on drawings
   - Mark embed locations for ease of identification later (tape, paint, GPS if required)

### Inspection Hold Points
- **Embed Schedule Approval**: Structural engineer and all MEP trades sign off on locations, tolerances, sequencing
- **Pre-Pour Walk**: Physical verification of embed locations on actual slab area (not just drawing review)
- **During Pour**: GC superintendent verifies embeds positioned at correct elevation and location as concrete is placed
- **Post-Pour (24 hours)**: Verify all embeds are visible (not buried), sleeves are capped, anchor bolts are clean and vertical
- **Before System Installation**: Verify sleeves/embeds match actual slab penetrations; no surprises when plumbers/electricians try to route systems

---

## 5. EQUIPMENT PAD & SUPPORT COORDINATION
*Mechanical equipment, roof units, floor-mounted items, and ceiling hangers all have specific support requirements*

### Mechanical Equipment Pad (Most Common Issue)
A typical HVAC unit (rooftop or floor-mounted) requires coordination across four to five different systems:

**Example: Rooftop AHU (Air Handling Unit)**
- **Structural Support**: Concrete pad or steel curb; designed for equipment weight plus vibration isolation + safety factor
- **MEP Connections**:
  - Ductwork (supply/return connections)
  - Electrical power (208V 3-phase or 480V; breaker and disconnect)
  - Plumbing (condensate drain; possibly chilled water/hot water lines)
  - Controls (thermostat, sensors, commissioning)
- **Roof Penetration**: Curb seals around equipment; roof membrane integrity maintained around pad
- **Accessibility**: Service access; filter replacement access; vibration isolation tuning access

### Coordination Checklist for Equipment Pad

| Coordination Item | Responsibility | Verification |
|------------------|----------------|--------------|
| **Pad Size & Location** | Structural Engineer → Mechanical Designer | Pad matches equipment footprint + 6" clearance; location verified on roof plan |
| **Pad Loading** | Structural Engineer | Equipment weight + dynamic load factor (typically 1.5× for vibration) verified; concrete strength adequate |
| **Housekeeping Pad Height** | Mechanical Designer | Pad height set to provide required clearance for ductwork, service access (typically 12"–18" above roof) |
| **Anchor Bolt Pattern** | Mechanical Equipment Manufacturer → Structural Engineer | Anchor bolts match manufacturer equipment feet pattern; sized for load + vibration |
| **Vibration Isolation** | Mechanical Contractor | Isolators specified per equipment (some equipment includes isolators; some site-furnished) |
| **Ductwork Connections** | HVAC Contractor | Ductwork routing to/from unit does not interfere with structural elements or curb |
| **Electrical Power** | Electrical Contractor | Panel location, disconnect, breaker sizing, wire gauge all per equipment specs |
| **Condensate Drain** | Plumbing Contractor | Drain lines sloped ≥ 1/8" per foot; must not back-up into equipment; typically to building drain |
| **Roof Membrane Seal** | Roofing Contractor | Curb flashing installed per roof assembly detail; no water intrusion paths; membrane sealed around pad perimeter |
| **Clearances** | All trades | Minimum 3-foot clearance around equipment for service access; no obstructions |

### Pre-Installation Conference for Equipment (Mandatory)
**Timing:** Before equipment arrives on-site

**Attendees:** GC Superintendent, HVAC Foreman, Electrical Foreman, Plumbing Foreman, Roofing Foreman, Structural Engineer (if heavy equipment), Equipment Manufacturer Rep (if available by phone/video)

**Required Reviews:**
1. **Physical Setup**
   - Walk the roof/room where equipment will be installed
   - Point to anchor bolt locations (already set in concrete pad)
   - Verify pad is level and clean
   - Confirm ductwork connections align with equipment port locations

2. **Drawing Verification**
   - Manufacturer equipment specs (weight, dimensions, connection sizes)
   - Pad design drawing (signed by engineer, confirms structural capacity)
   - Ductwork connection details
   - Electrical/plumbing interface drawings

3. **Sequencing**
   - When does equipment arrive? (coordinate with hoisting/rigging equipment)
   - When can installation begin? (pad cured? ductwork in place? electrical rough complete?)
   - What blocking/support is needed during rough-in phase? (temporary bracing?)

4. **Testing & Commissioning**
   - Who runs startup tests? (mechanical contractor or equipment rep)
   - When? (after all connections complete; before occupancy/turnover)
   - Will commissioning agents observe? (for complex systems, yes; for standard equipment, no)

### Ceiling-Hung Equipment (Vibration Isolation Hangers)
Rooftop units are typical. Less common: ceiling-hung equipment (large exhaust fans, ductwork supports, copters in mechanical rooms).

**Coordination:**
- **Structural**: Verify ceiling/truss can support equipment + vibration isolators + safety factor
- **Hangers**: Type of hanger (rod vs. cable vs. trapeze); spacing per engineer (typically 4–6 feet on center for large equipment)
- **Vibration Isolation**: Isolators mounted between hanger and equipment (springs or elastomeric pads reduce vibration transmission)
- **Clearance**: Minimum 18 inches clearance from equipment to structure above (allows vibration movement)

### Floor-Mounted Heavy Equipment (Printing Press, Manufacturing Equipment, Server Racks)
Equipment >1,000 lbs requires structural verification:

1. **Load Path**: Weight transfers through equipment feet → vibration isolators (if required) → floor slab/structure
2. **Floor Capacity**: Design dead load is typically 50 lbs/SF for office, 100 lbs/SF for storage. Heavy equipment may exceed design load.
3. **Engineer Review**: If equipment weight exceeds design capacity, structural engineer must verify or upgrade floor
4. **Anchor Requirements**: Heavy equipment may require bolting to floor (vs. freestanding). Verify anchor bolt design with equipment specs.
5. **Leveling**: Precision equipment (printing presses, laser systems) requires level mounting. Coordinate with installation contractor for shimming/leveling tolerance.

### Inspection Hold Points
- **Pad Installation**: Concrete pad cured to strength, anchor bolts in place and accessible, pad level verified
- **Before Equipment Arrival**: All ductwork, electrical, plumbing rough-in complete and within tolerance of equipment connection points
- **Equipment Installation**: Isolators installed per manufacturer, connections verified (ductwork sealed, electrical torqued per specs, drains flowing)
- **Startup/Commissioning**: Equipment runs at full load, no visible vibration issues, no leaks, electrical disconnect functional

---

## 6. PRE-INSTALLATION CONFERENCES
*The meeting that prevents 80% of coordination problems*

### When Pre-Installation Conferences Are Required
- **Structural Steel Erection**: Before first bolt is installed
- **Concrete Placement**: Before any slab/wall pour (especially mass concrete)
- **Roofing**: Before first membrane or shingles installed
- **MEP Rough-In** (Mechanical, Electrical, Plumbing, Fire Protection): Before any ductwork, conduit, or piping installed
- **Drywall**: Before first sheet is hung
- **Ceiling Grid**: Before hangers are installed
- **Flooring**: Before first floor finish installed
- **Elevator Installation**: Before any equipment on-site
- **Exterior Envelope** (windows, doors, siding): Before installation

**Guideline:** If a trade's work affects other trades' work, or if mistakes are expensive to fix, schedule a pre-installation conference.

### Who Attends
- **Always**: GC Superintendent, Trade Foreman, Trade Crew Leader
- **Usually**: Architect, General Contractor PM
- **As Needed**: Structural Engineer (for complex work), MEP Coordinator (for MEP conferences), Inspection Authority (for final inspections, sometimes pre-install walk)

### Standard Agenda (60 minutes typical)

#### Part 1: Scope Review (10 minutes)
- Foreman walks through the trade scope (what's included, what's not)
- GC confirms scope matches contract documents
- Any excluded items noted (these become potential change orders if requested later)

#### Part 2: Drawings & Specifications Review (15 minutes)
- Foreman confirms receipt of latest plans (rev. dated ___)
- Specification section(s) reviewed: Key requirements, quality standards, testing
- Submissions: Are all required submittals approved? (equipment cut sheets, product samples, etc.)
- Schedule: Confirm project schedule; verify trade start/end dates; identify critical path items

#### Part 3: Coordination Issues (15 minutes)
- Identify potential conflicts with other trades (MEP with structure, framing with MEP, etc.)
- Discuss shared resources (hoists, power, water, staging areas)
- Review sequencing: What must be complete before you start? What must you complete before next trade starts?
- Introduce coordination drawing (if applicable)

#### Part 4: Quality & Testing (10 minutes)
- Specification inspection hold points reviewed
- Testing requirements: Who performs? When? What are success criteria?
- Quality standards: What level of finish is expected? Showcase sample if possible
- Documentation: What photos/reports are needed?

#### Part 5: Safety & Logistics (10 minutes)
- Site-specific safety requirements (fall protection, electrical safety, material handling)
- Housekeeping: Material staging area, cleanup daily? End of shift?
- Traffic & access: How does trade access the site? Are restrictions in place for certain hours?
- Permits/inspections: Who coordinates with building department? When?

### Post-Conference Documentation
**Meeting Minutes** (issued within 24 hours):
- Date, attendees, trade, scope reviewed
- Key decisions (e.g., "Electrical will modify box locations per coordination drawing")
- Action items with responsibility and deadline
- Any open issues (with assigned owner to resolve)

**Distribution:**
- GC Project File (archive for disputes)
- Trade Foreman (confirms expectations)
- Architect/Engineers (notify if changes to scope)
- All trades (share coordination decisions that affect others)

### Common Pre-Installation Findings (and How They're Resolved)

| Issue Found | Resolution | Responsibility |
|-------------|-----------|-----------------|
| Specification section missing from trade packet | Issue updated specification; allow 24 hours for trade review before start | GC Superintendent |
| Coordination drawing not yet complete (MEP conflicts not identified) | Delay trade start by 2–3 days until coordination drawing approved; identify interim restrictions | GC PM + MEP Coordinator |
| Required submittal not approved (equipment cut sheet pending architect review) | Do not authorize start until submittal approved; verify in writing from architect | GC Superintendent |
| Subcontractor crew not ready (equipment not on-site, crew not assembled) | Negotiate revised start date; do not force start with unprepared crew (causes rework) | GC PM + Subcontractor PM |
| Safety requirement (fall protection, electrical lockout) not understood | Re-brief crew; verify understanding in writing; assign safety supervisor to first day | GC Superintendent + Safety Manager |
| Shared staging area conflict (two trades need same space at same time) | Coordinate staging schedule; one trade stages materials differently or at different location | GC Logistics Coordinator |

---

## 7. COORDINATION DRAWING PROCESS (The Core Coordination Tool)

A coordination drawing is the master document that prevents conflicts. Here's how to implement it effectively.

### Who Produces the Coordination Drawing?
Typically: **MEP Coordinator** (part of GC team, or consultant hired by GC) or **MEP General Contractor** (if MEP is self-performed)

Responsibility: Combine all trade submittals and identify conflicts BEFORE field installation.

### Input Documents (Required from Each Trade)
1. **Mechanical**
   - Ductwork routing plan (color: blue) showing all supply/return/exhaust runs
   - Equipment schedules (size, location, connections)
   - Hanger/support detail showing trapeze locations, hang points

2. **Electrical**
   - Conduit routing plan (color: red) showing all panel-to-load runs
   - Cable tray layout (if applicable)
   - Equipment location (transformers, disconnect, motor control centers)

3. **Plumbing**
   - Water supply routing (color: green) showing all supply lines
   - Waste/vent routing (color: brown) showing all drain lines and slope
   - Equipment pad locations (water heater, backflow preventer)

4. **Fire Protection**
   - Sprinkler main routing (color: yellow or orange)
   - Branch line coverage (grid spacing)
   - Drain line, main shut-off location

All drawings: Same scale (typically 1/4" = 1' or 1/2" = 1'), same base architectural plan (structural ceiling plan typical for above-ceiling work).

### Coordination Drawing Production Steps

**Step 1: Base Plan Preparation** (1 day)
- Start with architectural reflected ceiling plan (showing structural grid, columns, beams)
- Add room identification and dimensions
- Add structural soffit/beam information
- Copy as base for coordination overlay

**Step 2: Overlay Individual Systems** (2–3 days)
- Scan all MEP submittals
- Overlay ductwork on base (ductwork centerline, size label, hanger locations)
- Overlay electrical conduit/cable tray (color-coded; identify main runs and branch runs)
- Overlay plumbing (water supply in one color, waste/vent in another)
- Overlay fire protection sprinkler lines and zones

**Step 3: Conflict Identification** (1–2 days)
- Mark every location where systems overlap or violate clearance
- Assign conflict number: "Conflict #1," "Conflict #2," etc.
- Document conflict: Location (grid reference), systems involved, issue (overlap? clearance violation?), severity (critical/major/minor)

**Step 4: Conflict Resolution** (2–5 days)
- Notify trade responsible for moving system (typically: plumbing doesn't move, HVAC takes priority, electrical moves last)
- Get trade approval of revised routing
- Update coordination drawing with resolution details
- Document who approved: "HVAC approved electrical shift north 2 feet, per email dated 2/15/2026"

**Step 5: Sign-Off & Field Distribution** (1 day)
- Final coordination drawing printed on large format (24"×36" typical)
- All trades sign/initial: "I have reviewed and approve this coordination drawing"
- Post on job site: Job shack, MEP area, superintendent's office
- Issue to all trades: Printed copy or PDF access

### Field Implementation of Coordination Drawing

**Superintendent's Role:**
- Random spot-check verification: Once per week, walk the rough-in area with the coordination drawing
- Verify systems are in locations shown on drawing (not shifted by trade without permission)
- Mark on drawing any actual deviations found (photo + note)
- Report deviations to GC PM immediately (before major rework is needed)

**Trade Compliance:**
- Each foreman gets a copy of coordination drawing (printed or digital)
- Crew is briefed: "Stay on the coordination drawing; if you're off, notify your foreman"
- Deviations must be approved by GC before proceeding (no "creative" rerouting)

### Common Coordination Drawing Mistakes

| Mistake | Consequence | Prevention |
|---------|-------------|-----------|
| **Coordination drawing created AFTER trades start** | Conflicts already built in; expensive rework | Require coordination drawing approval BEFORE trade starts (minimum 3 days before start) |
| **Only two trades included** (e.g., ductwork + electrical, missing plumbing) | Plumbing arrives and finds conflicts not identified | All MEP trades included; require input from ALL trades with above-ceiling/in-wall work |
| **Conflicts marked but not resolved** (conflict list without resolution) | Trades don't know who moves or when | Every conflict must have a resolution signed by responsible trade before field distribution |
| **Coordination drawing not updated** (original issued, field changes not reflected) | Superintendent walks to verify, drawing is out of date, confusion | Minor changes OK (documented in field notes); major changes trigger new coordination drawing revision |
| **Drawing so cluttered it's unreadable** | Too much color, too many lines, legend missing | Limit to key area (zone the building; create separate coordination drawing for each zone if needed) |

---

## 8. TRADE SEQUENCING BY AREA (Preventing Interference)

The goal is to allow one trade to work in an area, complete 100%, be inspected, and then release that area to the next trade. This prevents rework and inspection complications.

### Typical Interior Finish Sequence
This sequence works for most commercial buildings. Adapt to your project specifics.

```
AREA A (E.g., Conference Room 201)

1. FRAMING (Frame walls, door openings, blocking)
   Status: ✓ Complete & Verified by Architect
   Release: → to MEP

2. MEP ROUGH-IN (Electrical boxes, ductwork, plumbing, sprinkler)
   Status: ✓ Complete & Inspected (electrical, plumbing, mechanical all rough-in complete)
   Release: → to Insulation/Vapor Barrier

3. INSULATION & VAPOR BARRIER (Fiberglass insulation, vapor barrier if required)
   Status: ✓ Complete
   Release: → to Drywall

4. DRYWALL HANGING (Install drywall; tape/joint compound if included in this phase)
   Status: ✓ Drywall hung, ready for finish
   Release: → to Drywall Finishing OR Paint

5. DRYWALL FINISH (Tape, joint compound, sand, prime)
   Status: ✓ Smooth finish, ready for paint
   Release: → to Paint

6. PAINT
   Status: ✓ Paint applied, dry, ready for finishes
   Release: → to Flooring / Casework (depending on order)

7. FLOORING (Vinyl, carpet, tile, wood, etc.)
   Status: ✓ Flooring installed, cured, protected
   Release: → to Casework / Millwork

8. CASEWORK / MILLWORK (Built-in cabinets, shelving, counters)
   Status: ✓ Installed, hardware installed, finish inspected
   Release: → to MEP Trim

9. MEP TRIM (Electrical outlets, switches, thermostats, registers, vents)
   Status: ✓ Devices installed, connected, operational
   Release: → to Final Inspection

10. FINAL INSPECTION & PUNCH (Building inspector, architect, GC identify remaining items)
    Status: ✓ Area passed final inspection; punchlist documented
    Release: → to Punch Completion

11. PUNCH COMPLETION (Punchlist items addressed; final walk)
    Status: ✓ All punchlist items complete; area released to occupancy
    Release: → OCCUPANCY
```

### Area Release Criteria
Before releasing an area to the next trade, confirm:

1. **Work is 100% Complete** (not 95%, not "mostly")
   - All specified work for that trade in that area is done
   - No "we'll come back and finish later" exceptions
   - If you release incomplete, next trade will work around it (inefficient, rework likely)

2. **Inspection Complete** (if required by code/spec)
   - Electrical rough-in inspected (rough-in electrical inspection by authority)
   - Plumbing rough-in inspected (plumbing rough-in inspection)
   - Mechanical rough-in inspected (if code-required)
   - Any code-required inspection has passed before next trade enters

3. **Cleanup & Site Readiness**
   - Trade's debris removed from area (not piled in corner)
   - Area broom-swept or vacuum-swept (if necessary for next trade)
   - No tripping hazards left behind

4. **Documentation & Verification**
   - Superintendent (or trade) signs off: "Area A is complete and released to [next trade]"
   - Date signed; condition noted (any exceptions documented)
   - Photo taken if applicable (for disputes later)

### Color-Coded Area Status Map (Visual Tracking)
Large projects benefit from a visual area status:

Create a floor plan or grid showing each area's status:
- **RED** = Not started
- **YELLOW** = In progress
- **BLUE** = Waiting for inspection
- **GREEN** = Complete & released to next trade
- **GRAY** = Complete & awaiting final punch

Update daily. Post on job shack. This gives superintendent quick visual: "Area A is blue (waiting inspection). Area B is green. Area C is red (not started yet)."

### Common Sequencing Mistakes

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| **Releasing area before 100% complete** | Next trade finds unfinished work; works around it; rework needed later | Enforce completion requirement; do not release until trade foreman signs off |
| **Releasing before inspection** (when required) | Authority has to re-inspect later; may find non-conformance after next trade started; expensive re-work | Verify inspection is passed (document inspector sign-off) before release |
| **Allowing trade to "work ahead" (leapfrogging areas)** | Trades interfere; tools/materials everywhere; confusion about what's complete | Enforce sequential release; one area per trade at a time |
| **Not documenting releases** (verbal OK only) | Later dispute: "I didn't know they were done" → rework initiated | Document area releases in writing; superintendent signature required |

---

## 9. UNIVERSAL RULES FOR CROSS-TRADE COORDINATION

These rules apply across all coordination scenarios:

### Rule 1: Coordination Drawing Before Installation
- No trade starts MEP rough-in, framing, or major work until coordination drawing is approved and signed
- Coordination drawing must resolve all identified conflicts
- Trade cannot proceed "hoping" conflicts won't be an issue

### Rule 2: One Area at a Time, One Trade at a Time
- Do not allow trades to leapfrog areas or work simultaneously in same area (unless explicitly planned for dense high-rise)
- Release area only when previous trade is 100% complete and inspected
- Efficiency = sequential release; rework = parallel interference

### Rule 3: Pre-Installation Conference Mandatory
- Before structural steel, concrete, roofing, MEP rough-in, drywall, flooring, ceiling grid, elevator
- Identify coordination issues, sequencing, quality standards, testing
- Document in meeting minutes; issue to all trades
- No trade starts without pre-installation conference on record

### Rule 4: Embed & Penetration Schedule Before Pour
- Create detailed embed/penetration schedule for every slab/wall pour
- All trades verify locations before pour (physical walk, not just drawing review)
- No changes after concrete is placed (cost jumps 30–50× compared to pre-pour change)

### Rule 5: Verify Before You Commit
- Superintendent walks the area with marking plan before trade starts
- Verify location with actual building dimensions (not just drawing)
- Mark with tape/paint where systems go; allow trade to verify alignment before committing to layout

### Rule 6: Document Everything
- Coordination drawings: signed by all trades
- Area releases: signed off by trade and superintendent
- Conflicts & resolutions: documented in meeting minutes or change order
- Deviations: photo + date + explanation
- Disputes later: your documentation is defense

### Rule 7: The Resolution Hierarchy
When conflicts cannot be avoided:
1. Plumbing waste doesn't move (gravity-dependent)
2. Water supply/fire protection doesn't move (code-required routing)
3. HVAC is third to move (complex but doable)
4. Electrical moves last (most flexible)

### Rule 8: Communication = Prevention
- Regular coordination meetings (weekly if active construction)
- Superintendent walks jobsite with each trade foreman (inspect progress, identify issues early)
- Email/text updates when changes occur (all trades copied)
- No surprises on Friday afternoon; communicate all week

---

## Summary: Coordination Topics at a Glance

| Topic | Key Deliverable | Timing | Owner |
|-------|-----------------|--------|-------|
| **Above-Ceiling** | Coordination drawing (color-coded systems overlay) | Before rough-in (3+ days) | MEP Coordinator |
| **Underground Utilities** | Utility trench layout, crossing details, 811 call | Before excavation | Design Team + GC |
| **Wall Coordination** | Pre-drywall MEP layout, backing/blocking schedule | Before insulation (at framing completion) | GC Superintendent |
| **Slab Embeds & Sleeves** | Embed/penetration schedule, pre-pour walkdown | 2–3 days before pour | GC + All Trades |
| **Equipment Pads** | Equipment specs, pad design, connection details | Before equipment purchase (design phase) | Architect/Engineer |
| **Pre-Installation Conference** | Meeting minutes, action items, coordination decisions | Before every major trade | GC Superintendent |
| **Coordination Drawing** | Signed master overlay; conflict list with resolutions | Before rough-in starts | MEP Coordinator |
| **Area Release** | Signed completion/release documentation | After each area/phase complete | Superintendent |

---

## When to Call the Architect vs. When to Solve Onsite

| Situation | Call Architect | Solve Onsite |
|-----------|---|---|
| HVAC ductwork conflicts with electrical — who moves? | If ductwork is shown on architectural reflected ceiling plan | If layout is flexible (GC + trades decide per resolution hierarchy) |
| Embed location is 2' different from drawing | YES (verify if revision occurred; check if other systems affected) | Only if contractor confirms difference is acceptable to equipment owner |
| Wall needs oversized studs for plumbing; framing not accommodating | YES (may require design modification to wall) | No; this is design-required change |
| Water line must cross sewer line; cannot maintain 12" separation | YES (engineer designs crossing detail) | No; crossing requires code review |
| Equipment pad is too close to building edge; conflicts with egress | YES (layout must be modified per life safety code) | No; code-required change |
| Ceiling grid must shift 2' to avoid ductwork | If shift affects multiple trades or structure; otherwise | GC can approve minor grid shift if it doesn't affect architectural finishes |
| Electrical boxes conflict with grab bar blocking | NO (GC + Electrical + Framing solve during pre-drywall) | Reposition one element; document change |

---

**END OF CROSS-TRADE COORDINATION REFERENCE**
