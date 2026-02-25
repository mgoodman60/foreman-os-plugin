---
description: Earned value management and S-curves
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [status|calculate|curve|forecast|report]
---

# Earned Value Management (EVM) Command

## Overview

Unified scope-schedule-cost performance measurement using Earned Value Management methodology. Calculate SPI, CPI, schedule and cost variances, generate three-line S-curves (BCWS/BCWP/ACWP), forecast project completion cost and date, and produce integrated EVM performance reports. EVM reveals whether cost overruns are due to inefficiency, scope growth, schedule delays, or a combination.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/earned-value-management/SKILL.md` — Full EVM methodology: BAC/PV/EV/AC calculations, SPI/CPI, SV/CV, EAC/ETC/VAC/TCPI, S-curves, forecasting methods
- `${CLAUDE_PLUGIN_ROOT}/skills/cost-tracking/SKILL.md` — Budget structure and actual cost data
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices. See the `web-artifacts-builder` Cowork skill for interactive S-curve HTML visualizations.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `cost-data.json` (budget_by_division, committed/invoiced/paid costs)
- `schedule.json` (milestones, percent_complete, baseline dates, critical_path)
- `labor-tracking.json` (labor hours and costs — key AC component)
- `pay-app-log.json` (billing progress, retainage)
- `change-order-log.json` (approved COs — for BAC adjustments)
- `procurement-log.json` (material costs)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"status"** — Quick EVM dashboard: SPI, CPI, SV, CV, EAC at a glance
- **"calculate"** — Full EVM calculation with all metrics and interpretation
- **"curve"** — Generate S-curve visualization (HTML or data for dashboard)
- **"forecast"** — Detailed forecasting: CPI-based, SPI-based, composite, independent EAC
- **"report"** — Generate comprehensive EVM performance report (.docx)

If no sub-action provided, show usage:
```
Usage: /evm [status|calculate|curve|forecast|report]
Examples:
  /evm status        → Quick SPI/CPI dashboard
  /evm calculate     → Full EVM calculation with interpretation
  /evm curve         → Generate S-curve visualization
  /evm forecast      → Detailed forecasting with multiple methods
  /evm report        → Generate EVM performance report
```

### Step 3: STATUS Sub-Action

Quick EVM dashboard:

1. Calculate core metrics:
   - **BAC**: Current contract value (original + approved COs)
   - **PV (BCWS)**: Budgeted cost of work scheduled through today
   - **EV (BCWP)**: Budgeted cost of work performed (BAC × % complete)
   - **AC (ACWP)**: Actual cost of work performed to date
2. Derive performance indices:
   - **SPI** = EV / PV (schedule efficiency)
   - **CPI** = EV / AC (cost efficiency)
   - **SV** = EV - PV (schedule variance in dollars)
   - **CV** = EV - AC (cost variance in dollars)
3. Display with status indicators:
   - SPI/CPI ≥ 1.0: On track (green)
   - SPI/CPI 0.90-0.99: Watch (yellow)
   - SPI/CPI < 0.90: Action needed (red)
4. Show quick EAC: BAC / CPI

### Step 4: CALCULATE Sub-Action

Full EVM calculation with interpretation:

1. Calculate all Step 3 metrics plus:
   - **EAC (Estimate at Completion)**: Multiple methods:
     - CPI-based: BAC / CPI
     - SPI×CPI composite: AC + (BAC - EV) / (CPI × SPI)
     - Management estimate (if available)
   - **ETC (Estimate to Complete)**: EAC - AC
   - **VAC (Variance at Completion)**: BAC - EAC
   - **TCPI (To-Complete Performance Index)**: (BAC - EV) / (BAC - AC)
   - **% Spent vs. % Complete**: Quick visual of cost-schedule alignment
2. Provide narrative interpretation:
   - "The project has earned $X of value while spending $Y. CPI of Z means..."
   - Flag concerns: "TCPI of 1.15 means the project must perform 15% better than average to finish on budget"
3. Break down by CSI division if data available
4. Show month-over-month trend for SPI and CPI

### Step 5: CURVE Sub-Action

Generate S-curve visualization:

1. Build monthly data points from project start through projected completion:
   - **PV line (BCWS)**: Cumulative planned value per baseline schedule
   - **EV line (BCWP)**: Cumulative earned value per actual progress
   - **AC line (ACWP)**: Cumulative actual costs
2. Generate as:
   - Interactive HTML chart (using Chart.js via web-artifacts-builder skill if available)
   - Data table for inclusion in reports
3. Annotate key points:
   - Current reporting date
   - SV and CV gaps (visual distance between curves)
   - Projected completion point
4. Save HTML to `{folder_mapping.ai_output}/{PROJECT_CODE}_S-Curve_{date}.html`

### Step 6: FORECAST Sub-Action

Detailed forecasting:

1. Calculate multiple EAC methods:
   - **EAC (CPI)**: BAC / CPI — assumes current cost efficiency continues
   - **EAC (SPI×CPI)**: AC + (BAC - EV) / (CPI × SPI) — accounts for schedule impact on cost
   - **EAC (Cumulative)**: AC + (BAC - EV) — assumes remaining work at budgeted rate
   - **Independent EAC**: Bottom-up re-estimate if data supports it
2. Project completion date:
   - Baseline completion date
   - SPI-based adjusted date: Baseline duration / SPI
   - Delay-adjusted date (incorporating delay-log.json data)
3. Confidence range: best case, most likely, worst case
4. Cash flow forecast: monthly projected spend through completion
5. Risk items: divisions or activities most likely to drive further variance

### Step 7: REPORT Sub-Action

Generate EVM performance report (.docx):

1. Include:
   - Executive summary with key metrics (BAC, EV, AC, SPI, CPI, EAC)
   - Performance interpretation narrative
   - S-curve chart (embedded)
   - SPI/CPI trend chart (monthly)
   - Variance analysis by CSI division
   - Forecasting comparison table (all EAC methods)
   - Risk register: items threatening performance
   - Recommendations for corrective action
2. Save to `{folder_mapping.ai_output}/{PROJECT_CODE}_EVM_Report_{date}.docx`

### Step 8: Save & Log

1. Update `cost-data.json` with latest EVM calculations
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | evm | [sub_action] | [key metrics: SPI=X, CPI=Y, EAC=$Z]
   ```
3. If SPI or CPI drops below 0.90, surface alert in next `/morning-brief`
4. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest EVM status

## Integration Points
- **Cost** (`/cost`): Shares budget and actual cost data; EVM extends with schedule integration
- **Morning Brief** (`/morning-brief`): SPI/CPI alerts, EAC vs. budget warnings
- **Weekly Report** (`/weekly-report`): EVM metrics included in cost section
- **Dashboard** (`/dashboard`): S-curve visualization, SPI/CPI trend, EAC cards
- **Labor** (`/labor`): Productivity ratios feed earned value calculations
- **Schedule** (`schedule.json`): Percent complete drives EV calculation
- **Pay App** (`/pay-app`): Billing % vs. schedule % comparison (pay app S-curve)
