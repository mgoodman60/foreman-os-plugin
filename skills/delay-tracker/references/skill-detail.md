# delay-tracker — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the delay-tracker skill.



## Weather Delay Calculation Methodology

Weather delays require special handling: they are excusable only if conditions exceed contract thresholds **and** exceed normal weather patterns for the location.

### Weather Threshold Sources

**Contract Thresholds** come from `specs-quality.json` weather_thresholds object:
```json
"weather_thresholds": {
  "concrete": {
    "min_temperature_fahrenheit": 40,
    "max_temperature_fahrenheit": 90,
    "remarks": "ACI 306 minimum; ACI 305 maximum"
  },
  "roofing_operations": {
    "max_wind_mph": 25,
    "min_temperature_fahrenheit": 40,
    "remarks": "OSHA 1926.752 wind; sealant requirements"
  },
  "asphalt_paving": {
    "min_ambient_temperature_fahrenheit": 50,
    "min_surface_temperature_fahrenheit": 40,
    "remarks": "Contractor standard specifications"
  },
  "earthwork": {
    "forbidden_conditions": ["frozen_material", "excess_moisture"],
    "max_moisture_percent_of_optimum": "102",
    "remarks": "Proofroll requirements; frost-susceptible soils"
  }
}
```

### Weather Day Identification Process

**Step 1: Collect Daily Weather Data**
From daily reports (`daily-report-data.json` weather section) or NOAA records:
- Daily high/low temperature
- Precipitation (rain, snow)
- Wind speed (max gusts)
- Humidity / soil moisture conditions
- Special conditions (frost, ice, heat advisory, etc.)

**Step 2: Compare to Contract Thresholds**
For each day that work was scheduled but could not proceed:
- Was temperature below ACI 306 minimum of 40°F for concrete?
- Was wind speed above OSHA 25 MPH threshold during roofing operations?
- Was precipitation preventing earthwork from meeting compaction specifications?

**Step 3: Compare to NOAA 30-Year Baseline**
Weather delays must also demonstrate that conditions exceeded **normal weather patterns** for the location. Contract language typically states: "...weather conditions beyond those reasonably anticipated based on historical weather data for the project location."

**NOAA Comparison Process**:
- Obtain 30-year average data for project location and season (NOAA National Weather Service)
- For example, Morehead, KY typical February: avg low 32°F, avg high 47°F, avg precip 3.5"
- Compare actual weather during delay to 30-year normal:
  - If February low is 32°F and actual was 15°F: **exceeds normal** (justifiable weather delay)
  - If February low is 32°F and actual was 40°F but above ACI minimum: may NOT justify weather delay

**Documentation**:
```json
{
  "weather_data": {
    "actual_conditions": "2 days of freezing rain and snow; low temperatures 12°F; soil freeze depth 6 inches",
    "contract_threshold_exceeded": true,
    "threshold_type": "temperature_min",
    "contract_requirement": "40°F minimum for concrete placement (ACI 306)",
    "actual_temperature": "12°F",
    "noaa_baseline": "February normal low: 32°F",
    "exceeds_baseline": true,
    "baseline_variance": "20 degrees below normal; approximately 3-sigma event",
    "justification": "Weather conditions significantly below historical norms; work stoppage necessary for contract compliance and worker safety"
  }
}
```

### Weather Delay Documentation Requirements

- **Daily weather observations** from daily reports (temperature, precipitation, wind)
- **NOAA data** from National Weather Service for project location
- **Contract specification references** (ACI 306, OSHA standards, etc.)
- **Photos** showing conditions (frozen ground, mud, ice, snow, etc.)
- **Foreman notes** on why work could not proceed
- **Schedule activities** that were prevented (concrete placement, roofing, earthwork, etc.)

### Weather Delay Reporting

Include in delay-log entry:
```json
{
  "type": "weather",
  "date_start": "2026-02-15",
  "date_end": "2026-02-17",
  "calendar_days": 3,
  "weather_data": {
    "actual_conditions": "Heavy freezing rain, snow accumulation 4 inches; ambient low 18°F",
    "contract_threshold_exceeded": true,
    "threshold_type": "temperature_min",
    "contract_requirement": "40°F minimum (ACI 306)",
    "noaa_baseline_comparison": "February normal low 32°F; actual 18°F is 2.33 standard deviations below normal"
  },
  "linked_daily_reports": ["2026-02-15", "2026-02-16", "2026-02-17"],
  "activities_impacted": ["Concrete Footings C1-C6"],
  "excusable": true,
  "compensable": false,
  "extension_days_earned": "[determined by critical path analysis]"
}
```

---



## Concurrent Delay Identification and Handling

Concurrent delays occur when multiple delays overlap in time and potentially affect the same critical path activities. Proper handling is essential for contract accuracy and defense against claims disputes.

### Definition & Detection

**Concurrent Delays** = Two or more delays occurring simultaneously (overlapping date ranges) that **potentially** impact the same activity or critical path sequence.

**Detection**:
When logging a new delay, query existing delays:
- Are dates overlapping with DELAY-001, DELAY-002, etc.?
- Are the delayed activities on the same critical path sequence?
- Could the delays have been avoided if the other delay had not occurred?

**Example**:
```
DELAY-001: Owner decision delays MEP approval 2026-02-20 to 2026-02-27 (7 days)
DELAY-002: Sub performance delays MEP rough-in 2026-02-25 to 2026-03-04 (7 days)

Overlap Period: 2026-02-25 to 2026-02-27 (3 days concurrent)
Potential Concurrent Impact: YES (both delays affect MEP activity)
```

### Concurrent Delay Impact Rules

**Rule 1: Single Critical Path (most common)**
If both delays affect the same activity on the critical path:
- **Total Extension** = MAX(delay_1, delay_2), NOT sum
- Concurrent delays don't stack; use longest single delay
- Example: 7-day owner delay + 7-day sub delay = **7-day extension** (not 14)

**Rule 2: Different Paths**
If delays affect different activities on different paths:
- Calculate float absorption separately for each path
- **Total Extension** = SUM of excusable delays that consume their own critical path impact
- Example: 5-day delay on Path 1 (no float) + 3-day delay on Path 2 (6 days float) = **5-day extension** (Path 2 absorbed by float)

**Rule 3: Causation Analysis**
Key question for each concurrent delay: **Would this delay have occurred but-for the other delay?**

```
Scenario A: Owner delay causes downstream sub delay
  - Owner delays decision 7 days
  - Sub cannot mobilize, resulting in additional 7-day delay
  - This is causation: sub delay is consequence of owner delay
  - Single extension = 7 days (not 14)
  - Responsibility: Owner for entire 14 days (owner's action caused both)

Scenario B: Independent concurrent delays
  - Owner delays decision 7 days (unrelated to sub work)
  - Sub also delayed 7 days (supply chain issue, independent of owner decision)
  - Delays overlap but don't cause each other
  - Extension calculation depends on critical path analysis:
    - If both on critical path, extension = 7 days max (longest single delay)
    - If one has float, extension = amount exceeding float

Scenario C: Contractor-caused delay masks owner delay
  - Contractor's poor planning creates 5-day float buffer
  - Owner-directed change would have caused 10-day delay
  - Contractor's incompetence "absorbs" owner's delay through positive float
  - Extension = 0 (float absorbed)
  - BUT: Owner still responsible for the change; contractor cannot benefit from own inefficiency
  - This is a disputed area; courts vary on "efficient breach" doctrine
```

### Documenting Concurrent Delays in Delay Log

```json
{
  "id": "DELAY-003",
  "type": "sub_performance",
  "date_start": "2026-02-25",
  "date_end": "2026-03-04",
  "calendar_days": 7,
  "concurrent_delays": ["DELAY-001"],
  "causation_analysis": {
    "related_delay_id": "DELAY-001",
    "overlap_dates": "2026-02-25 to 2026-02-27",
    "independent": false,
    "causation": "Owner delay (DELAY-001) prevented sub mobilization; sub unable to sequence work around owner decision.",
    "responsibility_allocation": "Primary: DELAY-001 (owner); this sub delay is consequential to owner's delay"
  },
  "critical_path_impact": "absorbed_float (through DELAY-001 extension)",
  "extension_days_earned": 0,
  "notes": "This delay occurs during owner-directed suspension. Critical path analysis shows extension already earned through DELAY-001. Sub delay does not independently extend project beyond DELAY-001 impact."
}
```

### Concurrent Delay Claim Risks

**From Contractor Perspective**:
- Concurrent delays can reduce time extension if contractor caused any delay
- "Concurrent Delay Defense" (owner response): Even though owner caused a delay, contractor's concurrent delay means owner didn't cause the overall delay
- Example: Owner delay 7 days + Contractor delay 7 days (concurrent) = Owner may argue NO extension owed (contractor's delay also pushing schedule)

**From Owner Perspective**:
- If contractor claims concurrent delay was owner-caused, contractor must prove causation
- Owner may dispute contractor's claim if contractor also had partial responsibility

**Best Practice**:
Document concurrent delays thoroughly:
1. Identify date overlap
2. Analyze causation (would the other delay have occurred independently?)
3. Perform separate critical path analysis for each delay
4. Include explicit causation analysis in delay log notes
5. Support with daily reports, RFIs, change orders, photographs

---



## Contract Extension Request Document Template

A contract extension request is a formal written request to the owner (typically via the project manager or architect) asking for an extension of the project completion date based on excusable delays.

### Document Structure

#### Cover Memo
```
TO:       [Project Manager Name/Title]
FROM:     [General Contractor Name, Superintendent Name]
DATE:     [Submission Date]
RE:       Request for Time Extension — [Project Name], [Project No.]
          Delays: [DELAY-001, DELAY-002, etc.]

This letter requests a time extension of [X] calendar days from the Substantial Completion date due to delays beyond Contractor's control, as detailed below.
```

#### Executive Summary
- Original Substantial Completion date: [Date]
- Requested Substantial Completion date: [New Date]
- Extension requested: [X] calendar days
- Basis: Excusable delays per Contract [reference contract article, e.g., "AIA A132, §8.3"]
- Supporting documentation: Attached (daily reports, RFIs, change orders, weather data)

#### Delay Summary Table
| Delay ID | Type | Date Range | Calendar Days | Float Consumed | Extension Days | Supporting Evidence |
|----------|------|------------|----------------|-----------------|-----------------|-------------------|
| DELAY-001 | Weather | 2/15-2/17 | 3 | 0 | 3 | Daily Reports 2/15-2/17, NOAA data |
| DELAY-002 | Design Issue | 3/1-3/8 | 8 | 2 | 6 | RFI-007, Architect Addendum 02 |
| | | | | **TOTAL** | **9 days** | |

#### Detailed Delay Narratives

For each delay, include 2-3 page narrative:

**Example: Weather Delay Narrative**
```
DELAY-001: Weather — Concrete Placement Delay (February 15-17, 2026)

Delay Overview:
Scheduled concrete placement for footings C1-C6 could not proceed due to ambient temperatures below ACI 306 minimum threshold of 40°F. Weather conditions during February 15-17 were significantly below historical norms for Morehead, Kentucky, preventing safe concrete operations.

Weather Conditions:
- February 15: Low 18°F, high 22°F; freezing rain with snow accumulation
- February 16: Low 12°F, high 20°F; continuing snow and ice
- February 17: Low 15°F, high 28°F; partially clearing by afternoon
- Weather source: NOAA National Weather Service, Cincinnati, Kentucky office

Contract Requirements:
ACI 306 (Specification 03300, Section 3.1.2) requires minimum ambient temperature of 40°F for concrete placement. The work was not rescheduled to avoid excessive cold weather protection requirements and associated costs.

Comparison to Historical Baseline:
NOAA 30-year normal for Morehead, Kentucky in February: Low 32°F, High 47°F
Actual conditions were 14-20 degrees below normal, representing a 2+ standard deviation event.

Critical Path Impact:
Concrete placement (Activity C1-FOUND) is on critical path with zero float. The 3-day delay directly extended critical path duration by 3 days.

Documentation:
- Daily reports dated 2/15, 2/16, 2/17 document actual temperature observations
- Daily reports note work suspension decision and communication with trades
- NOAA weather data attached as Exhibit A
- Photographs taken 2/16 showing ice and snow conditions at site

Extension Earned:
3 calendar days (zero float consumed; full extension to critical path)
```

**Example: Design Issue Narrative**
```
DELAY-002: Design/Specification Issue — MEP Coordinated Review (March 1-8, 2026)

Delay Overview:
Conflicts identified between mechanical (HVAC) design and structural framing required architect-coordinated re-review and modification of equipment placement. The scope remained unchanged; resolution required re-coordination and design verification, delaying mechanical roughing-in start date.

Trigger Event:
During pre-rough-in coordination meeting on March 1, Contractor's mechanical subcontractor (Davis & Plomin) identified that designed AHU location in south wing exceeded structural column limits by 8 inches and would not fit within building envelope per plans (Sheet M2.1).

Design Issue:
Plans (Sheet M2.1) showed AHU centerline 4" from structural column (per Structural Sheet S2.3). Actual structural column size and location per field verification showed only 4" clearance on opposite side of column, insufficient for equipment and ductwork routing.

Architect Resolution:
- RFI-007 submitted March 1 documenting conflict
- Architect issued revision to Sheet M2.1 on March 8
- Mechanical layout modified; equipment relocated to east wall location
- Revised submittal cycle required March 8-15 for new AHU support design

Timeline:
- March 1: Conflict identified; RFI-007 submitted
- March 1-7: Awaiting architect response (6-day wait)
- March 8: Architect issues revised drawing
- March 8-15: Subcontractor revises support system and re-submits (7-day cycle)

Activities Delayed:
- MEP Rough-In (originally scheduled 3/1 start) delayed to 3/15
- Related activities pushed: Duct testing (3/15→3/22), System startup (7/20→7/27)

Critical Path Impact:
MEP Rough-In is critical path activity. Delay of 2 days consumed 2 days of pre-existing float schedule. Remaining 6-day delay (8 days total - 2 float) extended critical path by 6 days.

Responsibility:
This conflict was design-related. The Contractor's responsibility was to identify the conflict during construction (which was performed as a courtesy). The Architect's responsibility is design adequacy per contract documents.

Documentation:
- RFI-007 and Architect's response (Exhibit B)
- Revised drawing dated 3/8 (Exhibit C)
- Original drawing with conflict notation (Exhibit D)
- Daily reports dated 3/1-3/8 documenting coordination efforts
- Mechanical subcontractor's revised submittal dated 3/15 (Exhibit E)

Extension Earned:
8 calendar days delay (2 days float consumed + 6 days extension to critical path)
```

#### Critical Path Analysis Summary
Include diagram or table showing:
- Original baseline critical path
- Activities affected by delays
- Updated critical path with actual dates
- Calculation of total extension earned: SUM of excusable delays minus float consumed

#### Supporting Documentation Attachments
- Daily reports (specific dates linked to each delay)
- RFIs and architect responses
- Change orders (if applicable)
- Weather data (NOAA printouts)
- Photographs (time-stamped)
- Correspondence with owner/architect regarding delay
- Meeting minutes discussing delays
- Submittal/approval documents showing delay impacts

#### Signature Block
```
By submitting this request, Contractor represents that:
1. The delays described are accurate and documented with contemporaneous records
2. All information is true and correct to the best of Contractor's knowledge
3. Contractor has not previously requested time extension for these same delays
4. Delays are excusable under the Contract and documented per AIA standard

Respectfully submitted,

_____________________________          Date: __________
[Superintendent Name], Superintendent

_____________________________          Date: __________
[PM or Company Officer], Project Manager
```

### Approval by Owner/Architect

```
APPROVED / APPROVED AS NOTED / DENIED

_____________________________          Date: __________
[Owner/Architect Representative]

If "Approved As Noted", provide explanation:
_________________________________________________________________
_________________________________________________________________
```

---



## Delay Claim Documentation Requirements

A delay claim is a request for both **time extension** (calendar days) **and** **cost recovery** (dollars for extended overhead, labor, equipment, financing).

### Claim Eligibility

Delay claims require **BOTH**:
1. **Compensable Delay**: Delay caused by owner/architect/third party (not contractor)
2. **Excusable Delay**: Delay not contractor's responsibility per contract
3. **Quantifiable Cost Impact**: Documented costs directly caused by the delay

### Documentation Framework

Delay claims rest on **five foundational elements**:

#### 1. **Causation**
Contractor must establish that:
- The alleged event (owner directive, design change, permit delay, etc.) **actually occurred**
- The delay **directly resulted** from that event (cause-and-effect)
- The delay **was not caused** by contractor's own actions or inefficiency

**Documentation**:
- Contemporaneous daily reports (dated, signed, detailed)
- Owner directives, emails, meeting notes
- RFI responses and architect clarifications
- Permit applications and approval letters
- Photos showing conditions necessitating delay

**Language Example**:
"On March 1, 2026, the Project Manager directed the Contractor to suspend MEP rough-in work pending architect review of structural coordination issues (RFI-007). Work remained suspended until March 8, 2026, when the architect issued revised drawings. This suspension was directly caused by the owner's design review requirement and prevented the mechanical subcontractor from continuing scheduled work."

#### 2. **Delay Impact Quantification**
Contractor must prove:
- The **actual duration** of work delay (calendar days)
- **Only the excusable portion** of delays qualifies for extension
- **Critical path analysis**: whether delay consumed float or extended completion date

**Documentation**:
- Baseline schedule (original contract schedule)
- As-planned schedule (what was planned to happen)
- As-built schedule (what actually happened)
- Critical path analysis showing impact on completion date
- Daily reports documenting actual work dates

**Calculation Example**:
```
Original Completion Date: July 29, 2026 (per contract)
Actual Completion Date: August 5, 2026 (7 days later)

Excusable Delays Identified:
  DELAY-001 (Weather): 3 calendar days (float: 0) → 3-day extension
  DELAY-002 (Design): 8 calendar days (float: 2) → 6-day extension
  DELAY-003 (Material): 4 calendar days (float: 4) → 0-day extension (float absorbed)

Total Extension Earned: 3 + 6 + 0 = 9 days

Actual Delay: 7 days (Aug 5 - July 29)
Variance: 9 days claimed vs. 7 days actual

Explanation: DELAY-002's 8-day impact was partially concurrent with other work; critical path analysis showed final impact of only 6 days. Total of 9 days excusable delay earned; actual project only delayed 7 days due to concurrent activity absorbing some impact.
```

#### 3. **Cost Impact Documentation**
Contractor must document **all costs directly caused** by the delay:

**Extended General Conditions**:
- Project management (superintendent, PM salaries) for extended days
- Temporary facilities (site office, equipment, utilities)
- Project insurance (cost increase for extended duration)
- Bonding (cost increase for extended contract period)
- Loan interest on construction financing (if financed)

**Calculation**:
```
Extended General Conditions = Daily G&A Rate × Extended Days

Example (weather delay):
  Daily G&A = $2,500/day (superintendent + PM + site office + insurance)
  Extension Days = 3 days
  Cost = $2,500 × 3 = $7,500

Must Document:
  - G&A budget/estimate showing daily rate
  - Actual costs (payroll records, insurance invoices, bond fees)
  - Time tracking showing staff present during extended period
```

**Labor/Equipment Restoration**:
- Crew re-mobilization costs (if project suspended >30 days)
- Equipment demobilization/re-mobilization (cranes, scaffolding, etc.)
- Expediting costs (accelerated work to recover schedule)
- Overtime (if acceleration measures were employed)

**Material Cost Increases**:
- Price escalation on materials held in inventory during delay
- Supplier storage costs
- Re-delivery costs if material had to be re-sourced

**Subcontractor Compensation**:
- Extended overhead claims from subcontractors
- T&M costs for work required to address delay causes

#### 4. **Contemporaneous Documentation**
Claims must rest on **contemporaneous records** (created at time of event, not reconstructed later):

**Acceptable**:
- Daily reports dated and signed on day of observation
- Email correspondence with dates
- RFI submittals and architect responses with dates
- Permit letters and agency correspondence
- Photographs with EXIF metadata (date/time stamp)
- Weather data from NOAA official records

**Unacceptable or Weak**:
- Reconstructed daily reports created weeks/months after the fact
- Emails forwarded without original dates
- Hand-written notes without date/signature
- Oral testimony without supporting documentation
- Photographs without time-stamp or location identification

**Best Practice**:
Every day on a construction project, document:
- Weather (temperature, precipitation, wind, conditions affecting work)
- Crew (subcontractors present, headcount, work performed)
- Equipment (equipment on site, operational status)
- Schedule impacts (any work blocked, delayed, or rescheduled)
- Visitors (inspectors, owner reps, architects, observations made)
- Issues (RFIs submitted, conflicts identified, concerns raised)

### Time Impact Analysis (TIA) Methodology Overview

A Time Impact Analysis (TIA) is a systematic methodology for quantifying the impact of a specific delay event on project schedule. It's the gold standard for demonstrating delay causation and quantification.

#### TIA Process

**Step 1: As-Planned Schedule**
Establish baseline schedule from contract documents:
- Activities, durations, dependencies
- Critical path
- Project completion date

**Step 2: Update Schedule to Point of Delay Event**
Update baseline schedule to reflect all work completed and in-progress up to the delay event date:
- Incorporate actual progress through delay event date
- Mark activities completed, in-progress, or not yet started
- Verify critical path remains consistent with baseline (or note changes)

**Step 3: Insert Hypothetical Delay Event**
Add the specific delay event to the schedule:
- Suspend the affected activity(ies) for the stated delay duration
- Recalculate schedule with the suspension in place
- Note the new completion date

**Step 4: Calculate Impact**
Compare:
- Original completion date (baseline or updated-to-delay-date)
- Completion date with delay event inserted
- **Difference = Quantified delay impact**

**Step 5: Document Assumptions**
Record:
- What activities are affected by the delay?
- How long does the delay last?
- Does the delay create a bottleneck (critical path) or is there workaround (float)?
- Are there mitigation measures (acceleration, re-sequencing)?
- What assumptions were made about resource availability?

#### TIA Example

```
Project: Morehead One Senior Care
Delay Event: Owner approval delay for MEP design (RFI-007)

BASELINE SCHEDULE ANALYSIS:
  Original Substantial Completion: July 29, 2026
  Critical Path: Foundation → Structural Steel → MEP Rough-In → MEP Finish → Final
  MEP Rough-In Start: March 1, 2026 (per contract schedule)
  MEP Rough-In Duration: 20 days
  MEP Rough-In Float: 0 days (critical)

ACTUAL SEQUENCE:
  Design coordination meeting: March 1, 2026
  Conflict identified (AHU placement vs. structure)
  RFI-007 submitted: March 1, 2026
  Architect response issued: March 8, 2026 (7-day delay)
  Revised submittal review/approval: March 15, 2026
  MEP Rough-In actually started: March 15, 2026 (14 days late vs. baseline)

TIA ANALYSIS:
  Delay Duration: 8 calendar days (March 1 RFI → March 8 revised drawing + 5 days for resubmittal = 8 days)
  Float Consumed: 2 days (MEP had 2 days pre-delay float in schedule margin)
  Critical Path Extension: 8 - 2 = 6 days

  New Completion Date: July 29 + 6 days = August 4, 2026

IMPACT QUANTIFICATION:
  Extended General Conditions: 6 days × $2,500/day = $15,000
  Additional Labor (MEP subcontractor OT): $8,000
  Extended Equipment Rental: $3,200
  Total Compensable Cost: $26,200

CAUSATION:
  Cause: Owner decision to require design coordination approval (outside contract baseline)
  Effect: MEP rough-in delayed 8 calendar days
  Contractor Action: Prompt identification of conflict and RFI submittal
  Contractor Responsibility: None; event caused by owner/architect design review requirement
```

### Integration with Daily Reports

Delay claims depend on **daily report documentation**. Each delay event must be linked to specific daily reports that contemporaneously document:
- The event or condition creating the delay
- The decision to suspend or modify work
- The impact on activities
- The duration of the delay

**Daily Report Linkage**:
```
DELAY-002: Design Issue
  linked_daily_reports: ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", "2026-03-06", "2026-03-07", "2026-03-08"]

  2026-03-01 Entry:
    "MEP coordination meeting at 10:00 AM. AHU placement conflict identified between mechanical layout (Sheet M2.1) and structural framing (Sheet S2.3). Equipment would not fit in designed location. RFI-007 submitted to architect requesting design revision. Mechanical subcontractor directed to stand by; MEP rough-in work cannot proceed pending architect clarification."

  2026-03-02 to 2026-03-07 Entries:
    "Awaiting architect response to RFI-007. Mechanical subcontractor on standby. No progress on MEP rough-in."

  2026-03-08 Entry:
    "Architect issued revised drawing (Sheet M2.1 Rev A). New AHU location specified in east wall. Mechanical subcontractor will prepare revised equipment support design. Resubmittal review expected within 7 days."
```

These daily report entries create the contemporaneous record proving the delay event, its duration, and the work impacts.

### Claim Documentation Checklist

Before submitting a delay claim, verify:

**Causation Evidence**:
- [ ] Daily reports documenting the event (dated, signed)
- [ ] Owner directive, email, or decision creating the delay
- [ ] RFI responses or architect clarifications documenting delay cause
- [ ] Meeting minutes or email confirming delay event
- [ ] Contemporaneous correspondence (no retroactive documents)

**Delay Quantification**:
- [ ] Baseline schedule clearly identified
- [ ] Updated schedule showing delay impact
- [ ] Critical path analysis (float vs. extension)
- [ ] Calendar day quantification with documented start/end dates
- [ ] TIA worksheet or schedule analysis

**Cost Documentation**:
- [ ] G&A budget with daily rate breakdown
- [ ] Payroll records showing extended staff presence
- [ ] Insurance/bonding invoices showing cost increase
- [ ] Subcontractor invoices for extended time
- [ ] Equipment rental invoices
- [ ] All invoice dates must correspond to extended period

**Supporting Documentation**:
- [ ] Photographs with date/time metadata
- [ ] Weather data (NOAA records if weather delay)
- [ ] Permit correspondence (if permit delay)
- [ ] All RFI/CO documentation (if design/scope issue)
- [ ] Correspondence with owner/architect regarding delay

**Compliance with Contract**:
- [ ] Delay falls within contract definition of excusable delay
- [ ] Claim submitted within contract notice period (typically 10-30 days of delay event)
- [ ] Contractor not also in breach of contract
- [ ] All mitigation efforts documented (acceleration, workarounds)

---



## Critical Path Impact Documentation

Proper documentation of critical path impact is the foundation of any delay claim or contract extension request. Each delay event must include a clear, defensible record of how it affected the project schedule.

### Documenting Critical Path Impact for Each Delay Event

Every delay entry in the delay log must include a critical path impact narrative that addresses:

1. **Baseline Schedule Reference**: Identify the baseline schedule version and date used for analysis. Reference the specific activity ID, activity name, and its position on the critical path or near-critical path.

2. **Activity Float Before Delay**: Record the total float (TF) and free float (FF) for the affected activity immediately before the delay event occurred. Pull this data from the most recent schedule update.

3. **Delay Duration and Type**: State the calendar days of delay, the delay type classification, and whether the delay is excusable, compensable, or both.

4. **Critical Path Determination**: Explicitly state whether the delayed activity was on the critical path (zero total float) or near-critical (total float less than or equal to 5 days). Near-critical activities require monitoring because they can become critical if float is consumed.

5. **Downstream Activity Identification**: List every successor activity affected by the delay, including activity ID, activity name, trade responsible, and the number of days each successor is pushed.

6. **Revised Completion Date**: State the original completion date, the revised completion date after the delay, and the net extension earned.

### Demonstrating Float Consumption: Before and After Float Analysis

Float analysis is the most powerful tool for proving (or disproving) delay impact. A before-and-after float analysis compares the schedule state immediately before the delay event to the schedule state immediately after.

**Before-Delay Snapshot**:
```
Activity: MEP Rough-In (ACT-045)
Baseline Duration: 20 days
Baseline Start: March 1, 2026
Baseline Finish: March 20, 2026
Total Float (TF): 4 days
Free Float (FF): 2 days
Critical Path: NO (near-critical)
Project Completion Date: July 29, 2026
```

**After-Delay Snapshot**:
```
Activity: MEP Rough-In (ACT-045)
Delay Event: DELAY-002 (Design Issue, 8 calendar days)
Revised Start: March 9, 2026
Revised Finish: March 28, 2026
Total Float (TF): 0 days (consumed 4 days; exceeded by 4 days)
Free Float (FF): 0 days
Critical Path: YES (delay consumed all float and extended critical path)
Revised Project Completion Date: August 2, 2026
Extension Earned: 4 days (8-day delay minus 4 days float consumed)
```

**Float Consumption Summary Table**:
```
Activity ID   Activity Name     TF Before   Delay Days   TF After   Float Consumed   Extension Earned
ACT-045       MEP Rough-In      4           8            0          4                4
ACT-046       Duct Testing      6           0 (pushed)   2          4 (inherited)    0
ACT-047       System Startup    3           0 (pushed)   0          3 (inherited)    1 (cumulative)
```

### Impact Analysis: Fragnet Methodology

A **fragnet** (fragment network) is a small sub-network of activities inserted into the baseline schedule to model the delay event. This is the industry-standard methodology for Time Impact Analysis (TIA).

**Fragnet Construction Process**:

1. **Identify the Insertion Point**: Determine where in the schedule the delay event occurs. The fragnet attaches to the activity that was interrupted or delayed.

2. **Create the Delay Activity**: Add a new activity representing the delay itself:
   - Activity Name: "DELAY-002: Design Coordination Delay (RFI-007)"
   - Duration: 8 calendar days
   - Predecessor: ACT-044 (activity immediately before the delay)
   - Successor: ACT-045 (the activity that was delayed)

3. **Insert into Baseline Schedule**: Place the fragnet between the predecessor and the delayed activity. The fragnet creates a new path through the schedule that models the actual delay.

4. **Recalculate Schedule**: Run a forward pass and backward pass through the updated schedule. The difference between the original completion date and the new completion date equals the delay impact.

5. **Document the Results**: Record the fragnet activity, its predecessors and successors, the recalculated critical path, and the net impact on project completion.

**Fragnet Example**:
```
BEFORE FRAGNET:
  ACT-044 (Structural Steel) → ACT-045 (MEP Rough-In) → ACT-046 (Duct Testing)
  Critical Path Duration: 150 days
  Completion: July 29, 2026

AFTER FRAGNET INSERTION:
  ACT-044 (Structural Steel) → DELAY-002 (8 days) → ACT-045 (MEP Rough-In) → ACT-046 (Duct Testing)
  Critical Path Duration: 154 days (+4 days after float absorption)
  Completion: August 2, 2026 (+4 days extension)
```

### Documenting Ripple Effects on Downstream Activities

Delay events rarely affect only a single activity. Ripple effects propagate through the schedule via predecessor-successor relationships. Documenting these ripple effects is critical for proving the full scope of a delay.

**Ripple Effect Documentation Template**:

```
DELAY EVENT: DELAY-002 (Design Issue, 8 calendar days, March 1-8, 2026)

PRIMARY IMPACT:
  Activity: ACT-045 MEP Rough-In
  Original Start: March 1, 2026 → Revised Start: March 9, 2026
  Float Consumed: 4 days | Extension Earned: 4 days

SECONDARY IMPACTS (Downstream Activities):

  Activity ID    Activity Name           Original Start   Revised Start   Days Pushed   Trade Affected
  ACT-046        Duct Testing            March 21         March 29        8             HVAC
  ACT-047        System Startup          March 28         April 5         8             HVAC
  ACT-048        Ceiling Grid Install    March 25         April 1         6             Drywall/Ceiling
  ACT-049        Sprinkler Trim-Out      March 30         April 7         8             Fire Protection
  ACT-050        Paint Prep              April 2          April 8         6             Painting
  ACT-051        Flooring Install        April 10         April 16        6             Flooring

CASCADING PATH ANALYSIS:
  Path 1 (Critical): ACT-045 → ACT-046 → ACT-047 → ACT-055 (Final Inspection)
    Impact: 4 days extension to project completion

  Path 2 (Near-Critical): ACT-045 → ACT-048 → ACT-050 → ACT-051
    Impact: 6 days pushed; 2 days float remaining (does not extend completion)

  Path 3 (Non-Critical): ACT-049 (independent successor)
    Impact: 8 days pushed; 5 days float remaining (absorbed)
```

### Establishing Contemporaneous Schedule Record

A contemporaneous schedule record is a schedule update created at or near the time of the delay event, not reconstructed after the fact. Courts and arbitrators give much greater weight to contemporaneous records than to after-the-fact analyses.

**Requirements for Contemporaneous Schedule Record**:

1. **Monthly Schedule Updates**: Update the project schedule at least monthly (or per contract requirements) with actual start dates, actual finish dates, remaining durations, and percent complete for all activities.

2. **Delay Event Schedule Snapshots**: When a significant delay event occurs, create a schedule snapshot immediately:
   - Save a copy of the schedule file with the date in the filename
   - Example: `schedule_update_2026-03-01_pre-DELAY-002.json`
   - Run critical path analysis and save the results

3. **Daily Report Cross-Reference**: Each schedule update must cross-reference the daily reports that document actual progress. The daily report dates and the schedule actual dates must be consistent.

4. **No Retroactive Manipulation**: Never alter past schedule updates. If an error is found, create a new update with a correction note, not a modification of the original file.

5. **Schedule Narrative**: Accompany each schedule update with a brief narrative explaining progress, delays, and any changes to the critical path. This narrative becomes part of the contemporaneous record.

**Documentation Best Practice**:
```
SCHEDULE UPDATE NARRATIVE — March 1, 2026

Progress This Period:
  Structural steel erection 100% complete (on schedule)
  Foundation work 100% complete (on schedule)
  MEP rough-in NOT started (delayed — see DELAY-002)

Delay Events This Period:
  DELAY-002: Design coordination issue identified March 1. RFI-007 submitted.
  MEP rough-in start pushed from March 1 to TBD pending architect response.
  Critical path impact: Pending — will update upon architect resolution.

Critical Path Status:
  Original critical path unchanged through structural steel.
  MEP rough-in now on critical path (float consumed by DELAY-002).
  Monitoring: If architect responds by March 8, 4-day extension earned.
  If response delayed beyond March 8, additional extension may be required.

Next Update: March 8, 2026 (or upon architect response to RFI-007)
```

---



## Concurrent Delay Identification and Allocation

### Definition of Concurrent Delay

Concurrent delay occurs when two or more independent delay events affect the critical path during overlapping time periods. This is one of the most complex and disputed areas of construction delay analysis. Proper identification, classification, and allocation of concurrent delays is essential for defensible claims and fair contract administration.

**Key Principle**: For delays to be truly concurrent, they must:
1. Occur during overlapping time periods (not merely sequential)
2. Each independently affect the critical path (or would affect it but-for the other delay)
3. Be caused by different responsible parties (e.g., one owner-caused, one contractor-caused)

### Types of Concurrent Delay

**1. True Concurrent Delay**
Two or more delays occur at exactly the same time and both independently extend the critical path. Neither delay would be absorbed by float even if the other delay had not occurred.

```
Example:
  DELAY-A: Owner suspends work on Wing A (Days 50-60, 10 days, owner-caused)
  DELAY-B: Contractor equipment breakdown on Wing B (Days 50-57, 7 days, contractor-caused)

  Both delays affect critical path activities simultaneously.
  Both would independently extend the project if the other had not occurred.
  This is TRUE concurrent delay.
```

**2. Sequential Concurrent Delay**
Two delays occur in sequence but overlap such that the second delay begins before the first delay ends. The overlap period is concurrent; the non-overlapping periods are sequential.

```
Example:
  DELAY-A: Owner design review (Days 50-65, 15 days, owner-caused)
  DELAY-B: Material delivery delay (Days 60-72, 12 days, contractor-caused)

  Overlap: Days 60-65 (5 days concurrent)
  DELAY-A alone: Days 50-60 (10 days sequential, owner-only)
  DELAY-B alone: Days 65-72 (7 days sequential, contractor-only)
```

**3. Pacing Delays**
A subcontractor or trade intentionally slows its work pace to match another delay that is already pushing the schedule. Pacing delays are NOT true concurrent delays because the pacing party would not have been delayed but-for the primary delay.

```
Example:
  Owner delay pushes MEP rough-in start by 10 days.
  Electrical sub slows mobilization to match the new MEP start date (pacing).
  Electrical delay is NOT concurrent — it is caused by the owner delay.
  Owner bears full responsibility for the extension.
```

### Allocation Methods

When concurrent delays are identified, several allocation methods may apply depending on contract language and jurisdiction:

**1. Apportionment Method**
Divide the delay impact proportionally between the responsible parties based on the relative severity or duration of each delay.

```
Example:
  Total concurrent delay period: 10 days
  Owner delay impact: 7 days (primary cause)
  Contractor delay impact: 5 days (secondary cause)
  Apportionment: Owner 70% (7 days), Contractor 30% (3 days)
  Extension granted: 7 days (owner's apportioned share)
```

**2. Dominant Cause Method**
Identify the dominant (primary) cause of the concurrent delay and assign full responsibility to that party. The dominant cause is the delay that would have caused the most impact even if the other delay had not occurred.

```
Example:
  Owner delay: 10 days (would extend critical path 10 days alone)
  Contractor delay: 3 days (would extend critical path 3 days alone)
  Dominant cause: Owner (10 days > 3 days)
  Extension granted: 10 days (full owner delay, minus contractor float if applicable)
```

**3. All-or-Nothing Method**
If the contractor contributed any concurrent delay, the contractor receives no time extension for the entire concurrent period. This is the harshest interpretation and is disfavored in most jurisdictions but may be enforced under specific contract language.

```
Example:
  Owner delay: 10 days concurrent with contractor delay: 3 days
  All-or-nothing: Contractor receives 0 days extension (contractor contributed)
  NOTE: This method is considered unfair by most construction law authorities
  and is not recommended for contract administration.
```

### Documentation Requirements for Concurrent Delay

To prove or defend against concurrent delay, maintain:

1. **Independent Causation Evidence**: For each delay, document the independent cause (separate triggering events, separate responsible parties, separate impacted activities).

2. **Timeline Overlap Analysis**: Create a Gantt chart or timeline showing the exact date ranges of each delay, with overlap periods clearly identified.

3. **But-For Analysis**: For each delay, perform a but-for analysis: "But for this delay, would the project have been extended?" If yes for both delays independently, they are truly concurrent.

4. **Critical Path Analysis for Each Delay**: Run separate schedule analyses inserting each delay independently (one at a time) to determine independent impact.

5. **Pacing Analysis**: Document whether any party slowed its work in response to another delay. If so, the pacing delay is NOT concurrent.

### Concurrent Delay Tracking Table

```
Delay ID    Type              Dates           Days   Concurrent With   Overlap Period    Independent?   Allocation
DELAY-001   Owner Decision    02/20-02/27     7      DELAY-003         02/25-02/27 (3d)  YES            Dominant cause
DELAY-003   Sub Performance   02/25-03/04     7      DELAY-001         02/25-02/27 (3d)  NO (pacing)    Consequential
DELAY-004   Weather           03/10-03/14     5      DELAY-005         03/12-03/14 (3d)  YES            Apportionment
DELAY-005   Material Delay    03/12-03/20     8      DELAY-004         03/12-03/14 (3d)  YES            Apportionment
```

---



## Delay Notice Letter Templates

Timely written notice is a contractual prerequisite for delay claims. Failure to provide proper notice within the contract-specified period can waive the contractor's right to a time extension or cost recovery, regardless of how well-documented the delay is.

### Delay Notice Requirements per AIA A201 Clause 15.1

Under AIA A201 (General Conditions of the Contract for Construction):
- Contractor must provide **written notice** to the Architect and Owner within **21 days** of the event giving rise to the claim (or within the time specified in the contract)
- Notice must identify the **nature of the claim**, the **contract provision** supporting the claim, and the **relief requested**
- Failure to provide timely notice may constitute a **waiver** of the claim
- Notice must be delivered by a method that provides **proof of delivery** (certified mail, email with read receipt, or hand delivery with signed acknowledgment)

### Sample Delay Notice: Time Extension Request

```
[COMPANY LETTERHEAD]

[DATE]

VIA CERTIFIED MAIL / EMAIL WITH READ RECEIPT

TO:     [Owner Name]
        [Owner Address]
CC:     [Architect Name]
        [Architect Address]

RE:     NOTICE OF DELAY AND REQUEST FOR TIME EXTENSION
        Project: [PROJECT NAME]
        Contract No.: [CONTRACT NUMBER]
        Delay Event: [BRIEF DESCRIPTION]

Dear [Owner/Architect Name]:

Pursuant to [Contract Section, e.g., AIA A201 §15.1.3], this letter constitutes
formal written notice of a delay event affecting the above-referenced project.

DELAY EVENT IDENTIFICATION:

  Event:          [Description of the delay-causing event]
  Date of Event:  [Date the event occurred or was discovered]
  Delay Type:     [Weather / Owner-Directed / Design Issue / etc.]
  Activities Affected: [List of schedule activities impacted]
  Estimated Duration:  [X] calendar days (subject to further analysis)

CONTRACT BASIS:

  This delay is excusable under [Contract Section] because [brief statement
  of why the delay qualifies for time extension under the contract].

  [If compensable]: This delay is also compensable under [Contract Section]
  because [brief statement of why cost recovery is warranted].

IMPACT ON PROJECT SCHEDULE:

  Current Substantial Completion Date: [Date]
  Estimated Revised Completion Date:  [Date]
  Extension Requested:                [X] calendar days (preliminary;
                                       final calculation pending)

DOCUMENTATION:

  Supporting documentation including daily reports, [RFIs/change orders/
  weather data/photographs] is being compiled and will be submitted with
  the formal time extension request.

MITIGATION:

  Contractor is taking the following steps to mitigate delay impact:
  [List mitigation measures: re-sequencing, overtime, additional crews, etc.]

REQUEST:

  Contractor respectfully requests [Owner/Architect] acknowledge receipt
  of this notice and schedule a meeting to discuss the delay impact and
  potential resolution.

This notice is submitted to preserve Contractor's rights under the Contract
and does not waive any rights or remedies available to Contractor.

Respectfully submitted,

_____________________________
[Name], [Title]
[Company Name]
[Phone] | [Email]

cc: [Distribution list]
```

### Change Notice: Schedule Impact of Changed Work

```
RE:     NOTICE OF CHANGE IN WORK AND SCHEDULE IMPACT
        Project: [PROJECT NAME]
        Change Directive/Proposal: [CO/CCD NUMBER]

This letter provides notice that the change in work identified as [CO/CCD
Number], dated [Date], will impact the project schedule as follows:

  Change Description: [Brief description of the changed work]
  Additional Duration: [X] calendar days required to perform changed work
  Activities Affected: [List of activities requiring modification]
  Critical Path Impact: [Yes/No — with explanation]
  Estimated Extension: [X] calendar days (preliminary)

Contractor will submit a detailed time impact analysis within [X] days.
```

### Differing Site Conditions Notice

```
RE:     NOTICE OF DIFFERING SITE CONDITIONS
        Project: [PROJECT NAME]
        Location: [Specific location on site]
        Contract Section: [DSC clause reference]

This letter provides notice of differing site conditions encountered at the
above-referenced project:

  Condition Encountered: [Description of actual conditions found]
  Contract Indication:   [What the contract documents showed for this area]
  Difference:            [How actual conditions differ from contract documents]
  Date Discovered:       [Date]
  Impact on Work:        [Description of how conditions affect planned work]
  Estimated Duration:    [X] calendar days to address conditions
  Estimated Cost Impact: [Preliminary cost estimate, if available]

Contractor requests that [Owner/Architect] inspect the conditions at the
earliest opportunity. Contractor will preserve the site conditions for
inspection and will not proceed with work in the affected area until
directed by [Owner/Architect].
```

### Notice Tracking Table

```
Notice ID   Date Sent   Method           Recipient        Event              Response Deadline   Response Received   Status
NTC-001     02/18/26    Certified Mail   Owner (Smith)    DELAY-001 Weather  03/11/26           03/05/26            Acknowledged
NTC-002     03/01/26    Email w/receipt  Architect (Lee)  DELAY-002 Design   03/22/26           Pending             Open
NTC-003     03/15/26    Hand Delivery    Owner (Smith)    DSC - Rock Found   04/05/26           03/18/26            Meeting Set
NTC-004     03/20/26    Certified Mail   Owner (Smith)    CO-003 Schedule    04/10/26           Pending             Open
```

**Cross-Reference**: See the contract-administration skill for comprehensive contractual notice provisions, including state-specific notice requirements, notice preservation strategies, and notice response tracking.

---



## Cross-Reference to Claims Documentation

### When a Delay Event Becomes a Claim

Not every delay event becomes a claim. A delay event escalates to a claim when:

1. **Notice Period Expires Without Resolution**: The contractor provides timely delay notice, but the owner/architect does not grant the requested time extension or cost recovery within the contract-specified response period.

2. **Dispute Over Excusability or Compensability**: The owner disputes whether the delay is excusable (e.g., argues the contractor caused the delay) or compensable (e.g., acknowledges time but denies cost recovery).

3. **Cumulative Impact Exceeds Threshold**: Multiple small delays accumulate to a significant schedule and cost impact that the owner has not addressed through individual time extension approvals.

4. **Contract Termination or Default Threat**: The owner threatens liquidated damages or default termination based on schedule overrun, and the contractor must demonstrate that the overrun was caused by excusable delays.

### Documentation Escalation: From Delay Log to Claims Package

When a delay event escalates to a claim, the delay tracker data feeds directly into the claims package:

```
DELAY LOG DATA                          CLAIMS PACKAGE SECTION
─────────────────────────────────────────────────────────────────
Delay ID, Type, Dates, Duration    →    Claim Narrative (Section 1)
Critical Path Analysis             →    Schedule Analysis (Section 2)
Float Consumption Data             →    TIA Worksheets (Section 3)
Concurrent Delay Analysis          →    Concurrent Delay Defense (Section 4)
Linked Daily Reports               →    Contemporaneous Records (Exhibit A)
Linked RFIs                        →    Design Issue Documentation (Exhibit B)
Linked Change Orders               →    Scope Change Documentation (Exhibit C)
Weather Data / NOAA Comparison     →    Weather Delay Justification (Exhibit D)
Notice Letters Sent                →    Notice Compliance (Exhibit E)
```

### Linking Delay Events to Cost Impacts for Claims Quantification

Each delay event in the delay log should include cost impact fields that feed into claims quantification:

```json
{
  "id": "DELAY-002",
  "type": "design_spec_issue",
  "calendar_days": 8,
  "extension_days_earned": 6,
  "cost_impact": {
    "extended_general_conditions": {
      "daily_rate": 2500,
      "days": 6,
      "subtotal": 15000,
      "breakdown": {
        "superintendent_salary": 1200,
        "pm_allocation": 500,
        "site_office_rental": 150,
        "temporary_utilities": 100,
        "insurance_daily": 350,
        "bond_premium_daily": 200
      }
    },
    "subcontractor_impacts": {
      "davis_plomin_standby": 8000,
      "davis_plomin_overtime_recovery": 3200
    },
    "equipment_impacts": {
      "crane_standby_6_days": 4800
    },
    "material_escalation": 0,
    "total_compensable_cost": 31000,
    "markup_overhead_profit": 3100,
    "total_claim_amount": 34100
  },
  "claim_status": "pending",
  "claim_reference": "CLAIM-002",
  "notes": "Cost impact documented with payroll records, equipment rental invoices, and sub standby invoices. All costs are directly attributable to DELAY-002."
}
```

**Key Principle**: The delay tracker is the single source of truth for delay events. When a delay escalates to a claim, the delay tracker data must be complete, accurate, and contemporaneous. Claims built on incomplete or retroactive delay records are significantly weaker in dispute resolution, mediation, and litigation.

---



## Integration with Daily Reports

Daily reports are the foundation of delay documentation. The `/delay log` command should:

1. **Auto-link daily reports** to delay events:
   - When delay is logged, query `daily-report-data.json` for dates matching delay date range
   - Automatically populate `linked_daily_reports` array with matching dates
   - Notify user of linked reports

2. **Auto-suggest delay logging** in daily report entry:
   - When daily report captures adverse weather, owner directive, or design issue, suggest delay logging
   - Template: "Conditions suggest potential delay event. Would you like to create a /delay log entry for [type]?"

3. **Reference delays in daily entries**:
   - Daily report entries can reference existing DELAY-NNN events
   - "Work suspended per DELAY-002 (MEP coordination delay)"

Example auto-link scenario:
```
User logs delay:
  /delay log
  Type: Design Issue
  Dates: March 1-8, 2026
  Description: RFI-007 coordination delay

System auto-links:
  Queries daily-report-data.json for dates 3/1, 3/2, ..., 3/8
  Finds daily reports matching dates
  Populates linked_daily_reports: ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", "2026-03-06", "2026-03-07", "2026-03-08"]

User confirmation:
  "Linked 8 daily reports (3/1-3/8) that document this delay event. Review report entries to verify they capture the RFI coordination and work suspension."
```

---



## Storage & Configuration

### Storage Location
- **File**: `{{folder_mapping.config}}/delay-log.json`
- **Section**: `delays` array
- **Project Config Reference**: `{{folder_mapping.config}}/project-config.json` (for project_basics, folder_mapping, version_history)
- **Backup**: Each save creates timestamped backup in `{{folder_mapping.config}}/backups/`

### Version History
All delay additions, status updates logged in `project-config.json` `version_history` array with:
- Timestamp (ISO 8601)
- Action type (delay-log, delay-status, delay-report-generated)
- Delay ID and type
- User/actor (if tracked)

### Delay Log JSON Structure

```json
{
  "delays": [
    {
      "id": "DELAY-001",
      "type": "weather",
      "description": "Concrete placement delayed due to ambient temperature below ACI 306 minimum (40°F)",
      "date_start": "2026-02-15",
      "date_end": "2026-02-17",
      "calendar_days": 3,
      "activities_impacted": ["Foundation_Footings_C1_C6"],
      "responsible_party": "force_majeure",
      "excusable": true,
      "compensable": false,
      "critical_path_impact": "extended_completion",
      "float_consumed_days": 0,
      "extension_days_earned": 3,
      "concurrent_delays": [],
      "linked_daily_reports": ["2026-02-15", "2026-02-16", "2026-02-17"],
      "linked_rfis": [],
      "linked_change_orders": [],
      "weather_data": {
        "actual_conditions": "Freezing rain, snow; low 12°F-18°F",
        "contract_threshold_exceeded": true,
        "threshold_type": "temperature_min",
        "contract_requirement": "40°F (ACI 306)",
        "noaa_baseline_comparison": "14-20 degrees below normal"
      },
      "date_logged": "2026-02-18T10:30:00Z",
      "notes": "Critical path impact verified; no float available. 3-day extension fully earned."
    }
  ]
}
```



## Output Routing

All generated documents route to project folder structure:
- **Delay Records**: Stored in `delay-log.json` `delays` array
- **Delay Reports**: `{{folder_mapping.reports}}/Delay_Impact_Report_[YYYYMMDD].docx`
- **Version History**: Logged in `project-config.json` `version_history` array
- **Backup Copies**: `{{folder_mapping.config}}/backups/delay-log_[TIMESTAMP].json`


