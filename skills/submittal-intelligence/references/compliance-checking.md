# Compliance Checking Guide

## Purpose

This guide provides the methodology for line-by-line comparison of submitted product specifications against project requirements. It establishes determination rules for each compliance status, and provides templates for professional review comments suitable for RFI responses and meeting minutes.

## Line-by-Line Comparison Methodology

### Basic Process

1. **Align** the requirement and submitted value in the same units and format
2. **Compare** using objective criteria (not subjective judgment)
3. **Determine** compliance status based on rules in next section
4. **Document** the finding with specific citation and rationale
5. **Draft** review comment if non-compliant or clarification needed

### Example Comparison Table

| Spec Ref | Requirement | Submitted Value | Status | Notes |
|----------|-------------|-----------------|--------|-------|
| 03.03.01 | Concrete strength ≥ 4,000 PSI at 28 days | Test report shows 4,150 PSI at 28 days | Compliant | Exceeds requirement by 150 PSI |
| 03.03.02 | Water-cement ratio ≤ 0.50 | W/C ratio 0.52 provided in mix design | Non-Compliant | Exceeds max W/C; see review comment below |
| 03.03.03 | Air entrainment 4–6% | Not addressed in submittal | Unable to Verify | Request clarification on air entrainment percentage |
| 05.03.01 | Steel Grade A992 minimum | Steel mill cert shows ASTM A36 | Non-Compliant | Spec requires Grade 50 minimum; A36 is Grade 36 |

## Determination Rules

### Rule 1: Exact Match → Compliant

**Applies when**: Submitted value exactly equals the spec requirement

**Example**:
- Spec requires: Stainless steel, Type 304
- Submitted: Type 304 stainless steel
- Status: **Compliant**
- Note: "Meets specification exactly"

### Rule 2: Exceeds Spec → Compliant

**Applies when**: Submitted value is better than, stronger than, or more stringent than spec requirement

**Examples**:
- Spec requires: PSI ≥ 4,000
  Submitted: 4,500 PSI
  Status: **Compliant**
  Note: "Exceeds requirement by 500 PSI; acceptable"

- Spec requires: Fire rating 20 minutes minimum
  Submitted: 60-minute fire rating
  Status: **Compliant**
  Note: "Exceeds fire rating requirement; superior product approved"

- Spec requires: Paint with zero-VOC or low-VOC (≤ 50 g/L)
  Submitted: Zero-VOC per EPA (0 g/L)
  Status: **Compliant**
  Note: "Meets more stringent requirement; approved"

**Important note**: Some specs prohibit "exceeding" in certain areas (e.g., oversizing may affect fit or cost). Review spec language for any restrictions. If spec says "shall be exactly" or "shall not exceed," then "exceeds" is non-compliant.

### Rule 3: Below Spec → Non-Compliant

**Applies when**: Submitted value falls short of spec minimum or exceeds spec maximum

**Examples**:
- Spec requires: Concrete strength ≥ 4,000 PSI at 28 days
  Submitted: 3,850 PSI per test report
  Status: **Non-Compliant**
  Note: "Falls short by 150 PSI; does not meet spec minimum. Contractor must retest concrete from same batch or submit revised design mix."

- Spec requires: Insulation R-value minimum R-15 per inch
  Submitted: R-13 per inch
  Status: **Non-Compliant**
  Note: "Insulation is R-13; spec requires minimum R-15. Submit alternative product or waiver request."

- Spec requires: VOC content maximum 50 g/L
  Submitted: VOC content 75 g/L per data sheet
  Status: **Non-Compliant**
  Note: "Exceeds VOC limit by 25 g/L; does not meet environmental requirements. Submit zero-VOC or low-VOC alternative."

**Documentation requirement**: Always cite the specific deficiency (by how much does it fall short) and what corrective action is needed.

### Rule 4: Different Unit/Format but Equivalent → Compliant

**Applies when**: Submitted value is in different units but converts to equivalent value; or stated differently but means the same

**Examples**:
- Spec requires: R-value minimum R-15 per inch
  Submitted: Thermal resistance = 5.28 m²·K/W per ASTM C518
  Status: **Compliant (with conversion note)**
  Conversion: R-15 per inch = 2.64 m²·K/W; submitted 5.28 exceeds this requirement
  Note: "Insulation value exceeds requirement when converted from metric units; compliant"

- Spec requires: Minimum 4,000 PSI concrete
  Submitted: 28 MPa (megapascals)
  Status: **Compliant (with conversion note)**
  Conversion: 28 MPa = 4,060 PSI
  Note: "Strength meets requirement when converted from metric units; compliant"

- Spec requires: Door frame depth 4½" ± ¼" for 4⅝" wall
  Submitted: Frame accommodates 4.50" nominal wall (metric: 114 mm)
  Status: **Compliant (with unit conversion)**
  Note: "Frame depth matches specification when converted from metric; compliant"

**Important**: Always show conversion math so architect/engineer can verify. Include reference to conversion standard if applicable.

### Rule 5: Spec Requirement Not Addressed → Unable to Verify

**Applies when**: Submittal does not provide information needed to verify compliance; missing data, incomplete documentation

**Examples**:
- Spec requires: Testing per ASTM C39 at 28 days
  Submitted: Submittal does not include test report
  Status: **Unable to Verify**
  Note: "Test report required. Request concrete compression strength test per ASTM C39. Submittal incomplete until test report provided."

- Spec requires: Door hardware prep for 4" center locks
  Submitted: Shop drawing does not show hardware prep locations
  Status: **Unable to Verify**
  Note: "Hardware prep detail missing from shop drawing. Provide detail showing lock prep location and dimensions for 4" center standard."

- Spec requires: VOC content maximum 50 g/L per EPA test
  Submitted: No testing data provided; only product name listed
  Status: **Unable to Verify**
  Note: "VOC documentation required. Provide EPA VOC test report or manufacturer certification of product VOC content."

- Spec requires: Stainless steel type specified
  Submitted: Submittal says "stainless steel" without type designation
  Status: **Unable to Verify**
  Note: "Steel type not specified in submittal. Clarify: Is this Type 304, 316, or other? Specification allows Type 304 or 316."

**Resolution path**: Send RFI or request clarification. Cannot approve without verification.

### Rule 6: Ambiguous or Partial Data → Partially Compliant

**Applies when**: Submittal addresses requirement but with reservations, conditions, or areas of ambiguity

**Examples**:
- Spec requires: Concrete air entrainment 4–6%
  Submitted: Mix design shows "air entrainment per industry standard practice, 4–8%"
  Status: **Partially Compliant**
  Concern: Range is broader than spec (8% exceeds spec maximum)
  Note: "Submittal addresses air entrainment but proposes wider tolerance (4–8%) than spec allows (4–6%). Revise to confirm range will be 4–6% in field. If not feasible, request waiver."

- Spec requires: Paint color matching Pantone 7447C
  Submitted: Paint color "custom blend, to be field-verified at time of painting"
  Status: **Partially Compliant**
  Concern: Color not pre-approved; method vague
  Note: "Color has not been pre-approved. Submit color sample or paint chips matching Pantone 7447C for approval before start of painting. Field color verification is not sufficient for initial approval."

- Spec requires: UL 1581 listing for electrical product
  Submitted: UL label shown on product photo, but no UL listing document provided
  Status: **Partially Compliant**
  Concern: UL listing not documented; date and scope unknown
  Note: "UL listing shown on product photo but listing document not provided. Submit copy of UL listing certificate showing current listing status and scope."

- Spec requires: Dimensional tolerance ± ¼" on door width
  Submitted: Shop drawing shows dimension but tolerance not noted
  Status: **Partially Compliant**
  Concern: No explicit tolerance specified; unclear if frame can accommodate ± ¼"
  Note: "Shop drawing does not specify tolerance. Confirm that submitted door frame can accommodate ± ¼" tolerance as required by spec. Note on shop drawing: 'Frame tolerance ± ¼'."

**Resolution path**: Request clarification or revision to address ambiguity. Escalate if condition is unacceptable.

## Detailed Evaluation Procedures

### Evaluating "Or Equal" Substitutions

When contractor proposes a different product as "or equal":

1. **Extract original requirement** from "or equal" clause:
   ```
   Original: "Doors shall be Model ABC-36, 20-min fire rating, STC ≥ 30"
   Or equal criteria:
     - 20-minute fire rating per NFPA 252
     - STC ≥ 30
     - Solid core hardwood veneer, 36" width
     - Hardware prep for 4" center locks
   ```

2. **Verify each criterion** in submitted alternative:
   - Fire rating: Check test report date, scope, lab credentials
   - STC: Check test report per ASTM E90 and ASTM E413
   - Construction: Check product data for core type, veneer material
   - Hardware prep: Check shop drawing detail

3. **Determine if truly equal**:
   - All criteria met → "Approved as equal product"
   - Some criteria not met → "Non-compliant; does not meet or-equal criteria"
   - Performance exceeds → "Approved as superior product"

4. **Document approval**:
   ```
   APPROVED EQUAL PRODUCT:
   Original spec: [Original Model]
   Submitted alternative: [Proposed Model]
   Basis of acceptance:
   - Fire rating: 20 minutes per NFPA 252 ✓ (test report 2024-01-15, lab ABC)
   - STC: 32 (exceeds minimum 30) ✓
   - Construction: Solid core hardwood veneer ✓
   - Hardware prep: 4" center locks ✓
   Conclusion: Alternative product is approved equal; proceed with procurement
   ```

### Checking Certifications and Test Reports

When spec requires third-party certification or testing:

**Verification checklist**:
- [ ] Test report date is current and within validity period (e.g., concrete within 28 days, paint testing within 2 years)
- [ ] Testing lab is accredited (NRTL, AISL, or equivalent for the test type)
- [ ] Test scope includes the specific property required (e.g., ASTM C39 for compression strength, not just any ASTM C test)
- [ ] Results clearly show acceptance or failure per test standard
- [ ] Report is specific to the submitted product (not generic or different model)
- [ ] Certifications are current (UL listing valid date, not expired)
- [ ] For material certifications (mill certs, safety data sheets), source is authoritative (manufacturer or certified distributor, not reseller)

**Example certification check**:
```
Spec requirement: "UL 1581 listing for electrical components"

Submitted: Copy of product label showing UL mark

Verification:
- [ ] UL listing document provided? NO → Request full UL listing certificate
- [ ] Lab credentials verified? NO → Request listing document from UL database
- [ ] Current listing status confirmed? NO → Verify with UL online listing search
- [ ] Product model matches submittal? UNKNOWN → Need to match exact model in UL list

Status: UNABLE TO VERIFY
Action: Request copy of UL listing certificate (full document, not just label). Provide manufacturer name, product model, and UL file number for verification.
```

### Shop Drawing Dimensional Checks

For shop drawings submitted for door frames, window frames, or other items with dimensional tolerances:

**Dimensional verification checklist**:
- [ ] Overall dimensions marked and match spec (width, height, depth)
- [ ] Tolerances explicitly noted (e.g., ± ¼")
- [ ] Construction details shown (core type, frame depth, mounting, etc.)
- [ ] Hardware locations marked if required by spec
- [ ] Details at scale or with dimensions for small features
- [ ] Material designation clear (type, grade, finish)
- [ ] Shop drawing signed/sealed by draftsman or engineer if required
- [ ] Compatibility with adjacent building systems shown (wall thickness, rough opening, etc.)

**Example shop drawing review**:
```
Door Frame Shop Drawing Review

Item: Metal door frame, 36" width, 80" height, 4½" frame depth

Verification:
✓ Width: 36" nominal, tolerance ± ⅛" noted
✓ Height: 80" nominal, tolerance ± ⅛" noted
✓ Frame depth: 4½" for 4⅝" wall nominal, ± ¼" tolerance noted
✓ Material: Stainless steel Type 304, per spec
✓ Hardware prep: Marked for 4" center pivoting hinge and lock
✓ Scale: 1" = 1', readable

Note: Frame tolerance ± ¼" noted as required by spec
Status: APPROVED FOR FABRICATION

Condition: Frame manufacturer must verify dimensional compatibility with actual wall thickness in field. Coordinate with contractor before fabrication if wall is non-standard.
```

### Evaluating Material Certifications

For material specifications that require mill certificates or certifications:

**Certification verification checklist**:
- [ ] Mill certificate (mill cert) or CoC (certificate of conformance) from authorized source
- [ ] Specific material properties listed (grade, PSI, carbon content, etc.)
- [ ] Testing results shown if required (tensile, yield, hardness, etc.)
- [ ] Material batch or lot number matches delivery documentation
- [ ] Certificate date is current (not historical)
- [ ] Certification authority is recognized (ASTM, API, AWS, etc.)

**Example material cert check**:
```
Spec requirement: "Structural steel Grade A992 minimum, with mill certificate"

Submitted: Mill certificate showing:
- Steel Grade: A992
- Yield strength: 50 ksi (exceeds A992 minimum 50 ksi)
- Tensile strength: 65 ksi (meets A992 minimum 65 ksi)
- Lot number: AB-2024-0456
- Certificate date: 2024-12-10

Verification:
✓ Grade matches specification
✓ Yield and tensile strength meet A992 minimum
✓ Certificate is recent (current year)
✓ Lot number traceable to delivery

Status: COMPLIANT
Action: Cross-reference lot number on fabrication drawings and shipping documents for complete traceability.
```

## Review Comment Templates

Use these templates to draft professional review comments for each compliance status.

### Template 1: Compliant Item (No Issues)

```
[REF-CODE] Requirement: [Requirement Text]
Status: ✓ APPROVED

The submitted [product/material] meets specification requirement [requirement text].

Submittal data confirms [specific fact], which satisfies the specification.

Action: Approved for [procurement/installation].
```

**Real example**:
```
03.03.01 Concrete Strength
Status: ✓ APPROVED

The submitted concrete mix meets the 4,000 PSI minimum compressive strength requirement.

Test report dated 2024-12-28 shows compression strength of 4,150 PSI at 28 days per ASTM C39, which exceeds specification minimum by 150 PSI.

Action: Approved for placement.
```

### Template 2: Compliant but Exceeds Spec

```
[REF-CODE] Requirement: [Requirement Text]
Status: ✓ APPROVED (Exceeds)

The submitted [product/material] exceeds specification requirements.

Specification allows [requirement]. Submittal provides [higher value]. This superior product is acceptable and approved.

Action: Approved for [procurement/installation].
```

**Real example**:
```
08.01.01 Door Fire Rating
Status: ✓ APPROVED (Exceeds)

The submitted door assembly exceeds the specification fire rating requirement.

Specification requires 20-minute fire rating per NFPA 252. Submittal provides 60-minute fire rating (UL 10B, Test #45-67-89, dated 2024-06-15). This superior product is accepted.

Action: Approved for installation. Coordinate with architect if door exceeds fire rating requirements is cost-driven; owner may approve cost reduction for standard 20-minute rated door.
```

### Template 3: Non-Compliant Item

```
[REF-CODE] Requirement: [Requirement Text]
Status: ✗ REJECTED - REVISE AND RESUBMIT

The submitted [product/material] does not meet specification requirements in the following respect:

Specification requires: [Required value]
Submittal provides: [Submitted value]
Deficiency: [Specific shortfall, e.g., "falls short by X", "exceeds maximum by Y"]

[Cite specification section and any relevant standards]

Required action: [Specific corrective action, e.g., "Resubmit concrete from revised design mix", "Submit alternative product meeting all criteria"]

If resubmission is not feasible, submit formal waiver request with engineering justification for owner/architect consideration.
```

**Real example**:
```
03.03.02 Water-Cement Ratio
Status: ✗ REJECTED - REVISE AND RESUBMIT

The submitted concrete mix does not meet specification water-cement ratio limit.

Specification requires: W/C ratio ≤ 0.50 maximum
Submittal provides: W/C ratio = 0.52 (from mix design data)
Deficiency: Exceeds maximum by 0.02; does not meet durability requirement

Per Section 03.03, water-cement ratio controls concrete durability and strength development. Exceeding 0.50 W/C is not acceptable for this exposure.

Required action: Revise concrete mix design to achieve W/C ratio ≤ 0.50. Resubmit mix design and test data showing revised ratio meets requirement. If revised design increases cost, submit cost impact and waiver request if contractor seeks price increase.
```

### Template 4: Unable to Verify

```
[REF-CODE] Requirement: [Requirement Text]
Status: ? UNABLE TO VERIFY - REQUEST INFORMATION

Specification requires [requirement], but required documentation is missing from submittal.

Missing information: [Describe what is needed]

Required action: Submit [specific document or data] to complete submittal. Provide [specific details].

Submittal cannot be approved until this information is received and verified.
```

**Real example**:
```
03.03.01 Concrete Compression Strength Testing
Status: ? UNABLE TO VERIFY - REQUEST INFORMATION

Specification requires concrete compression strength testing per ASTM C39 at 28 days, but test report is not included in submittal.

Missing information: ASTM C39 compression strength test report showing strength at 28 days for concrete batch used on project.

Required action: Submit compression strength test report from testing lab. Provide lab name, test date, concrete batch/lot number, and results in PSI. Test report must be dated within 28 days of concrete placement.

Submittal cannot be approved until test report is received.
```

### Template 5: Partially Compliant with Conditions

```
[REF-CODE] Requirement: [Requirement Text]
Status: ⚠ APPROVED AS NOTED - Conditions Required

The submitted [product/material] substantially meets requirements, with the following conditions or clarifications required:

Concern: [Identify ambiguity or condition]
Condition: [What must be done to resolve]

The item is approved conditioned on [completion of condition by date / approval of detail / clarification of detail].

Action: [Next step, e.g., "Submit revised detail", "Provide written confirmation", "Coordinate in field review"]
```

**Real example**:
```
05.03.01 Steel Verification
Status: ⚠ APPROVED AS NOTED - Conditions Required

The submitted structural steel grade is approved conditioned on material traceability verification.

Concern: Mill certificate shows ASTM A992 Grade 50, which meets specification. However, certificate lot number (AB-2024-0456) must be traced to actual steel delivered to site.

Condition: Steel fabricator must maintain traceability documentation from mill through delivery, and cross-reference lot number on all shop drawings and erection plans.

Action: Before start of fabrication, provide documented procedure for steel traceability and identification on site. Approval granted conditioned on this documentation.
```

## Escalation Criteria

Flag for escalation to architect, engineer, or project manager in these scenarios:

### Escalate to Structural Engineer

- **Material strength falls short** of requirement (concrete PSI, steel grade, weld quality)
- **Load capacity concern** (if proposed product has lower capacity than spec-required)
- **Foundation or lateral load bearing** affected by product substitution
- **Connection or joint detail** submitted that differs materially from specification intent
- **Non-destructive testing** results show defects or concerns (ultrasonic, radiography, magnetic particle)
- **Repair or rework** needed due to non-compliance with structural requirements
- **Safety concern** identified (fall protection, temporary support, staging, etc.)

**Escalation note**:
```
ESCALATION: Structural Engineer Review Required

Reference: [REF-CODE] [Requirement]
Issue: [Description of concern]
Reason: [Why structural engineer input is needed]
Status: HOLD pending structural engineer review

Recommend: [Specific recommendation if any]

Request: Structural engineer review of [specific item] and provide approval or direction for resubmission.
```

### Escalate to Architect/Engineer

- **Aesthetic or finish concern** (color, texture, appearance)
- **Material or product substitution** that materially changes appearance or performance
- **Dimensional tolerance** that affects fit or coordination with adjacent systems
- **Installation or construction method** differs from specification or drawings
- **Schedule impact** from required testing or resubmission
- **Cost impact** significant or scope-changing
- **Code compliance question** regarding ADA, fire, safety, accessibility
- **Waiver request** for non-compliance or deviation from specification

**Escalation note**:
```
ESCALATION: Architect/Engineer Review Required

Reference: [REF-CODE] [Requirement]
Issue: [Description of issue]
Reason for escalation: [Why architect/engineer input is needed]
Status: HOLD pending architect/engineer direction

Recommend: [Specific recommendation if any]

Request: Architect/engineer direction on [specific question/approval].
```

### Escalate to Project Manager

- **Schedule impact** from extended review, resubmission, or corrective action
- **Cost impact** exceeding budget or contingency
- **Supply chain risk** (long lead time, limited availability, rare product)
- **Owner decision required** (waiver request, budget increase, schedule adjustment)
- **Multi-trade coordination** needed to resolve conflict or condition
- **Delay risk** to critical path activities

**Escalation note**:
```
ESCALATION: Project Manager Notification

Reference: [REF-CODE] [Requirement]
Item: [Submittal item]
Issue: [Description of project impact]
Impact: [Schedule / Cost / Coordination / Other impact]
Status: [Current status and next step]

Action required: [What PM needs to do or decide]
Timeline: [When decision/action needed]
```

## Resubmission Tracking

When a submittal is revised and resubmitted, track what changed:

**Resubmission review checklist**:
- [ ] Compare new submittal to previous version item-by-item
- [ ] Flag each requirement: "Same as previous submission", "Revised from previous", or "New information"
- [ ] For revisions, document what changed and whether it addresses previous non-compliance
- [ ] For new information, verify it adequately addresses previous "Unable to Verify" status
- [ ] Identify any new deficiencies introduced in revised submittal
- [ ] Note if previous approval conditions are met in revised submission

**Resubmission tracking table**:
```
| Req-Code | Item | Previous Status | Revision | New Status | Change Summary |
|----------|------|-----------------|----------|------------|-----------------|
| 03.03.01 | Concrete Strength | Compliant | No | Compliant | No change; same test report |
| 03.03.02 | W/C Ratio | Non-Compliant | Yes | Compliant | Mix design revised to 0.48 W/C |
| 03.03.03 | Air Entrainment | Unable to Verify | Yes | Compliant | New data provided: 5.2% air entrainment |
| 05.03.01 | Steel Mill Cert | Compliant | No | Compliant | Same certificate; no revision needed |
```

**Resubmission approval logic**:
- **All previous non-compliances corrected** + **no new deficiencies** → APPROVED
- **Some deficiencies corrected** + **some remain** → REVISE AND RESUBMIT (cite remaining items)
- **New deficiencies introduced** → REVISE AND RESUBMIT (cite new issues + remaining previous issues)
- **Previous conditions met** → APPROVED AS NOTED (reference previous approval conditions)

**Resubmission comment example**:
```
SUBMITTAL RESUBMISSION REVIEW

Item: Concrete Mix Design and Testing (Second Submission)

Summary: Contractor has revised concrete mix design and submitted additional testing data to address previous non-compliance.

Changes from first submission:
- W/C ratio revised from 0.52 to 0.48 (addresses previous non-compliance)
- Additional air entrainment data provided (5.2%, addresses previous "unable to verify")
- Same concrete strength test report used (no new strength testing; first test report acceptable)

Revised status by requirement:
✓ 03.03.01 Concrete Strength: COMPLIANT (unchanged from first submission)
✓ 03.03.02 W/C Ratio: COMPLIANT (revised to meet requirement)
✓ 03.03.03 Air Entrainment: COMPLIANT (now documented at 5.2%)

RECOMMENDATION: APPROVED

All previously identified deficiencies have been corrected. Concrete mix is approved for placement.
```
