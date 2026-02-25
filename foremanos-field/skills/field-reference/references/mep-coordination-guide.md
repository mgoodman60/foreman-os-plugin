# MEP Coordination Field Guide
## Mechanical, Electrical, Plumbing System Routing & Above-Ceiling Installation

---

## 1. CEILING CAVITY DEPTH REQUIREMENTS

### Minimum Clearance Above T-Bar Ceiling
- **Base rule:** 6 inches minimum above grid for MEP routing
- **Reality check:** This is inadequate for most buildings; see below

### Typical Space Requirements by System (Depth from Structure)

| System | Min Depth | Typical Depth | Notes |
|--------|-----------|---------------|-------|
| HVAC main duct | 12" | 18-24" | Varies with CFM and ductwork size |
| HVAC branch duct | 8" | 12-14" | Smaller CFM = less depth |
| Plumbing drain | 6" | 9-12" | Includes 1/4" slope + 6" clearance |
| Fire sprinkler main | 4" | 5-6" | Pressure pipe, runs relatively flat |
| Fire sprinkler branch | 2" | 3-4" | Small diameter, flexible routing |
| Electrical conduit | 1" | 3-4" | Protection from mechanical damage |
| Cable tray | 4" | 6-8" | Need support structure too |

### Real-World Depth Targets
- **Standard commercial:** 24-30 inches minimum above finished ceiling
  - Allows main HVAC, plumbing waste, sprinkler, electrical to coexist
- **Healthcare/Lab buildings:** 36-48 inches minimum
  - More systems, stricter separation (infection control in healthcare)
  - Labs may need additional mechanical exhaust, special gases
- **Server rooms / Data centers:** 36-48 inches minimum
  - Redundant electrical, high-capacity cooling, cabling density

### How to Verify Adequate Depth
1. **Review design documents:** Floor plans should show soffit/cavity height
2. **Measure:** Verify finished ceiling height vs. structure above
3. **Calculate:** Structure height - finished floor height - finished ceiling height = cavity depth
4. **Add buffer:** If result is <24", escalate to designer (may require lower ceiling grid or higher structure)

### What Happens with Insufficient Depth
- Trades routing conflicts (forced re-routing)
- Squashed ductwork (reduces CFM, increases noise)
- No room for insulation (thermal/acoustic performance fails)
- Inspection difficulty (can't see or access)
- Future maintenance nightmare (plumber can't get to valve, electrician can't pull wire)

---

## 2. PIPE SLEEVE SIZING

### Sleeve Formula
**Sleeve diameter = Pipe OD + Insulation thickness + 1" clearance**

### Common Examples
| Pipe Type | OD | Insulation | Sleeve ID | Sleeve OD |
|-----------|----|-----------|-----------|-----------|
| 2" copper supply | 2.125" | 0.5" | 4.25" | 5" steel sleeve |
| 3" PVC drain | 3.5" | 0" | 4.5" | 5" steel sleeve |
| 4" ductile iron | 4.75" | 0.5" | 6.75" | 7" steel sleeve |
| 6" HVAC duct | 6.5" | 1" | 8.5" | 9" steel sleeve (or composite) |
| 1/2" PEX supply | 0.625" | 0.5" | 2.125" | 2.5" steel sleeve |

### Wall vs. Floor Installation Differences

**Fire-Rated Walls:**
- Steel sleeve required (maintains fire rating)
- Fire caulk per UL listed system (seals annular space)
- Both inside AND outside of wall perimeter must be caulked
- Inspection: third-party firestop inspector before wall closure

**Non-Rated Walls:**
- PVC or steel sleeve acceptable
- No fire caulk required
- Annular space can be sealed with standard caulk or left open

**Slab Penetrations:**
- Sleeve extends 1 inch above finished floor (prevents tracking, water pooling)
- Flush or slightly recessed below finished slab below
- Anchor with concrete collar pour (prevents sleeve rotation)
- Location coordination: **CRITICAL** — core drilling is expensive and weakens slab

### Pre-Concrete Coordination Critical Path
1. **Mechanical designer provides pipe schedule** with OD + insulation
2. **Structural engineer approves sleeve locations** (some near columns forbidden)
3. **Concrete contractor flags sleeve locations** in form work
4. **Sleeves installed in form** before concrete pour
5. **Pipes routed through sleeves** during rough-in
6. **Annular space sealed** after pipes installed

**Why this matters:** Core drilling to add a missed sleeve = $500-$2000 per hole + structural repair + schedule delay.

---

## 3. FIRE-STOPPING REQUIREMENTS

### What Needs Fire-Stopping
**Every penetration through a fire-rated assembly must be fire-stopped.**

Examples:
- Pipe through drywall wall
- Ductwork through floor assembly
- Conduit through rated partition
- Blank opening (future penetration) in rated wall
- Cable bundles through floor

### Fire Rating Terminology
- **F-Rating (Flame):** Minutes before flame appears on unexposed side of assembly
  - Example: 1-hour wall, F-60 system = flames prevented for 60 minutes
- **T-Rating (Temperature):** Minutes before temperature on unexposed side exceeds 140°C (284°F)
  - Example: 2-hour wall, T-120 system = temperature controlled for 120 minutes
- **Combined:** Both F and T ratings must meet or exceed the assembly rating
  - 1-hour wall = needs F-60 AND T-60 firestop system minimum
  - 2-hour wall = needs F-120 AND T-120 firestop system minimum

### Common Firestop Materials by Pipe Type

**Metallic Pipe (Steel, Copper)**
- **Method:** Intumescent caulk + mineral fiber insulation
- **Example:** 3M Intumescent caulk (red) + mineral fiber collar
- **Installation:** Caulk applied 5/8" depth minimum, mineral fiber loosely packed behind
- **UL listing:** Must be per UL 1479 listed system (use part number, not generic material)

**Plastic Pipe ≤4" (PVC, PEX, ABS)**
- **Method:** Intumescent wrap strip OR intumescent collar
- **Why:** Plastic melts in fire; intumescent material expands to block gap
- **Example:** Specified wrap strip, measured and sized to pipe OD
- **Installation:** Wrapped around pipe, over-lapped per instructions, caulked edges
- **Temperature rating:** Pipe must have proper rating (not all plastics rated for fire-rated assemblies)

**Plastic Pipe >4"**
- **Method:** Requires specific UL system (no generic wrap applicable)
- **Examples:** Mechanical restraint device, cast-in-place intumescent, or approved collar
- **Complexity:** Usually requires engineer review (cost + time)
- **Prevention:** Specify metallic piping through fire-rated walls when possible (costs less to firestop)

**Cable / Conduit Bundles**
- **Method:** Firestop mortar or firestop pillows + caulk
- **Density rule:** If cable fills <25% of opening, use pillows; >25% use mortar or special system
- **Expansion:** Material must accommodate thermal expansion during fire
- **Example:** Specified firestop mortar (by part number), applied to fill opening and surrounding annular space

**Blank Openings (Future Penetrations)**
- **Method:** Firestop mortar or pillows rated for the specific opening size
- **Sizing:** Opening size limited by manufacturer (e.g., max 4" x 4" opening, max 1" depth)
- **Larger openings:** Require frame + damper or other system

### Minimum Caulk Depth
- **1-hour assembly:** 5/8 inch minimum on both sides of wall/floor
- **2-hour assembly:** 5/8 inch minimum (depth doesn't increase, but test standards change)
- **Measurement:** Depth = distance of caulk packed into joint/annular space

### Installation Critical Points
1. **Annular space:** Gap between sleeve/pipe and surrounding material (drywall, concrete)
   - Too large (>1/2"): more material needed, potential voids
   - Properly sized: 1/4" to 1/2" is target
2. **No substitutions:** If UL system specifies Brand X caulk + Manufacturer Y mineral fiber, use exactly those products
   - Substituting "equivalent" materials voids listing
3. **Workmanship:** Voids in caulk = breach points; caulk must be continuous
4. **Cure time:** Some systems require 24-hour cure before exposure (check label)

### Inspection & Documentation
- **Third-party firestop inspector:** Common on commercial projects (required by some codes/lenders)
- **Photo documentation:** Every firestopped penetration photographed before wall closure
  - Photo must show pipe/conduit, caulk, and surrounding assembly
  - Date-stamp required
- **Firestop schedule:** Match-line drawing showing all firestopped penetrations
- **Warranty:** Firestop contractor typically provides 10-year workmanship warranty

---

## 4. ELECTRICAL CLEARANCES (NEC REQUIREMENTS)

### Working Space In Front of Panels
- **Minimum:** 36 inches (or greater if equipment label specifies)
- **Width:** 30 inches minimum (or equipment width, whichever is greater)
- **Height:** 6.5 feet minimum (6'-6" to above ceiling is preferred)
- **Examples:**
  - 24"-wide panel in 36"-wide space: NOT sufficient (need 30" width minimum)
  - 36"-wide panel: needs full 36" + 30" width = 66" x 36" clear floor space minimum

### Dedicated Space Above Panel
- **Required:** Extend to ceiling or structural floor directly above (no pipes, ducts, conduits)
- **Why:** Working space must be completely clear for breaker access and air circulation
- **Common violation:** HVAC duct routed above panel = ductwork must be relocated
- **Height:** If ceiling suspended, extend clear space to structural ceiling, not drop ceiling

### Panel Height & Handle Location
- **Breaker handle height:** 6'-7" maximum above finished floor (NEC 240.33)
- **All handle positions:** Operating handles must be reachable within this range
- **Bottom of panel:** Minimum clearance to floor (some codes: 18", verify local)
- **Side-by-side panels:** Each panel must have independent 36" x 30" minimum workspace (cannot share)

### Transformer Clearances
- **Access side:** 36 inches minimum
- **Other sides:** Per NEC 450.21 (typically 12" minimum)
- **Overhead:** No ductwork directly above
- **Ventilation:** Transformer must have adequate air flow (overcooling adds cost; undercooling = overheating failure)

### ADA Reach Range for Accessible Controls
- **Height:** 15-48 inches above finished floor (center of control)
- **Examples:**
  - Light switch at 48" = compliant
  - Electrical outlet at 18" = compliant
  - Thermostat at 60" = NOT accessible (too high)
- **Horizontal approach:** Minimum 18" clear space in front of control
- **Side approach:** Minimum 12" clear space

### Common Electrical / MEP Conflicts
| Conflict | Problem | Solution |
|----------|---------|----------|
| HVAC duct above panel | No clear space | Relocate duct or panel; document in RFI |
| Plumbing over panel workspace | Water damage risk | Relocate plumbing upstream |
| Low-volt cabling across panel face | Access obstruction | Route behind panel or in separate tray |
| Panel in mechanical room with no door | Maintenance access | Verify 36" clear space to next wall |
| Panel too high or too low | ADA non-compliant | Height check at trim-out phase |

---

## 5. PLUMBING SLOPE REQUIREMENTS

### Minimum Slope Rates (Must Not Exceed)
- **Sanitary drain ≤3" diameter:** 1/4 inch per foot minimum
  - Over 100 feet = 25 inches of elevation change
  - Over 50 feet = 12.5 inches
  - Rule: if horizontal run exceeds 20 feet, watch slope accumulation
- **Sanitary drain 4"+ diameter:** 1/8 inch per foot minimum
  - Larger pipes = lower velocity OK
  - Common for building mains and building sewers
- **Storm drain:** 1/8 inch per foot minimum (1/4" preferred for ≤3")
  - Storm volumes vary; steeper slope = more capacity
- **Condensate drain:** 1/8 inch per foot minimum
  - From HVAC coil to sump or exterior
  - Blockage = ice backup in winter
- **Grease waste:** 1/4 inch per foot minimum
  - Grease congeals if slope too shallow
  - Must slope continuously (no high spots)
- **Vent pipes:** Minimum 1/4 inch per foot slope BACK toward drain connection
  - Yes, vents slope too (prevents trap seal loss from water pocket)

### Slope Accumulation Example
| Distance | At 1/4"/ft | At 1/8"/ft |
|----------|------------|------------|
| 20 feet | 5" drop | 2.5" drop |
| 40 feet | 10" drop | 5" drop |
| 100 feet | 25" drop | 12.5" drop |
| 200 feet | 50" drop | 25" drop |

**Key takeaway:** Long horizontal runs accumulate significant elevation change. Verify finished floor elevation + pipe elevations match slope requirements.

### How Slope Failures Occur
1. **No slope installed** (pipe level)
   - Solids accumulate, slow drainage, backups
2. **Slope installed wrong direction** (upslope toward trap)
   - Water flows backward or puddles
3. **Slope lost in subsidence** (settling soil, pipe sags)
   - Soft trench = pipe sags over time
4. **Slope reversed mid-run** (high spot in middle)
   - Water pocket = organic growth, odors

### Field Verification of Slope
- **Tool:** Laser level or water level (not a 2-foot bubble level)
- **Method:** Shoot elevation at starting and ending point of run
- **Math:** (Start elevation - End elevation) / (Distance in feet) = slope per foot
- **Check:** If slope is less than minimum, it's a violation (requires rework)

### Common Sloping Mistakes to Prevent
- **Sanitary main slopes too much (>1/4"):** Creates high velocity, can separate P-trap seals
- **Kitchen grease line installed level:** Grease hardens immediately; plugs within weeks
- **Vent installed without slope:** Condensation pools in vent; water runs down drain side = siphoning
- **Slope drops below fixture:** Fixture can't drain (no gravity help); requires higher vent

---

## 6. HVAC DUCT SIZING BASICS

### Velocity Method (Standard Design Approach)
- **Main ducts:** 1000-1500 feet per minute (FPM)
  - Higher velocity = smaller duct (saves space, costs more in noise)
  - Lower velocity = larger duct (costs more in material, quieter)
- **Branch ducts:** 600-900 FPM
  - Smaller branches = higher velocity noise
  - Size up for quieter operation (especially bedrooms, classrooms)
- **Return ducts:** 700-900 FPM
  - Avoid undersizing return (creates house pressure, reduces supply)

### Equivalent Round Diameter (Critical Error Point)
- **Rectangular duct area ≠ actual CFM capacity**
- **Example:** 12" x 8" rectangular ≠ 10" round (same perimeter, different area)
  - 12" x 8" rectangular area = 96 sq inches
  - 10" round area = 78.5 sq inches
  - The round is SMALLER, will reduce CFM or increase velocity
- **Design requirement:** Use duct calculator or tables (SMACNA standard)
- **Field check:** If duct looks small, ask for duct size verification (don't assume "close enough")

### Duct Insulation Requirements
- **Supply ductwork in unconditioned spaces:** R-6 minimum
  - Examples: supply duct routed through attic, crawlspace, or exterior wall cavity
  - R-4 acceptable only in light commercial with short runs
- **Return ductwork in unconditioned spaces:** R-4 minimum
  - Less critical than supply (return temperature closer to ambient)
- **Mechanical room ducts:** R-4 minimum (some codes: none, but bad practice)

### Duct Clearance from Structure
- **Minimum clearance:** 2 inches from insulated ductwork to structure
  - Allows for slight sag, expansion, inspection access
  - Closer = risk of touching joist = condensation drip onto below space
- **Rigid ductwork:** 1 inch minimum clearance acceptable (more stable)
- **Fiberglass ductboard:** 2 inch minimum (more likely to sag)

### Support Spacing (SMACNA Standard)
- **Rectangular ducts:** 8-10 feet maximum between hangers
  - Longer spacing = sag risk
  - Lighter gauge = tighter spacing
- **Round ducts:** 10-12 feet maximum
  - More rigid; holds span better than rectangular
- **Hangers:** Proper sizing required (typically ductstrap or rod hangers)
  - Under-sized hanger = sag over time = velocity change = noise + performance loss

### Kitchen Grease Ductwork (Special Case)
- **Material:** 16-gauge steel minimum (type 304 stainless preferred, costs 2-3x)
- **Seams:** Fully welded (no screws, rivets, or sealed with sealant only)
  - Grease vapor escapes through seams
- **Slope:** Minimum 1/4 inch per foot TOWARD grease collection (gravity feed)
- **Cleanout:** Access points every 20 feet; cleanout at lowest point (sump)
- **Isolation:** Cannot mix exhaust in supply path (separate ductwork)
- **Fire suppression:** Type I hood required (with ansul system typically)

---

## 7. STANDARD TRADE SEQUENCE FOR ABOVE-CEILING ROUGH-IN

### Why Sequence Matters
Trades have different flexibility:
- **Least flexible:** Plumbing waste (needs slope, can't change elevation)
- **Most flexible:** Low-voltage cabling (can route anywhere)

### Recommended Order (Typical Commercial)

**Phase 1: Structural Support**
1. Structural framing installed (beams, joists verified)
2. Hangers and attachment points installed (per MEP drawings)

**Phase 2: Plumbing Waste/Vent**
3. **Plumbing waste/vent rough-in** (sanitary + storm)
   - Goes first because slope requirement = inflexible routing
   - Vent pipes sloped per code
   - Inspect before next trade (can't move once others over top)

**Phase 3: Fire Safety**
4. Fire sprinkler mains and branch lines installed
   - Mid-priority (moderate flexibility)
   - Cannot be relocated once drywall closes

**Phase 4: Mechanical**
5. HVAC ductwork installed (supply, return, exhaust)
   - Largest system = occupies most space
   - Install after plumbing (routes around as needed)
   - Seal ductwork; inspect before closure

**Phase 5: Plumbing Supply**
6. Plumbing supply lines (hot, cold, recirculation)
   - Can route around other systems
   - Lower priority than waste

**Phase 6: Electrical**
7. Electrical conduit and cable tray installed
   - High flexibility (can route around other systems)
   - Rough-in conduit for future wire pull

**Phase 7: Low-Voltage**
8. Low-voltage cabling (data, security, fire alarm, controls)
   - Maximum flexibility
   - Pull after conduit rough-in, before insulation

**Phase 8: Insulation & Close-Up**
9. Duct insulation applied (supply, return)
10. Pipe insulation applied (plumbing supply, condensate)
11. Acoustic treatment if required

**Phase 9: Above-Ceiling Inspection**
12. All trades walk above-ceiling together
    - Verify complete; all penetrations protected
    - Document any deficiencies

**Phase 10: Closure**
13. Drywall hung / ceiling grid installed
14. Final inspections per code

### Phase-Gate Inspections
- **After Phase 2 (plumbing waste):** Verify slope, no kinks, clean install
- **After Phase 4 (HVAC ductwork):** Verify seal, support spacing, clearances
- **After Phase 7 (electrical):** Verify conduit support, no physical damage
- **After Phase 8 (insulation):** Verify R-value, no compression, no voids

---

## 8. MEP COORDINATION MEETING FRAMEWORK

### Pre-Construction Coordination (Before Trades Start)

**Agenda:**
- Review ceiling height and cavity depth (confirm adequate)
- Review composite overlay drawings (all systems on one drawing)
- Confirm routing priorities and conflict resolution process
- Establish code requirements and inspection schedule
- Identify critical dimensions: panel heights, cleanout access, equipment room space

**Deliverables:**
- Clash detection report (3D model shows conflicts identified)
- Coordination drawing set (composite = all trades on one plan)
- Sequence agreement (order of rough-in phases)
- RFI log (design questions captured)

**Timing:** 2-4 weeks before first rough-in trade starts

### Weekly Coordination During Rough-In

**Process:**
1. **Site walk:** Every Friday (or after major work phase)
2. **Attendance:** General contractor + all active trade foremen
3. **Route walk:** Walk every ceiling area, observe conditions, discuss any conflicts
4. **Conflict resolution:** Real-time decisions
   - Example: HVAC duct hits sprinkler main → lower duct 2", relocate sprinkler 1 bay
5. **Schedule adjustment:** Confirm next week's activities; identify dependencies
6. **Photos:** Document progress, any rework needed

**Duration:** 30-60 minutes (depends on project size)

### Pre-Close-Up Coordination (Before Ceiling Closure)

**Checklist:**
- [ ] All MEP rough-in complete (no unfinished runs)
- [ ] All penetrations marked and fire-stopped (where applicable)
- [ ] All ductwork sealed and insulated
- [ ] All pipes insulated (supply, condensate)
- [ ] All support hangers in place and secure
- [ ] All equipment clearances verified (panel working space, transformer access, etc.)
- [ ] All above-ceiling voids accessible (no blocked access)
- [ ] Inspection schedule confirmed (code inspector, third-party firestop if required)

**Responsible party:** General contractor foreman (with subcontractor checklist sign-off)

**Timing:** 1-2 weeks before drywall/ceiling closure

### Documentation System

**Coordination Drawings:**
- Composite overlay: 1:1/8" or 1:1/4" scale showing all trades
- Color-coded (each trade different color)
- Updated weekly as trades shift to avoid conflicts
- Sent via email or uploaded to BIM model

**RFI Log:**
- Question, affected trades, proposed solution, approval date
- Prevents same issues being resolved twice
- Reference point if similar conflict recurs

**Photo Log:**
- Weekly photos of above-ceiling conditions (timestamped)
- Before/after rework (if conflicts resolved mid-installation)
- Proof of coordination efforts (useful if code dispute later)

**Meeting Minutes:**
- Weekly meeting summary: who attended, what was coordinated, decisions made
- Action items assigned to specific person + deadline
- Signed by general contractor

---

## Quick Reference: Who Pays for Conflicts?

| Situation | Payer | Prevention |
|-----------|-------|-----------|
| Ductwork hits existing column | HVAC (design error) | Clash detection in design phase |
| Plumbing waste not sloped correctly | Plumbing (installation error) | Phase-gate inspection after rough-in |
| Electrical panel in HVAC return path | Designer (layout error) | Pre-construction coordination |
| Sprinkler line cut by HVAC installer | Sprinkler + HVAC (mutual negligence) | Clear labeling + site coordination |
| Low-volt conduit run through supply duct | Electrical (site improvisation) | Weekly walk + clear "no go" zones |

**Rule:** Coordinate early, document often, walk weekly. Conflicts caught in pre-construction cost nothing. Conflicts found during drywall closure cost tens of thousands.

---

## 9. DUCTWORK INSTALLATION STANDARDS

### Sheet Metal Gauge by Duct Size (SMACNA Reference)

| Duct Dimension (Largest Side) | Minimum Gauge (Low Pressure, up to 2" w.g.) | Minimum Gauge (Medium Pressure, 2-6" w.g.) |
|-------------------------------|---------------------------------------------|---------------------------------------------|
| Up to 12" | 26 gauge | 24 gauge |
| 13" to 30" | 24 gauge | 22 gauge |
| 31" to 60" | 22 gauge | 20 gauge |
| 61" to 84" | 20 gauge | 18 gauge |
| 85" and larger | 18 gauge | 16 gauge |

**Field verification**: Measure sheet metal thickness with micrometer or reference manufacturer tag. Under-gauge ductwork = oil-canning (popping noise under pressure), eventual fatigue failure, and air leakage at seams.

### Seam Types

**Pittsburgh Lock Seam**
- Most common longitudinal seam for rectangular ductwork
- One edge folded into pocket; mating edge inserted and crimped
- Use for: standard rectangular ducts, all pressure classes
- Advantages: strong, airtight, fast assembly with roll-forming machine
- Limitation: requires straight run (cannot use on curved sections)

**Standing Seam**
- Both edges folded upward and interlocked
- Use for: round/oval spiral ductwork longitudinal seam
- Advantages: very strong, excellent air seal, smooth interior
- Limitation: requires factory fabrication (not field-formable)

**Drive Cleat (S-Cleat and Drive Slip)**
- S-shaped or Z-shaped metal clip connects two duct sections at transverse joint
- Use for: transverse joints on rectangular ductwork (connecting straight sections)
- S-cleat: standard for ducts up to 36" wide
- Drive slip: for larger ducts, provides additional rigidity
- Seal required: mastic or tape sealant on all transverse joints per pressure class

**Field decision**: Pittsburgh lock for longitudinal seams, S-cleat or drive cleat for transverse joints. Standing seam only on factory-fabricated spiral round duct.

### Duct Support and Hanger Spacing (per SMACNA)

| Duct Size (Largest Dimension) | Maximum Hanger Spacing | Hanger Type |
|-------------------------------|----------------------|-------------|
| Up to 30" | 10 feet | Strap hanger (1" wide galvanized) |
| 31" to 60" | 8 feet | Trapeze hanger (angle iron frame) |
| 61" to 96" | 6 feet | Trapeze hanger (heavy-duty) |
| Over 96" | 4-6 feet (engineered) | Structural support (engineered design) |

**Round duct**: 12 feet maximum spacing for round ducts up to 24" diameter; 10 feet for larger.

**Hanger rod sizing**:
- 3/8" diameter: ducts up to 48" wide
- 1/2" diameter: ducts 49" to 72" wide
- 5/8" diameter: ducts over 72" wide
- All-thread rod with nuts and washers at both ends (top and bottom connections)

**Attachment to structure**: Beam clamps, concrete inserts, or powder-actuated fasteners. Never attach hangers to other trades' supports, fire sprinkler piping, or non-structural elements.

### Duct Sealing Classes

| Seal Class | Pressure Classification | Sealing Requirement | Typical Application |
|-----------|------------------------|--------------------|--------------------|
| Class A | 4" w.g. and above | All transverse joints, longitudinal seams, and duct wall penetrations sealed | Supply mains, high-pressure systems |
| Class B | 3" w.g. and above (positive), 2" w.g. and above (negative) | All transverse joints and longitudinal seams sealed | Standard supply and return ducts |
| Class C | 2" w.g. and above (positive), 1" w.g. and above (negative) | Transverse joints only sealed | Low-pressure return ducts, exhaust |

**Sealant types**:
- Mastic (water-based): most common, applied with brush or glove; use on all joints and seams
- Tape (UL 181A for rigid, UL 181B for flex): backup or primary seal for transverse joints
- Gaskets: pre-formed for flanged connections (TDC, TDF flanges)
- Silicone or butyl sealant: for specialty applications (high-temperature, chemical exhaust)

**Field rule**: When in doubt, seal to Class A. The cost of sealant is minimal compared to the energy loss and balancing problems caused by leaking ductwork.

### Flexible Duct

**Maximum Length**
- Code maximum: varies by jurisdiction; many limit to 5 feet for supply connections
- SMACNA recommendation: as short as practical; never exceed 14 feet
- Best practice: limit to 5 feet for terminal connections (diffuser or register takeoff)
- Excessive length = high pressure drop, noise, and reduced airflow

**Installation Requirements**
- Must be fully extended (no compression or bunching; compressed flex duct has 5-10x the pressure drop)
- No kinking: minimum bend radius = one duct diameter (e.g., 6" flex duct = 6" minimum bend radius)
- Support every 5 feet maximum (sag between supports reduces effective diameter)
- Proper connection: inner liner pulled over collar, secured with draw band (not just tape)
- Outer jacket secured with draw band or zip tie
- Mastic seal at collar connection (tape alone is insufficient for code compliance in most jurisdictions)

**Prohibited uses:**
- Vertical risers (flex duct collapses under own weight)
- Through fire-rated assemblies (flex duct is not fire-rated)
- Return air plenums (most codes prohibit)
- Concealed spaces where not accessible for future maintenance

### Insulation

**Internal Insulation (Duct Liner)**
- Material: fiberglass duct liner with coated air-stream surface
- Thickness: 1" typical (R-4.2), 2" for high-performance (R-8.4)
- Application: inside supply ductwork for thermal and acoustic performance
- Advantages: reduces duct noise (sound attenuation), provides thermal insulation
- Limitations: can trap moisture, fiber release concern (must have coated surface), reduces effective duct cross-section
- Prohibited: commercial kitchen exhaust, laboratory exhaust, hospital operating rooms

**External Insulation (Duct Wrap)**
- Material: fiberglass blanket with vapor barrier facing (FSK - foil scrim kraft)
- Thickness: 1.5" (R-6) standard for supply in unconditioned spaces; 2" (R-8) for energy code compliance in some climate zones
- Vapor barrier: required on all supply ductwork in cooling climates (prevents condensation)
- Vapor barrier must face outward (warm side) with all seams taped and sealed
- Staple spacing: 6" maximum along seams
- No compression: compressed insulation loses R-value (2" compressed to 1" = approximately R-3 instead of R-8)

**R-Value Requirements (Energy Code Reference)**
- Supply ducts in unconditioned spaces: R-6 minimum (many jurisdictions now require R-8)
- Return ducts in unconditioned spaces: R-4 minimum (some jurisdictions R-6)
- Supply ducts in conditioned spaces: typically no insulation required (unless acoustic concerns)
- Verify with applicable energy code (IECC, ASHRAE 90.1, or state-specific)

### Fire Damper Installation

**Access Requirements**
- Minimum 16" x 16" access door on ductwork adjacent to each fire damper
- Access must allow visual inspection of damper blade and fusible link
- Access panel on accessible side of wall/ceiling (not above permanent fixtures)
- If damper in inaccessible location: coordinate relocation before installation

**Sleeve Details**
- Fire damper installed in steel sleeve that penetrates fire-rated assembly
- Sleeve size: match duct size (damper fits inside sleeve)
- Sleeve gauge: 16 gauge minimum (breakaway connection excepted)
- Sleeve extends through full thickness of wall/floor assembly
- Retaining angle on each side of wall secures sleeve in assembly
- Seal between sleeve and wall with fire-rated material (caulk or mineral fiber per UL listing)

**Breakaway Connections**
- Ductwork connects to fire damper sleeve with breakaway joint
- Purpose: if fire causes ductwork to fall or shift, duct separates from sleeve without pulling damper out of wall
- Connection: light-gauge S-cleat or sheet metal screws in duct flange (designed to shear under load)
- Required per NFPA 90A: ductwork shall not prevent damper from closing

---

## 10. PIPING INSTALLATION STANDARDS

### Copper Pipe Types

| Type | Wall Thickness | Color Code | Application |
|------|---------------|------------|-------------|
| Type K | Heaviest | Green | Underground water service, refrigeration |
| Type L | Medium | Blue | Interior water distribution (hot and cold), above-ground general use |
| Type M | Thinnest | Red | Domestic water where code allows, low-pressure applications |

**Selection rule**: Type L is the standard for commercial interior water distribution. Type M acceptable for residential in many jurisdictions (check local code). Type K for underground or high-pressure applications.

**Joining Methods**
- Soldering: most common for copper-to-copper joints
- Brazing: for high-temperature or high-pressure applications (refrigeration, medical gas)
- Press fittings (ProPress): mechanical crimp connection; faster installation, no flame required
- Flare fittings: for soft copper tubing connections (gas lines, refrigeration)

### Solder Types

**Lead-free solder required for potable water systems** (Safe Drinking Water Act)
- 95/5 tin-antimony: most common lead-free solder for plumbing
- Tin-silver (96/4): higher strength, better for larger pipe sizes
- Lead-containing solder (50/50 tin-lead): prohibited for potable water; permitted only for non-potable applications (drain, waste, vent)

**Flux**: water-soluble flux required for potable water; petroleum-based flux prohibited (contaminates water).

**Field rule**: If you see silver-colored solder on potable water joints, it is likely compliant. If you see dark gray solder, it may be lead-containing and requires investigation/replacement.

### PEX Pipe Types

| Type | Manufacturing Process | Fitting Method | Expansion Coefficient |
|------|----------------------|----------------|----------------------|
| PEX-A | Engel (peroxide) crosslinking | Expansion fittings (cold expansion + ring) | Highest flexibility; can repair kinks with heat gun |
| PEX-B | Silane crosslinking | Crimp rings or clamp rings | Most common; good balance of cost and performance |
| PEX-C | Electron beam crosslinking | Crimp rings or clamp rings | Least flexible; less common in commercial |

**Connection methods:**
- PEX-A: expansion tool expands pipe end; fitting inserted; pipe contracts around fitting (strongest joint)
- PEX-B/C: fitting inserted into pipe; crimp ring compressed around pipe with crimp tool (fastest installation)
- Clamp rings (Oetiker style): stainless steel ring with ear; compressed with clamp tool

**Installation rules:**
- Support spacing: every 32" for horizontal runs; every 4-6 feet for vertical
- Minimum bend radius: 6x pipe diameter (e.g., 1" PEX = 6" minimum bend radius)
- No kinking: kinked PEX restricts flow; PEX-A can be repaired with heat gun; PEX-B/C must be cut and re-fitted
- UV protection: PEX degrades in sunlight; protect from UV exposure during storage and installation
- Not permitted for: fire sprinkler mains (CPVC or steel required in most jurisdictions), exposed locations subject to physical damage

### Support Spacing by Pipe Size and Material

**Copper Pipe (per ASME B31.9)**

| Pipe Size | Horizontal Spacing | Vertical Spacing |
|-----------|-------------------|------------------|
| 1/2" - 3/4" | 6 feet | 10 feet |
| 1" - 1-1/4" | 8 feet | 10 feet |
| 1-1/2" - 2" | 10 feet | 10 feet |
| 2-1/2" - 3" | 12 feet | 15 feet |
| 4" and larger | 12 feet | 15 feet |

**Steel Pipe (per ASME B31.9)**

| Pipe Size | Horizontal Spacing | Vertical Spacing |
|-----------|-------------------|------------------|
| 1/2" - 3/4" | 7 feet | 15 feet |
| 1" | 7 feet | 15 feet |
| 1-1/2" - 2" | 10 feet | 15 feet |
| 2-1/2" - 3" | 12 feet | 15 feet |
| 4" - 6" | 15 feet | 15 feet |
| 8" and larger | 17 feet | 15 feet |

**PVC/CPVC (per ASTM F708)**

| Pipe Size | Horizontal Spacing (at 73 degrees F) | Note |
|-----------|--------------------------------------|------|
| 1/2" - 1" | 3 feet | Spacing reduces at higher temperatures |
| 1-1/4" - 2" | 4 feet | CPVC hot water: reduce to 3 feet |
| 2-1/2" - 4" | 4 feet | Continuous support at horizontal changes in direction |
| 6" and larger | 5 feet | Engineered support design recommended |

**Cast Iron (Hubless/No-Hub)**

| Pipe Size | Horizontal Spacing |
|-----------|-------------------|
| 1-1/2" - 4" | 5 feet (every joint + mid-span) |
| 5" - 8" | 5 feet |
| 10" and larger | Every joint + 5 feet maximum between |

### Expansion and Contraction

**Thermal Movement Rates (per 100 feet of pipe for 100 degrees F temperature change)**
- Steel: 0.75 inches
- Copper: 1.12 inches
- PVC: 3.60 inches
- CPVC: 2.40 inches
- PEX: 1.08 inches (similar to copper)

**Expansion Accommodation Methods**
- **Expansion loops**: U-shaped pipe detour allowing movement; size loop legs per pipe diameter and expected movement
- **Expansion offsets**: Z-shaped pipe routing using elbows to absorb movement
- **Expansion joints**: bellows or slip-type devices allowing axial movement; anchors required on each side
- **Bellows**: flexible corrugated metal element; use for large diameter or high-movement applications

**Calculation**: Movement (inches) = coefficient x pipe length (feet) / 100 x temperature change (degrees F) / 100

**Anchor and guide placement**: Anchors fix pipe at specific points; guides allow axial movement only; place anchors at midpoint of expansion loop and at each end of straight run. Guides spaced per SMACNA or engineering calculation.

### Pressure Testing

**Hydrostatic Test (Water)**
- Test pressure: 1.5x maximum operating pressure (e.g., 80 PSI operating = 120 PSI test)
- Duration: minimum 2 hours (some specifications require 4 or 24 hours)
- Acceptance: no visible leaks, pressure drop less than 5% over test duration (adjust for temperature)
- Procedure: fill system, bleed all air, pressurize with hand pump or test pump, isolate, observe
- Documentation: initial pressure, final pressure, time, temperature, inspector signature

**Pneumatic Test (Air)**
- Test pressure: 1.1x maximum operating pressure (lower than hydrostatic due to stored energy hazard)
- Duration: minimum 2 hours
- Acceptance: no audible leaks, pressure drop less than 1.5 PSI per hour
- Safety: pneumatic testing carries burst hazard (air is compressible; water is not); all personnel clear of test area
- Use only when hydrostatic test is not practical (freezing conditions, system cannot be dried)

**Documentation requirements**: test form with system identification, test medium, test pressure, start/end times, start/end pressures, temperature, pass/fail, inspector signature.

### Insulation Requirements

**Condensation Prevention**
- All cold water piping in conditioned spaces: insulate to prevent condensation
- Minimum insulation: 1/2" wall thickness for pipes up to 1"; 1" wall for pipes 1-1/4" and larger
- Vapor barrier: required on all cold piping insulation; seal all joints and seams
- Condensation drip = ceiling damage, mold growth, slip hazard

**Energy Code Compliance**
- Domestic hot water piping: insulate per energy code (IECC Table C403.11.3 or equivalent)
- Hot water recirculation: insulate entire loop
- First 8 feet from water heater: insulate minimum R-4 (most jurisdictions)
- HVAC hydronic piping: insulate per ASHRAE 90.1 Table 6.8.3-1 (varies by fluid temperature and pipe size)

**Firestop at Penetrations**
- Insulated pipe through fire-rated assembly: firestop system must be tested with insulation in place
- UL listing specifies whether insulation passes through wall or stops at wall face
- Never assume fire-stop system is compatible with any insulation; verify UL listing
- Plastic piping insulation (rubber, foam): may require removal at wall penetration and replacement with mineral fiber within wall thickness

---

## 11. ELECTRICAL DISTRIBUTION AWARENESS

### Cable Sizing Awareness (NEC 310.16 Reference)

**Field reference for common conductor ampacities (75 degrees C column, copper)**

| Wire Size (AWG/kcmil) | Ampacity | Typical Breaker | Common Application |
|------------------------|----------|-----------------|-------------------|
| 14 AWG | 15 A | 15 A | General lighting circuits |
| 12 AWG | 20 A | 20 A | General receptacle circuits |
| 10 AWG | 30 A | 30 A | Small appliance, water heater |
| 8 AWG | 50 A | 50 A | Range, large appliance |
| 6 AWG | 65 A | 60 A | Welder, sub-panel |
| 4 AWG | 85 A | 80 A | Sub-panel, large motor |
| 2 AWG | 115 A | 100 A | Service entrance, sub-panel |
| 1/0 AWG | 150 A | 150 A | Service entrance |
| 2/0 AWG | 175 A | 175 A | Large service |
| 4/0 AWG | 230 A | 200 A | Main service entrance |
| 250 kcmil | 255 A | 225 A | Large commercial panel |
| 500 kcmil | 380 A | 350-400 A | Main distribution |

**Note**: This is a field reference only. Actual conductor sizing requires derating for temperature, conduit fill, continuous loads, and other NEC factors. Always verify with electrical engineer for design decisions.

### Conduit Fill (NEC Chapter 9)

**Maximum conductor fill by number of conductors:**
- 1 conductor: 53% of conduit cross-sectional area
- 2 conductors: 31% of conduit cross-sectional area
- 3 or more conductors: 40% of conduit cross-sectional area

**Common conduit sizes and approximate capacity (3+ conductors of same size):**

| Conduit Size | #12 AWG THHN | #10 AWG THHN | #8 AWG THHN | #6 AWG THHN |
|-------------|-------------|-------------|------------|------------|
| 1/2" EMT | 9 | 5 | 3 | 2 |
| 3/4" EMT | 16 | 10 | 6 | 4 |
| 1" EMT | 26 | 16 | 9 | 6 |
| 1-1/4" EMT | 46 | 28 | 16 | 11 |
| 1-1/2" EMT | 58 | 36 | 21 | 14 |
| 2" EMT | 96 | 58 | 34 | 23 |

**Field rule**: If conduit appears full or difficult to pull wire through, it likely exceeds fill limits. Do not force additional conductors; upsize conduit or add a parallel run.

### Cable Tray Support Spacing and Loading

**Support spacing:**
- Standard cable tray: 8-10 feet maximum between supports (check manufacturer load tables)
- Reduce spacing for heavy cable loads or vertical runs
- Support at each direction change (elbow, tee, cross)
- Supports must be independently anchored to structure (not suspended from other systems)

**Loading:**
- Calculate total cable weight per linear foot
- Compare to tray rated load capacity (manufacturer table)
- Include future cable allowance (typically 25% spare capacity)
- Cables must not extend above tray side rail height
- Maintain cable layering (do not exceed 2-3 layers for power cables)

### Termination Standards

**Torque Values by Lug Size (General Reference)**

| Lug Size | Typical Torque (inch-lbs) | Note |
|----------|--------------------------|------|
| #14 - #10 AWG | 20-25 in-lbs | Small lugs; do not over-torque |
| #8 - #6 AWG | 35-45 in-lbs | |
| #4 - #2 AWG | 50-70 in-lbs | |
| #1/0 - #4/0 AWG | 100-200 in-lbs | Verify with lug manufacturer |
| 250-500 kcmil | 250-375 in-lbs | Always verify specific lug torque |

**Critical**: Always use calibrated torque wrench. Over-torque damages conductor; under-torque causes high-resistance connection (heat, fire risk).

**Anti-oxidant compound**: Required for all aluminum conductor terminations. Apply to conductor and lug contact surfaces before assembly. Prevents aluminum oxide buildup (insulating layer that causes overheating). Not required for copper but often used as best practice on large connections.

### Grounding

**Equipment Grounding Conductor (EGC) Sizing (NEC Table 250.122)**

| Overcurrent Device Rating | Copper EGC Size | Aluminum EGC Size |
|---------------------------|----------------|-------------------|
| 15 A | 14 AWG | 12 AWG |
| 20 A | 12 AWG | 10 AWG |
| 60 A | 10 AWG | 8 AWG |
| 100 A | 8 AWG | 6 AWG |
| 200 A | 6 AWG | 4 AWG |
| 400 A | 3 AWG | 1 AWG |
| 800 A | 1/0 AWG | 3/0 AWG |

**Ground Rod Requirements**
- Minimum one ground rod at service entrance (NEC 250.52)
- Ground rod: 5/8" diameter minimum, 8 feet long, driven full depth
- If single rod resistance exceeds 25 ohms: install supplemental rod minimum 6 feet from first
- Bond to building steel, water piping (metallic), and concrete-encased electrode when available

### Panel Clearances (NEC 110.26)

**Working Space Requirements**

| Condition | Minimum Depth (Front) | Width | Height |
|-----------|----------------------|-------|--------|
| Condition 1: Exposed live parts on one side, no live or grounded parts on other | 36 inches | 30 inches or equipment width (whichever greater) | 6 feet 6 inches (floor to ceiling or obstruction) |
| Condition 2: Exposed live parts on one side, grounded parts on other | 36 inches | 30 inches or equipment width | 6 feet 6 inches |
| Condition 3: Exposed live parts on both sides (facing) | 48 inches (for 151-600V) | 30 inches or equipment width | 6 feet 6 inches |

**Dedicated equipment space**: Above and below panel extending to structural ceiling; no piping, ductwork, or other non-electrical equipment permitted in this space. Foreign systems passing through dedicated space must be protected (drip pan, shield).

**Common violations to watch for:**
- Storage in front of panels (boxes, materials, equipment)
- Plumbing or ductwork installed above panel after electrical rough-in
- Panel installed in closet too narrow for 30" working space
- Suspended ceiling tiles blocking access to dedicated space above panel

### Arc Flash Awareness

**Labeling Requirements (NFPA 70E / NEC 110.16)**
- Arc flash labels required on all panels, switchboards, switchgear, motor control centers
- Label must include: nominal system voltage, arc flash boundary, available incident energy (cal/cm2) or PPE category, limited and restricted approach boundaries
- Labels generated from arc flash study (performed by qualified electrical engineer)

**PPE Categories (NFPA 70E)**

| Category | Incident Energy Range | Required PPE |
|----------|----------------------|-------------|
| 1 | 4 cal/cm2 | Arc-rated shirt/pants (min 4 cal/cm2), safety glasses, hearing protection |
| 2 | 8 cal/cm2 | Arc-rated shirt/pants (min 8 cal/cm2), arc-rated face shield, balaclava |
| 3 | 25 cal/cm2 | Arc flash suit (min 25 cal/cm2), arc-rated hood, gloves |
| 4 | 40 cal/cm2 | Arc flash suit (min 40 cal/cm2), arc-rated hood, gloves |

**Approach Boundaries**
- Limited approach: boundary within which a shock hazard exists; only qualified persons may enter
- Restricted approach: closer boundary requiring PPE and specific training
- Arc flash boundary: distance where incident energy equals 1.2 cal/cm2 (onset of second-degree burn)
- Prohibited approach: treated same as making contact with live part

**Field rule**: Never open energized panels without proper arc flash PPE. If arc flash labels are missing, treat as Category 2 minimum until study completed. Always de-energize and verify zero energy before working inside panels when possible.

---

## 12. SYSTEM TESTING AND STARTUP PROCEDURES BY TRADE

### HVAC Testing

**Ductwork Leak Testing**
- Seal all openings (diffusers, grilles, access panels)
- Pressurize ductwork to design static pressure using calibrated fan
- Measure leakage rate with flow meter
- Acceptance: Class A duct leakage not to exceed CL = 4 CFM per 100 SF of duct surface area at 1" w.g. (SMACNA)
- If leakage exceeds limit: locate leaks with smoke pencil, seal, retest

**Hydronic Pressure Test**
- Fill system, bleed all air from high points
- Pressurize to 1.5x operating pressure (typical test: 225 PSI for 150 PSI system)
- Hold for minimum 2 hours
- Acceptance: no visible leaks, pressure drop less than 5%
- Document with test form

**Controls Checkout**
- Verify all sensors reading correctly (compare to independent instrument)
- Test each control sequence: heating, cooling, economizer, occupied/unoccupied
- Verify damper operation: open, close, modulate through full range
- Verify valve operation: open, close, modulate, fail-safe position correct
- Test alarms: high/low temperature, filter differential, equipment failure

**Testing, Adjusting, and Balancing (TAB)**
- Performed by independent TAB contractor (AABC or NEBB certified)
- Measure and adjust airflow at every diffuser and grille to within +/- 10% of design
- Measure and adjust water flow at every coil, terminal unit, and branch
- Document all readings in TAB report
- Provide report to engineer and owner for review

### Plumbing Testing

**DWV (Drain, Waste, Vent) Testing**
- Water test: fill system to highest point of DWV, hold for 15 minutes minimum
- Air test (alternative): pressurize to 5 PSI, hold for 15 minutes; pressure drop must not exceed 1.5 PSI
- All joints and connections visible and accessible during test
- Plug all openings except test point
- Acceptance: no visible leaks (water test) or pressure within tolerance (air test)

**Water Supply Pressure Test**
- Pressurize to design working pressure (typically 80-100 PSI for domestic water)
- Hold for minimum 2 hours (some specifications require 24 hours)
- Acceptance: no visible leaks, pressure stable within 5% of test pressure
- Test both hot and cold water systems independently if possible
- Document initial and final pressure, time, temperature

**Gas Pressure Test**
- Test pressure varies by jurisdiction: typically 3 PSI for low-pressure systems (under 0.5 PSI operating)
- Duration: minimum 30 minutes (some AHJs require longer)
- Use manometer or calibrated gauge (standard pressure gauges insufficient for low-pressure gas)
- Acceptance: no pressure drop detectable
- Safety: no flame or spark sources in test area; ventilate before and during test

**Backflow Preventer Testing**
- Required annually after installation (and at initial startup)
- Performed by certified backflow tester
- Test all reduced pressure zone (RPZ), double check valve (DCVA), and pressure vacuum breaker (PVB) assemblies
- Document test results on jurisdiction-approved form
- Submit to water utility and building department

### Electrical Testing

**Megger Testing (Insulation Resistance)**
- Test conductor insulation resistance with megohmmeter
- Apply test voltage appropriate for circuit voltage (500V DC for up to 600V circuits)
- Minimum acceptable reading: 1 megohm per 1,000 volts of circuit voltage (e.g., 480V circuit = 0.48 megohm minimum; practical minimum is 1 megohm)
- Test between each conductor and ground, and between each pair of conductors
- Low readings indicate: wet insulation, damaged insulation, contamination

**Phasing Verification**
- Verify correct phase rotation (A-B-C sequence) at all three-phase panels and equipment
- Use phase rotation meter before energizing motors
- Incorrect rotation: motors run backward (pumps, fans, compressors can be damaged)
- Verify phase-to-phase voltage balance within 2% at each panel

**Rotation Check**
- Bump-test all three-phase motors: briefly energize to verify correct rotation direction
- Check fan rotation matches airflow arrow on housing
- Check pump rotation matches casing arrow
- Incorrect rotation: swap any two phase conductors at disconnect or starter

**Functional Testing**
- Test each circuit breaker: manually trip and reset
- Test GFCI and AFCI devices: press test button, verify trip
- Verify all panel schedules match installed circuits
- Test emergency lighting and exit signs: simulate power failure, verify 90-minute battery backup
- Test generator and ATS per NFPA 110 requirements

### Fire Protection Testing

**Hydrostatic Test**
- Test pressure: 200 PSI for 2 hours (NFPA 13 standard for new sprinkler systems)
- All joints and fittings visible and accessible during test
- Acceptance: no visible leaks, no pressure drop
- Alternative for existing systems: 50 PSI above static pressure for 2 hours
- Document with test certificate signed by installer and witness

**Flushing**
- Flush all underground and overhead piping before connecting sprinkler heads
- Flush at design flow velocity or greater to remove debris, cutting oil, scale
- Continue flushing until water runs clear
- Document flush procedure and visual clarity of discharge water

**Trip Test (Dry Systems and Pre-Action)**
- Open inspector's test connection: verify alarm activates within 60 seconds
- For dry systems: measure trip time (time from test valve open to water delivery at inspector's test)
- Maximum trip time: 60 seconds for dry pipe valve
- For pre-action: verify detection system activates valve, then water delivery

**Alarm Test**
- Activate waterflow switch: verify fire alarm panel receives signal
- Verify signal transmitted to monitoring station
- Test tamper switches on all control valves: verify supervisory signal at panel
- Test pressure switches on fire pump controller

### Cross-Reference

For formal commissioning procedures including functional performance testing, integrated systems testing, seasonal testing, and commissioning documentation requirements, refer to the **closeout-commissioning** skill in this plugin library. The commissioning process builds on the trade-specific testing described above and adds:
- Owner's Project Requirements (OPR) verification
- Basis of Design (BOD) compliance confirmation
- Commissioning agent oversight and issue tracking
- Seasonal performance verification (heating season and cooling season)
- Systems manual and training documentation

### System Startup Sequence

**Recommended order for building systems startup:**

1. **Electrical**: Energize main service, verify voltage/phasing at all panels, energize branch circuits, test emergency power
2. **Plumbing**: Fill domestic water system, test and flush, activate water heaters, verify drainage and venting
3. **Fire protection**: Fill sprinkler system, hydrostatic test, activate fire pump, test alarms and monitoring
4. **HVAC**: Start boilers/chillers, fill and test hydronic systems, start air handling units
5. **Controls**: Commission BAS (Building Automation System), verify all control sequences, calibrate sensors
6. **TAB**: Test, adjust, and balance all air and water systems to design flows
7. **Commissioning**: Functional performance testing of integrated systems, deficiency resolution, owner training

**Why this sequence matters:**
- Electrical must be first (all other systems need power)
- Plumbing before fire protection (domestic water confirms building water supply is functional)
- Fire protection before HVAC (life safety systems operational before occupancy-related systems)
- HVAC before controls (equipment must run before control sequences can be verified)
- Controls before TAB (systems must be under automatic control for accurate balancing)
- Commissioning last (verifies all systems work together as designed)

**Field rule**: Never skip startup sequence steps. Each step verifies prerequisites for the next. Shortcutting the sequence causes rework, equipment damage, and failed inspections.
