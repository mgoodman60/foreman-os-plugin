---
description: Schedule and track inspections, permits
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch
argument-hint: [schedule/log/status/permits] [details]
---

# Inspections & Permits Command

Manage construction inspections and permits throughout the project lifecycle. Schedule inspections, log results, track re-inspections, manage permits, and view status reports.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/inspection-tracker/SKILL.md` — Inspection scheduling, results logging, re-inspection tracking, and permit management

## Execution Flow

### 1. Load Project Configuration
```bash
# Check for project config
if [ ! -f "project-config.json" ]; then
  echo "No project configuration found. Run /set-project first."
  exit 1
fi
```

### 2. Parse Arguments & Route to Sub-Action

Extract sub-action from $ARGUMENTS: `schedule`, `log`, `status`, or `permits`

## Sub-Action: Schedule Inspection

**Trigger:** `/inspections schedule [type] [date] [inspector]`

**Collection Steps:**
1. **Inspection Type** — Prompt if not provided. Standard types:
   - Foundation, concrete pre-placement, rebar, formwork
   - Structural steel, fireproofing, anchor bolt (PEMB), high-strength bolt (PEMB), moment connection (PEMB)
   - Underground utilities, electrical, plumbing, mechanical
   - Fire protection, insulation, ADA compliance, life safety (healthcare)
   - State health dept inspection (healthcare), infection control, final

2. **Date & Time** — Parse ISO format or natural language (e.g., "next Monday 9 AM")

3. **Inspector Name** — Collect inspector, verify against approved inspector list if available

4. **Location** — Room/area/grid reference for linkage to project layout

**Auto-Linking Intelligence:**
- Query project intelligence for spec hold points matching inspection type
- Auto-link to related schedule activities (e.g., "Concrete Pour Day" → concrete pre-placement inspection)
- Extract spec section reference if available
- Generate unique ID: `INSP-{sequential 3-digit number}`

**Output:** Create entry in inspections registry with:
```json
{
  "id": "INSP-001",
  "type": "Concrete Pre-placement",
  "date_scheduled": "2025-03-15T09:00:00Z",
  "inspector": "John Smith",
  "location": "Building A, Level 2",
  "linked_schedule_activity": "SAC-042",
  "linked_hold_point": "HP-08",
  "linked_spec_section": "3.2.1",
  "status": "scheduled",
  "notes": ""
}
```

## Sub-Action: Log Inspection Result

**Trigger:** `/inspections log [INSP-NNN or type] [result] [notes]`

**Collection Steps:**
1. **Select Inspection** — Show upcoming inspections or accept INSP number directly
2. **Result** — One of: `pass`, `fail`, `conditional`, `cancelled`
3. **Inspector & Date** — Confirm or update inspector name, record completion date
4. **Notes & Evidence** — Detailed notes, photo references, deficiencies if applicable

**Conditional Logic:**
- **Pass:** Mark complete, record date, close out
- **Fail:** Flag `re_inspection_required: true`, collect deficiencies array, suggest re-inspection date (typically 48 hours)
- **Conditional:** Record conditions to satisfy, suggest follow-up verification date, generate re-inspection with `re_inspection_id` reference
- **Cancelled:** Record cancellation reason, suggest rescheduling if needed

**Output:** Update inspection entry:
```json
{
  "id": "INSP-001",
  "date_completed": "2025-03-15T10:30:00Z",
  "result": "pass",
  "notes": "Concrete strength verified via test cylinders.",
  "deficiencies": [],
  "re_inspection_required": false
}
```

If fail, auto-create re-inspection:
```json
{
  "id": "INSP-002",
  "type": "Concrete Pre-placement (Re-inspection)",
  "date_scheduled": "2025-03-17",
  "related_to": "INSP-001",
  "status": "scheduled"
}
```

## Sub-Action: Status Report

**Trigger:** `/inspections status`

**Display Three Sections:**

**Upcoming (Next 7 Days):**
- Table with: INSP ID, Type, Date, Inspector, Location, Spec Link
- Color: Gray (scheduled)

**Overdue Inspections:**
- Any scheduled inspection past date with no logged result
- Color: Red (attention required)

**Recent Results (Last 14 Days):**
- Completed inspections with results
- Color-coded: Green (pass), Red (fail), Yellow (conditional)

**Summary Metrics:**
- Total scheduled this month
- Pass rate (%)
- Failed requiring re-inspection
- Pending re-inspections

## Sub-Action: Permits Management

**Trigger:** `/inspections permits [add/status/expiring]`

**Add Permit:**
1. **Permit Type** — Building, electrical, plumbing, mechanical, trade-specific, health department, accessibility (ADA)
2. **Number & Details** — Permit number, jurisdiction, date applied, date issued (if available)
3. **Expiration & Conditions** — Expiration date, special conditions, required inspections

**Permit Entry Structure:**
```json
{
  "id": "PERMIT-001",
  "type": "Building Permit",
  "number": "BP-2025-4521",
  "jurisdiction": "City Building Department",
  "date_applied": "2025-02-01",
  "date_issued": "2025-02-20",
  "expiration": "2026-02-20",
  "status": "active",
  "conditions": ["Final inspection before occupancy"],
  "inspections_required": ["INSP-001", "INSP-003"]
}
```

**Status Report:**
- Show all permits with expiration tracking
- Flag expiring within 30 days (Yellow)
- Flag expired (Red)

## Integration & Persistence

**Save Configuration:**
- Update `inspection-log.json` (inspection_log and permit_log arrays)
- Update `project-config.json` version_history:
  ```
  [TIMESTAMP] | inspections | [sub-action] | [INSP-NNN or PERMIT-NNN or "status reviewed"]
  ```
- If project data changed significantly, regenerate `CLAUDE.md` to reflect the latest project state

**Integration Points:**
- `/morning-brief` displays upcoming & overdue inspections
- `/look-ahead` includes scheduled inspections by date
- `/daily-report` references today's completed & scheduled inspections
- Inspection status exportable to `folder_mapping.ai_output` for stakeholder reports

## Error Handling

- Validate INSP ID format; suggest correction if invalid
- Confirm re-inspection is not duplicate before creating
- Warn if inspection scheduled outside working hours
- Alert if inspector not in approved list; log as "External Inspector"
