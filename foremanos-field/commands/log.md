---
description: Log field observations for daily report
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [what happened on site | clear]
---

Accept conversational field input from the superintendent and log it to a running daily intake file. This is the primary way field data enters the system throughout the day.

Read the intake-chatbot skill at `${CLAUDE_PLUGIN_ROOT}/skills/intake-chatbot/SKILL.md` and the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding. If the user includes or references site photos, also read `${CLAUDE_PLUGIN_ROOT}/skills/photo-documentation/SKILL.md` for photo classification and documentation standards.

## Step 1: Load Context

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `directory.json` (subcontractors array)
- `schedule.json` (grid lines, building area context, milestones)
- `specs-quality.json` (spec_sections, weather_thresholds)
- `plans-spatial.json` (grid_lines, building_areas, floor_levels, locations)

- Check `project-config.json` for `claims_mode` flag. If `true`, apply claims-mode prompting rules from the intake-chatbot skill after each classification.

This context powers auto-classification and enrichment. If no config exists, still accept the log entry — just skip the enrichment step.

## Step 2: Check for Clear Action

If `$ARGUMENTS` is "clear", clear today's intake log instead of logging a new entry:

1. Read `daily-report-intake.json`. If it doesn't exist or has no entries for today, tell the user: "No entries to clear — today's log is already empty." Exit.
2. Show the user what will be cleared: number of entries, time range, brief summary of sections covered.
3. Ask: "Clear [X] entries from today's log? They'll be archived in case you need them."
4. If confirmed, archive the current entries to `daily-report-intake-archive-{YYYY-MM-DD}-{HHmmss}.json` in `folder_mapping.ai_output` (or working directory root).
5. Reset `daily-report-intake.json` to `{ "date": "[today]", "entries": [] }`.
6. Confirm: "Log cleared. [X] entries archived to [filename]. Start logging with `/log`."
7. Log in `project-config.json` version_history: `[TIMESTAMP] | log | clear | Cleared X entries, archived to [filename]`
8. Exit.

## Step 3: Accept Input

The user will provide field observations as natural language. They might say anything from a quick note to a detailed dump of what happened. Examples:

- "Walker had 6 guys doing backfill on the east side"
- "Concrete truck showed up at 9, poured the footings at grid C"
- "Rain started around 2pm, had to shut down exterior work"
- "Got a delivery of rebar from Harris, 12 tons, looked good"
- "Inspector came by at 10, passed the footing inspection"

If the user provided input as an argument ($ARGUMENTS), process it directly. If no arguments, ask: "What's happening on site?"

## Step 4: Classify and Structure

Using the intake-chatbot skill's classification rules, identify which daily report sections the input belongs to:

- Weather / site conditions
- Crew / work performed
- Materials / deliveries
- Equipment
- Schedule updates
- **Delays / Impacts** — work prevention, stoppages, holds, and their causes (feeds delay-tracker)
- Visitors / inspections
- Photos (if images are uploaded)
- General notes

A single user message may contain information for multiple sections. Parse and classify each piece separately.

## Step 5: Enrich with Project Intelligence

If project intelligence is loaded:
- Match sub names to the directory from `directory.json` (subcontractors array, fuzzy match casual references)
- Resolve locations to grid_lines and building_areas from `plans-spatial.json`
- Add spec references for materials mentioned from `specs-quality.json` (spec_sections)
- Note any weather threshold implications from `specs-quality.json` (weather_thresholds)
- Cross-reference schedule milestones from `schedule.json`

## Step 6: Save to Intake Log

Save the classified and enriched entry to `daily-report-intake.json` in the user's working directory. The intake log is a running list of timestamped entries for the current day:

```json
{
  "date": "2026-02-12",
  "entries": [
    {
      "timestamp": "2026-02-12T09:15:00Z",
      "raw_input": "Walker had 6 guys doing backfill on the east side",
      "sections": [
        {
          "section": "crew",
          "data": {
            "sub": "Walker Construction",
            "headcount": 6,
            "work": "Backfill operations at east wing",
            "location": "East Wing, Grid Lines E-G"
          }
        }
      ]
    }
  ]
}
```

If the intake file already exists for today, append to the entries array. If it's a new day, start fresh (but preserve yesterday's file as `daily-report-intake-{YYYY-MM-DD}.json` if it wasn't consumed by /daily-report yet).

## Step 7: Confirm

Give a brief confirmation that shows how the input was classified:

"Got it — logged Walker Construction (6 workers) doing backfill at the east wing. Anything else?"

Keep confirmations short and conversational. The user is in the field and doesn't want to read a novel.

## Step 8: Save & Log
1. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | log | intake | [count of entries added today]
   ```
