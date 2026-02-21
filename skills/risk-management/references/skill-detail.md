# risk-management — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the risk-management skill.



## Risk Register Data Model

The risk register is stored as a JSON file (`risk-register.json`) within the project configuration directory. Each risk entry captures identification, assessment, mitigation, and tracking information.

### Full JSON Schema

```json
{
  "risk_register": {
    "project_id": "PROJECT-001",
    "last_updated": "2025-04-01T14:30:00Z",
    "next_review_date": "2025-05-01",
    "contingency_budget": {
      "original_allocation": 250000,
      "current_remaining": 185000,
      "drawdowns": [
        {
          "date": "2025-03-20",
          "amount": 65000,
          "risk_id": "R-003",
          "description": "Additional dewatering required due to high water table",
          "approved_by": "Project Manager"
        }
      ]
    },
    "risks": [
      {
        "id": "R-001",
        "date_identified": "2025-03-15",
        "identified_by": "Superintendent",
        "identification_method": "site_walkthrough",
        "category": "supply_chain",
        "subcategory": "extended_lead_times",
        "description": "Structural steel delivery delayed 4-6 weeks beyond scheduled need date",
        "root_cause": "Fabrication shop drawing approval cycle exceeding planned duration; mill capacity constraints",
        "probability": 4,
        "impact": 4,
        "score": 16,
        "priority": "critical",
        "owner": "Project Manager",
        "mitigation_strategy": "reduction",
        "mitigation_actions": [
          "Expedite fabrication shop drawing review (reduce approval cycle to 5 business days)",
          "Identify alternate steel supplier as backup (3 suppliers contacted 3/16)",
          "Adjust schedule sequence to pull interior framing ahead of steel erection"
        ],
        "contingency_plan": "Re-sequence interior framing to occur during steel delay; add second steel erection crew when material arrives to compress erection duration by 40%",
        "trigger_conditions": [
          "Fabrication shop drawing approval >2 weeks late",
          "Mill cert delivery delayed beyond promised date",
          "Fabricator reports capacity issues or schedule slip"
        ],
        "cost_exposure": 150000,
        "schedule_exposure_days": 30,
        "status": "active",
        "status_history": [
          {
            "date": "2025-03-15",
            "status": "identified",
            "notes": "Initial identification during procurement review"
          },
          {
            "date": "2025-03-18",
            "status": "active",
            "notes": "Mitigation plan developed; owner notified"
          }
        ],
        "related_activities": ["Steel erection", "Metal deck", "Concrete on deck"],
        "related_risks": ["R-005"],
        "linked_rfis": [],
        "linked_change_orders": [],
        "last_reviewed": "2025-04-01",
        "review_notes": "Fabricator confirmed 2-week delay likely. Alternate supplier quote received. Mitigation plan activated.",
        "probability_trend": "increasing",
        "resolution_date": null,
        "resolution_notes": null
      }
    ],
    "closed_risks": [],
    "version_history": []
  }
}
```

### Data Model Field Definitions

**Risk Identification Fields**:
- `id`: Unique identifier, format `R-NNN` (auto-incremented)
- `date_identified`: ISO date when risk was first identified
- `identified_by`: Role or name of person who identified the risk
- `identification_method`: How the risk was found (brainstorming, checklist, site_walkthrough, historical_review, swot, field_observation, sub_report, rfi_trend)
- `category`: Primary risk category (site_conditions, weather, labor, supply_chain, regulatory, design, subcontractor, financial, force_majeure, safety)
- `subcategory`: Specific risk type within category
- `description`: Clear, specific description of the risk event
- `root_cause`: Underlying cause or driver of the risk

**Risk Assessment Fields**:
- `probability`: 1-5 rating per probability scale
- `impact`: 1-5 rating per impact scale
- `score`: Calculated as probability x impact
- `priority`: Derived from score (low/medium/high/critical)
- `cost_exposure`: Estimated cost impact if risk materializes (dollars)
- `schedule_exposure_days`: Estimated schedule impact if risk materializes (calendar days)
- `probability_trend`: Direction of probability change (increasing, stable, decreasing)

**Risk Response Fields**:
- `owner`: Person responsible for monitoring and managing the risk
- `mitigation_strategy`: Primary strategy type (avoidance, transfer, reduction, acceptance)
- `mitigation_actions`: Specific actions being taken to address the risk
- `contingency_plan`: What to do if the risk materializes despite mitigation
- `trigger_conditions`: Observable conditions that indicate the risk is materializing

**Tracking Fields**:
- `status`: Current status (identified, active, mitigating, monitoring, materialized, closed)
- `status_history`: Chronological record of status changes with dates and notes
- `related_activities`: Schedule activities affected if risk materializes
- `related_risks`: Other risks that are related or interdependent
- `linked_rfis`: RFI IDs related to this risk
- `linked_change_orders`: Change order IDs related to this risk
- `last_reviewed`: Date of most recent review
- `review_notes`: Notes from most recent review
- `resolution_date`: Date risk was closed/resolved (null if active)
- `resolution_notes`: How the risk was resolved or why it was closed

---



## Mitigation Strategies

For each identified risk, select the appropriate mitigation strategy based on the risk score, category, and available options. Construction projects typically use a combination of all four strategies.

### 1. Avoidance

**Definition**: Change the project plan, scope, method, or sequence to eliminate the risk entirely.

**When to Use**:
- Risk score is Critical (16-25) and avoidance is feasible
- Cost of avoidance is less than expected cost of risk materialization
- Risk is on or near the critical path with no float buffer

**Construction Examples**:
- **Risk**: Winter concrete placement with freeze risk
  - **Avoidance**: Reschedule concrete work to spring; accelerate preceding activities to enable earlier start
- **Risk**: Crane operations near overhead power lines
  - **Avoidance**: Relocate crane to opposite side of building; request utility company de-energize lines during critical lifts
- **Risk**: Excavation in contaminated soil
  - **Avoidance**: Redesign foundation to minimize excavation depth; use helical piles instead of spread footings
- **Risk**: Sole-source material with 26-week lead time
  - **Avoidance**: Work with architect to approve an equivalent alternate product with shorter lead time

**Limitations**: Avoidance may increase cost, change scope, or create new risks. Not always feasible for contractually required scope.

### 2. Transfer

**Definition**: Shift the risk impact to a third party through insurance, bonds, contractual provisions, or subcontract requirements.

**When to Use**:
- Risk is well-defined and transferable
- Third party is better positioned to manage the risk
- Cost of transfer (premium, markup) is acceptable relative to risk exposure

**Construction Examples**:
- **Risk**: Subcontractor default
  - **Transfer**: Require performance and payment bonds from all subs >$100K; verify bonding capacity pre-award
- **Risk**: Property damage to adjacent structures
  - **Transfer**: Builder's risk insurance; require sub liability insurance; indemnification clauses in subcontracts
- **Risk**: Material price escalation
  - **Transfer**: Fixed-price subcontracts with escalation locked; owner-funded material escalation clause in prime contract
- **Risk**: Design errors causing rework
  - **Transfer**: Architect professional liability insurance; contractual allocation of design responsibility to design team
- **Risk**: Site security and theft
  - **Transfer**: Security service contract; builder's risk coverage for theft; sub responsibility for securing own materials

**Limitations**: Transfer does not eliminate risk -- it shifts financial exposure. The transferred party may dispute responsibility. Insurance has deductibles and exclusions.

### 3. Reduction

**Definition**: Take proactive actions to reduce either the probability of occurrence or the severity of impact (or both).

**When to Use**:
- Most common strategy for Medium and High risks (5-15)
- Risk cannot be avoided or transferred cost-effectively
- Active management can meaningfully reduce probability or impact

**Construction Examples**:
- **Risk**: Steel delivery delay (P=4, I=4, Score=16)
  - **Reduction**: Early procurement (reduce P to 2); identify backup supplier (reduce I to 3); New Score = 6
- **Risk**: Foundation design inadequacy due to soil conditions
  - **Reduction**: Additional geotechnical borings (reduce P); design foundations with contingency capacity (reduce I)
- **Risk**: MEP coordination conflicts
  - **Reduction**: BIM clash detection pre-construction (reduce P); mock-up at congested areas (reduce I); coordination meetings weekly
- **Risk**: Roofing quality issues in cold weather
  - **Reduction**: Manufacturer cold-weather installation certification for crew (reduce P); additional QC inspections (reduce I); heated material storage
- **Risk**: Subcontractor productivity shortfall
  - **Reduction**: Weekly production tracking with early intervention (reduce P); contractual acceleration provisions (reduce I)

**Limitations**: Reduction requires investment (time, money, effort) with no guarantee of eliminating the risk. Must balance cost of reduction against expected value of risk.

### 4. Acceptance

**Definition**: Acknowledge the risk and prepare to manage it if it materializes, without taking proactive measures to avoid, transfer, or reduce it.

**When to Use**:
- Risk score is Low (1-4) and active mitigation is not cost-effective
- Risk is residual after other mitigation strategies have been applied
- Risk is inherent to construction and cannot be meaningfully reduced further
- Cost of mitigation exceeds expected cost of risk materialization

**Construction Examples**:
- **Risk**: Minor weather delays (1-2 days per month)
  - **Acceptance**: Budget weather float days in schedule; include weather contingency in budget
- **Risk**: Minor material price increases (<2%)
  - **Acceptance**: Include cost contingency in budget; monitor and absorb within project margin
- **Risk**: Normal inspection rework
  - **Acceptance**: Budget for typical rework rates; schedule buffer before inspections
- **Risk**: Minor sub coordination delays
  - **Acceptance**: Schedule float in non-critical activities; manage through weekly coordination meetings

**Acceptance Types**:
- **Active Acceptance**: Allocate contingency (time and/or money) to address the risk if it materializes
- **Passive Acceptance**: Acknowledge the risk but take no proactive action; deal with it if it occurs

### Strategy Selection Decision Framework

Use this decision tree to select the appropriate strategy:

```
1. Can the risk be eliminated entirely?
   YES → AVOIDANCE (if cost-effective)
   NO → Continue to 2

2. Can the risk be shifted to a third party?
   YES → TRANSFER (insurance, bonds, subcontract)
   NO → Continue to 3

3. Can probability or impact be meaningfully reduced?
   YES → REDUCTION (specific actions to lower P or I)
   NO → Continue to 4

4. Is the residual risk acceptable?
   YES → ACCEPTANCE (with contingency allocation)
   NO → Return to 1 and reconsider constraints; escalate to PM/Owner
```

**Strategy by Risk Score**:

| Score | Primary Strategy | Secondary Strategy |
|-------|-----------------|-------------------|
| 16-25 (Critical) | Avoidance or Transfer | Reduction + active contingency |
| 10-15 (High) | Reduction | Transfer or partial avoidance |
| 5-9 (Medium) | Reduction or Acceptance | Monitor closely; contingency |
| 1-4 (Low) | Acceptance | Passive monitoring |

---



## Contingency Management

Contingency is the financial and schedule buffer allocated to address risks that materialize. Effective contingency management ensures adequate reserves exist throughout the project without over-allocating capital.

### Contingency Allocation

**Initial Allocation Method**: Percentage-based by risk category, adjusted for project-specific conditions.

| Risk Category | Typical Contingency % (of category cost) | Basis |
|--------------|------------------------------------------|-------|
| Site Conditions | 5-15% of sitework budget | Higher for limited geotech data, brownfield sites |
| Weather | 3-8% of weather-sensitive work | Higher for winter work, hurricane season |
| Labor | 3-5% of labor budget | Higher for remote locations, specialty trades |
| Supply Chain | 5-10% of material budget | Higher for long-lead items, volatile commodities |
| Regulatory | 2-5% of permit-related costs | Higher for new jurisdictions, complex projects |
| Design | 5-10% of construction cost | Higher for fast-track, incomplete documents |
| Subcontractor | 3-5% of subcontract value | Higher for low-bid awards, new relationships |
| Safety | 1-3% of total project cost | Industry standard; higher for high-risk activities |

**Total Project Contingency**: Typically 5-10% of total construction cost for a well-defined project; 10-20% for complex or poorly-defined projects.

**Allocation Formula**:
```
Category Contingency = Category Budget x Category % x Project Risk Factor

Where Project Risk Factor:
  1.0 = Standard project, experienced team, complete documents
  1.25 = Moderate complexity, some unknowns, mostly complete documents
  1.5 = High complexity, significant unknowns, incomplete documents
  2.0 = Very high risk, major unknowns, fast-track, unfamiliar building type
```

### Contingency Drawdown Tracking

Track every use of contingency with full documentation:

```json
{
  "drawdown_id": "CD-001",
  "date": "2025-03-20",
  "risk_id": "R-003",
  "amount": 65000,
  "description": "Additional dewatering system required due to higher-than-expected water table at foundation excavation",
  "category": "site_conditions",
  "approved_by": "Project Manager",
  "documentation": "CO-005 (dewatering scope addition); daily reports 3/15-3/18 documenting water infiltration",
  "remaining_contingency": 185000,
  "percent_of_original": 74
}
```

### Burn Rate Alerts

Monitor contingency consumption relative to project progress:

**Alert Thresholds**:

| Condition | Alert Level | Action Required |
|-----------|-------------|-----------------|
| Contingency used > project % complete + 10% | Warning (Yellow) | Review remaining risks; assess if contingency is adequate |
| Contingency used > 50% before 50% project complete | Elevated (Orange) | Detailed risk review; consider contingency replenishment request to owner |
| Contingency used > 75% before 75% project complete | Critical (Red) | Executive escalation; formal contingency status report; owner notification |
| Contingency exhausted | Emergency (Red) | Immediate project management review; value engineering; scope reduction discussion |

**Burn Rate Calculation**:
```
Expected Burn Rate = Contingency Used / Project % Complete
Healthy Range: 0.8 - 1.2 (within 20% of linear consumption)

Example:
  Project 40% complete
  Contingency: $250,000 original
  Used: $130,000 (52%)
  Burn Rate: 52% / 40% = 1.30 (over budget pace)
  Alert: WARNING — contingency consumption exceeds project progress by 30%
```

### Contingency Release Schedule

As the project progresses and risks are retired, portions of unused contingency can be released:

| Project Phase | Risks Retired | Typical Release % |
|--------------|---------------|-------------------|
| Foundation complete | Site conditions, subsurface, dewatering | 15-20% of remaining |
| Structural complete / dried-in | Weather (exterior), crane operations, steel delivery | 10-15% of remaining |
| MEP rough-in complete | Design coordination, major sub performance | 10-15% of remaining |
| Systems testing complete | Equipment, commissioning, performance | 10% of remaining |
| Substantial Completion | Most risks retired | Release to project closeout contingency |
| Final Completion | All risks retired | Final release; close contingency account |

**Release Approval**: Contingency release requires Project Manager approval and should be documented in the risk register version history.

### Relationship to EVM Management Reserve

In projects using Earned Value Management (EVM):
- **Contingency** = Known risks (identified in risk register); managed by project team
- **Management Reserve** = Unknown risks (unidentified "unknown unknowns"); managed by executive/owner
- Contingency draws from project budget; Management Reserve draws from program budget
- When contingency is exhausted, request Management Reserve allocation through formal change control

---



## Weather Contingency Planning

Weather is the most common and most predictable risk category in construction. Effective weather contingency planning requires understanding seasonal patterns, activity-specific thresholds, and regional climate data.

### Seasonal Risk Profiles (General)

**Spring (March - May)**:
- Rain/wet conditions affecting earthwork and foundations
- Freeze-thaw cycles affecting concrete and masonry
- Thunderstorms and wind events
- Flooding from snowmelt and spring rains
- Positive: Warming temperatures enable more outdoor activities

**Summer (June - August)**:
- Extreme heat affecting worker productivity and concrete curing
- Afternoon thunderstorms (Southeast, Midwest, Mountain regions)
- Hurricane season begins (June 1 - Atlantic/Gulf states)
- Drought conditions affecting dust control and landscaping
- Positive: Longest work days; most favorable for outdoor construction

**Fall (September - November)**:
- Hurricane season peak (August - October; Atlantic/Gulf states)
- Early frost affecting concrete and masonry (northern climates)
- Shorter days reducing available work hours
- Positive: Generally moderate temperatures; good productivity season

**Winter (December - February)**:
- Cold temperatures below ACI 306 minimums (40 degrees F)
- Snow and ice affecting all outdoor operations
- Frozen ground preventing earthwork and foundations
- Reduced daylight limiting work hours
- Positive: Less precipitation in some regions; lower humidity for interior finishes

### Activity-Specific Weather Windows

**Critical Weather Thresholds by Activity**:

| Activity | Temperature Min | Temperature Max | Wind Max | Precipitation | Other |
|----------|----------------|-----------------|----------|---------------|-------|
| Concrete placement | 40 degrees F (ACI 306) | 90 degrees F (ACI 305) | 25 mph for pumping | No active rain | Cure temp >50 degrees F for 7 days |
| Concrete finishing | 40 degrees F | 90 degrees F | 15 mph (surface evap) | No rain | Humidity <80% preferred |
| Asphalt paving | 50 degrees F ambient, 40 degrees F surface | No max (but productivity drops >100 degrees F) | No limit (but windblown dust issue) | No rain; dry surface | Compaction temp >175 degrees F |
| Roofing (membrane) | 40 degrees F (adhesive dependent) | No max | 25 mph (OSHA) | No rain or dew | Dry substrate |
| Roofing (shingles) | 40 degrees F (seal strip activation) | No max | 25 mph | No rain | Seal strip needs 70 degrees F+ days to activate |
| Earthwork/grading | Not frozen | No max | No limit | No active heavy rain | Soil moisture within spec (optimum +/- 2%) |
| Steel erection | No min (but ice on steel = hazard) | No max | 30 mph (OSHA 1926.752) | No active lightning | Visibility >1/4 mile |
| Crane operations | No min | No max | Per crane chart (typically 20-35 mph) | No lightning | Firm, level ground |
| Masonry | 40 degrees F (mortar) | 100 degrees F (rapid set) | 25 mph | No rain on fresh mortar | Cold weather masonry procedures below 40 degrees F |
| Painting (exterior) | 50 degrees F (most coatings) | 95 degrees F (product specific) | 15 mph | No rain; dry surface | Humidity per product spec (typically <85%) |
| Waterproofing | 40 degrees F (most products) | Product specific | 15 mph | No rain; dry substrate | Surface moisture <5% typically |
| Landscaping/seeding | 50 degrees F (soil temp for germination) | No max | No limit | Moderate moisture needed | Irrigation capability if dry season |

### Weather Float Budgeting

Budget weather delay days per month based on regional historical data:

**General Guidelines** (adjust for specific location using NOAA 30-year averages):

| Month | Northern US | Southern US | Coastal/Hurricane Zone |
|-------|-------------|-------------|----------------------|
| January | 8-12 days | 4-6 days | 4-6 days |
| February | 8-10 days | 4-6 days | 3-5 days |
| March | 6-8 days | 4-6 days | 3-5 days |
| April | 4-6 days | 4-6 days | 3-4 days |
| May | 3-5 days | 4-6 days | 3-5 days |
| June | 2-4 days | 4-6 days | 4-6 days |
| July | 2-3 days | 4-6 days | 4-6 days |
| August | 2-3 days | 4-6 days | 5-8 days |
| September | 3-4 days | 4-6 days | 5-8 days |
| October | 4-6 days | 3-5 days | 4-7 days |
| November | 6-8 days | 3-5 days | 3-5 days |
| December | 8-12 days | 4-6 days | 3-5 days |

**Usage**: Build these days into the baseline schedule as weather float. Track actual weather days against budget monthly. If actuals exceed budget, evaluate whether contract extension is warranted.

### Extreme Weather Preparation Checklist

When extreme weather is forecast (severe storms, hurricanes, extreme cold/heat, flooding):

**48-Hour Pre-Event**:
- [ ] Secure all loose materials, equipment, and temporary structures
- [ ] Lower crane booms to minimum safe position
- [ ] Disconnect temporary electrical and protect panels
- [ ] Protect open excavations (dewatering pumps, slope protection)
- [ ] Cover and protect weather-sensitive materials (drywall, insulation, finishes)
- [ ] Verify site drainage is clear and functioning
- [ ] Communicate shutdown plan to all subcontractors
- [ ] Document pre-event site conditions with photos/video
- [ ] Verify insurance coverage and emergency contacts
- [ ] Notify owner of anticipated delay and protective measures

**24-Hour Pre-Event**:
- [ ] Final site walkdown to verify all protection measures
- [ ] Remove all personnel from site (if warranted by severity)
- [ ] Activate emergency communication protocol
- [ ] Ensure backup power for critical systems (sump pumps, security)
- [ ] Verify emergency contact list is current and distributed

**Post-Event**:
- [ ] Safety inspection before allowing any personnel on site
- [ ] Document all damage with photos, video, and written description
- [ ] Assess structural integrity of temporary structures and formwork
- [ ] Check all electrical systems before re-energizing
- [ ] File insurance claims if damage warrants
- [ ] Log weather delay event in delay tracker
- [ ] Update risk register with actual event data
- [ ] Develop recovery plan and revised schedule

---



## Force Majeure Management

Force majeure events are extraordinary circumstances beyond any party's control that prevent performance of contractual obligations. Proper management protects both contractor and owner interests.

### Contract Definition Awareness

**Typical Force Majeure Clause Elements**:
- Specific enumerated events (natural disasters, war, pandemic, government orders)
- "Catch-all" language ("...and other events beyond the reasonable control of the party")
- Exclusions (events that could have been foreseen, financial hardship, labor shortages that are not industry-wide)
- Notice requirements (written notice within specified timeframe)
- Duty to mitigate (affected party must take reasonable steps to minimize impact)
- Duration limitations (right to terminate if force majeure exceeds defined period, often 90-180 days)

**Pre-Construction Action**: Review the specific force majeure clause in the prime contract and all major subcontracts. Note:
- What events are specifically listed?
- What is the notice period?
- What documentation is required?
- Is there a duration cap?
- What are the cost recovery provisions?

### Notice Requirements

**Critical**: Failure to provide timely notice can waive force majeure rights entirely.

**Typical Notice Timeline**:
- **Immediate verbal notice**: Within 24 hours of event occurrence (phone call to owner/PM)
- **Written notice**: Within 48-72 hours (formal letter/email) -- check contract for specific requirement
- **Detailed impact assessment**: Within 7-14 days of event (schedule and cost impact analysis)
- **Ongoing updates**: Weekly status reports during force majeure period

**Notice Content Requirements**:
```
TO:       [Owner/Owner's Representative]
FROM:     [Contractor]
DATE:     [Date of Notice]
RE:       Force Majeure Notice — [Project Name], [Contract No.]

This letter constitutes formal notice of a Force Majeure event per
[Contract Article reference].

Event Description: [Specific description of the event]
Date of Occurrence: [Date event began affecting project]
Activities Affected: [List of affected schedule activities]
Estimated Duration: [Best estimate of delay duration]
Mitigation Measures: [Steps being taken to minimize impact]

We will provide a detailed impact assessment within [X] days per
contract requirements. Please confirm receipt of this notice.
```

### Documentation Requirements

Maintain comprehensive documentation throughout the force majeure period:

**Government and Official Records**:
- Government orders (shutdown orders, emergency declarations, curfews)
- Public health directives (quarantine orders, capacity restrictions)
- Weather service advisories and warnings (NOAA, NWS)
- Insurance claim documentation
- News reports documenting the event and regional impact

**Site Documentation**:
- Daily site condition photos/video documenting the event's impact
- Daily reports noting site status (closed, limited operations, full operations)
- Crew availability and attendance records
- Equipment status and any damage assessments
- Material condition assessments (damage, exposure, contamination)

**Communication Records**:
- All correspondence with owner regarding the event
- Subcontractor communications regarding their ability to perform
- Supplier communications regarding delivery impacts
- Insurance company communications
- Government agency communications

### Duty to Mitigate

The force majeure clause does not relieve the contractor of the duty to take reasonable steps to minimize the impact:

**Mitigation Actions**:
- Protect work in place from further damage
- Reassign resources to unaffected work areas if possible
- Seek alternative suppliers or subcontractors if original sources are unavailable
- Implement workarounds for affected activities
- Maintain site security during shutdown periods
- Preserve documentation and records

**Key Principle**: The contractor must demonstrate that the delay was not prolonged by inaction. "We couldn't work because of the hurricane" must be accompanied by "...and we took the following steps to resume work as soon as possible: [list of actions]."

### Cost Recovery Procedures

Force majeure cost recovery depends on specific contract language. Common recoverable costs include:

**Typically Recoverable**:
- Extended general conditions (staff, site office, utilities, insurance for extended period)
- Demobilization and re-mobilization costs
- Material protection and storage costs
- Damage repair costs (not covered by insurance)
- Acceleration costs to recover schedule (if directed by owner)

**Typically Not Recoverable**:
- Lost profit on work not performed
- Home office overhead (unless Eichleay formula applies)
- Consequential damages (unless contract specifically allows)

**Documentation for Cost Recovery**:
- Detailed cost breakdown with supporting invoices and receipts
- Payroll records for extended staff presence
- Equipment rental/ownership cost records
- Insurance deductible documentation
- Comparison of planned vs. actual costs attributable to force majeure event

---



## Monthly Risk Review Meeting

Regular risk reviews ensure the risk register stays current and risks are actively managed. Monthly reviews are the minimum recommended frequency; critical risks warrant more frequent attention.

### Meeting Cadence and Attendance

**Frequency**: Monthly (minimum); more frequent during high-risk phases

**Attendees**:
- Project Manager (required)
- Superintendent (required)
- Project Engineer (required)
- Key subcontractor foremen (for risks involving their scope)
- Owner's Representative (for top 5 risks, or as appropriate)
- Safety Manager (for safety-related risks)

**Duration**: 60-90 minutes

### Agenda Template

```
RISK REVIEW MEETING AGENDA
Project: [Project Name]
Date: [Meeting Date]
Attendees: [Names and roles]

1. REVIEW SUMMARY DASHBOARD (10 min)
   - Total active risks: [count]
   - Risk distribution: [X] Critical, [X] High, [X] Medium, [X] Low
   - Risks added since last review: [count]
   - Risks closed since last review: [count]
   - Risks that materialized: [count]
   - Contingency status: $[remaining] of $[original] ([X]% remaining)

2. CRITICAL RISK REVIEW (20 min)
   For each Critical risk (score 16-25):
   - Current status and mitigation effectiveness
   - Probability/impact re-assessment
   - Trigger condition monitoring
   - Action item status
   - Escalation needs

3. HIGH RISK REVIEW (15 min)
   For each High risk (score 10-15):
   - Status update
   - P/I re-assessment
   - Mitigation progress

4. NEW RISK IDENTIFICATION (15 min)
   - New risks identified since last meeting
   - Risks emerging from current project conditions
   - Risks identified by subcontractors or field personnel
   - Initial P/I rating for new risks

5. CONTINGENCY STATUS (10 min)
   - Drawdowns since last review
   - Burn rate assessment
   - Adequacy of remaining contingency
   - Release recommendations for retired risks

6. UPCOMING RISK WINDOWS (10 min)
   - Phase transitions in next 30 days
   - Weather forecast concerns
   - Critical procurements approaching
   - Regulatory milestones approaching

7. ACTION ITEMS AND ASSIGNMENTS (10 min)
   - Summarize all action items from meeting
   - Assign owners and deadlines
   - Confirm next review date
```

### Risk Review Format (Per Risk)

For each risk reviewed, walk through:

1. **Status Update**: Has anything changed since last review? Any trigger conditions observed?
2. **Probability Re-Assessment**: Has probability increased, decreased, or remained stable? Why?
3. **Impact Re-Assessment**: Has impact estimate changed based on new information?
4. **Score Recalculation**: Update score if P or I changed; update priority category
5. **Mitigation Effectiveness**: Are current mitigation actions working? Do they need adjustment?
6. **New Information**: Any new data, events, or conditions affecting this risk?
7. **Action Items**: What specific actions need to happen before next review?

### Reporting Format

#### Top 10 Risks Dashboard

```
TOP 10 PROJECT RISKS — [Project Name] — [Date]

| # | ID    | Category      | Description (abbreviated)           | P | I | Score | Priority | Trend | Owner     |
|---|-------|---------------|-------------------------------------|---|---|-------|----------|-------|-----------|
| 1 | R-001 | Supply Chain  | Structural steel delivery delay     | 4 | 4 | 16    | CRITICAL | UP    | PM        |
| 2 | R-007 | Design        | MEP coordination conflicts          | 4 | 3 | 12    | HIGH     | STABLE| PE        |
| 3 | R-003 | Site Cond.    | High water table at foundations     | 3 | 4 | 12    | HIGH     | DOWN  | Super     |
| 4 | R-012 | Weather       | Winter concrete placement risk      | 4 | 3 | 12    | HIGH     | UP    | Super     |
| 5 | R-005 | Subcontractor | HVAC sub capacity concerns          | 3 | 3 | 9     | MEDIUM   | STABLE| PM        |
| ...                                                                                                          |

Contingency: $185,000 remaining of $250,000 (74%) | Project 35% complete
Burn Rate: 1.06 (within healthy range)
```

#### Risk Heat Map

Display current risks plotted on the 5x5 matrix to visualize risk concentration:

```
RISK HEAT MAP — [Project Name] — [Date]

                          I M P A C T
                 1          2          3          4          5
              Negligible   Minor    Moderate    Major    Critical
         +----------+----------+----------+----------+----------+
    5    |          |          |          |  R-015   |          |
 Almost  |          |          |          |          |          |
 Certain |          |          |          |          |          |
         +----------+----------+----------+----------+----------+
    4    |          |          | R-007    |  R-001   |          |
 Likely  |          |          | R-012    |          |          |
         |          |          |          |          |          |
P        +----------+----------+----------+----------+----------+
R   3    |          |  R-009   | R-005    |  R-003   |          |
O Poss-  |          |  R-011   | R-008    |          |          |
B ible   |          |          | R-014    |          |          |
A        +----------+----------+----------+----------+----------+
B   2    |          |  R-010   | R-006    |  R-013   |          |
I Unlikely|         |          |          |          |          |
L        |          |          |          |          |          |
I        +----------+----------+----------+----------+----------+
T   1    |          |  R-016   |          |          |          |
Y Rare   |          |          |          |          |          |
         |          |          |          |          |          |
         +----------+----------+----------+----------+----------+

Risks in RED zone (16-25): 2    Risks in ORANGE zone (10-15): 4
Risks in YELLOW zone (5-9): 5   Risks in GREEN zone (1-4): 5
```

#### Trend Analysis

Track risk metrics over time to identify patterns:

```
RISK TREND — Last 6 Months

| Metric                    | Oct  | Nov  | Dec  | Jan  | Feb  | Mar  | Trend |
|---------------------------|------|------|------|------|------|------|-------|
| Total Active Risks        | 18   | 22   | 25   | 24   | 21   | 19   | DOWN  |
| Critical Risks            | 1    | 2    | 3    | 3    | 2    | 2    | STABLE|
| High Risks                | 3    | 4    | 5    | 4    | 4    | 3    | DOWN  |
| New Risks Added           | 5    | 6    | 4    | 3    | 2    | 1    | DOWN  |
| Risks Closed              | 2    | 2    | 1    | 4    | 5    | 3    | UP    |
| Risks Materialized        | 0    | 1    | 2    | 1    | 0    | 1    | STABLE|
| Contingency Remaining (%) | 100  | 92   | 85   | 78   | 74   | 70   | DOWN  |
| Avg Risk Score            | 7.2  | 8.1  | 8.5  | 7.8  | 7.0  | 6.5  | DOWN  |
```

---



## Integration with Other Skills

The risk-management skill connects with other ForemanOS skills to create a comprehensive project management ecosystem.

### delay-tracker

**Integration Point**: When risks materialize into actual delays.

- When a risk status changes to `materialized`, prompt user to create a delay log entry via `/delay log`
- Pre-populate delay log fields from risk register data (category, description, activities affected, cost/schedule exposure)
- Link risk ID to delay ID (`R-001` -> `DELAY-005`)
- When a delay is logged that matches an existing risk trigger condition, update the risk status to `materialized`
- Use delay data to validate risk impact estimates (actual vs. predicted impact)

### last-planner

**Integration Point**: Constraints and PPC as risk indicators.

- Last Planner System constraints are operational manifestations of risks
- When a constraint is identified that maps to an existing risk, link the constraint to the risk ID
- If PPC (Percent Plan Complete) falls below 60% for two consecutive weeks, trigger a risk review: low PPC indicates systemic issues that should be reflected in the risk register
- Variance reasons from weekly PPC tracking feed into risk category analysis (e.g., repeated "material not available" variances indicate supply chain risk escalation)

### cost-tracking

**Integration Point**: Contingency drawdown and budget risk alerts.

- Contingency drawdown transactions are recorded in both the risk register and cost tracking system
- When cost-to-complete forecast exceeds budget by >5%, trigger risk review for cost overrun risk
- Cost variance trends feed risk probability assessments (consistent negative variances increase financial risk probability)
- EVM metrics (CPI, SPI) serve as leading indicators for risk escalation

### safety-management

**Integration Point**: Safety risks feed the risk register.

- Safety hazards identified during JSAs, inspections, and incident investigations should be evaluated for inclusion in the project risk register
- OSHA recordable incidents trigger immediate risk review for the related activity
- Near-miss trends indicate areas where safety risk probability should be increased
- Safety leading indicators (toolbox talk frequency, inspection closure rates) affect safety risk probability assessments

### morning-brief

**Integration Point**: Top risk alerts in daily briefing.

- Morning brief surfaces the top 3-5 risks relevant to today's planned work
- If today's activities involve work related to a Critical or High risk, include specific risk alert and mitigation reminders
- Weather risk alerts based on forecast vs. activity thresholds
- Trigger condition alerts when monitored conditions approach risk thresholds

### change-order-tracker

**Integration Point**: Change events may trigger new risks.

- Scope changes (change orders) should be evaluated for new risks they introduce
- Change orders that affect schedule may increase existing schedule-related risk scores
- Cumulative change order volume exceeding budget contingency triggers financial risk escalation
- Disputed change orders increase contractual/legal risk probability

---



## Storage & Configuration

### Storage Location
- **File**: `{{folder_mapping.config}}/risk-register.json`
- **Section**: `risk_register` object containing `risks` array, `closed_risks` array, `contingency_budget` object
- **Project Config Reference**: `{{folder_mapping.config}}/project-config.json` (for project_basics, folder_mapping, version_history)
- **Backup**: Each save creates timestamped backup in `{{folder_mapping.config}}/backups/`

### Version History
All risk register changes logged in `project-config.json` `version_history` array with:
- Timestamp (ISO 8601)
- Action type (risk-add, risk-update, risk-close, risk-review, risk-report-generated, contingency-drawdown)
- Risk ID and category
- Summary of change

### Output Routing
- **Risk Records**: Stored in `risk-register.json` `risks` array
- **Risk Reports**: `{{folder_mapping.reports}}/Risk_Report_[YYYYMMDD].docx`
- **Risk Matrix**: `{{folder_mapping.reports}}/Risk_Matrix_[YYYYMMDD].docx`
- **Version History**: Logged in `project-config.json` `version_history` array
- **Backup Copies**: `{{folder_mapping.config}}/backups/risk-register_[TIMESTAMP].json`


