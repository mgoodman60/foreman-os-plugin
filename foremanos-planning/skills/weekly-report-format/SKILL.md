---
name: weekly-report-format
description: >
  Generate polished weekly owner/PM summary reports from daily report data. Use when the user asks to
  "generate a weekly report", "weekly summary", "owner report", "weekly owner report", "PM report",
  "send the weekly", "weekly update", or wants to aggregate daily reports into a weekly narrative.
version: 1.0.0
---

# Weekly Report Format Skill

## Overview

This skill aggregates a week's worth of daily reports into a professional weekly summary designed for owner and project manager communication. The output is a polished .docx (Word) report with optional PDF export that tells the story of the previous week's progress, challenges, and upcoming work.

Each weekly report includes:
- **Executive Summary** — A concise 2-3 sentence overview capturing the week's narrative arc
- **Schedule Status** — Current phase, percent complete with week-over-week change, milestone tracking, and delay mitigation
- **Work Accomplished** — Narrative summary of key activities organized by trade or building area
- **Crew Summary** — Attendance patterns and subcontractor deployment across the week
- **Upcoming Work** — Forward-looking preview of next week's planned activities
- **Weather Impact** — Conditions overview and any schedule delays caused by weather
- **Inspections & Testing** — Summary of inspections conducted and results
- **Materials & Deliveries** — Notable material arrivals and any supply chain issues
- **Active Issues & Open Items** — Tracked problems with status and expected resolution dates
- **Safety Summary** — Incidents, near-misses, observations, and toolbox talk topics
- **Site Photos** — Up to 5 representative images with captions showing progress and site conditions
- **Distribution & Signature** — Standard footer with distribution list and signature block for superintendent

The report is written in a confident, forward-looking tone appropriate for owner-level communication. Language is professional but accessible, focused on progress and momentum with issues addressed matter-of-factly and clear mitigation plans.

## Data Sources

- **daily-report-data.json** — All daily reports for the target week; provides raw data for aggregation (crew counts, weather, inspections, materials, safety, photos, open items)
- **project-config.json** — Project basics (name, code, location) and output directory paths
- **schedule.json** — Schedule milestones
- **specs-quality.json** — Contract documentation requirements, distribution list
- **change-order-log.json** — Change order data for weekly CO summary
- **inspection-log.json** — Inspection data including permit info
- **meeting-log.json** — Meeting records
- **punch-list.json** — Punch list items
- **rfi-log.json** — RFI status summary: new this week, closed this week, total open, aging (>14 days)
- **submittal-log.json** — Submittal status summary: submitted this week, approved, rejected/resubmit, critical-path items
- **pay-app-log.json** — Current billing status, retainage, percent complete from SOV
- **labor-tracking.json** — Weekly labor hours by trade, crew count trend, productivity metrics
- **quality-data.json** — Quality inspection results for the week, open deficiencies

## Workflow

### 1. Determine Target Week
- Default: Most recent complete week (Monday–Friday, ending on most recent Friday)
- User-specified: Accept week-ending date in format MM/DD/YYYY, YYYY-MM-DD, or "week ending [date]"
- Validate that at least 3 daily reports exist for the requested week (incomplete weeks trigger clarification)

### 2. Load and Validate Data
- Retrieve all daily reports for the target week from `daily-report-data.json`
- Load project metadata from `project-config.json`, schedule data from `schedule.json`, specs from `specs-quality.json`
- Verify that required sections are present in daily reports (crew, weather, inspections, materials, safety)

### 3. Aggregate Daily Data

#### Crew & Headcount
- Extract total headcount from each day
- Calculate average headcount for the week
- Identify peak headcount day
- List all subcontractors that appeared during the week
- For each sub: count days on site, calculate average crew size when present, list primary work

#### Weather
- Consolidate weather conditions across all days
- Identify days with weather delays or impacts
- Sum total delay hours attributed to weather
- Note any weather-related material delivery delays

#### Inspections & Testing
- Extract all inspections from daily reports
- Create pass/fail/conditional summary
- Group by inspection type (building, structural, MEP, etc.)
- Note any items requiring follow-up

#### Materials & Deliveries
- List all material deliveries noted during the week
- Flag any items that arrived damaged, late, or incorrect
- Consolidate delivery log into narrative form

#### Schedule Progress
- Extract percent complete from first daily report of the week
- Extract percent complete from last daily report of the week
- Calculate week-over-week progress
- Identify milestone status changes
- Cross-reference with schedule milestones from config

#### Open Items & Issues
- Gather all open items and issues from all daily reports
- Classify as: new (opened during week), carried forward (pre-existing), or resolved
- Note due dates, responsible parties, and status
- Highlight any critical or overdue items

#### Safety
- Extract all safety notes, incidents, near-misses
- Compile list of observations and toolbox talk topics
- Flag any incidents requiring follow-up or corrective action

### 4. Draft Executive Summary
- Write 2–3 sentences capturing the week's narrative arc
- Lead with the most significant accomplishment or milestone
- Acknowledge any major challenges and how they're being addressed
- Maintain tone: confident, forward-looking, factual

**Example language:**
- "The week saw substantial progress in [major area], with [specific milestone] achieved on schedule."
- "Despite [challenge], the team [mitigation], keeping overall progress on track."
- "The focus for the coming week is [upcoming priority] as we move toward [next milestone]."

### 5. Draft Section Narratives
Each section should be written as a narrative paragraph (not bullet points), organized logically:

- **Schedule Status** — Reference current phase, percent complete with notation of week-over-week change (e.g., "up 5% from last week"). List upcoming milestones with status. Address any delays with clear mitigation.
- **Work Accomplished** — Organize by trade or building area (whichever is more relevant). Summarize key activities, not every single task. Reference crew size and key subcontractors involved.
- **Crew Summary** — Present as table, then summary narrative noting staffing trends and any planned changes.
- **Upcoming Work** — Brief forward-looking preview (3–5 sentences) based on schedule and current trajectory. Highlight dependencies.
- **Weather Summary** — Conditions overview (temperature range, precipitation, etc.), any delays, and impact on schedule.
- **Inspections & Testing** — Narrative summary supported by table of results.
- **Materials & Deliveries** — Highlight significant arrivals and any issues; reference schedule of expected deliveries for coming week.
- **Active Issues & Open Items** — Present as table with item, date opened, status, and expected resolution.
- **Safety** — Narrative summary of the week's safety posture. Include incidents (if any) with action taken. Note observations and topics. End on a forward-looking note ("Continue focus on…").

All narratives should use:
- **Tense:** Past tense for accomplished work, future tense for upcoming work
- **Voice:** Third person (e.g., "The team completed…" not "We completed…")
- **Tone:** Professional but not stiff. Confident, factual, never defensive or alarming.

### 6. Select Representative Photos
- Retrieve up to 5 photos from the week's daily reports
- Prioritize:
  1. Major work areas showing progress
  2. Recent milestones or completed phases
  3. Different building areas or trades (variety)
  4. Images that communicate progress to owner (before/after, structural elements, finishes, etc.)
- Write clear, concise captions (1 sentence, present tense) describing what is shown and its significance
- Avoid photos that are blurry, poorly lit, or lack clear work context

### 7. QA Check
Validate the narrative against aggregated data:
- Do percentages and counts match the underlying data?
- Are all major accomplishments mentioned?
- Are all critical issues or delays addressed?
- Is the tone professional and appropriate for owner communication?
- Do sections flow logically and support one another?
- Are there any contradictions or gaps?
- Are all table data points accurate?

### 8. Generate .docx (with optional PDF)
- Use the weekly-template.md specification to structure the .docx
- Generate using `docx` npm library (docx-js) following docx skill guidelines
- Apply visual identity (colors: Navy #1B2A4A, Blue #2E5EAA, Light Blue #EDF2F9)
- Ensure proper pagination and section breaks
- Verify all tables render correctly with proper alignment and formatting
- Check photo placement and captions
- Generate document footer with proper spacing for signature block
- After generating .docx, ask: "Also export as PDF?" If yes, convert via LibreOffice headless

### 9. Save Output
- Name file: `{PROJECT_CODE}_Weekly_Report_{week_ending_date}.docx`
  - Example: `MOSC_Weekly_Report_2026-02-16.docx`
- If PDF exported: `{PROJECT_CODE}_Weekly_Report_{week_ending_date}.pdf`
- Save to output directory specified in `project-config.json` `folder_mapping.owner_reports` (typically `owner_reports` folder)
- Confirm successful save with file path and file size

### 10. Present to User
- Display report summary (which week, file name, location)
- Remind user of distribution list from config
- Provide next report date (following Friday)
- Offer option to open report, adjust and regenerate, or send immediately

## Tone Guidelines

**Professional & Confident:**
- Speak with authority. You are reporting factual project progress, not asking for approval.
- Avoid hedging language: "appears," "seems," "might." Use definitive statements.

**Factual & Data-Driven:**
- Every claim should be supported by aggregated daily data.
- Use specific numbers (headcount, percentages, delay hours, inspection results).
- Be precise: "3 days of weather delays" not "some weather issues."

**Progress-Focused:**
- Lead with accomplishments and milestone achievement.
- Frame challenges as problems with clear solutions.
- Emphasize forward momentum.

**Owner-Level Language:**
- Assume the reader is a busy executive; be concise and impactful.
- Use building trades language naturally, but avoid jargon when simpler terms work.
- Organize information in order of importance to the owner (schedule, budget implications, risk mitigation).

**Never Defensive, Never Alarming:**
- Do not make excuses for delays; explain mitigation.
- Do not overstate risks; present issues with planned responses.
- Maintain confidence in the team's ability to execute.

**Examples of appropriate language:**
- "Weather delays during Tuesday and Wednesday totaling 8 hours were mitigated by accelerated interior work."
- "The structural inspection on Friday identified one rebar spacing item requiring correction before concrete pour. This has been scheduled for Monday morning, with concrete still planned for Wednesday."
- "The team is positioned to complete [milestone] on schedule, pending timely delivery of [material] currently in transit."

## Output

### File Naming Convention
`{PROJECT_CODE}_Weekly_Report_{week_ending_date}.docx`
Optional PDF: `{PROJECT_CODE}_Weekly_Report_{week_ending_date}.pdf`

Example: `MOSC_Weekly_Report_2026-02-16.docx`

### Output Location
Directory specified in `project-config.json` under `folder_mapping.weekly_reports` (typically a folder named `owner_reports` at the project root or in reports directory).

### Content Verification
- .docx is readable and all sections are present
- All tables render with proper formatting
- Photos display clearly with captions
- Footer contains signature block and distribution list
- No orphaned text or formatting errors
- File size is reasonable (typically 2–5 MB with photos)

## Cross-References

- **project-data skill** — Used to load and validate project metadata from the multi-file data store (project-config.json, schedule.json, etc.)
- **daily-report-format skill** — Referenced for visual identity (colors, typography, table styles) to ensure weekly report is cohesive with daily reports
- **report-qa skill** — Called to validate narrative accuracy against aggregated data before .docx generation

