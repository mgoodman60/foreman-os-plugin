# ASI (Architect's Supplemental Instruction) - Deep Extraction Guide

Extract detailed data from Architect's Supplemental Instructions (ASIs), change directives, and architectural revisions. ASIs modify the contract documents after NTP and trigger cascading changes to submittals, procurement, scheduling, and cost.

---

## Extraction Priority Matrix

| Priority | Data Type | Use Case | Completeness Target |
|----------|-----------|----------|-------------------|
| **CRITICAL** | ASI number and date issued | Document tracking, change order linkage, scheduling | 100% per ASI |
| **CRITICAL** | Affected drawing list (sheet numbers) | Drawing cross-reference, plan updates, coordination | 100% per ASI |
| **CRITICAL** | Description of changes | Scope definition, specification impact, cost estimate | 100% per ASI |
| **CRITICAL** | Scope classification (additive/deductive/clarification) | Change order type, cost impact, contract interpretation | 100% per ASI |
| **HIGH** | Affected spec sections (CSI divisions) | Specification changes, testing/inspection impact | 100% if modified |
| **HIGH** | Revised drawings vs. original (before/after comparison) | Dimensional changes, layout impact, material quantity changes | 100% if drawings included |
| **HIGH** | Issuing architect name and signature | Authority verification, RFI response origin | 100% per ASI |
| **MEDIUM** | Effective date / when changes take effect | Schedule impact, when submittals affected, procurement cutoff | 100% if specified |
| **MEDIUM** | Cost impact (if stated) | Change order baseline, budget impact, approval authority | As provided |
| **MEDIUM** | Schedule impact (if stated) | Critical path impact, delay liability, completion date adjustment | As provided |

---

## ASI COVER SHEET PARSING

### Core Identification Data

**ASI Number and Sequence**:
- Extract ASI number in format: "ASI-001", "ASI No. 1", "Supplemental Instruction #1"
- Establish sequence: Is this 1st, 2nd, 3rd ASI issued on this project?
- Cross-reference with project-config.json to verify numbering consistency

**Date Issued**:
- Date the architect issued the ASI (not date it was received at site)
- Format: Month/Day/Year (e.g., "February 15, 2026")
- Use this date to determine "when change takes effect"

**Issuing Architect**:
- Name, title, firm (e.g., "John Smith, Architect, CMW - The Shape of Ideas")
- Signature or approval stamp
- Contact method for clarifications

**Description/Title**:
- One-line summary of what the ASI addresses
- Examples:
  - "Roof slope modification — revise to 1:8 slope from 1:12"
  - "Door schedule revision — Room 105 to single door instead of double"
  - "MEP coordination — add condensate drain from RTU-2 to Building D drain line"

**EXAMPLE COVER SHEET EXTRACT**:
```
Document Type: Architect's Supplemental Instruction
ASI Number: ASI-002
Project: Morehead One Senior Care
Issued by: CMW - The Shape of Ideas
Architect: Mary Johnson, AIA, Project Architect
Date Issued: February 15, 2026
Effective Date: Immediately upon receipt

Subject: Roof Slope Revision & Gutter Layout Change
Description: Changes roof slope from 1:12 to 1:8 (steeper) due to improved drainage analysis.
Revises gutters, downspouts, and related structural details. No change to eave height.

Affected Drawings:
  • S1.0 General Notes (structural note update)
  • S2.1 Roof Framing Plan (slope dimension change)
  • A4.1 Building Section (section view update)
  • C2.3 Roof Drainage (gutter redesign)
  • M3.2 Roof Penetrations (updated for new slope)

Affected Specifications:
  • Division 05 42 00 - PEMB (roof slope, ridge height)
  • Division 07 61 00 - Roof Accessories (gutters, downspouts)

Change Type: ADDITIVE (steeper slope requires additional structural analysis)
Architect Signature: [signature] Date: 02/15/2026
```

---

## AFFECTED DRAWING SHEET LIST

### Sheet Number Extraction

Extract every drawing sheet called out in the ASI's "Affected Drawings" section:

| Sheet Number | Discipline | Description | Change Type | Supersedes Sheet |
|---|---|---|---|---|
| S1.0 | Structural | General Notes | Modified | S1.0 (dated 01/22) |
| S2.1 | Structural | Roof Framing Plan | Modified | S2.1 (dated 01/22) |
| A4.1 | Architectural | Building Section A-A | Modified | A4.1 (dated 01/22) |
| C2.3 | Civil | Roof Drainage | New drawing | (new; no prior) |
| M3.2 | MEP | Roof Penetrations | Modified | M3.2 (dated 01/22) |

**RED FLAGS**:
- Sheet number referenced that doesn't exist in original drawing set → Ask architect for clarification
- Drawing title changed but sheet number same → Flag for reprint/archive
- Sheet marked "supersedes [old sheet]" → Mark old sheet as obsolete; destroy field copies
- ASI references "see attached revised drawing" but drawing not included → Escalate to get drawing

### Prior Version Identification

For each affected sheet, note:
- **Original version date** (from conformance set or most recent distribution)
- **Original revision letter/number** (e.g., "Revision A dated 01/22/2026")
- **New revision letter/number** (e.g., "Revision B dated 02/15/2026" effective with ASI-002)
- **What changed** (dimensions, materials, details, notes, zones)

**EXAMPLE**:
```
Sheet S2.1 - Roof Framing Plan
  Original: Revision A, dated 01/22/2026
  Revised: Revision B, dated 02/15/2026 (per ASI-002)
  Changes:
    • Roof slope dimension changed from 1:12 to 1:8 (callout on plan)
    • Ridge height increases from 36' to 37'-4"
    • Gutter line elevation revised (new dimension callout)
    • Eave height unchanged at 36'
    • No change to primary framing members (purlins, ridge connections)
```

---

## AFFECTED SPECIFICATION SECTIONS

### CSI Division Mapping

Extract any spec sections modified or clarified by the ASI:

| CSI Division | Section Number | Section Title | Change Description |
|---|---|---|---|
| 05 42 00 | PEMB | Metal Building Assembly | Roof slope revision (1:12 → 1:8); ridge height impact; no strength implications |
| 07 61 00 | Roof Accessories | Gutters, Downspouts, Fascia | Gutter profile resized; downspout routing modified for steeper slope |
| 07 72 00 | Roof Insulation | None specified | No change (R-value, thickness unchanged) |
| — | — | — | — |

**Extraction Steps**:
1. Scan ASI description and drawings for CSI references (e.g., "per Division 05")
2. Identify which specs are modified (tighter requirement, relaxed requirement, new requirement)
3. Note if modification adds cost (material upgrade, testing) or saves cost (material reduction, simplification)
4. Flag if modification requires submittal revision (new product, new testing, certification change)

**EXAMPLE CSI CHANGE**:
```
Division 07 61 00 - Roof Accessories (Gutters & Downspouts)

Original Spec (01/22/2026):
  "Gutters and downspouts per ASTM D3633 (aluminum). Gutter size 6" for 1:12 roof slope.
   Fastening per PEMB manufacturer detail."

ASI-002 Revision (02/15/2026):
  "Gutters and downspouts per ASTM D3633 (aluminum). Gutter size 8" for 1:8 roof slope.
   (Increased sizing due to steeper pitch and higher rainfall velocity.)
   Fastening per PEMB manufacturer detail (no change).
   Downspout routing modified per revised C2.3 (new drainage layout)."

Impact:
  • Gutter size increases (6" → 8") = material cost increase
  • Downspout count/layout changes = installation cost review needed
  • No change to ASTM standard, fastening, or material (aluminum)
  • Submittal impact: Door/frame submittals unaffected; gutter submittals must revise
```

---

## REVISED DRAWING COMPARISON

### Before / After Analysis

For each revised drawing, compare original (from conformance set) to ASI revision (if included):

**Comparison Focus Areas**:
1. **Dimensions** — Any measurements changed? (length, width, height, slope, spacing)
2. **Materials** — Any material type changed? (concrete type, steel grade, finish type)
3. **Layout / Spatial** — Any room/area/zone layout changed? (door location, equipment placement)
4. **Details** — Any connection or assembly detail changed? (bolting pattern, weld length, fastening)
5. **Notes** — Any specification or requirement note added/deleted/modified?
6. **Symbols / Notations** — Any building code references, warnings, or special markings changed?

**EXAMPLE COMPARISON - Roof Framing Plan**:
```
Sheet S2.1 Roof Framing Plan — Revision A to B Comparison

┌──────────────────────────────────────────┬──────────────────────────────────────────┐
│ Original (Revision A, 01/22/2026)        │ Revised (Revision B, 02/15/2026)         │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ Roof slope: 1:12 (5°)                    │ Roof slope: 1:8 (7.1°)                   │
│ Ridge elevation: 36'-0"                  │ Ridge elevation: 37'-4" (16" higher)      │
│ Eave height: 36'-0"                      │ Eave height: 36'-0" (unchanged)          │
│ Note: "Slope per geotechnical drainage"  │ Note: "Slope 1:8 per drainage analysis"   │
│                                          │        (new note added)                   │
│ Primary purlin size: 8" (no change)      │ Primary purlin size: 8" (no change)      │
│ Gutter elevation callout: 35'-8"         │ Gutter elevation callout: 35'-6"         │
│                                          │ (2" drop due to steeper slope)            │
│ No drainage detail callout               │ New detail callout: "See C2.3 for gutter"│
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ IMPACT: Moderate — geometry changes      │ IMPACT: Schedule/submittal review needed  │
│         (slope, ridge height, gutters)   │ Cost impact: Gutter material increase     │
│         NO structural member changes      │ Structural impact: None (framing same)    │
└──────────────────────────────────────────┴──────────────────────────────────────────┘
```

### Dimension Extraction Detail

For each changed dimension, extract:
- **Element name** (e.g., "roof ridge", "gutter elevation", "column height")
- **Original dimension** (e.g., "1:12 slope")
- **New dimension** (e.g., "1:8 slope")
- **Unit and precision** (e.g., "1/12 rise-run ratio" vs "8" rise for 12" run")
- **Source** (e.g., "dimension callout on plan", "note", "section view")

**EXAMPLE DIMENSION LOG**:
```
ASI-002 Dimension Changes (Roof Slope Revision)

Element: Roof Slope
  Original: 1:12 (4.76° angle)
  Revised: 1:8 (7.125° angle)
  Difference: +2.35° (steeper)
  Drawing source: S2.1 Roof Framing Plan, dimension callout

Element: Ridge Elevation
  Original: 36'-0" (above FFE)
  Revised: 37'-4" (above FFE)
  Difference: +16" (higher ridge)
  Drawing source: A4.1 Building Section, dimension line
  Why: Slope change causes ridge to rise; eave height fixed

Element: Gutter Elevation
  Original: 35'-8" (below ridge)
  Revised: 35'-6" (below ridge)
  Difference: -2" (2" lower)
  Drawing source: S2.1 plan dimension, C2.3 detail
  Why: Steeper slope at same eave height drops gutter

Element: Gutter Profile Size
  Original: 6" (nominal)
  Revised: 8" (nominal)
  Difference: +2" width
  Drawing source: C2.3 Roof Drainage detail
  Why: Steeper slope increases water velocity; larger gutter needed
```

---

## SCOPE CHANGE CLASSIFICATION

### Three Types of ASI Changes

**ADDITIVE** (Adds work, adds cost, adds time)
- New materials, new labor, new equipment
- Increases building size, quantity, or complexity
- Example: "Add 4 additional columns to support new roof slope"
- Cost impact: Positive (adds cost)
- Change order type: Price increase
- Schedule impact: May extend duration

**DEDUCTIVE** (Removes work, reduces cost, may save time)
- Deletes materials, deletes labor, simplifies scope
- Reduces quantity or complexity
- Example: "Delete second stair — use single stair instead"
- Cost impact: Negative (saves cost)
- Change order type: Price credit
- Schedule impact: May shorten duration (less work)

**CLARIFICATION ONLY** (No net cost change, no time change)
- Clarifies ambiguity in original documents
- Adds detail or specification but no new materials or labor
- Example: "Roof slope in original Note 5 is 1:12, not 1:8 — confirm 1:12"
- Cost impact: None (or minimal adjustment if clarification corrects error)
- Change order type: No CO needed (unless correcting prior error)
- Schedule impact: None

**CLASSIFICATION PROCESS**:
1. **Read ASI description** — Does it add, remove, or clarify?
2. **Review affected drawings** — Do they show MORE work, LESS work, or SAME work (different detail)?
3. **Review affected specs** — Are requirements INCREASED, DECREASED, or CLARIFIED?
4. **Estimate cost direction** — Will materials/labor cost more, less, or stay the same?
5. **Check original documents** — Does ASI correct an error in the original contract documents?

**EXAMPLE CLASSIFICATIONS**:
```
ASI-001: Add RTU-3 (HVAC unit) to west side of building
  Type: ADDITIVE
  Cost impact: +$45,000 (new equipment, installation labor)
  Spec impact: New spec section (HVAC equipment)
  Submittal impact: New HVAC equipment data sheet required
  Schedule impact: +2 weeks (procurement, installation, testing)

ASI-002: Roof slope revision 1:12 to 1:8 (steeper)
  Type: ADDITIVE (material increase for gutters) / NEUTRAL (structure unchanged)
  Cost impact: +$8,500 (larger gutters, modified drainage)
  Spec impact: Modification to Division 07 61 00 (gutter sizing)
  Submittal impact: Revised gutter submittal required
  Schedule impact: +3 days (revised drawings, re-coordination)

ASI-003: Delete concrete pedestal for exterior equipment — equipment now wall-mounted
  Type: DEDUCTIVE
  Cost impact: -$6,200 (concrete savings, but add wall-mount hardware)
  Net cost: -$3,800 (credit)
  Spec impact: Delete concrete spec ref; add wall-mounting detail
  Submittal impact: Wall-mount hardware submittal required
  Schedule impact: -2 days (less excavation/concrete work)

ASI-004: Confirm mechanical room layout — electrical panel location unchanged from Note 7
  Type: CLARIFICATION ONLY
  Cost impact: None
  Spec impact: None (confirms existing spec)
  Submittal impact: None (electrical panel unchanged)
  Schedule impact: None
  Note: Issued because contractor asked for clarification; no RFI needed
```

---

## IMPACT ASSESSMENT CHECKLIST

### Schedule Impact Analysis

**Questions to answer**:
1. Does this ASI affect a critical path activity? (Check against schedule.json)
2. Does it add duration to any task? (Revised design, new drawings, re-coordination)
3. Does it require submittals before installation can proceed?
4. Does it affect long-lead procurement items?
5. Does it create sequencing delays? (Must complete before next phase)

**SCHEDULE IMPACT MATRIX**:
```
ASI-002: Roof Slope Revision (1:12 → 1:8)

Critical path activity affected?
  ✓ YES — PEMB erection depends on finalized roof details

Duration impact:
  • Architect review of revised drawings: +3 days
  • Revised drawings distribution: +1 day
  • Contractor re-review for re-coordination: +2 days
  • Potential PEMB fabrication delay: +5 days (if Nucor schedule adjusts)
  • PEMB erection start date: May shift from 03/23 to 04/02 (10-day slip?)

Mitigation:
  • Issue revised drawings immediately (compress review time)
  • Concurrent design/fabrication (overlap drawing approval with fab prep)
  • Expedited gutter procurement (pre-order during review)
  • No impact to erection labor if slope geometry only change

Revised schedule: Pending architect review of revised drawings.
Contractor to submit updated schedule reflecting ASI impact.
```

### Cost Impact Analysis

**Questions to answer**:
1. Does this ASI add materials? (Cost increase)
2. Does it reduce materials? (Cost decrease)
3. Does it add labor? (Redesign, re-work, additional testing)
4. Does it create rework of completed work?
5. Does it affect subcontractor pricing? (Force change order on sub)

**COST IMPACT BREAKDOWN**:
```
ASI-002: Roof Slope Revision (1:12 → 1:8)

Material Cost Changes:
  Original gutter size: 6" × [length]
  Revised gutter size: 8" × [length]
  Gutter cost increase: +$3,200 (material)
  Downspout redesign: +$1,200 (new routing, additional fittings)
  Subtotal material: +$4,400

Labor Cost Changes:
  Revised drawing review: +$800 (contractor, architect)
  PEMB design re-check: +$1,200 (Nucor engineer review)
  Installation labor (larger gutter): +$1,500 (more complex installation)
  Subtotal labor: +$3,500

Other Costs:
  No rework required (no completed gutter work yet)
  Testing/inspections: No change (same as original spec)
  Subtotal other: $0

TOTAL COST IMPACT: +$7,900

This is an additive change order to the gutter/drainage trade.
Contractor to submit revised quote for gutter/downspout work.
Budget line item: Roof Accessories (07 61 00) — authorize CO pending gutter quote.
```

### Submittal Impact Analysis

**Questions to answer**:
1. What submittals must be revised due to this ASI?
2. Which submittals are NOT affected? (Avoid unnecessary re-submissions)
3. When must revised submittals be submitted? (New critical dates)
4. Must new submittals be created? (New product, new system)

**SUBMITTAL IMPACT CHECKLIST**:
```
ASI-002: Roof Slope Revision (1:12 → 1:8)

Submittals AFFECTED (require revision):
  ☑ Gutter/Downspout system (SUB-007)
    Status before ASI: "Approved as noted"
    Action required: Revise with new gutter profile (8" vs 6")
                     Revise downspout routing per C2.3
    Revised must-submit-by: 02/25/2026 (expedited, 10 days)
    Blocking work?: YES — gutter procurement starts after approval

  ☑ PEMB Erection (Nucor design, SUB-008)
    Status before ASI: "Under review" for final approval
    Action required: Nucor updates for 1:8 roof slope (minor update)
                     Ridge detail at steeper angle
                     Attachment points unchanged (same columns)
    Revised must-submit-by: 02/20/2026 (expedited, before erection starts)
    Blocking work?: YES — critical path

  ☑ Roof penetration drawings (architect, SUB-009)
    Status before ASI: "Approved"
    Action required: Update for new roof slope angle
                     Verify flashing details still work at steeper slope
    Revised must-submit-by: 02/20/2026 (coordinate with PEMB)
    Blocking work?: YES — if flashing design must change

Submittals NOT AFFECTED (no revision needed):
  ☐ Structural steel (foundation, columns) — unchanged by roof slope ASI
  ☐ Electrical service panel location — unchanged by ASI
  ☐ HVAC equipment (unless RTU mounting height affected by ridge change — verify)
  ☐ Doors, windows, finishes — unchanged by roof slope

New submittals REQUIRED:
  ✓ None (all affected items are revisions to existing submittals)

Timeline summary:
  Original submittal schedule: Gutter approved by 02/01, PEMB by 02/05
  ASI issued: 02/15 (LATE — already past original dates!)
  Impact: CRITICAL — both submittals now in revision/re-approval cycle
  Mitigation: Expedited review window (3-5 days for architect review)
              Concurrent approvals (approve PEMB + gutter together)
```

### Procurement Impact Analysis

**Questions to answer**:
1. What materials are affected by this ASI?
2. Must existing purchase orders be canceled or modified?
3. Are new materials needed that weren't in original scope?
4. What are lead times? Can we recover if procurement delayed?

**PROCUREMENT IMPACT TABLE**:
```
ASI-002: Roof Slope Revision — Procurement Impact

Material Item | Original PO | Status | ASI Action | Revised Lead Time | Cost Change |
---|---|---|---|---|---|
6" Aluminum Gutter | PO-015 | Ordered 02/01 | CANCEL | Return if not shipped | -$3,200 |
Gutter fasteners | PO-015 | Ordered 02/01 | CANCEL | Return/restock | -$400 |
Downspouts (6" dia) | PO-015 | Ordered 02/01 | CANCEL | Return/restock | -$800 |
8" Aluminum Gutter | NEW | Not yet ordered | NEW ORDER | 10-day lead (expedited) | +$4,200 |
Downspout fittings (revised routing) | NEW | Not yet ordered | NEW ORDER | 5-day lead | +$800 |
Gutter-to-PEMB brackets (modified) | PO-016 (partial) | Ordered 02/03 | MODIFY | 3-day expedite | +$300 |

Action items:
  1. Immediately cancel PO-015 for old gutter size (if not yet fabricated)
  2. Contact supplier: Can old PO be reduced/restocked?
  3. Issue new PO for 8" gutter with 10-day expedited lead (deliver by 02/25)
  4. Expedite downspout fittings (new routing, 5-day lead, deliver by 02/20)
  5. Modify PO-016 bracket order to account for steeper slope (attach angles different)
  6. Verify no other long-lead items affected (roof insulation, fasteners, roofing material)

Timeline:
  Original gutter delivery: 02/11 (PO-015, 10-day lead from 02/01 order)
  ASI issued: 02/15 (TOO LATE to preserve original delivery)
  New gutter delivery: 02/25 (expedited 10-day lead from 02/15)
  Installation start: 03/01 (delayed by 18 days from original plan)
  Impact: PEMB dry-in timeline may slip 5-10 days (gutter required before roof panels)

Cost impact: Net +$2,700 (credit old size, order new size, expedite fee)
```

### Inspection / Testing Impact

**Questions to answer**:
1. Are new inspection points created?
2. Are existing hold points deleted or modified?
3. Are new testing requirements added?
4. Do testing frequencies change?

**INSPECTION IMPACT ANALYSIS**:
```
ASI-002: Roof Slope Revision — Inspection Impact

NEW Inspection Points:
  ☑ Gutter slope verification (steeper 1:8 may need additional verification)
    Hold point: Before installing downspouts
    Verification: Slope gauge, elevation checks
    Who: Contractor super + architect (if roof slope tolerance >1/8")
    When: After gutter hung, before downspout connection
    Documentation: Photos, slope gauge reading, sign-off

Modified Existing Hold Points:
  ☑ Roof penetration flashing (modified detail for 1:8 slope)
    Original: Verify flashing meets 1:12 slope detail spec
    Modified: Verify flashing adapts to 1:8 slope, seal integrity maintained
    Who: Same inspector (roofer verification)
    When: Before roof panels installed (critical)

Testing Requirements - No Change:
  • Gutter strength/slope testing already in spec
  • No additional testing triggered by slope change
  • Existing roof assembly testing (water test, etc.) unchanged

Schedule impact: +1 day inspection time (additional gutter slope hold point)
```

---

## CROSS-REFERENCING & INTEGRATION

### Update plans-spatial.json (if spatial changes)

When ASI modifies building geometry or spatial layout:

**Fields to update**:
```json
{
  "asi_log": [
    {
      "asi_number": "ASI-002",
      "date_issued": "2026-02-15",
      "description": "Roof slope revision 1:12 to 1:8",
      "spatial_changes": {
        "affected_areas": ["Entire roof"],
        "dimensional_changes": [
          {
            "element": "roof_slope",
            "original_value": "1:12",
            "revised_value": "1:8",
            "unit": "rise-run ratio"
          },
          {
            "element": "ridge_elevation",
            "original_value": "36'-0\"",
            "revised_value": "37'-4\"",
            "unit": "elevation"
          }
        ],
        "layout_changes": "No building layout changes (geometry only)",
        "affected_zones": []
      },
      "updated_quantities": {
        "gutter_linear_feet": "Original 250 LF, no change (same building perimeter)",
        "gutter_size": "6\" to 8\" nominal width"
      }
    }
  ]
}
```

### Flag affected submittals in submittal-log.json

Mark submittals that must be revised:

```json
{
  "submittal_log": [
    {
      "id": "SUB-007",
      "item": "Gutter and Downspout System",
      "status": "approved_as_noted",
      "asi_revisions_required": [
        {
          "asi_number": "ASI-002",
          "revision_reason": "Gutter profile size increase 6\" to 8\" due to roof slope change",
          "new_must_submit_by_date": "2026-02-25",
          "original_must_submit_by_date": "2026-02-01",
          "critical_path_impact": "blocks_gutter_procurement"
        }
      ]
    }
  ]
}
```

### Update change-order-log.json

Create change order entry for cost tracking:

```json
{
  "change_order_log": [
    {
      "co_number": "CO-003",
      "co_date": "2026-02-15",
      "triggering_document": "ASI-002",
      "description": "Roof slope revision 1:12 to 1:8, gutter upsizing",
      "scope_type": "additive",
      "cost_impact": 7900,
      "schedule_impact_days": 10,
      "affected_trades": ["Roofer/Gutter Contractor"],
      "status": "pending_contractor_quote",
      "notes": "Pending gutter supplier quote; estimated $7,900 additive"
    }
  ]
}
```

### Update morning-brief to flag affected work

Add ASI information to daily alerts:

**Morning Brief ASI Section**:
```
ASI ALERTS — Active Changes in Review

⚠️  ASI-002 (Roof Slope Revision) — Issued 02/15
    Impact: Gutter/downspout revision required
    Submittal: SUB-007 must be resubmitted by 02/25 (expedited, 10-day window)
    Schedule: PEMB erection may slip 5 days if gutter delivery delayed
    Cost: Estimated +$7,900 (pending contractor quote)
    Action: Confirm gutter supplier can meet 02/25 delivery; expedited review scheduled

⚠️  ASI-001 (RTU-3 Addition — West HVAC) — Issued 02/10
    Impact: New HVAC equipment submittal required
    Submittal: SUB-015 HVAC equipment data must be submitted by 02/25
    Schedule: Adds 2 weeks to MEP rough-in phase (04/27 start)
    Cost: +$45,000 equipment; CO-002 issued and approved
    Action: Confirm RTU-3 delivery timeline with Davis & Plomin
```

---

## STORAGE SCHEMA

### ASI Log Structure in project-config.json

Add new `asi_log` array to track all ASIs:

```json
{
  "asi_log": [
    {
      "id": "ASI-001",
      "number": "ASI-001",
      "date_issued": "2026-02-10",
      "date_received": "2026-02-10",
      "issuing_architect": "CMW - The Shape of Ideas",
      "architect_name": "John Smith, AIA",
      "description": "Add RTU-3 (HVAC unit) to west side of building",
      "scope_type": "additive",
      "cost_estimate": 45000,
      "schedule_impact_days": 14,
      "affected_drawings": ["M3.1", "M3.2"],
      "affected_spec_sections": ["23 81 13 - Cooling equipment", "23 82 00 - HVAC terminals"],
      "affected_submittals": ["SUB-015"],
      "affected_change_orders": ["CO-002"],
      "critical_path_impact": true,
      "status": "active",
      "change_order_issued": "CO-002",
      "change_order_approved": true,
      "notes": "CMW requested HVAC expansion; added zone for west infill. Approved 02/12."
    },
    {
      "id": "ASI-002",
      "number": "ASI-002",
      "date_issued": "2026-02-15",
      "date_received": "2026-02-15",
      "issuing_architect": "CMW - The Shape of Ideas",
      "architect_name": "Mary Johnson, AIA",
      "description": "Roof slope revision 1:12 to 1:8 (steeper); gutter/drainage redesign",
      "scope_type": "additive",
      "cost_estimate": 7900,
      "schedule_impact_days": 10,
      "affected_drawings": ["S1.0", "S2.1", "A4.1", "C2.3", "M3.2"],
      "affected_spec_sections": ["05 42 00 - PEMB", "07 61 00 - Gutter/downspouts"],
      "affected_submittals": ["SUB-007", "SUB-008", "SUB-009"],
      "affected_change_orders": ["CO-003"],
      "critical_path_impact": true,
      "status": "active",
      "change_order_issued": "CO-003",
      "change_order_approved": false,
      "notes": "Drainage analysis indicated steeper slope needed. Revised drawings in distribution. Gutter quotes pending."
    }
  ]
}
```

---

## SUMMARY CHECKLIST — ASI EXTRACTION & PROCESSING

**WHEN RECEIVING AN ASI**:

- [ ] **Identification**: ASI number, date issued, architect name captured
- [ ] **Description**: Clear summary of what changed and why
- [ ] **Affected drawings**: All sheet numbers listed and located
- [ ] **Affected specs**: CSI divisions identified
- [ ] **Revised drawings**: Obtained and compared to originals (if included)
- [ ] **Scope type**: Classified as additive, deductive, or clarification
- [ ] **Cost impact**: Estimated or calculated if possible
- [ ] **Schedule impact**: Duration and critical path effects assessed
- [ ] **Submittal revisions**: Identified and scheduled for re-submission
- [ ] **Procurement impact**: Material cancellations/modifications captured
- [ ] **Inspection changes**: New hold points or modified testing requirements documented
- [ ] **Change order**: CO prepared and cost baseline established
- [ ] **Morning brief flag**: Alert generated for project team
- [ ] **Storage**: ASI logged in project-config.json

**AFTER PROCESSING**:

- [ ] Revised drawings distributed to all field copies (mark obsolete drawings)
- [ ] Submittal re-submissions tracked with new must-submit-by dates
- [ ] Change order approved and contractor pricing received
- [ ] Schedule updated to reflect ASI impacts
- [ ] Long-lead procurement expedited or canceled per ASI direction
- [ ] Inspectors and testing agencies notified of new hold points
- [ ] Project team briefed on scope, schedule, and cost impacts

---

## NOTES

- ASIs are formal contract documents; treat with same rigor as original contract drawings and specs
- Late ASIs (issued after related work has begun) create schedule impact and cost overruns — escalate to PM immediately
- Clarification-only ASIs may not require change orders; confirm with owner/architect
- Revisions to ASI (if architect makes error and reissues) must be clearly marked to avoid confusion
- Keep master list of all ASIs in project-config.json for weekly owner reports and project closeout
