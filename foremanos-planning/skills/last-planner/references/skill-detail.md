# last-planner — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the last-planner skill.



## Variance Categories: The Nine Sources of Incomplete Work

When a commitment is not met, assign a variance category. Track these over time to identify root causes and implement prevention.

### 1. Prerequisites Variance
**Definition**: Prior work was not complete, inspected, or accepted when downstream work was scheduled.

**Common Examples**:
- Footing not cured enough before stem wall
- Building Official inspection failed; rework required before next phase
- Prior trade's work not accepted by other trades or owner
- Scaffold not in place for trade to access work area

**Root Cause Patterns**:
- Poor sequence planning; insufficient lead time between phases
- Inspections scheduled too late; discovered problems delay completion
- Poor coordination between trades on handoff criteria

**Prevention**:
- Build mandatory inspection time into lookahead plan (minimum 1-2 days after completion)
- Specify "ready date" and acceptance criteria in prior week's commitment
- Assign inspection owner (Super, GC, or sub) with accountability
- Create a "prerequisite clearance" checklist reviewed in daily huddles

---

### 2. Material Variance
**Definition**: Required material was not on site, or was not inspected/approved in time for the work.

**Common Examples**:
- Concrete batch delayed; pour moved 1 week
- Door hardware submittals overdue; can't finalize door install
- Steel rebar wet from rain; can't tie until dry
- Drywall delivery missed; crew has no work

**Root Cause Patterns**:
- Submittals not approved on time (design constraint, not material)
- Supplier lead times underestimated in procurement
- Receiving and inspection not coordinated with work schedule
- No expediting when supply chain delays detected

**Prevention**:
- Material-tracker skill: pull material status into weekly planning; verify each material constraint explicitly
- Establish delivery window 2-3 days before planned use (buffer for inspection)
- Weekly supplier check-in call: confirm delivery dates
- Implement escalation trigger: if delivery within 7 days and NOT confirmed, notify PM for expediting
- Create "material ready" sign-off on the Weekly Work Plan (foreman confirms material on site, inspected, and ready)

---

### 3. Labor Variance
**Definition**: Crew was not available, too small to accomplish the task, or not qualified/trained for the work.

**Common Examples**:
- Crew called to other project by contractor
- Foreman absent without backup supervision
- Crew size underestimated; 2 carpenters can't finish framing in 1 day
- Crew not oriented on MEP install procedures; quality issues halt work
- Crew lack trade card or license (electrician apprentice not yet licensed)

**Root Cause Patterns**:
- No labor-tracker integration; crew headcount assumptions not verified
- Competing projects or other GC work pulling crews
- Foreman overcommitted across multiple projects
- Insufficient worker training/orientation program

**Prevention**:
- labor-tracking skill: pull crew availability into planning; no commitments without confirmed crew
- Create a "crew briefing" requirement in the commitment (QC, safety, sequence walkthrough)
- Require foreman sign-off on crew size and qualification
- Build 10% "flex crew" into schedule for absences
- Use daily huddle to confirm crew presence; adjust commitment same-day if needed

---

### 4. Equipment Variance
**Definition**: Required equipment was not available, operational, or scheduled for the work dates.

**Common Examples**:
- Crane double-booked; not available for framing erection
- Concrete batch plant breakdown on pour day
- Scaffolding delivery delayed 1 week
- Generator fails; MEP tools can't run
- Forklift tire flat; material handling delayed

**Root Cause Patterns**:
- Equipment reservations not made with sufficient lead time
- No daily equipment inspection; failures catch contractors off-guard
- Backup equipment not identified for critical tasks
- Weather delays push equipment need; not rescheduled

**Prevention**:
- Equipment checklist in lookahead plan: identify all equipment needed 6 weeks out
- Weekly equipment status review: is equipment on site? Inspected? Reserved for the correct dates?
- Identify backup equipment sources for crane, batch plant, generators, lifts
- Daily equipment inspection routine (checklist, photos)
- Equipment operator certification verified in crew roster

---

### 5. Design Variance
**Definition**: Drawings were not current, RFIs were unanswered, or critical design details were missing or unclear.

**Common Examples**:
- Framing crew can't start; CFS stud size RFI still pending from structural engineer
- Door hardware schedule not issued; can't finalize hardware selections
- MEP coordination drawing incomplete; trades don't know where to stub penetrations
- Change order details not finalized; crew doesn't know new scope

**Root Cause Patterns**:
- Submittals not processed on time (see Variance #5, Design Constraint)
- Insufficient coordination between design disciplines pre-construction
- RFIs answered too late in the process; crews already have material staged
- Change orders not documented in drawings; confusion on what's new vs. existing scope

**Prevention**:
- drawing-control skill: maintain issue log of drawing revisions and RFI responses
- Require design constraint check in Step 2 (Constraint Screening): "Is drawing current as of [date]? Are all RFIs answered?"
- Establish RFI turnaround SLA: 3 business days minimum, 5 days target
- Weekly design status meeting (Thu morning) to review pending RFIs and submittals
- Create a "Design Ready Checklist" for each phase (example: CFS framing phase must have Sheets S-3.1 to S-3.5, all details in place, no outstanding RFIs)

---

### 6. Weather Variance
**Definition**: Weather conditions prevented work as planned (temperature, rain, wind, extreme cold).

**Common Examples**:
- Heavy rain Tue-Wed; excavation and SOG placement postponed
- Frost in ground; can't excavate frozen soil
- Wind >25 mph Wed; PEMB erection paused (safety requirement)
- Below 40°F; concrete pour delayed until temp rises
- High humidity prevents sealant cure; door install paused

**Root Cause Patterns**:
- Weather not forecast far enough out during lookahead planning
- No weather buffer built into schedule
- Outdoor work scheduled without contingency
- Temperature or precipitation thresholds in specifications not respected

**Prevention**:
- Check 7-day forecast during weekly planning; identify weather risk tasks
- Build 1-2 day buffer into all outdoor-dependent work
- Establish "backup indoor work" list (material staging, shop assembly, training) for rainy days
- Verify temperature thresholds for each material (concrete, sealants, coatings)
- Implement weather decision trigger: if forecast predicts below-threshold conditions, pause planning until conditions clear

---

### 7. Space/Access Variance
**Definition**: Work area was not clear, or temporary access (ramps, stairs, scaffolding) was not in place.

**Common Examples**:
- Drywall crew can't start; CFS framing not complete, still staged in work area
- HVAC crew can't run ductwork; MEP rough-in electrical panel not yet moved out of mechanical room
- Window install blocked; exterior scaffold not yet erected (scaffolding sub delayed)
- Material pile blocking crane path; forklift operator can't stage materials efficiently

**Root Cause Patterns**:
- Trades work too close together; poor sequencing and coordination
- Temporary facilities (scaffold, stairs, ramps, power distribution) not scheduled as dependencies
- Material staging plan not communicated; materials block work areas
- Poor site logistics planning; no dedicated material receipt and staging area

**Prevention**:
- Create a "Site Logistics Plan" identifying material staging, temporary access routes, equipment staging
- In lookahead planning, explicitly schedule temporary facilities (scaffolding, stairs, ramps) as predecessors
- Daily huddle includes space/access check: "Is the work area clear for today's planned task?"
- Coordinate with site supervision on end-of-day cleanup; no clutter left in work paths
- Site plan shows material staging zones; enforce discipline (no materials left in walkways or work areas)

---

### 8. Rework Variance
**Definition**: Work had to be redone due to quality issues, code violations, or interface problems discovered post-completion.

**Common Examples**:
- Footing rebar spacing wrong; Building Official rejects; must retie all connections
- Concrete finish poor; surface not acceptable; grind and patch required
- MEP penetrations not coordinated; holes in wrong places; must cut new holes
- CFS framing misaligned; connection bolts won't fit; studs repositioned

**Root Cause Patterns**:
- Insufficient quality planning or inspection before moving to next phase
- Poor coordination between trades (e.g., MEP not consulted before framing installed)
- Crew not trained on specifications or sequencing
- Drawings unclear or inconsistent between disciplines

**Prevention**:
- Implement trade-specific QC checklists (example: CFS framing QC = plumb/level check, fastener spacing, track alignment, connection bolt fit-up)
- Require pre-inspection coordination meeting before phase completion: Super, Building Official, next-phase trades review work together
- Create a "sign-off" requirement: prior trade cannot move on until downstream trade agrees interfaces are correct
- Build rework contingency time into lookahead (2-5% of phase duration for minor rework)
- Daily huddle includes QC check: any quality concerns from yesterday's work?

---

### 9. Overcommitment Variance
**Definition**: Too much work was committed for the crew size, time window, or complexity; scope had to be deferred mid-week.

**Common Examples**:
- Concrete crew promised to place 200 CY in 1 day; after 100 CY, crew exhausted, rest deferred to next day
- Electrical rough-in promised to complete 2 zones; after 1 zone, wire delivery discovered incomplete; deferred 1 zone
- PEMB erection promised 4 frames in 3 days; weather and bolt issues kept pace at 2.5 frames; 1.5 frames deferred

**Root Cause Patterns**:
- Foreman overconfident about crew productivity (no historical data)
- Task not broken down to specific scope (too vague to plan accurately)
- Crew size or equipment not validated during commitment step
- No productivity baseline from similar prior phases

**Prevention**:
- Establish historical productivity norms: "CFS stud frame = 120 LF per crew per day" (refine over time with actual data)
- Break work into daily crew tasks, not weekly bulk estimates
- In commitment step, have foreman state crew size + daily task scope + realistic completion date
- Reference past project data: "Last week's excavation was 50 LF/day. This week's trench is 150 LF. Need 3 days, not 2."
- Build schedule padding for learning curve in early weeks; tighter planning as crew settles in

---



## Constraint Log: Managing Future Work

The Constraint Log is a key artifact of the Last Planner System. It captures work that "wants to" be done but cannot be committed because constraints are not cleared. The log drives the lookahead planning (make-ready) process.

### Constraint Log Format

| Log ID | Task | Trade | Constraint | Owner | Target Resolution | Escalation Trigger | Status |
|--------|------|-------|-----------|-------|-------|---|---|
| CL-2026-08-001 | Excavate north lot, X-4 to X-5 | Walker | Prerequisites (wet ground) | Super / Walker | 03/02/26 | If unresolved by 02/28, delay work 1 week | Open |
| CL-2026-09-001 | Install HM doors + hardware | Hek Glass / Schiller | Design (submittals overdue 24 days) | PM / Schiller | 03/01/26 | If unresolved by 02/27, escalate to Owner for liquidated damages | Open |
| CL-2026-09-002 | Rough-in MEP ductwork, Zones 1-3 | Davis & Plomin | Prerequisites (CFS framing not complete) | Super | 04/15/26 | Built into schedule; ductwork depends on framing |Open |

### Constraint Log Management Process

1. **During Step 2 (Constraint Screening)**: Any task that fails constraint check is added to Constraint Log, not to commitments
2. **Responsible Party Assignment**: Who owns the fix? Designer (for design constraint), Supplier (for material), Super (for prerequisites/access), Sub (for labor/equipment)
3. **Target Resolution Date**: When must constraint be cleared? Use lookahead logic:
   - For a task scheduled in Week N, constraints must be cleared by Week N-2 at latest (to allow make-ready prep)
   - For a task in Week N+4, resolve constraints by Week N+1
4. **Escalation Trigger**: At what point does the constraint become critical and need escalation to PM or Owner?
5. **Weekly Constraint Review**: Every Friday (as part of EOW Scoring), review open constraints:
   - Did any resolve this week? Move to closed.
   - Are any at risk? Escalate early.
   - Is resolution plan on track? Update status.

---



## Make-Ready Process: 6-Week Lookahead Screening

The Last Planner System's "make-ready" process is the bridge between Lookahead Planning (Tier 3) and Weekly Work Plans (Tier 4).

### Make-Ready Timeline

```
Week N+4      Week N+2      Week N (This Week)
6 Weeks Out   3 Weeks Out
   |             |
   V             V
Identify      Screen &       Week N: Weekly
Constraints   Plan Make-     Commitments Made
              Ready Actions  (Constraint-Free)
   ●──────────●──────────●
   |          |          |
   Lookahead  Constraint Make-Ready   Execution
   Planning   Log        (Detailed)
```

### The Four Make-Ready Milestones

**Milestone 1: 6-Week Lookahead Screening (Tier 3)**
- Look at work scheduled 4-6 weeks out
- Ask: What constraints could block this work?
- Create constraint log entries
- Example: "PEMB erection starts 03/23. Need anchor bolts approved, ordered, and on site by 03/20. Bolt drawings must go to fabricator by 02/15 at latest (6-week lead time)."

**Milestone 2: Active Constraint Removal (Weeks 3-4 Out)**
- Constraint log items become active assignments
- Responsible parties work to clear constraints
- Example: "Anchor bolt shop drawings to Nucor: due 02/15 (today). Architectural finalized details 02/12. Drawings released to Nucor 02/14. Bolts confirmed shipping 03/01. CLEARED."

**Milestone 3: Commitment-Ready Verification (Week 1-2 Out)**
- Final constraint check before work enters weekly plan
- Verify all 6 constraints cleared
- Example: "Anchor bolts arrived 03/01. Inspected and counted. Survey layout template prepared. HP-007 anchor bolt survey scheduled 03/16. Ready to commit PEMB framing erection for Week starting 03/23."

**Milestone 4: Weekly Commitment (This Week)**
- Task enters Weekly Work Plan only after all milestones passed
- Trade foreman commits confidently because constraints are genuinely cleared
- Example: "Week of 03/23/26: Erect 6 PEMB frames, 03/23-04/10. Alexander Construction commits to 3 frames/week (3 days per frame)."

### Integration with Look-Ahead-Planner Skill

The last-planner skill extends the look-ahead-planner by adding:

1. **Explicit constraint checks**: For each task in lookahead, verify the 6 constraint categories
2. **Make-ready task assignments**: Create specific work items (drawing finalization, long-lead orders, prep work) that must be completed before main work can proceed
3. **Escalation alerts**: Flag constraints at risk of missing resolution target
4. **Weekly plan handoff**: Tasks flow from lookahead → constraint log → make-ready → weekly commitments

Example: Look-ahead-planner shows "CFS Framing Phase: 04/21 - 05/20". Last-planner adds:
- **Constraint screening**: Design (YES—drawings ready), Material (pending final door schedule), Labor (TBD), Equipment (TBD), Prerequisites (requires SOG cure 28 days), Space (requires PEMB frames to be dried-in)
- **Make-ready actions**: (1) Finalize door schedule by 04/05; (2) Order CFS studs by 03/15 (6-week lead); (3) Conduct crew safety orientation by 04/18; (4) Verify PEMB erection complete and inspected by 04/19
- **Target: By 04/20, all constraints cleared, weekly plan ready to commit "CFS Framing Week 1" for week of 04/21**

---



## PPC Pareto Analysis: Root Cause Focus

Over 4-8 weeks of Last Planner execution, variance data accumulates. Use Pareto Analysis to identify the top 3 root causes blocking work.

### Pareto Aggregation Example (4 Weeks MOSC Data)

```
Variance Category    Count    % of Total    Cumulative %
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Prerequisites      8         42%           42%
2. Material           5         26%           68%
3. Labor              3         16%           84%
4. Equipment          2         11%           95%
5. Design             1          5%          100%
6. Weather            0          0%          100%
7. Space/Access       0          0%          100%
8. Rework             0          0%          100%
9. Overcommitment     0          0%          100%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL               19        100%
```

**Key Insight**: Prerequisites + Material = 68% of all variances. These two categories are the project's biggest bottlenecks.

### Action Plan from Pareto

1. **Prerequisites (42% of failures)**
   - Root causes: Prior work not inspected/accepted in time; unclear handoff criteria
   - Actions: (a) Assign inspection owner for each phase (Super or GC); (b) Create explicit "sign-off checklist" before prior trade leaves phase; (c) Schedule inspections 1-2 days after task completion (don't wait until next week)

2. **Material (26% of failures)**
   - Root causes: Long-lead items not ordered on time; supplier delays; missing approvals
   - Actions: (a) material-tracker: pull live procurement status into weekly planning; (b) Weekly supplier check-in call (Mon 8:00 AM); (c) Establish expediting trigger: if delivery within 7 days and unconfirmed, escalate to PM

3. **Labor (16% of failures)**
   - Root causes: Crew called away; insufficient crew size; lack of training
   - Actions: (a) labor-tracker: confirm crew headcount and availability in planning; (b) Develop crew size norms based on actual productivity; (c) Require crew orientation/briefing for each phase

### Improvement Cycle (Kaizen)

Every 4 weeks:
1. Aggregate variance data (Pareto chart)
2. Identify top 3 categories
3. Discuss root causes with trade foremen and subs
4. Implement one specific countermeasure per category
5. Monitor results for 2-4 weeks
6. Adjust and iterate

Example countermeasure: For Prerequisites delays, implement a "Phase Completion Checklist" reviewed in a kickoff meeting with next phase trades before current phase wraps. This explicit handoff dramatically improves PPC by avoiding the "we didn't know work was done" ambiguity.

---



## Command: /weekly-plan

The last-planner skill provides the following commands:

### /weekly-plan new
**Purpose**: Start a new weekly work plan for the upcoming week.

**Usage**:
```
/weekly-plan new
```

**Output**:
- Loads previous week's PPC results and retrospective
- Displays open constraint log
- Prompts for trade foreman input
- Creates a blank Weekly Work Plan template with:
  - Week dates
  - Constraint screening form (6 constraints × N tasks)
  - Commitment sign-off section
  - Notes and escalations field

---

### /weekly-plan commit
**Purpose**: Add a specific commitment to the weekly plan.

**Usage**:
```
/weekly-plan commit [trade] [task-description] [location] [duration-days]
```

**Example**:
```
/weekly-plan commit "Walker Construction" "Excavate south footing trench, X-1 to X-3" "Building foundation, south side" 3
```

**Process**:
1. Displays task details
2. Runs through 6-constraint checklist:
   - Design ready? (Y/N)
   - Material ready? (Y/N)
   - Labor ready? (Y/N)
   - Equipment ready? (Y/N)
   - Prerequisites done? (Y/N)
   - Space/Access clear? (Y/N)
3. If all YES → Constraint-free commitment created; trade foreman prompted to initial/sign
4. If any NO → Task moved to constraint log; responsible party and target resolution date assigned

---

### /weekly-plan score
**Purpose**: End-of-week scoring. Mark each commitment complete or incomplete, calculate PPC.

**Usage**:
```
/weekly-plan score
```

**Process**:
1. Displays all commitments for the week
2. For each, asks: "Completed? (Y/N)"
3. If N (incomplete), asks: "Variance category? (list 1-9)"
4. Computes:
   - Total commitments
   - Completed count
   - PPC = (Completed / Total) × 100
   - PPC by trade
   - Variance summary (count by category)
5. Generates EOW report with photos and notes
6. Stores results in weekly-plans.json for trending

**Example Output**:
```
WEEK OF 02/24 - 02/28, 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Commitments: 4
Completed: 3
PPC: 75%
4-Week Trend: [68%, 75%, 82%, 75%]  ← Trend stable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PPC BY TRADE:
  Walker Construction:       100% (2/2)  ✓ Reliable
  W Principles:               50% (1/2)  ✗ Marginal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VARIANCE BREAKDOWN:
  Prerequisites:  1 incomplete (100%)
  Material:       0
  Labor:          0
  Equipment:      0
  Design:         0
  Weather:        0
  Space/Access:   0
  Rework:         0
  Overcommitment: 0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INCOMPLETE ITEM:
  - COMM-2026-08-003: Stem wall concrete pour
    Variance: Prerequisites (supplier equipment failure)
    Rescheduled to Week 9 (03/03 pour)
```

---

### /weekly-plan ppc
**Purpose**: Display PPC history, trend, and performance by trade.

**Usage**:
```
/weekly-plan ppc
/weekly-plan ppc [--weeks 8]
/weekly-plan ppc [--by-trade]
```

**Output** (Example):
```
PPC TREND (8-Week History)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WK-2026-05 (01/27-01/31): 68%  ↗
WK-2026-06 (02/03-02/07): 71%  ↗
WK-2026-07 (02/10-02/14): 75%  ↗
WK-2026-08 (02/17-02/21): 72%  ↗
WK-2026-09 (02/24-02/28): 75%  ↗
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4-WEEK ROLLING AVERAGE: 73.5% (Yellow) ← Marginal

TARGET: 85% (Green)
STATUS: Improving trend; 12% gap to target
ACTION: Continue constraint discipline; focus on Prerequisites and Material (top 2 variance sources)

PPC BY TRADE (Latest 4 Weeks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Walker Construction:       87% ✓ Reliable
W Principles:              71% ↔ Marginal (watch)
[Others not yet active]
```

---

### /weekly-plan constraints
**Purpose**: View the active constraint log. Identify items that want to be worked but are blocked.

**Usage**:
```
/weekly-plan constraints
/weekly-plan constraints [--by-owner]
/weekly-plan constraints [--escalated]
```

**Output** (Example):
```
OPEN CONSTRAINT LOG
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CL-2026-08-001: Excavate north lot, X-4 to X-5
  Trade: Walker Construction
  Constraint: Prerequisites (wet ground, saturated from rain)
  Owner: Super / Walker (site drainage)
  Target Resolution: 03/02/26
  Status: Open (monitoring)
  Notes: Watch weather; if no rain, soil will drain by 03/02

CL-2026-09-001: Install HM doors + hardware
  Trade: Hek Glass / Schiller
  Constraint: Design (submittals overdue 24 days)
  Owner: PM / Schiller (submittal processing)
  Target Resolution: 03/01/26
  Status: ESCALATED (overdue)
  Escalation Trigger: If unresolved by 02/27, escalate to Owner for supplier performance
  Notes: Schiller submittals backlog; PM contacted supplier Friday

CL-2026-09-002: Rough-in MEP ductwork, Zones 1-3
  Trade: Davis & Plomin
  Constraint: Prerequisites (CFS framing not complete)
  Owner: Super (sequence management)
  Target Resolution: 04/15/26
  Status: On track (built into schedule)
  Notes: Ductwork depends on framing completion Week 16; plan predicts framing done by 04/14
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY:
  Total Open: 3
  At Risk (Target <7 days): 1 escalated
  On Track: 2
```

---

### /weekly-plan pareto
**Purpose**: Variance category analysis. Identify top root causes and improvement opportunities.

**Usage**:
```
/weekly-plan pareto
/weekly-plan pareto [--weeks 8]
```

**Output** (Example):
```
PARETO ANALYSIS: ROOT CAUSE BREAKDOWN (8 Weeks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Category              Count    % Total    Cumulative %
──────────────────────────────────────────────────────
1. Prerequisites        8       42%          42% ◄──────── TOP 3
2. Material             5       26%          68% ◄──────── account for
3. Labor                3       16%          84% ◄──────── 84% of variances
4. Equipment            2       11%          95%
5. Design               1        5%         100%
6. Weather              0        0%         100%
7. Space/Access         0        0%         100%
8. Rework               0        0%         100%
9. Overcommitment       0        0%         100%
─────────────────────────────────────────────────────
Total                  19      100%

TOP 3 OPPORTUNITIES FOR IMPROVEMENT:

1. PREREQUISITES (42% of failures)
   Root Causes: Prior work not inspected/accepted on time
   Recommendation: Assign inspection owner for each phase; schedule inspections 1-2 days after task completion, not wait until end of week
   Expected Impact: Eliminate ~8 failures/8-week cycle (assume +50% improvement) → 4 fewer failures → +2% PPC

2. MATERIAL (26% of failures)
   Root Causes: Long-lead items not ordered; supplier delays; missing approvals
   Recommendation: Pull material-tracker status into weekly planning; establish expediting trigger if delivery within 7 days and unconfirmed
   Expected Impact: Eliminate ~2-3 failures (supplier management improvement) → +1-1.5% PPC

3. LABOR (16% of failures)
   Root Causes: Crew unavailable; insufficient crew size
   Recommendation: Integrate labor-tracker; confirm crew headcount in weekly planning; develop crew size norms
   Expected Impact: Eliminate ~1-2 failures → +0.5-1% PPC

COMBINED EXPECTED IMPROVEMENT: +3.5-4.5% PPC (from 73.5% → 77-78% within 8 weeks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---



## Integration Points

### 1. look-ahead-planner Skill
**How Last Planner extends lookahead**:
- Lookahead displays 6-week schedule and identifies major task sequences
- Last Planner adds constraint screening (6 constraints per task) to lookahead output
- Constraint log items are make-ready assignments pulled from lookahead
- Weekly commitments fed back to lookahead to update actual progress

**Example data flow**:
- Lookahead shows: "CFS Framing Phase: Week 11-16 (04/21 - 05/29)"
- Last Planner constraint check: Design ✓, Material (pending), Labor (TBD), Equipment, Prerequisites (SOG cure), Space (PEMB)
- Constraint log: "Finalize door schedule by 04/05", "Order CFS by 03/15", "Crew safety orientation by 04/18"
- Weekly commitment (Week 16): "CFS Framing Week 1: frame bedroom zone A-B, 04/21-04/25 — ALL CONSTRAINTS CLEARED"

---

### 2. daily-report-format Skill
**How daily reports feed Last Planner**:
- Daily reports document completion status for each committed task (by crew, by day)
- Task completion data rolls up into EOW scoring
- Blockers logged in daily report inform constraint log updates
- Photos attached to daily reports document work status for EOW verification

**Example**:
- Daily Report (Tue 02/25): "Excavation — south trench, X-1 to X-3 — Status: In progress. Completed 50 LF. Weather good. No blockers."
- Daily Report (Wed 02/26): "Excavation — COMPLETE. 150 LF full depth. Compaction testing scheduled tomorrow."
- EOW Scoring: "Excavation task — Mark COMPLETE. Verify with photos from daily reports."

---

### 3. material-tracker Skill
**How material status feeds constraint checks**:
- Material-tracker maintains live procurement status (ordered, in transit, delivered, inspected, approved)
- Last Planner constraint check for each task queries material-tracker for required materials
- Material constraint status (YES/NO) pulled directly from material-tracker PO status
- Material delays flagged in constraint log trigger escalation in material-tracker

**Example**:
- Last Planner constraint check: "Pour concrete SOG — Material constraint: Wells Concrete batch ready?"
- Query material-tracker: "Wells Concrete PO status: Approved, delivery confirmed 02/26"
- Result: Material constraint = CLEARED
- If material-tracker showed: "Delivery pending, TBD date" → Material constraint = NOT CLEARED → add to constraint log

---

### 4. sub-performance Skill
**How PPC feeds sub scorecards**:
- Last Planner calculates PPC by trade (each sub's completion rate)
- sub-performance skill incorporates PPC into the Schedule Dimension of the sub scorecard
- Subs with PPC >85% earn high marks; subs with PPC <70% flagged for coaching
- Pareto analysis identifies subs with recurring variance patterns (e.g., chronic material delays = poor supply chain management)

**Example Sub Scorecard (Davis & Plomin Mechanical)**:
- Schedule Dimension (PPC): 78% (Marginal)
- Root cause: 60% of incomplete work due to "Prerequisites" (waiting for framing) — Acceptable
- Recommendation: Improve lookahead coordination with framing trades to verify frame completion dates

---

### 5. earned-value-management Skill
**How PPC trend correlates with Schedule Performance Index**:
- PPC trend (4-week rolling average) is a leading indicator of Schedule Performance Index (SPI)
- Rising PPC → confidence in schedule → SPI stable or improving
- Falling PPC → schedule at risk → SPI likely to decline
- When PPC drops below 70%, trigger earned-value review and schedule recovery plan

**Example**:
- Week 4-7 PPC trend: 68% → 71% → 73% → 75% (improving)
- Same period SPI: 0.95 → 0.96 → 0.97 → 0.98 (catching up to baseline)
- Interpretation: Last Planner discipline working; schedule improving

---

### 6. morning-brief Skill
**How Last Planner feeds the daily standup**:
- Morning brief opens with: "Today's committed tasks" (from current week's weekly plan)
- Constraint alerts displayed (any constraints due to clear in next 2 days?)
- PPC status shown (current week trend, prior week score)
- Crew assignments pulled from weekly plan

**Example morning brief**:
```
FRIDAY 02/28 MORNING BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TODAY'S COMMITTED WORK:
  Walker: Finish excavation south pit (if weather OK)
  W Principles: Build stem wall forms; prep for concrete pour (delivery scheduled today)

CONSTRAINT ALERTS:
  • Concrete delivery: Wells Concrete — delivery window 1-3 PM — confirm before 8 AM
  • Ground moisture: Saturated from Tue-Wed rain — soil testing this AM to verify readiness

WEEK SCORE (Due EOD Friday):
  Current week (02/24-02/28) PPC tracking: 3/4 committed (75% if stem wall pour succeeds)
  Prior week (02/17-02/21) PPC final: 72%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 7. project-dashboard Skill
**Dashboards powered by Last Planner data**:
- **PPC Trend Chart**: 8-week line chart showing weekly PPC + 4-week rolling average + target (85%) line
- **Variance Pareto Chart**: Bar chart of variance categories (count), sorted descending
- **PPC by Trade**: Table of each sub's PPC, sorted high to low; visual indicator (green/yellow/red)
- **Constraint Log Status**: Active constraints filtered by owner, target resolution date, escalation status
- **Make-Ready Pipeline**: Gantt-style view of constraint removal activities 6 weeks out

**Example Dashboard View**:
```
╔════════════════════════════════════════════════════════════════════╗
║ LAST PLANNER DASHBOARD — MOSC PROJECT (Updated Friday EOD)        ║
╠════════════════════════════════════════════════════════════════════╣
║ WEEK 9 (02/24-02/28, 2026) PPC: 75% (4-wk avg: 74%) — Yellow      ║
║ TARGET: 85% | GAP: 11 pts | STATUS: Improving (trends +2%/week)   ║
╠════════════════════════════════════════════════════════════════════╣
║ PPC BY TRADE                                                       ║
║  Walker Construction:        100% ██████████ ✓                     ║
║  W Principles:               50% ██████  ✗ (Watch)                 ║
╠════════════════════════════════════════════════════════════════════╣
║ TOP 3 VARIANCE SOURCES (8 weeks)                                   ║
║  1. Prerequisites:  8 incidents (42%) ◄─── FOCUS AREA              ║
║  2. Material:       5 incidents (26%) ◄─── FOCUS AREA              ║
║  3. Labor:          3 incidents (16%)                              ║
╠════════════════════════════════════════════════════════════════════╣
║ OPEN CONSTRAINT LOG (Active: 3)                                    ║
║  ⚠  CL-2026-09-001: Schiller submittals — ESCALATED (due 03/01)  ║
║  ✓  CL-2026-08-001: Excavation north lot — On track (target 03/02)║
║  ✓  CL-2026-09-002: MEP ductwork — On track (target 04/15)        ║
╠════════════════════════════════════════════════════════════════════╣
║ MAKE-READY PIPELINE (Next 6 Weeks)                                 ║
║  Week 9 (02/24): Finalize door schedule (Schiller)                ║
║  Week 10 (03/03): Order CFS studs (EKD)                           ║
║  Week 11 (03/10): Crew orientation — CFS framing                  ║
║  Week 12 (03/17): PEMB anchor bolt survey (HP-007)                ║
║  Week 13 (03/24): PEMB frame erection begins                      ║
║  Week 14 (03/31): SOG cure complete; framing ready                ║
╚════════════════════════════════════════════════════════════════════╝
```

---



## Data Store: weekly-plans.json

The last-planner skill maintains a persistent JSON file storing all weekly plans, constraints, and PPC history.

**File location**: `/path/to/project/02 - Contract Documents/weekly-plans.json`

**Structure**: Full JSON schema shown in "Weekly Plan Data Model" section above. Includes:
- 8+ weeks of historical weekly plans
- Aggregated PPC trend
- Constraint log (open + closed)
- Variance summary statistics

**Use cases**:
- Trend analysis over time
- Pareto analysis across all weeks
- Sub performance tracking
- Predictive analytics (if PPC drops below 70%, when will project slip?)
- Retrospective learning (what caused past failures? what prevented recurrence?)

---



## Best Practices for Last Planner Implementation

### 1. Leadership Commitment
- Superintendent must sponsor Last Planner; attend every weekly planning meeting
- PM attends at least 1x/month to review PPC trends and constraint escalations
- Owner / Architect invited to review constraint log monthly (design bottlenecks surface early)

### 2. Trade Foreman Buy-In
- Foremen must understand that **commitment = accountability**. Promises must be kept.
- Foremen see that Last Planner reveals the TRUE state of the project (no sandbagging; constraints surface)
- Foremen invited to Pareto analysis and improvement planning; their input is valued
- Subs with high PPC are recognized and rewarded (publicly, in performance reviews)

### 3. Discipline
- **Weekly planning meeting ALWAYS at same time**: Monday morning 8:00 AM. Foremen know it's non-negotiable.
- **Daily huddles ALWAYS 15 min**: 7:00 AM on site. Track commitment execution in real time.
- **EOW scoring ALWAYS Friday 4 PM**: Complete same-day, while work is fresh. Document with photos.
- **Pareto analysis ALWAYS every 4 weeks**: Identify and tackle the top 3 blockers.

### 4. Constraint Log Discipline
- **Every constraint gets an owner**. No "TBD"; the PM, Super, or sub foreman owns the fix.
- **Every constraint gets a target resolution date**. Write it down.
- **Every constraint at risk (target <7 days away) gets escalated** on Friday. No surprises Monday.
- **Weekly review**: Are open constraints tracking to resolution? Are new constraints appearing in same categories?

### 5. Make-Ready Process
- **6-week lookahead is MANDATORY input** to weekly planning. Don't plan weekly work that constraints aren't being cleared for.
- **Make-ready activities are scheduled work**. Assign crew and timeline to "finalize door schedule" or "order CFS" just like any trade work.
- **Hold weekly make-ready status review** (Fri 11 AM, 30 min): Are constraint removal activities on track?

### 6. Trust and Transparency
- **No punishment for honest constraints**. If a trade foreman says "I can't commit to that because material isn't in," thank them. That's the system working.
- **PPC is not a tool to blame subs**. Use PPC by trade to identify which subs need coaching, not to penalize.
- **Variance category is root-cause analysis, not blame**. "Material" is not the sub's fault if the supplier is late; escalate to procurement.

### 7. Continuous Improvement (Kaizen)
- **Every 4 weeks, run Pareto analysis**. Identify top 3 variance sources.
- **For each top 3 source, implement ONE countermeasure**. Don't try to fix everything at once.
- **Track improvement**: Did the countermeasure work? Did that variance category drop?
- **Example**: "We had 8 Prerequisites failures (42% of variances). We assigned inspection owners. Result: Prerequisites dropped to 3 failures (15%) in next 4-week cycle. +3% PPC improvement."

### 8. Weekly Planning Meeting Agenda (Example, ~2.5 hours)

```
MONDAY 8:00 AM - 10:30 AM — WEEKLY PLANNING MEETING

8:00-8:15  Retrospective Review (15 min)
           • Prior week PPC score
           • Incomplete items by variance category
           • Trade-by-trade PPC
           • Trend (4-week rolling avg)

8:15-8:45  Constraint Screening (30 min)
           • Walk through proposed tasks for this week
           • For each task, verify 6 constraints: Design, Material, Labor, Equipment, Prerequisites, Space
           • Any task with constraints uncleared → move to constraint log
           • Constraint log items get owner + target resolution date

8:45-9:30  Commitment Phase (45 min)
           • Trade foremen review constraint-free tasks
           • Each foreman commits verbally: "I promise to complete [task] by [date]"
           • Foreman initials commitment on Weekly Work Plan
           • Sequence commitments to avoid idle time
           • Identify backup work if upstream finishes early

9:30-9:45  Make-Ready Status Review (15 min, optional — if 6-week lookahead is active)
           • Review constraint removal activities planned
           • Are they on track? Any new blockers?

9:45-10:00 Escalations & Closeout (15 min)
           • Constraint log items at risk of missing target → escalate to PM
           • Assign photos/documentation responsibilities for EOW
           • Confirm daily huddle time (7:00 AM, 15 min)
           • Next week's meeting confirmed

10:00-10:30 Buffer / Q&A (optional)
```

### 9. Daily Huddle Agenda (7:00 AM, 15 minutes)

```
EVERY WEEKDAY 7:00 AM - 7:15 AM — DAILY HUDDLE (On-Site)

7:00-7:05  Status Update (5 min)
           • Recap: What was committed to be done today?
           • Actual: What happened yesterday? Any work complete?
           • Any blockers surfaced overnight?

7:05-7:10  Crew Readiness (5 min)
           • Is each crew present, ready to work?
           • Any absences, equipment issues, material shortages?
           • Adjust task if needed

7:10-7:15  Today's Focus (5 min)
           • Confirm today's committed work
           • Call out any safety or coordination issues
           • Assign standby/backup work if dependent work delayed

7:15       Adjourn (crews to work)
```

### 10. EOW Scoring Session (Friday 4:00 PM, 1 hour)

```
FRIDAY 4:00 PM - 5:00 PM — END-OF-WEEK SCORING

4:00-4:15  Site Walk (15 min)
           • Super walks site with each trade foreman
           • Verify completion status for each committed task
           • Take photos for documentation
           • Note any quality issues or rework needed

4:15-4:45  Scoring & Retrospective (30 min)
           • Mark each commitment Complete ✓ or Incomplete ✗
           • For incomplete, assign variance category
           • Calculate PPC = (Completed / Total) × 100
           • Calculate PPC by trade
           • Tally variance categories

4:45-5:00  Documentation & Closeout (15 min)
           • Store results in weekly-plans.json
           • Prepare summary for PM and Owner
           • Identify any escalations needed (big variances, subs in trouble)
           • Set agenda for next Monday (any special constraints to screen?)

5:00       EOW - Results published, shared with team
```

---



## Schedule Recovery & Compression

When schedule performance degrades beyond acceptable thresholds, recovery planning becomes a critical superintendent responsibility. The Last Planner System provides early warning through PPC trends and constraint analysis, but the super must know how to translate those warnings into actionable recovery strategies.

### When to Trigger Recovery Planning

Recovery planning should be initiated when any of the following conditions are met:

1. **PPC Below 60% for 2+ Consecutive Weeks**
   - Indicates systemic reliability failure, not just a bad week
   - Root cause analysis should already be underway via variance Pareto
   - Recovery plan needed because the weekly work plan process alone is not self-correcting fast enough

2. **SPI (Schedule Performance Index) < 0.90 on Critical Path Activities**
   - SPI = Earned Schedule / Actual Time
   - Below 0.90 means you are losing ground faster than normal variation
   - Focus specifically on critical path and near-critical path activities (total float < 5 days)

3. **Milestone at Risk with < 2 Weeks Float Remaining**
   - When float erosion puts a contractual milestone in jeopardy
   - Two weeks is the minimum buffer needed to implement meaningful recovery actions
   - Below this threshold, options narrow dramatically

4. **Multiple Constraint Failures in Screening**
   - When the 6-week lookahead consistently shows unresolved constraints
   - Indicates upstream planning process is breaking down
   - Recovery must address the planning system, not just the schedule

### Fast-Tracking Strategies

Fast-tracking means running activities in parallel that were originally planned as sequential. This compresses the schedule without adding resources, but increases risk because successor activities begin before predecessor activities are fully complete.

**Risk Assessment — Which Activities Can Overlap:**

```
OVERLAP FEASIBILITY MATRIX

Can Overlap (with precautions):
├── Interior framing before roof deck complete
│   → Protect with tarps, weather monitoring, limit to areas with deck
├── MEP rough-in in Phase A while framing continues in Phase B
│   → Physical separation provides natural risk mitigation
├── Drywall hanging in Phase A while MEP rough-in continues in Phase B
│   → Requires completed inspection in Phase A areas
├── Exterior cladding while interior work proceeds
│   → Normal practice, coordinate scaffold/access
└── Site utilities while foundation work proceeds in different area
    → Maintain safe separation distances

Cannot Overlap (hard dependencies):
├── Concrete pour before formwork/rebar complete → structural integrity
├── Insulation before framing inspection → code violation, rework risk
├── Drywall before MEP rough-in inspection → will be torn out
├── Ceiling grid before above-ceiling MEP complete → access blocked
├── Flooring before overhead wet work complete → damage risk
└── Paint before drywall finishing complete → quality failure
```

**Overlap Strategies:**

- **75% Rule:** Start successor when predecessor is 75% complete. This provides schedule compression of roughly 25% of the predecessor duration. Risk: if remaining 25% encounters problems, successor work may need rework or protection.
- **Finish-to-Start with Lag Reduction:** Reduce the lag between activities rather than eliminating the relationship entirely. Example: reduce FS+5d to FS+2d to gain 3 days.
- **Zone-Based Overlap:** Divide the work area into zones. Predecessor works in Zone 1 → Zone 2, while successor follows in Zone 1 as soon as it is complete. This is the safest form of fast-tracking.

**Example — Fast-Track Interior Sequence:**

```
ORIGINAL SEQUENCE (serial):
Framing → Rough-In → Insulation Inspect → Insulation → Drywall → Tape/Finish
  10d       15d          2d                   5d          8d        10d
Total: 50 days

FAST-TRACKED (zone-based, 3 zones):
Zone A Frame (4d) → Zone A Rough (5d) → Zone A Inspect → Zone A Insulate → Zone A DW
Zone B Frame (4d) → Zone B Rough (5d) → Zone B Inspect → Zone B Insulate → Zone B DW
Zone C Frame (4d) → Zone C Rough (5d) → Zone C Inspect → Zone C Insulate → Zone C DW

Compression: ~35 days total (30% reduction)
Risk: moderate — inspection bottleneck per zone, but each zone is independent
```

### Crashing Strategies

Crashing means adding resources to shorten activity duration. Unlike fast-tracking, crashing increases direct cost but does not increase technical risk (the sequence remains the same).

**Cost-Benefit Analysis:**

```
Crash Cost Per Day = (Crash Cost - Normal Cost) / (Normal Duration - Crash Duration)

Example:
  Activity: Concrete Flatwork
  Normal: 12 days, $48,000
  Crash:  8 days, $72,000
  Crash Cost/Day = ($72,000 - $48,000) / (12 - 8) = $6,000/day

Priority: Crash cheapest critical activities first.
Sort all critical activities by crash cost/day, ascending.
Crash the cheapest first until target completion date is met.
```

**Diminishing Returns of Adding Resources:**

Adding more crews or labor does NOT produce linear time reduction:

| Resource Increase | Expected Time Reduction | Efficiency |
|-------------------|------------------------|------------|
| +25% resources | ~15-18% reduction | 70% efficient |
| +50% resources | ~25-30% reduction | 55% efficient |
| +100% resources | ~35-40% reduction | 40% efficient |
| +200% resources | ~45-50% reduction | 25% efficient |

Rule of thumb: **50% more resources yields only 25-30% time reduction** due to:
- Crew interference and congestion
- Learning curve for new crews
- Increased coordination overhead
- Diminishing productive space
- Supervision capacity limits

**When Crashing Does Not Work:**

- **Space-constrained work:** Cannot fit more crews in a mechanical room, elevator shaft, or single-story area
- **Linear work:** Pipeline, roadway, and similar work where only one crew can work at the leading edge
- **Single-source material:** If the constraint is material delivery, more labor does not help
- **Inspection bottleneck:** If the constraint is inspection scheduling, more crews just means more idle time waiting
- **Skill-specific work:** When only one qualified crew/person can perform the work (e.g., controls programming, specialty welding)

### Recovery Plan Format

When recovery is needed, follow this structured process:

```
SCHEDULE RECOVERY PLAN

1. IDENTIFY AFFECTED ACTIVITIES
   - List all critical path activities that are delayed or at risk
   - List near-critical activities (TF < 5 days) affected
   - Identify downstream impacts (what else shifts if these are late?)

2. ASSESS RECOVERY OPTIONS FOR EACH ACTIVITY
   Option A: Fast-track (overlap with successor)
   Option B: Crash (add resources)
   Option C: Re-sequence (change work order)
   Option D: Scope reduction (negotiate with owner/architect)
   Option E: Accept delay (document impact, notify owner)

3. CALCULATE COST/RISK FOR EACH OPTION
   - Additional cost (labor, equipment, material premium)
   - Risk (rework probability, quality impact, safety impact)
   - Feasibility (can we actually get the resources? is space available?)

4. SELECT OPTIMAL COMBINATION
   - Minimize total recovery cost
   - Minimize risk
   - Maximize schedule compression
   - Get buy-in from affected trades

5. DOCUMENT REVISED PLAN
   - Updated CPM schedule with recovery logic
   - Cost impact summary
   - Risk register updates
   - Revised milestone dates (if any)

6. COMMUNICATE TO ALL TRADES
   - Recovery plan briefing (dedicated meeting, not tacked onto weekly)
   - Each trade confirms understanding and commitment
   - Updated lookahead and weekly work plans reflect recovery

7. MONITOR DAILY
   - Daily check-ins on recovery activities
   - Immediate escalation if recovery actions are not tracking
   - Weekly PPC must reflect recovery commitments
```

### Overtime Management

Overtime is the most common (and most overused) recovery tool. Understanding its true impact is critical.

**Productivity Impact of Sustained Overtime (Industry-Studied Diminishing Returns):**

| Duration | Work Schedule | Effective Productivity |
|----------|--------------|----------------------|
| Week 1 | 5x10 or 6x8 | ~90% of normal |
| Week 2 | Same | ~85% of normal |
| Week 3 | Same | ~75% of normal |
| Week 4+ | Same | ~65% of normal |

After 4 weeks of sustained overtime, you are paying 150-200% of normal labor cost for 65% productivity. This means **overtime beyond 3-4 weeks often produces negative net schedule benefit** — you pay more and get less done than a well-rested crew working normal hours.

**Cost Premium:**
- After 40 hours/week: 1.5x hourly rate (federal and most state law)
- Weekends: 1.5x to 2.0x depending on trade agreement
- Holidays: 2.0x to 2.5x depending on trade agreement
- Per diem/travel: additional cost if importing crews from outside area

**Fatigue and Safety Risk:**
- Incident rates increase ~30% after 10 hours on shift
- Incident rates increase ~60% after 12 hours on shift
- Weekend work after a 50+ hour week compounds fatigue
- OSHA scrutiny increases when sustained overtime is documented

**Overtime Schedules and Guidance:**
- **5x10:** Most sustainable. Two-day weekend allows recovery. Can sustain 4-6 weeks.
- **6x10:** Aggressive. One rest day. Limit to 2-3 weeks. Monitor fatigue closely.
- **7x10:** Emergency only. No rest days. **Never sustain more than 2 weeks.** Productivity collapse and safety risk are severe.

### Baseline Management

The CPM baseline schedule is the contractual benchmark against which all progress is measured. Managing baseline changes is a critical superintendent responsibility.

**When to Re-Baseline (New Baseline Justified):**
- **>10% schedule growth** from original baseline duration
- **Major scope change** that fundamentally alters the work sequence
- **Owner-directed phasing change** (e.g., split project into two phases)
- **Force majeure event** (pandemic, natural disaster, extended strike)
- **Mutual agreement** between owner and contractor that original baseline no longer represents a reasonable plan

**When NOT to Re-Baseline (Track Variance Instead):**
- Normal weather delays (track against original, claim float or time extension)
- Subcontractor performance issues (this is the contractor's problem to manage)
- Minor scope changes (adjust activities, track variance)
- Recovery schedule exists (track against both original baseline and recovery)

**Re-Baseline Procedure:**

```
1. NOTIFY OWNER/ARCHITECT
   - Written request to re-baseline with justification
   - Include impact analysis showing why current baseline is no longer valid

2. PRESERVE ORIGINAL BASELINE
   - Never delete or modify the original baseline
   - Save as "Original Contract Baseline" — this is the contractual document
   - All future baselines are numbered: Baseline 1 (original), Baseline 2 (revised), etc.

3. CREATE RECOVERY/REVISED SCHEDULE
   - Start from as-built status (actual dates for completed work)
   - Re-sequence remaining work based on current conditions
   - Apply recovery strategies where applicable
   - Ensure logic is sound (run DCMA 14-point check)

4. OBTAIN BUY-IN FROM TRADES
   - All affected subcontractors review and accept revised dates
   - Document acceptance (email confirmation minimum, signed letter preferred)

5. SUBMIT FOR APPROVAL
   - Owner/architect review and approve new baseline
   - Once approved, this becomes the new measurement benchmark
   - Continue tracking variance against BOTH original and revised baseline
```

---



## Forensic Schedule Analysis

Forensic schedule analysis is the after-the-fact examination of schedule delays, used for claims, disputes, change orders, and lessons learned. While the superintendent may not perform the forensic analysis personally, understanding the methods is essential for maintaining the right data during construction and for participating in delay disputes.

### Purpose

- Determine **what caused** schedule delays
- Allocate **responsibility** for delays (owner, contractor, third party, force majeure)
- Calculate **time and cost impact** of specific delay events
- Support **claims and dispute resolution**
- Provide **lessons learned** for future projects

### AACE Recommended Practice 29R-03

AACE International RP 29R-03 is the industry standard for forensic schedule analysis methods. It defines the accepted methodologies, their appropriate use, and the level of effort required. All forensic schedule work should reference this standard.

### Method Comparison

| Method | Description | When to Use | Complexity | Cost |
|--------|------------|-------------|------------|------|
| As-Planned vs. As-Built | Compare original baseline to actual completion | Simple disputes, small claims | Low | $ |
| Impacted As-Planned | Insert delays into baseline, calculate impact | Owner-caused delays, time extension requests | Medium | $$ |
| Collapsed As-Built | Remove delays from as-built, calculate "but-for" | Contractor proving entitlement, delay claims | Medium-High | $$$ |
| Time Impact Analysis (TIA) | Insert delay fragnets at each event, run forward pass | Most defensible, concurrent delay analysis | High | $$$$ |
| Window Analysis | Break project into windows, analyze each independently | Complex disputes, multiple delays from both parties | High | $$$$ |

### As-Planned vs. As-Built

The simplest method. Overlay the original baseline schedule with the actual as-built dates.

**Process:**
1. Export original baseline (planned start/finish for each activity)
2. Export as-built schedule (actual start/finish for each activity)
3. Compare activity-by-activity: which started late? which took longer?
4. Identify where actual diverged from plan
5. Root-cause each divergence (owner change, contractor issue, weather, etc.)

**Strengths:** Simple, inexpensive, easy to understand
**Weaknesses:** Does not account for concurrent delays, does not demonstrate critical path impact, limited defensibility in litigation

### Window Analysis

Divide the project into discrete time windows (typically monthly or by phase) and analyze each window independently.

**Process:**
1. Define windows (e.g., monthly periods, or milestone-to-milestone)
2. For each window:
   - What was planned to occur?
   - What actually occurred?
   - What delay events happened in this window?
   - Which delays affected the critical path during this window?
   - Who was responsible for each delay?
3. Calculate net delay per window
4. Sum across all windows for total project delay allocation

**Strengths:** Accounts for shifting critical path, handles concurrent delays fairly
**Weaknesses:** Requires detailed schedule updates at each window boundary, labor-intensive

### But-For (Collapsed As-Built) Analysis

This method asks: "But for [specific delay], when would the project have finished?"

**Process:**
1. Start with the as-built schedule (what actually happened)
2. Identify the specific delay to analyze (e.g., owner-caused design change)
3. Remove that delay from the as-built schedule
4. Recalculate the schedule — the resulting completion date is the "but-for" date
5. Difference between actual completion and but-for date = impact of that delay

**Strengths:** Demonstrates specific impact of specific delays, useful for contractor claims
**Weaknesses:** Requires well-maintained as-built data, can be challenged if multiple delays interact

### Concurrent Delay

Concurrent delay occurs when two or more independent delays affect the critical path during the same time period. This is the most contentious area of forensic schedule analysis.

**Definition:** Two or more delays occurring in the same time window, both affecting the critical path, caused by different responsible parties.

**Allocation Approaches (varies by jurisdiction and contract):**
- **Dominant Cause:** The delay with the greater impact controls; minor concurrent delay is subsumed
- **Shared Apportionment:** Delay is split proportionally between responsible parties
- **Global Impact:** Each party bears its own delay costs; neither receives time extension for concurrent period (most common in US courts)
- **First-in-Time:** The delay that started first controls the window

### How Last Planner Data Feeds Forensic Analysis

The data captured through the Last Planner System is valuable forensic evidence:

- **Delay log entries** become fragnet inserts for Time Impact Analysis
- **Daily reports** provide contemporaneous evidence of conditions and events
- **PPC records** show trade-by-trade performance (useful for allocating responsibility)
- **Constraint logs** document when issues were identified vs. resolved
- **Variance categories** provide a structured record of why work was not completed
- **Weekly work plans** show what was committed vs. what was achieved
- **Lookahead schedules** show what was anticipated and when constraints were identified

### Best Practices for Forensic-Ready Scheduling

1. **Maintain monthly schedule updates** at minimum (weekly preferred for critical periods)
2. **Preserve all schedule files** — never overwrite; save each update as a separate file with date
3. **Document all delays contemporaneously** — daily reports, delay notices, photos with timestamps
4. **Never delete or modify historical schedule data** — this destroys forensic evidence
5. **Use the delay tracker** — every delay event logged with date, cause, responsible party, duration
6. **Record actual dates** — actual start and actual finish for every activity, not just percent complete
7. **Maintain correspondence log** — RFIs, change orders, notices, and owner/architect directives all feed forensic analysis

---



## Schedule Specification Compliance

### DCMA 14-Point Assessment

The Defense Contract Management Agency (DCMA) 14-Point Assessment is the standard schedule health check for government and DOD projects. Even on non-government projects, these metrics provide an excellent framework for schedule quality assurance.

**The 14 Metrics:**

| # | Metric | Description | Threshold |
|---|--------|-------------|-----------|
| 1 | Logic | No open ends (activities without predecessors or successors) | 0% open ends |
| 2 | Leads | No negative lag (leads) | 0 leads |
| 3 | Lags | Limit positive lag | < 5% of relationships |
| 4 | Relationship Types | Minimize SS and FF relationships | > 90% FS relationships |
| 5 | Hard Constraints | Limit constraint use | < 5% of activities |
| 6 | High Float | Flag excessive total float | < 5% with TF > 44 days |
| 7 | Negative Float | No negative float | 0 activities with neg. float |
| 8 | High Duration | Flag excessively long activities | < 5% with duration > 44 days |
| 9 | Invalid Dates | All dates within project window | 0 invalid dates |
| 10 | Resources | All activities resource-loaded | 100% resourced |
| 11 | Missed Tasks | No tasks with actual dates past late dates | 0 missed tasks |
| 12 | Critical Path Test | 1-day delay test shifts completion by 1 day | Pass/Fail |
| 13 | CPLI (Critical Path Length Index) | (CP remaining + TF) / remaining duration | > 1.0 |
| 14 | BEI (Baseline Execution Index) | Completed / should-be-complete | > 0.90 |

**Common Failures and Remediation:**

- **Open ends:** Every activity must have at least one predecessor AND one successor (except project start and finish milestones). Fix: add missing logic links.
- **Leads (negative lag):** FS-5d means "start 5 days before predecessor finishes" — this hides logic. Fix: replace with SS+[appropriate lag] or add intermediate activities.
- **Hard constraints:** "Must Start On" or "Must Finish On" override schedule logic. Fix: use "Start No Earlier Than" or "Finish No Later Than" (softer constraints) where possible.
- **High duration activities:** Activities over 44 working days (approximately 2 months) lack granularity. Fix: break into smaller activities with meaningful milestones.
- **Negative float:** Indicates the schedule cannot meet a constraint or contractual date. Fix: investigate cause, add recovery logic, or negotiate date change.

### FAR Schedule Requirements

For projects governed by the Federal Acquisition Regulation (FAR):

- **Contract value < $1M:** Simplified schedule acceptable (bar chart)
- **Contract value $1M - $10M:** CPM schedule required, monthly updates
- **Contract value > $10M:** CPM schedule required, resource-loaded, monthly updates with narrative
- **All federal projects:** Initial baseline schedule due within [contract-specified] days of NTP
- **Update frequency:** Monthly at minimum; bi-weekly for critical or fast-track projects
- **Reporting:** Standard deliverables include schedule narrative, variance analysis, and critical path identification

### Schedule Health Metrics Beyond DCMA

**BEI (Baseline Execution Index):**

```
BEI = Tasks Completed / Tasks That Should Be Complete (per baseline)

BEI > 1.0  → Ahead of baseline (completing more tasks than planned)
BEI = 1.0  → On track with baseline
BEI 0.9-1.0 → Minor slippage, monitor closely
BEI < 0.9  → Significant slippage, recovery plan needed
BEI < 0.8  → Critical — re-baseline likely required
```

**Critical Path Length Ratio (CPLR):**

```
CPLR = (Critical Path Remaining Duration + Total Float) / Project Remaining Duration

CPLR > 1.0  → Project has float, likely to finish on time
CPLR = 1.0  → No float, any delay causes late finish
CPLR < 1.0  → Project WILL be late without recovery action
```

**Logic Density:**

```
Logic Density = Total Relationships / Total Activities

Target: > 1.5 (well-linked schedule)
1.0 - 1.5:  Adequate but may have open ends or weak logic
< 1.0:      Under-linked — schedule logic is incomplete
> 2.5:      May be over-constrained — review for unnecessary links
```

**Out-of-Sequence Progress:**

Activities that start or have progress recorded before their predecessors are complete. This indicates either:
- Actual work is out of sequence (may be intentional fast-tracking)
- Schedule logic is wrong (needs correction)
- Schedule is not being updated properly

Flag all out-of-sequence progress weekly. Resolve by either:
1. Updating logic to reflect actual sequence (if the change is intentional)
2. Stopping out-of-sequence work (if it creates risk)
3. Adding relationships to maintain the intended logic

### Integration with Weekly PPC Review

Schedule health metrics should be reviewed alongside PPC:

- **PPC + BEI together** tell you whether the team is reliable (PPC) AND whether that reliability is producing schedule progress (BEI)
- **High PPC + Low BEI** = team is completing commitments but the commitments are not the right activities (not on the critical path, not moving the schedule forward)
- **Low PPC + High BEI** = unusual, but possible if few commitments are made and most are completed
- **Low PPC + Low BEI** = systemic problem — both reliability and progress are failing
- **CPLR trending** should be tracked weekly alongside PPC trending
- **Out-of-sequence progress** should be flagged during the Friday scoring session

---



## Summary

The Last Planner System transforms construction scheduling from a static plan (created in the office, handed down to the field) to a **dynamic, constraint-driven commitment system** (created collaboratively by the trades who will do the work).

Key outcomes:
- **80%+ PPC** = reliable schedule = on-time delivery
- **Constraint focus** = problems surface weeks in advance, not days
- **Trade engagement** = foremen buy in because their input is valued
- **Continuous improvement** = Pareto analysis drives systematic problem-solving
- **Trust** = teams work together to clear constraints, not blame each other for delays

Last Planner is not a scheduling tool; it's a **management discipline**. Implement it rigorously, track PPC religiously, and adjust based on data. Within 4-8 weeks, your project's schedule reliability will transform.

## Weekly Plan Data Model (JSON Schema)

The Weekly Work Plan is captured in structured JSON to enable querying, trend analysis, and integration with dashboards.

```json
{
  "weekly_plans": [
    {
      "week_id": "WK-2026-08",
      "week_start": "2026-02-24",
      "week_end": "2026-02-28",
      "project_id": "MOSC-825021",
      "ppc_score": 75,
      "ppc_trend_4week": [68, 75, 82, 75],
      "planning_date": "2026-02-24",
      "planned_by": "John Smith (Super)",
      "ppc_by_trade": {
        "Walker Construction": {
          "commitments": 2,
          "completed": 2,
          "ppc": 100
        },
        "W Principles": {
          "commitments": 2,
          "completed": 1,
          "ppc": 50
        }
      },
      "variance_summary": {
        "prerequisites": 1,
        "material": 0,
        "labor": 0,
        "equipment": 0,
        "design": 0,
        "weather": 0,
        "space_access": 0,
        "rework": 0,
        "overcommitment": 0
      },
      "commitments": [
        {
          "commitment_id": "COMM-2026-08-001",
          "trade": "Walker Construction",
          "description": "Excavate south footing trench, lines X-1 to X-3, 2.5' depth",
          "location": "Building foundation, south side, grids X-1 to X-3",
          "scope_detail": "Linear excavation ~150 LF, remove topsoil and unsuitable fill, establish subgrade, compact to 98% Std Proctor",
          "schedule": {
            "committed_start": "2026-02-24",
            "committed_finish": "2026-02-26",
            "duration_days": 3
          },
          "constraints": {
            "design": {
              "status": "cleared",
              "evidence": "Civil drawings Sheet C-1.1, grading plan and footing elevations, survey locs provided, current"
            },
            "material": {
              "status": "cleared",
              "evidence": "Excavator + loader on site, fuel ready, ground thawed and compaction test slot booked"
            },
            "labor": {
              "status": "cleared",
              "crew_size": 1,
              "crew_names": ["Juan Rodriguez (Lead)", "2 laborers"],
              "evidence": "Walker crew available, OSHA Subpart P competent person certified, site orientation completed"
            },
            "equipment": {
              "status": "cleared",
              "equipment_list": ["Excavator CAT 320D", "Wheel loader CAT 906M"],
              "evidence": "Equipment on site, daily inspection completed, operators certified"
            },
            "prerequisites": {
              "status": "cleared",
              "evidence": "Site mobilization complete, SWPPP installed, utilities marked and located"
            },
            "space_access": {
              "status": "cleared",
              "evidence": "Site perimeter clear, temporary roads established, adjacent areas protected from dust"
            }
          },
          "constraint_free": true,
          "committed_by_name": "Juan Rodriguez",
          "committed_by_role": "Walker Construction Field Foreman",
          "committed_by_date": "2026-02-24T09:30:00Z",
          "committed_by_signature": "JR—signature on file",
          "notes": "Weather: 40F+ rising, ground thawed. Compaction testing by Terracon Wed 02/26 morning. Test results required before next phase (stem wall).",
          "status": "completed",
          "completion_date": "2026-02-26",
          "completion_notes": "Finished Wed as planned. Soil conditions excellent. Compaction test passed.",
          "variance_category": null
        },
        {
          "commitment_id": "COMM-2026-08-002",
          "trade": "W Principles",
          "description": "Set footing rebar X-1 to X-3, tie-off all connections",
          "location": "Building foundation, grids X-1 to X-3",
          "scope_detail": "Place and tie rebar per structural drawings: #5 bars at 12\" centers (main), #4 bars at 18\" (secondary), all connections per structural plans, layout to survey marks",
          "schedule": {
            "committed_start": "2026-02-25",
            "committed_finish": "2026-02-27",
            "duration_days": 3
          },
          "constraints": {
            "design": {
              "status": "cleared",
              "evidence": "Structural drawings S-2.1, S-2.2 rebar schedules; all connections detailed; no outstanding RFIs"
            },
            "material": {
              "status": "cleared",
              "evidence": "35 tons #5 and #4 rebar delivered 02/10, on site and dry under cover, mill certs on file"
            },
            "labor": {
              "status": "cleared",
              "crew_size": 3,
              "crew_names": ["Marcus Chen (Foreman)", "2 rebar specialists"],
              "evidence": "W Principles rebar crew available, trained and experienced, safety briefing completed"
            },
            "equipment": {
              "status": "cleared",
              "equipment_list": ["Rebar cutters", "Tie wire spoolers", "Scaffolding"],
              "evidence": "Equipment in yard, tools sharp and ready"
            },
            "prerequisites": {
              "status": "cleared",
              "evidence": "Excavation complete (COMM-2026-08-001), footing forms set and approved, compaction test passed"
            },
            "space_access": {
              "status": "cleared",
              "evidence": "Excavation area clear, work area marked, adjacent trades clear to proceed"
            }
          },
          "constraint_free": true,
          "committed_by_name": "Marcus Chen",
          "committed_by_role": "W Principles Concrete Foreman",
          "committed_by_date": "2026-02-24T10:00:00Z",
          "committed_by_signature": "MC—signature on file",
          "notes": "Building Official notification sent for HP-002 inspection (footing rebar) scheduled Thu 02/27 morning. Inspection required before concrete pour. Ready for inspection Thu AM.",
          "status": "completed",
          "completion_date": "2026-02-27",
          "completion_notes": "Crew finished tie-off Wed PM. HP-002 inspection passed Thu morning. Ready for concrete pour.",
          "variance_category": null
        },
        {
          "commitment_id": "COMM-2026-08-003",
          "trade": "W Principles",
          "description": "Build stem walls X-1 to X-4, pour concrete",
          "location": "Building perimeter, grids X-1 to X-4",
          "scope_detail": "Set stem wall forms (CFS and plywood), place concrete per mix design, cure and protect, strip forms after 3-day strength",
          "schedule": {
            "committed_start": "2026-02-28",
            "committed_finish": "2026-02-28",
            "duration_days": 1
          },
          "constraints": {
            "design": {
              "status": "cleared",
              "evidence": "Structural drawings S-2.3, S-2.4 show stem wall sections, elevations, and concrete specs; no outstanding details"
            },
            "material": {
              "status": "cleared",
              "evidence": "Concrete batch plant on standby, 80 CY ordered from Wells Concrete, delivery scheduled Fri 02/28, mix design approved 02/18"
            },
            "labor": {
              "status": "cleared",
              "crew_size": 4,
              "crew_names": ["Marcus Chen (Foreman)", "3 finishers"],
              "evidence": "W Principles concrete crew available, experienced in stem wall finishing"
            },
            "equipment": {
              "status": "cleared",
              "equipment_list": ["Concrete pump", "Vibrator"],
              "evidence": "Pump reserved for Fri, vibrator serviced and ready"
            },
            "prerequisites": {
              "status": "cleared",
              "evidence": "Footing rebar inspection passed (HP-002), footing forms still in place, foundation ready for stem wall"
            },
            "space_access": {
              "status": "cleared",
              "evidence": "Area cleared for concrete delivery truck and pump, staging area set"
            }
          },
          "constraint_free": true,
          "committed_by_name": "Marcus Chen",
          "committed_by_role": "W Principles Concrete Foreman",
          "committed_by_date": "2026-02-24T10:15:00Z",
          "committed_by_signature": "MC—signature on file",
          "notes": "Concrete delivery Fri 02/28. Forecast: 45-50F, clear. Temperature OK for placement. Forms will be built Thu/Fri morning; pour Fri afternoon if weather holds. 7-day cure required before removing forms; target form stripping ~03/07.",
          "status": "incomplete",
          "completion_date": null,
          "completion_notes": "Wells Concrete batch plant breakdown Thu evening. Delivery postponed to Mon 03/03. Crew on standby. Forms built Fri, ready for Mon pour. NOT COMPLETED THIS WEEK.",
          "variance_category": "prerequisites",
          "variance_notes": "Supplier equipment failure. Not the sub's fault. Rescheduled commitment to Week 9 (03/03 pour). No PPC penalty if force majeure; escalated to PM for supply chain management."
        },
        {
          "commitment_id": "COMM-2026-08-004",
          "trade": "W Principles",
          "description": "Install temporary site safety railing, south perimeter",
          "location": "Building perimeter, south side, full extent",
          "scope_detail": "Install 4' high temporary railing per OSHA Subpart P 1926.502, top rail, midrail, base, posts at 6' centers, secure fasteners",
          "schedule": {
            "committed_start": "2026-02-25",
            "committed_finish": "2026-02-26",
            "duration_days": 2
          },
          "constraints": {
            "design": {
              "status": "cleared",
              "evidence": "Safety plan (project document) specifies OSHA railing height and spacing; standard temporary railing details"
            },
            "material": {
              "status": "cleared",
              "evidence": "Temporary railing material (posts, rails, fasteners) delivered 02/20, on site and inventoried"
            },
            "labor": {
              "status": "cleared",
              "crew_size": 2,
              "crew_names": ["Marcus Chen (Foreman)", "1 laborer"],
              "evidence": "Crew available, OSHA trained, familiar with temporary railing installation"
            },
            "equipment": {
              "status": "cleared",
              "equipment_list": ["Power drill", "Fastener gun"],
              "evidence": "Tools available and functional"
            },
            "prerequisites": {
              "status": "cleared",
              "evidence": "Excavation area secured, work area established, no prior work required"
            },
            "space_access": {
              "status": "cleared",
              "evidence": "Perimeter clear, work area accessible from equipment staging zone"
            }
          },
          "constraint_free": true,
          "committed_by_name": "Marcus Chen",
          "committed_by_role": "W Principles Concrete Foreman",
          "committed_by_date": "2026-02-24T10:30:00Z",
          "committed_by_signature": "MC—signature on file",
          "notes": "Safety priority. Railing required to secure excavation area and meet OSHA compliance. Once installed, site is safer for all trades.",
          "status": "completed",
          "completion_date": "2026-02-26",
          "completion_notes": "Installed Tue-Wed as planned. Meets OSHA Subpart P standard. Inspector walked site; approved.",
          "variance_category": null
        }
      ],
      "constraint_log": [
        {
          "constraint_log_id": "CL-2026-08-001",
          "task_title": "Excavate north lot area, lines X-4 to X-5",
          "trade": "Walker Construction",
          "constraint_type": "prerequisites",
          "constraint_description": "Ground saturated from recent rain (2\" Tue-Wed). Soils not suitable for excavation per geotech specs. Cannot compact to 98% Std Proctor when wet.",
          "status": "open",
          "responsible_party": "Walker Construction / Super (site drainage verification)",
          "target_resolution": "2026-03-02",
          "escalation_trigger": "If not resolved by 02/28, delay PEMB foundation by 1 week",
          "notes": "Watch weather. If no rain and ground drains, can attempt Mon 03/03. If still wet, may delay through 03/05.",
          "resolution_plan": "Super to monitor ground moisture daily. Permit drainage time. Test soil with penetrometer before rescheduling excavation."
        }
      ]
    }
  ]
}
```

### Data Model Fields Explained

- **week_id**: Identifier for the planning week (format: WK-YYYY-##, where ## is ISO week number 01-53)
- **ppc_score**: This week's PPC result (0-100)
- **ppc_trend_4week**: Array of last 4 weeks' PPC values; used to plot trend
- **planning_date**: Date the weekly plan was created (usually Monday morning)
- **commitments**: Array of individual task commitments
  - **constraint_free**: Boolean; true only if all six constraints are "cleared"
  - **status**: "completed" or "incomplete"
  - **variance_category**: One of [prerequisites, material, labor, equipment, design, weather, space_access, rework, overcommitment] — only filled if incomplete
- **constraint_log**: Tasks screened out during planning (did not make the weekly commitment because constraints not cleared); tracked separately for make-ready action

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


