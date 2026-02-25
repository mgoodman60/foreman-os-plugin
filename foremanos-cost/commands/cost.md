---
description: Track costs, variance, and forecasting
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [status|forecast|variance|invoice|report]
---

# Cost Tracking Command

## Overview

Comprehensive project cost management for construction superintendents and project managers. Track actual costs against budget by CSI division, calculate Cost Performance Index (CPI), identify cost variances with early warning alerts, reconcile invoices against commitments, manage change order cost impacts, and project cash flow through completion.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/cost-tracking/SKILL.md` — Full cost tracking system: budget structure, CPI calculation, variance analysis, invoice reconciliation, change order cost impact, cash flow, contingency tracking
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/estimating-intelligence/SKILL.md` — Unit cost validation, productivity rates, and bid review (stub — full skill in foremanos-intel)

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `cost-data.json` (budget_by_division, cost_performance, contingency, cash_flow)
- `change-order-log.json` (approved COs — for applied cost adjustments)
- `pay-app-log.json` (sov, pay_applications — for invoiced/paid amounts)
- `labor-tracking.json` (labor costs for actual cost calculation)
- `procurement-log.json` (material commitments and deliveries)
- `schedule.json` (percent complete — for earned value and CPI)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"status"** — Budget vs. actual summary by CSI division with CPI
- **"forecast"** — Estimate at Completion (EAC), burn rate, and cash flow projection
- **"variance"** — Detailed variance analysis by division with root cause flags
- **"invoice"** — Reconcile an invoice against committed costs and budget
- **"report"** — Generate cost performance report (.docx)

If no sub-action provided, show usage:
```
Usage: /cost [status|forecast|variance|invoice|report]
Examples:
  /cost status            → Budget vs actual by division with CPI
  /cost forecast          → EAC, burn rate, cash flow projection
  /cost variance          → Detailed variance analysis
  /cost invoice           → Reconcile incoming invoice
  /cost report monthly    → Generate monthly cost report
```

### Step 3: STATUS Sub-Action

Display budget vs. actual summary:

1. Load `cost-data.json` budget_by_division
2. For each CSI division, calculate and display:
   - Original amount, applied COs, current budget
   - Committed costs, invoiced costs, paid costs
   - Forecast to complete, total forecast
   - Variance (current budget - total forecast): favorable or unfavorable
   - Variance percentage
3. Calculate project-level CPI:
   - Earned Value = Current budget × percent complete (from schedule.json)
   - Actual Cost = Total invoiced + paid costs
   - CPI = EV / AC
4. Color-code: green (CPI ≥ 0.95), yellow (0.90-0.95), red (<0.90)
5. Show project totals: original contract, approved COs, current contract, total forecast, variance

### Step 4: FORECAST Sub-Action

Generate cost forecasts:

1. Calculate key forecast metrics:
   - **EAC (Estimate at Completion)**: BAC / CPI (CPI-based forecast)
   - **ETC (Estimate to Complete)**: EAC - AC
   - **VAC (Variance at Completion)**: BAC - EAC
   - **TCPI (To-Complete Performance Index)**: (BAC - EV) / (BAC - AC)
2. Calculate burn rate:
   - Current daily/weekly spending rate
   - Projected spending through completion
3. Cash flow projection:
   - Monthly projected spend based on schedule and committed costs
   - Cumulative cash flow curve (actual vs. planned)
4. Contingency status:
   - Original contingency amount
   - Consumed contingency (from COs and overruns)
   - Remaining contingency
   - Projected contingency sufficiency
5. Alert if EAC exceeds budget or contingency insufficient

### Step 5: VARIANCE Sub-Action

Detailed variance analysis:

1. For each CSI division with variance >5%:
   - Show original budget, current budget, actual/forecast
   - Calculate variance amount and percentage
   - Flag root cause category: scope change, productivity, material price, schedule impact, rework
2. Sort by largest unfavorable variance
3. Show trend: is the variance growing or shrinking?
4. Recommend corrective actions for divisions >10% unfavorable:
   - Review committed costs for over-commitment
   - Check for unapproved scope additions
   - Analyze productivity data from labor-tracking
   - Verify material prices against procurement log

### Step 6: INVOICE Sub-Action

Reconcile an incoming invoice:

1. Collect invoice details:
   - Vendor/subcontractor name (resolve from directory.json)
   - Invoice amount
   - Invoice date and number
   - CSI division / cost code
   - Work period covered
2. Cross-check against:
   - Committed costs (POs, subcontracts)
   - Previous invoices (prevent double-billing)
   - Pay application progress (from pay-app-log.json)
   - Budget remaining for this division
3. Flag discrepancies:
   - Invoice exceeds committed amount
   - Invoice for work not in current schedule
   - Duplicate invoice detection
   - Retainage calculation verification
4. Approve or flag for review

### Step 7: REPORT Sub-Action

Generate cost performance report (.docx):

1. Determine period: monthly (default) or project-to-date
2. Include:
   - Executive cost summary (contract value, spent, forecast, variance)
   - Budget vs. actual table by CSI division
   - CPI trend chart (monthly)
   - Top 5 variance items with root cause
   - Change order cost impact summary
   - Cash flow projection chart
   - Contingency status
   - Recommendations and risk items
3. Save to `{folder_mapping.ai_output}/{PROJECT_CODE}_Cost_Report_{date}.docx`

### Step 8: Save & Log

1. Write updated `cost-data.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | cost | [sub_action] | [details]
   ```
3. If CPI drops below 0.90, surface alert in next `/morning-brief`
4. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest cost status

## Integration Points
- **Morning Brief** (`/morning-brief`): Budget divisions >10% variance, CPI alerts
- **Weekly Report** (`/weekly-report`): Cost vs. budget section, CPI trend
- **Dashboard** (`/dashboard`): Cumulative cost curve, CPI trend line, variance cards
- **Pay App** (`/pay-app`): Invoice reconciliation and billing progress
- **Change Order** (`/change-order`): CO cost impact applied to budget
- **Labor** (`/labor`): Labor costs feed actual cost accumulation
- **EVM** (`/evm`): Cost data provides AC for earned value calculations
- **Material Tracker** (`/material-tracker`): Procurement costs feed committed amounts
