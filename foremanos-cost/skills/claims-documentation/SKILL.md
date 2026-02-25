---
name: claims-documentation
description: >
  Build defensible construction claim records through contemporaneous documentation, formal notice tracking, and claims package assembly. Covers delay claims, cost claims, change order disputes, back-charges, acceleration claims, lost productivity, Eichleay home office overhead, and measured mile analysis. Integrates with daily reports, delay tracker, contract administration, and cost tracking for complete claims support. Triggers: "claim", "claims", "dispute", "notice", "damages", "delay claim", "cost claim", "change order dispute", "back-charge", "Eichleay", "home office overhead", "lost productivity", "acceleration claim", "claims package".
version: 1.0.0
---

# Claims Documentation Skill

## Overview

The **claims-documentation** skill provides construction superintendents and project managers with a systematic framework for building defensible claim records through contemporaneous documentation. The difference between winning and losing a construction claim is almost always documentation quality. Merits matter, but without proper records, even the strongest claim fails.

This skill ensures field teams create claims-grade records from day one -- not after a dispute arises. Retroactive documentation is always weaker than contemporaneous evidence. Courts, arbitrators, and mediators consistently give greater weight to records created at or near the time of the event than to after-the-fact reconstructions, no matter how detailed.

**Core principle**: Document everything as if you will need it in a dispute, even when the project is going smoothly. The cost of over-documenting is trivial compared to the cost of an unsupported claim or an indefensible position.

**What this skill covers**:
- Contemporaneous record standards and admissibility requirements
- Daily report requirements specifically for claims support
- Photo and video documentation standards with chain of custody
- Schedule impact documentation and Time Impact Analysis (TIA)
- Cost impact documentation including measured mile, Eichleay, and acceleration costs
- Causation evidence and the Event-Impact-Damages chain
- Notice requirements and contractual deadlines (the single most important procedural element)
- Concurrent delay identification and allocation
- Claims package assembly for formal submission
- Mediation and arbitration preparation
- Claims-specific data models and JSON schemas
- Integration with delay-tracker, contract-administration, cost-tracking, and other ForemanOS skills

---

## Contemporaneous Record Standards

### What Qualifies as Admissible Evidence in Construction Disputes

**Contemporaneous** = created at or near the time of the event. This is the gold standard for construction claims evidence. Courts and arbitrators heavily favor contemporaneous records over after-the-fact reconstruction because they are less susceptible to bias, faulty memory, and self-serving revision.

### Hierarchy of Evidence Quality

#### Tier 1: Strongest Evidence (Created Same Day)
- **Daily reports** completed and signed on the day of observation
- **Photographs** with original EXIF metadata (GPS coordinates, timestamp)
- **Emails** sent on the day of the event with original headers
- **Inspection reports** signed by inspector on date of inspection
- **Electronic logs** with system-generated timestamps (badge-in/out, GPS trackers, equipment telematics)
- **Weather station data** from on-site instruments or nearest NOAA station
- **Video footage** with embedded date/time overlay

#### Tier 2: Strong Evidence (Created Within 24-48 Hours)
- **Meeting minutes** distributed within one business day of the meeting
- **Handwritten field notes** with date, time, and author identification
- **RFI submissions** documenting conditions observed in the field
- **Delivery tickets** and material receiving documents
- **Time sheets** completed by end of shift or next morning

#### Tier 3: Acceptable Evidence (Created Within One Week)
- **Weekly reports** summarizing daily observations
- **Progress photographs** from regular weekly walkthroughs
- **Schedule updates** reflecting actual progress
- **Cost reports** compiled from daily records

#### Tier 4: Weak Evidence (Created After the Fact)
- **Reconstructed daily reports** written weeks or months later
- **Recollections** documented after a dispute has arisen
- **Undated photographs** without metadata
- **Oral testimony** without supporting documentation
- **Summaries** prepared specifically for the claim

### Record Integrity Requirements

1. **Date and time**: Every record must have a clear date of creation. Electronic records should preserve metadata timestamps. Handwritten notes must include date written.
2. **Author identification**: Who created the record? Name and role of the author must be clear.
3. **Original format preservation**: Keep original files. Do not edit, crop, or modify photographs. Do not alter email chains. Print-to-PDF preserves email formatting and headers.
4. **Chain of custody**: Who has had access to the record? For photographs and electronic files, maintain a log showing: original creation, transfers, storage locations.
5. **Consistency**: Records that contradict each other weaken the claim. Daily reports, photos, and correspondence should tell a consistent story.
6. **Specificity**: Vague records are nearly useless. "Weather delayed work" is weak. "Ambient temperature 28F at 7:00 AM prevented concrete placement per ACI 306 (40F minimum); crew of 6 from ABC Concrete stood down; notified PM at 7:15 AM" is strong.

### Electronic Record Considerations

- **Email**: Preserve full headers (sender, recipient, date, time, subject). Do not forward-only; keep original chain intact.
- **Text messages**: Screenshot with visible phone number and timestamp. Export to PDF for permanent record.
- **Project management software**: Export logs with timestamps. Screenshots showing status changes and dates.
- **BIM/model changes**: Document revision dates and who made changes.
- **GPS/telematics**: Equipment location and operating hours data from fleet management systems.

---

## Daily Report Requirements for Claims Support

Beyond standard daily reporting, claims-grade daily reports must capture significantly more detail than a typical field log. Every superintendent should write daily reports as if they will be read aloud in a deposition or arbitration hearing.

### Required Fields for Claims-Grade Daily Reports

#### 1. Labor Documentation
- **Exact headcount by trade**: Not just "plumbers on site" but "4 plumbers from XYZ Mechanical: J. Smith, R. Jones, M. Davis, T. Williams"
- **Start and stop times by trade**: "Electricians arrived 7:00 AM, departed 3:30 PM (8 hrs); Plumbers arrived 6:30 AM, departed 5:00 PM (9.5 hrs, 1.5 OT)"
- **Specific work activities and locations**: "Electricians pulling wire in Panel Room B2 (grid C-4 to D-6, 2nd floor); Plumbers roughing-in restroom 204 (grid A-2, 2nd floor)"
- **Work NOT performed and reason**: "Mechanical sub could not start ductwork in south wing -- awaiting architect response to RFI-042 (submitted 3/15). 3 sheet metal workers on standby."
- **Productivity observations**: "Framing crew completed 12 LF of partition wall per hour vs. estimate of 18 LF/hr. Reduced productivity due to material staging in work area from concurrent flooring installation."

#### 2. Equipment Documentation
- **Equipment type, size, and identification**: "CAT 320 excavator (Unit #E-207), 40-ton RT crane (Crane #C-003), 2x concrete pump trucks"
- **Hours operated**: "Excavator operated 6.5 hours; Crane on standby 4 hours waiting for steel delivery"
- **Equipment idle time and reason**: "Crane idle from 10:00 AM to 2:00 PM awaiting steel truck delayed in transit (ETA revised 3x)"
- **Equipment moves**: "Concrete pump relocated from east pad to west pad at 1:00 PM (1-hour move time)"

#### 3. Weather Observations
- **Multiple observations per day**: Minimum at start of work, midday, and end of work
- **Temperature**: Actual readings, not "cold" or "warm"
- **Precipitation**: Type (rain, snow, sleet), start/stop times, accumulation
- **Wind**: Speed and direction, especially if affecting crane operations or roofing
- **Ground conditions**: "Standing water in excavation from overnight rain; 2 hours pumping before work could proceed"
- **Impact on work**: Direct connection between weather and work affected

#### 4. Material Deliveries
- **What was delivered**: Material type, quantity, specification
- **Delivery time**: Actual arrival vs. scheduled arrival
- **Condition on arrival**: Accepted, rejected, or accepted with exceptions
- **Delivery ticket reference**: Number and date
- **Storage location**: Where material was staged

#### 5. Visitors and Inspections
- **Who visited**: Name, company, role
- **Purpose of visit**: Inspection, meeting, observation, directive
- **Duration**: Arrival and departure time
- **Outcome**: Inspection passed/failed, directives given, observations made
- **Verbal directives**: Document in writing immediately: "At 10:30 AM, owner's rep John Miller directed crew to stop work on east wall pending review of revised elevation. Directive given verbally; this report serves as written documentation per AIA A201 Section 3.2."

#### 6. Impacts and Delays
- **Work out of sequence**: "Drywall installation in corridor 200 could not proceed because fire sprinkler rough-in not complete. Sprinkler sub reports 3-day delay for fittings. Drywall crew redirected to corridor 300."
- **Waiting for answers**: "MEP coordination hold continues. No response to RFI-042 (submitted 3/15, 12 days outstanding). This exceeds the 7-day contractual response period per spec 01 33 00."
- **Design issues**: "Field measurement shows column C-7 is 4 inches east of plan location. Ductwork routing per mechanical plans will not fit. RFI prepared for submittal tomorrow."
- **Owner/architect directives**: Any direction that changes scope, sequence, or schedule -- even if presented informally.
- **Access restrictions**: "South parking area not available per owner directive; material staging relocated to east lot, adding 200 feet to haul distance."

#### 7. Cross-References
- **Linked delay events**: Reference any active DELAY-NNN entries
- **Linked RFIs**: Reference pending or resolved RFIs affecting today's work
- **Linked change orders**: Reference any pending CORs or approved COs
- **Photo references**: "See photos IMG-2026-0315-001 through IMG-2026-0315-024 documenting conditions"

### Daily Report Writing Standards for Claims

- **Factual, not opinion**: "Concrete test cylinders showed 2,800 PSI at 7 days vs. specified 3,000 PSI" NOT "The concrete was bad"
- **Specific, not general**: Include grid lines, floor numbers, room numbers, compass directions
- **Complete sentences**: Fragments and abbreviations may be misinterpreted later
- **Consistent terminology**: Use the same names for locations, trades, and people throughout the project
- **No blame language**: State facts, not conclusions about fault. "Owner directed work stoppage" not "Owner caused a delay"
- **Preserve uncertainty**: "It appears that..." or "Based on field observation..." rather than definitive statements about matters not fully confirmed

---

## Photo and Video Documentation Standards

### Systematic Evidence Capture

Photography is the most powerful claims documentation tool available to field teams. A single well-timed, well-labeled photograph can be worth more than pages of written narrative. But photographs without context, organization, and metadata preservation are nearly worthless.

### Photo Schedule

**Minimum frequency for claims-sensitive activities**:

| Situation | Minimum Frequency | What to Capture |
|-----------|-------------------|-----------------|
| Normal operations | 2x daily (AM start, PM end) | General progress, crew deployment, conditions |
| Claims-sensitive work | 4x daily (start, mid-AM, mid-PM, end) | Specific activity, conditions, labor, equipment |
| Delay events | Hourly during event | Conditions causing delay, idle crews/equipment, affected areas |
| Differing site conditions | Immediately upon discovery + hourly | Actual conditions vs. expected, scale references, GPS location |
| Owner/architect directives | Before and after | Conditions before directive, work affected, scope changes |
| Weather events | At each weather observation | Sky conditions, precipitation, temperature display, ground conditions |
| Inspections | Before, during, after | Pre-inspection condition, inspector present, results |

### Metadata Preservation

**Critical rule**: Never edit original photo files. Editing, cropping, or filtering photographs destroys or alters EXIF metadata, which reduces evidentiary value.

**EXIF data to preserve**:
- **GPS coordinates**: Proves location of photograph
- **Timestamp**: Proves when photograph was taken
- **Camera/device identification**: Proves which device was used
- **Original file name**: Maintains traceability

**Best practices**:
- Enable GPS tagging on all field cameras and phones
- Verify date/time settings are correct on all devices
- Use a photo management app that preserves original metadata
- When sharing photos, share originals -- do not use messaging apps that strip metadata (iMessage, WhatsApp compress and strip EXIF)
- Store originals in a cloud service that preserves metadata (Google Drive, Dropbox, OneDrive)

### Photo Log Requirements

Every photograph should be traceable through a photo log entry:

```
Photo Log Entry:
  File: IMG-2026-0315-007.jpg
  Date: 2026-03-15
  Time: 10:30 AM
  Location: South Wing, Grid C-4 to D-6, 2nd Floor
  Direction: Facing north
  Photographer: Mike Thompson, Superintendent
  Description: MEP rough-in area showing ductwork routing conflict with structural column C-7.
               Column location prevents designed duct path. See RFI-042.
  Purpose: Document differing field condition vs. mechanical plans (Sheet M2.1)
  Linked To: RFI-042, DELAY-005, Daily Report 2026-03-15
```

### Video Documentation

**Weekly video walkthroughs** for projects with active or potential claims:

- **Duration**: 15-30 minutes covering all active work areas
- **Narration**: Superintendent narrates as they walk -- describing location, conditions, progress, issues
- **Steady movement**: Walk slowly, pause at key areas for 5-10 seconds
- **Scale references**: Include tape measures, rulers, or known objects for scale
- **Date/time**: State date and time at beginning of recording
- **Storage**: Upload same day to cloud storage; do not rely on phone storage alone

**When to increase video frequency**:
- Active delay events: daily video documenting conditions
- Differing site conditions: video immediately upon discovery
- Acceleration periods: video showing additional crews, overtime work
- Disputes in progress: daily video of all affected work areas

### Chain of Custody

For photographs and videos that may become evidence:

1. **Creation**: Document who took the photo/video, when, where, with what device
2. **Transfer**: Log when files are moved from device to computer to cloud
3. **Storage**: Maintain originals in a dedicated, access-controlled folder structure
4. **Access**: Document who has accessed original files and when
5. **Copies**: Clearly mark copies vs. originals; never modify originals
6. **Organization**: Store by date and location: `Photos/2026-03-15/South_Wing/`

### Cloud Backup Protocol

- Upload all photos and videos to cloud storage same day they are taken
- Organize by date, then location, then purpose
- Never delete from cloud storage even if project issue resolves
- Maintain backup on separate service or external drive
- Retention: minimum 6 years after substantial completion (statute of limitations varies by state; 6 years covers most jurisdictions)

---

## Schedule Impact Documentation

### Baseline vs. As-Built Reconciliation

Schedule analysis is the backbone of any delay or acceleration claim. Without a clear comparison between what was planned and what actually happened, there is no way to quantify the impact of a claimed event.

**Three schedules to maintain**:
1. **Baseline Schedule (As-Planned)**: The original contract schedule, accepted by all parties at project start. This is the benchmark.
2. **Updated Schedules**: Periodic schedule updates reflecting actual progress and re-forecasting remaining work. Typically monthly.
3. **As-Built Schedule**: The actual sequence and timing of all activities as they occurred. Reconstructed from daily reports, photos, delivery logs, and inspection records.

### Delay Event Correlation

Every claimed delay event must be mapped to its impact on the schedule:

```
Delay Event → Activity Affected → Float Available → Critical Path Impact → Schedule Extension

Example:
  Event: Owner approval delay for MEP design (RFI-042)
  Activity: MEP Rough-In (Activity ID: MEP-RI-001)
  Float: 2 days available
  Impact: 8-day delay consumed 2 days float, extended critical path 6 days
  Extension: 6 calendar days
```

### Time Impact Analysis (TIA)

The TIA is the gold standard methodology for demonstrating delay causation and quantification. Each delay event gets its own TIA:

**Step 1: Establish Pre-Delay Schedule**
Update the baseline schedule to reflect all actual progress up to the day before the delay event began. This becomes the "but-for" schedule -- what would have happened but for the delay.

**Step 2: Insert Delay Activity (Fragnet)**
Create a "fragnet" (fragment network) representing the delay event:
- Activity name: Description of the delay
- Duration: Actual duration of the delay
- Predecessors: Tie to the activity that was delayed
- Successors: Tie to the activities that could not proceed until delay resolved

**Step 3: Recalculate Schedule**
Run the CPM calculation with the fragnet inserted. The new completion date minus the pre-delay completion date equals the delay impact.

**Step 4: Document Results**
```
TIA Summary:
  Pre-Delay Completion Date:  July 29, 2026
  Post-Delay Completion Date: August 4, 2026
  Delay Impact: 6 calendar days
  Cause: Owner approval delay (RFI-042)
  Critical Path: Confirmed (MEP Rough-In is critical)
  Float Consumed: 2 days
  Net Extension: 6 days
```

### Fragnet Creation

A fragnet is a mini-schedule network inserted into the project schedule to model a specific delay event. For each delay:

```json
{
  "fragnet_id": "FRAG-005",
  "linked_delay": "DELAY-005",
  "description": "Owner approval delay for MEP design revision per RFI-042",
  "activities": [
    {
      "id": "FRAG-005-A",
      "name": "Awaiting architect response to RFI-042",
      "duration_days": 7,
      "predecessor": "MEP-RI-001-START",
      "successor": "FRAG-005-B"
    },
    {
      "id": "FRAG-005-B",
      "name": "Revised submittal review and approval",
      "duration_days": 5,
      "predecessor": "FRAG-005-A",
      "successor": "MEP-RI-001-RESUME"
    }
  ],
  "total_fragnet_duration": 12,
  "float_absorbed": 2,
  "net_critical_path_impact": 10
}
```

### Concurrent Delay Identification

When two or more delays overlap in time:

**Step 1: Identify Overlap**
Map delay date ranges on a timeline. Are any overlapping?

**Step 2: Determine Independence**
Are the delays independent of each other, or did one cause the other?

**Step 3: Determine Path Impact**
Are the delays on the same critical path, different paths, or a combination?

**Step 4: Allocate Impact**
- **Same path, independent delays**: Extension = MAX(delay_1, delay_2), not SUM
- **Different paths**: Each delay analyzed separately against its own path float
- **Causation chain**: If Delay A caused Delay B, total impact is the full chain, attributed to the root cause

### Float Ownership and Consumption Tracking

Float ownership is often disputed. Key positions:

- **Contractor position**: Float belongs to whoever needs it; first to use it owns it
- **Owner position**: Float is a project resource, not belonging to either party
- **Contract language controls**: Many contracts specify float ownership. Check the contract first.

**Tracking requirements**:
- Record baseline float for every activity at project start
- Track float consumption as delays occur
- Document which party consumed float and why
- Flag when critical path shifts due to float consumption

### Acceleration Documentation

**Directed acceleration**: Owner formally directs contractor to accelerate schedule.
- Document: Written directive, acknowledgment, cost proposal, approval
- Cost basis: Overtime premium, additional crews, equipment mobilization, out-of-sequence work premium

**Constructive acceleration**: Owner denies time extension for an excusable delay, forcing contractor to accelerate to meet original deadline.
- Document: Time extension request, denial letter, evidence of excusable delay, evidence of acceleration measures taken
- This is a claim -- the contractor accelerates under protest and seeks cost recovery
- Critical documentation: The denial of the time extension must be clear and documented

**Acceleration cost categories**:
- Overtime labor premium (typically 1.5x or 2x base rate)
- Additional crew mobilization and management
- Expedited material procurement (premium pricing, air freight)
- Out-of-sequence work (reduced productivity from working trades concurrently in same space)
- Extended supervision for multiple shifts
- Productivity loss from fatigue (overtime beyond 50 hrs/week shows measurable decline)

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
