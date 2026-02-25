---
name: pay-application
description: >
  Comprehensive pay application (G702/G703) management including schedule of values creation, percentage complete tracking, retainage calculations, lien waiver management, and document generation. Triggers: "pay app", "payment application", "G702", "G703", "create pay app", "billing status", "retainage", "schedule of values", "lien waiver".
version: 1.0.0
---

# Pay Application Skill

## Overview

The **pay-application** skill provides comprehensive management of AIA G702/G703 payment applications for construction projects. It enables project managers and superintendents to create, track, and generate professional payment applications while automatically managing schedule of values, percentage complete calculations, retainage, lien waiver collection, and financial reporting.

## Pay Application Lifecycle

Pay applications progress through a defined workflow to ensure proper documentation and payment authorization:

```
[draft] → [submitted] → [pending payment] → [paid]
```

### Lifecycle Stages

| Stage | Description | Actions Allowed |
|-------|-------------|-----------------|
| **draft** | Pay app created, SOV populated, percentages estimated | Edit SOV, update percentages, submit |
| **submitted** | Pay app submitted to owner/architect for review | View review comments, track pending lien waivers |
| **pending payment** | Pay app approved by architect, awaiting owner payment | Monitor payment status, update when received |
| **paid** | Owner payment received and processed | Mark as paid, apply to subcontractor invoices |

## Schedule of Values (SOV)

The Schedule of Values is the foundation of all pay applications. It establishes the baseline contract breakdown and tracks value completion through the project lifecycle.

### SOV Structure

The SOV can be organized by either **CSI Division** or **Subcontractor**, depending on project requirements:

**Option A: CSI Division Organization**
```json
{
  "organization_method": "csi_division",
  "line_items": [
    {
      "line_item_id": "SOV-001",
      "csi_division": "01",
      "csi_title": "General Requirements",
      "description": "Site mobilization, temporary facilities, project management",
      "original_contract_value": 145000,
      "related_subs": ["General Contractor", "Safety Consultant"]
    },
    {
      "line_item_id": "SOV-002",
      "csi_division": "02",
      "csi_title": "Existing Conditions",
      "description": "Demolition and site preparation",
      "original_contract_value": 85000,
      "related_subs": ["Walker Land Company (Sitework)"]
    }
  ]
}
```

**Option B: Subcontractor Organization**
```json
{
  "organization_method": "subcontractor",
  "line_items": [
    {
      "line_item_id": "SOV-001",
      "subcontractor_name": "Walker Land Company",
      "trade": "Sitework & Excavation",
      "description": "Site demolition, excavation, fill removal, grading",
      "original_contract_value": 220000,
      "csi_divisions": ["02"]
    },
    {
      "line_item_id": "SOV-002",
      "subcontractor_name": "W Principles",
      "trade": "Concrete",
      "description": "Foundation, floor slab, exterior concrete work",
      "original_contract_value": 185000,
      "csi_divisions": ["03"]
    }
  ]
}
```

### SOV Line Item Fields

Each line item in the SOV maintains consistent structure:

```json
{
  "line_item_id": "SOV-001",
  "description": "[CSI Division or Sub Name]",
  "original_contract_value": "[number]",
  "change_orders": [
    { "co_id": "CO-001", "amount": 5000, "status": "approved" },
    { "co_id": "CO-003", "amount": -2000, "status": "approved" }
  ],
  "revised_contract_amount": "[calculated = original + approved COs]",
  "work_completed_previous": "[cumulative from prior pay apps]",
  "work_completed_this_period": "[new work this period only]",
  "materials_stored": "[materials on site but not yet installed]",
  "total_work_completed": "[work_completed_previous + this_period]",
  "total_billable": "[total_work_completed + materials_stored]",
  "percent_complete": "[total_billable / revised_contract_amount * 100]",
  "retainage_rate": "[0.10 flat per W Principles standard, 0.00 at substantial completion]"
}
```

### SOV Locking Rules

- **SOV is locked at creation of first pay application** — structure cannot be altered
- **Line items cannot be added, removed, or reordered** once first pay app is issued
- **Original contract values are immutable** — historical record of baseline scope
- **Change orders modify revised contract amount, not SOV structure** — maintains audit trail
- **If new scope emerges after SOV locked**, it must be handled via Change Order, which updates revised contract amount but not SOV structure

## Retainage Management

Retainage is the percentage of payment withheld to ensure contractor performance and final completion.

### W Principles Retainage Policy

**Flat 10% Retainage**
- W Principles standard: 10% retainage applied uniformly throughout the project
- Applied to both work completed and materials stored
- No reduction at 50% completion — rate stays at 10% until substantial completion
- Released at substantial completion per contract terms

**Note**: This differs from the common 10%/5% tiered approach. W Principles uses a flat 10% for simplicity and stronger financial position through project completion. Override per contract if a specific project has different terms.

### Retainage Release Milestones

1. **At Substantial Completion**: All retainage released
   - User identifies Substantial Completion date in project schedule
   - All remaining retainage becomes immediately due
   - Typically requires Substantial Completion Certificate from Architect

3. **At Final Payment**: Any remaining retainage released
   - Final pay app typically issued 30–60 days after Substantial Completion
   - All lien waivers (conditional final + unconditional final) received
   - Final account reconciliation complete

### Retainage Calculation Examples

**Example 1: Mid-Project (30% Complete, 10% Retainage)**
- Work Completed to Date: $300,000
- Retainage (10%): $30,000
- Amount Due: $270,000

**Example 2: Beyond 50% (65% Complete, 5% Retainage Going Forward)**
- Work at 30%: $300,000 @ 10% = $30,000 retainage
- Work at 35% (65% - 30%): $350,000 @ 5% = $17,500 retainage
- Total Retainage Held: $47,500
- Amount Due (if billing to 65%): $603,000 - $47,500 = $555,500

**Example 3: At Substantial Completion (100% Complete, 0% Retainage)**
- Total Billed to Date: $2,770,000
- All Retainage Released: $0
- Final Payment: Remaining balance + released retainage

## Lien Waiver Management

Lien waivers protect the owner by ensuring subcontractors and suppliers have been paid and waive their right to file liens. Four types are tracked:

### Lien Waiver Types

**1. Conditional Progress Waiver**
- **Issued by**: Subcontractors (in exchange for payment)
- **Condition**: Payment of current invoice
- **Release**: Waives lien rights for work/materials through current pay app period
- **Timing**: Must be received prior to GC receiving payment from owner
- **Example**: Sub signs conditional waiver saying "I waive lien rights for work through Feb 28, 2026, upon receipt of payment"

**2. Unconditional Progress Waiver**
- **Issued by**: Subcontractors
- **Condition**: None — unconditional release
- **Release**: Waives lien rights for work/materials through specified date, regardless of payment status
- **Timing**: Typically required for final payment
- **Less Common**: Sometimes required mid-project to satisfy bonding companies

**3. Conditional Final Waiver**
- **Issued by**: Subcontractors
- **Condition**: Payment of final invoice
- **Release**: Waives all lien rights through final payment
- **Timing**: Required with final pay application
- **Scope**: Covers all work on project (no date limitation)

**4. Unconditional Final Waiver**
- **Issued by**: Subcontractors
- **Condition**: None — unconditional final release
- **Release**: Absolute waiver of all lien rights
- **Timing**: Last item received before issuing final payment
- **Business Logic**: Sub certifies they have been fully paid and have no further claims

### Lien Waiver Tracking Structure

```json
{
  "pay_app_id": "PAY-001",
  "lien_waivers": {
    "conditional_progress": [
      {
        "subcontractor": "W Principles",
        "type": "conditional_progress",
        "period_covered": "2026-02-01 to 2026-02-28",
        "date_received": "2026-02-28",
        "status": "received",
        "document_reference": "LW-001_WPrinciples_Conditional_020226.pdf"
      }
    ],
    "unconditional_progress": [],
    "conditional_final": [],
    "unconditional_final": []
  },
  "lien_waiver_summary": {
    "total_required": 8,
    "conditional_progress_received": 7,
    "conditional_progress_pending": ["Alexander Steel - PEMB Erection"],
    "payment_holdback": "[amount withheld pending waiver receipt]"
  }
}
```

### Lien Waiver Workflow

1. **Create Pay Application**: PAY-001 identifies all active subcontractors and suppliers
2. **System Auto-Lists**: Required lien waivers for current period (conditional progress for all subs)
3. **Track Receipt**: As waivers arrive, mark received with date and document reference
4. **Enforce Rules**:
   - Cannot process GC payment from owner until all current conditional waivers received
   - Can process sub payment once conditional waiver received (GC holds until owner pays)
5. **Final Pay App**: Requires unconditional final waivers from all subs who worked on project
6. **Release Holdbacks**: Once all waivers received, GC can release final retainage

## Sub Pay Application Aggregation

Individual subcontractor pay apps aggregate into the master GC pay application to the owner.

### Sub Pay App Structure

Each sub may submit their own pay app for work performed:

```json
{
  "pay_app_id": "PAY-001",
  "sub_pay_apps": [
    {
      "subcontractor": "W Principles",
      "sub_pay_app_number": "1",
      "work_completed_this_period": 45000,
      "materials_stored": 0,
      "previous_payments": 0,
      "amount_due": 45000,
      "lien_waiver_status": "pending"
    },
    {
      "subcontractor": "Davis & Plomin",
      "sub_pay_app_number": "1",
      "work_completed_this_period": 67200,
      "materials_stored": 8500,
      "previous_payments": 0,
      "amount_due": 75700,
      "lien_waiver_status": "received"
    }
  ],
  "sub_total": 120700,
  "gm_overhead_and_profit": "[percent or fixed amount]",
  "master_pay_app_total": "[calculated]"
}
```

### Aggregation Rules

1. **Sum all sub work completed** to derive total work billable this period
2. **Sum all sub materials stored** to derive total materials billable
3. **Apply GC overhead & profit** at specified percentage (typically 5–10% of sub costs)
4. **Total = Sub Work + Sub Materials + GC Markup**
5. **Retainage applied** to total after GC markup
6. **Master pay app total** is what GC bills owner

### Sub Payment Waterfall

```
Sub Invoice Amount:                    $45,000
Less: Retainage (10%):                -$4,500
GC Payment to Sub:                     $40,500

GC Invoice to Owner (with markup):     $47,250  (45,000 × 1.05)
Less: Retainage (10%):                -$4,725
GC Net Due from Owner:                 $42,525

Difference (GC Margin):                $2,025   (45,000 × 0.05 - 4,725 + 4,500)
```

## G702/G703 Document Structure

The G702/G703 format is the industry standard for construction payment applications.

### AIA G702 — Application and Certificate for Payment

**Section 1: Header Information**
- Project Name, Number, Address
- Contractor Name, Address
- Owner Name, Address
- Architect/Engineer Name, Address
- Application Period (From/To dates)
- Application Number and Date

**Section 2: Schedule of Values Table**
Columns:
1. Line Item Description (CSI Division or Sub)
2. Original Contract Amount
3. Previous Work Completed
4. Work Completed This Period
5. Materials Stored
6. Total Completed & Stored to Date
7. Percent Complete
8. Retainage Rate
9. Retainage Amount
10. Net Amount Due

**Section 3: Summary Calculations**
- Total Work Completed to Date: [sum of all line items]
- Total Materials on Hand: [sum of stored materials]
- Total Work + Materials: [combined total]
- Less: Previous Applications: [sum of prior pay apps]
- Balance to Finish: [Revised Contract Amount - Total to Date]

**Section 4: Retainage Calculation Detail**
- Work Completed to Date: [amount]
- Retainage % (Work): [10% or 5% or 0%]
- Retainage $ (Work): [calculated]
- Materials Stored: [amount]
- Retainage % (Materials): [same rate]
- Retainage $ (Materials): [calculated]
- **Total Retainage This Period**: [sum]
- **Total Retainage Held (Cumulative)**: [historical retainage]

**Section 5: Payment Summary**
- Total Billable Amount (Work + Materials): [sum]
- Less: Retainage: [amount]
- **Amount Now Due**: [billable - retainage]
- Previous Payments: [cumulative]
- **Current Amount Due**: [amount due minus previous retainage released]

**Section 6: Certification and Signature**
- Contractor Certification: "I certify that the above represents work performed and materials stored in accordance with the contract documents."
- Contractor Signature, Date
- Architect/Engineer Certification: "In my opinion, the work has been performed in accordance with the contract documents."
- Architect/Engineer Signature, Date

### AIA G703 — Continuation Sheet

Multi-page detailed breakdown organized by CSI Division or Subcontractor:

**Columns (per line item):**
1. Item Number
2. Description
3. Original Contract Amount
4. Change Order Adjustments
5. Revised Contract Amount
6. Prior Period Work Completed
7. This Period Work Completed
8. Prior Period Materials
9. This Period Materials
10. Total Completed & Stored to Date
11. Percent Complete
12. Retainage Rate & Amount
13. Net Due This Period

**Running Totals**
- After each division/sub section
- Grand totals at end of G703


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
