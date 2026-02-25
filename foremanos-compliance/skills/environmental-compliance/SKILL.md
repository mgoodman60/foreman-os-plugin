---
name: environmental-compliance
description: >
  Environmental compliance management for construction projects. Covers LEED v4.1 construction administration, SWPPP permit compliance and inspections, hazardous materials management (asbestos, lead, mold, contaminated soil), construction waste management and diversion tracking, dust and air quality control, noise ordinance compliance, silica exposure prevention, and environmental incident response. Beyond basic BMP installation (see field-reference/bmp-field-guide.md). Triggers: "environmental", "LEED", "SWPPP", "hazmat", "hazardous materials", "asbestos", "lead paint", "waste management", "dust control", "noise", "environmental compliance", "recycling", "diversion", "VOC", "silica", "EPD", "HPD", "spill", "contaminated soil", "mold", "air quality", "noise variance", "waste diversion", "C&D waste".
version: 1.0.0
---

# Environmental Compliance Skill

## Overview

The **environmental-compliance** skill provides systematic environmental regulatory compliance management for construction superintendents. It covers the full scope of environmental obligations on a construction project — from LEED certification administration through SWPPP permit lifecycle, hazardous materials field procedures, construction waste diversion tracking, dust and air quality monitoring, noise ordinance management, and environmental incident response.

This skill manages the **regulatory and administrative** side of environmental compliance. For BMP installation procedures, specifications, and field maintenance details, refer to `field-reference/references/bmp-field-guide.md`. The two skills work together: the BMP guide tells you how to install and maintain erosion controls; this skill tells you how to administer the permits, track the documentation, and stay compliant with the full range of environmental regulations.

**Key Regulatory Frameworks Covered**:
- LEED v4.1 BD+C (construction-phase credits and prerequisites)
- Clean Water Act / NPDES Construction General Permit (SWPPP)
- NESHAP (National Emission Standards for Hazardous Air Pollutants — asbestos)
- EPA RRP Rule (Renovation, Repair, and Painting — lead paint)
- OSHA Silica Rule (29 CFR 1926.1153 — Table 1 controls)
- CERCLA / EPCRA (spill reporting and hazardous substance thresholds)
- Local municipal noise ordinances
- State and local air quality regulations (PM10/PM2.5)
- RCRA (Resource Conservation and Recovery Act — hazardous waste)

---

## LEED Construction Administration

### LEED v4.1 BD+C — Construction-Phase Credits

LEED certification requires active participation from the construction team. The superintendent's role is critical for several prerequisites and credits during the construction phase. The LEED coordinator manages documentation and submittals, but the superintendent ensures field compliance.

> **Cross-Reference**: For detailed credit-by-credit requirements, documentation checklists, and common pitfalls, see `references/leed-construction-guide.md`.

#### SS Credit: Construction Activity Pollution Prevention

**Requirement**: Erosion and sedimentation control plan conforming to EPA Construction General Permit OR local equivalent.

| Element | Requirement | Super's Role |
|---------|-------------|--------------|
| Erosion control | Prevent soil loss from disturbed areas | Install and maintain BMPs per SWPPP |
| Sedimentation control | Prevent sediment from leaving site | Inspect silt fence, inlet protection, stabilized entrance |
| Dust control | Prevent airborne particulate | Water trucks, chemical stabilizers, wind fencing |
| Waterway protection | No discharge of pollutants to waterways | Maintain 50-ft buffer, inspect outfalls |

**Cross-Reference**: BMP installation and maintenance procedures are in `field-reference/references/bmp-field-guide.md`. This credit requires the BMPs to be installed AND documented per the SWPPP.

**Documentation Required**:
- SWPPP document (on-site copy)
- Weekly inspection logs with photos
- Corrective action records
- BMP maintenance logs

#### MR Credit: Construction & Demolition Waste Management

**Prerequisite (MR Prerequisite)**: Construction waste management plan required for all LEED projects.

**Credit Thresholds**:

| Diversion Rate | Points |
|----------------|--------|
| 50% (by weight or volume) | 1 point |
| 75% (by weight or volume) | 2 points |

**Waste Management Plan Requirements**:
1. **Waste streams identified**: Concrete/masonry, wood, metals, drywall, cardboard, plastic, mixed C&D
2. **Diversion strategies**: On-site segregation vs. commingled recycling facility
3. **Hauler certifications**: Recycling facility documentation, diversion rate verification
4. **Tracking method**: Monthly weight tickets from haulers, diversion rate calculation
5. **Reporting**: Monthly diversion reports, cumulative project total

**Diversion Rate Calculation**:
```
Diversion Rate = (Total Recycled Weight) / (Total Recycled + Total Landfilled) x 100%

Example:
  Recycled: 85 tons (concrete 40T, metals 20T, wood 15T, cardboard 10T)
  Landfilled: 25 tons (mixed debris)
  Diversion Rate = 85 / (85 + 25) x 100% = 77.3% (qualifies for 2 points)
```

**Superintendent Responsibilities**:
- Enforce segregation on site (labeled dumpsters/bins)
- Verify hauler certifications
- Collect and file weight tickets
- Calculate monthly diversion rate
- Report to LEED coordinator

#### EQ Credit: Construction Indoor Air Quality Management

**Requirement**: SMACNA IAQ Guidelines for Occupied Buildings Under Construction (ANSI/SMACNA 008-2008) during construction.

**Key Field Requirements**:

| Element | Requirement | Implementation |
|---------|-------------|----------------|
| HVAC protection | Seal duct openings during construction | Tape, plastic caps on all open duct ends |
| Material storage | Protect absorptive materials from moisture | Store drywall, insulation, ceiling tile off ground, covered |
| Housekeeping | Regular cleanup of dust and debris | Daily sweeping, HEPA vacuum for fine dust |
| Pathway protection | Protect permanent finishes during construction | Floor protection (ram board, plastic), wall corner guards |
| Air filtration | Filter return air during construction | MERV-8 minimum at returns during construction; replace with MERV-13 before occupancy |
| Moisture control | Prevent mold growth on building materials | Dry-in building ASAP; dehumidify if needed |

**HVAC Protection Protocol**:
1. Before ductwork installation: seal all openings with plastic caps or tape
2. During construction: keep return air grilles covered
3. Use temporary filtration (MERV-8 minimum) at all return openings
4. Before occupancy: replace all filters with design-specified MERV rating
5. Document with photos at each stage

**Construction IAQ Testing (Option 2)**:
- Conduct air quality testing after construction, before occupancy
- Test for: formaldehyde, TVOC, PM10, carbon monoxide, 4-PCH (for carpet)
- Testing must meet LEED thresholds (formaldehyde < 27 ppb, TVOC < 500 ug/m3)
- Flush-out alternative: 14,000 CF of outdoor air per SF of floor area

#### Low-Emitting Materials Tracking

**LEED EQ Credit: Low-Emitting Materials** requires tracking VOC content of installed products.

| Product Category | VOC Limit | Standard |
|------------------|-----------|----------|
| Interior paints & coatings (flat) | 50 g/L | GS-11 |
| Interior paints & coatings (non-flat) | 150 g/L | GS-11 |
| Anti-corrosive coatings | 250 g/L | GS-11 |
| Clear wood finishes (varnish) | 350 g/L | SCAQMD Rule 1113 |
| Adhesives (wood flooring) | 100 g/L | SCAQMD Rule 1168 |
| Sealants (non-membrane) | 250 g/L | SCAQMD Rule 1168 |
| Carpet adhesive | 50 g/L | SCAQMD Rule 1168 |
| Composite wood | No added urea-formaldehyde | CARB ATCM |
| Flooring (resilient, tile, carpet) | FloorScore or GreenLabel Plus certified | — |

**Tracking Process**:
1. Collect product data sheets (PDS) and safety data sheets (SDS) for all interior products
2. Verify VOC content against LEED limits
3. Reject non-compliant products BEFORE installation
4. Maintain product tracking log with: product name, manufacturer, VOC content, area installed, date
5. File documentation for LEED submittal

#### MR Credit: Sustainable Purchasing — EPDs and HPDs

**EPDs (Environmental Product Declarations)**:
- Third-party verified lifecycle assessment of product environmental impact
- Products with EPDs earn credit toward LEED MR Credit
- Types: Industry-wide EPD (generic), Product-specific EPD (verified by third party)
- Priority: Product-specific EPD with third-party verification = most credit value

**HPDs (Health Product Declarations)**:
- Disclosure of product ingredients and health hazards
- Products with HPDs contribute to LEED Credit: Building Product Disclosure
- Superintendent should request HPDs from manufacturers at submittal stage

**Superintendent Action Items**:
- Flag submittal packages that include EPDs/HPDs (coordinate with LEED coordinator)
- Verify EPD/HPD documentation is filed with product data
- Track which products have EPDs/HPDs in material log

#### LEED Documentation Summary

| Document | Frequency | Responsible | Filed With |
|----------|-----------|-------------|------------|
| SWPPP inspection logs | Weekly + after rain events | Superintendent | Environmental file + LEED coordinator |
| Waste hauling weight tickets | Per haul (monthly summary) | Superintendent | Environmental file + LEED coordinator |
| Waste diversion rate report | Monthly | Superintendent | LEED coordinator |
| IAQ management photos | Per phase (duct seal, storage, filters) | Superintendent | LEED coordinator |
| Product VOC tracking log | Per product installation | Superintendent | LEED coordinator |
| EPD/HPD documentation | Per product submittal | PM/Submittal coordinator | LEED coordinator |
| Construction IAQ test results | Pre-occupancy | Testing contractor | LEED coordinator |
| LEED photo documentation | Weekly minimum | Superintendent | LEED coordinator |

---

## SWPPP Administration

### Permit Lifecycle

The SWPPP (Stormwater Pollution Prevention Plan) is required under the Clean Water Act for construction sites disturbing 1 acre or more. The NPDES Construction General Permit (CGP) governs compliance.

**Permit Cycle**:
```
NOI Filed → Permit Issued → Construction Begins → Compliance Monitoring → Construction Complete → Site Stabilized → NOT Filed
  │              │                    │                      │                        │                  │              │
  │              │                    │                      │                        │                  │              └─ Record retention
  │              │                    │                      │                        │                  └─ Final stabilization
  │              │                    │                      │                        └─ Punch-out BMPs
  │              │                    │                      └─ Inspections, corrective actions, reporting
  │              │                    └─ Install BMPs per SWPPP plan
  │              └─ Post permit on-site (NOI receipt, SWPPP available for review)
  └─ Submit 14+ days before land disturbance begins
```

**Key Terminology**:
- **NOI**: Notice of Intent — filed with EPA/state before construction begins
- **NOT**: Notice of Termination — filed after final stabilization achieved
- **CGP**: Construction General Permit — the NPDES permit for construction stormwater
- **Final Stabilization**: 70% perennial vegetative cover OR permanent cover (pavement, buildings)

### SWPPP Document Requirements

The SWPPP must contain:

1. **Site Description**:
   - Project location, size, and nature of construction
   - Existing site conditions and receiving waters
   - Sequence of major construction activities

2. **Site Map**:
   - Property boundaries and disturbed area limits
   - Drainage patterns and discharge points
   - BMP locations by construction phase
   - Receiving waters and buffer zones
   - Stockpile locations
   - Construction entrance locations

3. **BMPs by Phase**:
   - Phase 1 (Site Prep/Grading): Perimeter silt fence, stabilized construction entrance, inlet protection, temporary seeding
   - Phase 2 (Utilities/Foundation): Dewatering controls, concrete washout, material storage BMPs
   - Phase 3 (Vertical Construction): Dust control, material staging, waste containment
   - Phase 4 (Final Grading/Stabilization): Permanent seeding, sod, mulch, final inlet protection removal

4. **Inspection Schedule and Procedures**
5. **Maintenance Procedures for Each BMP**
6. **Responsible Parties** (SWPPP administrator, inspectors, emergency contacts)
7. **Spill Prevention and Response Plan**
8. **Pollution Prevention Measures** (concrete washout, chemical storage, equipment fueling)

### Inspection Requirements

**Standard Inspection Frequency**:

| Condition | Frequency | Inspector |
|-----------|-----------|-----------|
| Routine | Every 7 calendar days | Qualified inspector |
| Post-storm | Within 24 hours of 0.25" rainfall event | Qualified inspector |
| Active earth disturbance near waterways | Every 3 calendar days | Qualified inspector |
| After BMP installation or modification | Within 24 hours | Qualified inspector |

**Inspection Checklist Items**:
- [ ] All BMPs in place and functioning
- [ ] No sediment discharge beyond site boundary
- [ ] Stabilized construction entrance functional (no track-out on public road)
- [ ] Silt fence intact, no overtopping, sediment < 1/3 height
- [ ] Inlet protection in place and functional
- [ ] Concrete washout area contained, not overflowing
- [ ] Chemical/fuel storage secondary containment intact
- [ ] Stockpiles stabilized (seeded, covered, or silt fence perimeter)
- [ ] Dewatering discharge clear (no visible turbidity)
- [ ] No visible sheen, discoloration, or odor in discharge
- [ ] Outfall inspection — no sediment plume in receiving water

### Inspector Qualifications

The SWPPP inspector must be a **qualified person** who:
- Has knowledge of NPDES CGP requirements
- Can identify BMP deficiencies and required corrective actions
- Is familiar with the site-specific SWPPP
- Has authority to modify BMPs as conditions change
- Many states require specific certification (e.g., CPESC, CESSWI, QCI)

### Corrective Action Process

```
Deficiency Identified → Document (photo + description) → Initiate Repair
        │                                                        │
        │                                          ┌─────────────┴─────────────┐
        │                                          │                           │
        │                                    Within 24 hours              > 24 hours
        │                                    (standard)                   (complex repair)
        │                                          │                           │
        │                                    Repair complete              Document timeline
        │                                          │                      and justification
        │                                          │                           │
        └──────────────── Re-Inspect ──────────────┴───────────────────────────┘
                              │
                        Document repair
                        in SWPPP log
```

**Corrective Action Requirements**:
1. **Identify**: Note deficiency during inspection (exact location, description, severity)
2. **Document**: Photo with date stamp, written description, severity rating
3. **Repair**: Initiate repair within 24 hours of identification (before next rain event if possible)
4. **Re-Inspect**: Verify repair effectiveness within 24 hours of completion
5. **Log**: Record corrective action in SWPPP inspection log with dates and photos

### Record Retention

- **Minimum 3 years** after NOT (Notice of Termination) is filed
- Retain all inspection reports, corrective action logs, photos, weight tickets
- Some jurisdictions require longer retention (check local requirements)
- Digital records acceptable if properly backed up and accessible

### Common SWPPP Violations and Penalties

| Violation | EPA Penalty Range | Notes |
|-----------|-------------------|-------|
| No SWPPP for qualifying site | $5,000 - $50,000+ per day | Criminal penalties possible |
| Failure to install BMPs | $5,000 - $37,500 per day | Per violation |
| Failure to inspect per schedule | $5,000 - $37,500 per day | Each missed inspection |
| Sediment discharge to waterway | $10,000 - $50,000+ per day | Plus cleanup costs |
| No NOI filed | $5,000 - $37,500 per day | Must file before land disturbance |
| Inadequate record keeping | $5,000 - $25,000 per day | Missing logs, photos |
| Failure to maintain BMPs | $5,000 - $37,500 per day | Silt fence down, inlet protection missing |

**State penalties may be higher**. Some states have independent enforcement with additional fines. Many violations are discovered during state or EPA inspections triggered by citizen complaints or aerial observation.

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
