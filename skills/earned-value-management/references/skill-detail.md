# earned-value-management — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the earned-value-management skill.



## TCPI (To-Complete Performance Index)

**Formula**: TCPI = (BAC - EV) / (BAC - AC)

**Interpretation**: The required cost performance (CPI) needed for remaining work to complete within budget.

**Examples**:

| Scenario | BAC | EV | AC | Remaining Work | Remaining Budget | TCPI | Assessment |
|----------|-----|-----|-----|-----------------|------------------|------|------------|
| On track | $2,805k | $198k | $210k | $2,607k | $2,595k | 1.005 | Achievable; slight recovery needed |
| Moderate overrun | $2,805k | $280k | $305k | $2,525k | $2,500k | 1.010 | Achievable with modest improvements |
| Severe overrun | $2,805k | $280k | $350k | $2,525k | $2,455k | 1.029 | Recovery difficult; needs aggressive corrective action |
| Critical overrun | $2,805k | $280k | $400k | $2,525k | $2,405k | 1.050 | Likely unachievable; project will overrun |

**Construction Decision Rule**:
- TCPI < 1.05: Green — achievable with normal project management
- TCPI 1.05–1.15: Yellow — requires documented corrective actions
- TCPI > 1.15: Red — recovery nearly impossible; escalate to management/client

---



## Alert Thresholds (Green / Yellow / Red)

Use these thresholds to flag project health in dashboards, daily briefings, and reports:

### Schedule Performance Index (SPI)

| Threshold | Status | Action |
|-----------|--------|--------|
| 0.95–1.10 | Green | On schedule; no action required |
| 0.85–0.94 | Yellow | Monitor closely; develop recovery plan if SPI continues to decline |
| <0.85 | Red | Schedule at risk; escalate to management; accelerate remaining work or defer scope |

**Construction context**: For a 151-day project, SPI of 0.90 at 25% completion suggests a ~16-day slip. At 50% completion, SPI of 0.90 suggests ~7-day slip (recoverable). Early detection is critical.

### Cost Performance Index (CPI)

| Threshold | Status | Action |
|-----------|--------|--------|
| 0.95–1.10 | Green | On budget; monitor for continuation |
| 0.85–0.94 | Yellow | Cost overrun; investigate root causes; implement cost control measures |
| <0.85 | Red | Severe overrun; escalate; re-estimate remaining work; consider value engineering |

**Construction context**: CPI <0.90 in foundation/early phases often recovers as work shifts to more predictable construction tasks. CPI <0.90 in rough-in and finishes is more concerning (indicates systemic labor or material issues).

### To-Complete Performance Index (TCPI)

| Threshold | Status | Action |
|-----------|--------|--------|
| <1.05 | Green | Recovery to budget is achievable with normal project management |
| 1.05–1.15 | Yellow | Recovery is difficult; requires documented corrective actions; monitor progress monthly |
| >1.15 | Red | Recovery is nearly impossible; project will likely overrun; escalate to sponsor/client |

**TCPI formula interpretation**:
- TCPI = 1.0: Remaining work must be done at planned rate
- TCPI = 1.10: Remaining work must be done 10% more efficiently than budgeted (to recover the overrun)
- TCPI = 1.20: Remaining work must be done 20% more efficiently (nearly impossible without value engineering or scope reduction)

### Estimate at Completion (EAC) vs. Budget at Completion (BAC)

| Variance | Status | Action |
|----------|--------|--------|
| EAC within 3% of BAC | Green | On track for budget; no action required |
| EAC 3–8% above BAC | Yellow | Potential overrun; implement corrective actions; monitor EAC monthly |
| EAC >8% above BAC | Red | Significant overrun forecast; escalate; prepare change order or budget revision |

**Example**:
- BAC = $2,805,000
- EAC (Month 4) = $3,032,326 (from CPI method)
- VAC = $2,805,000 - $3,032,326 = -$227,326 (8.1% overrun)
- Status: Red (threshold >8%)
- Action: Escalate to management; prepare cost recovery plan; decide on scope deferral

---



## Forecasting Methods in Detail

### 1. CPI-Based Forecasting (Most Common, Conservative)

**Formula**: EAC = BAC / CPI

**Assumption**: Current cost performance continues for all remaining work.

**Advantages**:
- Simple and transparent
- Conservative (tends to overstate cost overrun if project implements corrective actions)
- Works well early in project when trends are uncertain

**Disadvantages**:
- Ignores management intervention (assumes no corrective action)
- Ignores schedule effects on cost
- Can be overly pessimistic

**Use case**: Monthly status reports, quick forecasts, default method in project dashboards.

---

### 2. Remaining Work at Original Rate (Optimistic)

**Formula**: EAC = AC + (BAC - EV)

**Assumption**: Remaining work will be completed at the original budgeted efficiency (CPI = 1.0).

**Advantages**:
- Reflects management confidence in corrective actions
- Realistic if cost overrun root causes are one-time (e.g., soil remediation complete)
- Less pessimistic than CPI method

**Disadvantages**:
- Often unrealistic unless root causes are truly addressed
- Can be misleading if overrun is systemic (labor inefficiency, material escalation)

**Use case**: When documented corrective actions exist (e.g., "labor productivity improved from 0.90 to 1.05 in Month 4").

---

### 3. Composite Forecasting (CPI × SPI) — Schedule + Cost

**Formula**: EAC = AC + [(BAC - EV) / (CPI × SPI)]

**Assumption**: Remaining work will be completed at a combined rate influenced by both cost and schedule performance.

**Advantages**:
- Most realistic for construction projects
- Reflects that schedule delays extend general conditions, overhead, and crew inefficiency
- Captures the interaction between schedule and cost

**Disadvantages**:
- Requires accurate SPI calculation (schedule data must be reliable)
- Can be pessimistic if project is already implementing schedule recovery (added crew)

**Use case**: Mid-to-late project phases; detailed cost/schedule integration analysis.

**Construction example**:
- SPI = 0.90 (10% behind schedule)
- CPI = 0.92 (8% over budget)
- Combined: 0.90 × 0.92 = 0.828
- Means: "For every $1 of remaining work, we're spending $1.21 and earning only 0.828 worth of progress"
- EAC will be significantly higher than BAC, justifying aggressive corrective action

---

### 4. Bottom-Up Re-Estimate (Manual Override)

**When to use**: Mid-to-late project phases when actual productivity/costs are well-established.

**Method**:
1. Review remaining work scope (not yet started + in-progress tasks)
2. Re-estimate cost for each remaining work package using actual productivity rates
3. Sum the re-estimates to get "Estimate to Complete" (ETC)
4. EAC = AC + ETC

**Advantages**:
- Most accurate if detailed re-estimation is performed carefully
- Reflects learned lessons and updated market conditions
- Can incorporate recent cost data (labor rates, material pricing)

**Disadvantages**:
- Labor-intensive (requires estimator/superintendent review)
- Subjective (can be influenced by optimism bias)
- Time-consuming for large projects

**Use case**: Formal cost/schedule reviews; significant change events; mid-project re-baselining.

---

### 5. Range Forecasting (Optimistic / Most Likely / Pessimistic)

**Method**: Calculate three EAC scenarios to establish a confidence range.

| Scenario | Assumption | Typical Formula | Example (MOSC Month 4) |
|----------|-----------|-----------------|------------------------|
| **Optimistic** | Corrective actions fully effective; SPI/CPI improve to 0.98 | EAC = AC + (BAC - EV) / 0.98 | $2,895,000 |
| **Most Likely** | Composite forecast; current trends continue | EAC = AC + (BAC - EV) / (CPI × SPI) | $3,032,326 |
| **Pessimistic** | No improvement; CPI worst-case | EAC = AC + (BAC - EV) / 0.92 | $3,125,000 |

**Decision rule**: Report the most likely EAC, but flag if pessimistic scenario exceeds 10% variance (material impact on client).

---



## Monthly EVM Report Template

### Executive Summary

*One paragraph synthesizing project health across schedule, cost, and forecast.*

Example:
"The project is 27.4% complete (by AC) as of February 28, 2026. Schedule performance is below baseline (SPI = 0.951; 1-week slip accumulated due to weather and ground condition discovery). Cost performance is also below baseline (CPI = 0.928; overrun of $25,000 or 2.5% of work completed). Combined schedule and cost trends forecast an EAC of $3,145,623 (CPI × SPI method), representing a potential $340,623 overrun (12.1% above BAC). This is primarily driven by foundation work delays (3 days) and concrete admixture cost escalation (+2.5%). Corrective actions in progress: (1) Alexander Construction crew added 3/1 for PEMB acceleration; (2) EKD scheduled to start framing on 3/15. Forecast shows SPI recovery to 0.96+ by Month 4 and CPI stabilization at 0.93–0.95 if no additional scope changes. ETC = $2,800,258; TCPI = 1.021 (achievable with documented actions)."

### Key Metrics Table

| Metric | Current Period | Month-over-Month | Status | Target |
|--------|---|---|---|---|
| **Schedule Variance (SV)** | -$16,600 | -16.6% vs. Month 1 | Yellow | $0 ± $10k |
| **Cost Variance (CV)** | -$25,000 | -1,325% vs. Month 1 | Yellow | $0 ± $5k |
| **Schedule Performance Index (SPI)** | 0.951 | -4.9% vs. Month 1 | Yellow | 0.95–1.10 |
| **Cost Performance Index (CPI)** | 0.928 | -6.1% vs. Month 1 | Yellow | 0.95–1.10 |
| **Estimate at Completion (EAC)** | $3,145,623 | +10.8% vs. Month 1 | Red | $2,805,000 |
| **Variance at Completion (VAC)** | -$340,623 | Worsening | Red | $0 ± $84,150 |
| **To-Complete Performance Index (TCPI)** | 1.021 | +1.8% vs. Month 1 | Yellow | <1.05 |

### S-Curve Chart

*Include Chart.js configuration for three-line S-curve (PV, EV, AC) with cumulative cost (Y-axis) vs. date (X-axis). See Chart.js section below.*

### Variance Analysis

**Top 3 Schedule Drivers (Negative SV)**:
1. Foundation excavation and footing work: 3-day slip due to wet ground conditions (clay with 18% moisture vs. design 16%). Terracon performed compaction test on 2/15; required re-work of east portion. Recovery: Walker added crew 2/18; expected recovery by 2/28.
2. Anchor bolt template verification hold point: Surveyor delayed verification from 2/24 to 2/28 (4-day wait). Nucor PEMB delivery remains on 3/5 track.
3. Stem wall inspection: Building Official backlog caused 2-day delay in scheduling inspection. Rescheduled for 3/3.

**Top 3 Cost Drivers (Negative CV)**:
1. Concrete admixture escalation: Wells Concrete RSA-10 air entrainer cost increased $0.45/CY due to supply shortage (expected 2-3 weeks). Affects 350 CY of footing concrete and 800 CY of SOG. Impact: ~$22,500 on current and planned pours.
2. Rework on east footing: Compaction test failure required partial excavation and re-compaction. Labor: +$8,000. Disposal/remediation: +$3,500.
3. Subcontractor labor rate adjustment: Walker Construction requested labor rate adjustment (market-driven crew wage increase) effective 2/15. Approved at $0.50/hr increase per ASI #2. Affects remaining excavation work (~1,200 labor hours). Impact: +$600/week for 4 weeks = $2,400 additional cost.

**Corrective Actions in Progress**:
1. **Crew acceleration (PEMB)**: Alexander Construction 4-man crew added 3/1 to compress PEMB erection from 19 days to 15 days (4-day save). Estimated cost: $12,000 for overtime and expediting.
2. **Alternative concrete mix**: Working with Wells to substitute RSA-20 air entrainer ($0.15/CY savings) effective March pours. Estimated savings: $9,600 on 800 CY SOG.
3. **EKD mobilization early**: Scheduled CFS framing start on 3/15 (5 days earlier than baseline 3/20). Requires temporary scaffolding (+$4,000) but recovers 5 days from downstream schedule. Net recovery: 3–4 days after accounting for ramp-up.

### Forecast Narrative

As of February 28, combined schedule and cost trends point to a project completion cost of approximately $3.14M (using CPI × SPI composite method), representing a $340k overrun above the $2.805M baseline. The overrun is primarily driven by foundation schedule delays (3 days, extending general conditions by ~$18k) and concrete cost escalation (admixture shortage, estimated $22.5k impact through SOG completion).

The good news: SPI is recovering (0.951 in Month 2, improving from 1.00 baseline if we exclude the 3-day slip). If the Alexander Construction crew adds 4 days of schedule recovery in March PEMB phase, SPI could return to 0.96–0.97 by Month 4, reducing EAC by approximately $100k.

Cost-wise, CPI remains stable at 0.928. If admixture costs normalize in April (supply expected to ease) and rework is complete, CPI could improve to 0.94–0.95, further reducing EAC by $50–75k.

**Best case (optimistic)**: EAC = $2,920k (if SPI and CPI both improve 2–3%)
**Most likely**: EAC = $3,032k (CPI-only method; schedule recovery partial)
**Worst case (pessimistic)**: EAC = $3,145k (current trends; no improvement)

**Management decision point**: If EAC exceeds $3.05M in Month 3, recommend escalation to client with three options: (1) approve budget increase, (2) defer finishes scope to Phase 2, or (3) reduce quality/spec in negotiation with owner. TCPI = 1.021 is still achievable but leaving little room for error.

---



## Command: /evm

The earned-value-management skill exposes the following commands:

### /evm status

**Purpose**: Display current period EVM metrics snapshot.

**Output**:
```
═══════════════════════════════════════════════════════════════
  EARNED VALUE MANAGEMENT STATUS — 2026-02-28
═══════════════════════════════════════════════════════════════

PROJECT: Morehead One Senior Care (Job #825021)
BASELINE: 01/21/26 — 07/29/26 (151 days) | BAC: $2,805,000

PROGRESS SNAPSHOT:
  Planned Value (BCWS):     $336,600 (12.0% complete)
  Earned Value (BCWP):      $320,000 (11.4% complete)
  Actual Cost (ACWP):       $345,000 (12.3% expended)

PERFORMANCE METRICS:
  Schedule Variance (SV):    -$16,600    [YELLOW]
  Schedule Index (SPI):       0.951       [YELLOW]

  Cost Variance (CV):        -$25,000    [YELLOW]
  Cost Index (CPI):           0.928       [YELLOW]

FORECAST:
  EAC (CPI method):         $3,021,258
  EAC (Remaining rate):     $2,808,000
  EAC (CPI × SPI):          $3,145,623
  Most Likely EAC:          $3,032,326  [RED — 8.1% overrun]

  ETC (Estimate to Complete): $2,687,326
  VAC (Variance at Completion): -$227,326
  TCPI (Required CPI):       1.021      [YELLOW]

INTERPRETATION:
  Project is 2.6% behind schedule and 7.2% over budget to date.
  EAC of $3.03M forecasts $227k overrun (12.1% of work complete).
  Recovery is achievable (TCPI 1.021 < 1.05 threshold).

  Root causes: Foundation delays (weather, soil), concrete cost escalation.
  Corrective actions: Crew acceleration PEMB 3/1, alternative concrete mix March.

═══════════════════════════════════════════════════════════════
```

---

### /evm report [month]

**Purpose**: Generate comprehensive monthly EVM report (as per template above).

**Example**: `/evm report 2026-02`

**Output**: Full report (as shown in "Monthly EVM Report Template" section) in PDF or HTML format, ready for management distribution.

---

### /evm forecast

**Purpose**: Show EAC projections using all three methods, with range and confidence.

**Output**:
```
═══════════════════════════════════════════════════════════════
  EAC FORECAST — All Three Methods
═══════════════════════════════════════════════════════════════

SCENARIO 1: CPI-Based (Current Trend Continues)
  Formula: EAC = BAC / CPI
  EAC = $2,805,000 / 0.928 = $3,021,258
  VAC = -$216,258 (7.7% overrun)
  [Conservative; assumes no improvement]

SCENARIO 2: Remaining Work at Original Rate
  Formula: EAC = AC + (BAC - EV)
  EAC = $345,000 + ($2,805,000 - $320,000) = $2,830,000
  VAC = -$25,000 (0.9% overrun)
  [Optimistic; assumes corrective actions work]

SCENARIO 3: Composite (CPI × SPI)
  Formula: EAC = AC + [(BAC - EV) / (CPI × SPI)]
  EAC = $345,000 + [$2,485,000 / 0.830] = $3,143,373
  VAC = -$338,373 (12.1% overrun)
  [Realistic; schedule + cost interaction]

CONFIDENCE RANGE:
  Optimistic (Scenario 2):    $2,830,000 (0.9% overrun)
  Most Likely (Scenario 3):   $3,143,373 (12.1% overrun)
  Pessimistic (Scenario 1):   $3,021,258 (7.7% overrun)

  Range: $2.83M — $3.14M (±4.6% confidence band)

RECOMMENDATION:
  Report Most Likely EAC of $3.14M to stakeholders.
  If composite EAC exceeded $3.05M by Month 3, escalate for approval.
  Monitor admixture costs and PEMB schedule recovery closely in March.

═══════════════════════════════════════════════════════════════
```

---

### /evm trend

**Purpose**: Show SPI and CPI trend over all completed periods.

**Output**: Line chart showing SPI and CPI trajectory Month 1 through current.

```
SPI TREND:
  Month 1: 1.00 (on schedule)
  Month 2: 0.951 (slightly behind)
  Month 3: 0.904 (catching up?)
  Month 4: 0.963 (improving)

CPI TREND:
  Month 1: 0.988 (slightly over budget)
  Month 2: 0.928 (overrun detected)
  Month 3: 0.925 (stable overrun)
  Month 4: 0.926 (slightly improving)

ANALYSIS:
  SPI shows W-shaped pattern: dip in Month 2 (foundation delay),
  recovery in Month 4 (PEMB acceleration crew). If trend continues,
  SPI could reach 0.97+ by Month 5 (on track for substantial completion).

  CPI is stable around 0.926 (on a cost efficiency plateau).
  Indicates systemic cost drivers (admixture, rework) not yet resolved.
  Alternative concrete mix (March) and rework completion should lift CPI
  to 0.94+ by Month 5.
```

---

### /evm update

**Purpose**: Input current period EV and AC data to refresh calculations.

**Interactive form**:
```
Enter EVM Data for Period: 2026-02-28

Planned Value (BCWS) $ [  336,600   ]
Earned Value (BCWP)  $ [  320,000   ]
Actual Cost (ACWP)   $ [  345,000   ]
Percent Complete (%) [  11.4       ]

Notes: [Foundation delayed 3 days. Concrete cost +$22.5k. Recovery crew added 3/1.]

[SUBMIT]

Calculations updated. Metrics recalculated.
SPI: 0.951, CPI: 0.928, EAC: $3,032,326, TCPI: 1.021
Status: YELLOW (SV: -$16.6k, CV: -$25k)
```

---

### /evm baseline

**Purpose**: Set or reset the baseline plan (PV curve).

**Options**:
- `/evm baseline set [schedule.json]` — Import baseline schedule with cost allocation
- `/evm baseline reset` — Return to original approved baseline
- `/evm baseline rebase [change-order-adjustment]` — Re-baseline after approved scope change

**Use case**: When major scope changes occur, re-baselining ensures EVM comparisons are valid. Without re-baselining, approved scope increases would artificially inflate EV and AV metrics.

---



## Integration Points with Other Skills

### 1. cost-tracking skill

**Relationship**: Earned-value-management extends cost-tracking by adding schedule integration.

**Data flow**:
- Cost-tracking provides: BAC, actual costs by cost code/CSI division, spending rates
- EVM adds: Schedule integration, planned value curve, SPI/CPI calculations, forecasting
- Result: Unified three-dimensional performance view

**Use**: Monthly cost report includes EVM section (SPI, CPI, EAC, S-curve).

---

### 2. look-ahead-planner skill

**Relationship**: Flags look-ahead items at risk based on SPI trends.

**Integration**:
- If SPI < 0.90 at any point, look-ahead highlights high-risk upcoming work
- Suggests crew acceleration, resource reallocation, or scope deferral
- EVM trend line indicates whether delays are recoverable

---

### 3. project-dashboard skill

**Relationship**: Dashboard includes new EVM section alongside cost/schedule tabs.

**Dashboard widgets**:
- SPI / CPI gauges (green/yellow/red)
- S-curve interactive chart (zoom, data-table toggle)
- EAC forecast table (three methods)
- VAC / TCPI trending
- Monthly variance drivers (top 3 schedule, top 3 cost)

---

### 4. weekly-report-format skill

**Relationship**: Weekly reports include 2-sentence EVM health summary.

**Example**:
"Schedule performance at 0.951 (1-week slip accumulated). Cost performance at 0.928 (8.1% overrun to date). EAC forecast: $3.03M (+$227k over BAC). Corrective actions: PEMB crew acceleration 3/1, alternative concrete mix March."

---

### 5. morning-brief skill

**Relationship**: Daily brief includes EVM status indicator.

**Example**:
"[EVM: YELLOW] SPI 0.951 | CPI 0.928 | EAC $3.03M"

---

### 6. change-order-tracker skill

**Relationship**: Approved COs trigger BAC re-baseline in EVM.

**Integration**:
- When CO-001 ($250k) is approved, BAC updates from $2,805,000 to $3,055,000
- All subsequent EV/SV/CV calculations use new BAC
- Historical data preserved (baseline vs. re-baseline tracking)

---

### 7. labor-tracking skill

**Relationship**: Labor cost component feeds AC in EVM.

**Integration**:
- Weekly timesheets → labor cost summary → AC (labor portion)
- Combined with material costs and subcontractor invoices to calculate total AC
- Labor productivity metrics (hours/task) inform SPI/CPI variance analysis

---

### 8. pay-application skill

**Relationship**: Percent complete and billed amounts feed EV/AC.

**Integration**:
- Pay application Line 1 (Foundation): 85% complete, $180k budgeted → EV = $153k
- Pay application Line 2 (PEMB): 0% complete, $275k budgeted → EV = $0
- Actual invoice amounts feed AC
- Monthly consolidation of all line items generates total EV and AC

---



## Percent Complete Methods (Detailed)

EVM accuracy depends entirely on accurate percent complete assessment. Foreman OS supports four methods:

### 1. Weighted Milestones (Preferred for Construction)

**Method**: Assign percent complete based on achieving discrete, measurable milestones.

**Example (Foundation phase)**:
- Excavation complete: 20% of phase
- Footing rebar inspection approved: +10% (total 30%)
- Footings concrete placed: +15% (total 45%)
- Stem walls rebar inspection approved: +5% (total 50%)
- Stem walls concrete placed: +20% (total 70%)
- Anchor bolt template verification: +10% (total 80%)
- Backfill and final grading: +20% (total 100%)

**Advantages**:
- Objective (milestone either achieved or not)
- Aligns with contract requirements and inspections
- Reflects actual work scope

**Disadvantages**:
- Requires careful milestone definition upfront
- Must be calibrated against similar historical phases

---

### 2. Units Completed / Total Units

**Method**: Track physical units completed vs. total units for the activity.

**Example**:
- Masonry: 3,200 SF laid of 8,500 SF total = 37.6% complete
- Electrical panels: 2 of 3 panels installed = 66.7% complete
- Drywall: 12,400 LF of 18,600 LF hung = 66.7% complete

**Advantages**:
- Highly objective (units are measurable)
- Easy to verify in the field

**Disadvantages**:
- Not all work is easily quantified (coordination, inspection, rework)
- Can be misleading if units don't reflect cost curve (e.g., first unit takes 40%, last unit takes 10%)

---

### 3. Cost Ratio (Work Completed / Estimated Cost at Completion)

**Method**:
- Track actual costs incurred to date
- Divide by the total estimated cost for the activity
- Percent complete = (Cost to date) / (Total estimated cost) × 100%

**Example**:
- Labor cost to date: $45,000
- Material cost to date: $20,000
- Total cost to date: $65,000
- Total estimated cost for activity: $120,000
- Percent complete = 65,000 / 120,000 = 54.2%

**Advantages**:
- Objective (cost is hard financial data)
- Works for any type of activity

**Disadvantages**:
- Assumes cost is proportional to progress (not always true if rework or inefficiency present)
- Can overstate progress if early costs spike (equipment delivery)

---

### 4. Level of Effort (Time-Based)

**Method**: For support activities (project management, quality, safety), assign percent complete based on time elapsed.

**Example**:
- Project Manager effort: Budgeted for 26 weeks (full project duration)
- After 6 weeks: Percent complete = 6 / 26 = 23.1%
- Quality Manager effort: Budgeted for 20 weeks
- After 6 weeks: Percent complete = 6 / 20 = 30%

**Advantages**:
- Simple (time elapsed is objective)
- Appropriate for activities with undefined physical output

**Disadvantages**:
- Assumes effort is linear throughout project
- Can hide productivity issues (PM could be ineffective despite time passing)

---

### 5. Superintendent Estimate (With Calibration)

**Method**: Field superintendent provides weekly % complete estimate for each work package, reviewed/approved by PM.

**Calibration**:
- Compare superintendent estimate to other methods (milestone, cost ratio) monthly
- Flag discrepancies >5%
- Document rationale for differences
- Use multiple methods to triangulate a defensible % complete

**Advantages**:
- Reflects field reality and judgment
- Can incorporate subjective factors (safety, quality, coordination)

**Disadvantages**:
- Subjective (open to bias)
- Requires disciplined calibration against objective metrics

---



## EVM for Construction — Special Considerations

### 1. Weather Impacts on SPI

In construction, weather is a primary driver of schedule performance. EVM interpretation must account for weather context:

**Scenario A: Weather-Caused Delay (Not Recoverable)**
- Baseline plan: 151-day schedule
- Weather delays: 8 days (winter project, multiple freeze-thaw cycles)
- If delays are unavoidable, should SPI be penalized?

**Guidance**:
- **Option 1**: Keep baseline unchanged; report SPI <1.0; document weather reason in notes. This shows true schedule variance.
- **Option 2**: Adjust PV for documented weather delays (extend baseline); report SPI near 1.0. This isolates project management performance from weather.

**Foreman OS approach**: Option 1 (maintain baseline integrity). Use "weather notes" field to distinguish weather delays from project-management delays. In monthly briefing, report both "SPI including weather" and "SPI excluding weather" for transparency.

---

### 2. Change Order Handling and Re-Baselining

A change order creates three decisions:

**Decision 1: Approved Scope Change**
- Add to BAC (new baseline budget)
- Create new baseline plan (PV) incorporating CO scope, cost, and schedule
- Reset EV/AC calculation from CO effective date

**Example**:
- Original BAC: $2,805,000
- CO #1: $250,000 additional scope (extra 10 bedrooms)
- New BAC: $3,055,000
- Decision: Adjust PV for additional scope; reset baseline

**Decision 2: Disputed Change (Pending)**
- Do NOT include in BAC yet
- Track separately in "pending changes" log
- Report two EAC scenarios: "with pending changes" and "without pending changes"

**Decision 3: Change Order Backlogs**
- If design changes are in process but not yet authorized, track as "design contingency" separate from EVM
- Once authorized, flow into BAC/PV/EV

---

### 3. Retainage and Front-Loaded Billing

Retainage (typically 10%) withheld from subcontractor invoices creates a timing mismatch between EV and AC:

**Scenario**:
- Subcontractor invoice: $100,000 for foundation work (60% complete)
- Retainage (10%): $10,000 withheld
- Billed amount: $90,000 (payment made to sub)
- Invoice recorded as: EV = $100,000, AC = $100,000 (full commitment, even though only $90k paid)

**Guidance**:
- Record AC at full invoice amount (true cost commitment)
- Retainage is recorded as a liability, released at project completion
- This ensures EVM reflects true project cost, not cash flow timing

---

### 4. Front-Loaded Long-Lead Delivery

Materials with long lead times often create front-loaded cost curves (early spending, late work completion). Example:

- PEMB order: $275,000 (15% of project cost)
- Order placed Month 1, delivery Month 3
- Invoice and payment: Month 2 (AC spikes)
- Work performed (PEMB erection): Month 3–4

**EVM effect**:
- Month 2: AC = $275,000 (PEMB billed), but EV only $80,000 (other work)
- CPI Month 2 = 80k / 275k = 0.29 (severely skewed)
- Misrepresents project cost performance

**Guidance**:
- Use "milestone-based billing" for long-lead items: bill 50% at order, 50% at delivery
- Or defer AC recognition to work performance date (not invoice date)
- Or normalize EVM reporting by excluding one-time front-load spikes (note in monthly report)

---



## Error Handling and Validation

### Division by Zero Prevention

If PV or AC equals zero, SPI/CPI calculations fail:

**Safeguards**:
- If PV = 0: Check that project is not in pure planning phase; if so, defer SPI calculation until first work begins
- If AC = 0: If project has started but no costs recorded, flag as data entry error
- If EV = 0: Possible if project is 0% complete (valid in early phases); SPI = 0/PV = 0 (undefined)

**Foreman OS handling**: Return "N/A" or "Not Applicable" for SPI/CPI if denominator is zero. Flag in data validation report.

---

### Negative EV Checks

EV should never be negative. If EV < 0 is calculated:
- Root cause: Negative percent complete (entered in error)
- Fix: Validate percent complete data; correct to 0 or positive value
- Alert: Flag in system with "Please review percent complete entries"

---

### SPI > 1.5 Warning

An SPI of 1.5 or higher is rare and suggests possible measurement error:

**Scenarios that could cause SPI > 1.5**:
- Percent complete is inflated (superintendent report overstates progress)
- PV is understated (baseline schedule was very conservative)
- Change orders added scope at lower cost (new scope pulls down blended rate)

**Foreman OS handling**: Alert user when SPI > 1.5: "Verify percent complete data for accuracy. SPI of 1.5+ is unusual and may indicate measurement error."

---

### EAC < AC Warning

EAC should never be less than AC (Estimate at Completion cannot be less than Actual Cost to date):

**Scenarios that could cause EAC < AC**:
- Re-baseline reduced BAC significantly
- Major scope was deleted
- Formula error in EAC calculation

**Foreman OS handling**: Alert user if EAC < AC: "EAC ($X) is less than AC ($Y). This is mathematically inconsistent. Review BAC re-baselining decisions and change orders."

---



## Best Practices for EVM in Construction

### 1. **Establish Strong Baselines**
- Cost-load the baseline schedule by activity (not just by phase)
- Allocate at least 80% of BAC to specific work activities; reserve 20% for overhead, contingency, management reserve
- Validate baseline with project team before kickoff

### 2. **Consistent Percent Complete Methodology**
- Choose one primary method (e.g., weighted milestones) for all activities
- Calibrate monthly against 1–2 secondary methods (cost ratio, units complete)
- Document and archive percent complete assessment rationale
- Never retroactively change percent complete for prior periods

### 3. **Monthly EVM Discipline**
- Close out EVM data within 5 business days of month-end
- Hold monthly EVM review meeting with PM, estimator, superintendent, and finance
- Discuss variances > 3% and take corrective action
- Trend SPI/CPI month-over-month to identify patterns early

### 4. **Separate Schedule Recovery from Cost Recovery**
- If schedule recovery requires additional crew (crash cost), model the cost impact separately
- Don't assume schedule improvement will automatically improve CPI (it may worsen if recovery crew is less efficient)
- Track cost of schedule recovery as a change order (approved or pending)

### 5. **Use Multiple EAC Methods**
- Always calculate CPI-based and composite (CPI × SPI) EAC
- Compare the two; if they diverge by >5%, investigate why (schedule or cost issue?)
- In reports, present all three methods with explanation of most likely scenario

### 6. **Communicate Clearly to Non-Technical Stakeholders**
- Avoid jargon; explain SPI/CPI as "earning per dollar spent"
- Use S-curves visually; three lines tell the story instantly
- Focus on actionable insights: "SPI 0.90 means 10% behind schedule; we need recovery crew by March 15"
- Be honest about variances; don't downplay overruns

### 7. **Integrate with Change Management**
- When change orders are proposed, run EVM impact: "How will this affect EAC?"
- For approved COs, re-baseline only if scope, cost, or schedule changes materially (>5% of BAC)
- Maintain historical baselines for post-project analysis and dispute resolution

### 8. **Account for Inflation and Escalation**
- If material prices or labor rates increase after baseline, adjust baseline or track separately
- EVM formula assumes consistent cost; inflation will inflate CV even if project is well-managed
- Document inflation/escalation impact separately from project management performance

### 9. **Use EVM for Forecast, Not Blame**
- EVM is a diagnostic tool, not a blame tool
- Use variances to identify problems early and solve them
- Avoid punitive response to yellow/red metrics; focus on root cause and corrective action
- Build trust: transparent reporting attracts early action, not defensive behavior

### 10. **Archive and Learn**
- Retain all monthly EVM reports and raw data post-project
- Compare final EAC to actual final cost; calibrate future estimates
- Analyze top cost drivers (what actually caused overruns?)
- Use lessons learned to refine baseline estimates on future projects

---



## Summary

Earned Value Management transforms construction cost and schedule tracking from two separate silos into a unified, integrated analytical framework. By measuring progress in dollars (EV vs. PV and AC), EVM reveals whether cost overruns are due to inefficiency, schedule delays, scope growth, or a combination.

The three-line S-curve instantly communicates project health to any stakeholder: Are we ahead or behind? Over or under budget? What will it cost to finish? EVM answers these questions with mathematical rigor, enabling proactive management decisions before crises emerge.

For a 151-day, $2.8M healthcare project like MOSC, EVM-driven monthly reviews can identify an 8% cost overrun and 10-day schedule slip within the first two months—time enough to implement corrective actions (crew acceleration, value engineering, scope deferral) before the project spirals out of control.

Foreman OS EVM skill integrates seamlessly with cost-tracking, scheduling, and change management, providing the unified intelligence necessary for data-driven project leadership.

---

**Foreman OS EVM Skill v1.0.0**
*Unified scope-schedule-cost performance management for construction.*



