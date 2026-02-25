# Report History Schema

Full schema for `daily-report-data.json`. This file stores structured data from every generated daily report, feeding the project dashboard.

## File Structure

The file is a JSON object with a `reports` array. Each entry represents one daily report:

```json
{
  "project_code": "MOSC",
  "project_name": "Morehead One Senior Care",
  "reports": [
    { ... },
    { ... }
  ]
}
```

## Single Report Entry Schema

```json
{
  "report_date": "2026-02-12",
  "report_number": "MOSC-005",
  "generated_at": "2026-02-12T16:45:00Z",
  "docx_filename": "2_12_26_Daily_Report_MOSC.docx",
  "pdf_filename": "2_12_26_Daily_Report_MOSC.pdf",
  "claims_mode": false,

  "weather": {
    "readings": [
      {
        "time": "7:00 AM",
        "temperature": "32°F",
        "conditions": "Overcast"
      },
      {
        "time": "12:00 PM",
        "temperature": "41°F",
        "conditions": "Partly cloudy"
      },
      {
        "time": "4:00 PM",
        "temperature": "38°F",
        "conditions": "Clear"
      }
    ],
    "high_temp": "41°F",
    "low_temp": "32°F",
    "conditions_summary": ["overcast", "partly_cloudy", "clear"],
    "precipitation": "none",
    "wind": "10-15 mph gusts",
    "impact": "minor",
    "impact_details": "Cold weather concrete protocols in effect. Ground frost present in morning.",
    "weather_delay_hours": 0,
    "thresholds_triggered": [
      {
        "work_type": "Concrete placement",
        "threshold": "Cold weather: below 40°F",
        "action_taken": "Cold weather protection plan activated"
      }
    ]
  },

  "crew": {
    "subs_on_site": [
      {
        "name": "Walker Construction",
        "trade": "Excavation / Sitework",
        "headcount": 6,
        "work_performed": "Backfill operations continued at east wing foundation walls. Approximately 120 CY of structural fill placed and compacted.",
        "foreman": "John Walker"
      },
      {
        "name": "Metro Concrete",
        "trade": "Concrete",
        "headcount": 8,
        "work_performed": "Strip and clean formwork at west wing grade beams. Set forms for east wing SOG pour scheduled 02/14.",
        "foreman": "Dave Martinez"
      }
    ],
    "total_headcount": 45,
    "total_subs": 6,
    "expected_subs_missing": [
      {
        "name": "ABC Mechanical",
        "reason": "Material delay — ductwork not yet delivered",
        "impact": "Underground rough-in delayed 2 days"
      }
    ],
    "gc_staff_on_site": [
      {
        "name": "Miles Goodman",
        "role": "Superintendent"
      }
    ]
  },

  "materials": {
    "deliveries": [
      {
        "material": "Structural fill",
        "supplier": "Martin Marietta",
        "quantity": "6 loads (approx. 120 CY)",
        "po_number": "PO-2026-045",
        "condition": "Good",
        "location_stored": "East wing backfill area",
        "quantity_ordered": "",
        "quantity_received": "",
        "quantity_short": "",
        "partial_delivery": false,
        "backorder_expected": ""
      }
    ],
    "delivery_count": 1,
    "issues": []
  },

  "equipment": {
    "on_site": [
      {
        "equipment": "CAT 320 Excavator",
        "owner": "Walker Construction",
        "hours": 8,
        "status": "Active"
      },
      {
        "equipment": "Bomag BW 213 Roller",
        "owner": "Walker Construction",
        "hours": 6,
        "status": "Active"
      }
    ],
    "equipment_count": 8,
    "equipment_down": [],
    "new_equipment_mobilized": [],
    "equipment_demobilized": []
  },

  "schedule": {
    "current_phase": "Foundation / Structural",
    "percent_complete": "18%",
    "work_completed_today": [
      "East wing backfill 80% complete",
      "West wing grade beam formwork stripped"
    ],
    "delays": [
      {
        "description": "Mechanical underground delayed due to ductwork delivery",
        "cause": "material",
        "duration": "2 days estimated",
        "impact_on_critical_path": false,
        "sub_affected": "ABC Mechanical"
      }
    ],
    "milestones_hit": [],
    "milestones_approaching": [
      {
        "name": "Foundation Complete",
        "date": "2026-03-15",
        "days_away": 31,
        "on_track": true
      }
    ]
  },

  "delay_events": [
    {
      "delay_type": "Weather",
      "description": "",
      "activities_impacted": [],
      "date_start": "",
      "date_end": "",
      "estimated_duration": "",
      "critical_path_impact": false,
      "linked_delay_id": "",
      "responsible_party": "",
      "supporting_references": []
    }
  ],

  "inspections": {
    "conducted": [
      {
        "type": "Compaction testing",
        "inspector": "Smith Testing Lab",
        "organization": "Third-party",
        "purpose": "Backfill compaction at east wing",
        "time_in": "10:00 AM",
        "time_out": "11:30 AM",
        "result": "Pass",
        "notes": "98% modified proctor achieved. 3 tests conducted.",
        "linked_hold_point": "",
        "linked_spec_section": "",
        "linked_quality_checklist_id": "",
        "measurement_data": {
          "type": "",
          "value": "",
          "spec_requirement": "",
          "result": ""
        }
      }
    ],
    "visitors": [],
    "inspections_upcoming": [
      {
        "type": "Footing inspection",
        "scheduled_date": "2026-02-14",
        "area": "East wing SOG subgrade",
        "inspector": "City of Morehead"
      }
    ],
    "inspections_required_not_scheduled": []
  },

  "photos": {
    "count": 4,
    "photos": [
      {
        "caption": "Backfill operations in progress at east wing, Grid Lines E-G between Lines 3-7. Looking northwest.",
        "section_placed": "Crew on Site",
        "subject": "earthwork",
        "location": "East Wing"
      }
    ]
  },

  "notes": "Coordinated with ABC Mechanical foreman regarding delayed ductwork delivery. Supplier confirmed delivery for 02/14. Underground rough-in to resume upon receipt. Pre-pour meeting scheduled for 02/13 to review east wing SOG placement plan.",

  "open_items": [
    {
      "item": "ABC Mechanical ductwork delivery",
      "status": "pending",
      "date_opened": "2026-02-11",
      "expected_resolution": "2026-02-14"
    },
    {
      "item": "RFI #047 — East wing foundation drain detail",
      "status": "pending",
      "date_opened": "2026-02-05",
      "expected_resolution": "Awaiting architect response"
    }
  ],

  "carry_forward_items": [
    {
      "type": "failed_inspection|open_rfi|unresolved_delay|missing_crew|qa_flag|open_item",
      "description": "",
      "source_section": "",
      "date_originated": "",
      "priority": "high|medium|low",
      "linked_id": ""
    }
  ],

  "safety_notes": {
    "incidents": [],
    "near_misses": [],
    "toolbox_talk_topic": "",
    "safety_observations": ""
  },

  "swppp_notes": {
    "inspection_conducted": false,
    "rainfall_last_24h": "0.0\"",
    "bmp_conditions": "",
    "corrective_actions": []
  }
}
```

## Dashboard Aggregation Queries

The dashboard skill reads this file and aggregates data. Common queries:

### Weekly Tab Data
- **Crew trend**: `reports[last 7 days].crew.total_headcount` → line chart
- **Sub attendance**: `reports[last 7 days].crew.subs_on_site[].name` → who showed up each day
- **Missing subs**: `reports[last 7 days].crew.expected_subs_missing` → attendance gaps
- **Weather this week**: `reports[last 7 days].weather` → conditions, temps, delays
- **Weather delays**: `reports[last 7 days].weather.weather_delay_hours` → total hours lost
- **Inspections**: `reports[last 7 days].inspections` → pass/fail summary
- **Active delays**: `reports[latest].schedule.delays` → current delay list
- **Open items**: `reports[latest].open_items` → unresolved items

### Project Tab Data
- **Headcount over time**: `reports[all].crew.total_headcount` → line chart
- **Cumulative weather delays**: Running sum of `weather.weather_delay_hours`
- **Weather day breakdown**: Count of days by `weather.impact` (none/minor/major)
- **Milestone tracking**: Compare `schedule.milestones_hit` dates vs. planned dates from config
- **Milestone drift**: Track milestone date changes through `version_history` in config
- **Sub mobilization timeline**: First/last appearance of each sub in `crew.subs_on_site`
- **Inspection rates**: Aggregate `inspections.conducted[].result` → pass/fail/conditional counts
- **Percent complete curve**: `reports[all].schedule.percent_complete` → S-curve
- **Delivery log**: All `materials.deliveries` across all reports
- **Equipment utilization**: Equipment appearances and status across reports

## Notes

- Report entries are appended chronologically. Never modify a past entry — the data represents what was reported on that date.
- If a report is regenerated for the same date, replace the entry for that date (don't duplicate).
- The `open_items` array carries forward — items from previous reports that are still open should appear in the latest report. When resolved, mark status as "resolved" with the resolution date.
- `safety_notes` and `swppp_notes` are included even if empty, to maintain the schema for dashboard aggregation.
