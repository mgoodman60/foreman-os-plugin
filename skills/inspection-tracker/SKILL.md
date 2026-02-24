---
name: inspection-tracker
description: >
  Track inspections and permits through the construction lifecycle. Handles scheduling, result logging, re-inspection tracking, permit management, and status reporting. Healthcare-specific: state health dept inspections, life safety, ADA compliance. PEMB-specific: anchor bolt, high-strength bolt, moment connection special inspections. Integrates with morning brief and look-ahead. Triggers: "inspection", "schedule inspection", "log inspection", "inspection status", "permit", "failed inspection", "re-inspect", "upcoming inspections", "special inspection".
version: 1.0.0
---

# Inspection Tracker Skill

## Overview

The Inspection Tracker skill manages all construction inspections and permits throughout the project lifecycle. It provides real-time scheduling, result logging, re-inspection workflows, permit tracking, and comprehensive status reporting with integration into daily project management routines.

## Data Model

### Inspection Object

```json
{
  "id": "INSP-001",
  "type": "Concrete Pre-placement",
  "date_scheduled": "2025-03-15T09:00:00Z",
  "date_completed": null,
  "inspector": "John Smith",
  "result": null,
  "notes": "",
  "deficiencies": [],
  "re_inspection_required": false,
  "re_inspection_id": null,
  "linked_schedule_activity": "SAC-042",
  "linked_hold_point": "HP-08",
  "linked_spec_section": "03 30 00",
  "location": "Building A, Level 2",
  "photos": [],
  "status": "scheduled"
}
```

**Fields:**
- `id`: Unique identifier (INSP-001, INSP-002, etc.)
- `type`: Inspection classification (see Standard & Special Inspection Types)
- `date_scheduled`: ISO 8601 timestamp
- `date_completed`: Completion timestamp; null if not yet completed
- `inspector`: Name of inspector; external if not in approved list
- `result`: `pass`, `fail`, `conditional`, `cancelled`, or `null` if pending
- `notes`: Detailed observations, findings, or cancellation reason
- `deficiencies`: Array of identified issues requiring correction (if result = fail)
- `re_inspection_required`: Boolean; true if result = fail
- `re_inspection_id`: Reference to linked re-inspection (INSP-NNN)
- `linked_schedule_activity`: Schedule activity ID for smart linking (e.g., SAC-042)
- `linked_hold_point`: Spec hold point reference (e.g., HP-08)
- `linked_spec_section`: CSI specification section (e.g., 03 30 00)
- `location`: Physical location (room, area, grid reference)
- `photos`: Array of photo file paths or URLs for evidence
- `status`: `scheduled`, `completed`, `cancelled`, `hold` (awaiting prerequisites)

### Permit Object

```json
{
  "id": "PERMIT-001",
  "type": "Building Permit",
  "number": "BP-2025-4521",
  "date_applied": "2025-02-01",
  "date_issued": "2025-02-20",
  "expiration": "2026-02-20",
  "jurisdiction": "City Building Department",
  "status": "active",
  "conditions": ["Final inspection before occupancy", "Weekly inspection during excavation"],
  "inspections_required": ["INSP-001", "INSP-003"],
  "notes": ""
}
```

**Fields:**
- `id`: Unique identifier (PERMIT-001, PERMIT-002, etc.)
- `type`: Permit classification
- `number`: Official permit number
- `date_applied`: Application submission date
- `date_issued`: Date permit was issued; null if pending
- `expiration`: Expiration date for renewal tracking
- `jurisdiction`: Issuing authority
- `status`: `applied`, `issued`, `active`, `expired`, `renewed`
- `conditions`: Array of permit conditions or special requirements
- `inspections_required`: Array of inspection IDs required per permit
- `notes`: Additional remarks or tracking notes

## Standard Inspection Types

| ID | Type | Typical Spec Section | Hold Point | Notes |
|----|------|----------------------|------------|-------|
| 01 | Foundation | 03 11 00 | HP-01 | Before concrete placement |
| 02 | Concrete Pre-placement | 03 30 00 | HP-02 | Rebar, formwork, reinforcement |
| 03 | Rebar | 03 20 00 | HP-03 | Size, spacing, cover verification |
| 04 | Formwork | 03 10 00 | HP-04 | Structural adequacy, bracing |
| 05 | Structural Steel | 05 12 00 | HP-05 | Connections, bolt torque, straightness |
| 06 | Underground Utilities | 33 00 00 | HP-06 | Location, depth, protection |
| 07 | Electrical | 26 00 00 | HP-07 | Rough-in, panel installation, grounding |
| 08 | Plumbing | 22 00 00 | HP-08 | Rough-in, pressure test, slope |
| 09 | Mechanical | 23 00 00 | HP-09 | Equipment installation, ductwork |
| 10 | Fire Protection | 21 00 00 | HP-10 | Sprinkler lines, device placement |
| 11 | Insulation | 07 21 00 | HP-11 | R-value verification, continuity |
| 12 | Fireproofing | 07 81 00 | HP-12 | Applied thickness, coverage |
| 13 | Final | 01 77 00 | HP-13 | Walk-through, punch list generation |

## Healthcare-Specific Inspections

| Type | Trigger | Requirement | Notes |
|------|---------|-------------|-------|
| Life Safety | Continuous | Code compliance | ADA accessibility, egress paths, alarm systems |
| ADA Compliance | Pre-occupancy | Americans with Disabilities Act | Ramps, doors, restrooms, signage |
| State Health Dept | Final | Health Dept approval | Medical gas outlets, emergency systems, infection control |
| Infection Control | Pre-occupancy | Special protocols | HVAC testing, surface finishes, hand hygiene stations |

## PEMB-Specific Special Inspections

Pre-Engineered Metal Building (PEMB) requires specialized inspections per AWS D1.1 and manufacturer specs:

| Type | Tolerance | Requirement | Notes |
|------|-----------|-------------|-------|
| Anchor Bolt | ±1/8" | Location & elevation | Grid reference, hold-down torque verification |
| High-Strength Bolt | ±1/32" | Proper tension | Calibrated wrench, bolt grade certification |
| Moment Connection | ±1/4" | Beam-to-column welds | 100% visual + UT inspection required |

**Special Inspection IDs:** INSP-PEMB-001, INSP-PEMB-002, etc.

## Auto-Linking Intelligence

The inspection-tracker skill automatically links inspections to project intelligence:

### Schedule Activity Linking
Query project intelligence for schedule activities matching inspection date and type:
- "Concrete Pour Day" → auto-link to concrete pre-placement inspection
- "Steel Erection Week 3" → auto-link to structural steel inspection
- "Electrical Rough-In Phase" → auto-link to electrical inspection

### Hold Point Linking
Cross-reference spec hold points from project spec database:
- Inspection type matched to standard hold point (HP-02, HP-05, etc.)
- Override if project-specific hold point defined
- Display linked hold point ID to superintendent

### Specification Section Linking
Auto-populate CSI specification section reference:
- Foundation → 03 11 00
- Concrete → 03 30 00
- Structural Steel → 05 12 00
- Electrical → 26 00 00

### Hold Point Auto-Population
Read `specs-quality.json` → `hold_points[]` → match inspection type to hold point by `work_type`:
- Pull the hold point's `inspection_name`, `trigger` condition, `inspector`, and `spec_reference`
- Auto-populate the inspection's `linked_hold_point` and `linked_spec_section` fields
- Example: Scheduling "Concrete Pre-placement" → match hold_points where work_type contains "Concrete" → auto-link HP-02 with trigger "Before concrete placement" and spec reference

### Weather Threshold Check
Before scheduling outdoor inspections:
- Read `specs-quality.json` → `weather_thresholds[]` → match by the inspection's work type
- Cross-check forecasted weather against `min_temp`, `max_temp`, `max_wind`, and `moisture_ok`
- Flag if weather conditions may prevent the inspection or the underlying work (e.g., concrete pour inspection + temp < 40°F cold weather threshold)
- Include mitigation measures from the spec when flagging

### Spec Section Deep-Link
When an inspection type is identified:
- Read `specs-quality.json` → `spec_sections[]` → find the matching CSI section
- Pull specific `testing` requirements (frequency, type, agency), acceptance criteria from `key_req`, and required documentation
- Auto-populate inspection notes with testing protocol and acceptance criteria
- Example: Compaction inspection → pull "95% modified Proctor, testing every 500 CY" from spec section

### Schedule Activity Linking (Enhanced)
- Read `schedule.json` → `critical_path[]` and `milestones[]` → match inspection date/type to schedule activities
- Auto-link inspection to schedule activity and flag if the activity is on the critical path
- If critical path: add note "Critical path activity — inspection delay will impact project completion"

### Drawing Reference
When inspection location is identified:
- Read `plans-spatial.json` → `sheet_cross_references.drawing_index[]` → find relevant structural/MEP drawings for the inspection location and discipline
- Include referenced sheet numbers in inspection record for field use
- Example: Foundation inspection at Grid C-3 → reference sheets S2.1, S5.1

## Re-Inspection Workflow

When inspection result = `fail`:

1. **Create Re-Inspection Entry:**
   - Auto-generate new INSP ID (sequential)
   - Set type as "{Original Type} (Re-inspection)"
   - Set `related_to` field to original inspection ID
   - Suggest date 48 hours after deficiency notification

2. **Track Deficiencies:**
   - Collect detailed deficiency descriptions
   - Log which contractor responsible for correction
   - Reference section of spec violated
   - Attach photos of deficiency

3. **Notification:**
   - Alert responsible trade contractor
   - Flag in morning brief
   - Include in daily report until re-inspection passed

4. **Closure:**
   - Log re-inspection result
   - Document corrective action taken
   - Release hold if pass
   - Create additional re-inspection if still fail

## Permit Tracking & Expiration Alerts

**Auto-Alert Thresholds:**
- **30 days to expiration:** Yellow flag in status report; suggest renewal inquiry
- **7 days to expiration:** Red flag; escalate to project manager
- **Expired:** Red flag; mark status as `expired`; notify responsible party

**Renewal Workflow:**
- Track date application submitted for renewal
- Update status to `renewed` upon reissuance
- Maintain continuous permit coverage throughout project

## Integration Points

### Morning Brief (`/morning-brief`)
Display under "Inspections & Permits" section:
- Upcoming inspections (next 24 hours) — show type, time, location, inspector
- Overdue inspections (no result logged) — Red flag with days overdue
- Permits expiring within 30 days — Yellow alert with days remaining

### Look-Ahead Schedule (`/look-ahead`)
Include scheduled inspections in weekly look-ahead:
- Inspections integrated by date into weekly view
- Show impact on critical path if hold point inspection
- Cross-reference with material delivery/contractor schedule
- Highlight PEMB special inspections with bold/asterisk

### Daily Report (`/daily-report`)
Section: "Inspections Today"
- Scheduled inspections for the day (time, type, location, inspector)
- Completed inspections from previous day (result, notes summary)
- Pending re-inspections affecting schedule
- Permit status reminder (expiring within 14 days)

## Error Handling & Validation

- **Duplicate Re-inspection:** Warn if re-inspection already exists for same deficiency
- **Invalid Inspector:** Log "External Inspector" if not in approved list; alert PM
- **Missing Linked Activity:** Alert if schedule activity cannot be found; allow manual entry
- **Permit Conflict:** Warn if inspection scheduled outside permit scope
- **Date Validation:** Reject inspection scheduled before permit issued
- **Status Consistency:** Prevent result logging if status ≠ `scheduled`

## Triggers & Voice Commands

- "Schedule an inspection"
- "Log inspection INSP-042"
- "Show inspection status"
- "What inspections are overdue?"
- "Upcoming inspections?"
- "Schedule a rebar inspection for Monday"
- "Inspection failed — need re-inspection"
- "Track permits"
- "When does the building permit expire?"
- "Special inspection — anchor bolts"
- "Healthcare inspection — state health dept"

## Safety Incident Cross-Reference

For safety incidents discovered during inspections, route to the **safety-management** skill for incident documentation, root cause analysis (5-Why, Fishbone), OSHA recordkeeping (300/300A/301), and corrective action tracking. Write incident data to `safety-log.json`, not `inspection-log.json`.

When an inspection failure reveals a safety concern:
1. Log the inspection result normally in `inspection-log.json` (result: "fail", deficiencies noted)
2. Create a separate safety incident via the safety-management skill → writes to `safety-log.json`
3. Cross-reference the inspection ID in the safety incident record
4. The safety-management skill handles TRIR calculation, OSHA compliance, and corrective action lifecycle

---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
