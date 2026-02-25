---
description: BIM coordination and clash management
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [status|clash|model|scan]
---

# BIM Coordination Command

## Overview

BIM coordination management for construction superintendents. Track clash detection workflows, log model reviews and field verification findings, document laser scans and drone flights, and manage coordination meeting records. Provides real-time BIM metrics including open clash counts, model version status, scan schedules, and coordination meeting history.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/bim-coordination/SKILL.md` — Full BIM coordination system: clash detection workflows, model-to-field verification, 4D scheduling, laser scanning, drone surveys, digital twin closeout, LOD specifications, data model
- `${CLAUDE_PLUGIN_ROOT}/skills/bim-coordination/references/bim-field-guide.md` — Field reference: model viewer controls, clash report reading, field measurement methods, common model issues, coordination meeting checklist, LOD quick reference, AR tools, scan-to-BIM verification
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/rfi-preparer/SKILL.md` — RFI tracking for clash-driven RFIs

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `bim-log.json` (clash_reports, model_reviews, field_verifications, scan_records, drone_flights, coordination_meetings)
- `schedule.json` (current phase, active work — for 4D context)
- `directory.json` (subcontractors — for trade coordination assignments)
- `rfi-log.json` (existing RFIs — for cross-referencing clash-driven RFIs)

If `bim-log.json` does not exist, create it with the empty schema:
```json
{
  "clash_reports": [],
  "model_reviews": [],
  "field_verifications": [],
  "scan_records": [],
  "drone_flights": [],
  "coordination_meetings": []
}
```

Determine the next available ID for each category by scanning existing entries (e.g., if last clash report is CR-003, next is CR-004).

### Step 2: Parse Arguments

The user provides one of four subcommands:
- **status** — Display current BIM coordination metrics and dashboard
- **clash** — Log clash resolution, review clash reports, generate clash-driven RFIs
- **model** — Log model review findings, field verification discrepancies, update issue status
- **scan** — Schedule/document laser scans and drone flights, log results

If no argument is provided, default to **status**.

If the user provides additional natural language after the subcommand, use it as context (e.g., `/bim clash resolved 5 clashes at Level 3` or `/bim scan drone flight completed today`).

### Step 3: STATUS — Display BIM Coordination Dashboard

When the argument is `status` (or no argument):

1. **Clash Summary**:
   - Total open clashes (from most recent clash report)
   - Clash trend: compare to previous report (increasing/decreasing/stable)
   - Breakdown by category (MEP/structural, MEP/MEP, MEP/architectural, 4D)
   - Priority breakdown (critical, high, medium, low)
   - Clashes past resolution deadline (flag these prominently)

2. **Model Version**:
   - Current model version (from most recent model_review or clash_report)
   - Date of last model update
   - Open model review findings count

3. **Recent Scans**:
   - Last scan date, type, location
   - Out-of-tolerance items count from last scan
   - Upcoming scans scheduled (if noted in entries)

4. **Drone Flights**:
   - Last flight date and purpose
   - Upcoming flights scheduled

5. **Coordination Meetings**:
   - Last meeting date and key decisions
   - Next meeting date (from last meeting's next_meeting field)
   - Open action items from previous meetings

6. **Field Verifications**:
   - Open deviations count
   - In-progress resolutions count
   - Recent deviations (last 7 days)

Format output as a clean dashboard with clear section headers.

### Step 4: CLASH — Clash Management

When the argument is `clash`:

**Log New Clash Report**:
- Prompt for: tool used, model version, total clashes, breakdown by category and priority
- Auto-assign next CR-### ID
- Calculate resolved/open from previous report comparison if available
- Add entry to `clash_reports` array

**Resolve Clashes**:
- Prompt for: clash IDs resolved, resolution description, resolution type (model change, field adjustment, RFI, acceptance)
- Update notes on the relevant clash report entry
- If resolution generated an RFI, note the RFI ID for cross-reference with rfi-log.json

**Review Clash Report**:
- Display most recent clash report with full breakdown
- Highlight critical and high-priority items
- Show trend vs. previous reports (are clashes being resolved faster than new ones appear?)
- List clashes assigned to each trade

**Generate Clash-Driven RFI**:
- Collect clash details: clash ID, elements involved, grid location, description of design conflict
- Format RFI description referencing the clash report and model version
- Note RFI in bim-log.json for cross-reference
- Instruct user to submit through the `/rfi` command for full RFI tracking

### Step 5: MODEL — Model Review and Field Verification

When the argument is `model`:

**Log Model Review**:
- Prompt for: model version, discipline, reviewer, findings (list), action items
- Auto-assign next MR-### ID
- Set status to "open"
- Add entry to `model_reviews` array

**Log Field Verification**:
- Prompt for: location, element, deviation type, modeled value, measured value
- Auto-calculate deviation and whether within tolerance (reference tolerance table in SKILL.md)
- Auto-assign next FV-### ID
- Add entry to `field_verifications` array

**Update Status**:
- Prompt for: entry ID (MR-### or FV-###), new status, resolution notes
- Update the relevant entry in bim-log.json
- Valid statuses for model reviews: open, in_progress, resolved, closed
- Valid statuses for field verifications: open, in_progress, resolved

**Review Open Items**:
- Display all open model reviews with findings and action items
- Display all open field verifications with deviation details
- Sort by date, flag items older than 2 weeks as overdue

### Step 6: SCAN — Scan and Drone Management

When the argument is `scan`:

**Log Laser Scan**:
- Prompt for: type (terrestrial/handheld/drone-mounted), location, scanner/operator, deliverables received
- Prompt for tolerance check results: elements checked, within tolerance count, out-of-tolerance count, max deviation
- Auto-assign next SC-### ID
- Add entry to `scan_records` array

**Log Drone Flight**:
- Prompt for: pilot (with Part 107 cert#), aircraft, purpose, flight altitude, GSD, deliverables, conditions
- Prompt for airspace authorization details
- Auto-assign next DF-### ID
- Add entry to `drone_flights` array

**Schedule Future Scan/Flight**:
- Note the planned date, type, location, and purpose in a new entry with status "scheduled"
- Set reminder context for morning-brief integration

**Review Scan Results**:
- Display most recent scan with full tolerance check breakdown
- Highlight out-of-tolerance items requiring action
- Cross-reference with field_verifications for items already logged

**Review Drone Deliverables**:
- Display recent drone flights with deliverable status
- Note any missing deliverables that should be followed up with the drone operator

### Step 7: Save and Log

After any data modification:

1. Write updated `bim-log.json` to the project data directory
2. Confirm the save with a summary of changes:
   - New entries added (with IDs)
   - Entries updated (with IDs and field changes)
   - Current totals (open clashes, open reviews, open verifications, scan count, flight count)
3. If the action has integration implications, note them:
   - New critical clash? Flag for morning-brief
   - Clash-driven RFI? Note for rfi-preparer
   - Field deviation? Note for daily-report
   - Upcoming scan? Note for look-ahead-planner

## Integration Points

This command connects to other ForemanOS commands and skills:

- **`/morning-brief`** — Pulls open clash count, upcoming scans, overdue action items from bim-log.json
- **`/daily-report`** — Includes BIM verification activities, clash resolution progress, scan results
- **`/rfi`** — Clash-driven RFIs cross-reference bim-log.json clash IDs
- **`/look-ahead`** — 4D phasing data, scan scheduling, model update deadlines
- **`/closeout`** — Digital twin handoff status, COBie data collection, as-built model verification
- **`/drawings`** — Model version tracking, coordination drawing management
- **`/inspections`** — Scan-based quality verification, tolerance checks

## Example Usage

- `/bim` — Show BIM coordination dashboard (same as `/bim status`)
- `/bim status` — Display current BIM metrics and open items
- `/bim clash` — Log or review clash reports, resolve clashes, generate RFIs
- `/bim clash we resolved 12 clashes at the Level 3 coordination meeting today` — Log clash resolutions with context
- `/bim model` — Log model review or field verification, update status
- `/bim model field check found the duct at C-4 is 4 inches low` — Log a specific field deviation
- `/bim scan` — Log laser scan or drone flight, review results
- `/bim scan drone flight completed today for monthly progress` — Log a completed drone flight
