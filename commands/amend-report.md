---
description: Amend a previously generated daily report
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [report number or date]
---

Amend a previously generated daily report. Applies corrections or additions to the report data, regenerates the .docx, and runs QA on the changed sections.

Read the daily-report-format skill at `${CLAUDE_PLUGIN_ROOT}/skills/daily-report-format/SKILL.md` and all files in `${CLAUDE_PLUGIN_ROOT}/skills/daily-report-format/references/` before proceeding. Also read the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` and the report-qa skill at `${CLAUDE_PLUGIN_ROOT}/skills/report-qa/SKILL.md`. If available, also read the `docx` Cowork skill for .docx generation best practices.

## Step 1: Load Project Config and Report History

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping, report_tracking)
- `daily-report-data.json` (structured report history)

If no config exists, tell the user: "No project set up. Run `/set-project` first."

## Step 2: Identify the Report to Amend

Parse `$ARGUMENTS` to find the target report:

- **By report number** (e.g., `/amend-report MOSC-003` or `/amend-report 3`): Look up in `daily-report-data.json` by report_number
- **By date** (e.g., `/amend-report 2/15` or `/amend-report 2026-02-15`): Look up by report_date
- **No argument**: Show the last 5 reports and ask which one to amend

If the report isn't found, tell the user: "No report found for [input]. Check the report number or date."

## Step 3: Load the Original Report Data

Load the full structured report entry from `daily-report-data.json`. Display a summary of what's in the current report:

```
Report MOSC-003 — February 15, 2026

Weather: Partly cloudy, 45-62°F, no impact
Crew: 4 subs, 18 total workers
Materials: 1 delivery (rebar from Harris)
Equipment: 2 pieces active, 0 down
Schedule: Foundation phase, 35% complete
Visitors: 1 inspection (footing — passed)
Photos: 3 included
Notes: None
```

Ask: "What needs to change?"

## Step 4: Collect Amendments

Accept corrections or additions in natural language. The user might say:
- "Add Smith Electric — they had 2 guys doing conduit rough-in on the east wing"
- "Change the temperature high to 65°F"
- "Add a note about the RFI discussion with the architect"
- "Remove the rebar delivery — that was actually yesterday"

For each amendment:
1. Identify which report section is affected
2. Apply the change to the structured report data
3. Track what was changed (old value → new value) for the amendment log

## Step 5: Run QA on Changed Sections

Run the report-qa skill checks, but only on the sections that were modified:
- If crew was changed → re-validate sub names against directory
- If weather was changed → re-check weather vs. work thresholds
- If work activities were added → check for required inspections
- Present any new flags or notes

## Step 6: Regenerate the .docx

Regenerate the full .docx using the daily-report-format skill with the amended data. Apply the same template, formatting, and language standardization as the original.

Name the file: `{M_D_YY}_Daily_Report_{PROJECT_CODE}_AMENDED.docx`

Save to the same location as the original (`folder_mapping.daily_reports`).

If the user wants PDF export, generate that as well.

## Step 7: Update Report History

Update the entry in `daily-report-data.json`:
- Add an `amendments` array to the report entry:
```json
{
  "amendments": [
    {
      "date": "2026-02-19",
      "changes": [
        {
          "section": "crew",
          "action": "added",
          "detail": "Added Smith Electric (2 workers, conduit rough-in, east wing)"
        }
      ]
    }
  ]
}
```
- Update the report data with the amended values
- Keep the original report_number (do NOT assign a new number)

Log the amendment in `project-config.json` version_history:
```json
{
  "timestamp": "2026-02-19T15:00:00Z",
  "command": "amend-report",
  "sub_action": "MOSC-003",
  "details": "Amended crew section — added Smith Electric"
}
```

## Step 8: Present to User

"Report MOSC-003 has been amended. Changes: [summary]. Amended .docx saved to [path]."

If QA flags were raised on the amendments, note them: "QA note: [brief flag description]."
