---
description: Track labor hours and productivity
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [log|summary|productivity|validate|payroll|cost]
---

# Labor Tracking Command

## Overview

Comprehensive labor hour management and productivity analysis. Log daily worker hours by trade and classification, track crew-level productivity ratios, validate labor entries against daily reports, generate Davis-Bacon certified payroll data, and analyze labor cost variance.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/labor-tracking/SKILL.md` — Full labor tracking system: entry schemas, crew summaries, productivity benchmarks, validation rules, certified payroll, cost integration
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `labor-tracking.json` (labor_entries, crew_summaries, weekly_summaries, productivity_benchmarks)
- `directory.json` (subcontractors — for employer resolution)
- `daily-report-data.json` (for cross-validation of crew counts)
- `cost-data.json` (for labor cost integration)
- `schedule.json` (for budget hours comparison)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"log"** — Enter daily labor entries for workers/crews
- **"summary"** — Generate weekly or monthly labor summary by trade
- **"productivity"** — Display productivity metrics for a specific trade
- **"validate"** — Cross-check labor entries against daily report crew counts
- **"payroll"** — Generate certified payroll (WH-347) data for Davis-Bacon projects
- **"cost"** — Labor cost analysis and variance reporting

If no sub-action provided, show usage:
```
Usage: /labor [log|summary|productivity|validate|payroll|cost]
Examples:
  /labor log                    → Enter daily labor hours
  /labor summary week           → Weekly labor summary by trade
  /labor productivity concrete  → Productivity metrics for concrete trade
  /labor validate               → Cross-check against daily reports
  /labor payroll week 2026-02-17 → Certified payroll for week
  /labor cost summary           → Labor cost analysis
```

### Step 3: LOG Sub-Action

Collect labor entry details. Support both individual worker entries and bulk crew entry:

**Individual Entry:**
1. **Date**: Default to today
2. **Worker Name**: Full name
3. **Trade**: Select from project subs or enter (Concrete, Steel, Framing, MEP, etc.)
4. **Employer**: Resolve from directory.json subcontractors
5. **Classification**: journeyman, apprentice, foreman, superintendent, laborer, operator
6. **Hours Regular**: Standard hours (40-hr base week)
7. **Hours Overtime**: OT hours (1.5x)
8. **Hours Double-Time**: DT hours (2x, holidays)
9. **Work Description**: What was accomplished
10. **Location**: Grid reference or area
11. **Cost Code**: CSI division code
12. **Hourly Rate**: Base and burdened rates
13. **Certified Payroll Flag**: Include in WH-347?

**Bulk Crew Entry:**
Accept input like: "6 concrete workers from W Principles, 8 hours each, footing rebar"
Auto-expand into individual entries or a crew summary.

Auto-assign entry ID: `LAB-YYYY-MM-DD-NNN`. Save to `labor-tracking.json` labor_entries array.

Also generate crew summary record in crew_summaries array.

### Step 4: SUMMARY Sub-Action

Generate labor summary for specified period:

1. Parse period from arguments: "week" (default) or "month"
2. Aggregate from `labor-tracking.json`:
   - Total hours by trade (regular, OT, DT)
   - OT percentage by trade
   - Labor cost (burdened) by trade
   - Budget vs. actual hours and cost
   - Headcount trend (daily breakdown)
   - Top OT contributors
3. Display formatted summary with variance indicators

### Step 5: PRODUCTIVITY Sub-Action

Display productivity metrics:

1. Parse trade from arguments (e.g., "concrete", "steel", "mep")
2. Pull crew summaries for the specified trade
3. Calculate:
   - Average productivity ratio (output per labor-hour)
   - Comparison to benchmark (from skill's benchmark table)
   - Efficiency factor (actual ÷ benchmark)
   - Weekly trend
   - Earned hours vs. actual hours
   - Cost variance from productivity gap
4. Alert if efficiency drops below 85% threshold

### Step 6: VALIDATE Sub-Action

Cross-check labor entries against daily reports:

1. Parse date or date range from arguments (default: today)
2. Run validation rules from the labor-tracking skill:
   - VR-001: Crew size match (labor entries vs. daily report count)
   - VR-002: Trade completeness (all daily report trades have labor entries)
   - VR-003: Overtime verification (OT hours match daily report notes)
   - VR-004: Headcount trend (>30% drop triggers alert)
3. Display pass/fail for each check with discrepancy details
4. Flag missing entries for reconciliation

### Step 7: PAYROLL Sub-Action

Generate certified payroll data:

1. Parse period from arguments (week ending date or month)
2. Filter labor entries with `certified_payroll_flag: true`
3. Generate WH-347 form data:
   - Worker classifications and prevailing wage rates
   - Hours breakdown (regular, OT)
   - Gross wages and fringe benefits
   - Apprentice ratio compliance check
4. Display summary and offer export (CSV or formatted report)

### Step 8: COST Sub-Action

Labor cost analysis:

1. Parse sub-action: "summary", "by-trade", "by-division", "forecast"
2. Calculate:
   - Total labor cost (burdened) to date
   - Budget vs. actual by trade/division
   - Cost variance percentage
   - Productivity-based earned value variance
   - Burn rate and forecast to completion
3. Alert on divisions >10% over budget

### Step 9: Save & Log

1. Write updated `labor-tracking.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | labor | [sub_action] | [entry IDs or summary details]
   ```
3. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest labor status

## Integration Points
- **Daily Report** (`/daily-report`): Crew counts feed labor validation; labor section prompts for hours
- **Morning Brief** (`/morning-brief`): Yesterday's headcount, OT trending, productivity alerts
- **Weekly Report** (`/weekly-report`): Labor summary aggregated for the week
- **Dashboard** (`/dashboard`): Labor cost burn chart, headcount trend, productivity by trade
- **Cost** (`/cost`): Labor hours drive actual cost calculations
- **EVM** (`/evm`): Productivity ratios feed earned value
- **Sub Scorecard** (`/sub-scorecard`): Efficiency metrics feed performance scoring
