# claims-documentation — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the claims-documentation skill.



## Cost Impact Documentation

### Loss of Productivity

Loss of productivity claims assert that the contractor's work was less efficient than it should have been due to owner-caused disruptions. These claims require rigorous documentation because the burden of proof is on the contractor.

#### Measured Mile Analysis

The measured mile is the most defensible method for proving lost productivity. It compares the contractor's actual productivity during an unimpacted period (the "measured mile") against productivity during the impacted period.

**Requirements**:
1. **Identify unimpacted period**: A period on the same project where the same type of work was performed without the claimed disruption
2. **Identify impacted period**: The period when disruption was occurring
3. **Compare productivity**: Units of work per labor hour in each period
4. **Calculate loss**: Difference in productivity multiplied by total impacted work quantity

**Example**:
```
Measured Mile Analysis: Electrical Conduit Installation

Unimpacted Period (January 2026):
  Work completed: 2,400 LF of 3/4" EMT conduit
  Labor hours: 300 hours (4 electricians x 75 hrs each)
  Productivity: 8.0 LF per labor hour

Impacted Period (March 2026 -- concurrent trade stacking):
  Work completed: 1,800 LF of 3/4" EMT conduit (same spec, same conditions)
  Labor hours: 360 hours (4 electricians x 90 hrs each)
  Productivity: 5.0 LF per labor hour

Productivity Loss: 8.0 - 5.0 = 3.0 LF/hr (37.5% reduction)

Total Impacted Work Remaining: 6,000 LF
Additional Hours Required: 6,000 / 5.0 - 6,000 / 8.0 = 1,200 - 750 = 450 extra hours
Cost at $65/hr fully burdened: 450 x $65 = $29,250 productivity loss claim
```

**Key requirements for measured mile**:
- Same type of work in both periods (same specification, same general conditions)
- Same crew or comparable crew skill level
- Clear identification of the disruption that differentiates the periods
- Sufficient sample size in both periods (minimum 2 weeks of data recommended)

#### Industry Studies

When a measured mile comparison is not possible (no unimpacted period exists on the project), industry studies provide recognized productivity loss factors:

**Mechanical Contractors Association (MCA) Study**: Provides productivity loss factors for various disruption types:
- Trade stacking (multiple trades in same area): 10-25% loss
- Overtime (sustained, >50 hrs/week): 15-25% loss after 4 weeks
- Morale/attitude (from disruption): 5-15% loss
- Reassignment of manpower: 5-10% loss
- Concurrent operations: 10-20% loss

**Leonard Study (1988)**: Factors for productivity impact of changes on unchanged work:
- Projects with 10-15% change: 5-8% productivity loss on remaining unchanged work
- Projects with 15-25% change: 8-15% loss
- Projects with 25%+ change: 15-25% loss

**Ibbs Study (2005)**: Updated productivity impact research confirming similar ranges with additional data on timing of changes (late changes cause disproportionately higher productivity loss).

**Important caveat**: Industry studies are a fallback, not a first choice. Arbitrators and courts prefer project-specific data (measured mile) over industry averages. Use industry studies only when project data is insufficient.

#### Force Account Comparison

When productivity cannot be measured by the mile, force account (T&M) records provide cost documentation:
- Detailed daily time sheets by worker name and hours
- Material quantities installed per day
- Equipment hours by machine
- Comparison to original estimate or bid labor hours for the same work

### Remobilization Costs

When work is suspended and later resumed, remobilization costs include:

- **Equipment move-in/move-out**: Crane mobilization ($5,000-$25,000 per move), heavy equipment transport
- **Crew reassignment**: Travel costs, per diem, lost time between assignments
- **Learning curve**: First 2-3 days after remobilization show reduced productivity (typically 20-40% loss)
- **Material re-staging**: Moving stored materials back to work areas
- **Re-inspection**: Work completed before suspension may require re-inspection before resuming

### Acceleration Costs

Document acceleration costs separately from base contract work:

- **Overtime premium**: Track hours at straight time vs. 1.5x vs. 2x separately
- **Additional crews**: Document mobilization date, crew size, daily cost
- **Out-of-sequence work**: Track productivity loss when work must be performed out of optimal sequence
- **Expedited materials**: Document original delivery date, expedited delivery date, premium paid
- **Additional supervision**: Cost of additional foremen, superintendents, or PMs for extended hours or multiple shifts

### Extended General Conditions

For each day of compensable delay, the contractor incurs general conditions costs that would not have been incurred but for the delay:

**Daily General Conditions Rate Calculation**:
```
Monthly General Conditions Budget: $75,000
  Superintendent salary + benefits:    $18,000
  Project Manager (allocated):         $12,000
  Site office rental:                  $3,500
  Temporary utilities:                 $2,200
  Site phone/internet:                 $800
  Temporary toilets:                   $1,200
  Dumpster service:                    $2,400
  Project insurance (monthly):         $8,500
  Bond cost (monthly):                 $4,200
  Equipment rental (monthly):          $12,000
  Vehicle/fuel:                        $3,200
  Miscellaneous:                       $7,000

Daily Rate: $75,000 / 30 = $2,500/day

For 15 days of compensable delay:
Extended General Conditions Claim: 15 x $2,500 = $37,500
```

**Documentation requirements**: Actual invoices, payroll records, and receipts for each line item. The daily rate must be supportable with real costs, not estimates.

### Eichleay Formula for Home Office Overhead

The Eichleay formula is the standard method for calculating unabsorbed home office overhead during a period of government-caused delay (primarily used on federal contracts, but increasingly accepted in private work).

**The Formula**:
```
Step 1: Allocable Overhead
  (Contract Billings / Total Company Billings for Period) x Total Home Office OH for Period
  = Allocable Overhead

Step 2: Daily Rate
  Allocable Overhead / Days of Contract Performance
  = Daily Contract OH Rate

Step 3: Recoverable Amount
  Daily Contract OH Rate x Days of Compensable Delay
  = Recoverable Home Office Overhead
```

**Worked Example**:
```
Eichleay Calculation:

Company Data (Annual):
  Total company billings (all projects): $25,000,000
  Total home office overhead:            $2,500,000

This Project:
  Contract billings to date:             $4,200,000
  Contract performance period:           365 days
  Compensable delay period:              30 days

Step 1: Allocable OH
  ($4,200,000 / $25,000,000) x $2,500,000 = $420,000

Step 2: Daily Rate
  $420,000 / 365 days = $1,150.68/day

Step 3: Recoverable HOH
  $1,150.68 x 30 days = $34,520.55

Total Home Office Overhead Claim: $34,520.55
```

**Eichleay requirements**:
- Government (or owner) caused the delay
- Contractor was on standby and could not take on replacement work
- Contractor's home office continued to incur overhead during the delay
- Financial records must be auditable and verifiable

### Lost Profit

Lost profit (consequential damages) is rarely recoverable in construction contracts because most contracts contain mutual waiver of consequential damages clauses (AIA A201 Section 15.1.7).

**When recoverable**:
- Contract does not contain consequential damages waiver
- Breach is willful or in bad faith
- Lost profits are reasonably foreseeable and provable

**Documentation**: If pursuing lost profit, document: revenue lost from inability to take on other work during delay, contracts or bids declined due to resource commitment, historical profit margins on comparable work.

---



## Causation Evidence

### The Critical Chain: Event to Impact to Damages

Every construction claim must establish three linked elements. Missing any one element defeats the claim:

```
EVENT ──────────► IMPACT ──────────► DAMAGES
(What happened)   (What it caused)   (What it cost)

Example:
EVENT:   Owner directed suspension of MEP work pending design review (RFI-042)
IMPACT:  MEP rough-in delayed 8 calendar days; critical path extended 6 days
DAMAGES: Extended general conditions ($15,000) + sub standby ($8,000) + equipment ($3,200) = $26,200
```

### Traceability Requirements

Each damage item must trace back through the impact to the event. This is the "but-for" test: but for the event, the contractor would not have incurred this cost.

**Traceability matrix**:
```
| Damage Item | Amount | Impact | Event | Evidence |
|------------|--------|--------|-------|----------|
| Extended superintendent | $7,500 | 6-day CP extension | Owner RFI delay | Payroll records, daily reports |
| Sub standby (XYZ Mech) | $8,000 | MEP crew idle 8 days | Owner RFI delay | Sub invoices, daily reports |
| Crane rental extension | $3,200 | Equipment held on-site | Owner RFI delay | Rental invoices |
| Overtime premium | $4,800 | Acceleration to recover | Owner denied extension | Time sheets, denial letter |
```

### Common Causation Failures

**1. Gap in documentation**: The event is documented but the link to the impact is not. Example: Daily reports show the delay, but there is no schedule analysis showing critical path impact.

**2. Assumed rather than proven causation**: "The delay must have caused the cost increase" is not sufficient. Must show specific cost increases tied to specific delay days.

**3. Failure to account for concurrent causes**: If the contractor also caused delays during the same period, failing to address concurrent causation destroys credibility.

**4. Speculative damages**: Damages must be proven with reasonable certainty, not hypothetical calculations. "We think we lost about $50,000" will not survive scrutiny.

**5. Betterment**: If the claimed event resulted in an improvement to the work (better design, upgraded materials), the contractor cannot claim the full cost -- must net out the betterment value.

### Causation Documentation Checklist

For each claimed event:
- [ ] Written record of the event (directive, RFI, inspection report, daily report)
- [ ] Date and time of the event
- [ ] Who caused or directed the event
- [ ] What work was affected and how
- [ ] Duration of the impact (start date, end date)
- [ ] Schedule analysis showing critical path effect
- [ ] Cost records showing damages incurred during impact period
- [ ] "But-for" analysis: these costs would not have been incurred but for the event
- [ ] Mitigation efforts documented (what the contractor did to minimize impact)
- [ ] Concurrent cause analysis (were there other contributing factors?)

---



## Notice Requirements

### THE MOST IMPORTANT PROCEDURAL ELEMENT

**Failure to give timely notice can waive all claim rights regardless of merit.** This cannot be overstated. A contractor with a $2 million claim supported by perfect documentation will recover nothing if the contract required 21-day notice and the contractor gave notice on day 25.

### Standard Notice Periods

| Contract Form | Notice Provision | Deadline | Reference |
|--------------|-----------------|----------|-----------|
| AIA A201 (2017) | Claims must be initiated by written notice | Within 21 days of event | Section 15.1.3 |
| AIA A201 (2017) | Concealed/unknown conditions | Promptly upon discovery | Section 3.7.4 |
| ConsensusDocs 200 | Written notice of claim | Within 14 days of event | Section 8.4 |
| Federal (FAR) | Notice of differing site conditions | Promptly, before conditions disturbed | FAR 52.236-2 |
| Federal (FAR) | REA/Claim submission | Within 6 years | Contract Disputes Act |
| EJCDC C-700 | Written notice of claim | Within 30 days of event | Section 12.01 |

**Critical**: Always check the specific contract for notice provisions. Many owners modify standard forms to shorten notice periods (7 days, 10 days, or even "immediate" notice).

### Notice Letter Content

Every formal notice must include:

1. **Date of notice letter**
2. **Parties**: To (owner/architect) and From (contractor)
3. **Contract reference**: Project name, contract number, date of agreement
4. **Contract provision**: Specific section requiring notice (e.g., "Per AIA A201 Section 15.1.3")
5. **Description of event**: Factual description of what occurred or was discovered
6. **Date of event**: When the event occurred or was first discovered
7. **Impact on work**: How the event is affecting or will affect the work
8. **Request for relief**: Specific request (time extension, cost adjustment, both)
9. **Reservation of rights**: Statement preserving all contractual and legal remedies
10. **Supporting documentation reference**: List of attached or forthcoming documentation

### Notice Delivery Requirements

- **Certified mail with return receipt requested**: Creates proof of delivery with date
- **Email**: Send to all contract-designated recipients AND project manager/architect
- **Hand delivery**: With signed acknowledgment of receipt
- **Best practice**: Send by ALL three methods simultaneously
- **Keep proof**: Certified mail receipt, email sent confirmation, signed acknowledgment

### Reservation of Rights Language

Every notice should include reservation of rights language:

```
Contractor reserves all rights under the Contract Documents, at law, and in equity,
including but not limited to the right to seek additional time and/or cost adjustments
as the full extent of the impact becomes known. This notice is provided to preserve
Contractor's rights and is not intended to be a complete or final statement of
Contractor's claim. Contractor will supplement this notice with additional information
as it becomes available.
```

### Notice Types and Templates

**Type 1: Delay Notice**
```
RE: Notice of Delay -- [Project Name], Contract No. [XXX]

This letter provides formal notice pursuant to [Contract Section] that Contractor
has encountered a delay to the Work caused by [description of event].

Event Date: [Date]
Description: [Factual description]
Activities Affected: [List activities]
Estimated Duration: [Days, if known] (to be updated as impact becomes clear)
Critical Path Impact: [Preliminary assessment]

Contractor requests a time extension of [X] calendar days (subject to refinement
as the full impact is determined). [Add cost recovery request if compensable delay.]
```

**Type 2: Change Order / Extra Work Notice**
```
RE: Notice of Change in Work -- [Project Name], Contract No. [XXX]

This letter provides formal notice pursuant to [Contract Section] that Contractor
has been directed to perform work that constitutes a change to the Contract.

Directive Date: [Date]
Directive Source: [Who gave the directive, verbal/written]
Description of Changed Work: [What was directed]
Contract Basis: [Why this is a change -- not in original scope, different conditions, etc.]
Estimated Cost Impact: [Preliminary, subject to detailed pricing]
Estimated Schedule Impact: [Preliminary]

Contractor will submit a formal Change Order Request within [X] days.
```

**Type 3: Differing Site Conditions Notice**
```
RE: Notice of Differing Site Conditions -- [Project Name], Contract No. [XXX]

Pursuant to [Contract Section / FAR 52.236-2], Contractor provides notice of
subsurface or physical conditions materially different from those indicated in
the Contract Documents.

Date of Discovery: [Date]
Location: [Specific location with grid/coordinates]
Condition Discovered: [Factual description of actual conditions]
Contract Indication: [What the contract documents showed/indicated]
Difference: [How actual differs from indicated]
Impact on Work: [How this affects current and planned work]

Contractor requests that Owner investigate the conditions before they are
further disturbed. Contractor reserves the right to request equitable adjustment
for time and cost.
```

**Type 4: Constructive Change Notice**
```
RE: Notice of Constructive Change -- [Project Name], Contract No. [XXX]

Contractor provides notice that actions by [Owner/Architect] constitute a
constructive change to the Contract, entitling Contractor to equitable adjustment.

Event: [Description of owner/architect action that changes the work without a formal CO]
Date: [When it occurred]
Why This Is a Change: [Contract basis -- how it differs from original scope/requirements]
Impact: [Cost and schedule impact, preliminary]

Contractor will perform the work under protest and reserves the right to seek
equitable adjustment for all additional costs and time.
```

**Type 5: Acceleration Notice**
```
RE: Notice of Constructive Acceleration -- [Project Name], Contract No. [XXX]

Contractor provides notice that Owner's denial of Contractor's time extension
request dated [date], combined with Owner's insistence on maintaining the
original completion date, constitutes constructive acceleration.

Time Extension Request: [Reference to original request]
Excusable Delay: [Description of the excusable delay]
Owner's Response: [Denial of extension, with date]
Acceleration Required: [What the contractor must do to meet original deadline]
Estimated Acceleration Cost: [Preliminary]

Contractor will proceed with acceleration measures under protest and will seek
recovery of all acceleration costs incurred.
```

### Notice Tracking

Maintain a notice log tracking:

```json
{
  "notice_id": "NOTICE-001",
  "type": "delay",
  "date_sent": "2026-03-02",
  "contract_provision": "AIA A201 Section 15.1.3",
  "event_date": "2026-03-01",
  "deadline_date": "2026-03-22",
  "days_remaining_at_notice": 20,
  "sent_via": ["certified_mail", "email"],
  "certified_mail_tracking": "9400111899223100XXXXX",
  "recipients": ["owner_pm@example.com", "architect@example.com"],
  "delivery_confirmed": true,
  "delivery_date": "2026-03-04",
  "linked_claim": "CLAIM-001",
  "linked_delay": "DELAY-005",
  "response_received": false,
  "response_date": null,
  "follow_up_required": true,
  "follow_up_date": "2026-03-16"
}
```

---



## Concurrent Delay

### Definition and Identification

Concurrent delays occur when two or more delay events overlap in time and both potentially affect project completion. Concurrent delay is one of the most contentious areas in construction claims because it directly affects the allocation of responsibility.

### Types of Concurrent Delay

**True Concurrent Delay**: Two independent delays occur simultaneously, both on the critical path. Neither party can prove their delay would not have occurred but for the other delay.

**Pacing Delay**: A non-critical delay that appears concurrent but is actually caused by a party deliberately slowing down because the critical path is already delayed. Example: Contractor slows interior work because the building envelope is delayed by owner changes -- the interior slow-down is pacing, not an independent delay.

**Sequential Delay**: Delays that appear concurrent in time but affect different paths. These are not truly concurrent and should be analyzed independently.

### Allocation Methods

**1. Apportionment (Shared Responsibility)**
- Each party bears a proportional share of the delay based on the relative duration and criticality of their respective delays
- Example: If owner caused 7 days of delay and contractor caused 3 days concurrently, owner bears 70% and contractor bears 30%
- Favored in many jurisdictions but requires sufficient evidence to apportion

**2. Dominant Cause**
- The delay that had the greatest impact on the critical path governs
- If owner delay is 7 days on critical path and contractor delay is 3 days on a near-critical path, owner delay dominates
- Used when apportionment is impractical

**3. All-or-Nothing**
- Some jurisdictions hold that if the contractor contributed to any concurrent delay, the contractor recovers nothing
- Harsh rule, but applied in some federal government contexts
- Makes it critical to document that contractor delays were independent and minimal

### Documentation Requirements for Concurrent Delay

1. **Independent analysis**: Analyze each delay separately to show its individual impact
2. **Timeline mapping**: Create a timeline showing when each delay started, ended, and overlapped
3. **Critical path analysis**: Show which delays were on the critical path and which had float
4. **Causation independence**: Document that the delays were caused by different parties for different reasons
5. **Pacing defense**: If accused of concurrent delay, show that any contractor slow-down was pacing a prior owner-caused delay

---



## Claims Package Assembly

### Structure of a Formal Claims Package

A claims package is the formal submission of a claim to the owner, typically after initial notice and failed resolution at the project level. It must be comprehensive, organized, and professionally presented.

#### 1. Cover Letter
- Date, parties, contract reference
- Summary of claim (one paragraph)
- Total amount claimed (time and/or cost)
- Request for resolution meeting or ADR

#### 2. Executive Summary (2-5 pages)
- Project background (brief)
- Chronology of events leading to the claim
- Summary of liability basis (contract provisions supporting the claim)
- Summary of damages (time extension, cost recovery, or both)
- Total claim value with breakdown by category

#### 3. Chronology of Events
- Detailed timeline from project start through the claim events
- Each entry dated with source document reference
- Focus on key events, decisions, and impacts
- Format: Date | Event | Source Document | Impact

#### 4. Liability Analysis
- Contract provisions supporting the claim (quoted with section references)
- Applicable law (state contract law, federal regulations if applicable)
- Comparison of contract requirements to actual events
- Demonstration that the claimed events fall within the contract's remedy provisions

#### 5. Quantum Analysis (Damages Calculation)
- Detailed calculation of each damage category
- Supporting worksheets and backup documentation
- Summary table:

```
| Category | Amount | Basis |
|----------|--------|-------|
| Extended General Conditions | $37,500 | 15 days x $2,500/day |
| Loss of Productivity | $29,250 | Measured mile analysis |
| Acceleration Costs | $18,400 | Overtime + additional crews |
| Home Office Overhead (Eichleay) | $34,521 | 30-day delay period |
| Subcontractor Impacts | $22,000 | Sub claims passthrough |
| Equipment Standby | $8,800 | Idle equipment during delay |
| TOTAL | $150,471 | |
```

#### 6. Schedule Analysis
- Baseline schedule summary
- TIA for each delay event
- As-built schedule reconstruction
- Critical path analysis showing delay impact
- Concurrent delay analysis (if applicable)
- Float consumption summary

#### 7. Supporting Documents Appendix
Organized by exhibit number:
- **Exhibit A**: Notices (all formal notices with proof of delivery)
- **Exhibit B**: Daily reports (for all dates referenced in the claim)
- **Exhibit C**: Correspondence (emails, letters, meeting minutes)
- **Exhibit D**: RFIs and responses
- **Exhibit E**: Change orders (approved and pending)
- **Exhibit F**: Schedule documents (baseline, updates, as-built)
- **Exhibit G**: Cost documentation (invoices, payroll, equipment records)
- **Exhibit H**: Photographs and videos (with photo log)
- **Exhibit I**: Weather data (NOAA records)
- **Exhibit J**: Expert reports (if applicable)

### Organization Principles

- **Chronological within each section**: Events, documents, and evidence organized by date
- **Cross-referenced**: Every statement in the narrative references a specific exhibit
- **Indexed**: Table of contents for the entire package, plus index for each exhibit
- **Paginated**: Sequential page numbers throughout (including exhibits)
- **Electronic and hard copy**: Provide both; electronic version should be searchable PDF with bookmarks

### Expert Report Coordination

When to engage experts:
- **Schedule expert (delay analyst)**: When delay claims exceed $100,000 or involve complex concurrent delays
- **Cost expert (forensic accountant)**: When cost claims exceed $250,000 or involve multiple damage categories
- **Claims consultant**: When total claim value exceeds $500,000 or dispute is headed to arbitration/litigation

---



## Mediation/Arbitration Preparation

### Document Organization for Proceedings

When a claim proceeds to mediation, arbitration, or litigation, document organization becomes critical. The goal is to present a clear, compelling narrative supported by easily accessible evidence.

### Timeline Creation

Build a visual chronology showing:
- Key project milestones (NTP, substantial completion, etc.)
- Delay events with duration bars
- Notice dates (sent and received)
- Correspondence highlights
- Schedule impacts
- Cost accrual points

Format: Wall-sized timeline for hearing room + digital version for screen sharing.

### Witness Identification and Preparation

**Fact witnesses** (people with direct knowledge of events):
- Superintendent(s) who observed conditions
- Project manager who managed communications
- Subcontractor foremen who experienced impacts
- Owner's representatives who gave directives

**Expert witnesses** (if retained):
- Schedule analyst for delay opinions
- Cost consultant for damages opinions
- Industry expert for standard of care opinions

**Witness preparation**:
- Review all documents the witness authored or received
- Identify key events the witness will testify about
- Prepare a timeline of the witness's involvement
- Anticipate cross-examination questions
- Remind witnesses: answer only what is asked, do not volunteer

### Key Document Identification

**Smoking gun documents**: The single most impactful document for each element of the claim. Examples:
- Owner email directing work stoppage (proves the event)
- Daily report showing idle crews (proves the impact)
- Invoice for overtime premium (proves the damages)

**Corroborating evidence**: Secondary documents that support the smoking gun:
- Multiple daily reports showing the same condition
- Photographs confirming written descriptions
- Third-party records (NOAA weather, inspector reports)

### File Organization System

For hearings, organize into binder sets:

**Binder 1: Claim Summary**
- Executive summary, chronology, damages summary

**Binder 2: Contract Documents**
- Relevant contract provisions, specifications, drawings

**Binder 3: Notices and Correspondence**
- All formal notices, key emails, letters

**Binder 4: Daily Reports**
- Daily reports for all dates referenced, tabbed by date

**Binder 5: Schedule Analysis**
- Baseline, updates, as-built, TIA worksheets

**Binder 6: Cost Documentation**
- Invoices, payroll, equipment records, damage calculations

**Binder 7: Photographs and Visual Evidence**
- Photo log with selected key photographs, printed and labeled

---



## Claims Documentation Data Model

### JSON Schema for Claims Management

#### claims-log.json

```json
{
  "claims": [
    {
      "id": "CLAIM-001",
      "status": "active",
      "title": "MEP Design Coordination Delay and Acceleration",
      "type": "delay_and_cost",
      "date_initiated": "2026-03-02",
      "notice_date": "2026-03-02",
      "notice_deadline": "2026-03-22",
      "notice_compliant": true,
      "contract_provision": "AIA A201 Section 15.1.3",
      "description": "Owner approval delay for MEP design revision per RFI-042 caused 8-day delay to critical path MEP rough-in, resulting in 6-day schedule extension and acceleration costs to recover partial schedule.",
      "events": [
        {
          "event_id": "EVT-001",
          "date": "2026-03-01",
          "description": "MEP coordination conflict identified; RFI-042 submitted",
          "type": "trigger",
          "evidence": ["RFI-042", "DR-2026-03-01", "IMG-2026-0301-004"]
        },
        {
          "event_id": "EVT-002",
          "date": "2026-03-08",
          "description": "Architect issued revised drawing M2.1 Rev A",
          "type": "resolution",
          "evidence": ["DWG-M2.1-RevA", "DR-2026-03-08"]
        }
      ],
      "schedule_impact": {
        "delay_days": 8,
        "float_consumed": 2,
        "critical_path_extension": 6,
        "acceleration_days": 3,
        "net_schedule_impact": 3,
        "linked_delays": ["DELAY-005"],
        "tia_performed": true,
        "fragnet_id": "FRAG-005"
      },
      "damages": {
        "extended_general_conditions": 15000,
        "loss_of_productivity": 0,
        "acceleration_costs": 18400,
        "home_office_overhead": 0,
        "subcontractor_impacts": 8000,
        "equipment_costs": 3200,
        "material_escalation": 0,
        "total_claimed": 44600,
        "calculation_method": "actual_cost",
        "supporting_docs": ["INV-XYZ-0308", "PAY-2026-03", "EQ-RENT-0308"]
      },
      "notices": ["NOTICE-001", "NOTICE-003"],
      "linked_delays": ["DELAY-005"],
      "linked_change_orders": ["COR-012"],
      "linked_rfis": ["RFI-042"],
      "linked_daily_reports": ["2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04", "2026-03-05", "2026-03-06", "2026-03-07", "2026-03-08"],
      "evidence_inventory": [
        {
          "exhibit": "A",
          "description": "Notice of Delay dated 2026-03-02",
          "type": "notice",
          "file_ref": "NOTICE-001"
        },
        {
          "exhibit": "B",
          "description": "RFI-042 and architect response",
          "type": "rfi",
          "file_ref": "RFI-042"
        },
        {
          "exhibit": "C",
          "description": "Daily reports 3/1-3/8",
          "type": "daily_report",
          "file_ref": "DR-2026-03-01 through DR-2026-03-08"
        },
        {
          "exhibit": "D",
          "description": "Photographs of MEP conflict area",
          "type": "photo",
          "file_ref": "IMG-2026-0301-004 through IMG-2026-0308-012"
        }
      ],
      "resolution": {
        "status": "pending",
        "method": null,
        "settlement_amount": null,
        "settlement_date": null,
        "notes": ""
      },
      "date_created": "2026-03-02T08:00:00Z",
      "date_updated": "2026-03-15T14:30:00Z"
    }
  ],
  "notice_log": [
    {
      "id": "NOTICE-001",
      "type": "delay",
      "claim_id": "CLAIM-001",
      "date_sent": "2026-03-02",
      "deadline_date": "2026-03-22",
      "contract_provision": "AIA A201 Section 15.1.3",
      "sent_via": ["certified_mail", "email"],
      "tracking_number": "9400111899223100XXXXX",
      "recipients": ["owner_pm@example.com", "architect@example.com"],
      "delivery_confirmed": true,
      "delivery_date": "2026-03-04",
      "response_received": false,
      "response_date": null,
      "follow_up_date": "2026-03-16",
      "content_summary": "Notice of delay due to MEP design coordination issue per RFI-042. Request for time extension and cost adjustment."
    }
  ],
  "evidence_inventory": [
    {
      "id": "EVID-001",
      "type": "daily_report",
      "date": "2026-03-01",
      "description": "Daily report documenting MEP coordination conflict discovery",
      "file_path": "daily-report-data.json#2026-03-01",
      "linked_claims": ["CLAIM-001"],
      "quality_rating": "tier_1",
      "verified": true
    }
  ],
  "timeline_events": [
    {
      "date": "2026-03-01",
      "event": "MEP coordination conflict identified; RFI-042 submitted",
      "type": "trigger",
      "claim_id": "CLAIM-001",
      "category": "design_issue"
    },
    {
      "date": "2026-03-02",
      "event": "Formal delay notice sent (NOTICE-001)",
      "type": "notice",
      "claim_id": "CLAIM-001",
      "category": "procedural"
    },
    {
      "date": "2026-03-08",
      "event": "Architect issues revised drawing M2.1 Rev A",
      "type": "resolution",
      "claim_id": "CLAIM-001",
      "category": "design_issue"
    }
  ],
  "summary": {
    "total_active_claims": 1,
    "total_claimed_amount": 44600,
    "total_recovered_amount": 0,
    "pending_notices": 1,
    "overdue_notices": 0,
    "next_deadline": "2026-03-22",
    "last_updated": "2026-03-15T14:30:00Z"
  }
}
```

---



## Integration with Other Skills

### delay-tracker
- Delay events logged via `/delay` feed directly into claims documentation
- Each DELAY-NNN entry can be linked to a CLAIM-NNN entry
- Delay classification (excusable/compensable) determines claim eligibility
- TIA and critical path analysis from delay-tracker provide schedule impact documentation
- Weather delay data provides environmental claims support

### contract-administration
- Notice provisions (deadlines, delivery methods) from contract analysis
- Dispute resolution procedures (mediation, arbitration, litigation)
- Change order clauses and procedures
- Claims initiation requirements per contract
- Consequential damages waiver identification
- Liquidated damages provisions

### daily-report-format
- Claims-grade daily reports provide the foundation for all claims
- Auto-linking daily reports to delay events and claims
- Daily report fields specifically designed for claims support (headcount by name, exact times, impacts observed)
- Photo documentation integrated with daily reports

### change-order-tracker
- Disputed change orders become potential claims
- COR (Change Order Request) documentation feeds claims package
- Constructive change documentation
- Back-charge disputes

### cost-tracking
- Actual cost data for damages quantification
- Labor hour tracking for measured mile analysis
- Equipment cost tracking for extended rental claims
- General conditions daily rate calculation from actual costs
- Subcontractor cost documentation

### pay-application
- Payment disputes may escalate to claims
- Retainage disputes
- Disputed back-charges on pay applications
- Lien rights and timing (related to but separate from claims)

### safety-management
- Safety incidents caused by owner conditions may support claims
- OSHA compliance costs imposed by changed conditions
- Work stoppage due to unsafe owner-created conditions

### look-ahead-planner
- Three-week look-ahead changes due to delay events
- Documentation of schedule recovery efforts
- Evidence of acceleration measures in look-ahead revisions

---



## Output Routing

All generated documents route to project folder structure:
- **Claims Log**: Stored in `{{folder_mapping.config}}/claims-log.json`
- **Notice Letters**: `{{folder_mapping.correspondence}}/Notices/NOTICE-NNN_[type]_[date].docx`
- **Claims Packages**: `{{folder_mapping.reports}}/Claims/CLAIM-NNN_Package_[date].docx`
- **Evidence Exports**: `{{folder_mapping.reports}}/Claims/Evidence/[exhibit_letter]_[description].pdf`
- **Version History**: Logged in `project-config.json` `version_history` array
- **Backup Copies**: `{{folder_mapping.config}}/backups/claims-log_[TIMESTAMP].json`


