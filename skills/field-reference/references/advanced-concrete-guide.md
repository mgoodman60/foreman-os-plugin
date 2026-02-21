# Advanced Concrete Operations Reference
**Foreman OS Plugin | Practical Field Reference**

---

## 1. MATURITY TESTING (ACI 1074 STANDARD)

### Concept & Purpose

**Maturity method** predicts concrete strength based on temperature history rather than relying solely on calendar time. Useful for:
- Cold weather construction (delayed strength gain)
- Early form removal decisions
- Post-tension stressing timing
- Accelerated schedules requiring early strength verification

**Principle**: Concrete strength is a function of time × temperature. A concrete cured at 40°F for 7 days gains similar strength to concrete cured at 70°F for 2-3 days.

### Maturity Index Fundamentals

**Maturity (M)** = Sum of (concrete temperature - reference temperature) × time

**Standard reference temperature**: 32°F (0°C)

**Example calculation**:
- Day 1: Concrete avg 60°F for 24 hours → (60 - 32) × 24 = 672 degree-days
- Day 2: Concrete avg 55°F for 24 hours → (55 - 32) × 24 = 552 degree-days
- Day 3: Concrete avg 50°F for 24 hours → (50 - 32) × 24 = 432 degree-days
- **Cumulative maturity after 3 days**: 1,656 degree-days

### Equipment Setup (Temperature Monitoring)

**Thermocouple Installation**:
- Type K thermocouples (most common, ±1°F accuracy)
- Install during casting: 3-4 thermocouples per pour location (typical)
- Placement: Near center of section, at depth representative of interior
- Lead wires: Run to data logger (located within 50 feet typical)

**Data Logger Setup**:
- Record interval: Every 15-30 minutes typical (minimum 60 min intervals acceptable)
- Battery life: 7-14 days typical (must last until maturity target reached)
- Download frequency: Daily or per schedule (prevent data loss)
- Accuracy: ±1°F temperature; time-stamp verification required

**Field setup cost**: $1,500-3,000 equipment (thermocouples, logger) plus labor; reusable across projects.

### Nurse-Saull Method (Simplified Maturity)

**Simplified maturity formula**:
- M = (average temperature - 40°F) × age in days
- Example: 60°F average for 4 days → (60 - 40) × 4 = 80 degree-days

**Limitations**:
- Less accurate than Arrhenius (below 50°F, overestimates strength)
- Suitable for moderate-temperature conditions (50-85°F range)
- Field use: Acceptable if precise strength prediction not critical

### Arrhenius Method (Advanced Maturity)

**More accurate strength prediction**, especially at cold temperatures:

**Formula**:
```
M = [ΔE/R × (1/Tref - 1/T)] × t

Where:
ΔE/R = Activation energy parameter (~32-45 for concrete, typical ~40 K)
Tref = Reference temperature (usually 298 K = 77°F)
T = Absolute temperature in Kelvin (°F + 459.67)
t = Age in days
```

**Practical simplification**: Use maturity testing software (Giatec, Concreflex, others) that applies Arrhenius correction automatically.

**Advantage**: More accurate at cold temperatures (below 50°F); recommended for post-tensioning, critical early strength.

### Correlation Testing Requirements

**Strength-Maturity Relationship**:

Before using maturity for decisions, establish concrete-specific correlation curve:

1. **Cast test cylinders** (minimum 6-10 cylinders)
2. **Cure cylinders** with thermocouples at same location as field concrete
3. **Break cylinders** at various ages (3-day, 5-day, 7-day, 10-day minimum)
4. **Plot strength vs. maturity** (creates correlation curve specific to mix design)
5. **Once curve established**: Maturity index predicts strength at any time without additional testing

**Correlation testing cost**: $2,000-5,000 per mix design (one-time, reusable for project duration)

**Accuracy**: ±5-10% strength prediction once correlated (acceptable for field decisions).

### Field Data Collection Protocol

**Daily Monitoring**:
- Download data logger temperature records each morning
- Verify thermocouple operation (check for sensor drift)
- Calculate cumulative maturity index
- Cross-reference to established correlation curve
- Document estimated strength in field log

**Common pitfalls**:
- Thermocouple fails midway (wire break, sensor disconnection) → void test
- Concrete colder than ambient (night wind, shade loss) → temperature logger placement critical
- Missing correlation curve data → cannot make predictions (must cast correlation cylinders before field use)

### When to Use Maturity Testing

**Beneficial scenarios**:
- Cold weather placement (below 50°F ambient expected)
- Early form removal critical (schedule-driven projects)
- Post-tensioning stressing timing (requires f'ci early strength verification)
- Accelerated concrete schedules (e.g., high-rise construction needing rapid floor-to-floor cycle)

**NOT recommended**:
- Mild weather, standard curing (28-day cylinder breaks sufficient, cost-justified only if schedule benefit >correlation cost)
- Shallow slabs (can be test-broken without maturity expense)
- Projects with long cure time buffers (schedule flexibility eliminates need)

---

## 2. SELF-CONSOLIDATING CONCRETE (SCC)

### Definition & Properties

**Self-consolidating concrete (SCC)**: High-slump, low-yield-strength mix that flows under its own weight, fills forms and surrounds reinforcement without mechanical vibration.

**Mix characteristics**:
- Slump flow: 22-28" target (no vibration needed for flow)
- High paste content (typically 36-38% of total volume)
- Supplementary cementitious materials (fly ash, slag, silica fume) = 25-50% cement replacement
- Polycarboxylate superplasticizer (critical admixture)
- Lower water-cement ratio than conventional concrete (0.40-0.50 typical)

**Advantages**:
- No vibration labor (elimination of vibrator operators)
- Improved consolidation in congested rebar areas
- Reduced noise, dust
- Faster placement, potential schedule compression

**Cost premium**: +$15-50/CY over standard concrete (primarily admixture cost).

### Slump Flow Testing (ASTM C1611)

**Target slump flow**: 22-28" (varies by application; 26" typical target)

**Equipment**:
- Standard slump cone
- Measuring tape
- Smooth, level surface

**Procedure**:
1. Place cone on smooth horizontal surface
2. Fill cone completely without rodding or vibration
3. Lift cone vertically (instantaneously)
4. Measure horizontal spread of concrete (2 perpendicular diameters)
5. Average the two measurements = slump flow

**Field acceptance**:
- 22-28" = ACCEPT
- <22" = Too stiff, concrete will not self-consolidate (risk of segregation, incomplete fill)
- >28" = Risk of excessive segregation, bleeding
- Record slump flow on pour card (baseline for SCC acceptance)

### T50 Measurement (Flow Time)

**T50** = Time (seconds) for concrete to spread to 20" diameter (half of maximum slump flow spread)

**Field procedure**:
1. Measure and mark 20" diameter circle on test surface
2. Start concrete flow (remove cone)
3. Begin stopwatch at moment of release
4. Stop stopwatch when concrete fully covers 20" circle
5. Record T50 time (typically 2-5 seconds for SCC)

**Acceptance criteria**:
- 2-5 seconds = good flow, stable
- <2 seconds = risk of segregation (excessively flowable, may separate coarse aggregate from paste)
- >5 seconds = poor flowability (consult mix design engineer)

**Field use**: T50 quick indicator of viscosity; rapid flow (low T50) indicates proper superplasticizer dose.

### J-Ring Test (Passing Ability Through Rebar)

**Purpose**: Verify concrete can flow through confined rebar spacing without blocking

**Equipment**:
- J-Ring (13 vertical reinforcing bars spaced 1" apart, 12" diameter, 12" tall)
- Standard slump cone (centered inside J-Ring)
- Measuring tape

**Procedure**:
1. Place slump cone inside J-Ring
2. Fill cone with SCC (no vibration)
3. Remove cone
4. Allow concrete to flow through bars
5. Measure slump flow diameter outside J-Ring
6. Measure slump flow diameter inside J-Ring (if measurable)
7. Calculate J-Ring blocking ratio: (Slump outside - Slump inside) / Slump outside

**Acceptance criteria**:
- Blocking ratio <6% = PASS (good passing ability)
- Blocking ratio >10% = FAIL (rebar spacing may obstruct placement)
- If flow cannot penetrate ring: Concrete will not self-consolidate through rebar; REJECT

**Field decision**: If J-Ring test shows blocking, notify engineer; may require mix adjustment (increase superplasticizer, reduce aggregate size, increase paste content).

### L-Box Test (Lateral Flow & Segregation Resistance)

**Equipment**:
- L-Box apparatus: Vertical section (height 13") and horizontal section (length 27"), 6" wide
- Divider gate between sections
- Measuring tape

**Procedure**:
1. Fill vertical section with SCC (no vibration)
2. Lift gate; concrete flows horizontally
3. Measure final horizontal distance (how far concrete flows)
4. Observe for segregation (coarse aggregate separated from paste at end of flow)

**Acceptance criteria**:
- Horizontal flow distance: 24-27" typical (indicates good self-consolidation)
- Visual segregation: NONE acceptable (if coarse aggregate clearly separated, SCC not suitable for application)

**Field use**: Primarily lab test (rarely done in field); indicates viscosity and segregation resistance of mix.

### Visual Stability Index (VSI)

**Qualitative assessment** of SCC quality during slump flow test:

| VSI Rating | Description | Acceptance |
|---|---|---|
| **0 - Stable** | Uniform color, no coarse aggregate at perimeter | PASS |
| **1 - Slight segregation** | Minor coarse aggregate at outer edge, slight color variation | CONDITIONAL (acceptable if localized) |
| **2 - Segregation** | Notable coarse aggregate separation, visible paste ring at edge | FAIL |
| **3 - Severe segregation** | Extreme separation, coarse aggregate at far edge, clear paste halo | FAIL |

**Field observation**: During slump flow test, visually inspect concrete spread pattern. If severe segregation visible, SCC mix not acceptable for placement.

### SCC Placement Procedures (Critical - NO VIBRATION)

**Key principle**: SCC achieves consolidation through gravity and flow energy, not mechanical vibration.

**Placement technique**:
1. **Form preparation**: Clean forms, remove debris
2. **Rebar spacing verify**: Must be ≥2" clear spacing minimum (for 19-25mm aggregate); <1" spacing requires smaller aggregate SCC
3. **Pouring rate**: Moderate speed (not full-bucket drops); avoid impact
4. **Placement location**: Pour at lowest point; allow concrete to self-level
5. **No vibration**: DO NOT vibrate; vibration destroys air stability and causes segregation
6. **Monitor fill**: Observe concrete flowing into voids, around rebar
7. **Top strike-off**: Level with form top after flow completes

**Common error**: Applying vibrators to SCC causes:
- Destruction of air void network (loss of stability)
- Separation of paste from aggregate
- Voids in section (poor consolidation despite vibration)

**Field rule**: If superintendent instinctively vibrates SCC, stop immediately. SCC consolidation is gravity-driven; vibration is counterproductive.

### Common SCC Defects

**Segregation** (coarse aggregate separated from paste):
- Cause: Excessive slump flow (>28"), low paste content, inadequate viscosity
- Prevention: Control slump flow to 22-28", verify T50 2-5 sec
- Remedy: Remove segregated concrete; consult mix engineer for adjustment

**Bleeding** (excess water at surface):
- Cause: Inadequate paste content, coarse aggregate settlement
- Prevention: Verify mix design includes >36% paste; check slump flow not >28"
- Remedy: Allow bleed water to rise naturally; do NOT finish until bleed water evaporates

**Voids/Honeycombing** (despite no vibration):
- Cause: Inadequate flow (slump flow <22"), rebar spacing too tight, air entrapment
- Prevention: Verify slump flow within range, check rebar spacing ≥2" clear
- Remedy: Use L-box test during mock placement to verify flow through rebar

**Surface wrinkles/ridges**:
- Cause: Concrete speed too slow, inadequate flow energy
- Prevention: Increase pouring rate slightly; consider admixture adjustment
- Remedy: Light finishing acceptable (minimal troweling)

---

## 3. CONCRETE REPAIR & REHABILITATION

### ICRI Surface Preparation Profiles (CSP 1-10)

**ICRI standard** defines concrete surface texture for bonding requirements.

| CSP Level | Description | Typical Method | Use Case | Bond Strength Impact |
|---|---|---|---|---|
| **1 - None** | Original cast finish, no texture | None | No repair bonding | Minimal |
| **2 - Light** | Surface dust removed, minimal profile | Broom/wire brush | Non-structural repair | Moderate |
| **3 - Medium** | ~0.5-1.5mm average profile | Grinding, light sandblasting | Standard repairs | Good |
| **4 - Heavy** | 1.5-2.5mm profile | Medium sandblasting, milling | Structural repairs | Excellent |
| **5-10 - Extra Heavy** | >2.5mm, exposed aggregate | Heavy sandblasting, scabbling | High-load repairs, overlay prep | Maximum |

**Field measurement**: Use ICRI profile gauge (tactile standard); compare surface roughness to gauge.

**Cost impact**:
- CSP 2: Labor only, ~$0.50/SF
- CSP 3: Grinding/light abrasion, ~$1-3/SF
- CSP 4+: Heavy abrasion/scabbling, ~$5-15/SF

**Critical decision**: Underestimate CSP for repair = bond failure (repair spalls, delaminates). Overestimate CSP = unnecessary cost. Verify with repair material specification.

### Repair Material Selection

**Cementitious Repair Mortar**:
- **Composition**: Portland cement + sand + admixtures (shrinkage reducer, bonding agent)
- **Strength**: 3,000-5,000 psi (structural grade available)
- **Cost**: $100-200/bag (25 lb typical)
- **Application**: Standard repairs, patches <1/2" depth typical
- **Advantage**: Cost-effective, familiar application
- **Limitation**: Shrinkage cracking if thick repair (>2"); moisture absorption if not sealed
- **Use when**: Repair <1" depth, non-critical load-bearing surface

**Epoxy Repair Mortar**:
- **Composition**: Epoxy resin + hardener + aggregate
- **Strength**: 4,000-8,000 psi (exceeds parent concrete)
- **Cost**: $300-500/cartridge (1-2 hour pot life typical)
- **Application**: Bonding to damp/wet surfaces, high-load repairs
- **Advantage**: Superior bond (adhesive joint), moisture-insensitive, rapid cure (24-48 hours)
- **Limitation**: Cannot apply in cold weather (<50°F), cost premium, requires surface profiling (CSP 3+)
- **Use when**: Structural repair, high-traffic area, schedule-critical

**Polymer-Modified Mortar**:
- **Composition**: Portland cement + synthetic polymer (acrylic, SBR latex) + sand
- **Strength**: 2,500-4,500 psi
- **Cost**: $150-250/bag
- **Application**: Non-structural repairs, cosmetic patching
- **Advantage**: Moderate cost, improved flexibility, good adhesion without chemical bonding
- **Limitation**: Lower strength than epoxy, moisture-sensitive during cure
- **Use when**: Spalls, cosmetic defects, minor repairs <3/4"

### Crack Classification & Assessment

**Structural vs. Non-Structural**:

| Classification | Width | Cause | Risk | Action |
|---|---|---|---|---|
| **Non-structural** | <0.01" | Drying shrinkage, thermal | Cosmetic, no load implication | Monitor, seal if water ingress risk |
| **Structural** | >0.01" | Load-induced, settlement, rebar corrosion | Potential capacity loss | Engineer evaluation required |

**Active vs. Dormant**:

**Dormant cracks** (stable, no movement):
- Measure width with crack gauge
- Monitor width monthly; no increase = dormant
- Repair without concern of re-cracking

**Active cracks** (widening or closing seasonally):
- Measure width at min and max temperatures (winter vs. summer)
- If width change >0.005": Active
- Require flexible repair method (polyurethane injection, expansion joints)
- Do NOT rigidly patch (will re-crack); use expandable sealant

**Field decision**: Use tell-tales (glass plates glued across crack) to visually confirm activity over 3-6 months.

### Crack Injection (Epoxy vs. Polyurethane)

**Epoxy Injection**:
- **Use for**: Dormant structural cracks (load-bearing elements)
- **Mechanism**: Adhesive bonding; permanently seals crack
- **Procedure**:
  1. Clean crack (blow-out loose material, air pressure)
  2. Install injection ports (small-diameter tubes) at ~2' intervals
  3. Pump epoxy at low pressure (100-300 psi) until emerges from next port
  4. Move to next port
  5. Allow 48 hours cure
- **Cost**: $1,500-3,000 per 100 linear feet (including ports, labor)
- **Limitation**: Cannot inject into damp/wet cracks (epoxy cures with moisture as catalyst, not compatible)

**Polyurethane Injection**:
- **Use for**: Active cracks (movement expected), damp concrete
- **Mechanism**: Foaming sealant; expands to fill void, accommodates movement
- **Procedure**:
  1. Install injection ports (same as epoxy)
  2. Pump polyurethane at higher pressure (500-1,000 psi; reacts with moisture)
  3. Foam expands as it cures, fills all voids
  4. Allow 24 hours cure
- **Cost**: $1,000-2,000 per 100 linear feet (slightly less than epoxy)
- **Advantage**: Works in wet cracks, accommodates movement, flexible cure
- **Limitation**: Less rigid than epoxy (not ideal for load-bearing reinforcement bonding)

**Field decision**: Use epoxy for static, dormant cracks; polyurethane for active, wet cracks.

### Surface Repair Methods

**Spall Repair (<1 SF)**:
1. **Remove loose concrete**: Chip back to sound material (test with hammer)
2. **Preparation**: Clean, blow out debris, dampen (not saturated)
3. **Prime**: Apply bonding agent per repair material specification
4. **Fill**: Apply cementitious or epoxy repair mortar in layers (if deep repair)
5. **Finish**: Strike off flush, light trowel finish
6. **Cure**: Seal or cover (prevent rapid drying)

**Cost**: $100-300 per spall (labor + materials)

**Overlay/Topping (Large areas)**:
1. **Surface prep**: CSP 3-4 per repair specification (grinding, scabbling)
2. **Dampening**: Pre-wet surface 24 hours before overlay (not saturated)
3. **Primer/bonding layer**: 1/8-1/4" thick epoxy or polymer-modified adhesive layer
4. **Overlay placement**: Self-leveling mortar or concrete, 1/2-2" thickness typical
5. **Finish**: Strike off, trowel, broom finish per specification
6. **Cure**: Seal, protect from traffic for 7 days minimum

**Cost**: $3-8/SF for overlay (total installed, labor + materials)

---

## 4. POST-TENSIONING

### Stressing Sequence & Planning

**Planning before stressing**:
- Verify concrete strength achieved (require 28-day break results ≥90% of f'ci if using early break, or 90-day alternative)
- Confirm f'ci (initial strength at stressing) from cylinder correlation or 56-day cylinder break
- Establish stressing schedule (cables or strands per day, sequence across building if multi-bay)
- Verify PT Equipment on-site (jacks, gauges, load cells, elongation measuring devices)

**Typical stressing sequence**:
1. Stress all transverse cables (east-west) first
2. Then stress longitudinal cables (north-south)
3. Within each direction: Stress alternating cables (balance load introduction)
4. Example: 10-cable span → Stress cables 1, 3, 5, 7, 9 first; then 2, 4, 6, 8, 10

**Rationale**: Alternating stress avoids one-sided loading (prevents slab tilting, differential settlement during stressing).

### Elongation Calculations & Field Measurement

**Elongation (ΔL)** = Expected change in cable length due to stress applied.

**Calculation**:
```
ΔL = (Stress × Cable Length) / (Young's Modulus)

Typical strand steel:
Young's Modulus (E) = 28.5 × 10^6 psi
Stressing stress = 0.75 × ultimate strength (typical)

Example:
1/2" diameter strand, 100' long cable
Ultimate strength = 270,000 psi (typical 7-wire)
Stressing stress = 0.75 × 270,000 = 202,500 psi
ΔL = (202,500 × 1,200 inches) / (28.5 × 10^6)
ΔL = 8.5 inches total elongation expected
```

**Field measurement procedure**:
1. Mark reference points on cable at jacking end (before stressing)
2. Install elongation gauge (vernier calipers, measuring tape, electronic displacement transducer)
3. Stress cable gradually (10% increments typical)
4. Measure elongation at each 10% increment
5. Compare measured vs. calculated elongation
   - Within ±10% = ACCEPT (normal friction, seating loss)
   - >10% deviation = INVESTIGATE
     - May indicate broken strands, friction in ducts, seating loss
     - Consult PT engineer before proceeding

**Common issues**:
- **Excessive elongation**: Cable friction in duct > expected; may indicate blocked tendon (debris, kinks)
- **Insufficient elongation**: Broken strands discovered during stressing (must replace; costly delay)

### Grouting Procedures (Post-Tensioning)

**Purpose of grouting**: Fill tendon duct; protect strand from corrosion.

**Grouting timing**:
- Begin grouting when all tendons stressed (typically 3-7 days after final stress)
- Do NOT delay >30 days (strand corrosion risk in ungrouted ducts)
- Verify weather: Min 50°F ambient, avoid heavy rain during/after grouting

**Grout selection**:
- **Cementitious grout** (most common): 1:1 cement:sand, w/c ~0.45
  - Cost: $50-100/SF grouted area
  - Set time: 24-48 hours
  - Advantage: Standard, cost-effective

- **Epoxy grout**: Higher strength, moisture-resistant
  - Cost: $150-300/SF
  - Set time: 4-8 hours
  - Advantage: Premium protection, rapid turnaround
  - Use when: High-corrosion risk (coastal, underground)

**Grouting procedure**:
1. **Pressure grouting**: Pump grout from lowest point (entry port) to highest point (exit port)
2. **Pressure range**: 25-100 psi typical (verify per specification)
3. **Monitoring**: Continue grouting until grout exits all ports uniformly
4. **Port plugging**: Close exit ports when grout emerges
5. **Curing**: Protect grouted duct from rain, maintain ≥50°F for 48 hours

**Field verification**:
- Record start/end time, grout volume, pressure
- Inspect all ports grouted (no dry pockets)
- Post-cure test: Probe ducts at intervals to confirm fill (no voids)

### Anchor Set Loss

**Anchor set loss** = Elongation lost due to slack taken up at anchor head during seating.

**Typical anchor set loss**: 1/4 - 1/2 inch (varies by anchor type, strand properties)

**Impact on final stress**:
- If 1/2" anchor set loss occurs after stressing, cable relaxes ~0.5"
- Stress drops by ~0.5"/1,200" = 0.04% of total (minor, typically <1% stress drop)
- Effect: After stressing, cable may require re-stressing if anchor set excessive

**Field measurement**:
1. After jacking, measure cable length again (same reference points)
2. Calculate total elongation achieved
3. After 24 hours (anchor set complete), re-measure
4. Difference = anchor set loss
5. If >0.5": Consult engineer; may require re-stressing to target load

**Prevention**: Use modern anchor systems with minimal set loss (wedge-type anchors typical modern practice; older barrel anchors had higher set loss).

### Stressing Log Documentation (Critical Record)

**Required documentation** for PT inspection and acceptance:

```
PROJECT: ________________  DATE: ___________
CABLE ID: ________________  LOCATION: _______

STRESSING PARAMETERS
  Cable length: ________ feet
  Number of strands: ____ (each 0.5" or 0.6" diameter)
  Ultimate strength per strand: _______ psi
  Target stressing load: _______ kips (=0.75 × ultimate)
  Target elongation (calculated): _______ inches

STRESSING PROCEDURE
  Start time: _______  End time: _______
  Jack ID / Serial #: _________________
  Load cell reading (start): _______ kips
  Load cell reading (final): _______ kips
  Measured elongation (inches): _______
  Deviation from calculated: _______ % (✓ PASS / ✗ INVESTIGATE)

GROUTING
  Grouting date: _________
  Grout type: [ ] Cementitious [ ] Epoxy
  Grouting start time: _______  End time: _______
  Total grout volume used: _______ gallons
  Pressure maintained: _______ psi
  All ports grouted: [ ] YES [ ] NO (if NO, note exceptions: ________)

INSPECTION
  Inspector name: __________________
  Sign-off date: ___________
  Notes / Non-conformances: _______________________________
```

**Retaining stressing logs**: Required for code compliance, future rehabilitation, warranty validation. Store in project files minimum 5 years.

---

## 5. MASS CONCRETE (ACI 207 THERMAL CONTROL)

### ACI 207 Standard & Thermal Management Concept

**Mass concrete** = Any concrete section >3 feet thick where internal heat development and cooling is a concern.

**Thermal risk**: Hydration heat generates 100-150 BTU per pound of cement. In mass concrete:
- Interior remains >150°F for weeks
- Surface cools rapidly (exposed to air)
- Temperature differential creates cracking risk

**ACI 207 requirement**: Maximum internal-to-surface temperature differential ≤ 35°F (conservative limit for most projects).

### Thermal Control Plan (Required for Mass Concrete)

**Develop plan BEFORE placing concrete**:

1. **Heat generation analysis**:
   - Estimate peak internal temperature (function of cement content, water content, insulation)
   - Typical peak internal temps: 140-180°F (mass concrete in cold climate)

2. **Cooling method selection**:
   - Insulation blankets (passive cooling, delays heat loss)
   - Cooling pipes (active cooling, passes chilled water)
   - Cryogenic nitrogen (emergency rapid cooling, rare)

3. **Scheduling**:
   - Determine when peak temperature reached (typically 5-10 days post-placement)
   - Plan cooling initiation
   - Plan removal of cooling system and insulation timing

### Temperature Monitoring Setup

**Thermocouple installation** (same as maturity testing):
- Install during placement (embedded thermocouples, wire leads to logger)
- Location: Center and near surface (4" from face minimum)
- Record every 2-4 hours during critical period (first 14 days)
- Monitor continuously until ΔT (interior - surface) <20°F

**Field log example**:
```
MASS CONCRETE THERMAL LOG
Pour date: 2/15  Concrete temp at placement: 65°F

Day    Time    Interior °F    Surface °F    ΔT °F    Action
1      6:00    72            68            4        Monitor
1      12:00   95            85            10       Monitor
1      18:00   125           102           23       Monitor
2      6:00    145           110           35       Cooling initiation
2      12:00   148 (peak)    120           28       Cooling pipes on
3      6:00    135           125           10       Continue cooling
```

**Decision point**: When ΔT reaches 35°F or higher, activate cooling method.

### Insulation Blankets (Passive Control)

**Purpose**: Slow cooling rate, reduce thermal shock at surface.

**Thickness** (rigid foam typical):
- 2" rigid foam: Reduces cooling rate ~50% (delays peak temp by ~2-3 days)
- 4" rigid foam: Reduces cooling rate ~70% (delays peak temp by ~4-5 days)
- Cost: $2-5/SF for material + installation labor

**Duration**:
- Leave in place 7-14 days minimum (longer reduces thermal shock)
- Remove gradually over 2-3 days (remove portion daily to acclimate)

**Limitation**: Only delays cooling; does NOT accelerate cooling or prevent high peak temperatures. Not primary control for large mass sections.

### Cooling Pipes (Active Control)

**Purpose**: Pump chilled water through embedded pipes; actively remove heat.

**System setup**:
1. **Embed cooling pipes** during placing (typically 0.5" or 0.75" diameter HDPE tubing)
   - Spacing: 2-4 feet apart (typical), grid pattern covering section
   - Depth: Locate at mid-depth of section

2. **Connect to chiller unit** (external, size = 50-150 tons cooling capacity typical)
   - Supply chilled water (~40-50°F)
   - Return hot water (cooler ambient air dissipates heat)

3. **Flow rate**: 10-30 gallons per minute typical per pipe loop

4. **Duration**: 5-10 days active cooling (depending on section size, peak temperature)

**Cost impact**:
- Cooling pipes installation: $2-5/SF (in embedded cost)
- Chiller rental: $2,000-5,000/day
- Total 10-day cooling: $25,000-75,000+ (for large pour)

**Benefit**: Maintains ΔT <25°F throughout cure (prevents thermal cracking).

**Field decision**: Use cooling pipes if section >6' thick, peak interior temperature predicted >160°F, or project in cold climate (risk of thermal shock).

### Maximum Temperature Differential Control

**ACI 207 limit**: 35°F max (ΔT = interior temp - surface temp)

**Implications**:
- 35°F ΔT is threshold; exceeding creates high tensile stress at surface
- Concrete at surface typically develops surface cracks (pattern random, 6-12" spacing) if ΔT >40°F
- Cracks rarely penetrate deep (structural concern low, cosmetic concern moderate)

**Monitoring protocol**:
1. Record interior and surface temps every 4 hours (peak period)
2. Calculate ΔT continuously
3. When ΔT approaches 35°F, initiate cooling (cooling pipes) or delay insulation removal
4. Maintain ΔT <35°F until interior temperature drops below 120°F (safe plateau)

### Extended Curing Duration

**Standard curing** (ACI 301):
- Hard-troweled floors: 3-7 days moist curing
- Structural concrete: 7 days minimum

**Mass concrete extended curing** (ACI 207):
- Moist curing required: 14-28 days minimum
- Rationale: Slower hydration at reduced interior temperature requires extended cure
- Method: Wet burlap, plastic covering, fog misting (continuous 24-hour cycles)

**Post-cure monitoring**:
- After moist curing stops, monitor for drying shrinkage cracks
- Continue thermal monitoring; ΔT should be <15°F by end of extended cure
- Allow gradual temperature drop (do NOT remove all insulation abruptly)

---

## 6. HIGH-PERFORMANCE CONCRETE (HPC)

### Low Water-Cement Ratio Placement Challenges

**High-performance concrete** typically specified with:
- w/c ratio: 0.35-0.45 (vs. standard 0.50-0.55)
- 28-day strength: 5,000-10,000+ psi
- Low permeability, high durability goals

**Placement challenges with low w/c**:

1. **Reduced slump** (stiffer mix):
   - Low w/c means less free water for flow
   - Typical slump: 2-4" (vs. standard 4-6")
   - Requires increased vibration (longer vibration times, 15-30 seconds/location vs. 10-15 standard)
   - Risk: Over-vibration entrains excess air, destroys desired low-permeability properties

2. **Increased segregation risk**:
   - Stiff mixes separate coarse aggregate from paste more readily
   - Vibration and placement must be methodical, not aggressive

3. **Pumping difficulty**:
   - Low slump concrete is harder to pump
   - Requires larger pump diameter, higher pressure
   - Pipeline friction losses increase
   - Pump must be sized for stiff mix (not standard pump for same size section)

**Field solution**:
- Use superplasticizer dose increased (0.75-1.5% by cement weight, vs. standard 0.5%)
- Maintain slump 2-4" (lower than standard, but flowable enough to consolidate with moderate vibration)
- Avoid excess vibration (consolidate just until settled, no additional time)

### Curing Sensitivity (Critical for HPC)

**HPC durability depends on** complete hydration and low permeability; inadequate curing voids this.

**Extended curing requirement**:
- Minimum 7 days moist curing (vs. 3 days standard)
- Optimal: 14-28 days moist curing (for w/c <0.40)
- Rationale: Low w/c leaves limited water for complete hydration; external moisture supply necessary

**Curing method**:
- Wet burlap: Best for HPC (continuous moisture saturation)
- Plastic sheeting: Acceptable if heat and humidity managed (prevents drying)
- Fog misting: Adequate if frequency maintained (4-6 times daily minimum, vs. 1-2 times for standard concrete)
- Sealed plastic bags: Acceptable (prevents any moisture loss)

**Cost impact**: Extended curing labor 2-3x standard curing (burlap changes, water supply).

**Field risk**: Early curing stoppage (before 7 days) results in:
- Surface permeability high (air-exposed surface dries, doesn't hydrate fully)
- Chloride penetration accelerated (coastal environment vulnerability)
- Corrosion of reinforcement potential high despite low w/c benefit

### Permeability Testing (RCPT & Surface Resistivity)

**Rapid Chloride Penetration Test (RCPT, ASTM C1202)**:

**Purpose**: Measure concrete resistance to chloride ion migration (durability indicator).

**Procedure**:
1. Cut cylinder sample (2" thick disk from 6"x12" cylinder)
2. Vacuum-saturate sample 18 hours
3. Place disk in electrical cell (two compartments separated by concrete disk)
4. Apply 60-volt potential (4 hours typical duration)
5. Measure total charge passed (coulombs)
6. Charge determines chloride penetration resistance

**Results interpretation**:
| Charge (Coulombs) | Permeability Rating | Performance |
|---|---|---|
| <100 | Very low | Excellent (typical HPC target) |
| 100-1,000 | Low | Good |
| 1,000-2,000 | Moderate | Fair |
| >2,000 | High | Poor |

**Field use**: RCPT typically performed by lab at 28 days; if >1,000 coulombs, indicates inadequate w/c or curing (recommend additional testing).

**Surface Resistivity (ASTM C1876)**:

**Advantage over RCPT**: Non-destructive (no sample destruction), faster (minutes vs. hours), reusable cores.

**Procedure**:
1. Allow concrete to surface-dry (1-2 hours)
2. Apply four-point probe to concrete surface
3. Apply small AC current (100 mV, 1 kHz)
4. Measure resistance
5. Calculate resistivity (ohm-cm unit)

**Results interpretation**:
| Resistivity (kΩ-cm) | Chloride Corrosion Risk |
|---|---|
| <12.5 | High |
| 12.5-25 | Moderate |
| 25-37.5 | Low |
| >37.5 | Very low |

**Field use**: QC testing at 28 days; if <25 kΩ-cm, investigate curing adequacy, w/c ratio verification. Non-destructive allows sampling multiple locations.

---

## UNIVERSAL FIELD RULES (ADVANCED CONCRETE)

1. **Maturity testing is cost-justified only if schedule benefit exceeds correlation cost** — Do not use routinely for mild-weather standard construction.

2. **SCC requires NO vibration; vibration destroys the mix** — Educate entire placement crew on this critical difference.

3. **Crack repair success depends on surface preparation** — Underestimate CSP (concrete surface profile) and repair fails; overestimate CSP and cost balloons unnecessarily.

4. **Active cracks require flexible repair (polyurethane); dormant cracks use rigid repair (epoxy)** — Mismatching repair type to crack activity causes repeated failure.

5. **Post-tensioning elongation measurement must be within ±10% of calculated** — Deviation indicates cable issue; do not stress beyond this tolerance.

6. **Mass concrete thermal control begins in design phase, not day-of-placement** — Thermal plan must be approved pre-pour; field-day improvisation typically inadequate.

7. **High-performance concrete extends curing minimum 7 days** — Skipping extended curing voids HPC durability benefits entirely.

8. **Permeability testing (RCPT/resistivity) at 28 days provides durability verification** — Recommended for HPC and harsh environments; informs future inspection protocols.

---

**Document Version**: Advanced Concrete 1.0
**Last Updated**: 2026
**Always Verify**: Project specifications, approved mix designs, engineer approvals, ACI standards before field decisions
