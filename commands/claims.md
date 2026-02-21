---
description: Document claims and generate notices
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [document|notice|package|status]
---

# Claims Management Command

## Overview

Comprehensive claims documentation management for construction superintendents. Log claims-relevant events with contemporaneous records, generate and track formal notice letters, assemble complete claims packages, and review active claims status with evidence inventory and deadline tracking.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/claims-documentation/SKILL.md` -- Full claims documentation system: contemporaneous records, notice requirements, damages calculation, claims package assembly
- `${CLAUDE_PLUGIN_ROOT}/skills/claims-documentation/references/claims-evidence-guide.md` -- Evidence standards, notice templates, damages worksheets, photo protocol
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` -- Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/delay-tracker/SKILL.md` -- Delay events and schedule impact analysis
- `${CLAUDE_PLUGIN_ROOT}/skills/contract-administration/SKILL.md` -- Contract provisions, notice deadlines, dispute resolution procedures

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `claims-log.json` (claims, notice_log, evidence_inventory, timeline_events, summary)
- `delay-log.json` (delays -- for linking delay events to claims)
- `change-order-log.json` (change_orders -- for disputed CO claims)
- `daily-report-data.json` (daily reports -- for evidence linking)
- `directory.json` (project contacts -- for notice recipients)
- `schedule.json` (schedule data -- for critical path references)

If no project config: "No project set up yet. Run `/set-project` first."

If `claims-log.json` does not exist, create it with empty structure:
```json
{
  "claims": [],
  "notice_log": [],
  "evidence_inventory": [],
  "timeline_events": [],
  "summary": {
    "total_active_claims": 0,
    "total_claimed_amount": 0,
    "total_recovered_amount": 0,
    "pending_notices": 0,
    "overdue_notices": 0,
    "next_deadline": null,
    "last_updated": null
  }
}
```

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"document"** -- Log a claims-relevant event with contemporaneous record
- **"notice"** -- Generate and track a formal notice letter
- **"package"** -- Assemble a claims package from accumulated documentation
- **"status"** -- Review all active claims, notice deadlines, and evidence inventory

If no sub-action provided, show usage:
```
Usage: /claims [document|notice|package|status]
Examples:
  /claims document              -> Log a claims-relevant event (delay, directive, differing condition)
  /claims notice delay          -> Generate a formal delay notice letter
  /claims notice change         -> Generate a change order notice letter
  /claims package CLAIM-001     -> Assemble claims package for CLAIM-001
  /claims status                -> Review all active claims, deadlines, evidence gaps
```

### Step 3: DOCUMENT Sub-Action

Log a claims-relevant event with contemporaneous record. Collect details conversationally:

1. **Event Type**: Classify the event:
   - Delay event (owner-caused, design issue, differing site condition, permit delay)
   - Directive (owner verbal/written directive changing scope, sequence, or schedule)
   - Differing site condition (subsurface or physical conditions different from contract)
   - Constructive change (action requiring additional work without formal CO)
   - Acceleration (directed or constructive -- forced schedule compression)
   - Disruption (trade stacking, out-of-sequence work, access restriction)
   - Back-charge dispute (owner or sub back-charge the contractor disputes)

2. **Date and Time**: When did the event occur or when was it discovered?

3. **Description**: Factual narrative of what happened. Coach the user on claims-grade language: specific, factual, no blame, no conclusions. Include who, what, where, when.

4. **Location**: Resolve against project intelligence (grid lines, floor, area, room).

5. **Parties Involved**: Who caused or directed the event? Who was affected? Resolve from directory.json.

6. **Impact on Work**: What activities are affected? Is work stopped, delayed, disrupted, or changed?

7. **Schedule Impact (Preliminary)**: Is this on the critical path? Estimated duration of impact? Reference delay-log.json for existing delay entries.

8. **Cost Impact (Preliminary)**: Estimated cost categories affected (labor standby, equipment idle, material escalation, overtime).

9. **Evidence Captured**: What documentation exists?
   - Daily report for today (auto-link)
   - Photographs taken (file references)
   - Emails or written directives received
   - RFIs submitted or pending
   - Meeting minutes referencing the event

10. **Linked Records**: Auto-link to existing DELAY-NNN, COR-NNN, RFI-NNN entries if applicable.

11. **Notice Required?**: Based on contract provisions, determine if formal notice is required and calculate the deadline. Alert user if deadline is approaching: "Contract requires notice within 21 days. Deadline: [date]. Recommend sending notice immediately."

Auto-assign unique ID: `CLAIM-NNN` (increment from highest existing). If this event relates to an existing claim, add it as a new event entry within that claim.

Create timeline_events entry. Add to evidence_inventory. Save to `claims-log.json`.

### Step 4: NOTICE Sub-Action

Generate and track a formal notice letter. Parse notice type from arguments:
- **"delay"** -- Delay notice (Template A from claims-evidence-guide.md)
- **"change"** -- Change order / extra work notice (Template B)
- **"site"** or **"dsc"** -- Differing site conditions notice (Template C)
- **"constructive"** -- Constructive change notice (Template D)
- **"acceleration"** -- Acceleration notice (Template E)

For the selected notice type:

1. **Identify the claim**: Which CLAIM-NNN does this notice relate to? If no existing claim, create one first via the DOCUMENT flow.

2. **Pull contract provisions**: From contract-administration skill, identify the applicable notice provision and deadline.

3. **Populate template**: Fill in the notice template using:
   - Project information from project-config.json
   - Claim details from claims-log.json
   - Recipient information from directory.json
   - Contract section references from contract-administration data

4. **Review with user**: Present the draft notice for review. Confirm all facts are accurate and complete.

5. **Generate document**: Save notice as .docx to `{folder_mapping.correspondence}/Notices/NOTICE-NNN_[type]_[date].docx`

6. **Track in notice log**: Create notice_log entry with:
   - Notice ID (auto-assign NOTICE-NNN)
   - Type, date sent, deadline date, contract provision
   - Delivery method (remind user: certified mail + email recommended)
   - Recipients
   - Linked claim ID
   - Follow-up date (set at 14 days after sending, or 7 days before deadline -- whichever is sooner)

7. **Alert user**: "Notice NOTICE-NNN generated. IMPORTANT: Send via certified mail AND email today. Deadline for this notice is [date]. Follow-up reminder set for [date]."

### Step 5: PACKAGE Sub-Action

Assemble a claims package from accumulated documentation. Parse claim ID from arguments (e.g., `/claims package CLAIM-001`).

1. **Load claim data**: Pull all data for the specified CLAIM-NNN from claims-log.json.

2. **Verify completeness**: Check that the claim has:
   - [ ] At least one formal notice on file (warn if missing)
   - [ ] Events documented with evidence references
   - [ ] Schedule impact analysis (TIA or critical path analysis)
   - [ ] Cost documentation for each damage category
   - [ ] Daily reports linked for all relevant dates
   - [ ] Photographs/evidence in inventory
   Report any gaps: "WARNING: No TIA has been performed for this claim. Schedule analysis is required for a complete claims package. Consider running `/delay report` first."

3. **Generate package sections** per the claims-documentation skill:
   - Cover letter
   - Executive summary (2-5 pages)
   - Chronology of events (from timeline_events)
   - Liability analysis (contract provisions, applicable sections)
   - Quantum analysis (damages calculation with supporting worksheets)
   - Schedule analysis summary (reference TIA and delay-log data)
   - Supporting documents index (from evidence_inventory)

4. **Create exhibit index**: List all supporting documents organized by exhibit letter:
   - Exhibit A: Notices
   - Exhibit B: Daily reports
   - Exhibit C: Correspondence
   - Exhibit D: RFIs and responses
   - Exhibit E: Change orders
   - Exhibit F: Schedule documents
   - Exhibit G: Cost documentation
   - Exhibit H: Photographs
   - Exhibit I: Weather data (if applicable)
   - Exhibit J: Expert reports (if any)

5. **Save package**: `{folder_mapping.reports}/Claims/CLAIM-NNN_Package_[date].docx`

6. **Confirm to user**: "Claims package for CLAIM-NNN assembled. Total claimed: $[amount] ([X] days time extension + $[amount] cost). File saved to [path]. Review package before submission. Consider engaging a claims consultant for claims exceeding $100,000."

### Step 6: STATUS Sub-Action

Review all active claims, notice deadlines, and evidence inventory.

1. **Active Claims Summary**:
   Display table of all active claims:
   ```
   | ID | Title | Type | Amount | Status | Next Action |
   ```

2. **Notice Deadline Alert**:
   Check all claims for notice compliance:
   - Notices sent on time (green/compliant)
   - Notices approaching deadline (yellow/warning -- within 7 days)
   - Notices past deadline (red/critical -- rights may be waived)
   - Notices requiring follow-up (no response received within expected period)

3. **Evidence Inventory Review**:
   For each active claim, assess evidence completeness:
   - Daily reports: Are all dates in the claim period covered?
   - Photographs: Are key events documented with photos?
   - Correspondence: Are owner directives and communications on file?
   - Schedule analysis: Has a TIA been performed?
   - Cost documentation: Are actual costs documented for each damage category?
   Report gaps: "CLAIM-001: Missing daily reports for 3/4 and 3/5. Missing TIA. Cost documentation incomplete for subcontractor impacts."

4. **Financial Summary**:
   ```
   Total Active Claims:       [X]
   Total Claimed Amount:      $[amount]
   Total Recovered to Date:   $[amount]
   Pending Resolution:        $[amount]
   ```

5. **Upcoming Deadlines**:
   List all time-sensitive items sorted by date:
   - Notice deadlines
   - Follow-up dates for sent notices
   - Response deadlines from owner/architect
   - Claim submission deadlines (if contractual)

### Step 7: Save & Log

1. Write updated `claims-log.json` with all changes.
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | claims | [sub_action] | [CLAIM-NNN or NOTICE-NNN or "status review"]
   ```
3. If notice deadline is within 7 days, surface alert in next `/morning-brief`.
4. If evidence gaps identified, add recommendations to next `/morning-brief`.
5. If project data changed significantly, regenerate `CLAUDE.md` to reflect claims status.

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces notice deadlines, evidence gaps, upcoming claim actions
- **Daily Report** (`/daily-report`): Claims-grade documentation fields; auto-link to active claims
- **Delay Tracker** (`/delay`): Delay events feed claims; TIA and schedule analysis
- **Change Order** (`/change-order`): Disputed COs escalate to claims
- **Cost** (`/cost`): Actual cost data for damages quantification
- **Pay App** (`/pay-app`): Payment disputes and retainage claims
- **Weekly Report** (`/weekly-report`): Claims status summary section
- **Dashboard** (`/dashboard`): Claims KPI cards (active claims, total exposure, notice compliance)
