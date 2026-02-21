---
description: Manage punch list items — add, update status, or generate punch list reports
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [add/status/generate] [area or trade]
---

# Punch List Management

## Overview
This command manages punch list items throughout the project lifecycle. Track deficiencies from identification through completion, manage back-charges, and generate professional closeout reports. Integrates with project dashboard for real-time completion tracking.

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/punch-list/SKILL.md` — Punch item schema, status workflow, back-charge tracking
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

## Quick Start

```
/punch-list add Room 107
→ Collect new punch items for Room 107

/punch-list status drywall
→ Show all drywall punch items, filterable by status/priority

/punch-list generate area
→ Create .docx report grouped by location

/punch-list generate trade
→ Create .docx report grouped by responsible sub
```

## Workflow

### Step 1: Load Project Configuration
Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `directory.json` (subcontractors — for resolving responsible subs)
- `plans-spatial.json` (building_areas, floor_levels, grid_lines — for location resolution)
- If missing, prompt user to run `/set-project` first

### Step 2: Load Punch List Skill
- Read `${CLAUDE_PLUGIN_ROOT}/skills/punch-list/SKILL.md` to confirm field definitions and business logic
- This ensures consistency with punch item schema and status workflow

### Step 3: Parse Arguments
Detect sub-action:
- **add**: Create new punch items
- **status**: View and update existing items
- **generate**: Create professional .docx report

Optional: Extract area/trade filter from arguments (e.g., `/punch-list status drywall`)

### Step 4: ADD Action — Collect New Items
If user provides multi-item summary ("I found 5 items in Room 107"), parse and create each:

For each item, collect:
- **Description**: What is the deficiency? (e.g., "Drywall mud pops in corner")
- **Location**: Resolve against project intelligence
  - Room number → room_number (e.g., "Room 107")
  - Area reference (e.g., "East Wing, 3rd Floor") → building_area + floor_level
  - Grid reference (e.g., "Grid C3") → grid_reference
- **Trade**: (e.g., "Drywall", "Electrical", "Painting", "Plumbing")
- **Responsible Sub**: Resolve against `directory.json` (subcontractors array)
- **Priority**: A (safety/code), B (functional), C (cosmetic)
- **Photos**: Accept file paths; store reference in photos[]
- **Identified By**: Current user name
- **Date Identified**: Auto-populate today's date
- **Status**: Auto-set "open"

Auto-generate unique ID: **PUNCH-{NNN}** (increment from highest existing ID in punch list)

Save to punch list data store. Log action in version_history.

#### Bulk Add Example
User: *"I found 5 items in Room 107: mud pop in corner, paint scuff on south wall, missing outlet cover, cracked tile, and grout missing in shower."*

→ Create 5 items, all in Room 107, prompt for trade and sub for each, auto-assign PUNCH-001 through PUNCH-005

### Step 5: STATUS Action — View & Update Existing Items
1. Load punch list data
2. If area/trade provided in arguments, filter automatically
3. Display current items in table format:
   ```
   ID      | Location    | Description        | Trade    | Sub         | Priority | Status       | Days Open
   --------|-------------|-------------------|----------|-------------|----------|------------|----------
   PUNCH-001| Room 107   | Drywall mud pops  | Drywall  | ABC Drywall | A        | in_progress | 3 days
   PUNCH-002| Room 107   | Paint scuff       | Painting | Ready Paint | C        | open       | 2 days
   ...
   ```

4. Allow interactive updates per item:
   - Mark as **completed** (status → "completed", date_completed → today, completed_by → user)
   - Add **notes** (e.g., "Fixed, awaiting inspection")
   - Change **priority** (A/B/C)
   - Flag for **back-charge** (status → "back_charge", prompt for amount and reason)
   - Mark as **disputed** (status → "disputed", prompt for reason)

5. Support bulk updates:
   - *"All drywall items in Room 107 are done"* → Mark matching items completed
   - *"Flag all priority A items as back-charge with $500 per item"* → Bulk back-charge

6. Save punch list. Log changes in version_history.

### Step 6: GENERATE Action — Create Professional .docx Report
1. Load punch list data and apply filters (all items unless area/trade specified)
2. Generate professional .docx with:
   - **Header**: Project name, date generated, report type (by area or trade)
   - **Completion Statistics**:
     - Overall % complete
     - % complete by area (if grouped by area)
     - % complete by trade (if grouped by trade)
     - Breakdown by priority: % A items done, % B items done, % C items done
   - **Punch Items** grouped as requested:
     - **By Area**: Section per location with all trades
     - **By Trade**: Section per responsible sub with all locations
   - **For Each Item**:
     - ID, location, description, trade, responsible sub, status, priority
     - Date identified, date completed (if done)
     - Photos (embedded if available, or reference paths)
     - Notes and back-charge info (if applicable)
   - **Back-Charge Summary**: Total back-charge amount, items flagged, responsible subs
   - **Footer**: Project info, generated date/time, superintendent name

3. Save .docx to `{folder_mapping.ai_output}/Punch-List-{ProjectName}-{Date}.docx`
4. Log report generation in version_history
5. Notify user of file location and offer to open/attach to daily report

### Step 7: Save & Log
- Write updated punch list to persistent storage (YAML/JSON in config folder)
- Update `project-config.json` version_history:
  ```
  [TIMESTAMP] | punch-list | [sub-action] | [PUNCH-NNN or count of items affected]
  ```
- Trigger dashboard update to reflect punch completion charts
- If project data changed significantly, regenerate `CLAUDE.md` to reflect the latest project state

## Integration Points
- **Project Dashboard** (`/project-dashboard`): Shows punch completion % by area and trade
- **Daily Report** (`/daily-report`): Can reference punch walk findings and new items identified
- **Closeout Workflow**: Pre-final vs. final punch list distinction
- **Healthcare/Senior Care**: Flag ADA items, infection control concerns, nurse call system items for priority tracking

## Tips
- Use bulk operations for efficiency: "5 items in Room 107" or "All drywall done"
- Review completion statistics before final inspection
- Photos document condition; include references in .docx reports
- Back-charge tracking prevents sub disputes at closeout
- Disputed items halt closeout; resolve before final sign-off
