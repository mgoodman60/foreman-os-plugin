# Concrete Field Operations Reference
**Foreman OS Plugin | Practical Field Reference**

---

## 1. SLUMP RANGES BY APPLICATION

### Standard Slump Requirements (ACI 301)

| Application | Slump Range | Notes | Testing Frequency |
|---|---|---|---|
| **Footings, mass concrete** | 2-4" | Stiff mix, minimal vibration required | Every 150 CY |
| **Walls, columns (exposed)** | 4-6" | Self-consolidating, vibration still needed | Every load |
| **Slabs on grade** | 4-5" | Finishable without over-working, good flow | Every 100 CY |
| **Beams, columns (structural)** | 4-6" | Standard range, vibration required | Every load |
| **Pumped concrete** | 4-6" | Minimum 4" (pumpability critical) | Every load pumped |
| **Decorative, architectural** | 3-5" | Spec-dependent; tighter control | Every load |
| **Flowable fill (non-structural)** | 8"+ | Self-leveling, rapid setup | As-needed |

### Slump Test Field Procedure (ASTM C143)

**Equipment**:
- Standard cone (12" tall, 8" dia. base, 4" dia. top)
- Measuring stick (marked at 1" intervals)
- Wet concrete sample (fresh from truck, 15 min. old typical)

**Steps**:
1. Lift cone vertically, measure drop of concrete at highest point
2. Record to nearest 0.5 inch
3. **Variation rule**: Do NOT accept single test; average at least 2 tests
4. If tests vary >1", reject sample (contamination, segregation, age)

**Field acceptance**:
- Average slump within specified range = ACCEPT
- Slump too low (stiff): Cannot accept; return truck
- Slump too high (flowable): Indicates excessive water added
  - Batch ticket water content vs. submitted mix design
  - If over-watered, reject or add retarder (consult supplier)

### High-Slump Concrete & Superplasticizers

**Normal slump (4") vs. High-slump (8"+) with superplasticizer**:
- Same water-cement ratio (W/C) can achieve higher slump
- Superplasticizer allows fluidity without additional water
- Result: Same strength potential, better workability
- Cost: +$3-8/CY for admixture

**Field advantage**: Pumped concrete or rapid-set finishes benefit from plasticizer-induced slump without strength compromise.

**Caution**: Slump drop occurs over time (1-2" per 30 minutes typical). Test immediately after truck arrival. Retest if time elapsed >1 hour before placement.

---

## 2. AIR ENTRAINMENT REQUIREMENTS

### Air Content by Exposure & Application

| Exposure Type | Aggregate Size | Required Air % | Purpose |
|---|---|---|---|
| **Hard-troweled floors (interior, no freeze-thaw)** | Any | 3% MAX | Higher air = blistering, delamination |
| **Moderate freeze-thaw exposure** | #57 aggregate (3/4") | 5.0-6.0% | ~275 cycles freeze-thaw resistance |
| **Severe freeze-thaw exposure** | #57 aggregate | 6.0-7.5% | Cold climate, deicing salt zones |
| **Moderate F/T, fine aggregate (sand)** | < 3/8" | 5.5-7.0% | Adjust for fine material |
| **Non-air-entrained (interior only)** | Any | 1-2% trapped | Natural entrapment, no agent needed |

### Air Content Test Method (ASTM C231, Pressure Meter Type B)

**Standard procedure** (most common):
1. Fill Type B pressure meter with wet concrete (3 layers, tamp each)
2. Apply air pressure per procedure (typically 7.5 psi gauge)
3. Read dial at stabilization (±1 psi variation acceptable)
4. Record air content percentage

**Field rule**: Test every truck arrival if air-entrained concrete. Acceptable range: ±1.5% from spec (example: spec 6% = accept 4.5-7.5%).

**Variability causes**:
- High slump concrete = lower measured air (fluidity masks air)
- Cold concrete = lower measured air (pressure meter less sensitive)
- Lightweight aggregate = different readings (use ASTM C173 if specified)
- Admixture reactions (retarders, accelerators) = slight variation

### Hard-Troweled Floor (Maximum Air Content)

**Critical control**: Do NOT exceed 3% total air (entrained + trapped).
- Reasons: Air voids near surface blister, delaminate during troweling
- Causes: Excess entrainment agent, retarder interaction, over-vibration trapping air
- Mitigation:
  - Reduce air-entrainment agent dose by 0.5-1 oz/CY
  - Avoid over-vibration (vibrate only until concrete settles)
  - Air test every load; reject if >3%

**Surface finish impact**: Blistering typically appears 7-14 days post-cure (thermal release of trapped air). Prevention during placement eliminates costly grinding/patching.

### Freeze-Thaw Exposure Verification

**When to use 5.0-7.5% air**:
- Above grade exterior concrete
- Patios, parking lots subject to deicing salt
- Structures in Climate Zone 4 or higher (cold winter regions)
- Verify with project specifications or geotechnical report

**When to use non-air-entrained**:
- Interior structural concrete (no weather exposure)
- Below-grade (groundwater contact, no F/T cycles)
- Decorative flatwork not exposed to salts

---

## 3. COLD WEATHER CONCRETE (ACI 306 STANDARD)

### Cold Weather Definition & Trigger

**Cold weather = ANY of the following**:
- Ambient temperature below 40°F
- Temperature expected to drop below 40°F within 24 hours of placement
- Early morning work in fall/spring with frost risk

### Concrete Temperature at Placement

| Section Thickness | Minimum Placement Temperature | Notes |
|---|---|---|
| Thin sections (slabs 4-6") | 50°F concrete | Small mass, cools quickly |
| Medium (walls, beams 6-12") | 55°F concrete | Standard cold weather placement |
| Mass concrete (footings, piers >12") | 60-65°F concrete | Large mass retains heat longer |

**Temperature measurement** (ASTM C1064):
- Insert thermometer 3 inches into fresh concrete
- Wait 30-60 seconds for equilibration
- Record to nearest 1°F
- Accept concrete only if temperature within range

### Protection Period (Critical for Strength Gain)

**Minimum curing temperature: 50°F** (failure to maintain = strength loss, durability issues)

**Required duration**:
- **Thin sections (4-6")**: 48 hours minimum at 50°F
- **Medium sections (6-12")**: 48-72 hours at 50°F
- **Mass concrete (>12")**: 72+ hours (verify with engineer)

**Strength consequence** (rule of thumb):
- Concrete below 40°F: Essentially ZERO strength gain (hydration pauses)
- Concrete 40-50°F: ~10-20% normal strength gain rate
- Below 32°F (freezing): Damage to immature concrete (ice formation expands)

### Cold Weather Mitigation Methods

**Insulated Blankets** (temporary insulation)
- Cost: $2-5/SF (reusable, depreciate over projects)
- Setup: 2-4" rigid foam or blanket over forms
- Duration: 48-72 hours post-placement
- Effectiveness: Retains 15-25°F heat differential (ambient 20°F → concrete 40°F possible)
- Limitations: Only delays cooling; not indefinite protection

**Heated Enclosures** (tent + heater)
- Cost: $5-15/SF (temporary structure)
- Duration: 48-72 hours
- Effectiveness: Maintains 50°F+ ambient (heater = 30-50 kW typical)
- Fuel cost: $50-150/day (natural gas or propane)
- Best for: Walls, columns, exposed sections

**Ground Thaw Heaters** (subgrade warming)
- Cost: $200-500/day rental
- Duration: 3-7 days pre-placement (depends on soil depth)
- Purpose: Warm subgrade 4-6 inches before slab placement
- Effectiveness: Prevents conduction loss through frozen ground
- Application: Slabs on grade in northern climates

**Steam/Hot Water Curing** (embedded systems):
- Cost: $1,000-5,000 installation + fuel
- Duration: 48-72 hours
- Effectiveness: Accelerated strength (6-8°F above ambient per hour)
- Industry use: Precast plants, critical schedules
- Field use: Rare (cost-prohibitive)

### Calcium Chloride Restriction (Post-Tensioned & Galvanized Steel)

**DO NOT use calcium chloride accelerators if**:
- Post-tensioned concrete (chloride attacks steel tendons)
- Galvanized steel embedded (accelerates corrosion)
- Reinforcement in high-humidity environment

**Acceptable cold weather accelerators**:
- Non-chloride accelerators (triethanolamine, potassium salts)
- Retarder + internal heater (delayed set, extended workability)

**Field rule**: Confirm accelerator type with concrete supplier; confirm with engineer if structural component. Cost difference negligible; corrosion damage catastrophic.

### Never Place on Frozen Ground

**Consequence of frozen subgrade**:
- Concrete-to-soil separation (thaw settlement)
- Loss of bearing capacity (frost heave, soil movement)
- Slab cracking, differential settlement, structural failure

**Prevention**:
- Test subgrade temperature (thermometer 4-6" deep)
- If frost line present (frozen crust), thaw with heaters before slab placement
- Alternative: Delay placement until natural thaw (more common in mild climates)

---

## 4. HOT WEATHER CONCRETE (ACI 305 STANDARD)

### Hot Weather Definition & Conditions

**Hot weather = ANY**:
- Ambient temperature above 85°F
- Concrete temperature above 90°F at placement
- Low relative humidity (<40%) causing rapid evaporation
- High wind speed (>15 mph) accelerating surface drying

### Maximum Concrete Temperature at Placement

| Specification | Maximum Temperature |
|---|---|
| **Standard (most projects)** | 90°F concrete at placement |
| **Conservative (high risk)** | 85°F concrete |
| **Special (low permeability, high performance)** | 80°F concrete |

**Field adjustment**:
- Ice in mix water (cool 3-8°F)
- Cool aggregates with sprinklers (4-6 hours before mixing, air-dried)
- Use shaded stockpiles (aggregates exposed to sun = +10-20°F)
- Placement time: Early morning (6-8 AM) or evening (4-6 PM)

### Mitigation Measures (In Priority Order)

**1. Reduce concrete temperature at placement**
   - Ice in water: 1 pound ice per CY ≈ 2-3°F reduction
   - Cost: ~$50-100/truck addition
   - Most effective single measure

**2. Use retarding admixtures**
   - Slows set time 2-4 hours (allows better consolidation, curing)
   - Cost: +$1-3/CY
   - Benefit: Extends finish window, reduces early cracking

**3. Fog mist curing (immediate)**
   - Start curing (water spray) within 10-15 minutes of finish
   - Duration: 7 days continuous mist (or per spec)
   - Prevents plastic shrinkage cracking (major risk)
   - Cost: Labor + water (minimal)
   - Non-negotiable: Required for hot weather concrete

**4. Shade stockpiles & cover concrete in truck**
   - Shade net over aggregates (reduces solar heat)
   - White tarp over ready-mix truck during wait (reflects heat)
   - Cost: ~$100-200/truck (minimal, high value)

### Hot Weather Consequences (If Not Mitigated)

**Plastic shrinkage cracking**:
- Rapid surface drying faster than bleed water rise
- Cracks form 4-8 hours post-placement
- Shallow, interconnected network pattern
- Remedy: Fog mist curing immediately (prevention only, cannot repair after)

**Reduced workability**:
- Concrete stiffens faster (1-2 hours vs. 2-4 hours normal)
- Less time for placement, consolidation, finishing
- Risk: Improper consolidation, cold joints

**Lower strength at 28 days**:
- Rapid evaporation = higher water-cement ratio effectively
- Hot concrete cures faster initially (28-day strength may be normal, but early strength reduced)
- Long-term durability risk: Higher porosity, permeability

**Increased shrinkage cracking**:
- Drying occurs faster, more total drying
- Larger cracks, more frequent cracking pattern
- Prevention: Reduce W/C ratio, air entrainment (if appropriate), curing

### Field Checklist for Hot Weather Placement

- [ ] Concrete temperature <90°F confirmed at truck arrival
- [ ] Retarder dose confirmed with mix design
- [ ] Fog mist curing equipment on-site (hoses, nozzles, water supply)
- [ ] Finish crew briefed: Start curing 10-15 minutes after finish
- [ ] Shade structures (if available) over placement area
- [ ] Placement time early morning/evening if >95°F ambient
- [ ] Air test and slump test every load (workability verification)
- [ ] Extended curing period (7-10 days fog mist, not 3-day standard)

---

## 5. CYLINDER TESTING SCHEDULE (ACI 318 REQUIREMENTS)

### Standard Testing Protocol

| Test Age | Typical Use | Strength Expectation | Acceptance |
|---|---|---|---|
| **3-day** | Early monitoring only | 40-50% of 28-day | NOT for acceptance |
| **7-day** | Optional progress check | 65-75% of 28-day | Can be tracked trend |
| **28-day** | Standard acceptance | 100% (reference) | REQUIRED for acceptance |

**Field rule**: 28-day breaks are required for structural acceptance. 7-day breaks optional (useful for early form removal decisions, early strength verification).

### Sampling Frequency (ACI 301)

| Scenario | Sampling Rate |
|---|---|
| Standard construction | 1 set per 150 CY per day |
| Elevated risk (large pour, critical strength) | 1 set per 100 CY |
| Frequent placements | 1 set per day minimum (even if <150 CY) |
| High-rise / continuous placement | 1 set per lift or per 4 hours |

**Set definition**:
- 6"x12" cylinders: Minimum 2 per set
- 4"x8" cylinders: Minimum 3 per set (smaller = more variation)
- Standard practice: 2 samples per set = 2 breaks (one at 28-day, reserve for 56-day if needed)

### Cylinder Casting (ASTM C31)

**Equipment**:
- Molds: Plastic or steel, standard sizes (6"x12" or 4"x8")
- Tamper rod: 5/8" diameter, rounded end
- Vibration table or hand rodding

**Field Procedure**:

1. **Fill in layers**:
   - 6"x12" cylinder: 2 equal layers (3" each)
   - 4"x8" cylinder: 3 equal layers (~2.7" each)

2. **Rod each layer**: 25 roddings per layer (distribute evenly)
   - Insert rod vertically through concrete
   - Withdraw slowly, do not jab excessively (creates segregation)
   - Rod must penetrate previous layer ~1"

3. **Tap mold**: Light striking with mallet between layers (removes air voids)

4. **Strike-off top**: Level with mold top, smooth finish

5. **Identification**: Mark mold with project, date, time, mix design number

6. **Curing**:
   - 24 hours in mold at room temperature (68-77°F ideal)
   - Remove from mold after 24 hours
   - Cure in moist room (95%+ humidity) or saturated lime water until test
   - Transport to lab in sealed plastic bag (prevents moisture loss)

**Cold weather adjustment**: If <50°F ambient, keep cylinders inside (heated space) for first 24 hours, then move to curing condition.

### Acceptance Criteria (ACI 318)

**Acceptance requires BOTH conditions**:

1. **Average of any 3 consecutive tests ≥ f'c** (specified strength)
   - Example: f'c = 4,000 psi
   - Three consecutive 28-day results: 4,100, 3,950, 4,200 psi
   - Average = 4,083 psi ≥ 4,000 psi ✓ PASS

2. **No individual test < (f'c - 500 psi)**
   - Example: f'c = 4,000 psi
   - Minimum acceptable single break = 3,500 psi
   - Single result of 3,400 psi = FAIL (even if average OK)

**Failure consequence**:
- Concrete may be tested in-place (core drilling, compressive testing)
- Load testing may be required
- Cost: $5,000-20,000+ for failure investigation
- Schedule delay: 2-4 weeks typical

### Field Tips for Cylinder Reliability

- **Temperature control**: Curing temperature variation = strength variation (±5°F = ±3-5% strength)
- **Moisture loss**: Cylinders cured dry (not moist room) = lower strength (not representative of field)
- **Rodding technique**: Under-rodded = low strength; over-rodded = high strength (not representative)
- **Mold sealing**: Air-tight curing (sealed plastic bags) = most accurate (representative of actual concrete behavior)

---

## 6. POUR CARD & FIELD DOCUMENTATION

### Pre-Pour Verification Checklist

- [ ] **Forms & Supports**:
  - Forms clean, properly braced, checked for dimensional accuracy
  - Shoring verified for load-carrying capacity
  - Joint locations marked (control joints, expansion joints)
  - Form release agent applied (if no staining risk)

- [ ] **Rebar & Embedded Items**:
  - Rebar inspection completed (quantity, spacing, cover verification)
  - Concrete cover requirements marked (minimum cover depth to outer rebar)
  - Dowels, anchors, embed plates positioned and secured
  - Utility sleeves, blockouts, conduits in place

- [ ] **Preparation**:
  - Forms wetted (absorbs water, prevents form suction)
  - Debris removed (leaves, dust, dirt in forms = weak bond)
  - Temperature: Ambient >50°F, subgrade not frozen

- [ ] **Batch Ticket Review**:
  - Mix design number matches approved submittal
  - W/C ratio acceptable (if sensitive application)
  - Air content, slump specifications correct
  - Batch time, truck arrival time logged

### Pour Card Template (Field Documentation)

```
PROJECT: _______________  DATE: __________  LOCATION: ______________

BATCH INFORMATION
  Mix Design: _______  Batch Ticket #: _______  Truck #: _______
  Concrete Supplier: ______________  Delivery Time: _______

PLACEMENT CONDITIONS
  Ambient Temperature: ______°F    Concrete Temp: ______°F
  Weather: [ ] Clear [ ] Cloudy [ ] Rain [ ] Hot/Dry/Windy
  Wind Speed: ______ mph    Humidity: ______ %

CONCRETE ACCEPTANCE
  Slump: ______ inches (specify: ___" ± ___")
  Air Content: ______ % (specify: ___% ± __%)
  REJECT: [ ] YES [ ] NO  (If yes, reason: _______________)

PLACEMENT DETAILS
  Method: [ ] Pump [ ] Bucket [ ] Chute [ ] Conveyor [ ] Direct dump
  Placement Duration: _____ hours
  Vibrator Type: [ ] Immersion [ ] Form [ ] Table
  Vibrator Duration per Location: _____ seconds

CYLINDER CASTING
  Time Cast: _______  Number of Sets: _____
  Curing Method: [ ] Moist room [ ] Field cured [ ] Sealed bags
  Set 1 ID: _______  Set 2 ID: _______  Set 3 ID: _______

FINISH & CURING
  Finish Method: [ ] Broom [ ] Trowel [ ] Float [ ] Power finish
  Fog Mist Start Time: _______  Duration: ______ days
  Form Strip Timing: [ ] 24 hr [ ] 3 day [ ] 7 day [ ] Engineer approval
  Curing Method: [ ] Membrane [ ] Wet burlap [ ] Plastic cover [ ] Misting

NOTES
  Special conditions: _________________________________
  Non-conformances: __________________________________
  Weather delays: ____________________________________

SIGNATURES
  Superintendent: ________________  Date: _______
  Inspector: ____________________  Date: _______
```

### During-Pour Monitoring

**Real-time observations** (document on pour card):
- Slump loss over time (acceptable: 1-2" per 2 hours)
- Air content consistency (variation >1.5% indicates problem)
- Vibration effectiveness (observe aggregate settlement, void elimination)
- Finishing window (time available for proper finish before set)
- Labor performance (adequate crew size, skill level, efficiency)

**Critical interventions**:
- Concrete too stiff (slump <spec): Do NOT add water (violates W/C)
  - Action: Reject load or consult engineer for admixture adjustment
- Concrete too fluid (slump >spec): Indicates over-water or segregation
  - Action: Reject load
- Air content out of range (>1.5% variation): Indicates batching error
  - Action: Investigate with supplier, monitor next load

### Post-Pour Documentation

- **Curing initiation**: Record start date/time of misting, membranes
- **Form removal timing**: Document when forms stripped (typically 24-72 hours per ACI)
- **Early strength**: If 7-day cylinders available, note if meeting expectation
- **Weather exposure**: Record any weather events (heavy rain, frost risk) during curing period
- **Non-conformances**: Document any deviations (late curing, delayed finishing, temperature extremes)

---

## 7. COMMON FIELD PROBLEMS & CORRECTIONS

### Honeycombing (Voids in Concrete Surface)

**Cause**:
- Inadequate vibration (concrete not fully consolidated)
- Mix too stiff (slump too low, not flowing into forms)
- Rebar spacing too tight (concrete cannot flow between bars)
- Air pockets not released during vibration

**Prevention** (in order of priority):
1. Verify slump within spec (4-6" typical allows consolidation)
2. Vibrate 10-20 seconds per location (zone overlap required)
3. Ensure rebar spacing ≥ 1" clear (minimum for concrete flow)
4. Use immersion vibrator (not form vibration alone)

**Repair**:
- Shallow honeycombing (< 0.5"): Acceptable if isolated (verify with engineer)
- Deep honeycombing (≥ 0.5"): Repair required
  - Chip out voids to solid concrete
  - Clean compressed air, water
  - Patch with concrete putty or epoxy injection (per engineer)
  - Cost: $50-150/SF for extensive repair

### Cold Joints (Horizontal Separation Between Lifts)

**Cause**:
- Delay between concrete lifts (>30 minutes typical)
- Surface hardened before next lift placed
- Weak bond between old and new concrete

**Prevention**:
1. Keep surface "live" (still plastic/workable)
2. Continuous placement within 30 minutes of previous lift
3. Roughen surface before next lift if delay occurs (light broom sweep)
4. Apply bonding agent (if engineer-approved)

**Field decision**:
- If delay <1 hour: Resume placement, keep surface wet
- If delay >2 hours: Consider lift as complete; plan next lift per contract (day-joint, construction joint)

**Repair**:
- Cold joints at side forms (faces) often acceptable (cosmetic)
- Cold joints affecting structural capacity: Core testing required
- Remedy: Epoxy injection along joint plane (engineer evaluation)

### Plastic Shrinkage Cracking (Early, Random Pattern)

**Cause**:
- Rapid surface drying (hot, dry, windy weather)
- Drying faster than bleed water can rise
- Typically occurs 4-8 hours post-placement, before final set

**Prevention** (mandatory in hot weather):
1. **Fog mist immediately** (10-15 minutes after finish)
   - Keep surface damp continuously for 7 days
   - Most effective single control
2. Reduce concrete surface temperature (shade covers, cool aggregates)
3. Use evaporation retarder (spray applied, reduces moisture loss)
4. Place during cooler times of day (early morning/evening)

**Repair**:
- Prevention only; cracks cannot be sealed after hardening
- If occurred: Monitor for pattern (typically minor, non-structural)
- Cosmetic repair: Sealant in cracks if appearance critical

### Scaling (Surface Deterioration from Freeze-Thaw or Deicing Salt)

**Cause**:
- Insufficient air entrainment (no air voids to accommodate ice expansion)
- Premature finishing (before bleed water rises, traps water in surface)
- Deicing salt exposure without air entrainment
- Surface permeability too high (poor quality)

**Prevention**:
1. **Air entrainment** (5-7.5% for F/T exposure) — CRITICAL
2. **Do NOT finish early** (wait for bleed water to evaporate naturally)
3. **Moist curing** (saturated conditions prevent drying, ingress)
4. **Avoid deicing salts** (specify salt-free de-icing alternatives if possible)

**Field verification**:
- Air content test: Confirm 5-7.5% for any exterior/freeze-thaw exposure
- Do NOT accept high-slump concrete if scaling risk (indicates low air)

**Repair**:
- Limited options; scaling indicates structural deterioration
- Minor scaling: Cosmetic coating
- Extensive scaling: Surface grinding, replacement of affected section

### Popouts (Small Surface Protrusions/Spalls)

**Cause**:
- Reactive aggregate (chert, opaline chert, strained quartz)
- Aggregate particle expands during hydration or thermal cycling
- Typically near surface (within 1/2")
- Appears 6-24 months post-construction

**Prevention**:
1. Specify non-reactive aggregates in geotechnical report
2. Avoid specific regions known for reactive aggregates
3. Use low W/C ratio (limits moisture availability for reaction)

**Field remedy**: Limited once occurred
- Monitoring: Document frequency, location
- If structural: Core testing may be required
- Cosmetic: Patching if needed

**Caution**: Popouts may indicate alkali-aggregate reaction (AAR) — structural concern. Investigate if pattern spreading.

### Blistering & Delamination (Subsurface Voids)

**Cause**:
- High air content (>3%) in hard-troweled floors
- Over-finishing (seals surface, traps subsurface air)
- Rapid set (accelerators) = insufficient bleed time
- Surface curing too early (moisture trapped below)

**Prevention**:
1. **Limit air content to 3% maximum** for hard-troweled finishes
2. **Do NOT over-finish** (avoid excess troweling, sealing surface early)
3. **Allow bleed time** (finish only after moisture evaporates naturally)
4. Avoid rapid-set accelerators unless necessary

**Field control**:
- Air test every load for hard-troweled floors
- Reject if >3.5% air
- Instruct finishers: Light finishing only, minimal troweling passes

**Repair**:
- Blister <1 SF: Cosmetic acceptance
- Blister >1 SF or delaminated: Grinding, epoxy injection, or section replacement
- Cost: $5,000-50,000+ depending on extent

---

## 8. FIELD TESTING QUICK REFERENCE

### Slump Test (ASTM C143)

**Equipment**: Slump cone (standard size), straightedge, measuring ruler

**Procedure**:
1. Place cone on smooth, level surface
2. Fill with 3 equal layers
3. Rod each layer 25 times (penetrate previous layer ~1")
4. Strike off top level with cone rim
5. Lift cone vertically (slow, no horizontal movement)
6. Measure vertical distance from original top to slumped peak
7. **Acceptance**: Repeat if necessary; average 2+ tests

**Field use**: Every truck arrival, every 150 CY per ACI
**Acceptance window**: Within ±1" of specified slump

---

### Air Content Test (ASTM C231, Pressure Meter Type B)

**Equipment**: Type B pressure meter (Chappuis meter), tamper rod, ruler

**Procedure**:
1. Fill Type B meter with 3 equal layers (concrete sample)
2. Rod each layer 25 times
3. Strike off top level
4. Add water cap to top, apply water to bring level to graduated mark
5. Insert air piston, apply pressure (typically 7.5 psi gauge)
6. Stabilize pressure, note needle position
7. Read air content (%) directly from dial
8. **Acceptance**: Repeat if variation >1.5%

**Field use**: Every load for air-entrained concrete
**Acceptance window**: Within ±1.5% of specified air content (example: 6% ±1.5% = 4.5-7.5% acceptable)

---

### Concrete Temperature (ASTM C1064)

**Equipment**: Digital thermometer with probe (±1°F accuracy) or analog concrete thermometer

**Procedure**:
1. Insert probe 3 inches minimum into fresh concrete
2. Wait 30-60 seconds for stabilization (thermometer lag time)
3. Read temperature to nearest 1°F
4. **Acceptance**: Temperature within specified range (typically 50-90°F)

**Field use**: Every truck arrival, especially cold/hot weather
**Cold weather placement**: Minimum 50°F (verify before accepting concrete)
**Hot weather placement**: Maximum 90°F (mitigate if higher)

---

### Cylinder Casting (ASTM C31)

**Equipment**: Mold (6"x12" or 4"x8"), tamper rod, mallet, marking tools

**Procedure**:
1. Fill mold in layers (2 layers for 6"x12", 3 for 4"x8")
2. Rod each layer 25 times, penetrating previous layer ~1"
3. Tap mold sides gently (1-2 taps per location) to release air
4. Strike off top level with mold rim
5. Mark mold: Project, date, time, mix number, position
6. **Curing**: 24 hours at room temperature, then moist room or sealed bags

**Field use**: Per ACI — minimum 2 cylinders per set, per sampling frequency
**Critical**: Do NOT over-rod (creates high strength artificially) or under-rod (creates low strength, non-representative)

---

### Unit Weight (ASTM C138)

**Equipment**: Standard measure (0.5 CF typical), scale, strike rod, mallet

**Procedure**:
1. Fill measure with 3 equal layers
2. Rod each layer 25 times
3. Strike off top level
4. Weigh filled measure (include mold weight)
5. Tare mold weight
6. Calculate: Unit weight (lbs/CF) = (Total weight - Mold weight) / Measure volume

**Field use**: Useful for quality control (if weight drops >5 lbs/CF, indicates low consolidation)
**Acceptance**: ±3% of expected unit weight (based on mix design)

---

## FIELD DECISION FLOWCHART: CONCRETE ACCEPTANCE

```
CONCRETE TRUCK ARRIVES

├─ CHECK DOCUMENTATION
│  ├─ Match batch ticket to purchase order (mix design, qty)
│  ├─ Verify delivery time (concrete age: reject if >1.5 hours old)
│  ├─ Confirm strength, slump, air requirements
│  └─ If mismatch → REJECT truck
│
├─ SLUMP TEST
│  ├─ Test 2 samples, average results
│  ├─ Compare to specification (±1")
│  ├─ If low (too stiff) → Cannot add water; REJECT
│  ├─ If high (too fluid) → Indicates water added; REJECT or consult engineer
│  └─ If acceptable → Continue
│
├─ AIR CONTENT TEST (if air-entrained specified)
│  ├─ Test pressure meter
│  ├─ Record result (±1.5% of spec)
│  ├─ If >3% for hard-troweled floors → REJECT
│  ├─ If outside range → REJECT or consult engineer
│  └─ If acceptable → Continue
│
├─ TEMPERATURE TEST
│  ├─ Cold weather: Minimum 50°F
│  ├─ Hot weather: Maximum 90°F
│  ├─ If out of range → REJECT
│  └─ If acceptable → Continue
│
├─ VISUAL INSPECTION
│  ├─ Check for segregation (coarse aggregate at top, paste below)
│  ├─ Check for discoloration (indicates chemical issue)
│  ├─ If severe segregation → REJECT
│  └─ If acceptable → Continue
│
├─ CAST CYLINDERS
│  ├─ Minimum 2 per set per ASTM C31
│  ├─ Identify with project, date, time, mix number
│  ├─ Cure per specification (moist room or sealed bags)
│  └─ Label for 28-day break
│
└─ ACCEPTANCE DECISION
   ├─ All tests pass → ACCEPT, proceed with placement
   ├─ Any test fails → REJECT
   │  ├─ Contact concrete supplier
   │  ├─ Document rejection reason
   │  ├─ Arrange truck return (cost to supplier if defective)
   │  └─ Notify ready-mix plant of issue
   └─ Unusual result → Consult engineer before accepting
```

---

## UNIVERSAL FIELD RULES

1. **Project specifications and approved mix designs override all general guidelines** — Always consult submittal data, project specs, and engineer approvals before final decisions.

2. **Air entrainment is non-negotiable for freeze-thaw exposure** — Omitting air from freeze-thaw concrete is a structural deficiency (scaling, deterioration inevitable).

3. **Cold weather concrete below 40°F gains no strength** — Freeze risk is real; insulation/heating is required, not optional.

4. **Fog mist curing is mandatory in hot weather** — Plastic shrinkage cracks appear 4-8 hours post-placement; prevention-only control.

5. **28-day cylinder breaks are the acceptance standard** — Early breaks (7-day, 3-day) are informational only; final strength verified at 28 days.

6. **Slump and air content variation indicates a problem** — Investigate batch-to-batch inconsistency (supplier issue, material variation, or admixture error).

7. **Do NOT modify concrete at placement** — Adding water, accelerators, or retarders in the field without engineer approval voids mix design and warranty.

8. **Documentation protects everyone** — Complete pour card, test results, and weather notes prevent disputes on strength, timing, and conformance.

---

## QUICK REFERENCE TABLES

### Strength Gain vs. Temperature (Approximate % of 28-Day Strength)

| Age | 90°F | 70°F | 50°F | 40°F |
|---|---|---|---|---|
| 3 days | 55% | 40% | 20% | 5% |
| 7 days | 75% | 65% | 35% | 10% |
| 14 days | 90% | 85% | 60% | 25% |
| 28 days | 95% | 100% | 85% | 50% |
| 90 days | 100% | 110% | 110% | 90% |

**Key insight**: Curing temperature affects rate; cold curing delays strength but may achieve similar 90-day strength. Freezing (below 32°F) causes permanent damage.

---

### Cylinder Strength Quality Acceptance (f'c = 4,000 psi Example)

| Test Result | 28-Day Average (Avg of Last 3) | Pass / Fail | Reason |
|---|---|---|---|
| 4,100 / 4,050 / 3,950 psi | 4,033 psi | PASS | Average ≥ 4,000 psi; no result <3,500 psi |
| 4,200 / 3,900 / 3,500 psi | 3,867 psi | FAIL | Average <4,000 psi |
| 4,100 / 4,100 / 3,400 psi | 3,867 psi | FAIL | One result <3,500 psi (minimum acceptance) |
| 4,100 / 4,050 / 4,000 psi | 4,050 psi | PASS | Average ≥ 4,000 psi; all >3,500 psi |

---

**Document Version**: Field Reference 1.0
**Last Updated**: 2026
**Always Verify**: Project specifications, approved mix designs, local building codes before final decisions
