---
name: daily-report-format
description: >
  This skill should be used when the user asks to "create a daily report",
  "generate a daily report", "write today's report", "fill out the daily",
  "do the daily", or needs guidance on construction daily report formatting,
  section content, or professional construction language standards.
  Also handles report amendments — trigger phrases: "fix yesterday's report",
  "amend report", "I need to correct something on a report", "update report #5",
  "change something on a previous report", "amend the daily".
version: 1.0.0
---

# Construction Daily Report Format

## Overview

Generate professional construction daily reports as .docx (Word) files matching the W Principles DailyReport_v5_Fillable.docx template. Apply AI-powered language standardization, automatic photo captioning, and smart photo placement. Optional PDF export via LibreOffice conversion.

## Report Sections (in order)

### 1. Project Info Header
Four-row, four-column table at the top of every report. Fields: Project name, Date, Project No, Report No, Client, Superintendent, Architect, Project Manager. Pull from saved project config if available (see Project Config below).

### 2. Weather Conditions
Section header bar with blue accent (#2E5EAA left edge, #EDF2F9 background). Three-column table: Time | Temperature | Conditions. Standard rows: 7:00 AM, 12:00 PM, 4:00 PM. Below the table, include a narrative paragraph about site conditions (ground conditions, wind, precipitation impact on work).

Below the weather table, include a narrative paragraph about site conditions:

**Narrative rules**:
- If precipitation occurred: state type (rain, snow, sleet), duration, and approximate accumulation
- If temperature triggered a cold/hot weather threshold (from specs-quality.json): state the threshold and protocol activated
- If wind affected crane operations or exterior work: state approximate speed and impact
- If ground conditions affected work: describe conditions (standing water, frozen ground, saturated soil) and areas impacted
- If no weather impact on work: "Weather conditions did not impact work activities."
- Always use past tense, factual statements

### 3. Crew on Site
Table: Subcontractor | Headcount | Work Performed. Include a TOTAL row summing headcount. Leave empty rows for additional subs (template has 10 rows total). Standardize "Work Performed" into professional construction language.

### 4. Materials Received
Table: Material | Supplier | Quantity | PO # | Condition. Use "Good" as default condition unless noted otherwise. If no materials received, write "No material deliveries today."

### 5. Equipment on Site
Table: Equipment | Owner/Sub | Hours | Status. Status options: Active, Idle, Down. If equipment is down, note reason in parentheses.

### 6. Schedule Updates
Fields: Current Phase, Percent Complete (estimate), Upcoming Milestones (next 2 weeks), Delays/Impacts (with cause and duration). Use professional language: "schedule impact" not "we're behind."

### 7. Visitors / Inspections
Table: Name | Organization | Purpose | Time In | Time Out | Result. Result column for inspections: Pass, Fail, Conditional, N/A. If no visitors, write "No visitors or inspections today."

### 8. Site Photos
Embed photos with AI-generated captions. Smart placement rules in `references/photo-guidelines.md`. Each photo gets: a descriptive caption, location reference (grid line, building area, floor level), and compass direction if determinable.

### 9. General Notes
Open narrative section for anything not covered above: conversations with subs, owner directives, RFI status updates, upcoming coordination needs, site condition observations.

### 10. Delay Events

If delay events were logged via `/log` or identified during report collection, include them in the **Schedule Updates** section with structured documentation:

**Format**: "[Description of impact]. Delay type: [type]. Duration: [estimated]. See DELAY-[NNN]."

**Example**: "Concrete placement at east wing foundation delayed due to ambient temperature of 32°F, below the 40°F cold weather threshold per Section 03 30 00. Delay type: Weather. Estimated duration: 2 days. See DELAY-003."

**Integration**: Delay events documented here are automatically linked to `delay-log.json` entries for delay-tracker consumption. If a matching DELAY-NNN entry already exists, reference it. If this is a new delay event, the daily report command will create a new entry.

**Claims mode enhancement**: When claims mode is active, include additional detail: specific start/stop times of work stoppage, workers and equipment affected by name/unit number, activities impacted with schedule IDs, and critical path impact assessment.

## AI Processing Rules

### Language Standardization
Rewrite all user input into professional construction daily report language. See `references/language-standards.md` for patterns. Key principles:
- Third person, past tense for completed work ("Concrete was placed" not "We poured concrete")
- Include specifics: grid lines, floor levels, building areas, spec sections when known
- Quantify where possible: "Approximately 45 CY of concrete placed" not "poured a lot of concrete"
- Use standard construction terminology (see reference file)

### Claims Mode

When `project-config.json` has `claims_mode: true`, apply claims-grade documentation standards on top of standard professional language:

- **Crew descriptions**: Include worker names and start/end times when available
- **Equipment descriptions**: Include unit IDs and idle/standby time
- **Delivery descriptions**: Include ticket numbers and scheduled vs actual times
- **Delay descriptions**: Use complete sentences with exact times, no abbreviations
- **Work not performed**: Explicitly document what was NOT done and why

Standard mode remains the default. Claims mode enhances but does not replace the standard report format.

### Photo Intelligence
When the user uploads photos, analyze content to determine subject, location clues, condition, and visible work. Generate professional captions and place in the most relevant report section. See `references/photo-guidelines.md` for the full captioning rules, smart placement logic, tiebreaker rules, and sizing specifications.

**Report Numbering**: Format `{PROJECT_CODE}-{NNN}`. Auto-increments with duplicate prevention and immediate write-back to prevent collisions. See the `/daily-report` command (Step 1, Report Number Assignment) for the full assignment and locking procedure.

## Visual Design Specs

Match the W Principles DailyReport_v5_Fillable.docx template exactly. Detailed specs in `references/template-spec.md`.
- **Output format:** .docx (Microsoft Word) using the `docx` npm library (docx-js)
- Company logo in header (extract from template or AI - Project Brain/company_logo.png)
- Section header bars: thin blue (#2E5EAA) left accent, light blue (#EDF2F9) background, dark navy text (#1B2A4A)
- Table headers: dark navy (#1B2A4A) background, white text, 8.5pt bold
- Table body: alternating white/light gray rows, 10pt text
- Borders: light gray (#CCCCCC), 1pt
- Page size: US Letter (12240 × 15840 DXA), margins: top/right/left 1440, bottom 1080

### docx-js Critical Rules
- Always use `WidthType.DXA` — never `WidthType.PERCENTAGE` (breaks in Google Docs)
- Set both `columnWidths` on each table AND `width` on each cell
- Use `ShadingType.CLEAR` — never SOLID
- Use separate `Paragraph` elements — never `\n`
- Use `LevelFormat.BULLET` for lists — never unicode bullets
- `ImageRun` requires `type` parameter (png, jpg, etc.)

### Logo Handling
Check for `AI - Project Brain/company_logo.png` first; if not found, extract from the DailyReport template `.docx`. See `references/template-spec.md` (Logo Handling section) for the full procedure, fallback behavior, and exact EMU sizing (2085975 × 638175 EMU ≈ 2.29" × 0.70").

## Project Config and Intelligence

Read from multiple data files in the user's working directory:

### Layer 1: Project Basics
Auto-fills the report header — project name, code, number, team, report numbering. Located in `project-config.json` at `project_basics`.

### Layer 2: Project Intelligence
Deep project knowledge extracted from project documents. Located in multiple files:
- `project-config.json` — Project basics, report tracking, folder mapping, documents loaded, version history
- `plans-spatial.json` — Grid lines, building areas, floor levels, room schedule, site layout, sheet cross-references, quantities, site utilities
- `specs-quality.json` — Spec sections, key materials, weather thresholds, hold points, tolerances, contract, safety, SWPPP, geotechnical, mix designs
- `schedule.json` — Milestones, critical path, near-critical, weather-sensitive activities, long-lead items
- `directory.json` — Subcontractors, subcontractor assignments, vendor database, owner reports
- `inspection-log.json` — Scheduled/completed inspections, permit status, re-inspection items. **Use to**: flag inspections required for today's work, note pending permits, include inspection results in the report narrative.
- `rfi-log.json` — Open RFIs and their status. **Use to**: note when today's work is impacted by an open RFI, include RFI closures in the report, flag overdue RFIs (>14 days).
- `submittal-log.json` — Submittal status and lead times. **Use to**: note when work is waiting on submittal approval, flag critical-path submittals approaching deadline.
- `pay-app-log.json` — Payment status and schedule of values. **Use to**: reference percent complete from SOV when reporting progress on major work items.

Data is managed by the **project-data** skill and extracted by the **document-intelligence** skill.

Use the project-data skill's **smart retrieval** to pull only relevant intelligence based on the work being documented. Don't load entire files — request data by work type, location, or subcontractor. The project-data skill cross-references related information automatically.

This data powers the smart features:

- **Grid lines and building areas** (from `plans-spatial.json`) → Used to add specifics when the user gives general locations. "Poured the east side" becomes "Concrete placed at East Wing, Grid Lines E-G / 1-5."
- **Subcontractor directory** (from `directory.json`) → Matches casual sub references to official names. "Walker was here" becomes "Walker Construction (3 workers)."
- **Schedule milestones** (from `schedule.json`) → Adds context to schedule updates. "Foundation work continuing. Foundation Complete milestone: 03/15/2026."
- **Material specs** (from `specs-quality.json`) → Enriches material references. "Poured footings" becomes "Concrete placed per Section 03 30 00, 4000 PSI mix design."
- **Site layout / compass orientation** (from `plans-spatial.json`) → Improves photo captions with direction and area references.
- **Testing requirements** (from `specs-quality.json`) → Flags required inspections for current work types.
- **Floor levels and room schedule** (from `plans-spatial.json`) → Proper naming for interior work locations.
- **Weather thresholds** (from `specs-quality.json`) → Compares today's weather against spec limits for documented work. Flags cold-weather concrete protocols, wind limits for crane operations, moisture restrictions for roofing, etc.
- **Hold points and witness points** (from `specs-quality.json`) → Identifies required inspection stops based on the work being performed. "Concrete placed" triggers a check: was a pre-placement inspection documented?
- **Quality tolerances** (from `specs-quality.json`) → Adds spec-level detail to inspection results and material documentation. Slump ranges, compaction densities, steel erection tolerances.
- **Geotechnical data** (from `specs-quality.json`) → Enriches earthwork documentation with bearing capacity, compaction requirements, and dewatering triggers.
- **Safety zones** (from `specs-quality.json`) → Notes when work occurs in fall protection zones, confined spaces, or hot work areas. Adds safety context to crew descriptions.
- **SWPPP / erosion control** (from `specs-quality.json`) → Checks precipitation against inspection triggers. Flags when BMP inspections are required based on rainfall.
- **Quantities** (from `plans-spatial.json`) → When work is reported, include relevant quantities and progress percentages. "Completed VCT in Rooms 007-009: 1,240 SF of 4,800 SF total VCT (26% complete)." "Poured Footings F1-F4: 9.5 CY of 42.3 CY total footings (22% complete)." Source attribution tracks whether quantities came from DXF, visual analysis, takeoff, or text extraction.
- **Sheet cross-references** (from `plans-spatial.json`) → When referencing specific plan elements, note which sheets contain the relevant details. "Footing F1 per S2.1, detail on S5.1." This helps the field crew find the right sheet quickly.
- **Inspection status** (from `inspection-log.json`) → Cross-checks today's work against required inspections. "Foundation rebar placed — pre-pour inspection scheduled for 2/24." Flags if inspection is overdue or permit not yet obtained.
- **Open RFIs** (from `rfi-log.json`) → Notes when documented work is affected by pending RFIs. "Framing at corridor partition on hold — RFI-003 (wall type clarification) pending architect response since 2/10." Includes RFI closures received today.
- **Submittal status** (from `submittal-log.json`) → Flags when work depends on submittal approvals not yet received. "Door frame installation pending — SUB-001 (HM Doors/Frames) still under review." Notes submittals approved today that unblock upcoming work.

If project intelligence exists, ALWAYS use it to enrich the report. If it doesn't exist, generate the report without it — just use whatever details the user provides.

See the **project-data** skill for the full schema and retrieval patterns. See the **document-intelligence** skill for how data is extracted from project documents.

### Layer 3: Report QA
After report content is generated but before the .docx is created, the **report-qa** skill reviews the report against project intelligence. It catches missing inspections, weather threshold conflicts, unrecognized subs, and other gaps. See the report-qa skill for details.

### Layer 4: Report History
After the .docx is generated, a structured copy of the report data is saved to `daily-report-data.json` for use by the **project-dashboard** skill. This enables the Weekly and Project dashboard views. See the project-data skill's report history schema for the data format.

## Output

Generate the report as a .docx file using the `docx` npm library (docx-js). Name format: `{M_D_YY}_Daily_Report_{PROJECT_CODE}.docx` (e.g., `2_14_26_Daily_Report_MOSC.docx`).

### PDF Export Option
After generating the .docx, ask: "Also export as PDF?" If yes, convert using LibreOffice:
```bash
python3 {scripts_path}/office/soffice.py --headless --convert-to pdf {docx_path}
```
Save both the .docx and .pdf to `folder_mapping.daily_reports`.

## Related Skills

- **document-intelligence** — classifies and extracts data from project documents
- **project-data** — manages the project intelligence store and report history; use for smart retrieval
- **quantitative-intelligence** — provides measured quantities, cross-sheet references, and progress percentages for report enrichment
- **report-qa** — reviews the generated report for completeness and consistency before .docx creation
- **project-dashboard** — generates interactive HTML dashboard from report history

## Report Amendment

When the user asks to amend a previously generated report ("fix yesterday's report", "amend report #5", "I need to correct something"), follow this workflow:

### Step 1: Identify the Report
- If the user specifies a report number (e.g., "amend MOSC-005"), look it up directly in `daily-report-data.json`
- If the user says "yesterday's report" or "last report", find the most recent entry in report history
- If ambiguous, show the last 5 reports and ask which one to amend:
  "Which report? Here are the most recent: MOSC-005 (2/14), MOSC-004 (2/13), MOSC-003 (2/12)..."

### Step 2: Load the Report Data
- Load the full structured data for the identified report from `daily-report-data.json`
- Present a summary of the original report so the user can see what they're working with

### Step 3: Collect Amendments
- Accept corrections conversationally — the user can say things like:
  - "Add Metro Concrete, 4 guys doing formwork"
  - "Change the weather to partly cloudy"
  - "Remove the note about the crane"
  - "The inspection was conditional, not a pass"
- Apply the same AI processing rules (language standardization, entity resolution, enrichment)

### Step 4: Apply and Confirm
- Show the user what changed (before → after for each amendment)
- Wait for confirmation before regenerating

### Step 5: Re-run Report QA
- Run the report-qa skill checks against the amended report data
- Present any new flags

### Step 6: Regenerate the .docx
- Generate a new .docx with "AMENDED" watermark and amendment date in the header
- Name format: `{M_D_YY}_Daily_Report_{PROJECT_CODE}_AMENDED.docx`
- Keep the original report number — do not assign a new one
- If the user also wants a PDF, convert via LibreOffice after generating the .docx

### Step 7: Update Report History
- Update the report entry in `daily-report-data.json` with:
  - The amended data
  - An `amendments` array recording what changed, when, and why
  - `amended_date` timestamp
- Preserve the original data in a `pre_amendment` field for audit trail

## Additional Resources

- **`references/template-spec.md`** — exact dimensions, colors, fonts, and spacing
- **`references/language-standards.md`** — professional construction language patterns and examples
- **`references/photo-guidelines.md`** — photo captioning and smart placement rules
- **`references/project-intelligence.md`** — how to extract and use project knowledge from documents
