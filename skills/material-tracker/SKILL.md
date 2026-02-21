---
name: material-tracker
description: >
  Track materials from purchase order through delivery through spec verification. Use when the user
  mentions "material tracking", "procurement", "delivery", "long lead", "order status", "PO",
  "purchase order", "material status", "vendor", "supplier", "sourcing", "find a vendor",
  "who sells", "where to get", "cert tracking", "mill certs", "material certs".
version: 1.0.0
---

# Material Tracker Skill

## Overview

The material-tracker skill provides full lifecycle material management for construction projects — from identifying what needs to be ordered, through PO tracking, delivery logging, spec verification, and certification tracking. It also maintains a vendor database for sourcing decisions.

**Key capabilities:**
- Identify long-lead items from project schedule and specification requirements
- Track purchase orders from creation through delivery
- Log incoming deliveries with date, quantity, and condition data
- Verify delivered materials against specification requirements
- Track material certifications and test reports
- Source vendors and suppliers for any required material
- Alert on critical timeline risks (materials needed within 14 days but not yet ordered)
- Cross-reference submittals for approval status before material acceptance

---

## Five Core Actions

### A) **Add** — Add New Procurement Item

**What it does:** Creates a new tracking record for a material that needs to be procured. Automatically populates details from schedule long-lead items and spec sections when matches exist.

**Workflow:**
1. Trigger: User identifies a material to procure, or system detects from schedule
2. Input required:
   - Material name/description
   - Quantity and units
   - Target delivery date (or search window)
   - Responsible party (contractor, subcontractor, owner-supplied)
3. System auto-populates:
   - Spec section reference (from spec_sections matching material type)
   - Key material requirements (from key_materials database)
   - Expected delivery window (from schedule.long_lead_items if applicable)
   - Linked submittal (if one exists for this material)
   - Vendor suggestions (from vendor_database recent suppliers)
4. Manual entry for:
   - Specific requirements/options
   - Budget/cost estimate
   - PO number (once issued)
5. Saves to procurement_log with status = "identified"

**Auto-population rules:**
- If material name matches key_materials entry, populate: spec requirements, expected lead time, typical vendors
- If material is in schedule.long_lead_items, populate: scheduled delivery date, related task
- If material has associated submittal, link submittal_log entry and show approval status
- Cross-reference with subcontractors list to identify who furnishes each material

---

### B) **Status** — Show Procurement Dashboard

**What it does:** Displays current status of all procurement items with filtering, color-coding, and alerts.

**Workflow:**
1. Query procurement_log with current dates and statuses
2. Display options:
   - **All items** — Full procurement list with columns: material, spec section, PO status, expected delivery, actual delivery, cert status
   - **Long-lead filter** — Only items from schedule.long_lead_items
   - **Delayed items** — Where actual_delivery > expected_delivery OR delivery_status still "ordered"
   - **Upcoming deliveries** — Items due within 14 days
   - **Missing certs** — Items where cert_status ≠ "verified"
3. Color coding:
   - Green: Item ordered, on schedule, certs received
   - Yellow: Item ordered but near due date, or certs pending review
   - Red: Item not ordered but due soon, delayed delivery, missing required certs
   - Gray: Not yet ordered, future item
4. Alert highlights:
   - **Critical:** Items where delivery_expected < today + 14 days AND (status = "not_ordered" OR status = "ordered")
   - **Warning:** Items where delivery_expected < today + 30 days AND delivery_status = "not_ordered"
   - **Overdue:** delivery_actual < delivery_expected
5. Summary metrics: # ordered, # delivered, # with complete certs, # at risk

---

### C) **Delivery** — Log Incoming Material Delivery

**What it does:** Records the arrival of materials, capturing date, quantity received, condition, and cross-checking against PO.

**Workflow:**
1. Trigger: Material arrives on site
2. Input collected:
   - Procurement item (lookup from log)
   - Actual delivery date
   - Quantity received (compare against PO qty)
   - Condition assessment: intact/undamaged, minor damage, major damage
   - Packing slip/bill of lading #
   - Receiving notes (any discrepancies)
3. System validation:
   - Does received quantity match PO quantity?
   - Does packing slip item description match PO?
   - Is material needed for upcoming work?
4. Cross-check against spec:
   - Confirm this material matches the spec section requirement
   - Note if product model/version differs from submittal
5. Update procurement_log:
   - Set delivery_status = "delivered"
   - Record delivery_date, delivery_quantity, delivery_condition
   - Link to packing slip documentation
6. Generate receiving report for daily log integration
7. Trigger next action: **Verify** (if certs required and received) or hold for verification

---

### D) **Verify** — Run Spec Verification on Delivered Material

**What it does:** Compares delivered material properties, documentation, and certifications against specification requirements. Uses submittal-intelligence compliance checking methodology.

**Workflow:**
1. Trigger: Material received and ready for inspection
2. Gather verification data:
   - Material documentation (certs, test reports, product data sheets)
   - Specification section requirements for this material type
   - Approved submittal (if exists) from submittal_log
3. Run compliance checks (per submittal-intelligence):
   - Product model matches submittal and spec
   - Material properties meet spec minimums (strength, durability, etc.)
   - Certifications present and valid (mill certs, test reports, UL listing, etc.)
   - Installation/handling instructions reviewed
4. Document findings:
   - Conforming: Material meets all requirements → Mark cert_status = "verified"
   - Non-conforming: Document deficiency with photo, reference spec requirement
   - Conditional approval: Material acceptable with conditions (e.g., different color lot, different option)
5. Update procurement_log:
   - Set verification_status
   - Record verification_date and inspector
   - Attach compliance report
   - Note any exceptions or deviations
6. Alert actions:
   - If non-conforming: Notify supplier, document decision (accept/reject/return)
   - If verified: Clear for installation/use
   - If incomplete certs: Escalate and hold material

---

### E) **Source / Find Vendor** — Search for Suppliers

**What it does:** Identifies vendors and suppliers for materials. Checks internal vendor database first, then offers web search. Saves results for future reference.

**Workflow:**
1. Trigger: User needs to source a material or establish where to buy
2. Input: Material name/specification
3. Search vendor_database:
   - Look up by material type
   - Show recent suppliers (with past performance notes)
   - Filter by: location, specialty, certified capability
4. If no suitable match in database:
   - Offer structured web search suggestions
   - Typical search terms: material type + local area + supplier category
5. Capture results:
   - Company name, contact (phone/email), location
   - Specialty/products offered
   - Lead time estimate
   - Cost range (if quoted)
   - Performance notes: reliability, quality, responsiveness
6. Save to vendor_database:
   - Auto-tag with material type
   - Link to project if sourced for specific item
   - User can rate/comment for future projects
7. Recommend best match based on:
   - Lead time fit with schedule
   - Availability of spec version
   - Geographic proximity (delivery cost)
   - Past performance history

---

## Data Sources

The material-tracker skill integrates with:

- **procurement_log** — Core record of all materials being tracked, with status, dates, quantities, costs
- **spec_sections** — Specification requirements for each material type (cross-reference for verification)
- **key_materials** — Project's critical materials list (auto-population source)
- **schedule.long_lead_items** — Long-lead materials from project schedule
- **submittal_log** — Submittal approval status (track approvals before material use)
- **vendor_database** — Historical and recommended suppliers by material type
- **subcontractors** — List of responsible parties for furnishing materials
- **daily reports** — Receiving and delivery logs for integration

---

## Auto-Population Rules

When **Add** action creates a new procurement item:

1. **Match to key_materials:** If material name matches entry in key_materials, auto-fill:
   - Spec section reference
   - Typical lead time
   - Spec requirements summary
   - Last vendor used (from procurement_log history)

2. **Match to schedule.long_lead_items:** If material is in schedule long-lead list, auto-fill:
   - Scheduled delivery date
   - Related schedule activity
   - Dependencies/critical path impact

3. **Match to submittal:** If material has associated submittal in submittal_log, auto-fill:
   - Link submittal record
   - Show submittal approval status
   - Reference approved model/options

4. **Vendor assignment:** Assign responsible party from subcontractors list:
   - Some items are owner-supplied
   - Some are general contractor furnished
   - Some are subcontractor furnished

---

## Alert Rules

The system flags items for superintendent attention:

**Critical (red):**
- Expected delivery date is within 14 days AND delivery_status = "not_ordered" or "ordered"
- Delivery is overdue (delivery_actual_date > expected_delivery_date)
- Required certification is missing and hold period expired

**Warning (yellow):**
- Expected delivery within 30 days AND status = "not_ordered"
- Certification received but not yet verified (cert_status = "requested")
- Non-conformance pending disposition decision

**Information (blue):**
- Upcoming delivery (within 60 days) to plan receiving
- New vendor used for first time (cross-reference on performance)

---

## Cross-References

- **project-data skill** — For schedule, spec sections, project site info, subcontractor list
- **submittal-intelligence skill** — For compliance checking methodology when verifying delivered materials against specs; for tracking submittal approvals that gate material use

---

## Workflow Integration

**Typical material procurement workflow:**

1. **Identify** (project-data) — Review schedule long-lead items and spec sections
2. **Add** (this skill) — Create procurement tracking record, auto-populate from schedule/spec
3. **Source** (this skill) — Find vendor, get quote, recommend supplier
4. **Order** — Issue PO (external system, record PO# in material-tracker)
5. **Track** (this skill) → **Status** — Monitor delivery timeline
6. **Receive** (this skill) → **Delivery** — Log arrival, inspect condition
7. **Verify** (this skill) → **Verify** — Check against spec, collect certifications
8. **Approve** — Clear for use or escalate non-conformance
9. **Closeout** — Verify all certs filed, update daily reports

---

## SC/PO Log Spreadsheet Sync

Many GCs maintain an Excel-based SC/PO log for subcontract and purchase order tracking. The material-tracker can read from this spreadsheet to auto-populate procurement data.

### How it works:

1. During `/set-project` (Step 1C), the plugin scans `folder_mapping.spreadsheets` for files matching `*SC*PO*Log*.xlsx` or `*SC-PO*.xlsx`
2. If found, the file path is stored in `folder_mapping.sc_po_log`
3. When `/material-tracker status` is run and `sc_po_log` is set, the skill reads the spreadsheet to sync data

### Spreadsheet reading workflow:

1. Open the SC/PO Log spreadsheet using the xlsx skill
2. Identify the header row and map columns to procurement_log fields:
   - Look for columns like: "SC/PO #", "Vendor/Sub", "Description", "Amount", "Status", "Delivery Date", "Notes"
   - Common column names vary — use fuzzy matching (e.g., "PO Number" = "SC/PO #", "Supplier" = "Vendor/Sub")
3. For each row with data:
   - Check if a matching procurement_log entry already exists (match on PO number or description)
   - If new: create a PROC-XXX entry and populate from spreadsheet data
   - If existing: update delivery status, dates, and amounts if the spreadsheet has newer data
4. After sync, present a summary: "Synced X items from SC/PO Log. Y new items added, Z items updated."
5. Store `last_sync_date` in config so the user knows when data was last refreshed

### Important rules:
- The spreadsheet is the **source of truth** for PO numbers, contract values, and vendor assignments
- The plugin is the **source of truth** for delivery verification, spec compliance, and certification tracking
- Never write back to the spreadsheet — only read from it
- Flag discrepancies between spreadsheet data and plugin data for the user to resolve

---

## Daily Report Integration

Procurement data feeds into daily reports:

- **Receiving log** — Materials delivered today (from Delivery logs)
- **Material status dashboard** — At-risk items flagged by Status action
- **Certification tracker** — Certs due/received, missing items
- **Vendor performance** — On-time delivery, quality, responsiveness notes

---

## File Structure

```
material-tracker/
├── SKILL.md (this file)
└── references/
    ├── delivery-verification.md
    └── cert-tracking.md
```

