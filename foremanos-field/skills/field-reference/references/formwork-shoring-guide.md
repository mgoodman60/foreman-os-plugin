# Formwork and Shoring Field Guide
## Superintendent's Reference — ACI 347 Principles, Selection, Stripping, and Safety

---

## 1. FORMWORK TYPES COMPARISON

### System Selection Table

| System | Best For | Reuse Cycles | Finish Quality | Relative Cost | Setup Speed |
|--------|----------|-------------|----------------|---------------|-------------|
| **Plywood/Lumber (Job-Built)** | Custom shapes, one-off pours, small jobs | 3-5 uses (plywood), unlimited (lumber) | Good with HDO plywood | Low material, high labor | Slow |
| **Aluminum Panel (Symons, etc.)** | Walls, columns, repetitive layouts | 200-500+ uses | Good (panel marks at joints) | Medium | Fast |
| **Engineered Systems (Doka, PERI, EFCO)** | High-rise, heavy pours, large walls, post-tensioned decks | 500-1,000+ uses | Excellent (tight tolerances) | High rental, low labor | Fast |
| **Steel Forms** | Repetitive elements (curb, tunnel liner, precast) | 1,000+ uses | Excellent | High | Medium |
| **Insulating Concrete Forms (ICF)** | Residential, low-rise walls (stay-in-place) | 1 (permanent) | N/A (covered) | Medium | Fast |
| **Fiber Tube (Sonotube)** | Round columns | 1 (disposable) | Smooth | Low | Very Fast |

### Selection Criteria Decision Guide

- **Pour height <4 feet:** Job-built plywood/lumber or aluminum panels — simplest, most economical
- **Pour height 4-12 feet:** Aluminum panel systems or engineered forms — lateral pressure demands stiffer systems
- **Pour height >12 feet:** Engineered systems mandatory — ganged forms, climbing forms, or slip forms
- **Reuse >10 cycles on same project:** Aluminum or engineered systems pay for themselves
- **Architectural finish required:** HDO plywood, fiberglass-lined forms, or engineered systems with controlled tie patterns
- **Curved walls:** Flexible plywood (1/4" bending ply), curved engineered panels, or custom-built
- **Budget-critical small job:** Job-built lumber/plywood; rent aluminum for walls

---

## 2. FORMWORK PRESSURE — SIMPLIFIED CALCULATIONS

### Lateral Pressure Basics

Concrete exerts lateral pressure on wall and column forms. This is the #1 cause of blowouts when underestimated.

**Basic Rule:**
- **Lateral pressure = 150 x h (PSF)**
- Where h = head of concrete in feet (depth of fluid concrete above the point)
- 150 PCF = unit weight of standard concrete

**Example:** At 6 feet below the top of a pour, lateral pressure = 150 x 6 = **900 PSF**

### Maximum Pressure by Pour Rate and Temperature

ACI 347 provides maximum design pressures considering pour rate (R, in feet per hour) and concrete temperature (T, in degrees F). These simplified rules apply to **walls** with normal-weight concrete, no retarders, and internal vibration:

| Pour Rate (ft/hr) | Concrete Temp 50°F | Concrete Temp 70°F | Concrete Temp 90°F |
|--------------------|--------------------|--------------------|--------------------|
| 3 | 900 PSF | 750 PSF | 660 PSF |
| 5 | 1,200 PSF | 975 PSF | 840 PSF |
| 7 | 1,500 PSF | 1,200 PSF | 1,020 PSF |
| 10 | 2,000 PSF | 1,575 PSF | 1,320 PSF |
| >10 (pumped/fast) | Full hydrostatic | Full hydrostatic | Full hydrostatic |

**Critical Rules of Thumb:**
- **Pour rate >7 ft/hr or concrete temp <50°F:** Design for full hydrostatic pressure (150 x total head)
- **Retarders or HRWR admixtures:** Add 20-30% to calculated pressure — concrete stays fluid longer
- **SCC (Self-Consolidating Concrete):** ALWAYS full hydrostatic — SCC exerts full fluid pressure
- **Columns:** ALWAYS design for full hydrostatic regardless of pour rate (small cross-section, fast fill)

### Quick Pressure Check for the Field

1. Determine planned pour rate (feet per hour)
2. Check concrete temperature on batch ticket
3. Look up maximum pressure from table above
4. Compare to form system rated capacity (from manufacturer or engineer)
5. **If calculated pressure exceeds form capacity — STOP and reduce pour rate or get engineering review**

---

## 3. SHORING AND SHORES

### Shore Types

- **Single post shores (Ellis type):** Adjustable steel posts, most common for slab forming, rated 5,000-10,000 lbs typical
- **Frame shores:** H-frame with cross-bracing, higher capacity, 10,000-25,000 lbs per leg
- **Heavy-duty towers (Doka Staxo, PERI PD 8):** Modular tower systems for high clearances or heavy loads, 30,000-100,000+ lbs per leg

### Shore Spacing — Rules of Thumb

**For typical 8" concrete slab (100 PSF dead load):**

| Shore Capacity (lbs) | Typical Spacing | Tributary Area per Shore |
|-----------------------|-----------------|--------------------------|
| 5,000 lbs | 5' x 5' (25 SF) | 25 SF x 100 PSF + form weight = ~2,800 lbs |
| 8,000 lbs | 6' x 6' (36 SF) | 36 SF x 100 PSF + form weight = ~3,900 lbs |
| 10,000 lbs | 7' x 7' (49 SF) | 49 SF x 100 PSF + form weight = ~5,200 lbs |

**Key Capacity Rules:**
- **Minimum shore capacity** = (slab thickness in inches / 12) x 150 PCF x tributary area + 50 PSF live load (construction loads) x tributary area + form dead load
- **Safety factor:** Shores must be rated for 2x calculated load minimum (ACI 347 requirement)
- **Never exceed manufacturer's rated capacity** — check the label stamped on the shore
- **Soft ground:** Use shore base plates on mudsills (minimum 2x nominal lumber); shore on bare soil is an immediate failure risk

### Shore Installation Checklist

1. Verify shore capacity matches shoring layout drawing
2. Install mudsills on all soil or weak surfaces (minimum 2x10 continuous under row of shores)
3. Set base plates — wedge tight, plumb
4. Shore must be plumb within 1/8" per foot of height
5. Cross-brace all freestanding shores per manufacturer requirements
6. Tighten all adjustment screws — finger tight plus 1/4 turn with wrench
7. Verify shore head contacts stringer/joist tightly — no gaps
8. Do not modify shores (no cutting, welding, or bending)
9. Tag or mark each shore with rated capacity if not factory-stamped

---

## 4. RESHORING — MULTI-STORY CONSTRUCTION

### Why Reshoring Matters

When formwork is stripped from a recently poured slab, that slab must carry its own weight plus any construction loads above. If the slab has not reached adequate strength, it can crack, deflect excessively, or collapse. Reshoring transfers load to multiple floors below.

### Reshoring Procedure

1. **Strip forms from slab** — remove formwork and original shores
2. **Install reshores within 24 hours of stripping** — do NOT leave slabs unsupported overnight
3. **Reshores placed directly under shores above** — load path must be continuous through floors
4. **Number of reshored floors:** Typically **2-3 floors below the active pour level**
   - 2 floors minimum for slabs with normal reinforcement
   - 3 floors for post-tensioned or heavy slabs, or when rapid cycling
5. **Reshores remain until concrete reaches design strength** — typically 28 days, but check with engineer

### Reshoring vs. Backshoring

| Method | Definition | When Used |
|--------|-----------|-----------|
| **Reshoring** | Strip all forms, then install new shores (reshores) | Standard multi-story — slab briefly carries own weight during strip |
| **Backshoring** | Install new shores BEFORE removing original shores (never fully unloaded) | Critical slabs, long spans, or when engineer requires no deflection during strip |

### Reshoring Layout Rules

- **Place reshores at same spacing as original shores** or tighter — never wider
- **Snug tight only** — reshores should be firm contact but not jacked to pre-load the slab
- **If slab deflected during strip:** Reshores under the deflected slab do NOT push it back up — they only prevent further deflection
- **Document reshoring installation** — note date, location, floor number, and configuration

---

## 5. STRIPPING TIMES

### Minimum Stripping Times by Element

| Element | Minimum Concrete Strength | Typical Time (70°F, Type I cement) | Notes |
|---------|---------------------------|-------------------------------------|-------|
| **Walls (vertical forms)** | 500 PSI | 12-24 hours | Support own weight only; no lateral loads |
| **Columns (vertical forms)** | 500 PSI | 12-24 hours | Protect from impact after strip |
| **Beam sides** | 500 PSI | 12-24 hours | Leave beam bottom shores in place |
| **Slab forms (span ≤10')** | 75% of f'c | 3-7 days | Reshore immediately after strip |
| **Slab forms (span 10-20')** | 75% of f'c | 7-10 days | Engineer may require higher % |
| **Beam bottoms (span ≤10')** | 75% of f'c | 7-10 days | Reshore required |
| **Beam bottoms (span >20')** | 85% of f'c or engineer approval | 10-14 days | Extended shoring typical |
| **Post-tensioned slabs** | After stressing (typically 3,000-3,500 PSI) | 3-5 days | Do NOT strip until tendons are stressed and engineer approves |
| **Cantilever elements** | 90% of f'c or engineer approval | 14+ days | Most critical — backshore until full strength |

### Verifying Strip Strength

- **Maturity method (best):** Embedded sensors track temperature history and calculate equivalent age/strength in real time
- **Cylinder breaks:** Field-cured cylinders (NOT lab-cured) at jobsite conditions; break at planned strip time
- **Minimum:** 2 cylinders per test; average must meet required strength
- **Rebound hammer (Schmidt hammer):** Quick field check, NOT a substitute for cylinders, but useful for relative comparison

### Extended Stripping Times — Cold Weather

| Average Curing Temperature | Multiplier on Typical Strip Time |
|----------------------------|----------------------------------|
| 70°F+ | 1.0x (standard) |
| 60°F | 1.3x |
| 50°F | 1.7x |
| 40°F | 2.5x |
| Below 40°F | Do NOT strip without cylinder break verification |

---

## 6. FORM RELEASE AGENTS

### Types and Selection

| Type | Application | Pros | Cons |
|------|-------------|------|------|
| **Petroleum-based (mineral oil)** | Brush, spray, or roller | Inexpensive, widely available | Stains concrete, interferes with coatings/sealers |
| **Vegetable/plant-based** | Brush, spray | Low VOC, less staining, environmentally preferred | Higher cost, may require reapplication |
| **Chemical-reactive** | Spray | Best finish quality, reacts with cement to form release layer | Most expensive, temperature-sensitive application |
| **Wax-based emulsion** | Spray | Good for steel and aluminum forms | Can leave residue, may affect bonding of finishes |

### Application Rules

- **Apply to CLEAN forms before rebar placement** — release agent on rebar reduces bond strength
- **Thin, uniform coat** — excessive release agent causes bug holes and surface defects
- **Apply immediately before forming** where possible — dust and debris stick to oiled forms
- **Do NOT apply in rain or on wet forms** — water prevents adhesion to form surface
- **Temperature:** Most products require application above 40°F
- **Reapply if forms sit idle more than 24 hours** before pour

---

## 7. FORMWORK INSPECTION CHECKLIST

### Pre-Pour Verification (Every Pour)

**Alignment and Dimensions:**
- [ ] Form dimensions match drawings (check at top, middle, and bottom)
- [ ] Walls plumb within 1/4" per 10 feet (check with 4' level or plumb bob)
- [ ] Bracing adequate — diagonal braces at 45° maximum, minimum every 8 feet along wall
- [ ] Top of form at correct elevation (survey check)
- [ ] Corners square — check diagonals

**Structural Integrity:**
- [ ] Snap ties at correct spacing per form design (typically 18-24" OC horizontal, 12-18" OC vertical)
- [ ] All snap tie wedges tight — hand tight plus tap with hammer
- [ ] Walers aligned and continuous — no gaps at splices
- [ ] Strongbacks plumb and attached to walers
- [ ] Kickers/braces anchored to concrete or deadmen (not just stakes in soil)

**Pour Preparation:**
- [ ] Cleanout openings at base of all walls >4 feet tall — debris removed, openings secured for pour
- [ ] Form release agent applied — uniform coat, no excess, no overspray on rebar
- [ ] Chamfer strips installed at exposed corners (3/4" typical)
- [ ] Rustication strips, reveals, and blockouts secured and oiled
- [ ] Embedded items placed and secured: anchor bolts, sleeves, inserts, MEP penetrations
- [ ] Rebar cover verified with chairs/spacers — minimum cover per drawings

**Deck/Slab Forms:**
- [ ] Shore spacing matches shoring layout
- [ ] All shores plumb, tight, on base plates
- [ ] Mudsills under all shores on soil
- [ ] Stringers and joists at correct spacing
- [ ] Plywood joints over supports — no unsupported edges
- [ ] Camber built in per structural drawings (typically L/360 to L/240 of span for beams)
- [ ] Edge forms at correct elevation and secured

---

## 8. COMMON FORMWORK FAILURES

### Blowouts

**What it looks like:** Concrete bursts through or bulges forms outward, usually at the base of tall pours.

**Causes:**
- Pour rate exceeded form design capacity
- Missing or improperly installed snap ties
- Snap tie wedges not tightened
- Waler splice at a high-pressure location
- Hot concrete in cold weather (stays fluid, builds pressure)
- SCC or heavily retarded concrete used without form upgrade

**Prevention:**
- Verify pour rate before starting — communicate maximum rate to pump operator and crew
- Double-check snap ties in bottom 1/3 of wall (highest pressure zone)
- Monitor form during pour — assign a dedicated form watcher
- Have backup materials on site (lumber, clamps, come-alongs) for emergency bracing
- **Stop the pour immediately** if any form movement detected — do NOT "pour through it"

### Settlement and Deflection

**Causes:** Shores on soft ground, undersized shores, missed shores in layout, overloaded deck
**Prevention:** Mudsills mandatory on soil, verify shore layout matches drawing, pre-load check

### Misalignment

**Causes:** Inadequate bracing, wind loads, vibrator contact with forms, unbalanced pour
**Prevention:** Brace both sides, pour in balanced lifts, check plumb during pour

### Leakage at Joints

**Causes:** Gaps between form panels, worn form edges, missing foam tape
**Prevention:** Foam tape at panel joints, caulk at penetrations, tighten all hardware

---

## 9. COLD WEATHER FORMWORK CONSIDERATIONS

### Insulation Requirements

- **Protect concrete from freezing for minimum 24 hours** — concrete that freezes before reaching 500 PSI can lose 50% of ultimate strength permanently
- **Insulated blankets:** 2" minimum thickness on exposed surfaces when ambient temp below 40°F
- **Heated enclosures:** Required when ambient below 20°F; maintain 50°F minimum inside enclosure
- **Leave forms in place longer** — wood forms provide insulation value (R-1 per inch of plywood)

### Extended Stripping Times

- Standard stripping times assume 70°F curing
- Below 50°F: Double the standard stripping time or verify strength with cylinder breaks
- Below 40°F: Do NOT strip without cylinder breaks confirming minimum strength
- After stripping in cold weather: Apply insulation to exposed surfaces immediately

### Heating Methods

| Method | Pros | Cons | Safety Notes |
|--------|------|------|-------------|
| **Hydronic heat (glycol tubing)** | Even heat, safe, no CO2 | Expensive setup | Best for large pours |
| **Electric blankets** | Easy to use, consistent | Limited coverage | Check for wet connections |
| **Propane indirect heaters** | Portable, high output | CO2 concerns in enclosures | Ventilation mandatory |
| **Direct-fired heaters** | PROHIBITED | Carbonation of surface, CO2 exposure | Do NOT use near fresh concrete |

---

## 10. FORMWORK SAFETY — OSHA 1926.703

### Key OSHA Requirements

- **Formwork must be designed, fabricated, erected, supported, braced, and maintained** so it will support all loads without failure
- **Drawings/plans required** for all shoring systems — must be available on-site for inspection
- **Shoring equipment must not be damaged** — bent shores, cracked screw threads, or damaged frames must be removed from service
- **No construction loads** on partially completed structures until forms and shores are in place and the engineer of record approves

### Fall Protection During Form Work

- **Guardrails required** on all formwork platforms and working surfaces 6 feet or more above lower level
- **Guardrail specs:** 42" top rail (±3"), mid-rail, toe board (3.5" minimum)
- **Leading-edge work:** Personal fall arrest system required when guardrails not feasible
- **Perimeter protection** during deck forming — cable/chain guardrails or personal fall arrest
- **Openings in formed decks** >2" must be covered or guarded

### Concrete Placement Safety

- **No workers allowed below forms being filled** unless protected from falling objects
- **Concrete bucket/hopper inspection** — check for cracks, worn cables, latch function before each use
- **Concrete pump line restraints** at every elbow and at discharge hose — sudden pressure surges can whip unrestrained lines
- **Vertical pour protection:** Workers placing concrete on walls >6 feet must have fall protection; working from top of wall forms requires guardrails or harness

### Stripping Safety

- **Concrete must have adequate strength before stripping** — superintendent must authorize strip
- **No one below the area being stripped** — falling forms and debris are the primary hazard
- **Remove forms systematically** — start at one end, work to the other; never remove random sections
- **Shore removal sequence matters** — remove shores from mid-span toward supports (prevents concentrated loads)
- **Stack stripped forms immediately** — do not lean loose form panels against walls or columns

---

## 11. QUICK REFERENCE — FIELD DECISION TABLE

### "What System Do I Need?"

| Situation | Recommended System | Key Consideration |
|-----------|--------------------|-------------------|
| Foundation walls <8' tall | Job-built plywood or aluminum panels | Check pressure vs. tie spacing |
| Foundation walls 8-16' tall | Aluminum panel systems (ganged) | Gang forms for speed; crane required |
| Core walls high-rise | Engineered climbing/self-climbing forms | Engineer designs; crew training required |
| Elevated slabs, typical | Plywood on aluminum beams + post shores | Standard shore spacing per layout |
| Elevated slabs, heavy loads or long span | Engineered table forms or flying forms | Crane picks; cycle time advantage |
| Round columns ≤36" diameter | Sonotube (fiber tube) | One-time use; easy strip |
| Round columns >36" or architectural | Steel or fiberglass column forms | Reusable; better finish |
| Grade beams | Job-built plywood + stakes/bracing | Simple; stakes must resist lateral pressure |
| Retaining walls | Aluminum panels or engineered (based on height) | One-sided forming against soil = special design |

### Pour Rate Quick Decision

| Condition | Maximum Safe Pour Rate |
|-----------|------------------------|
| Standard wall forms, 70°F+ concrete | 5-7 ft/hr |
| Standard wall forms, 50-70°F concrete | 3-5 ft/hr |
| Standard wall forms, <50°F concrete | Reduce to 2-3 ft/hr or upgrade forms |
| Column forms (any temp) | Full hydrostatic — pour rate doesn't reduce pressure |
| SCC concrete (any element) | Full hydrostatic — always |
| Retarded concrete | Reduce rate 30-50% from standard |

---

## 12. DOCUMENTATION AND RECORDS

### Required Records for Each Pour

- **Shoring/forming layout drawing** — signed/stamped by engineer or qualified designer
- **Pre-pour inspection checklist** — signed by superintendent and/or form carpenter foreman
- **Concrete delivery tickets** — time, mix design, slump, temperature, admixtures
- **Cylinder break results** — field-cured and lab-cured, linked to pour location
- **Strip authorization** — documented decision with strength verification method and results
- **Reshoring log** — dates installed, dates removed, floors involved
- **Any deviations or field modifications** — documented with engineer approval if structural

### Liability Notes

- Formwork failure is one of the most common causes of construction fatalities
- The GC/superintendent has responsibility for means and methods — formwork design and execution falls on the builder, not the structural engineer of the permanent structure
- Document everything — if a blowout, collapse, or failure occurs, OSHA will ask for your shoring plans, inspection records, and concrete strength verification
