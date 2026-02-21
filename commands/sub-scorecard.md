---
description: Subcontractor performance scorecards
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [sub name|all|report]
---

# Subcontractor Performance Scorecard Command

## Overview

Generate objective, data-driven performance scorecards for every subcontractor on the project. Scorecards aggregate actual project data across five critical performance dimensions — Schedule Adherence (25%), Quality (25%), Safety (20%), Responsiveness (15%), and Professionalism (15%) — each scored 1-10 to produce a weighted composite score. Enables informed bidding decisions, back-charge documentation, and performance improvement conversations.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/sub-performance/SKILL.md` — Full scoring methodology: 5 dimensions with criteria, data sources, calculation formulas, composite scoring, example scorecards
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `directory.json` (subcontractors — master list of subs with contact info)
- `daily-report-data.json` (crew counts, attendance, field observations by sub)
- `quality-data.json` (FPIR by trade, deficiencies, rework items)
- `safety-log.json` (incidents, near-misses, toolbox talk participation by sub)
- `rfi-log.json` (response time, quality of responses)
- `submittal-log.json` (submittal turnaround, resubmission rate)
- `inspection-log.json` (inspection pass/fail rates by trade)
- `labor-tracking.json` (crew consistency, productivity)
- `punch-list.json` (punch items by responsible sub)
- `change-order-log.json` (CO responsiveness, disputed items)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments

Examine `$ARGUMENTS` to determine scope:
- **Sub name** (e.g., "Walker", "EKD") — Generate scorecard for a specific subcontractor
- **"all"** — Generate scorecards for all active subcontractors
- **"report"** — Generate comprehensive performance report (.docx) for all subs
- **"compare"** — Side-by-side comparison of specified subs

If no argument provided, show usage:
```
Usage: /sub-scorecard [sub name|all|report|compare]
Examples:
  /sub-scorecard Walker          → Scorecard for Walker Construction
  /sub-scorecard all             → Scorecards for all active subs
  /sub-scorecard report          → Full performance report (.docx)
  /sub-scorecard compare Walker EKD → Side-by-side comparison
```

### Step 3: Resolve Subcontractor

1. Parse sub name from arguments
2. Match against `directory.json` subcontractors array (fuzzy match on name)
3. If "all", iterate through all subs with status "active" or "executed"
4. If no match found, list available subs and ask user to clarify

### Step 4: Calculate Five Dimensions

For each subcontractor, calculate scores across all 5 dimensions:

**Dimension 1: Schedule Adherence (25% weight)**
- Primary metric: PPC (Percent Plan Complete) from weekly planning data
- Secondary: Crew size consistency (promised vs. actual from daily reports)
- Secondary: Milestone performance (on-time vs. late)
- Scoring: 90%+ PPC = 10, 80-89% = 8, 70-79% = 6, 60-69% = 4, <60% = 2
- Adjust ±0.5 for crew consistency and milestone performance
- Data sources: daily-report-data.json (crew counts), schedule.json (milestone dates)

**Dimension 2: Quality (25% weight)**
- Primary: First-Pass Inspection Rate (FPIR) from quality-data.json
- Secondary: Punch list items attributed to this sub
- Secondary: Rework cost attributed to this sub
- Scoring: FPIR >95% = 10, 90-95% = 8, 85-90% = 6, 80-85% = 4, <80% = 2
- Adjust for rework cost impact and punch list density
- Data sources: quality-data.json, inspection-log.json, punch-list.json

**Dimension 3: Safety (20% weight)**
- Primary: Incident rate (recordable incidents per 200K hours for this sub)
- Secondary: Toolbox talk participation rate
- Secondary: Near-miss reporting (higher is better — indicates safety culture)
- Secondary: PPE compliance from daily observations
- Scoring: Zero incidents + active safety participation = 10; any recordable = max 6
- Data sources: safety-log.json, daily-report-data.json

**Dimension 4: Responsiveness (15% weight)**
- Primary: RFI response turnaround time (average days)
- Secondary: Submittal turnaround time
- Secondary: Communication quality (rated from field observations)
- Secondary: Change order response time
- Scoring: <3 day avg response = 10, 3-5 days = 8, 5-7 days = 6, 7-10 days = 4, >10 days = 2
- Data sources: rfi-log.json, submittal-log.json, change-order-log.json

**Dimension 5: Professionalism (15% weight)**
- Primary: Site cleanliness and housekeeping (from daily report observations)
- Secondary: Cooperation with other trades
- Secondary: Documentation quality (daily logs, certifications on time)
- Secondary: Contract compliance (insurance, bonds, payroll on time)
- Scoring: Based on field observation patterns in daily reports
- Data sources: daily-report-data.json (field observations), project-config.json (contract compliance)

### Step 5: Calculate Composite Score

```
Composite = (Schedule × 0.25) + (Quality × 0.25) + (Safety × 0.20) + (Responsiveness × 0.15) + (Professionalism × 0.15)
```

Rating scale:
- 9.0-10.0: Excellent — Preferred for future projects
- 7.0-8.9: Good — Reliable performer
- 5.0-6.9: Average — Room for improvement; monitor closely
- 3.0-4.9: Below Average — Performance improvement plan needed
- 1.0-2.9: Unsatisfactory — Contract review; consider replacement

### Step 6: Present Scorecard

Display scorecard for each sub:

```
SUBCONTRACTOR PERFORMANCE SCORECARD
══════════════════════════════════════════════════
Walker Construction (Excavation/Sitework)
Period: Project to Date (01/27/26 - 02/19/26)

  Schedule Adherence (25%)  ████████░░  8.5
  Quality (25%)             ██████████  10.0
  Safety (20%)              ████████░░  8.0
  Responsiveness (15%)      ██████░░░░  6.0
  Professionalism (15%)     ████████░░  8.0
  ─────────────────────────────────────────
  COMPOSITE SCORE:                      8.3 (Good)

Strengths: Zero deficiencies, consistent crew size, strong safety record
Improvement Areas: RFI response averaging 6 days (target: <5)
```

### Step 7: REPORT Sub-Action

Generate comprehensive performance report (.docx):

1. Include for each sub:
   - Full scorecard with all 5 dimensions
   - Data sources and calculation methodology (transparency)
   - Trend over time (if multiple scoring periods exist)
   - Strengths and improvement areas narrative
   - Specific examples from project data
2. Project-wide summary:
   - Average scores across all subs by dimension
   - Ranking table (highest to lowest composite)
   - Recommendations for performance conversations
   - Preferred vendor list candidates (score >8.0)
   - At-risk subs requiring attention (score <5.0)
3. Save to `{folder_mapping.ai_output}/{PROJECT_CODE}_Sub_Performance_{date}.docx`

### Step 8: Save & Log

1. Save scorecard data to project configuration (for historical tracking)
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | sub-scorecard | [sub name or "all"] | [composite score]
   ```
3. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest sub performance data

## Integration Points
- **Morning Brief** (`/morning-brief`): Flag subs with declining scores or recent incidents
- **Weekly Report** (`/weekly-report`): Sub performance summary section
- **Dashboard** (`/dashboard`): Sub performance comparison chart
- **Daily Report** (`/daily-report`): Field observations feed professionalism scoring
- **Quality** (`/quality`): FPIR and rework data feed quality dimension
- **Safety** (`/safety`): Incident and participation data feed safety dimension
- **Labor** (`/labor`): Productivity and crew consistency feed schedule dimension
- **Plan** (`/plan`): PPC by trade feeds schedule adherence dimension
