---
description: Generate construction schedules from plans
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [door|hardware|fixture|finish|plumbing|equipment|room|all]
---

Generate professional construction schedules from project intelligence. Pulls extracted data from plans and specs to produce formatted schedules by trade or type.

Read the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding. Also read the quantitative-intelligence skill at `${CLAUDE_PLUGIN_ROOT}/skills/quantitative-intelligence/SKILL.md` for measurement and calculation support.

**Output Skills**: See the `xlsx` Cowork skill for spreadsheet formatting and the `docx` Cowork skill for .docx output, if available.

## Step 1: Load Project Intelligence

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `plans-spatial.json` (room_schedule, door_schedule, hardware_schedule, fixture_schedule, finish_schedule, plumbing_fixture_schedule, equipment_schedule, quantities, sheet_cross_references)
- `specs-quality.json` (spec_sections — for material specs and standards)
- `schedule.json` (milestones, activity dates — for installation timing)
- `directory.json` (subcontractors — for responsible trade assignments)

If no config exists, tell the user: "No project set up. Run `/set-project` first."

If `plans-spatial.json` doesn't exist or has no schedule data, tell the user: "No plan data extracted yet. Run `/process-docs` on your plan sheets first — I need the plan data to build schedules."

## Step 2: Determine Schedule Type

Parse `$ARGUMENTS` to identify the requested schedule type:

| Argument | Schedule Generated |
|---|---|
| `door` | Door schedule — door marks, sizes, types, hardware sets, fire ratings, frame types |
| `hardware` | Hardware schedule — hardware sets, hinges, locksets, closers, accessories by door |
| `fixture` | Fixture schedule — light fixtures, plumbing fixtures, or general fixtures by room |
| `finish` | Finish schedule — floor, wall, ceiling, base finishes by room |
| `plumbing` | Plumbing fixture schedule — fixture types, counts, rough-in specs by room |
| `equipment` | Equipment schedule — owner-furnished and contractor-furnished equipment by room/area |
| `room` | Room schedule — room numbers, names, areas, departments, occupancy |
| `all` | Generate all available schedule types |
| (none) | Show available types with data coverage and ask which to generate |

If no argument is provided, show what data is available:
```
Available schedules from extracted plan data:

  Door Schedule:      ✓ 47 doors extracted
  Hardware Schedule:  ✓ 12 hardware sets extracted
  Finish Schedule:    ✓ 34 rooms with finish data
  Fixture Schedule:   ✗ No fixture data — run /process-docs on electrical/lighting plans
  Plumbing Schedule:  ✓ 22 fixtures extracted
  Equipment Schedule: ✗ No equipment data — run /process-docs on equipment plans
  Room Schedule:      ✓ 34 rooms extracted

Which schedule would you like to generate?
```

## Step 3: Build the Schedule

For each requested schedule type, pull data from `plans-spatial.json` and enrich with spec references:

### Door Schedule
Columns: Door Mark, Room From, Room To, Door Size (W×H), Door Type, Frame Type, Fire Rating, Hardware Set, Glazing, Threshold, Weatherstrip, Notes
- Cross-reference hardware sets to hardware schedule
- Pull fire rating requirements from specs
- Note ADA-compliant doors

### Hardware Schedule
Columns: Hardware Set, Hinges (qty/type), Lockset, Closer, Stop, Kickplate, Seal, Accessories, Notes
- Pull manufacturer/model from approved submittals if available
- Note fire-rated hardware requirements

### Finish Schedule
Columns: Room Number, Room Name, Floor Finish, Base, North Wall, South Wall, East Wall, West Wall, Ceiling, Ceiling Height, Notes
- Resolve finish codes to material descriptions from specs
- Note moisture-resistant requirements for wet areas

### Fixture Schedule
Columns: Fixture Type/Mark, Manufacturer, Model, Lamp/Source, Voltage, Mounting, Rooms/Locations, Quantity, Notes
- Pull from electrical plans if available
- Cross-reference with spec sections

### Plumbing Fixture Schedule
Columns: Fixture Type, Manufacturer, Model, Connection Size, Room/Location, Quantity, Rough-In Specs, Notes
- Pull from plumbing plans
- Cross-reference with plumbing spec sections

### Equipment Schedule
Columns: Equipment Tag, Description, Manufacturer, Model, Utility Requirements, Room/Location, Furnished By (Owner/Contractor), Installed By, Notes
- Separate owner-furnished vs. contractor-furnished
- Note utility rough-in requirements

### Room Schedule
Columns: Room Number, Room Name, Department/Area, Floor Level, Net Area (SF), Occupancy, Finish Group, Notes
- Pull from architectural plans
- Cross-reference with finish schedule

## Step 4: Format and Generate Output

Generate the schedule as a formatted table. Offer output format options:

1. **Display in chat** — Show the formatted table directly (default for small schedules)
2. **Export as .xlsx** — Professional spreadsheet with column formatting, filters, and conditional formatting (if xlsx Cowork skill available)
3. **Export as .docx** — Formatted document with schedule tables (if docx Cowork skill available)

For exported files:
- Filename: `{Schedule_Type}_Schedule_{PROJECT_CODE}_{date}.{ext}`
- Save to `folder_mapping.ai_output`

## Step 5: Cross-Reference Validation

After building the schedule, run validation checks:

- **Completeness**: Flag rooms/doors/fixtures that appear in plans but have incomplete data (e.g., door with no hardware set assigned)
- **Spec compliance**: Check extracted materials against spec requirements (e.g., fire-rated door has fire-rated hardware)
- **Consistency**: Check for duplicate marks, missing room references, or orphaned entries
- **Quantity verification**: Compare schedule counts against plan quantities from `plans-spatial.json`

Present any issues:
```
Schedule Validation — 2 notes:
• Door D-107 has no hardware set assigned
• Room 203 appears in room schedule but has no finish data
```

## Step 6: Save and Log

Log the schedule generation in `project-config.json` version_history:
```json
{
  "timestamp": "2026-02-19T10:00:00Z",
  "command": "schedules",
  "sub_action": "door",
  "details": "Generated door schedule — 47 doors, 2 validation notes"
}
```

Present to user: "Here's your [type] schedule — [X] items. [Saved to path if exported]. [Validation notes if any]."
