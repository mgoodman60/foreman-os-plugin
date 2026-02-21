# cost-tracking — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the cost-tracking skill.



## Cost Forecast Trend Analysis

Track monthly cost curves and S-curves to identify acceleration or deceleration in spending:

```json
{
  "forecast_trends": [
    {
      "month": "2026-02",
      "planned_spend": 125000,
      "actual_spend": 118000,
      "cumulative_planned": 125000,
      "cumulative_actual": 118000,
      "variance": 7000,
      "cpi": 1.06,
      "percent_complete": 12
    },
    {
      "month": "2026-03",
      "planned_spend": 275000,
      "actual_spend": null,
      "cumulative_planned": 400000,
      "cumulative_actual": null,
      "variance": null,
      "cpi": null,
      "percent_complete": 35
    }
  ]
}
```

**Trend Alerts:**
- When cumulative variance > ±5% of budget: Yellow alert
- When cumulative variance > ±10% of budget: Red alert
- When CPI drops below 0.95: Red alert — "Cost overrun trend"
- When month-over-month spending accelerates 20%+: Yellow alert — "Spending acceleration"



## Change Order Cost Impact Tracking

Change orders directly affect project budget and contingency:

```json
{
  "change_order_costs": [
    {
      "co_id": "CO-001",
      "description": "Owner request: Secondary electrical subpanel",
      "originator": "owner",
      "date_approved": "2026-02-17",
      "approved_amount": 17800,
      "cost_impact_category": "owner_directed",
      "charged_against_contingency": true,
      "contingency_used": 17800,
      "affected_divisions": ["26"],
      "affected_subs": ["Electrical (Pending)"],
      "cumulative_owner_cos": 67800,
      "cumulative_contractor_cos": 0,
      "cumulative_all_cos": 67800,
      "notes": ""
    }
  ]
}
```

### CO Cost Trending

Track cumulative CO costs by month and originator:

```json
{
  "co_cost_trending": [
    {
      "month": "2026-02",
      "owner_directed_cos": 67800,
      "architect_cos": 0,
      "contractor_initiated_cos": 0,
      "total_cos_this_month": 67800,
      "cumulative_cos": 67800,
      "percent_of_contract": 2.4,
      "contingency_used_this_month": 17800,
      "contingency_remaining": 132200
    },
    {
      "month": "2026-03",
      "owner_directed_cos": 0,
      "architect_cos": 12000,
      "contractor_initiated_cos": 0,
      "total_cos_this_month": 12000,
      "cumulative_cos": 79800,
      "percent_of_contract": 2.8,
      "contingency_used_this_month": 0,
      "contingency_remaining": 132200
    }
  ]
}
```

### Pending CO Exposure

Track change orders not yet approved but with cost exposure:

```json
{
  "pending_change_orders": [
    {
      "co_id": "CO-002",
      "description": "Potential HVAC capacity upgrade (subject to performance criteria)",
      "estimated_cost": 45000,
      "status": "under_review",
      "probability_of_approval": 0.75,
      "exposure_cost": 33750,
      "notes": "Owner interested but subject to final test results"
    }
  ]
}
```

**Pending CO Calculation:**
- Exposure = Estimated Cost × Probability of Approval
- Total Potential Exposure = Sum of all pending CO exposures
- Alert if exposure > available contingency: "Pending COs exceed available contingency"



## Back-Charge Tracking

Back-charges recover costs for work performed by one sub that should have been done by another:

```json
{
  "back_charges": [
    {
      "id": "BC-001",
      "date_issued": "2026-02-10",
      "charged_to_sub": "ABC Concrete",
      "description": "Rework of floor slab due to improper finishing",
      "amount": 8500,
      "cost_code": "03",
      "originating_cost": "Rework labor + material",
      "reason": "Sub did not meet finish tolerances; GC had to bring in specialist to correct",
      "status": "issued|disputed|resolved|paid",
      "approved_amount": 8500,
      "date_paid": "2026-03-15",
      "notes": ""
    }
  ]
}
```



## Cash Flow Projections

Project cash flow based on billing schedule and payment timing:

### Monthly Billing Projections

```json
{
  "monthly_cash_flow": [
    {
      "month": "2026-02",
      "period_start": "2026-02-01",
      "period_end": "2026-02-28",
      "projected_percent_complete": 12,
      "projected_billable_work": 336600,
      "projected_materials_stored": 8500,
      "subtotal_billable": 345100,
      "retainage_rate": 0.10,
      "projected_retainage": 34510,
      "projected_billing_to_owner": 310590,
      "historical_payment_lag_days": 14,
      "projected_payment_received_date": "2026-03-14",
      "sub_payment_obligations": 280000,
      "sub_payment_timing": "within 3 days of receiving owner payment",
      "gc_net_cash_flow": 30590
    },
    {
      "month": "2026-03",
      "period_start": "2026-03-01",
      "period_end": "2026-03-31",
      "projected_percent_complete": 35,
      "projected_billable_work": 981750,
      "projected_materials_stored": 18500,
      "subtotal_billable": 1000250,
      "retainage_rate": 0.10,
      "projected_retainage": 100025,
      "projected_billing_to_owner": 900225,
      "historical_payment_lag_days": 14,
      "projected_payment_received_date": "2026-04-14",
      "sub_payment_obligations": 820000,
      "sub_payment_timing": "within 3 days of receiving owner payment",
      "gc_net_cash_flow": 80225
    }
  ]
}
```

### Cash Flow S-Curve

Plots planned vs. actual cumulative cash receipts and disbursements:

```json
{
  "cash_flow_curve": {
    "planned_cumulative": [125000, 400000, 980000, 1650000],
    "actual_cumulative": [118000, null, null, null],
    "month": ["Feb", "Mar", "Apr", "May"],
    "variance": [7000, null, null, null],
    "forecast_completion_cost": 2750000,
    "forecast_final_cash_position": "positive"
  }
}
```



## Cost Report Generation

### Monthly Cost Report Structure

```
PROJECT COST SUMMARY — Month Ending [Date]

EXECUTIVE SUMMARY
  Current Contract Amount:        $2,805,000
  Total Spent to Date:            $320,000
  Percent of Budget Spent:        11.4%
  Cost Performance Index:          1.05 (5% under budget)
  Estimated Final Cost (EAC):     $2,671,429
  Projected Savings:              $133,571
  Contingency Remaining:          $115,000
  Status:                         ON TRACK

BUDGET vs ACTUAL BY DIVISION
  [Table showing each division with budget, spent, committed, forecast, variance]

SUB COST SUMMARY
  [Table showing each sub with contract value, spent, retainage, remaining]

CHANGE ORDER SUMMARY
  [Table of all COs with cost impact and status]

CASH FLOW SUMMARY
  [Monthly billing projections, payment receipts]

VARIANCE ANALYSIS
  [Budget variances by division, schedule impact, material costs]

FORECAST ANALYSIS
  [EAC, burn rate, risk assessment]

ALERTS & ACTIONS
  [Any thresholds exceeded, recommended actions]
```



## Data Store Integration

### cost-data.json Structure

```json
{
  "project_code": "MOSC-825021",
  "last_updated": "2026-02-18",
  "budget": {
    "original_contract_value": 2770000,
    "approved_cos_total": 35000,
    "current_contract_value": 2805000,
    "budget_by_division": []
  },
  "actuals": {
    "total_invoiced": 320000,
    "total_paid": 305500,
    "total_retainage_held": 14500,
    "invoices": [
      {
        "invoice_id": "INV-001",
        "from_sub": "W Principles",
        "invoice_date": "2026-02-15",
        "invoice_amount": 120000,
        "csi_division": "03",
        "associated_pay_app": "PAY-001",
        "status": "submitted|approved|paid",
        "payment_date": null,
        "notes": ""
      }
    ]
  },
  "forecasts": {
    "eac_cpi_based": 2671429,
    "eac_revised_estimate": 2506600,
    "eac_burn_rate": 1789648,
    "recommended_eac": 2671429,
    "variance_to_contract": -133571,
    "total_forecast_by_division": []
  },
  "change_order_costs": [],
  "contingency": {},
  "monthly_trends": [],
  "cash_flow": {}
}
```



## Integration Points

### Morning Brief Integration

**Cost Alerts:**
- Display any division with variance > ±5% of budget
- Surface cost overrun trend if CPI < 0.95
- Alert if contingency drawdown > 50%
- Flag pending COs if exposure exceeds available contingency
- Show budget variance for current month

**Example Morning Brief Section:**
```
COST STATUS — As of 2026-02-18

  Overall CPI:                    1.05 ✓ (under budget)
  Estimated Final Cost (EAC):     $2,671,429 ($133,571 savings)
  Contingency:                    $115,000 (77% remaining)

  ALERTS:
    • None currently. Project costs tracking well.

  PENDING COs:
    • CO-002 (Electrical upgrade, $45K, 75% probability) — Exposure: $33.75K
```

### Weekly Report Integration

**Cost Summary Section:**
- Weekly cost recap (new costs, new invoices)
- Month-to-date and year-to-date totals
- CPI trend (week-over-week)
- Contingency burn rate and runway
- Variance by division (top 3 overages and savings)
- Cash flow projection (next 4 weeks)

**Example Weekly Report Section:**
```
COST SUMMARY — Week Ending 2026-02-18

This Week:
  New Invoices:          $45,000
  New Payments:          $38,000

Month-to-Date:
  Invoiced:              $320,000 (11.4% of budget)
  Paid:                  $305,500
  Retainage Held:        $14,500

Variance Highlights:
  Division 02 (Site):    $2,500 under budget ✓
  Division 03 (Concrete): $5,000 over budget ⚠
  Overall CPI:           1.05 (tracking efficiently)

Contingency Burn:
  Used This Month:       $17,800
  Remaining:             $115,000
  Runway:                6.5 months at current burn rate

Next 4 Weeks Forecast:
  Projected Billing:     $290,000
  Projected Payment:     $276,000 (net of retainage)
```

### Pay Application Integration

When `/pay-app` is used, it queries cost-data.json:
- Pre-populate committed costs from procurement-log.json
- Calculate % complete using spend vs budget
- Flag overbilling if invoice exceeds % complete threshold
- Update cost-tracking with paid amounts when pay app is processed

### Change Order Integration

When CO is approved:
- Auto-update budget_by_division for affected divisions
- Update current_contract_value
- Deduct from contingency if owner-directed
- Update forecast_to_complete
- Trigger cost variance recalculation

### Schedule Integration

When schedule changes:
- If milestone delayed: Calculate schedule variance cost impact
- If project accelerates: Update labor/overhead forecast
- Update cash flow projection to reflect new completion date



## Early Warning Thresholds

System alerts superintendent when:

| Alert Level | Trigger | Action |
|-----------|---------|--------|
| **Green** | CPI ≥ 0.95, Variance < ±5% | Continue normal monitoring |
| **Yellow** | CPI 0.90–0.94, Variance ±5–10%, Contingency 50–75% used | Review cause; plan mitigation |
| **Red** | CPI < 0.90, Variance > ±10%, Contingency > 75% used | Escalate to PM/owner; stop discretionary spending |



## Cost Tracking Formulas Reference

**Core Formulas:**

| Formula | Purpose | Example |
|---------|---------|---------|
| CPI = Earned Value / Actual Costs | Cost efficiency index | 1.05 = good |
| EAC = Current Budget / CPI | Estimate at completion | $2.67M ÷ 1.05 |
| Budget Variance = Budget − Forecast | Under/over budget | -$5K = over |
| Contingency Remaining = Original − Used | Reserve funds left | $115K available |
| Daily Overhead = Div 01 / Project Days | Cost per day | $961/day |
| Burn Rate = Spent / Days Elapsed | Spending pace | $11,852/day |
| Overbilling Check = Invoice ≤ (Budget × % Complete) | Invoice validation | OK if < $83,250 |



## Example Monthly Cost Report

**PROJECT COST REPORT — MOSC-825021**
**Period: February 2026 | Date: 2026-02-18**

```
EXECUTIVE SUMMARY
Current Contract:           $2,805,000
Total Spent to Date:        $320,000 (11.4%)
Cost Performance Index:      1.05 ✓
Estimated Final Cost:       $2,671,429
Projected Savings:          $133,571
Contingency Remaining:      $115,000 (77%)
Status:                     ON TRACK

BY DIVISION (Top 5)
Division 01 (Gen Req):      $38K / $145K = 26.2% ✓
Division 02 (Site Work):    $65K / $85K = 76.5% ✓
Division 03 (Concrete):     $87K / $190K = 45.8% ✓
Division 05 (Steel):        $78K / $85K = 91.8% ✓
Division 26 (Electrical):   $52K / $300K = 17.3% ⚠ (PENDING)

CHANGE ORDER IMPACT
Total COs Approved:         $35,000 (1.3% of contract)
Costs Within Contingency:   $17,800 owner-directed
Remaining CO Exposure:      $33,750 (pending COs)

CASH FLOW STATUS
This Month Billings:        $310,590
This Month Payments:        $305,500
Projected Payment Lag:      14 days
Next Month Forecast:        $900,225 billing

ALERTS:
  ✓ No cost overruns
  ✓ CPI healthy at 1.05
  ✓ Contingency in good position
  ⚠ Monitor Division 05 (Steel) closely — 91.8% committed
```



## Data Store Storage Location

- **File**: `{{folder_mapping.ai_output}}/cost-data.json`
- **Section**: Root-level `budget`, `actuals`, `forecasts`, `change_order_costs`, `contingency`, `monthly_trends`, `cash_flow`
- **Related Files**: pay-app-log.json (billing), change-order-log.json (CO costs), procurement-log.json (committed), schedule.json (% complete)
- **Backup**: Timestamped backups in `{{folder_mapping.config}}/backups/cost-data_[TIMESTAMP].json`



## Version History & Audit

- All cost updates logged in project-config.json `version_history`
- Timestamp, source (pay-app, change-order, manual entry), amounts, reason tracked
- Original budget values immutable — history maintained
- Approved CO amounts locked — prevents post-approval drift



## Error Handling & Validation

**Missing Project Setup:**
- Inform user to run `/set-project` first
- Cannot generate cost report without budget baseline

**Invoice Exceeds Budget:**
- Flag overbilling and block payment pending review
- Suggest superintendent confirm % complete

**CPI Calculation Error:**
- If actual costs are zero: Prevent division by zero; show "Insufficient data"
- If percent complete is zero: Show "Project in mobilization; CPI not yet calculable"

**Contingency Overspend:**
- If pending COs exceed available contingency, alert: "Contingency at risk. Recommend owner meeting."
- Prevent approval of new owner-directed COs without contingency availability

**Schedule/Cost Mismatch:**
- If project 20% behind schedule but spending on budget, alert: "Schedule risk may inflate overhead costs."
- Recommend acceleration plan or budget adjustment



## Cost Control Best Practices

1. **Weekly Monitoring** — Review cost report every Friday; address variances same week
2. **Budget Discipline** — No spending outside approved budget or contingency without CO
3. **Early Warnings** — Escalate yellow alerts immediately; don't wait for red
4. **Invoice Accuracy** — Verify every invoice; catch overbilling before payment
5. **Change Control** — Every CO must be approved before work; capture full cost impact
6. **Forecast Discipline** — Update EAC monthly; use multiple methods for confidence
7. **Retainage Management** — Track by sub; ensure release at proper milestones
8. **Contingency Reserve** — Protect contingency for true unknowns; use COs for scope changes

---

**End of Cost Tracking Skill Documentation**


