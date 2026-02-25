# Delivery Verification Reference

## Overview

When materials arrive on the jobsite, verification is a critical quality control step. This reference covers how to verify an incoming delivery against purchase order requirements and specification requirements, including visual inspection, documentation review, and spec compliance checking.

**Purpose:** Ensure materials meet project requirements before acceptance and installation.

---

## Three-Part Verification Process

### Part 1: Visual Inspection Checklist

Perform at material arrival, before unloading and acceptance:

**Quantity & Packaging:**
- [ ] Count/measure received quantity (compare against PO quantity)
- [ ] Verify packaging condition: crates intact, shrink wrap not compromised, pallets undamaged
- [ ] Check for signs of shipping damage: dents, crushed corners, torn cartons
- [ ] Confirm no visible water damage or weather exposure
- [ ] For bulk materials (concrete, asphalt): verify truck/load ID matches PO

**Product Identity:**
- [ ] Confirm product model/part number matches PO
- [ ] Check product labels/markings visible and legible
- [ ] Verify color/finish matches (for finish materials, paint, etc.)
- [ ] Lot numbers or batch numbers visible (for consistency-critical items)
- [ ] Serial numbers documented (for equipment/appliances)

**Condition Assessment:**
- Document condition at arrival:
  - **Acceptable** — Material undamaged, ready for use
  - **Minor damage** — Small dents, scratches, tape creases; does not affect performance
  - **Major damage** — Deformation, cracking, water intrusion; may affect performance
  - **Refused** — Damaged beyond acceptance; do not unload

**Photo documentation:**
- Take photos of any damage or unusual conditions
- Photo should show product identity marker (label, model #) and damage
- Attach to receiving report

---

### Part 2: Documentation Verification

Review all paperwork that accompanies the material:

**Packing Slip / Bill of Lading:**
- [ ] Matches PO number and PO date
- [ ] Item descriptions match (not just part numbers)
- [ ] Quantity listed matches physical count
- [ ] Date shipped aligns with expected lead time
- [ ] Carrier/truck information for receiving records

**Manufacturer Documentation:**
- [ ] Product data sheet or specification sheet included
- [ ] Model number and serial number (if applicable)
- [ ] Installation/handling instructions provided
- [ ] Warranty card or documentation present
- [ ] Safety warnings or precautions clearly marked

**Certifications & Test Reports (if required):**
- [ ] Mill certificate present (for structural steel, rebar)
- [ ] Batch ticket included (for concrete, asphalt)
- [ ] Product certification present (UL listing, ETL, CSA, etc.)
- [ ] Test reports (ASTM or equivalent) included
- [ ] Lab accreditation visible (for test results)

**Special Requirements:**
- [ ] For materials requiring SDS (Safety Data Sheets): confirm present
- [ ] For materials with restricted use: confirm restrictions noted on documentation
- [ ] For specialty items: confirm all required certs/approvals present

**Document Filing:**
- Place originals in project cert tracking file immediately
- Scan for digital archive
- Link to procurement record in material-tracker system

---

### Part 3: Specification Compliance Check

Compare material against specification section requirements:

**Material Properties:**
- [ ] Material type/class meets spec requirement (e.g., Grade 60 rebar, 4,000 PSI concrete)
- [ ] Strength/performance specs verified by certs or test reports
- [ ] Chemical composition acceptable (e.g., carbon content, alloy elements)
- [ ] Finishing/coating meets spec (e.g., paint system, galvanizing)

**Dimensional Requirements:**
- [ ] Product dimensions within spec tolerance
- [ ] For fabricated items: confirm fabrication matches approved submittal
- [ ] For MEP equipment: model selected is submittal-approved version

**Compliance Review Methodology:**
Reference **submittal-intelligence skill** for detailed compliance checking:
1. Pull approved submittal from submittal_log
2. Cross-check product data against submittal approvals
3. Verify material certs/test results meet submittal-approved properties
4. Note any deviations from approved submittal
5. Document compliance decision: conforming, conditional, non-conforming

**Spec Section References:**
- Note the applicable spec section number
- Quote relevant spec language (e.g., "Rebar shall be ASTM A615 Grade 60")
- Confirm material meets minimum requirements (use ≥, ≤, = as applicable)

---

## Material-Specific Verification Checklists

### Concrete (Ready-Mix)

**On Arrival:**
- [ ] Truck ID and load number match ticket
- [ ] Batch ticket present and legible
- [ ] No visible segregation of aggregate and cement paste
- [ ] Slump appears consistent (if observable)

**Batch Ticket Verification:**
- [ ] Batch ticket matches load number on truck
- [ ] Mix design number matches spec requirement
- [ ] PSI design strength meets spec (e.g., 4,000 PSI)
- [ ] Slump range documented (typically 4-6 inches)
- [ ] Air content recorded (6% ± 1.5% for air-entrained)
- [ ] Water-cement (w/c) ratio as designed
- [ ] Admixtures listed and match spec:
  - Air entrainment for freeze-thaw exposure
  - Retarders for hot weather
  - Water reducers for strength gain
  - Fly ash or other pozzolans if spec-required
- [ ] Time batched recorded
- [ ] Batch ticket signed by concrete supplier QC

**Strength Verification:**
- Confirm test cylinders will be cast (if required by spec)
- Verify curing conditions for test cylinders
- Schedule cylinder testing at 7 days and 28 days
- Curing condition matches design assumptions (standard, field, etc.)

**Non-Conformance Examples:**
- Slump outside range (concrete may be too dry or too wet)
- Air content < 4% or > 8% (durability issue)
- Wrong PSI shipped (must resolve before placement)
- Unknown admixtures present (may not be approved)

---

### Structural Steel

**On Arrival:**
- [ ] Mill certs present (critical; material should not be unloaded without)
- [ ] No visible corrosion, rust, or scale damage
- [ ] All members present (count against packing list)
- [ ] Fabrication markings/erection marks present and legible

**Mill Certificate Verification:**
- [ ] Heat number clearly marked and matches mill cert
- [ ] Grade designation visible (e.g., ASTM A992 Grade 50)
- [ ] Heat number cross-referenced on bill of lading
- [ ] Chemical analysis results included:
  - Carbon content within range
  - Manganese, silicon, vanadium as applicable to grade
- [ ] Tensile and yield strength test results:
  - Meets or exceeds spec minimum (e.g., 50 ksi yield for Grade 50)
- [ ] Elongation percentage meets ASTM requirement
- [ ] Mill test lab accreditation visible

**Dimensional Check:**
- [ ] Shapes match design drawings (e.g., W12x40, C8x11.5)
- [ ] Length within tolerance (typically ±1/4 inch for most shapes)
- [ ] For built-up sections: verify component plates present and dimensioned
- [ ] Bolt holes (if pre-drilled): verify location against approved fabrication drawings

**Fabrication Verification:**
- [ ] Welding present per approved fabrication drawings
- [ ] Weld quality apparent (no excessive spatter, incomplete fusion)
- [ ] Paint system applied per spec (if shop painting required)
- [ ] Connection details (bolts, pins) present as designed

**Non-Conformance Examples:**
- Mill cert missing → material cannot be installed
- Heat number not visible → material cannot be tracked to cert
- Wrong grade shipped (e.g., A36 instead of A992) → strength deficiency
- Cracks observed in welds → structural integrity at risk

---

### Rebar

**On Arrival:**
- [ ] Mill certs present
- [ ] Bundle tags visible with heat number
- [ ] No visible rust scaling (light surface rust is acceptable; heavy scaling is not)
- [ ] Bundle strapping intact

**Mill Certificate Verification:**
- [ ] Heat number matches bundle tag
- [ ] Grade matches spec (typically Grade 60, increasingly Grade 80)
- [ ] Size matches spec (e.g., #4, #5, #6)
- [ ] Chemical analysis provided:
  - Carbon equivalent in acceptable range
  - Sulfur and phosphorus content
- [ ] Tensile and yield strength test results meet ASTM A615/A615M:
  - Yield strength ≥ spec (e.g., 60 ksi for Grade 60)
  - Tensile strength ≥ requirement
  - Elongation % meets requirement
- [ ] Bend test results (if conducted at mill):
  - Rebar bent 180 degrees around mandrel without cracking
  - Mandrel diameter appropriate for bar size
- [ ] Mill cert signature and lab accreditation

**Inspection for Use:**
- [ ] Rebar size and grade match placing drawings
- [ ] Number of bars in bundle matches order
- [ ] No broken/damaged bars (count and note any defects)
- [ ] For epoxy-coated rebar: coating intact, no holidays (exposed base metal)

**Non-Conformance Examples:**
- Mill cert missing → cannot verify grade/strength
- Grade 40 shipped instead of Grade 60 → severe strength deficiency
- Heavy rust scaling → surface quality may affect bond in concrete
- Epoxy coating with holidays → corrosion risk in service

---

### Lumber

**On Arrival:**
- [ ] Grade stamp visible on member edges (must identify lumber grade)
- [ ] No visible warping, cupping, twisting, or severe checking
- [ ] No insect damage or rot
- [ ] Member dimensions match specification

**Grade Stamp Verification:**
- [ ] Species clearly identified (e.g., Douglas Fir, Spruce-Pine-Fir)
- [ ] Grade clearly marked (e.g., #2, #1, Structural, etc.)
- [ ] Grading agency symbol visible (NLGA, SPIB, WCLIB, etc.)
- [ ] Mill name and location
- [ ] Condition of grade stamp (not so faded as to be unreadable)

**Species Confirmation:**
- Spec requirement calls out specific species
- Lumber mill certs verify species (when available)
- Visual inspection confirms expected appearance for species

**Moisture Content:**
- [ ] Lumber for interior use should be ≤ 19% MC (green lumber not acceptable unless construction lumber)
- [ ] For finish carpentry, target ≤ 12% MC
- [ ] Lumber exposed to weather should be treated if required by code
- For critical uses, moisture meter testing can be performed

**Condition Assessment:**
- [ ] No splits or checks extending more than 1 ft per lumber grading rules
- [ ] No knots larger than grade allows
- [ ] No damage from handling (crushed edges, gouges)
- [ ] Straightness adequate (crowned members should be installed crown-up)

**Treatment Verification (if required):**
- [ ] Pressure-treated lumber: mill stamp shows treatment chemical and retention level
- [ ] Fire rating: if rated lumber required, mark clearly visible
- [ ] Fingerprint test not available; rely on mill stamp

**Non-Conformance Examples:**
- Grade stamp missing or illegible → cannot verify grade
- Wrong species shipped → may not meet structural/finish requirements
- Green lumber delivered when kiln-dried required → dimensional stability issue
- Visibly rotted or insect-damaged → reject, do not use

---

### MEP Equipment (Mechanical, Electrical, Plumbing)

**On Arrival:**
- [ ] All pieces/components present (confirm against packing list)
- [ ] Packaging intact, no shipping damage
- [ ] No water/moisture damage (critical for electrical equipment)
- [ ] Equipment accessible for inspection (not sealed in permanent packaging)

**Nameplate Data Verification:**
- [ ] Equipment model number matches PO and spec
- [ ] Model matches approved submittal (check submittal_log)
- [ ] Serial number recorded (for warranty tracking)
- [ ] Voltage/phase/frequency rating correct for site electrical service
- [ ] Cooling capacity (for HVAC) or other performance rating matches design

**Submittal Comparison:**
- [ ] Cross-check with approved submittal from submittal_log
- [ ] Model selected is the submittal-approved version (not a "or equal")
- [ ] Finish/color matches submittal specification
- [ ] Available options match approval (e.g., voltage options, control accessories)
- [ ] Certificate of Conformance (if submittal required) present

**Certifications:**
- [ ] UL listing mark present (for electrical/mechanical equipment)
- [ ] AHRI certification (for HVAC equipment)
- [ ] FM approval (for fire protection equipment)
- [ ] NSF mark (for water-related equipment)
- [ ] CSA mark (Canada)
- Certification numbers match nameplate

**Documentation:**
- [ ] Operating manual/instruction booklet included
- [ ] Warranty documentation with terms and coverage
- [ ] Test/commissioning record (if pre-commissioned)
- [ ] Control/sequence-of-operation documentation

**Installation Requirements:**
- [ ] Manufacturer clearance requirements noted (ventilation, service access)
- [ ] Electrical requirements (dedicated circuit, size, protection)
- [ ] Refrigerant type (for HVAC equipment with replacements)
- [ ] Shipping bolts/blocking present (must be removed before operation)

**Non-Conformance Examples:**
- Equipment shipped for 208V when site is 480V → incorrect equipment
- Wrong cooling capacity (e.g., 2-ton instead of 3-ton) → undersized system
- Missing certification marks → cannot verify code compliance
- Physical damage to unit → potential reliability/safety issue

---

### Finish Materials (Paint, Flooring, Hardware, Millwork)

**Paint:**
- [ ] Paint color matches specification/approved color sample
- [ ] Paint type correct (acrylic, epoxy, polyurethane, etc.)
- [ ] Sheen level correct (flat, eggshell, satin, gloss)
- [ ] Quantity matches coverage estimate for project
- [ ] Batch/lot numbers recorded (for consistency across multiple deliveries)
- [ ] Expiration date not exceeded
- [ ] Product data sheet and SDS present
- [ ] All cans from same lot (to ensure color consistency)

**Flooring:**
- [ ] Flooring type matches spec (laminate, LVT, tile, carpet, etc.)
- [ ] Color/pattern matches approved sample
- [ ] Lot numbers/dye lots recorded (for within-room consistency)
- [ ] Quantity adequate for square footage (account for waste factor)
- [ ] No visible factory defects (manufacturer should provide some overage for defects)
- [ ] Moisture-related materials (wood, carpet): verify acclimation requirements

**Hardware (Door locks, hinges, trim):**
- [ ] Finish matches specification (stainless, bronze, chrome, etc.)
- [ ] Product type matches design (e.g., lever vs knob style)
- [ ] Function correct (keyed, dummy, passage, privacy lever)
- [ ] Quantity per door/application correct
- [ ] Keying matches security design
- [ ] Installation instructions provided

**Millwork:**
- [ ] Dimensions match approved shop drawings
- [ ] Finish matches specification
- [ ] No visible damage to wood/veneer surfaces
- [ ] If prefinished: finish quality meets expectations
- [ ] For cabinet assembly items: all components present, hardware included
- [ ] Installation instructions provided

**Non-Conformance Examples:**
- Paint color off-sample → must be rejected (cannot apply different color)
- Flooring lots don't match → visible color variation in finished floor
- Hardware finish doesn't match → aesthetic and durability issues
- Millwork dimensions don't match drawings → installation problems

---

## Non-Conformance Handling

When material does not meet requirements:

### Step 1: Document the Deficiency
- **What is wrong?** Describe specific deviation from spec or PO
- **How was it discovered?** Which requirement failed verification
- **Reference requirement:** Quote spec section or submittal approval
- **Evidence:** Photographs, cert comparison, dimension check results
- **Severity:** Critical (safety/code), Major (performance/aesthetics), Minor (documentation)

### Step 2: Photograph and Record
- Take clear photos showing:
  - Product identity (label, model number visible)
  - Nature of deficiency (damage, wrong product, missing cert)
  - Scale reference (ruler, measurement)
- Document date/time of discovery
- Record inspector name and signature

### Step 3: Notify Supplier
- Contact material supplier/manufacturer within 24 hours
- Provide documented evidence of non-conformance
- Present options: accept with concession, repair, replace, return
- Get response timeline (48-72 hours typical)
- Do not remove material from site without approval

### Step 4: Determine Disposition Decision
**Three options:**
1. **Accept with concession:** Material acceptable despite deficiency
   - Example: Different color lot acceptable (painted over), minor dent in equipment
   - Requires sign-off from engineer of record or building official (for code items)
   - Document decision and approval
   
2. **Repair/Remedy:** Supplier corrects issue
   - Example: Mill cert missing (resubmit), finish touch-up, re-packaging
   - Establish timeline and who performs repair
   - Reverify after repair
   
3. **Reject/Return:** Material does not meet requirements
   - Example: Wrong grade steel, damaged beyond use, no cert available
   - Initiate return/credit per supplier terms
   - Re-order compliant material from same or alternative supplier
   - Update procurement timeline

### Step 5: Record Disposition
- Update material-tracker with non-conformance entry
- Document decision made, by whom, and on what date
- Attach deficiency photos and approval documentation
- Update material status (accepted/rejected/pending decision)
- If accepted with concession: note condition in installation records

**Example non-conformance log entry:**
```
Material: Structural Steel Beams (W12x40)
Spec Ref: Section 05 12 00
Deficiency: Mill certificate missing from 4 of 8 pieces
Severity: Critical (cannot verify grade/strength)
Discovery Date: 2024-01-15
Corrective Action: Supplier re-submitted mill certs for all pieces on 2024-01-16
Disposition: Accepted (certs now complete)
Approved By: John Davis, Project Manager
Approval Date: 2024-01-16
```

---

## Storage and Protection Requirements by Material Type

Materials must be stored to protect from damage until installation:

### Concrete
- Not applicable (used immediately after delivery)
- Document strength testing schedule (7-day, 28-day cylinders)
- Keep test cylinders in controlled conditions (temperature, humidity)

### Structural Steel
- [ ] Store elevated off ground (on blocking or racks)
- [ ] Protect from weather (cover with tarps, store under roof if possible)
- [ ] Minimize rust formation (inspect monthly, touch up bare spots)
- [ ] Do not expose to salt spray (de-icing salts near stockpile area)
- [ ] Stack safely (segregate by size/shape, use blocking between layers)
- [ ] Keep mill certs in dry, secure location

### Rebar
- [ ] Store on racks, elevated from ground
- [ ] Keep bundle wrapping intact until placement
- [ ] Protect from weather to minimize rusting
- [ ] In coastal/high-chloride areas: consider plastic sheeting protection
- [ ] Do not bend or cut steel before inspection/verification

### Lumber
- [ ] Stack on level ground with ground contact blocked by sleepers
- [ ] Allow air circulation (stickers between layers for large quantities)
- [ ] Protect from direct sun/rain (cover if stored long-term)
- [ ] Do not apply protective finishes before verification
- [ ] Interior lumber: protect from weather

### Paint/Coatings
- [ ] Store in cool, dry location (temperature range per manufacturer specs)
- [ ] Protect from freezing
- [ ] Keep containers sealed until use
- [ ] Store away from ignition sources
- [ ] Maintain SDS sheets in secure location

### Drywall/Gypsum Board
- [ ] Store flat on the floor or on boards elevated 1-2 inches
- [ ] Do not stand on edge
- [ ] Protect from moisture (keep away from exterior doors, water sources)
- [ ] Allow climate acclimation if stored outdoors initially

### MEP Equipment
- [ ] Indoor storage in dry, climate-controlled space
- [ ] Protect from dust, moisture, mechanical damage
- [ ] For equipment with refrigerant: keep upright, protect caps
- [ ] Do not remove shipping braces until ready for installation
- [ ] Store manuals/certs with equipment

### Finish Materials
- [ ] Flooring: flat storage, avoid standing water/moisture
- [ ] Paint: temperature and humidity controlled
- [ ] Hardware: dry storage, original packaging if possible
- [ ] Millwork: similar to lumber (dry, temperature stable)

---

## Delivery Logging Format for Daily Report Integration

When logging a delivery in material-tracker, use this format for daily report inclusion:

### Essential Fields to Record:
- **Material:** (name/type)
- **Spec Section:** (reference)
- **PO Number:** (link to purchase order)
- **Delivery Date:** (actual arrival date)
- **Quantity:** (amount received)
- **Quantity Expected:** (PO quantity, for comparison)
- **Condition:** (acceptable / minor damage / major damage / refused)
- **Certs Present:** (yes / partial / no)
- **Verification Status:** (conforming / non-conforming / conditional / pending)

### Sample Daily Report Entry:
```
RECEIVING LOG - January 15, 2024

Material: Concrete - 4,000 PSI ready-mix
Spec Ref: Section 03 30 00
PO #: PO-2024-1547
Delivery Date: 1/15/2024, 7:00 AM
Quantity Received: 18 cubic yards
Quantity Expected: 18 cubic yards (✓ Match)
Condition: Acceptable - no damage observed
Batch Ticket: #BT-4521 (attached)
Verification: Batch ticket reviewed, meets spec requirements
Certs: Batch ticket present and complete
Acceptance: APPROVED - ready for placement
Received By: J. Martinez, Superintendent
Verified By: M. Patterson, Quality Control

---

Material: Structural Steel W12x40
Spec Ref: Section 05 12 00
PO #: PO-2024-1548
Delivery Date: 1/15/2024, 1:30 PM
Quantity Received: 8 pieces
Quantity Expected: 8 pieces (✓ Match)
Condition: Acceptable - no shipping damage
Mill Certs: 4 pieces have certs attached; 4 pieces missing certs
Verification: PENDING - certs required before acceptance
Certs: Partial (4 of 8)
Acceptance: CONDITIONAL - awaiting mill certs for remaining pieces
Action: Contacted supplier; certs expected 1/17/2024
Received By: J. Martinez, Superintendent
Status: ON HOLD - do not install until all certs received
```

### Integration with Daily Report System:
- Receiving log section pulls from material-tracker Delivery entries
- Flag any items with non-conformance or missing certs
- Include summary: # items received today, # fully accepted, # pending, # rejected
- Note any at-risk deliveries (certs due but not received)

---

## Summary Checklist for Delivery Verification

Use this quick reference when material arrives:

- [ ] **Visual Inspection** — Quantity, packaging condition, product identity, damage assessment
- [ ] **Documentation Review** — Packing slip matches, item descriptions match, certs present
- [ ] **Spec Compliance** — Material properties meet spec requirements, verified by certs/test reports
- [ ] **Material-Specific Requirements** — Refer to appropriate section above for material type
- [ ] **Non-Conformance?** — Document, photograph, notify supplier, determine disposition
- [ ] **Acceptance Decision** — Conforming (accept), non-conforming (reject/return), conditional (accept with conditions)
- [ ] **Record & File** — Update material-tracker, save certs, file receiving report
- [ ] **Next Step** — Clear for installation or escalate to engineer of record

