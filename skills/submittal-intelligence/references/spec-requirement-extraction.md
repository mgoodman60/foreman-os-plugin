# Spec Requirement Extraction Guide

## Purpose

This guide explains how to extract testable, verifiable requirements from a CSI (Construction Specifications Institute) spec section for submittal compliance checking. A good requirement extraction identifies measurable criteria that can be directly compared against submitted product data.

## Categories of Requirements

Requirements in construction specifications typically fall into these categories. Extract requirements separately for each category and assign testable acceptance criteria.

### 1. Material Properties

**Definition**: Physical and chemical properties of materials that define their composition, grade, quality, or performance class.

**Common CSI sections**: Division 03 (Concrete), 04 (Masonry), 05 (Metals), 07 (Thermal & Moisture), 09 (Finishes)

**Examples of material property requirements**:
- Concrete strength: "Concrete shall be 4,000 PSI at 28 days"
- Steel grade: "Structural steel shall be ASTM A992 Grade 50 or A36"
- Insulation R-value: "Rigid foam insulation shall have minimum R-value of R-15 per inch of thickness"
- Paint finish: "Interior paint shall be zero-VOC latex, eggshell finish"
- Flooring: "Carpet shall be solution-dyed nylon, 42 oz face weight, low-pile construction"
- Wood species: "Exterior doors shall be solid core, hardwood veneer, or equivalent"

**Extraction format**:
```
[REQ-CODE] Material Property: [Property Name]
  Spec requirement: [Extract exact requirement from spec]
  Acceptance criteria: [Measured value] meets [requirement]
  Verification method: Manufacturer data sheet, material certification, lab test report
  Example: Concrete strength ≥ 4,000 PSI per ASTM C39 at 28 days
```

### 2. Dimensional Requirements

**Definition**: Size, shape, or spacing requirements that affect fit, function, or appearance.

**Common CSI sections**: Division 08 (Doors and Frames), 09 (Finishes - tile layouts, trim sizing), Shop Drawings

**Examples of dimensional requirements**:
- Door width: "Doors shall be 36" nominal width, 80" nominal height"
- Frame depth: "Door frame shall accommodate 4½" wall thickness nominal ± ¼" tolerance"
- Sill slope: "Exterior sill shall slope minimum ¼" per foot for drainage"
- Tile alignment: "Tile layout shall be symmetric, with cut tiles minimum ½" width"
- Beam spacing: "Roof beams shall be spaced 16" on center maximum"

**Extraction format**:
```
[REQ-CODE] Dimension: [Dimension Name]
  Spec requirement: [Extract exact requirement]
  Tolerance: ± [amount] or [range]
  Verification method: Shop drawing measurement, field verification, manufacturer data
  Example: Door width 36" nominal, ± ¼" tolerance, verified on shop drawing
```

**Note on tolerances**: Always extract tolerance information. If tolerance is not stated, note "tolerance not specified" and clarify with specifier.

### 3. Performance Requirements

**Definition**: Ratings, capacities, or functional characteristics that the product must meet in use.

**Common CSI sections**: All divisions - fire ratings, sound transmission class, load capacity, thermal properties, etc.

**Examples of performance requirements**:
- Fire rating: "Doors shall have 20-minute fire rating per NFPA 252"
- Sound dampening: "Ceiling tiles shall have NRC (Noise Reduction Coefficient) of 0.85 minimum"
- Load capacity: "Shelf shall support 150 lbs per linear foot"
- Thermal: "Window assembly shall have U-value of 0.32 maximum"
- Light transmission: "Window glazing shall have minimum visible transmittance of 67%"
- Impact resistance: "Impact rating: ASTM F2812 Level 3 or equivalent"

**Extraction format**:
```
[REQ-CODE] Performance: [Performance Name]
  Spec requirement: [Extract exact requirement]
  Rating/capacity/value: [required value] per [standard]
  Verification method: Manufacturer rating, third-party test report, lab certification
  Example: 20-minute fire rating per NFPA 252 or UL 10B; verify test report date and scope
```

### 4. Testing & Certification Requirements

**Definition**: Third-party testing, lab analysis, or industry certifications required to verify the material or product.

**Common CSI sections**: All divisions typically require specific test standards

**Examples of testing requirements**:
- Concrete testing: "Testing per ASTM C31 (field sampling) and ASTM C39 (compression strength)"
- Welds: "All welded connections shall be tested per AWS D1.1; provide inspection report"
- Finishes: "Paint shall be tested per ASTM D3359 (adhesion) and ASTM D3787 (drapeability)"
- Insulation: "Thermal properties verified per ASTM C518 (thermal conductivity)"
- Masonry: "Masonry units shall be tested per ASTM C270 (mortar strength)"
- Products: "Product shall carry UL 1581 listing for electrical products"

**Extraction format**:
```
[REQ-CODE] Testing/Certification: [Test or Certification Name]
  Spec requirement: [Extract exact requirement]
  Test standard(s): [ASTM / NFPA / UL / other standard]
  What is tested: [Parameter that is tested]
  Acceptance criteria: [Pass/fail criteria or required value]
  Verification method: Test report with valid date, scope, and lab credentials
  Example: Compression strength ≥ 4,000 PSI per ASTM C39 at 28 days; test report must be dated within 28 days of concrete pour
```

### 5. Environmental & Safety Requirements

**Definition**: VOC limits, chemical composition, sustainability certifications, and compliance with environmental or safety regulations.

**Common CSI sections**: Division 09 (Finishes, especially paint and adhesives), 07 (Sealants), 03 (Concrete admixtures)

**Examples of environmental requirements**:
- VOC limits: "Acrylic latex paint shall contain zero VOC (0 g/L) per EPA standards"
- Lead-free: "All copper tube and fittings shall be lead-free per NSF/ANSI 61"
- Phthalate-free: "Vinyl flooring shall not contain phthalates (DEHP, DBP, or BBP)"
- Sustainability: "Flooring shall be FSC-certified or equivalent for renewable forestry sources"
- RoHS compliance: "All electrical components shall be RoHS compliant (Directive 2011/65/EU)"
- Formaldehyde: "Plywood and particleboard shall be CARB Phase 2 compliant for formaldehyde emissions"

**Extraction format**:
```
[REQ-CODE] Environmental/Safety: [Requirement Name]
  Spec requirement: [Extract exact requirement]
  Regulated substance/standard: [VOC / lead / phthalates / formaldehyde / other]
  Limit or requirement: [Numeric limit or compliance statement]
  Verification method: Manufacturer certification, third-party lab report, safety data sheet
  Example: Zero-VOC acrylic latex per EPA standards; verify against SCAQMD Rule 1113 or equivalent state VOC limits
```

## Requirement Structure Template

For each extracted requirement, structure it as a checklist item with these fields:

```
Reference Code: [Unique ID within spec section, e.g., "03.03.01"]
Requirement Category: [Material / Dimension / Performance / Testing / Environmental]
Requirement Text: [Exact extract from spec, or paraphrase if clearer]
Measurable Criterion: [The specific value, range, or certification needed]
Acceptance Criteria: [How to verify: equals, exceeds, within range, has certification]
Spec Citation: [Exact section/paragraph where requirement appears]
CSI Division: [Division code, e.g., "Division 03 - Concrete"]
Submittal Required: [Yes / No]
Notes: [Any ambiguities, industry standards, or special conditions]
```

**Example**:
```
Reference Code: 03.03.01
Requirement Category: Material Property
Requirement Text: Concrete shall be 4,000 PSI minimum compressive strength at 28 days
Measurable Criterion: 4,000 PSI compression at 28 days
Acceptance Criteria: Lab test report shows ≥ 4,000 PSI per ASTM C39
Spec Citation: Section 03.03 - Structural Concrete, Paragraph 3.1
CSI Division: Division 03 - Concrete
Submittal Required: Yes
Notes: Contractor must submit concrete test report within 28 days of pour; accepts standard commercial concrete suppliers
```

## Common CSI Divisions and Typical Key Requirements

### Division 03 - Concrete
- **Material properties**: Strength (PSI), water-cement ratio, air entrainment, slump, aggregate size
- **Testing**: Concrete test cylinders per ASTM C31/C39, cube tests, abrasion tests
- **Performance**: Finish quality (broom, trowel), flatness (F-numbers), crack control
- **Environmental**: Air-entrainment for freeze-thaw resistance, low-alkali cement for reactive aggregates

### Division 04 - Masonry
- **Material properties**: Brick/block grade, compressive strength, water absorption, color, finish
- **Testing**: Unit strength per ASTM C67, mortar strength per ASTM C270, prism tests
- **Performance**: Bond pattern, joint finish, weathering resistance
- **Dimensional**: Unit size tolerances, joint width (typically ⅜" nominal)

### Division 05 - Metals
- **Material properties**: Steel grade (A36, A992, etc.), carbon content, weld class
- **Testing**: Mill certs, tension tests per ASTM A370, weld inspection per AWS D1.1, NDT (ultrasonic, X-ray)
- **Performance**: Load capacity, deflection limits, corrosion protection (galvanize, paint, stainless)
- **Dimensional**: Beam sizes, bolt spacing, connection plate dimensions

### Division 07 - Thermal & Moisture Protection
- **Material properties**: Insulation R-value, vapor permeability, membrane type (TPO, EPDM, PVC)
- **Testing**: Thermal properties per ASTM C518, flame spread per ASTM E84, water penetration tests
- **Performance**: Fire rating, impact resistance, wind uplift resistance
- **Environmental**: VOC emissions (for spray foam), ozone depletion potential

### Division 08 - Openings (Doors, Windows, Frames)
- **Material properties**: Door core type (hollow, solid, metal), frame material, glazing type
- **Testing**: Fire rating per NFPA 252, air leakage per ASTM E779, water penetration per ASTM E331
- **Performance**: Acoustic rating (STC), thermal rating (U-value for windows), load capacity (door closers)
- **Dimensional**: Width/height nominal and tolerance, frame depth for wall thickness

### Division 09 - Finishes
- **Material properties**: Paint type (latex, enamel), sheen (flat, eggshell, satin), carpet fiber type
- **Testing**: Paint adhesion per ASTM D3359, VOC per EPA/SCAQMD, colorimeter match
- **Performance**: Scuff resistance, stain resistance, cleanability
- **Environmental**: Zero-VOC or low-VOC paints, formaldehyde-free flooring underlayment, phthalate-free vinyl

## Handling "Or Equal" and "Approved Equal" Clauses

Specs often use "or equal" to allow substitutions. Extract the original requirement as specified, then note the substitution process:

```
Original Requirement: Door shall be Model XYZ from Manufacturer ABC
Or Equal Clause: Or approved equal meeting following criteria:
  - Wood core construction, hardwood veneer
  - 20-minute fire rating per NFPA 252
  - Sound transmission class (STC) ≥ 30
  - Hardware prep for 4" center locks

Extraction approach:
  - Create separate line items for each criteria in "or equal" clause
  - For "approved equal", require:
    a) Detailed submittal showing each criterion met
    b) Architect/engineer written approval before installation
    c) Cost comparison (if cost was selection factor)
    d) Third-party testing reports (for fire rating, STC, etc.)
  - Note: "Approved equal" gives specifier authority; contractor must obtain approval, not assume equivalence
```

## Prescriptive vs. Performance Specifications

Understand the difference when extracting requirements:

**Prescriptive Specification**: Specifies the exact product, material, brand, model
- Example: "Doors shall be solid core hardwood veneer, Model SDC-36 or approved equal"
- Extraction: Specify exact model, and if "or equal" used, extract approval process

**Performance Specification**: Specifies results or characteristics to be achieved
- Example: "Doors shall achieve 20-minute fire rating and STC ≥ 30 with 36" width"
- Extraction: Extract each performance criterion as separate requirement; allow product flexibility

**Best practice**: For performance specs, extract each performance criterion separately and clearly separate them from any product examples the spec may provide.

## Ambiguous or Vague Requirements

Some specs contain unclear or subjective language. Flag these during extraction:

```
Vague requirement: "Finish shall be high quality with no visible defects"
Issues:
  - "High quality" is subjective
  - "Visible" depends on viewing distance and light
  - "Defects" not defined

Clarification needed:
  - Reference ASTM standard for finish (e.g., ASTM E1679 for paint)
  - Define viewing distance (e.g., "no visible defects at 12 inches")
  - List accepted defect types and size limits per standard
  - Request specifier clarification before proceeding with submittal review
```

## Extraction Checklist

Before finalizing extracted requirements:

- [ ] All requirements are testable/measurable (not subjective)
- [ ] Tolerance ranges are specified (or noted as "not specified")
- [ ] Test standards are cited (ASTM, UL, NFPA, etc.)
- [ ] Acceptance criteria are clear (equals, exceeds, range, certification)
- [ ] Ambiguous language flagged and clarified with specifier
- [ ] "Or equal" and approval processes documented
- [ ] Performance criteria separated from example products
- [ ] Environmental and safety requirements included
- [ ] Reference codes are unique and logical within spec section
- [ ] Extraction ready for comparison against submitted product data
