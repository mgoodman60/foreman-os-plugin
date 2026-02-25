# Intake Log Schema

JSON schema for `daily-report-intake.json`. This file accumulates classified field observations throughout the day.

## File Structure

```json
{
  "date": "2026-02-12",
  "entries": [
    {
      "timestamp": "2026-02-12T09:15:00Z",
      "raw_input": "Original user input exactly as typed",
      "sections": [
        {
          "section": "crew",
          "data": {
            "sub": "Walker Construction",
            "sub_matched": true,
            "headcount": 6,
            "work": "Backfill operations at east wing foundation walls",
            "location": "East Wing, Grid Lines E-G",
            "location_resolved": true
          }
        }
      ],
      "photos": [],
      "enrichment_applied": ["sub_resolution", "location_resolution"],
      "unresolved": []
    }
  ],
  "summary": {
    "total_entries": 1,
    "sections_covered": ["crew"],
    "sections_missing": ["weather", "materials", "equipment", "schedule", "inspections", "notes"],
    "unresolved_entities": [],
    "carry_forward_items": []
  }
}
```

## Section Data Schemas

### Weather Entry
```json
{
  "section": "weather",
  "data": {
    "time": "7:00 AM",
    "temperature": "35°F",
    "conditions": "Overcast",
    "site_impact": "Ground frost present, soft conditions in laydown area",
    "work_impact": "none|minor|major",
    "delay_hours": 0
  }
}
```

### Crew Entry
```json
{
  "section": "crew",
  "data": {
    "sub": "Walker Construction",
    "sub_matched": true,
    "headcount": 6,
    "trade": "Excavation / Sitework",
    "work": "Backfill operations at east wing",
    "location": "East Wing, Grid Lines E-G",
    "location_resolved": true,
    "spec_references": []
  }
}
```

**Claims-mode optional fields** (when `claims_mode: true` in project-config.json):

```json
"claims_detail": {
  "worker_names": ["J. Smith", "R. Jones", "M. Davis"],
  "start_time": "7:00 AM",
  "end_time": "3:30 PM",
  "total_hours": 8.5,
  "overtime_hours": 0,
  "productivity_observation": "",
  "work_not_performed": "",
  "work_not_performed_reason": ""
}
```

### Materials Entry
```json
{
  "section": "materials",
  "data": {
    "material": "Structural fill",
    "supplier": "Martin Marietta",
    "quantity": "6 loads (approx. 120 CY)",
    "po_number": "",
    "condition": "Good",
    "location_stored": "East wing backfill area",
    "issues": [],
    "quantity_ordered": "",
    "quantity_received": "",
    "quantity_short": "",
    "partial_delivery": false,
    "backorder_expected": ""
  }
}
```

**Claims-mode optional fields:**

```json
"claims_detail": {
  "scheduled_delivery_time": "9:00 AM",
  "actual_delivery_time": "11:30 AM",
  "delivery_ticket_number": "DT-2026-0215",
  "accepted_rejected": "accepted",
  "exceptions": ""
}
```

### Equipment Entry
```json
{
  "section": "equipment",
  "data": {
    "equipment": "CAT 320 Excavator",
    "owner": "Walker Construction",
    "hours": 8,
    "status": "Active|Idle|Down|Mobilized|Demobilized",
    "down_reason": "",
    "location": "",
    "mobilization_date": "",
    "demobilization_date": ""
  }
}
```

**Claims-mode optional fields:**

```json
"claims_detail": {
  "equipment_id": "Unit #E-207",
  "idle_hours": 0,
  "idle_reason": "",
  "standby_hours": 0,
  "standby_reason": ""
}
```

### Schedule Entry
```json
{
  "section": "schedule",
  "data": {
    "update_type": "progress|delay|milestone|phase_change",
    "description": "Foundation work 80% complete",
    "percent_complete": "18%",
    "milestone_affected": "",
    "delay_cause": "",
    "delay_duration": ""
  }
}
```

### Delay Event Entry

When work is prevented, stopped, or impacted, classify as BOTH the relevant work section AND as a `delay_event`. The delay event captures the cause; the work section captures the effect.

```json
{
  "section": "delay_event",
  "data": {
    "delay_type": "Weather|Owner-Directed|Design/Spec|Material/Supply Chain|Sub Performance|Force Majeure|Permit/Regulatory|Differing Site Conditions",
    "description": "Concrete placement delayed due to temperature below 40°F threshold",
    "activities_impacted": ["Foundation_Footings_C1_C6"],
    "date_start": "2026-02-15",
    "date_end": "",
    "estimated_duration": "2 days",
    "critical_path_impact": true,
    "linked_delay_id": "DELAY-001",
    "responsible_party": "force_majeure|owner|architect|sub|gc|other",
    "supporting_references": ["RFI-042", "weather readings"]
  }
}
```

- `delay_type` values match delay-tracker skill categories exactly
- `linked_delay_id` references existing DELAY-NNN entries in delay-log.json, or empty for new events
- `activities_impacted` uses schedule activity IDs from schedule.json
- `responsible_party` identifies who bears responsibility for the delay

### Inspection Entry
```json
{
  "section": "inspections",
  "data": {
    "type": "visitor|inspection",
    "name": "John Smith",
    "organization": "City of Morehead",
    "purpose": "Footing inspection",
    "time_in": "10:00 AM",
    "time_out": "11:00 AM",
    "result": "Pass|Fail|Conditional|N/A",
    "notes": "",
    "linked_hold_point": "HP-08",
    "linked_spec_section": "3.2.1",
    "linked_quality_checklist_id": "QC-03-001",
    "measurement_data": {
      "type": "compaction",
      "value": "98%",
      "spec_requirement": "95% modified proctor",
      "result": "Pass"
    }
  }
}
```

The `linked_hold_point` format matches inspection-tracker's HP-XX pattern. The `linked_quality_checklist_id` matches quality-management's QC-XX-XXX format. When work type is logged that has known hold points in specs-quality.json, the system auto-suggests matching hold points for user confirmation.

### Notes Entry
```json
{
  "section": "notes",
  "data": {
    "content": "Coordinated with architect regarding stair detail RFI #047",
    "category": "coordination|rfi|directive|observation|upcoming|other"
  }
}
```

### Photos Entry

```json
{
  "section": "photos",
  "data": {
    "filename": "IMG_2026_0215_001.jpg",
    "caption": "Backfill operations in progress at east wing",
    "subject": "earthwork|concrete|steel|equipment|delivery|conditions|safety|general",
    "location": "East Wing, Grid Lines E-G",
    "direction": "northwest",
    "section_placed": "crew|materials|equipment|inspections|weather|notes",
    "analysis_notes": ""
  }
}
```

- `subject` classifies the photo content for indexing
- `section_placed` indicates which report section the photo was placed in (per photo-guidelines.md tiebreaker rules)
- `direction` captures compass direction if determinable from the image

## Summary Object

The summary object is updated after each new entry to give a quick overview of coverage:

- `sections_covered`: which report sections have at least one entry
- `sections_missing`: which sections have no entries yet (used for gap analysis during /daily-report generation)
- `unresolved_entities`: sub names or locations that couldn't be matched to project intelligence

### Carry-Forward Items

Populated at report generation time (not during intake). Consumed by the `/morning-brief` command's Step 5.

```json
"carry_forward_items": [
  {
    "type": "failed_inspection|open_rfi|unresolved_delay|missing_crew|qa_flag|open_item",
    "description": "Compaction test failed at east wing — re-test required",
    "source_section": "inspections",
    "date_originated": "2026-02-12",
    "priority": "high|medium|low",
    "linked_id": "INSP-005"
  }
]
```

- `type` maps to morning-brief's 5 carry-forward sources: open items, active delays, failed inspections, missing subs, upcoming inspections
- `priority` determines presentation order in the morning briefing
- `linked_id` cross-references specific inspection, delay, or RFI entries

## Section-to-Template Mapping

| Schema Section | Template Section Header | Report History Key |
|---|---|---|
| `weather` | WEATHER CONDITIONS | weather |
| `crew` | CREW ON SITE | crew |
| `materials` | MATERIALS RECEIVED | materials |
| `equipment` | EQUIPMENT ON SITE | equipment |
| `schedule` | SCHEDULE UPDATES | schedule |
| `inspections` | VISITORS / INSPECTIONS | inspections |
| `photos` | SITE PHOTOS | photos |
| `notes` | GENERAL NOTES | notes |
| `delay_event` | *(captured in SCHEDULE UPDATES and/or GENERAL NOTES)* | delay_events |

## Enum Values

| Field | Valid Values |
|---|---|
| `weather.work_impact` | none, minor, major |
| `equipment.status` | Active, Idle, Down, Mobilized, Demobilized |
| `schedule.update_type` | progress, delay, milestone, phase_change |
| `inspections.result` | Pass, Fail, Conditional, N/A |
| `notes.category` | coordination, rfi, directive, observation, upcoming, other |
| `delay_event.delay_type` | Weather, Owner-Directed, Design/Spec, Material/Supply Chain, Sub Performance, Force Majeure, Permit/Regulatory, Differing Site Conditions |
| `delay_event.responsible_party` | force_majeure, owner, architect, sub, gc, other |
| `carry_forward_items.type` | failed_inspection, open_rfi, unresolved_delay, missing_crew, qa_flag, open_item |
| `carry_forward_items.priority` | high, medium, low |
| `photos.subject` | earthwork, concrete, steel, equipment, delivery, conditions, safety, general |
| `materials.condition` | Good, Damaged, Wrong, Short, Partial |
