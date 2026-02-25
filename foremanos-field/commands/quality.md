---
description: Quality inspections and deficiency tracking
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [checklist|itp|deficiency|metrics|report] [trade or phase]
---

# Quality Management Command

## Overview

Formal Quality Management System (QMS) for construction projects. Run three-phase inspection checklists (pre-installation, installation, post-installation) organized by CSI division, manage the Inspection and Test Plan (ITP), track corrective actions, monitor quality metrics (FPIR, rework rate, deficiency density), and generate quality reports.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/quality-management/SKILL.md` — Full QMS: three-phase checklists by trade, ITP master schedule, corrective action workflows, quality metrics, rework tracking
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `quality-data.json` (checklists, itp, corrective_actions, rework_items, quality_metrics)
- `specs-quality.json` (acceptance criteria, hold_points, weather_thresholds)
- `plans-spatial.json` (grid_lines, building_areas — for location resolution)
- `directory.json` (subcontractors — for trade/sub assignment)
- `schedule.json` (for ITP schedule alignment)
- `inspection-log.json` (for cross-reference with formal inspections)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"checklist"** — Generate or complete a three-phase inspection checklist for a specific trade
- **"itp"** — Display or manage the Inspection and Test Plan master schedule
- **"deficiency"** — Add, update, or close a deficiency/corrective action
- **"metrics"** — Display current quality KPIs (FPIR, rework rate, deficiency density, QCI)
- **"report"** — Generate quality performance report (.docx)

If no sub-action provided, show usage:
```
Usage: /quality [checklist|itp|deficiency|metrics|report] [trade or phase]
Examples:
  /quality checklist concrete pre_installation  → Pre-install checklist for concrete
  /quality checklist pemb installation          → Installation checklist for PEMB
  /quality itp                                  → View full ITP schedule
  /quality itp --hold-points-only               → View pending hold points
  /quality deficiency add                       → Log a new deficiency
  /quality deficiency close CA-03-001           → Close a corrective action
  /quality metrics                              → View quality KPIs
  /quality report weekly                        → Generate weekly quality report
```

### Step 3: CHECKLIST Sub-Action

Generate or complete a three-phase inspection checklist:

1. Parse trade and phase from arguments (e.g., "concrete pre_installation")
2. Load the appropriate checklist template from the quality-management skill:
   - Concrete (CSI 03): formwork, rebar, embedments, mix design, weather, curing
   - Structural Steel / PEMB (CSI 05): anchor bolts, material certs, connections, torque
   - CFS Framing & Gypsum Board (CSI 09): stud spacing, fastener pattern, fire-stopping
   - Roofing & Building Envelope (CSI 07): substrate moisture, seam integrity, flashing
   - MEP Systems (CSI 21-28): routing, hanger spacing, pressure testing, penetration sealing
   - Flooring (CSI 09 65): substrate moisture, adhesive, seam integrity
   - Doors & Hardware (CSI 08): frame plumb, hardware function, fire-rated assembly
   - Paint & Coatings (CSI 09 91): surface prep, mil thickness, coverage
3. Auto-populate acceptance criteria from `specs-quality.json` where available
4. Walk through items interactively — for each item:
   - Pass/fail result
   - Measurement value (if applicable)
   - Notes and photo references
5. Track hold points and witness requirements
6. Generate checklist summary: items passed, failed, conditional
7. Auto-assign checklist ID: `QC-[DIV]-NNN`
8. Save to `quality-data.json` checklists array

### Step 4: ITP Sub-Action

Display or manage the Inspection and Test Plan:

1. If no filter, display the full ITP master schedule from quality-data.json
2. Support filters:
   - By trade: `--trade pemb`
   - By status: `--status pending`
   - By date range: `--from 03/01 --to 03/31`
   - Hold points only: `--hold-points-only`
3. For each ITP entry, show:
   - Activity, CSI division, hold point ID
   - Witness requirement
   - Inspection method and acceptance criteria
   - Scheduled date and status
4. Allow updates: mark hold points as released, schedule new inspections

### Step 5: DEFICIENCY Sub-Action

Manage deficiency and corrective action items:

**Add**: Collect deficiency details:
1. Location (resolve against project intelligence)
2. Description of non-conformance
3. Severity: minor (5 business days), major (2 business days), critical (24 hours)
4. Specification violated (reference from specs-quality.json)
5. Discovery source (inspection checklist, field observation, punch list)
6. Responsible trade/sub (from directory.json)
7. Root cause analysis (5 Whys if severity > minor)
8. Corrective actions with responsible party and deadline
9. Prevention measure

Auto-assign ID: `CA-[DIV]-NNN`. Save to `quality-data.json` corrective_actions array.

**Update**: Change status, add notes, update completion progress.

**Close**: Mark as verified and closed with verification date and inspector.

### Step 6: METRICS Sub-Action

Calculate and display quality KPIs:

1. **FPIR (First-Pass Inspection Rate)**: (inspections passed first attempt / total inspections) × 100%
   - Target: >90%
2. **Rework Rate**: (rework cost / contract value) × 100%
   - Target: <2.0%
3. **Deficiency Density**: (total deficiencies / building SF) × 1,000
   - Target: <5 per 1,000 SF
4. **Quality Cost Index (QCI)**: (prevention + appraisal + failure costs / contract value) × 100%
   - Target: 3-5%
5. **Trend Analysis**: Weekly FPIR trend, rework by trade, deficiency closure rate
6. **Trade Quality Summary**: FPIR and deficiency count by trade

### Step 7: REPORT Sub-Action

Generate quality performance report (.docx):

1. Determine period: weekly (default) or monthly
2. Include:
   - Quality scorecard with all KPIs
   - Inspection activity summary (conducted, passed, failed)
   - Hold point status (released, pending)
   - Open corrective actions with aging
   - Rework items and cost impact
   - Trade quality summary table
   - Upcoming hold points and inspections
   - Pareto analysis of deficiency root causes (monthly)
   - Recommendations
3. Save to `{folder_mapping.ai_output}/{PROJECT_CODE}_Quality_Report_{date}.docx`

### Step 8: Save & Log

1. Write updated `quality-data.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | quality | [sub_action] | [checklist/CA ID or "report generated"]
   ```
3. If critical deficiency logged, surface alert in next `/morning-brief`
4. If failed post-installation items exist, auto-create punch list entries via punch-list integration
5. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest quality status

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces open corrective actions, failed inspections, upcoming hold points
- **Daily Report** (`/daily-report`): Quality observations link to active checklists
- **Weekly Report** (`/weekly-report`): Quality metrics aggregated for the week
- **Dashboard** (`/dashboard`): Quality KPI cards (FPIR, rework trend, deficiency density)
- **Inspections** (`/inspections`): Quality hold points trigger formal code inspections
- **Punch List** (`/punch-list`): Failed Phase 3 items auto-convert to punch list entries
- **Sub Scorecard** (`/sub-scorecard`): FPIR and deficiency data feed quality dimension
- **Drawing Control** (`/drawings`): Checklist references validated against current drawing revisions
