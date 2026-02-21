---
description: Track delays with classification and TIA
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [log/status/report] [details]
---

# Construction Delay Management Command

## Overview

Track construction delays from initiation through documentation and claims preparation. This command enables construction superintendents to:
- **Log** new delay events with classification, impacts, and supporting documentation
- **Status** review all active delays, cumulative impact tally, and contract extension calculations
- **Report** generate professional delay impact reports (.docx) suitable for contract extension requests or delay claims

Auto-populates project data, manages delay numbering, tracks float absorption vs. critical path impact, and integrates with morning briefs, daily reports, and look-ahead schedules.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/delay-tracker/SKILL.md` — Core delay lifecycle management, classification taxonomy, critical path analysis, contract extension calculation
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration, folder structure, schedule baseline, weather thresholds
- `${CLAUDE_PLUGIN_ROOT}/skills/daily-report-format/SKILL.md` — Link delay events to contemporaneous daily reports for supporting documentation

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration
Load `project-config.json` for version_history and folder_mapping.
Load `delay-log.json` for existing delay records.
Load `schedule.json` for baseline schedule, critical path definition, and float analysis.
Load `specs-quality.json` for weather_thresholds and contract requirements.

If the config file is not found, inform the user:
> "Project configuration not found. Please run `/set-project` first to initialize your project structure."

### Step 2: Parse Arguments for Sub-Action
Examine `$ARGUMENTS` to determine which operation:
- **"log"** — Create a new delay event record
- **"status"** — Review all active delays and cumulative impact summary
- **"report"** — Generate and export delay impact report document

If no sub-action provided, show usage:
```
Usage: /delay [log/status/report] [details]
Examples:
  /delay log
  /delay status
  /delay report
```

### Step 3: Process "log" Sub-Action
Collect delay details conversationally:
1. **Delay Type**: Select from taxonomy (weather, owner-directed, design issue, material, sub performance, force majeure, permit/regulatory, differing site conditions)
2. **Description**: Narrative of the delay event and conditions
3. **Date Range Affected**: Start date and end date of delay impact
4. **Activities Impacted**: Which schedule activities were delayed (reference schedule.json activities)
5. **Calendar Days Impact**: Number of calendar days the delay consumed
6. **Weather-Specific Data** (if applicable): Compare actual weather to contract thresholds from specs-quality.json
7. **Responsible Party**: Owner, architect, subcontractor, force majeure, or internal
8. **Excusable/Compensable Classification**: Auto-suggest based on type (see delay-tracker SKILL for matrix)
9. **Critical Path Analysis**: Does delay extend project completion or consumed float?
10. **Concurrent Delays**: Are there other delays occurring at same time?
11. **Supporting Documentation**: Link to daily reports (daily-report-data.json) documenting conditions
12. **RFI/Change Order References**: Link to any RFIs or COs that caused the delay
13. **Photos**: Attachment or reference to photo documentation

**Auto-assign Delay Number**: Query `delay-log.json` for highest DELAY-NNN, increment by 1. Lock immediately.

**Store in `delay-log.json`**:
```json
{
  "id": "DELAY-001",
  "type": "[weather|owner-directed|design|material|sub_performance|force_majeure|permit|differing_site_conditions]",
  "description": "[user input]",
  "date_start": "[ISO 8601]",
  "date_end": "[ISO 8601]",
  "calendar_days": "[number]",
  "activities_impacted": ["[schedule activity ID/name]"],
  "responsible_party": "[owner|architect|sub_name|force_majeure|internal]",
  "excusable": "[true|false]",
  "compensable": "[true|false]",
  "critical_path_impact": "[extended_completion|absorbed_float|partial]",
  "float_consumed_days": "[number]",
  "extension_days_earned": "[number calculated as: calendar_days - float_consumed]",
  "concurrent_delays": ["[DELAY-NNN]"],
  "linked_daily_reports": ["[date YYYY-MM-DD]"],
  "linked_rfis": ["[RFI-NNN]"],
  "linked_change_orders": ["[CO-NNN]"],
  "weather_data": {
    "actual_conditions": "[description of actual weather]",
    "contract_threshold_exceeded": "[true|false]",
    "threshold_type": "[temperature_min|temperature_max|precipitation|wind_speed]",
    "contract_requirement": "[value from specs-quality.json]",
    "noaa_baseline_comparison": "[exceeds NOAA 30-year average by X days]"
  },
  "date_logged": "[ISO 8601]",
  "notes": "[additional context]",
  "documentation_status": "[complete|partial|insufficient]"
}
```

### Step 4: Process "status" Sub-Action
1. Load `delay-log.json` and display summary:
   - Active delays (by type, sorted by date_start)
   - Status badges: [Closed] [Pending] [Documented] [Documented + Supporting Photos]
2. Calculate and display:
   - **Total Calendar Days Impacted**: Sum of all calendar_days across open delays
   - **Total Float Consumed**: Sum of float_consumed_days
   - **Contract Extension Earned**: Sum of extension_days_earned (excusable delays only)
   - **Compensable Exposure**: Sum of all delays where compensable=true
   - **Critical Path Delays**: Count and list delays that extended completion
3. Show delay taxonomy breakdown:
   - Count by type (weather: 3, owner-directed: 1, material: 2, etc.)
   - Count by responsible party
4. **Documentation Completeness**:
   - Count delays with complete supporting documentation
   - Alert on delays with insufficient documentation (< 3 daily reports linked)
   - Suggest daily report linking for gaps
5. **Contract Extension Summary**:
   - Days earned (excusable, non-compensable): ready for extension request
   - Days with claim potential (excusable, compensable): ready for claim documentation
6. Highlight any delays aging >7 days without supporting documentation

### Step 5: Process "report" Sub-Action
Generate a professional delay impact report (.docx format):
1. Extract all delays from `delay-log.json` sorted by date_start
2. Create executive summary section:
   - Total delays logged
   - Total calendar days impacted
   - Total float consumed
   - **Contract Extension Justification**: Total excusable delay days minus float consumed = extension days earned
   - Cumulative impact on project completion date
3. Detailed delay table with columns:
   - Delay ID
   - Type
   - Date Range
   - Calendar Days
   - Responsible Party
   - Excusable / Compensable
   - Critical Path Impact
   - Extension Days Earned
   - Documentation Status
4. **Weather Delay Section** (if applicable):
   - List all weather delays with actual conditions vs. contract thresholds
   - NOAA 30-year average comparison for project location
   - Days exceeding contract thresholds
5. **Delay Impact Analysis**:
   - Delay type distribution (chart: count and days by type)
   - Responsible party breakdown
   - Month-by-month timeline showing when delays occurred
6. **Critical Path Analysis Section**:
   - Activities affected by delays that extended completion
   - Activities with float absorption
   - Concurrent delay identification and quantification
7. **Documentation & Supporting Evidence**:
   - List linked daily reports (by date)
   - List linked RFIs and change orders
   - Photo references (if applicable)
   - Note: Full daily report text/photos not included in report, but references provided for archival
8. **Contract Extension Claim Template**:
   - Recommended extension days (excusable delays - float consumed)
   - Format suitable for submission to owner/architect
   - Signature block for superintendent and project manager
9. **Delay Claim Documentation Template** (if compensable delays present):
   - Recommended structure for documenting causation and damages
   - Reference to delay events and responsible parties
10. Save to `{{folder_mapping.reports}}/Delay_Impact_Report_[YYYYMMDD].docx`
11. Confirm file location to user

### Step 6: Save & Log
1. Write updated `delay-log.json`
2. Update `project-config.json` version_history with timestamp and action:
   ```
   [TIMESTAMP] | delay | [sub-action] | [DELAY-NNN or "report generated"]
   ```
3. If log sub-action, auto-populate related morning brief alert:
   - Surface in /morning-brief if delay extends critical path
   - Show cumulative contract extension earned
4. If status sub-action, confirm summary data to user with completeness assessment
5. If report sub-action, confirm generation with filename and next steps for claims/extension submission
6. If project data changed significantly, regenerate `CLAUDE.md` to reflect the latest project state

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces active delays, critical path impact, and cumulative extension earned
- **Daily Report** (`/daily-report`): Auto-suggests delay logging when weather or other conditions impact work; provides template for linking to existing delay events
- **Weekly Report** (`/weekly-report`): Includes delay summary section with type breakdown, trending, and updated contract extension calculation
- **Look-Ahead** (`/look-ahead`): Factors active delays into projected dates; highlights activities at risk of further delay
- **Schedule** (`schedule.json`): Cross-references delay impacts to schedule activities; critical path analysis uses baseline schedule

## Notes
- All delay numbers are immutable once assigned
- Calendar days capture total duration of delay impact; float consumed is separately calculated
- Excusable delays that consume project float = basis for time extension requests
- Compensable delays = basis for cost claims (if applicable per contract)
- Weather delays require NOAA 30-year average comparison to demonstrate contract threshold exceedance
- Delay impact analysis requires contemporaneous daily report documentation (not retroactive)
- Critical path determination based on schedule.json baseline and actual progress tracking
