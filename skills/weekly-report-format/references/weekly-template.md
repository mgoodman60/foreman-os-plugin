# Weekly Report Template Specification

## Document Setup

### Page Configuration
- **Format:** US Letter (8.5" × 11")
- **Margins:** 1" on all sides (top, bottom, left, right)
- **Orientation:** Portrait
- **Font:** Segoe UI or Calibri, 11pt body text
- **Line Spacing:** 1.15 for body text, single for tables

### Color Palette (consistent with daily report visual identity)
- **Navy (Primary):** #1B2A4A — Headers, footers, accent lines
- **Blue (Secondary):** #2E5EAA — Section headers, table headers, emphasis
- **Light Blue (Background):** #EDF2F9 — Table alternate rows, header backgrounds
- **Dark Gray (Body):** #333333 — Body text
- **Medium Gray (Secondary text):** #666666 — Subtitles, captions

### Header Bar (Top of Every Page)
- **Height:** 0.75"
- **Background:** Navy #1B2A4A
- **Content Layout:**
  - Left: Project name (bold, white, 14pt)
  - Center: Week Ending [DATE] (white, 11pt)
  - Right: Report Number (WR-XXX, white, 11pt)
- **Bottom Border:** Blue #2E5EAA, 2pt

---

## Page 1 Structure

### 1. Title Section (After Header)
- **Project Code** — Navy #1B2A4A, 10pt, bold
- **Project Name** — Navy #1B2A4A, 18pt, bold
- **Week Ending:** [DATE] — Blue #2E5EAA, 12pt
- **Report #:** WR-XXX — Dark Gray, 10pt
- **Spacing:** 0.5" below header bar; 0.25" between lines

### 2. Executive Summary
- **Section Header:** "Executive Summary" — Navy #1B2A4A, bold, 12pt
- **Divider:** Thin line (Blue #2E5EAA, 1pt) below header
- **Content:** 2–3 sentences, bold formatting, 11pt
- **Background:** Light Blue #EDF2F9 box (0.1" padding)
- **Spacing:** 0.25" above and below section
- **Purpose:** High-impact opening telling the week's story in owner-friendly language

**Aggregation Rules:**
- Lead with most significant accomplishment or milestone achieved
- Acknowledge any major challenges and mitigation approach
- End with forward-looking statement about momentum

**Language Example:**
> "The team completed structural steel installation on Schedule B, achieving 65% overall project completion—a 5% increase from the previous week. Weather delays on Tuesday and Wednesday (8 hours total) were mitigated by accelerated interior MEP rough-in, keeping critical path activities on track. The focus for the coming week is concrete placement for the parking structure, pending final rebar inspection on Monday."

---

### 3. Schedule Status
- **Section Header:** "Schedule Status" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content Layout:**
  - **Current Phase:** [Phase name], [% complete] (up X% from last week)
  - **Paragraph narrative** (4–6 sentences) covering:
    - Current phase name and percent complete
    - Week-over-week progress notation (e.g., "up 5% from last week")
    - Upcoming milestone tracker (table or inline list)
    - Any delays and mitigation plans
  - **Upcoming Milestones Table:**
    - Columns: Milestone | Planned Date | Status | Notes
    - Rows: 3–5 upcoming milestones
    - Table header: Blue #2E5EAA background, white text
    - Alternate row colors: Light Blue #EDF2F9 every other row
    - Border: Light gray, 0.5pt

**Aggregation Rules:**
- Extract percent complete from first and last daily report of week
- Calculate change (e.g., Mon: 40%, Fri: 45% = "up 5% from last week")
- Reference schedule milestones from `schedule.json`
- For each milestone: note actual date if completed this week, or planned date if upcoming
- If delays exist: state cause (weather, material, inspection hold, etc.), quantify delay hours, and describe mitigation

**Language Example:**
> "Schedule B structural work progressed to 65% complete this week, an increase of 5 percentage points from the previous week. The installation of roof trusses on Buildings A and B proceeded ahead of schedule, while weather delays on Tuesday and Wednesday (total 8 hours) were absorbed through overtime scheduling and accelerated MEP work in Building C. The structural inspection is scheduled for Monday, with concrete placement for the parking structure planned for Wednesday pending rebar approval."

---

### 4. Work Accomplished
- **Section Header:** "Work Accomplished" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:** Narrative paragraphs organized by trade or building area, 4–8 sentences total
- **Sub-headers (if applicable):** Building/Area names in Blue #2E5EAA, 11pt, bold
- **Spacing:** 0.1" between trade/area sections

**Aggregation Rules:**
- Review all daily reports for the week
- Group work by trade (Structural, MEP, Drywall, Finishes, etc.) or by building area (Building A, Building B, etc.)
- Choose organization based on what makes most sense for the project (if work is spread across multiple buildings, organize by building; if work is concentrated in one area, organize by trade)
- Summarize key activities and accomplishments, not a line-by-line dump of every task
- Include crew/subcontractor names for significant work
- Emphasize progress, completion, and forward momentum
- Avoid daily minutiae; focus on narrative arc of the week's work

**Language Example (by Trade):**
> "**Structural Steel & Framing:** The team completed installation of columns and beams for Schedule B, working through a compressed timeline due to earlier delays. Heavy civil contractor (ABC Steel) deployed a crew of 8 daily, completing an average of 12 column connections per day. Welding and bolt torque inspection proceeded in parallel, positioning the structural package for final inspection by Monday.
>
> **MEP Rough-in:** Mechanical and electrical crews accelerated rough-in work in Building C to absorb weather delays from earlier in the week. Plumbing rough-in in Building A was completed for drywall framing, and electrical conduit and box rough-in progressed in Building B. The MEP team coordinated a material delivery of ductwork and electrical panels on Thursday, preparing for next week's installation phase."

---

### 5. Crew Summary
- **Section Header:** "Crew Summary" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Table:** Subcontractor attendance and headcount
    - Columns: Subcontractor | Days on Site | Avg Headcount | Key Work
    - Rows: One per active subcontractor + Total row
    - Table header: Blue #2E5EAA, white text
    - Alternate rows: Light Blue #EDF2F9
    - Total row: Slightly darker shading, bold text
  - **Narrative Summary (below table):** 2–3 sentences on staffing trends and planned changes

**Aggregation Rules:**
- Extract each unique subcontractor from daily reports for the week
- For each sub: count days present (Mon–Fri); calculate average crew size across those days; summarize primary work (1–2 words)
- Total row: Sum of days (if tracking), sum of headcount across all days, sum of total unique headcount, "All Trades"
- In narrative: Note any staffing increases or decreases planned for coming week
- Flag any attendance issues or unexpected changes

**Table Layout:**
| Subcontractor | Days on Site | Avg Headcount | Key Work |
|---|---|---|---|
| ABC Structural | 5 | 8 | Steel erection |
| XYZ Mechanical | 4 | 6 | MEP rough-in |
| General Crew | 5 | 12 | Demolition, framing |
| **Total** | **—** | **26** | **—** |

**Language Example (Narrative):**
> "The crew averaged 26 workers across all trades this week, with structural and MEP trades running at peak strength. General labor contingent was reduced from 15 to 12 daily due to completion of demolition; these workers transitioned to framing support. Next week, we anticipate an increase to 30 workers as drywall and finish trades ramp up, pending inspection approvals."

---

## Page 2 Structure

### 6. Upcoming Work (Next Week)
- **Section Header:** "Upcoming Work" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:** 3–5 sentences forward-looking preview
- **Tone:** Confident and momentum-forward
- **References:** Schedule, current trajectory, dependencies

**Aggregation Rules:**
- Review schedule milestones and planned activities for the coming week
- Cross-reference with current percent complete and any open items or dependencies
- Identify any material deliveries, inspections, or approvals needed before work can proceed
- Highlight any risks or critical paths

**Language Example:**
> "The coming week focuses on completion of structural inspection and concrete placement for the parking structure, pending delivery of final rebar materials (due Monday). Drywall framing in Buildings A and B will advance in parallel with MEP rough-in completion. Finish material deliveries, including flooring and interior doors, are scheduled for Wednesday and Thursday, positioning the team to begin flooring installation the following week. The team is on track to meet the phase completion milestone of 70% by Friday."

---

### 7. Weather Summary
- **Section Header:** "Weather Summary" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Overview:** Temperature range, precipitation, notable conditions
  - **Delays:** Days affected, type of delay (work stoppage, reduced productivity, etc.), total hours
  - **Schedule Impact:** How delays were mitigated or absorbed

**Aggregation Rules:**
- Extract weather conditions from each daily report
- Consolidate into overview narrative (don't list each day separately)
- For each day with weather impact, extract delay hours and notes
- Sum total delay hours for the week
- Reference mitigation strategies mentioned in daily reports

**Language Example:**
> "Weather conditions ranged from clear and 65°F on Monday to rainy and 52°F on Tuesday and Wednesday. Tuesday and Wednesday rain events caused a total of 8 hours of work delays due to site safety protocols and material staging constraints. The team mitigated these delays by accelerating covered interior work and scheduling overtime on Thursday and Friday, keeping the critical path on schedule. Forecast for the coming week is favorable (clear to partly cloudy, highs of 68°F) with no anticipated weather-related delays."

---

### 8. Inspections & Testing
- **Section Header:** "Inspections & Testing" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Narrative Summary:** 2–3 sentences
  - **Inspections Table:**
    - Columns: Inspection Type | Date | Inspector | Result | Notes
    - Rows: All inspections conducted during the week
    - Table header: Blue #2E5EAA, white text
    - Alternate rows: Light Blue #EDF2F9
  - Results: PASS / FAIL / CONDITIONAL (passed with notes requiring follow-up)

**Aggregation Rules:**
- Extract all inspections mentioned in daily reports
- Group by type (Building Inspection, Structural, MEP, etc.)
- For each: capture date, inspector/authority, result, and any follow-up notes
- Conditional passes: note the specific item(s) requiring correction and expected resolution date
- Create summary: "X inspections conducted; Y passed, Z conditional, 0 failed"

**Language Example (Narrative):**
> "Five inspections were conducted this week: the building envelope inspection and structural rebar inspection both passed, while the electrical rough-in inspection passed conditionally with 3 minor items requiring correction before concealment. HVAC ductwork inspection is scheduled for Monday. Follow-up on the three electrical items is planned for Monday morning, keeping the drywall schedule intact."

**Table Layout:**
| Inspection Type | Date | Inspector | Result | Notes |
|---|---|---|---|---|
| Building Envelope | Mon 2/10 | City Inspector | PASS | — |
| Structural Rebar | Fri 2/14 | Structural Eng. | PASS | — |
| Electrical Rough-in | Thu 2/13 | City Inspector | CONDITIONAL | 3 minor box/conduit items; correction Tue 2/16 |
| HVAC Ductwork | (Scheduled) | Mech. Eng. | (PENDING) | Mon 2/17 |

---

### 9. Materials & Deliveries
- **Section Header:** "Materials & Deliveries" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Narrative Summary:** List significant deliveries, any issues
  - **Upcoming Deliveries:** Materials expected in coming week

**Aggregation Rules:**
- Extract all material deliveries from daily reports
- Note delivery date, material type, quantity (if noted), and any issues (damage, incomplete, incorrect)
- Flag any materials that arrived late or with damage; note impact on schedule
- For upcoming deliveries: reference purchase orders or delivery schedules from `procurement-log.json`

**Language Example:**
> "Deliveries this week included structural steel (completed Thursday per schedule), electrical panels and conduit (Thursday), and plumbing rough-in materials (Friday). All materials arrived in good condition and on schedule. Upcoming deliveries for the coming week include drywall materials (Monday), flooring substrate and underlayment (Wednesday), and interior doors and frames (Thursday). No supply chain issues are anticipated."

---

### 10. Active Issues & Open Items
- **Section Header:** "Active Issues & Open Items" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Issues Table:**
    - Columns: Item | Date Opened | Status | Expected Resolution
    - Rows: All open items and issues
    - Table header: Blue #2E5EAA, white text
    - Alternate rows: Light Blue #EDF2F9
    - Color-code critical or overdue items: light red background (#FFE6E6) or bold red text

**Aggregation Rules:**
- Gather all open items and issues from all daily reports for the week
- Classify: NEW (opened this week), CARRIED FORWARD (pre-existing), or RESOLVED (closed this week)
- For each open item: capture date opened, current status, target resolution date
- Flag any that are overdue or critical to schedule
- If no issues, state: "No critical issues identified this week. X minor items are being tracked and are not expected to impact schedule."

**Language Example (if issues exist):**
> "Two issues are under active mitigation. The delayed delivery of Window Set A (opened 2/1, now due Monday 2/17) is being tracked with the supplier; this has been absorbed into the schedule with a 2-day buffer. Electrical panel modification for Building B (opened 2/10) is in progress with the electrical contractor and is expected to be resolved by Tuesday 2/16, maintaining schedule. All other minor items are tracking to resolution on schedule."

**Table Layout:**
| Item | Date Opened | Status | Expected Resolution |
|---|---|---|---|
| Window Set A Delivery | 2/1 | In Transit | Mon 2/17 |
| Electrical Panel Modification (Building B) | 2/10 | In Progress | Tue 2/16 |
| Rebar Spacing Correction | 2/14 | Scheduled | Mon 2/17 |

---

### 11. Safety
- **Section Header:** "Safety" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Safety Posture Summary:** 1–2 sentences on overall week safety
  - **Incidents:** (Hopefully none; if any, state briefly with action taken)
  - **Near-Misses & Observations:** Bullet list of items noted by crew or superintendent
  - **Toolbox Topics:** Topics covered during crew safety meetings
  - **Forward Statement:** 1–2 sentences on safety focus going forward

**Aggregation Rules:**
- Extract all safety notes from daily reports
- Incidents: Any recordable or near-miss events; note what happened, who was involved (generically), what action was taken
- Observations: General safety behaviors, hazards noted and mitigated, close calls
- Toolbox topics: Safety themes discussed during crew meetings
- If no incidents: lead with positive statement about safety culture and near-miss awareness

**Language Example (No Incidents):**
> "The team maintained a strong safety culture this week with no incidents or near-misses reported. Observations noted include excellent PPE compliance, orderly housekeeping in staging areas, and proactive communication regarding tie-off points during high-access work. Toolbox topics included fall protection review (Tuesday) and electrical safety during conduit work (Thursday). The safety focus for the coming week will be drywall installation safety, including proper scaffolding use and dust control procedures."

**Language Example (With Incident):**
> "One near-miss was reported on Wednesday when a worker nearly stepped off the edge of a platform due to inadequate guardrailing. The incident was immediately mitigated by installing temporary guardrails, and the full crew was briefed on the hazard and preventive measures. No injuries resulted. All incidents and near-misses are reviewed daily, and corrective actions are implemented immediately. The safety focus for the coming week is platform and fall protection awareness during drywall installation."

---

### 12. Site Photos
- **Section Header:** "Site Photos" — Navy #1B2A4A, bold, 12pt
- **Divider:** Blue #2E5EAA, 1pt line below header
- **Content:**
  - **Photo Layout:** 2-up (two photos side-by-side) or 3-up (three photos) as space allows
  - **Photo Size:** Typically 3" wide × 2" tall (2:3 aspect ratio) for 2-up layout, or 2.25" wide × 1.5" tall for 3-up
  - **Spacing:** 0.2" between photos and caption
  - **Captions:** Below each photo, centered, 9pt, Dark Gray #333333
    - Format: One sentence, present tense, describing what is shown and its significance
    - Examples: "Structural steel erection in Building A, showing progress toward completion."
    - "Interior MEP rough-in in progress, with ductwork installation underway in Building C."
    - "Completed envelope work on Building B, ready for interior finishing."

**Photo Selection Rules:**
- Select up to 5 photos from the week's daily reports
- Prioritize:
  1. Major work areas showing tangible progress
  2. Completed milestones or phases
  3. Different building areas or trades (visual variety)
  4. Images that communicate progress to owner (before/after, structural elements, finishes, critical path work)
- Avoid:
  - Blurry or poorly lit photos
  - Photos lacking clear work context
  - Duplicate or redundant images
  - Photos of individuals (unless necessary to show scale or crew involvement)
- Ensure photos are dated and correspond to the report week

**Layout Examples:**
- **2-up layout (Page 2):** Two 3" × 2" photos side-by-side; allows room for caption and section content
- **If page 3 is needed:** 3-up layout (3 photos, 2.25" × 1.5" each) or 2-up with larger captions

---

## Page 3 Structure (if needed)

### Continuation of Site Photos
- If more than 2 photos are included, continue photos on page 3 using same formatting
- Maintain consistent spacing and caption style

### 13. Footer Block (All Pages)
- **Height:** 0.5"
- **Background:** Navy #1B2A4A
- **Content Layout:**
  - **Left:** Distribution List (see below)
  - **Right:** Report Details (see below)
- **Signature Block:** (On final page)
  - Line 1: Superintendent: _________________ Date: _________
  - Line 2: Project Manager: ________________ Date: _________

### Distribution List
- Extract from `specs-quality.json` under `contract.documentation_requirements.distribution_list` key
- Format: Comma-separated or bullet list, 9pt, white text
- Typical list: Owner, Project Manager, Construction Manager, Superintendent, Key Subcontractors, Architect/Engineer
- Example: "Distribution: Owner, PM, CM, Superintendent, Structural Engineer, MEP Lead"

### Report Details
- **Report #:** WR-XXX (auto-incremented each week)
- **Next Report Date:** Week ending [next Friday date]
- **Font:** 9pt, white text

---

## Table Formatting Standards

All tables throughout the document use consistent formatting:

### Table Header
- **Background Color:** Blue #2E5EAA
- **Text Color:** White
- **Font:** Bold, 11pt
- **Padding:** 0.1" top and bottom
- **Border:** Light gray, 0.5pt

### Table Data Rows
- **Alternate Row Colors:** 
  - Odd rows: White background
  - Even rows: Light Blue #EDF2F9
- **Text Color:** Dark Gray #333333 (body), Navy #1B2A4A (important data)
- **Font:** Regular, 10pt
- **Padding:** 0.05" top and bottom
- **Border:** Light gray, 0.5pt
- **Alignment:** Left-aligned for text, center-aligned for numbers/dates

### Total/Summary Row (if applicable)
- **Background:** Slightly darker than even rows (Light Blue with 20% gray overlay), or light gray
- **Text:** Bold, Navy #1B2A4A
- **Border:** Light gray, 0.5pt, slightly heavier (1pt) top and bottom

### Critical Items (Issues, Overdue)
- **Optional Highlight:** Light red (#FFE6E6) background for critical or overdue items
- **Or:** Red text (#C00000) for item descriptions
- **Use sparingly** — only for items requiring owner attention

---

## Aggregation Rules by Section

### General Principles
1. **Do not duplicate information** — Each fact appears once in the report, in the most relevant section
2. **Organize by importance to owner** — Schedule, cost/resource impact, risk mitigation first
3. **Use narrative + data** — Combine flowing prose with tables/numbers for clarity
4. **Tell a coherent story** — The report should flow from accomplishments to challenges to upcoming work
5. **Quantify everything** — Use actual numbers (percent complete, hours, crew counts, inspection results)
6. **Forward momentum** — End each section looking ahead to next steps

### Section-Specific Aggregation

**Executive Summary:**
- One sentence: primary accomplishment this week
- One sentence: primary challenge + mitigation (if any)
- One sentence: forward-looking statement about next week

**Schedule Status:**
- Percent complete from first and last day of week (calculate % change)
- List of 3–5 upcoming milestones with planned dates
- Summary of delays (if any) with mitigation

**Work Accomplished:**
- Group by trade or building area (choose based on project structure)
- For each trade/area: one paragraph summarizing activities, crew involved, key accomplishments
- Avoid detailed task lists; focus on narrative arc and major milestones

**Crew Summary:**
- One row per active subcontractor (from all daily reports)
- Calculate average headcount for subcontractor across days present
- Total row: sum of unique headcount and all trades

**Upcoming Work:**
- Pull from schedule for next week
- Cross-reference with current trajectory and dependencies
- Highlight critical deliveries, inspections, or approvals

**Weather Summary:**
- One paragraph covering: conditions, delays, impact on schedule
- Use actual numbers: temperature range, delay hours, days affected

**Inspections & Testing:**
- One row per inspection (combine multiple inspections of same type if more than 5)
- Summary counts: "X inspections, Y passed, Z conditional, 0 failed"

**Materials & Deliveries:**
- Bullet or paragraph form: notable deliveries this week, any issues
- Upcoming deliveries for next week

**Active Issues & Open Items:**
- One row per open item
- Classify: NEW, CARRIED FORWARD, or RESOLVED
- Flag critical or overdue items visually

**Safety:**
- Summary statement on safety culture
- List of incidents, near-misses, observations
- Toolbox topics
- Forward-looking statement on safety focus

**Site Photos:**
- Up to 5 photos
- Prioritize progress, variety, owner-relevant images
- One-sentence captions, present tense

---

## Visual Design Notes

### Typography
- **Headings:** Navy #1B2A4A, bold, sans-serif (Segoe UI or Calibri)
- **Body Text:** Dark Gray #333333, regular, sans-serif
- **Emphasis:** Bold text (not italics) for important data and callouts
- **Captions:** Medium Gray #666666, 9pt

### Spacing & Layout
- **Section spacing:** 0.25" below section header; 0.1" above next section header
- **Paragraph spacing:** 0.05" between paragraphs within a section
- **Table spacing:** 0.1" above and below tables
- **Page breaks:** Avoid orphaning section headers at bottom of page; break after complete section

### Consistency with Daily Report
- Match color scheme exactly (Navy, Blue, Light Blue palette)
- Use same table formatting (headers, alternate rows)
- Match typography style (Segoe UI or Calibri, same sizes)
- Ensure weekly and daily reports have cohesive visual identity

---

## Document Generation Checklist

- [ ] All sections present and in order
- [ ] Project name, code, week-ending date correct
- [ ] Report number (WR-XXX) auto-incremented
- [ ] All tables render with correct formatting and alignment
- [ ] Photos are clear, relevant, and properly captioned
- [ ] No orphaned text or formatting errors
- [ ] All data (percentages, counts, dates) verified against source data
- [ ] Narrative tone is professional and owner-appropriate
- [ ] Footer contains correct distribution list and signature block
- [ ] File size is reasonable (typically 2–5 MB with photos)
- [ ] File naming convention followed: {PROJECT_CODE}_Weekly_Report_{YYYY-MM-DD}.docx (and optional .pdf)
- [ ] File saved to owner_reports directory per project-config.json folder_mapping

