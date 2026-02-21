---
description: Track project closeout, commissioning, and warranty items
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [status | add | commission | warranty | checklist | generate]
---

# /closeout Command

Track project closeout deliverables, building systems commissioning, and warranty documentation. Manages closeout status from pre-substantial completion through final closeout and warranty management.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/closeout-commissioning/SKILL.md` — Skill documentation
- `${CLAUDE_PLUGIN_ROOT}/skills/closeout-commissioning/references/closeout-checklist.md` — Master checklist reference
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project information
- `${CLAUDE_PLUGIN_ROOT}/skills/field-reference/SKILL.md` — System startup sequences
- `${CLAUDE_PLUGIN_ROOT}/skills/cobie-export/SKILL.md` — COBie export for facility handover (if COBie deliverable is required)

## Usage

```
/closeout [status | add | commission | warranty | checklist | generate]
```

---

## Step 1: Initialize Closeout Data

If this is the first use of the /closeout command on a project, initialize the closeout data file:

1. Read `/folder_mapping.ai_output` directory path from project configuration
2. Create `/folder_mapping.ai_output/closeout-data.json` if it does not exist
3. Initialize with template structure:
   ```json
   {
     "project_id": "[from project-data.json]",
     "project_name": "[from project-data.json]",
     "closeout_status": {
       "phase": "pre_substantial",
       "substantial_completion_date": null,
       "final_completion_date": null,
       "items": [],
       "retainage": {
         "total_held": 0,
         "released": 0,
         "remaining": 0,
         "conditions_for_release": []
       }
     },
     "commissioning": {
       "commissioning_agent": null,
       "systems": []
     },
     "warranties": {
       "standard_warranty_start": null,
       "warranties": []
     }
   }
   ```

---

## Command: `/closeout status`

Display current closeout status dashboard.

### Steps

1. Read `closeout-data.json` from `folder_mapping.ai_output`
2. Calculate completion metrics by category:
   - Count items by status (not_started, in_progress, submitted, approved, na)
   - Calculate percentage complete for each category (O&M, As-builts, Warranties, Training, Testing, Spare Parts, Keys, Certificates)
   - Identify any overdue items (due_date before today)

3. Display dashboard with:
   ```
   CLOSEOUT STATUS DASHBOARD
   =========================

   Phase: [pre_substantial | substantial_punch | final_closeout | complete]

   COMPLETION BY CATEGORY
   ─────────────────────
   O&M Manuals:          5/8 (62%)
   As-Built Drawings:    2/3 (67%)
   Warranties:           4/12 (33%)
   Training:             3/5 (60%)
   Testing & TAB:        2/4 (50%)
   Spare Parts:          1/7 (14%)
   Keys/Access:          0/2 (0%)
   Certificates:         1/5 (20%)

   OVERALL CLOSEOUT:     18/46 (39%)

   RETAINAGE
   ─────────
   Total Held:           $[retainage.total_held]
   Released:             $[retainage.released]
   Remaining:            $[retainage.remaining]
   Release Conditions:   [list conditions]

   OVERDUE ITEMS (4 items)
   ──────────────────────
   [List all items where due_date < today, sorted by due date]
   - CLO-162: Ceiling Tiles Procured (Due: 2026-04-15)
   - CLO-167: Spare Parts Inventory List (Due: 2026-04-20)
   - CLO-171: Master Keying Schedule (Due: 2026-05-01)
   - CLO-181: Request COO (Due: 2026-05-10)

   COMMISSIONING STATUS
   ───────────────────
   Total Systems: [count]
   Completed: [count]
   In Progress: [count]

   Systems by Phase:
   - Pre-Functional: [system list]
   - Functional Testing: [system list]
   - Integrated Testing: [system list]
   - Seasonal Testing: [system list]
   - Complete: [system list]

   UPCOMING DEADLINES (Next 14 days)
   ────────────────────────────────
   [List items due within 14 days, sorted by date]
   - 2026-04-25: CLO-201 Owner Walkthrough
   - 2026-04-28: CLO-202 Create Punch List
   - 2026-05-01: CLO-203 Certificate of Substantial Completion

   PUNCH LIST SUMMARY
   ──────────────────
   Total Items: [count from punch-list.json]
   Not Started: [count]
   In Progress: [count]
   Completed: [count]

   View details: /punch-list
   ```

4. If overdue items exist, highlight in red and indicate scheduling risk
5. If in substantial_punch phase, highlight punch list and reinspection status
6. If in final_closeout phase, highlight critical path items (final payment, lien waivers, retainage release)

---

## Command: `/closeout add [item description]`

Add a new closeout item to tracking.

### Steps

1. If no arguments provided:
   - Display the master closeout checklist from `closeout-checklist.md`
   - Ask superintendent to select which items to add
   - Present menu with categories:
     ```
     Select category for new item:
     1. Contract Closeout Documents
     2. O&M Manuals
     3. As-Built Drawings
     4. Warranty Documentation
     5. Training Documentation
     6. Spare Parts & Attic Stock
     7. Keys & Keying Schedule
     8. Certificates
     9. Testing & Balancing
     ```

2. If item description provided:
   - Classify item into appropriate category
   - Check if item already exists in closeout-data.json (avoid duplicates)
   - Prompt for:
     - Responsible party (read from `directory.json` if available)
     - Due date (allow selection or manual entry)
     - Specification section (if applicable)
     - Notes (optional)

3. Create new item object:
   ```json
   {
     "id": "[CLO-NNN]",
     "category": "[category]",
     "description": "[description]",
     "responsible_party": "[party]",
     "status": "not_started",
     "due_date": "YYYY-MM-DD",
     "date_submitted": null,
     "date_approved": null,
     "notes": "[notes]",
     "spec_section": "[section]"
   }
   ```

4. Generate next available CLO number by reading existing closeout-data.json
5. Add item to closeout-data.json
6. Confirm item added; display summary:
   ```
   Item added: CLO-XXX
   Description: [description]
   Responsible: [party]
   Due: [date]
   Category: [category]
   ```

---

## Command: `/closeout checklist`

Generate full closeout checklist pre-populated with project-specific data.

### Steps

1. Read `closeout-checklist.md` reference document
2. Read `closeout-data.json` to get current status of all items
3. Read `directory.json` to substitute actual contractor/subcontractor names for responsible parties
4. Read `specs-quality.json` to identify all systems (HVAC, electrical, plumbing, fire protection, elevators, etc.)
5. Generate comprehensive checklist organized by phase:
   - Pre-Substantial Completion (30-60 days before)
   - Substantial Completion (the event)
   - Punch List Period (30-60 days after)
   - Final Completion
   - Post-Completion (Year 1 and beyond)

6. For each line item in checklist:
   - Show item number (CLO-XXX)
   - Show description
   - Show responsible party (substituted from directory.json)
   - Show status from closeout-data.json
   - Show due date
   - Show date submitted (if applicable)
   - Show date approved (if applicable)
   - Show completion percentage (submitted + approved / total)

7. Display in table format with color coding:
   - Green: Completed/Approved
   - Yellow: In Progress/Submitted
   - Red: Not Started or Overdue
   - Gray: Not Applicable

8. Display summary statistics:
   ```
   CLOSEOUT CHECKLIST
   ==================

   PROJECT: [name]
   CURRENT PHASE: [phase]

   PHASE: PRE-SUBSTANTIAL COMPLETION
   ─────────────────────────────────
   [Table with all phase items, status, responsible parties]
   Phase Completion: 18/47 (38%)

   PHASE: SUBSTANTIAL COMPLETION
   ──────────────────────────────
   [Table with all phase items]
   Phase Completion: 0/7 (0%)

   PHASE: PUNCH LIST PERIOD
   ───────────────────────
   [Table with all phase items]
   Phase Completion: 0/24 (0%)

   PHASE: FINAL COMPLETION
   ──────────────────────
   [Table with all phase items]
   Phase Completion: 0/15 (0%)

   PHASE: POST-COMPLETION
   ────────────────────
   [Table with all phase items]
   Phase Completion: 0/8 (0%)

   OVERALL COMPLETION: 18/101 (18%)
   CRITICAL PATH: [identify items on critical path]
   ```

9. At bottom, show checklist legend and key dates

---

## Command: `/closeout commission [system]`

Track commissioning for a specific system.

### Steps

1. If no system specified:
   - Display list of all systems from specs-quality.json
   - Ask which system to track
   - Allow multi-select for commissioning multiple systems

2. For selected system:
   - Read commissioning data from closeout-data.json
   - Display system startup sequence from field-reference SKILL (or SKILL.md reference table)
   - Show current phase (pre_functional, functional_testing, integrated_testing, seasonal_testing, complete)

3. Display interactive form to log commissioning activities:
   ```
   COMMISSIONING TRACKER - [SYSTEM NAME]
   =====================================

   Current Phase: [phase]

   PRE-FUNCTIONAL TESTING
   ──────────────────────
   Date: [YYYY-MM-DD or click to set]
   Result: [ ] Pass  [ ] Fail  [ ] Conditional
   Deficiencies: [text field for issues found]

   FUNCTIONAL PERFORMANCE TESTING
   ──────────────────────────────
   Date: [YYYY-MM-DD or click to set]
   Result: [ ] Pass  [ ] Fail  [ ] Conditional
   Test Data: [hyperlink to test results file]
   Deficiencies: [text field for issues found]

   INTEGRATED SYSTEMS TESTING
   ──────────────────────────
   Date: [YYYY-MM-DD or click to set]
   Result: [ ] Pass  [ ] Fail  [ ] Conditional
   Systems Integrated With: [list]
   Deficiencies: [text field for issues found]

   SEASONAL TESTING (if applicable)
   ────────────────────────────────
   Summer Test Date: [YYYY-MM-DD]
   Summer Result: [ ] Pass  [ ] Fail  [ ] Conditional
   Winter Test Date: [YYYY-MM-DD]
   Winter Result: [ ] Pass  [ ] Fail  [ ] Conditional

   DEFICIENCIES & RETESTING
   ────────────────────────
   [ ] Retesting Required
   Retesting Date: [YYYY-MM-DD]
   Retesting Result: [ ] Pass  [ ] Fail  [ ] Conditional

   TRAINING & DOCUMENTATION
   ────────────────────────
   [ ] Owner Training Complete
   Training Date: [YYYY-MM-DD]
   [ ] Commissioning Report Complete
   [ ] O&M Manual Updated
   [ ] Startup Sequence Documented

   NOTES
   ─────
   [multiline text field]

   [SAVE] [CANCEL]
   ```

4. When save is clicked:
   - Validate required fields
   - Update commissioning section of closeout-data.json
   - Update phase based on test results (if all phases pass, mark complete)
   - If deficiencies found, create deficiency tracking items

5. Display confirmation:
   ```
   System commissioning updated: [SYSTEM NAME]
   Phase: [phase]
   Status: [status]
   Last Updated: [date/time]

   Next Steps:
   - [action required]
   ```

6. If deficiencies found, offer to create punch list items or deficiency tracking

---

## Command: `/closeout warranty [add | status | expiring]`

Track warranties for systems and equipment.

### Steps: Add Warranty

1. Display form to add new warranty:
   ```
   ADD WARRANTY
   ============

   Warranty Type:
   [ ] Standard Construction (1-year from SC)
   [ ] Extended Warranty (roofing, waterproofing, equipment)
   [ ] Manufacturer Warranty

   System/Product: [dropdown from specs-quality.json]
   Warranty Start Date: [YYYY-MM-DD]
   Warranty Duration: [years/months]
   Warranty Expiration Date: [auto-calculated]
   Coverage Details: [text field]
   Manufacturer/Contractor: [name]
   Contact Person: [name, phone, email]
   Documentation Location: [file path or hyperlink]

   [ADD WARRANTY] [CANCEL]
   ```

2. When add is clicked:
   - Validate all required fields
   - Calculate expiration date
   - Create warranty entry:
   ```json
   {
     "id": "WRR-XXX",
     "system": "[system]",
     "type": "[type]",
     "start_date": "YYYY-MM-DD",
     "expiration_date": "YYYY-MM-DD",
     "duration": "[years]",
     "coverage": "[description]",
     "manufacturer": "[name]",
     "contact": "[name/phone/email]",
     "documentation": "[path]",
     "claims": []
   }
   ```
   - Add to closeout-data.json warranties section
   - Confirm warranty added

### Steps: Warranty Status

1. Display warranty status by system:
   ```
   WARRANTY STATUS
   ===============

   SYSTEM: HVAC
   ────────────
   Standard Warranty (1-year from SC)
   Start: 2026-04-01
   Expires: 2027-04-01 (350 days remaining)
   Manufacturer: Johnson Controls
   Contact: John Smith (555-1234)

   Extended Warranty - RTU Compressor (5-year)
   Start: 2026-04-01
   Expires: 2031-04-01 (5+ years remaining)
   Manufacturer: Carrier
   Contact: Support (1-800-CARRIER)

   SYSTEM: ROOFING
   ───────────────
   Extended Warranty - Membrane (25-year material)
   Start: 2026-04-01
   Expires: 2051-04-01 (25+ years remaining)
   Manufacturer: Carlisle SynTec
   Contact: Warranty Claims (1-877-CARLISLE)

   [Show all systems and warranties]

   CLAIMS HISTORY
   ──────────────
   [List any warranty claims made to date]
   ```

2. Color-code by status:
   - Green: Valid warranty (> 1 year remaining)
   - Yellow: Expiring soon (30-90 days)
   - Red: Critical (< 30 days or expired)

### Steps: Expiring Warranties

1. Read all warranties from closeout-data.json
2. Filter for warranties expiring within 30 days, 7 days, or already expired
3. Display expiration alerts:
   ```
   EXPIRING WARRANTIES ALERT
   ==========================

   CRITICAL - Expires within 7 days (1)
   ─────────────────────────────────────
   Standard Construction Warranty (HVAC)
   Expires: 2027-04-01
   Action: Contact GC immediately for any deficiencies

   WARNING - Expires within 30 days (2)
   ────────────────────────────────────
   Plumbing 5-Year Equipment Warranty
   Expires: 2027-04-15

   Electrical Panel 5-Year Warranty
   Expires: 2027-04-22

   ACTION REQUIRED
   ───────────────
   - Conduct 11-month warranty inspection
   - Document any deficiencies
   - Submit warranty claims before expiration
   - Coordinate repairs with GC or manufacturer
   ```

---

## Command: `/closeout generate`

Generate a professional closeout status report for distribution to owner and PM.

### Steps

1. Read all data:
   - closeout-data.json for status, retainage, commissioning data
   - punch-list.json for punch list status
   - inspection-log.json for final inspection data
   - directory.json for project team information
   - project-data.json for project details

2. Create professional report document (.docx format):
   ```
   CLOSEOUT STATUS REPORT
   [PROJECT NAME]
   [DATE]

   EXECUTIVE SUMMARY
   ──────────────────
   Project Phase: [phase]
   Overall Closeout Completion: [percentage]
   Outstanding Items: [count]
   Schedule Status: [On Track / At Risk / Delayed]
   Key Milestones: [list with dates]

   PROJECT INFORMATION
   ───────────────────
   Project: [name]
   Owner: [name]
   General Contractor: [name]
   Architect: [name]
   Project Manager: [name]
   Superintendent: [name]
   Report Date: [today]
   Report Period: [date to date]

   CLOSEOUT STATUS BY CATEGORY
   ──────────────────────────

   O&M Manuals
   Status: [X/8 Complete] ([%])
   Outstanding Items: [list]
   Target Date: [date]

   As-Built Drawings
   Status: [X/X Complete] ([%])
   Outstanding Items: [list]
   Target Date: [date]

   [Continue for all categories]

   RETAINAGE SUMMARY
   ─────────────────
   Total Contract Value: $[from directory.json]
   Total Retainage: $[total_held]
   Retainage % of Contract: [%]
   Released to Date: $[released]
   Remaining Retainage: $[remaining]

   Conditions for Release:
   - [condition 1]
   - [condition 2]
   - [condition 3]

   COMMISSIONING STATUS
   ───────────────────

   Completed Systems: [count]
   - [System 1]
   - [System 2]

   In Progress Systems: [count]
   - [System 1] - Phase: [phase] - Est. Completion: [date]

   System Startup Sequences:
   - [Link to field-reference documentation]

   PUNCH LIST STATUS
   ─────────────────

   Total Items: [count]
   Completed: [count] ([%])
   In Progress: [count]
   Not Started: [count]

   Top 5 Outstanding Items:
   [List highest priority items]

   Weekly Progress: [Show trend of completion]

   Estimated Final Completion: [date]

   WARRANTY DOCUMENTATION
   ──────────────────────

   Warranty Tracking Status: [X/X Complete]
   Extended Warranties: [count by type]
   Expiring Within 30 Days: [count and list]

   Standard Warranty Period:
   Start Date: [SC date]
   Expiration Date: [+1 year from SC]
   Days Remaining: [number]

   OUTSTANDING ITEMS
   ─────────────────

   Critical/Overdue Items:
   1. [Item] - Due: [date] - [X days overdue]
   2. [Item] - Due: [date] - [X days overdue]

   At-Risk Items (Due within 7 days):
   1. [Item] - Due: [date]
   2. [Item] - Due: [date]

   SCHEDULE & NEXT STEPS
   ───────────────────

   Key Milestones:
   [ ] Substantial Completion: [date] [Status: Complete/In Progress/Pending]
   [ ] Punch List Completion: [date] [Status: Complete/In Progress/Pending]
   [ ] Final Completion: [target date]

   Actions Required:
   - [action] - Owner / Responsible Party - Due: [date]
   - [action] - GC / Responsible Party - Due: [date]

   APPENDICES
   ──────────
   A. Detailed Closeout Checklist (50+ items)
   B. Commissioning System Startup Sequences
   C. Warranty Tracking Summary
   D. Retainage Schedule
   E. Contact Information

   ---

   Report Prepared By: [superintendent name]
   Approved By: [project manager name]
   ```

3. Format report as professional .docx document with:
   - Project logo (if available)
   - Table of contents
   - Page numbers
   - Professional formatting and color coding
   - Charts/graphs for completion percentages and schedule timeline

4. Save report to:
   ```
   /folder_mapping.ai_output/reports/Closeout-Status-[YYYY-MM-DD].docx
   ```

5. Display confirmation:
   ```
   CLOSEOUT STATUS REPORT GENERATED
   ════════════════════════════════

   Report: Closeout-Status-2026-04-15.docx
   Location: /[path to folder_mapping.ai_output]/reports/
   Size: [file size]
   Created: [date/time]

   The report is ready for distribution to the owner and project manager.

   Distribution Checklist:
   [ ] Email to Project Manager
   [ ] Email to Owner
   [ ] Share with Architect
   [ ] Post to project portal (if applicable)
   ```

---

## Data Integration

### Reads From:
- `closeout-data.json` (closeout and commissioning status)
- `punch-list.json` (punch list items and status)
- `inspection-log.json` (inspection results and dates)
- `directory.json` (contractor and subcontractor names, contact info)
- `specs-quality.json` (building systems, equipment lists)
- `folder_mapping.ai_output` (data storage location)

### Writes To:
- `closeout-data.json` (all closeout and commissioning updates)
- `/reports/Closeout-Status-[YYYY-MM-DD].docx` (generated reports)

### Save & Log:
- Update `project-config.json` version_history:
  ```
  [TIMESTAMP] | closeout | [sub-action] | [details]
  ```
- If project data changed significantly, regenerate `CLAUDE.md` to reflect the latest project state

---

## Example Workflows

### Workflow 1: Add All Standard Closeout Items
```
1. User runs: /closeout add
2. Display master checklist
3. User selects: "Initialize all standard items"
4. System loads all ~50 items from closeout-checklist.md
5. System substitutes contractor names from directory.json
6. System adds all items to closeout-data.json
7. Dashboard shows: 0/50 items complete (0%)
```

### Workflow 2: Track HVAC Commissioning
```
1. User runs: /closeout commission HVAC
2. Display HVAC system startup sequence (from field-reference)
3. User enters pre-functional test results (Pass/Fail/Conditional)
4. If conditional, user enters deficiencies
5. System advances phase to functional_testing
6. User schedules functional performance test date
7. Upon completion, system advances to integrated_testing phase
8. Final status shows commissioning complete when all phases pass
```

### Workflow 3: Generate Monthly Status Report
```
1. User runs: /closeout generate
2. System reads current status from all data files
3. System calculates completion percentages by category
4. System identifies critical path items and overdue items
5. System generates professional .docx report
6. Report saved to /reports/ folder
7. User can distribute to owner and PM
```

---

## Notes for Field Superintendent

- **Timing:** Start closeout tracking 60 days before expected substantial completion
- **Key Dates:** Track substantial completion date carefully; all warranty periods start from this date
- **Documentation:** Keep all testing reports, training records, and warranties organized in closeout binder
- **Owner Communication:** Update closeout status weekly during punch list period; communicate critical path items
- **Critical Items:** Focus on Fire Marshal approval, Elevator inspection, and final C.O. as these often delay project
- **Commissioning:** Coordinate with commissioning agent; ensure all systems tested and approved before owner turnover
- **Retainage:** Track retainage carefully; conditions for release must be met for final payment
