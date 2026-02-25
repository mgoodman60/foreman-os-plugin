# Project Documents - Deep Extraction Guide

Extract actionable data from contracts, sub lists, RFIs, and submittals.

## Subcontractor List

For each sub:
- **Company name**: Legal name
- **Trade**: e.g., "Concrete", "PEMB Erection", "Electrical"
- **Scope**: Detailed description
- **Foreman**: Name and cell phone
- **Email**: Primary contact
- **Contract value**: $__ (if visible)
- **Start/finish dates**: Scheduled dates

**Example**:
```
Alexander Construction
  Trade: PEMB Erection
  Scope: Erect Nucor PEMB structure per contract drawings
  Foreman: John Smith, 859-555-1234
  Email: jsmith@alexanderconstruction.com
  Value: $85,000
  Dates: 03/23/26 - 04/20/26
```

## RFI Log

For each RFI:
- **Number**: Sequential (RFI-001, RFI-002)
- **Date submitted**
- **Subject**: Brief description
- **Drawing/spec ref**: Sheet or section number
- **Status**: Open, answered, closed
- **Blocking work?**: Critical flag if work cannot proceed

**Example**:
```
RFI-003
  Date: 02/10/26
  Subject: Foundation wall height clarification at Grid A
  Ref: S-101, Detail 3/S-101
  Status: Open
  Blocking: Yes - cannot form walls until answered
```

## Submittal Log

For each submittal:
- **Number**: e.g., "03300-1"
- **Section**: CSI spec section
- **Title**: e.g., "Concrete mix designs"
- **Submitted**: Date
- **Status**: Submitted, approved, approved as noted, revise, rejected
- **Lead time**: Weeks from approval to delivery
- **Critical path**: Yes/no

**Example**:
```
03300-1
  Section: 03 30 00
  Title: Concrete mix designs
  Submitted: 12/15/25
  Status: Approved
  Lead time: 2 weeks (ready mix, no lead time)
  Critical: No
```

## Contract Terms

- **NTP**: Notice to Proceed date
- **Substantial completion**: Contractual date
- **Final completion**: Contractual date
- **Liquidated damages**: $__ per day
- **Working hours**: Start-end, days of week
- **Noise limits**: dBA, restricted hours

**Example**:
```
NTP: 01/21/26
Substantial: 07/29/26
Final: 08/12/26
LDs: $1,000/day after substantial
Hours: 7:00 AM - 5:00 PM, Mon-Fri
Noise: 85 dBA at property line, no work before 7 AM
```

---

## Executed Subcontracts

### Document Identification

**Signals this is an executed subcontract**:
- "SUBCONTRACT AGREEMENT" or "SUBCONTRACT" title
- Signature pages with executed dates
- Scope of work exhibit (Exhibit A, Schedule A)
- Contract value, retainage percentage
- Insurance requirements exhibit
- Reference to prime contract/owner

### Extraction Targets

**EXTRACT FOR EVERY EXECUTED SUBCONTRACT**:

| Data Point | Example |
|-----------|---------|
| Subcontractor name | "Alexander Construction LLC" |
| Contract number | "SC-825021-06" |
| Trade/scope description | "PEMB Erection — Erect Nucor PEMB structure per contract drawings" |
| Contract value | "$85,000.00" |
| Execution date | "01/28/2026" |
| Start date | "03/23/2026" |
| Completion date | "04/20/2026" |
| Retainage | "10% until 50% complete, 5% thereafter" |
| Payment terms | "Net 30 from approved pay app" |
| Liquidated damages | "$500/day (if applicable)" |

**SCOPE DETAILS — Extract from scope exhibit**:

- **Included scope**: Itemized list of what the sub will furnish and install
- **Excluded scope**: What is NOT included (critical for gap identification)
- **Allowances**: Any dollar or unit allowances within the scope
- **Unit prices**: If contract includes unit price items (e.g., "rock excavation at $XX/CY")
- **Alternates**: If any alternates were accepted or rejected
- **Owner-furnished items**: Materials provided by GC or owner that sub installs
- **Sub-furnished items**: Materials the sub procures

**INSURANCE REQUIREMENTS**:

| Coverage | Required Limit |
|----------|---------------|
| General liability | "$1,000,000 per occurrence / $2,000,000 aggregate" |
| Auto liability | "$1,000,000 combined single limit" |
| Workers compensation | "Statutory" |
| Umbrella/excess | "$2,000,000" |
| Professional liability | "If design-build scope" |
| Builder's risk | "Covered by GC" or "Sub-provided" |

**KEY CONTRACT CLAUSES**:

- **Change order process**: How changes are handled, markup percentages (OH&P)
- **Schedule requirements**: Milestones, float ownership, acceleration rights
- **Warranty**: Duration beyond standard 1-year (e.g., "2-year roof warranty")
- **Indemnification**: Hold harmless clause scope
- **Dispute resolution**: Mediation, arbitration, litigation
- **Termination**: For cause and for convenience provisions
- **Safety requirements**: Site-specific safety obligations
- **Clean-up**: Daily clean-up, final clean-up responsibilities

**Output format**:
```json
{
  "subcontract": {
    "contractor": "Alexander Construction LLC",
    "contract_number": "SC-825021-06",
    "trade": "PEMB Erection",
    "scope_summary": "Erect Nucor PEMB structure per contract drawings",
    "value": "$85,000.00",
    "executed": "01/28/2026",
    "start": "03/23/2026",
    "completion": "04/20/2026",
    "retainage": "10% flat per W Principles standard",
    "payment_terms": "Net 30",
    "inclusions": [
      "Erection of all primary framing (columns, rafters)",
      "Installation of secondary framing (purlins, girts)",
      "Installation of all bracing",
      "Crane and rigging for erection",
      "Erection bolts and hardware"
    ],
    "exclusions": [
      "Roof and wall panels (by others)",
      "Trim and accessories (by others)",
      "Foundation and anchor bolts (by others)",
      "Touch-up paint on field connections"
    ],
    "insurance": {
      "gl": "$1M/$2M",
      "auto": "$1M CSL",
      "wc": "Statutory",
      "umbrella": "$2M"
    },
    "warranty": "1 year standard",
    "change_order_markup": "15% OH&P on subcontractor work"
  }
}
```

---

## Purchase Orders

### Document Identification

**Signals this is a purchase order**:
- "PURCHASE ORDER" header or "PO" designation
- PO number (sequential or project-coded)
- Vendor/supplier name and address
- Line items with quantities, unit prices, extended prices
- Delivery dates and shipping terms
- Payment terms
- May reference spec sections or submittal approvals

### Extraction Targets

**EXTRACT FOR EVERY PURCHASE ORDER**:

| Data Point | Example |
|-----------|---------|
| PO number | "PO-2026-0142" |
| Vendor/supplier | "Ferguson Enterprises" |
| Date issued | "02/01/2026" |
| Total value | "$24,850.00" |
| Payment terms | "Net 30" |
| Shipping terms | "FOB jobsite" |
| Expected delivery | "03/15/2026" |
| Delivery contact | "Site superintendent" |
| Ship-to address | Project address |

**LINE ITEMS — Extract every line**:

| Data Point | Example |
|-----------|---------|
| Line number | "1" |
| Description | "4\" PVC DWV pipe, Sch 40" |
| Spec section | "22 11 16" |
| Quantity | "500 LF" |
| Unit price | "$4.25/LF" |
| Extended price | "$2,125.00" |
| Manufacturer | "Charlotte Pipe" |
| Lead time | "Stock — 3 days" |

**DELIVERY AND LOGISTICS**:

- **Delivery schedule**: Single delivery or phased deliveries
- **Partial shipments**: Allowed or not
- **Storage requirements**: Covered, climate-controlled, lay-flat
- **Unloading responsibility**: Vendor or GC
- **Inspection period**: Days to inspect after delivery

**WARRANTY AND DOCUMENTATION**:

- **Warranty period**: Standard manufacturer warranty
- **Required certifications**: Mill certs, test reports, UL listings
- **O&M manuals**: Required with delivery or at closeout
- **Attic stock**: Percentage or quantity of spare material

**CRITICAL PATH FLAG**:

- Is this material on the critical path? (based on schedule cross-reference)
- Is this a long-lead item? (lead time > 4 weeks)
- Does delivery date align with scheduled installation date?

**Output format**:
```json
{
  "purchase_order": {
    "po_number": "PO-2026-0142",
    "vendor": "Ferguson Enterprises",
    "date_issued": "02/01/2026",
    "total_value": "$24,850.00",
    "payment_terms": "Net 30",
    "shipping": "FOB jobsite",
    "expected_delivery": "03/15/2026",
    "line_items": [
      {
        "line": 1,
        "description": "4\" PVC DWV pipe, Sch 40",
        "spec_section": "22 11 16",
        "quantity": "500 LF",
        "unit_price": "$4.25",
        "extended": "$2,125.00",
        "manufacturer": "Charlotte Pipe",
        "lead_time": "Stock — 3 days"
      }
    ],
    "certifications_required": ["Material test reports"],
    "critical_path": false,
    "long_lead": false,
    "notes": "Standard plumbing rough-in materials"
  }
}
```

---

## Cross-Referencing Project Documents

### Subcontract ↔ Other Data

- **Sub list**: Verify SC scope matches sub list trade description
- **Schedule**: Verify SC dates align with scheduled activities
- **Specifications**: Verify SC scope covers all spec section requirements
- **Insurance log**: Verify insurance certificates match SC requirements
- **Daily reports**: Use SC scope to validate work reported by sub

### Purchase Order ↔ Other Data

- **Submittals**: Verify PO materials match approved submittal products
- **Specifications**: Verify PO items meet spec requirements
- **Schedule**: Verify PO delivery dates align with installation schedule
- **Procurement log**: Update delivery tracking with PO data
- **Budget**: Track committed costs vs. budget by CSI division
