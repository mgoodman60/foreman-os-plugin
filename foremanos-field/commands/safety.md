---
description: Safety management and OSHA reporting
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [log|incident|toolbox|jsa|metrics|inspect|report]
---

# Safety Management Command

## Overview

Comprehensive safety management for construction superintendents. Log incidents and near-misses, conduct and document toolbox talks, create Job Safety Analyses (JSAs), run site safety inspections, track OSHA metrics (TRIR/DART/EMR), and generate professional safety reports.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/safety-management/SKILL.md` — Full safety management system: incident tracking, OSHA recordkeeping, toolbox talks, JSAs, inspection checklists, metrics
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/field-reference/references/` — Field-specific safety references based on current work types

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `safety-log.json` (incidents, near_misses, first_aid_log, toolbox_talks, jsas, inspections, metrics)
- `schedule.json` (current phase, active work types — for relevant toolbox talk topics)
- `directory.json` (subcontractors — for crew/trade identification)
- `labor-tracking.json` (total hours worked — needed for TRIR/DART calculation)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"log"** or **"incident"** — Log a recordable incident, near-miss, or first-aid event
- **"toolbox"** — Document a toolbox talk with topic, attendance, and key points
- **"jsa"** — Create or review a Job Safety Analysis for a specific activity
- **"metrics"** — Display current safety KPIs (TRIR, DART, leading/lagging indicators)
- **"inspect"** — Run a safety inspection checklist (fall protection, excavation, electrical, housekeeping)
- **"report"** — Generate weekly or monthly safety summary report (.docx)

If no sub-action provided, show usage:
```
Usage: /safety [log|incident|toolbox|jsa|metrics|inspect|report]
Examples:
  /safety log                → Log an incident, near-miss, or first-aid event
  /safety toolbox            → Document a toolbox talk
  /safety jsa concrete pour  → Create JSA for concrete pour activity
  /safety metrics            → View current TRIR, DART, and leading indicators
  /safety inspect fall       → Run fall protection inspection checklist
  /safety report weekly      → Generate weekly safety summary
```

### Step 3: LOG / INCIDENT Sub-Action

Collect incident details conversationally:

1. **Incident Type**: Classify using the recordability decision tree from the safety-management skill
   - Recordable incident (OSHA 300 Log)
   - Near-miss
   - First-aid only
2. **Date and Time**: When did it occur?
3. **Location**: Resolve against project intelligence (grid, area, room)
4. **Description**: Factual narrative of what happened
5. **Personnel Involved**: Craft, employer (resolve from directory.json)
6. **Injury Details** (if applicable): Body part, injury type, severity
7. **Medical Treatment**: First aid only vs. medical treatment (determines recordability)
8. **Root Cause Analysis**: Walk through the 5-Whys method per the skill
9. **Corrective Actions**: Specific, assignable, measurable actions with deadlines
10. **Photos/Documentation**: Accept file path references
11. **Linked Daily Report**: Auto-link to today's date

Auto-assign unique ID: `INC-NNN`, `NEAR-MISS-NNN`, or `FIRST-AID-NNN` (increment from highest existing).

If recordable, also populate OSHA 300 Log fields (days away, restricted duty, classification).

Save to `safety-log.json` in the appropriate array. Log to version_history.

### Step 4: TOOLBOX Sub-Action

Document a toolbox talk:

1. **Topic**: Select from the safety-management skill's topic library based on current work types, or enter custom topic
2. **Duration**: Minutes (typically 5-15)
3. **Facilitator**: Name of person conducting the talk
4. **Attendance Count**: Number of attendees
5. **Trades Present**: Which trades/crews attended
6. **Key Points Covered**: 3-5 bullet points discussed
7. **Action Items**: Any follow-up actions from discussion
8. **Linked Daily Report**: Auto-link to today's date

Auto-suggest topic based on today's scheduled work from schedule.json and recent incidents/near-misses.

Auto-assign ID: `TOOLBOX-NNN`. Save to `safety-log.json` toolbox_talks array.

### Step 5: JSA Sub-Action

Create or review a Job Safety Analysis:

1. If user provides an activity name, generate a JSA using the safety-management skill's structure:
   - Task steps → Hazards → Controls → Responsible parties
2. Cross-reference with current weather thresholds from specs-quality.json
3. Cross-reference with active work types from schedule.json
4. Include relevant OSHA standard references
5. Format as a printable sign-off document
6. Save to `safety-log.json` jsas array

If "review" specified, display existing JSAs and allow updates/additions.

### Step 6: METRICS Sub-Action

Calculate and display current safety KPIs:

1. **TRIR**: (Recordable Cases × 200,000) / Total Hours Worked
2. **DART Rate**: (DART Cases × 200,000) / Total Hours Worked
3. **Near-Miss Ratio**: Near-misses to incidents ratio (target >5:1)
4. **Leading Indicators**: Toolbox talks held, JSAs completed, inspections conducted, corrective actions closed
5. **Lagging Indicators**: Recordable incidents, days away, restricted duty days
6. **Trend**: Compare current month to previous month and project goal

Pull total hours from `labor-tracking.json`. If not available, estimate from daily report headcounts.

### Step 7: INSPECT Sub-Action

Run a safety inspection checklist:

Parse the inspection type from arguments (fall, excavation, electrical, housekeeping, or general).

Use the safety-management skill's inspection checklists:
- Fall Protection Inspection Checklist
- Excavation & Trenching Safety Checklist
- Electrical Safety Inspection Checklist
- Housekeeping & General Site Safety Checklist

Walk through items interactively. For each item:
- Mark pass/fail
- Note deficiencies with description and severity (minor/major)
- Assign corrective actions with responsible party and deadline

Save inspection results to `safety-log.json` inspections array.

### Step 8: REPORT Sub-Action

Generate a professional safety report (.docx):

1. Determine period: weekly (default) or monthly from arguments
2. Pull all safety data for the period from `safety-log.json`
3. Include:
   - **Incident Summary**: Recordable incidents, near-misses, first-aid events
   - **TRIR/DART Calculations**: Current rates with trend
   - **Toolbox Talks**: Topics covered, attendance, frequency
   - **JSA Activity**: New/reviewed JSAs
   - **Inspection Results**: Deficiencies found, closure rate
   - **Leading Indicators**: Metrics with trend arrows
   - **Upcoming High-Risk Activities**: From schedule.json
   - **Recommendations**: Based on data trends
4. Save to `{folder_mapping.ai_output}/{PROJECT_CODE}_Safety_Report_{date}.docx`
5. Confirm file location to user

### Step 9: Save & Log

1. Write updated `safety-log.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | safety | [sub_action] | [ID or "report generated"]
   ```
3. If incident logged, surface alert in next `/morning-brief`
4. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest safety status

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces open incidents, near-misses, toolbox talk due dates, safety alerts
- **Daily Report** (`/daily-report`): Safety section auto-populates from today's logged incidents and toolbox talks
- **Weekly Report** (`/weekly-report`): Aggregates safety metrics for the week
- **Dashboard** (`/dashboard`): Safety KPI cards (TRIR, DART, leading indicators)
- **Sub Scorecard** (`/sub-scorecard`): Safety dimension feeds from incident data by sub
