# Concrete Mix Design - Deep Extraction Guide

Extract detailed mix design data from concrete supplier submittals, trial batch reports, and lab certifications. These documents define the exact concrete properties for every placement on the project and are critical for daily QC verification and inspector approval.

---

## Extraction Priority Matrix

| Priority | Data Type | Use Case | Completeness Target |
|----------|-----------|----------|-------------------|
| **CRITICAL** | Mix ID and element assignment | Daily report, load verification, placement coordination | 100% per element type |
| **CRITICAL** | Design f'c (28-day strength) | Specification compliance, compression testing schedule | 100% per mix |
| **CRITICAL** | w/c ratio (water-to-cement ratio) | Durability verification, field testing, spec check | 100% per mix |
| **CRITICAL** | Slump range | Workability acceptance, field testing, daily report | 100% per load |
| **CRITICAL** | Air content | Freeze-thaw protection, field testing, placement acceptance | 100% per mix |
| **HIGH** | Cement type and content | Cold/hot weather adjustments, source identification | 100% per mix |
| **HIGH** | Aggregate specifications | Material traceability, visual QC, batch variance | 100% per mix |
| **HIGH** | Admixture type, dosage, product | Batch control, substitution tracking, QC verification | 100% per mix |
| **HIGH** | Lab certification (test reports, break dates) | Acceptance criteria, test schedule, cross-reference | 100% if provided |
| **MEDIUM** | Temperature modifications | Cold/hot weather notification, placement conditions | 100% if applicable |
| **MEDIUM** | Unit weight and maximum aggregate size | Density verification, placing density measurement | 100% per mix |

---

## MIX DESIGN IDENTIFICATION

### Mix ID Numbering Conventions

Concrete suppliers use different systems for mix identification. Learn the producer's system immediately:

**Common Naming Patterns**:
- **"4000-1"**: f'c value (4000 PSI) + version number
- **"4K"** or **"4K-FA"**: f'c + modifier (FA = fiber-added, AE = air-entrained)
- **"Mix A-1", "Mix B-2"**: Alphabetic + sequential
- **"FOO-4000-STD"**: Customer-Supplier-f'c-Standard
- **Producer's internal codes**: Typically include location, plant code, revision date

**ACTION**: On first submittal, create a mapping document. Ask supplier: "What does your mix ID system mean? Are there version numbers? How do you track revisions?"

### Element-to-Mix Assignment Mapping

Structural general notes call out concrete requirements by element and f'c. The concrete submittal must clearly map producer mixes to these callouts.

**Typical Spec Language**:
```
• All footings: 4,000 PSI concrete with w/c ratio ≤ 0.50
• Slab-on-grade: 3,500 PSI with 6 oz/CY fiber
• Exposed exterior walls: 5,000 PSI with air entrainment (5-7%)
• Vertical walls below grade: 4,000 PSI, w/c ≤ 0.45
• Grade beams: 4,000 PSI
```

**Your Task**: Match each spec callout to the producer's mix ID:

| Structural Element | Spec Requirement | Producer Mix ID | Design f'c | w/c Ratio | Air Content | Fiber | Notes |
|---|---|---|---|---|---|---|---|
| Footings | 4,000 PSI, w/c ≤ 0.50 | 4000-1 | 4,000 | 0.48 | None | No | Standard |
| Grade beams | 4,000 PSI | 4000-1 | 4,000 | 0.48 | None | No | Same as footings |
| SOG | 3,500 PSI with fiber | 3500-F | 3,500 | 0.55 | None | 6 oz/CY | Sika FibraSeed |
| Exterior walls | 5,000 PSI, air ent. | 5000-AE | 5,000 | 0.42 | 5.5% | No | Air-entrained |
| Below-grade walls | 4,000 PSI, w/c ≤ 0.45 | 4000-2 | 4,000 | 0.45 | None | No | Tighter w/c |

**RED FLAGS**:
- Design f'c < specified f'c → flag for engineer review
- w/c ratio > specification maximum → reject submittal
- Element missing from assignment table → ask supplier for clarification
- "Using standard mix" without matching → unacceptable

---

## CORE PROPERTIES TO EXTRACT

For **EVERY mix design**, extract and verify these properties. These are the daily control parameters.

### Concrete Strength (f'c)

- **Design f'c**: Target 28-day compressive strength in PSI (e.g., "4000 PSI")
- **Margin above minimum**: Typical = 400-500 PSI above spec (so 4000 PSI spec → 4400-4500 design)
- **Seven-day target** (if specified): Some specs require 7-day strength verification before removal of forms
- **Testing schedule**: Verify lab breaks at 7 and 28 days (minimum 2 cylinders each age)

**EXAMPLE EXTRACT**:
```
Design f'c: 4,000 PSI (28-day)
Specified f'c: 3,500 PSI (per Structural Note 5)
Margin: 500 PSI safety margin
7-day target: 2,800 PSI (70% of 28-day)
Lab testing: 2 cylinders @ 7d, 2 cylinders @ 28d, standard cure
```

### Water-to-Cement Ratio (w/c)

The w/c ratio is the most critical durability parameter. Extract and verify against spec limits.

- **Actual w/c ratio**: Decimal value (e.g., "0.48" means 0.48 lbs water per 1 lb cement)
- **Maximum allowed**: Specification limit (e.g., "≤ 0.50")
- **Method of achievement**: Adjust by reducing water, increasing cement, or using admixtures
- **How it's maintained in field**: Reject any truck that adjusts water without producer approval

**Why It Matters**:
- Lower w/c = higher strength, better durability
- w/c of 0.45 ≈ very good durability (up to 75 years exposure)
- w/c of 0.55 ≈ moderate durability (20-40 years)
- Every 0.01 increase in w/c ≈ 200-300 PSI strength loss

**EXAMPLE EXTRACT**:
```
w/c ratio: 0.48
Spec maximum: 0.50
Cement content: 564 lbs/CY
Water content: 271 lbs/CY
Water in admixtures: Accounted for (WRDA-60 is water-based)
Total water (including admixtures): 285 lbs/CY
```

### Slump

- **Slump range**: High and low (e.g., "3-5 inches", "4-6 inches")
- **Measurement method**: ASTM C143 (standard slump test)
- **Acceptability**: Field slump must be within this range; outside range = reject truck
- **Slump loss over time**: How much slump is expected to decrease during transit

**EXAMPLE EXTRACT**:
```
Slump range: 4.0 to 6.0 inches
Method: ASTM C143 standard slump cone
Measured at plant: 5.0 inches
Expected slump loss in first 30 minutes: 0.5 inches
At job site (after ~20 min transit): expect 4.5 inches
Maximum acceptable: 6.5 inches (slightly high but acceptable)
Minimum acceptable: 3.5 inches (slightly low but acceptable)
```

### Air Content

- **Target air content**: Percentage range (e.g., "5-7%")
- **Type**: Entrained air (intentional, for freeze-thaw) vs entrapped (accidental, reduces strength)
- **Freeze-thaw protection**: Any concrete exposed to freezing needs ≥4% air
- **Measurement**: ASTM C231 (pressure method) or ASTM C173 (volumetric method)

**EXAMPLE EXTRACT**:
```
Air content requirement: 5.0% to 7.0% (freeze-thaw exposure)
Air-entraining admixture: Daravair 1400
Dosage: 0.4-0.6 oz per CY
Lab test (ASTM C231): 5.5% air
Field acceptance: 4.5% to 7.5% (±2% field tolerance)
Concrete without air for protected interior floors: 2-4% entrapped
```

### Cement

- **Cement type**: I, II, III, I/II, or V (per ASTM C150)
  - Type I: General purpose (most common)
  - Type II: Moderate sulfate resistance, moderate heat
  - Type III: High early strength (fast strength gain)
  - Type V: High sulfate resistance (for exposed conditions, underground)
- **Cement content**: Lbs per cubic yard (e.g., "564 lbs/CY")
- **Cement source/mill**: Brand (Lafarge, Essroc, Riverside, etc.) — for batch control

**Cement Type Selection**:
- **Moderate heat environment**: Type II
- **Cold weather mix** (rapid strength needed): Type III or Type II with accelerator
- **Sulfate exposure** (coastal, corrosive soils): Type II or V
- **Standard interior concrete**: Type I

**EXAMPLE EXTRACT**:
```
Cement type: Type I/II (blend)
Cement content: 564 lbs/CY
Cement source: Lafarge Mill, TX
Moisture content accounted: Yes
Clinker variability: Normal range
Type III substitute available for cold weather: Yes, at +$2/CY premium
```

### Aggregate

#### Coarse Aggregate
- **Size**: Nominal maximum (#57 = ¾", #67 = ½", #8 = ⅜", #411 = mixed)
- **Source**: Quarry name/location (e.g., "ABC Quarry, Johnson County")
- **Material**: Limestone, granite, trap rock (affects color, durability, absorption)
- **Gradation**: ASTM C33 compliant?
- **Absorption**: Important for w/c ratio (high-absorption aggregate "drinks" more water)

#### Fine Aggregate
- **Type**: Natural sand vs manufactured sand (M-sand or crushed sand)
- **Source**: Same quarry or different?
- **Fineness modulus (FM)**: Number 2.6-3.0 (affects workability) — ask supplier if not provided
- **Moisture content**: Affects water content calculation

**EXAMPLE EXTRACT**:
```
Coarse aggregate:
  - Nominal max size: ¾" (#57 limestone)
  - Source: Granite Ridge Quarry, 3 miles from plant
  - Absorption: 0.8% (low)
  - Specific gravity: 2.68
  - ASTM C33 compliance: Yes

Fine aggregate:
  - Type: Natural sand (not manufactured)
  - Source: Granite Ridge Quarry (same source as coarse)
  - Fineness modulus: 2.85
  - Moisture content: 4.2% (included in water calculation)
  - Clay/fines (< 200 mesh): 2.1% (within ASTM C33 limit of 5%)

Ratio coarse to fine: 62% coarse / 38% fine (by absolute volume)
```

### Admixtures

Extract every admixture with type, function, dosage, and product name.

#### Water Reducers (WR)
- **Function**: Reduce water content while maintaining slump → lower w/c ratio
- **Type**: WRDA (water reducing and delaying) or WR (water reducing only)
- **Dosage**: oz per CY (e.g., "4-6 oz/CY")
- **Product name**: "WRDA-60", "Daravair 60", "Sika Viscocrete-5930", etc.
- **Effect on strength**: Typically +5-10% strength at same slump

#### Retarders
- **Function**: Slow hydration for hot weather placement or extended working time
- **Type**: Admixture retarder (chemical) or ice/cooled water (physical)
- **Dosage**: oz/CY (chemical) or lbs replaced (ice)
- **Product**: "Daravair Retarder", "Delvo", "Sika Plastiment", etc.
- **When used**: Only in hot weather (typically >85°F ambient)
- **Time delay**: How much longer does initial set take (e.g., "+2 hours")

#### Accelerators
- **Function**: Speed up strength gain for cold weather or early formwork removal
- **Type**: Chemical (calcium chloride — often not allowed) or non-chloride (alternative)
- **Dosage**: oz/CY
- **Product**: "Pozzutec", "Sika Plastiment", "Calcium Chloride-free accelerator"
- **Caution**: Chloride accelerators banned in most specs (corrosion risk) — verify
- **Strength gain**: e.g., "doubles 1-day strength, minimal effect on 28-day"

#### Air-Entraining Agent (AEA)
- **Function**: Creates stable, controlled air bubbles for freeze-thaw protection
- **Product**: "Daravair 1400", "Rheomac AE", "Sika AEA-90", etc.
- **Dosage**: 0.3-0.6 oz/CY (highly variable by product and admixture compatibility)
- **Compatibility**: Some dosing changes if using water reducer concurrently
- **Target air content**: Usually 5-7% for exterior concrete
- **Measurement**: ASTM C231 (air meter in field)

#### Superplasticizers
- **Function**: Dramatically increase slump without adding water (used for self-consolidating concrete or high-slump applications)
- **Type**: Polycarboxylate (modern) or naphthalene/melamine formaldehyde (older)
- **Dosage**: Usually lower (1-3 oz/CY) but highly sensitive — "superplasticizers are not linear"
- **Product**: "Glenium", "Master Glenium", "Viscocrete", "Delvo SP", etc.
- **Slump effect**: Can increase slump by 4-6" at same water content
- **Strength effect**: Minimal if done correctly; if overdosed, causes segregation

#### Shrinkage-Reducing Admixtures
- **Function**: Reduce concrete shrinkage (for slabs, exposed surfaces, architectural finishes)
- **Dosage**: Usually 1-2 gallons/CY
- **Product**: "Kryton Permaduct", "Conprove SRA", etc.
- **Cost**: Premium (typically +$5-8 per CY)
- **When specified**: Slabs on grade, architectural surfaces, basement walls below grade

**EXAMPLE EXTRACT**:
```
Admixtures for 4000-1 standard mix:
  1. WRDA-60 water reducer
     - Type: Water reducing + delaying
     - Dosage: 4.0 oz/CY (plant batch)
     - Product: MasterRheobuild 2100
     - Function: Reduce w/c ratio from 0.55 to 0.48
     - Slump effect: Maintains 5" slump with less water

  2. Daravair 1400 air-entraining agent
     - Type: Stable air for freeze-thaw
     - Dosage: 0.4 oz/CY
     - Target: 5-7% air content
     - Measurement: ASTM C231 at plant
     - Lab tested: 5.5%

  3. Sika Plastiment retarder (HOT WEATHER ONLY)
     - Type: Set-delay admixture
     - Dosage: 2.0 oz/CY (not included in base mix)
     - Use condition: Ambient > 85°F at placement
     - Effect: Delays initial set ~2 hours
     - Cost: +$0.40/CY added only when needed
```

### Unit Weight

- **Expected unit weight**: Lbs per cubic yard (typically 140-150 PCF for normal-weight concrete)
- **Measurement method**: ASTM C138 (unit weight test at plant)
- **Lab test result**: Actual density from trial batch or previous production
- **Significance**: Verify concrete isn't segregating or over/under-sanded
- **Field acceptance**: Usually ±3% variance allowed

**EXAMPLE EXTRACT**:
```
Target unit weight: 145.0 PCF (for normal-weight concrete)
ASTM C138 lab test: 144.8 PCF (acceptable)
Field measurement tolerance: 144 - 147 PCF
Variation indicates: Material batching correct, no major segregation
```

### Maximum Aggregate Size (MAS)

- **Nominal maximum aggregate size**: Typically ¾" to 1½" for structural concrete
- **Relevance to placement**: Smaller aggregate (½") needed for restricted spaces, reinforcement spacing
- **Larger aggregate** (1½") is cheaper but may not fit in thin walls
- **Specification**: Check structural drawings for any size restrictions

**EXAMPLE EXTRACT**:
```
Maximum aggregate size (nominal): ¾" (#57)
Specification limit: 1/5 of thinnest dimension in slab (wall = 8" → max 1.6" aggregate OK)
Footing placement: ¾" aggregate fits easily, no restriction
Wall placement at closely-spaced rebar: Verify spacing vs ¾" aggregate
```

---

## TEMPERATURE-DEPENDENT MIXES

### Cold Weather Mix (When Ambient ≤ 40°F)

Cold weather mixes accelerate strength gain so formwork can be removed faster and concrete reaches design strength before freeze-thaw cycles damage it.

**Cold Weather Modifications**:
- **Type III cement**: Faster strength gain (can be +50% at 1 day)
- **Accelerator admixture**: Chemical set-accelerator (non-chloride only)
- **Heated water**: Replace mixing water with hot water (up to 160°F) to warm the concrete
- **Steam curing**: If available (not common for cast-in-place)
- **Protection**: Insulation, tarps, heaters to maintain ≥50°F for first 48 hours

**EXAMPLE COLD WEATHER MIX**:
```
Base mix: 4000-1 (standard)
Cold weather modification: 4000-CW
  - Cement: Type III (not Type I/II)
  - Content: Still 564 lbs/CY
  - Accelerator: 2% Pozzutec non-chloride (added at plant or job site)
  - Water temperature: 120°F (heated at plant)
  - Concrete temp at placement: 55-65°F (ensure > 50°F)
  - Strength development: 1-day target 1800 PSI (50% of 28-day)
  - Forms: Can strip at 3-5 days vs 7-10 days for standard
  - Cost premium: +$3.50/CY (Type III + heated water + accelerator)
  - When ordered: 48 hours before placement if sourcing Type III cement
  - Placement window: December 15 - March 1

Supplier note: "Type III must be ordered; not kept in inventory"
```

**COLD WEATHER REQUIREMENTS**:
- Minimum concrete temperature at placement: 50°F
- Minimum ambient during placement: 35°F (do NOT place below)
- Minimum protection temperature after placement: 50°F for 7 days (or until f'c ≥ 2000 PSI)
- If temperature drops below required levels, heating, insulation, and protection must be employed

### Hot Weather Mix (When Ambient ≥ 85°F)

Hot weather mixes slow hydration and combat rapid water loss and early strength gain (which locks in shrinkage before concrete is strong).

**Hot Weather Modifications**:
- **Retarder admixture**: Chemical set-delay (extends working time 2-4 hours)
- **Ice replacement**: Use ice instead of some mixing water to cool the concrete
- **Cooled/chilled water**: Use cold water at plant
- **Reduced cement content**: Slightly lower cement (but maintain f'c by w/c adjustment)
- **Reduced slump**: Thinner concrete to reduce heat generation
- **Pozzolanic admixtures**: Fly ash or slag (if specified) — slower hydration

**EXAMPLE HOT WEATHER MIX**:
```
Base mix: 4000-1 (standard)
Hot weather modification: 4000-HW
  - Retarder: Delvo retarder, 2.0 oz/CY (adds delay, maintains strength)
  - Water temperature: Cooled to 45°F if possible (or ice added)
  - Concrete temp at placement: Target 65-70°F (measured at truck)
  - Slump: 5.0" (standard)
  - Extended workability: +2 hours on site (set time delayed)
  - Initial set: Delayed 3-4 hours vs standard
  - 28-day strength: Unchanged from standard (retarder doesn't reduce f'c)
  - Cost premium: +$0.40/CY (retarder only)
  - When ordered: 24 hours before placement
  - Placement window: May 15 - September 30

Supplier note: "Ice must be loaded at plant; we can add up to 300 lbs ice per truck"
```

**HOT WEATHER REQUIREMENTS**:
- Maximum concrete temperature at placement: 90°F
- Maximum ambient during placement: 100°F (assess case-by-case)
- Wind speed during placement: <20 mph (higher wind increases evaporation)
- Sun exposure: Shade/cover concrete after placement
- Curing: Keep moist for full 7 days (hot weather accelerates drying)
- Retarder allows extended finishing window (important for large slabs)

---

## LAB TEST CROSS-REFERENCE

### Trial Batch Report

Before production begins, most suppliers (and specs) require a trial batch — a test run to verify the mix design meets all requirements.

**What to Extract from Trial Batch Report**:

| Data Point | Typical Value | Acceptance |
|-----------|---|---|
| **Lab ID** | e.g., "TB-2026-001" | Unique identifier for traceability |
| **Mix ID** | "4000-1" | Matches your mix identification |
| **Batch date** | "January 10, 2026" | When trial was made |
| **Trial contents** | "3 cubic feet per ASTM C192" | Standard trial volume |
| **Slump ASTM C143** | "5.5 inches" | Must be within specified range (4-6") |
| **Air content ASTM C231** | "5.5%" | Must be within range (5-7% for AEA mixes) |
| **Unit weight ASTM C138** | "144.8 PCF" | Typical 145 PCF ± 3% |
| **7-day strength** | "2,850 PSI" (2 cylinders avg) | Typically 60-75% of 28-day target |
| **28-day strength** | "4,120 PSI" (2 cylinders avg) | Must be ≥ design f'c (4000 PSI here) |
| **w/c ratio** | "0.48" | Verified from batch contents |
| **Cement type** | "Type I/II" | Must match submittal |
| **Admixtures** | "WRDA-60 @ 4 oz/CY, AEA @ 0.4 oz/CY" | Exact dosages confirmed |
| **Approvals** | "Engineer signature, date" | Must be signed by spec engineer or ACI inspector |

**EXAMPLE TRIAL BATCH REPORT EXTRACT**:
```
Trial Batch Report
Lab ID: TB-4000-2026-001
Project: ABC Building Foundation

Mix ID: 4000-1
Date Made: January 10, 2026
Lab: Ready Mix Testing Lab, Certified ACI

Trial Batch Composition (per CY):
  Cement (Type I/II): 564 lbs
  Coarse aggregate: 1,870 lbs
  Fine aggregate: 1,120 lbs
  Water: 271 lbs
  WRDA-60: 4.0 oz
  Daravair 1400: 0.4 oz
  ─────────────────────
  Total batch: 27 liters

Fresh Concrete Tests (ASTM):
  Slump (C143): 5.5 inches ✓ (spec: 4-6")
  Air content (C231): 5.5% ✓ (spec: 5-7%)
  Unit weight (C138): 144.8 PCF ✓ (nominal 145)
  Temperature at test: 72°F

Hardened Concrete Tests (cylinders, std cure):
  7-day strength (avg of 2 cylinders):
    Specimen 1: 2,875 PSI
    Specimen 2: 2,825 PSI
    Average: 2,850 PSI (expected ~71% of 28-day)

  28-day strength (avg of 2 cylinders):
    Specimen 1: 4,180 PSI
    Specimen 2: 4,060 PSI
    Average: 4,120 PSI ✓ (spec: ≥ 4,000 PSI, margin = 120 PSI)

Verification:
  w/c ratio: 0.48 ✓ (spec: ≤ 0.50)
  Cement content: 564 lbs/CY ✓
  Aggregate quality: Visual inspection OK

Approvals:
  ✓ Approved by Engineer
  ✓ Ready for Production
  Date: January 11, 2026
  Signature: John Smith, P.E., Project Engineer
```

**ACTIONS ON RECEIPT OF TRIAL BATCH**:
- [ ] Verify mix ID matches your submittal
- [ ] Confirm 28-day strength ≥ design f'c (4120 ≥ 4000 OK here)
- [ ] Confirm all test results within spec (slump, air, w/c)
- [ ] Check engineer has signed approval
- [ ] File in project QC folder — reference on first load
- [ ] If any test FAILS or is MARGINAL, reject submittal and request revision

---

### Break Schedule and Strength Correlation

**Standard Break Schedule** (ASTM C31 / C192):

| Age | Cylinders | Use Case |
|-----|-----------|----------|
| 1-day | Optional (2 cyl) | Cold weather, early removal prediction |
| 7-day | Standard (2 cyl) | Form removal decision, trend check |
| 28-day | **CRITICAL** (2 cyl) | **Design strength acceptance** |
| 56-day | Optional (2 cyl) | Long-term trend, durability verification |

**Correlation Formula** (approximate):
```
7-day strength ≈ 60-75% of 28-day (varies by mix, cement type, temp)
Type III cement: 7-day ≈ 75% of 28-day (faster)
Type I cement: 7-day ≈ 60% of 28-day (slower)
Cold weather cured: 7-day ≈ 55% of 28-day (slower hydration at low temp)
```

**Field Implication**: If 7-day test is weak, 28-day will be weak too. Flag immediately.

**EXAMPLE STRENGTH TREND**:
```
4000-1 Standard Mix - Strength Development
  Lab trial batch (Jan 10):
    1-day: not tested
    7-day: 2,850 PSI (71% of 28-day)
    28-day: 4,120 PSI ✓

  Job placement #1 (Feb 15):
    7-day: 2,780 PSI (67% of expected 28-day)
    Predicted 28-day: ~4,150 PSI ✓
    28-day actual: 4,190 PSI ✓

  Job placement #2 (Feb 20, cold weather 38°F):
    7-day: 1,950 PSI (48% — lower due to cold cure temp)
    Predicted 28-day (with heating): ~4,050 PSI ✓
    28-day (heated cured): 4,080 PSI ✓

Interpretation: Cold weather 7-day is lower than warm weather, but 28-day
catches up due to continued hydration. This is normal and acceptable.
```

---

## ASTM STANDARD TEST METHODS TO VERIFY IN SUBMITTAL

### ASTM C39/C39M: Compression Strength Testing

- **How cylinders are tested**: 4" × 8" cylinders placed in compression machine
- **How curing is done**: Standard cure = 72°F ± 2°F in moist room for 28 days
- **Number of cylinders**: Minimum 2 per age (2 @ 7d, 2 @ 28d standard)
- **Acceptance**: Average of 2 cylinders is reported; individual cylinder strength ≤ average - 500 PSI is OK
- **Frequency**: Usually 1 test per 100 CY per day (for normal projects)

### ASTM C138/C138M: Unit Weight (Density) Test

- **How measured**: Fresh concrete is measured by volume and weighed
- **Timing**: Within 15 minutes of batching (before any hydration sets in)
- **Normal range**: 140-150 PCF for normal-weight concrete
- **Purpose**: Verify batch proportions are correct; extreme variance indicates segregation or batching error

### ASTM C231/C231M: Air Content Test (Pressure Method)

- **How measured**: Fresh concrete in sealed pressure bowl; air is forced into solution by known pressure
- **Timing**: Within 15 minutes of batching
- **Acceptance range**: Usually ±1% from target (target 5.5% → accept 4.5-6.5% in field)
- **Failure**: If air is low (< 4% on freeze-thaw exposed concrete), concrete is vulnerable to ice damage
- **False readings**: Vibration or voids from coarse aggregate can cause errors; use ASTM C173 (volumetric) if doubt

### ASTM C143/C143M: Slump Test

- **How measured**: 12" cone filled with concrete in 3 lifts; cone lifted and concrete subsidence measured
- **Timing**: Within 15 minutes of batching
- **Acceptance**: Within ±1 inch of spec range (spec 4-6" → accept 3-7")
- **Failure**: Outside acceptable range = truck rejected

---

## ELEMENT-TO-MIX MAPPING TABLE

This is your primary working document. Create this table during submittal review and maintain it throughout the project.

### Table Template

```
PROJECT: ABC Building Foundation
CONCRETE SUPPLIER: Ready Mix Company
SUBMITTAL DATE: January 8, 2026
SUBMITTAL ID: SUB-023

ELEMENT-TO-MIX ASSIGNMENT

Element | Struct Note | Spec f'c | Spec w/c | Air | Fiber | Supplier Mix ID | Design f'c | Approval | QC Checkpoint |
---|---|---|---|---|---|---|---|---|---|
Footings | Note 4 | 4,000 PSI | ≤ 0.50 | None | No | 4000-1 | 4,000 | ✓ Engineer | 28-day break ≥ 4,000 |
Grade beams | Note 4 | 4,000 PSI | ≤ 0.50 | None | No | 4000-1 | 4,000 | ✓ Engineer | Same as footings |
Slab-on-grade | Note 6 | 3,500 PSI | ≤ 0.55 | 6 oz/CY | Sika | 3500-F | 3,500 | ✓ Engineer | Fiber dispersion check |
Exterior walls | Note 5 | 5,000 PSI | ≤ 0.42 | 5-7% AEA | No | 5000-AE | 5,000 | ✓ Engineer | Air content ≥ 5% |
Below-grade walls | Note 7 | 4,000 PSI | ≤ 0.45 | None | No | 4000-2 | 4,000 | ✓ Engineer | w/c ratio check |
Pier caps | Note 3 | 3,500 PSI | ≤ 0.55 | None | No | 3500-1 | 3,500 | ✓ Engineer | Exposed surface QC |
```

**How to Use This Table**:
1. **Before first load**: Print this table and post at site
2. **On load ticket delivery**: Cross-reference truck against correct mix ID
3. **At placement**: Do final verification that truck matches element being placed
4. **In daily report**: Log which element received which mix

**ACTION**: If truck arrives with wrong mix ID, REJECT and send back.

---

## QUALITY CONTROL DATA POINTS — DAILY VERIFICATION

### Slump Test (ASTM C143) — Test Every Load

**What to Check**:
- [ ] Slump measured within 15 minutes of load arrival
- [ ] Cone not damaged
- [ ] Three lifts, tamped 25 times each
- [ ] Measurement from original height to slumped concrete
- [ ] Result recorded and within specification range

**RED FLAGS**:
- Slump low (<3.5"): Concrete stiff, hard to place; reject unless supplier can explain
- Slump high (>6.5"): Too wet, may affect strength; likely w/c ratio increased without permission — **REJECT**
- Same slump all loads: Either consistent batching (good) or not measuring properly (bad)
- Slump drops more than 1" between front and rear of load: Segregating — **REJECT**

**EXAMPLE DAILY LOG**:
```
Slump Test Log — Feb 15, 2026

Load 1 (4000-1 to footings)
  Arrival time: 8:15 AM
  Measured slump: 5.0"
  Spec: 4-6"
  ✓ ACCEPT

Load 2 (4000-1 to footings)
  Arrival time: 8:45 AM
  Measured slump: 6.2"
  Spec: 4-6"
  ⚠ MARGINAL (slightly high)
  Supplier: "Mixer ran few extra minutes, slump dropped in truck"
  Placed after 5 min rest
  ✓ ACCEPT

Load 3 (5000-AE to exterior walls)
  Arrival time: 10:15 AM
  Measured slump: 3.2"
  Spec: 4-6"
  ✗ REJECT — Low slump, too stiff for wall placement
  Truck returned to plant
```

### Air Content Test (ASTM C231) — Test Entrained Air Mixes

**For ANY concrete spec'd with air entrainment** (freeze-thaw exposure):

- [ ] Air meter (pressure method) or volumetric method used
- [ ] Fresh concrete sample from middle of load (not front/rear)
- [ ] Test within 15 minutes of arrival
- [ ] Result within ±1% of spec (spec 5-7% → accept 4-7% in field)
- [ ] If air is low and concrete is exposed to freeze-thaw, it will spall and deteriorate

**RED FLAGS**:
- Air content <4% on freeze-thaw exposed concrete: **REJECT or get engineer approval**
- Air content >8%: Excessive, will reduce strength — **REJECT**
- Air content varies >2% between loads: Admixture dosing inconsistent — notify supplier

**EXAMPLE DAILY LOG**:
```
Air Content Test Log — Feb 15, 2026 (5000-AE exterior walls)

Load 1 (5000-AE)
  Arrival: 9:00 AM
  Air content (ASTM C231): 5.5%
  Spec: 5-7% with AEA
  ✓ ACCEPT

Load 2 (5000-AE)
  Arrival: 9:30 AM
  Air content: 4.8%
  Spec: 5-7% with AEA
  ⚠ MARGINAL (slightly low)
  Within field tolerance (4-7%), acceptable
  ✓ ACCEPT

Load 3 (5000-AE)
  Arrival: 10:45 AM
  Air content: 3.5%
  Spec: 5-7% with AEA
  ✗ REJECT — Air too low
  Concrete is exposed exterior (freeze-thaw)
  Low air content → spalling risk
  Truck returned to plant
  Supplier to investigate AEA dosing error
```

### Concrete Temperature

- **Measure at placement**: Use thermometer in fresh concrete
- **Specification limits**:
  - Cold weather: ≥ 50°F minimum at placement
  - Hot weather: ≤ 90°F maximum at placement
- **Importance**: Low temperature slows strength gain; high temperature increases shrinkage

**EXAMPLE**:
```
Load 1 (Feb 15, warm weather)
  Concrete temp at arrival: 72°F ✓ (normal, 50-90°F range)

Load 2 (Dec 20, cold weather, 5000-CW cold weather mix)
  Concrete temp at arrival: 58°F ✓ (heated water, above 50°F minimum)
  Protection required: Heat, blankets until ≥ 2,000 PSI strength

Load 3 (August 5, hot weather, 3500-HW hot weather mix)
  Concrete temp at arrival: 88°F ✓ (below 90°F maximum)
  Retarder: Yes, verified (extends working time for placement)
  Protect from sun: Yes, sprinkle water after placement
```

### Cylinder Casting and Curing

- **How many cylinders per load**: Typically 2 @ 7d, 2 @ 28d (4 cylinders per critical load)
- **Who casts them**: Concrete supplier's lab technician or ACI-certified inspector
- **Curing method**:
  - **Standard cure**: Moist room at 72°F ± 2°F (typical for design strength acceptance)
  - **Field cure**: Same location/conditions as concrete in structure (to show in-place strength; if weak, indicates field curing inadequate)
- **Storage**: Cylinders must not be moved after casting; kept moist or in moist room
- **Chain of custody**: Labeled with mix ID, date, load number

**RED FLAGS**:
- Cylinders air-dried instead of moist-cured: Will test low (not valid for acceptance)
- Cylinders moved/disturbed before testing: Invalid test
- Cylinders cast by untrained person: Suspect validity; may require re-test

**EXAMPLE CYLINDER LABEL**:
```
┌─────────────────────────┐
│ PROJECT: ABC Building   │
│ MIX ID: 4000-1          │
│ LOAD: #001              │
│ PLACED: Feb 15, 2026    │
│ AGE: 28-day STANDARD    │
│ LAB ID: TB-4000-F15-01  │
│ CURED: Standard, 72°F   │
│ STRENGTH: [result]      │
│ DATE TESTED: Mar 15     │
└─────────────────────────┘
```

### w/c Ratio Field Verification

The w/c ratio cannot be tested in the field (requires lab analysis), but you can verify:

- [ ] Producer's statement on load ticket matches submittal (same mix ID)
- [ ] No visible excess water in truck (segregation, water on surface = over-watered)
- [ ] Slump consistent with stated mix (if very high slump, water may have been added)
- [ ] Concrete is cohesive (well-distributed sand and cement); not runny

**NOTE**: If w/c ratio is critical (durability specification), some projects perform concrete hardness testing (Maturity method) to verify strength development matches expected w/c performance.

---

## MERGE RULES — HOW TO HANDLE SUBMITTAL REVISIONS

When the supplier submits mix design updates or corrections:

### Adding a New Mix

**Scenario**: Supplier submits 3500-F mix for first time (was not in original submittal).

**ACTION**:
- Add new row to your element-to-mix table
- Require trial batch report BEFORE any placement
- Get engineer signature
- Proceed with first load

### Revision to Existing Mix (Same ID, Different Properties)

**Scenario**: 4000-1 initially had 564 lbs cement; supplier updates to 580 lbs (stronger design f'c).

**ACTION**:
- Flag as revision; ask supplier: "Is this a mix change? What triggered it?"
- If it's a source change (different cement mill), mark as "Version 2, effective [date]"
- Require new trial batch report
- Get engineer approval signature
- In element-to-mix table, add note: "4000-1 (Rev. 2, from [date])"
- Store BOTH versions (v1 and v2) with dates

**EXAMPLE**:
```
Mix ID: 4000-1
Version 1 (original): Jan 8, 2026
  Design f'c: 4,000 PSI
  w/c ratio: 0.48
  Cement: 564 lbs/CY Type I/II
  Placements: Loads #1-15

Version 2 (revised): Feb 10, 2026
  Design f'c: 4,000 PSI (same)
  w/c ratio: 0.47 (tighter)
  Cement: 580 lbs/CY Type I/II (higher cement, lower water)
  Reason: Durability improvement for below-grade walls
  Placements: Loads #16 onward
  Trial batch: Feb 5 (4,120 PSI @ 28d) ✓
```

### Flagging Non-Conformances

**When to flag**:
- [ ] Design f'c < specified f'c (e.g., spec 4000, design 3900): **REJECT**
- [ ] w/c ratio > spec maximum (e.g., spec ≤ 0.45, submittal 0.48): **REJECT**
- [ ] Element missing from assignment table (not mapped to a mix)
- [ ] Trial batch strength marginal (barely above minimum)
- [ ] Engineer has NOT signed approval

**Your Document**: Create a "Submittal Issues" list and email to engineer:
```
CONCRETE SUBMITTAL SUB-023 — ISSUES REQUIRING RESOLUTION

Mix 5000-AE for exterior walls:
  ⚠ Specified minimum f'c: 5,000 PSI
  ⚠ Submittal design f'c: 4,950 PSI
  ISSUE: Design strength BELOW spec requirement
  ACTION: Revise mix to design f'c ≥ 5,000 PSI or get engineer waiver

Mix 4000-2 for below-grade walls:
  ⚠ Specified maximum w/c: 0.45
  ⚠ Submittal w/c ratio: 0.47
  ISSUE: w/c ratio ABOVE spec requirement
  ACTION: Revise mix or obtain engineer waiver (durability risk noted)

Missing element:
  ⚠ Pier caps (Struct. Note 3) not assigned to any mix ID
  ACTION: Supplier to clarify — use 3500-1 or 4000-1?

Please advise how to proceed.
```

---

## STORAGE SCHEMA — MULTI-FILE DATA STORE

### Where Mix Data Goes in Your QC System

**File**: `specs-quality.json` (or your project QC database)

**Section**: `mix_designs` array

**Complete example entry**:
```json
{
  "mix_id": "4000-1",
  "version": 1,
  "producer": "Ready Mix Company",
  "producer_contact": "Joe Smith, (555) 123-4567",
  "design_fc": 4000,
  "spec_fc": 4000,
  "wc_ratio": 0.48,
  "slump_range": "4-6 inches",
  "air_content": "5-7%",
  "air_entraining": true,
  "cement_type": "Type I/II",
  "cement_content_lbs_cy": 564,
  "coarse_aggregate": "#57 limestone, 1.875\" #57",
  "fine_aggregate": "Natural sand, Granite Ridge Quarry",
  "aggregate_max_size": "3/4 inch",
  "admixtures": [
    {
      "type": "water reducer with delay",
      "product": "MasterRheobuild 2100",
      "dosage": "4.0 oz/CY",
      "function": "reduce w/c, extend working time"
    },
    {
      "type": "air-entraining agent",
      "product": "Daravair 1400",
      "dosage": "0.4 oz/CY",
      "function": "freeze-thaw protection"
    }
  ],
  "unit_weight_pcf": 145.0,
  "trial_batch_report": {
    "lab_id": "TB-4000-2026-001",
    "date": "2026-01-10",
    "slump_measured": 5.5,
    "air_content_measured": 5.5,
    "strength_7d": 2850,
    "strength_28d": 4120,
    "unit_weight_measured": 144.8,
    "approved": true,
    "approval_date": "2026-01-11"
  },
  "assigned_elements": [
    "footings",
    "grade_beams",
    "pier_caps"
  ],
  "element_mapping": {
    "footings": {
      "spec_section": "03 30 00",
      "spec_note": 4,
      "spec_requirement": "4,000 PSI, w/c <= 0.50"
    },
    "grade_beams": {
      "spec_section": "03 30 00",
      "spec_note": 4,
      "spec_requirement": "4,000 PSI, w/c <= 0.50"
    }
  },
  "spec_section": "03 30 00",
  "submittal_id": "SUB-023",
  "submittal_date": "2026-01-08",
  "approval_status": "approved",
  "approval_date": "2026-01-11",
  "approval_by": "John Smith, P.E.",
  "cold_weather_modification": {
    "active": true,
    "mix_id_variant": "4000-CW",
    "cement_type": "Type III",
    "accelerator": "2% Pozzutec non-chloride",
    "water_heating": "120°F",
    "placement_temp_min": 50,
    "ambient_temp_trigger": 40,
    "form_strip_time": "3-5 days",
    "cost_premium": 3.50,
    "available_dates": "Dec 15 - Mar 1"
  },
  "hot_weather_modification": {
    "active": true,
    "mix_id_variant": "4000-HW",
    "retarder_type": "Delvo retarder",
    "retarder_dosage": "2.0 oz/CY",
    "ice_replacement": "up to 300 lbs/truck",
    "placement_temp_max": 90,
    "ambient_temp_trigger": 85,
    "set_delay": "2 hours",
    "cost_premium": 0.40,
    "available_dates": "May 15 - Sep 30"
  },
  "field_testing_frequency": "1 test per 100 CY per day (slump, air)",
  "strength_test_breaks": [
    {
      "age_days": 7,
      "cylinders": 2,
      "cure_method": "standard (72°F moist room)",
      "expected_strength": 2850,
      "acceptance_min": 2500,
      "notes": "Form removal decision"
    },
    {
      "age_days": 28,
      "cylinders": 2,
      "cure_method": "standard (72°F moist room)",
      "expected_strength": 4120,
      "acceptance_min": 4000,
      "notes": "Design strength acceptance"
    }
  ],
  "qc_checkpoints": [
    "slump within 4-6 inches (test every load)",
    "air content 5-7% if AEA (test first 3 loads, then every 100 CY)",
    "no visible excess water in truck",
    "load ticket matches mix ID",
    "concrete temperature 50-90°F at placement",
    "7-day strength >= 2,500 PSI (flag if weak)",
    "28-day strength >= 4,000 PSI (design acceptance)",
    "cylinder curing method confirmed (standard or field)",
    "w/c ratio not increased without approval"
  ],
  "cost_per_cy": 125.50,
  "notes": "Standard mix for footings/grade beams. Trial batch passed Jan 10. Ready for production."
}
```

**Additional Storage**:

**File**: `daily-placements.json` (or concrete delivery log)

```json
{
  "placements": [
    {
      "date": "2026-02-15",
      "element": "footings",
      "mix_id": "4000-1",
      "load_number": 1,
      "load_ticket_number": "RTM-002841",
      "volume_cy": 8.5,
      "arrival_time": "08:15",
      "slump_measured": 5.0,
      "slump_spec": "4-6",
      "slump_status": "accept",
      "air_content_measured": null,
      "air_content_spec": "5-7",
      "air_content_status": "not tested (no AEA)",
      "concrete_temp_f": 72,
      "weather": "Clear, 65°F",
      "cylinders_cast": 4,
      "cylinders_ids": ["TB-4000-F15-01a", "TB-4000-F15-01b", "TB-4000-F15-02a", "TB-4000-F15-02b"],
      "placement_time": "08:30-09:00",
      "placed_by": "ABC Concrete Contractor, Super: Tom Jones",
      "accepted_by": "John Smith, P.E.",
      "notes": "First footing pour. Trial batch approved Jan 11. All tests passing. Standard cure cylinders sent to lab."
    },
    {
      "date": "2026-02-15",
      "element": "exterior walls",
      "mix_id": "5000-AE",
      "load_number": 1,
      "load_ticket_number": "RTM-002842",
      "volume_cy": 12.0,
      "arrival_time": "09:00",
      "slump_measured": 5.5,
      "slump_spec": "4-6",
      "slump_status": "accept",
      "air_content_measured": 5.5,
      "air_content_spec": "5-7",
      "air_content_status": "accept",
      "concrete_temp_f": 73,
      "weather": "Clear, 66°F",
      "cylinders_cast": 4,
      "cylinders_ids": ["TB-5000-F15-01a", "TB-5000-F15-01b", "TB-5000-F15-02a", "TB-5000-F15-02b"],
      "placement_time": "09:15-10:15",
      "placed_by": "ABC Concrete Contractor, Super: Tom Jones",
      "accepted_by": "John Smith, P.E.",
      "notes": "First wall pour. Air-entrained mix, freeze-thaw exposure. Slump and air both passing."
    }
  ]
}
```

---

## SUMMARY CHECKLIST — CONCRETE MIX SUBMITTAL REVIEW

**BEFORE FIRST LOAD**:

- [ ] **Identification**: Producer's mix ID system understood; mixes clearly identified
- [ ] **Element mapping**: Every structural element assigned to a mix ID (no gaps)
- [ ] **Design strength**: Design f'c ≥ specified f'c for each element
- [ ] **w/c ratio**: w/c ratio ≤ specified maximum for each mix
- [ ] **Trial batch report**: Received, reviewed, engineer-approved
- [ ] **Trial strength**: 28-day ≥ design f'c (margin verified)
- [ ] **Admixtures**: All products and dosages listed; compatible with each other
- [ ] **Certifications**: ACI Concrete Certifications provided (lab certification, mix design cert)
- [ ] **Cold/hot weather**: Modifications identified if required for project schedule
- [ ] **Engineer signature**: All mixes signed approved by PE/engineer

**FOR EACH LOAD**:

- [ ] **Load ticket**: Cross-reference mix ID with submittal
- [ ] **Slump test**: ASTM C143, recorded, within spec range
- [ ] **Air content test**: ASTM C231 (if AEA mix), within spec range
- [ ] **Concrete temperature**: Within placement limits (50-90°F typical)
- [ ] **Appearance**: Cohesive, no excess water, no segregation
- [ ] **Cylinder casting**: Correct number cast, labeled, sent to lab
- [ ] **Daily report**: Load logged with all QC data
- [ ] **Acceptance**: Signed by site inspector and engineer

**ON TEST RESULTS**:

- [ ] **7-day strength**: Trend check; flag if weak (may indicate cold cure or batch error)
- [ ] **28-day strength**: Acceptance test; must be ≥ design f'c
- [ ] **Strength > minimum**: Safety margin present; not barely passing
- [ ] **Uniform strength**: Loads show consistent strength (not high/low variance)

---

## NOTES

- Concrete submittal review is a foundation-level task. Weak submittals lead to field failures, compression test rejections, and schedule delays.
- The element-to-mix table is your reference document. Maintain it on the jobsite and use it for every load verification.
- w/c ratio and slump are your two daily control parameters. Verify these at every load.
- Cold weather mixes must be ordered in advance (Type III cement, heating); hot weather mixes need retarder in advance.
- Trial batch reports are not optional; they are your baseline for accepting production concrete.
- Strength testing takes time (28 days); do not delay specifying the test if you need early results (request 7-day trend, 14-day intermediate).
- Common submittal failures: Design f'c too low, w/c ratio too high, missing elements, no trial batch, no engineer signature, admixture incompatibilities.
