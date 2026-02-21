# project-data — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the project-data skill.



## Data Validation

Before saving any data, validate:

### Consistency checks (cross-file)
- Sub mentioned in `schedule.json` but not in `directory.json` → Flag
- Spec section referenced in `plans-spatial.json` but not in `specs-quality.json` → Flag
- Grid line referenced that doesn't exist in `plans-spatial.json` → Flag
- Floor level mentioned that's not in `plans-spatial.json` → Flag

### Duplicate detection
- Same sub name with slightly different spelling in `directory.json` → Ask user which is correct
- Same milestone with different names in `schedule.json` → Merge or ask user
- Overlapping scope between subs → Note but don't flag (this is normal)

### Completeness checks
- `project-config.json` → project_basics missing required fields → Prompt user
- `schedule.json` → milestones missing key dates (substantial completion, etc.) → Note
- `directory.json` → sub directory missing contact info → Note for user



## Merge Rules

When new data comes in from `/process-docs`, write to the appropriate file:

| Data Type | Target File | Merge Strategy |
|---|---|---|
| Subcontractors | directory.json | Add new, update existing (match on name), never delete |
| Vendor database | directory.json | Add new, update existing (match on company_name), never delete |
| Milestones | schedule.json | Update dates, add new milestones, never delete |
| Schedule (full update) | schedule.json | Replace current dates/critical path, keep history |
| Spec sections | specs-quality.json | Add new sections, update requirements, never delete |
| Weather thresholds | specs-quality.json | Update per spec section, log changes |
| Testing requirements | specs-quality.json | Add new, update frequency/agency, never delete |
| Safety zones | specs-quality.json | Add new, update existing |
| Geotechnical | specs-quality.json | Replace with newer data (assumes newer report) |
| SWPPP BMPs | specs-quality.json | Add new, update existing locations |
| Grid lines | plans-spatial.json | Merge (add new grids), never replace |
| Contract dates | specs-quality.json | Replace with newer, log change in version_history |
| RFIs | rfi-log.json | Add new, update status on existing (match on id), never delete |
| Submittals | submittal-log.json | Add new, update status/review on existing (match on id), never delete |
| Procurement | procurement-log.json | Add new, update delivery/status on existing (match on id), never delete |
| Owner reports | directory.json | Append only, never modify past entries |
| Lookahead history | schedule.json | Append only, keep historical records |

### Numbering Rules

Sequential IDs are auto-generated and must never duplicate:

| Log | File | Format | Example |
|---|---|---|---|
| RFIs | rfi-log.json | RFI-{NNN} | RFI-001, RFI-002 |
| Submittals | submittal-log.json | SUB-{NNN} | SUB-001, SUB-002 |
| Procurement | procurement-log.json | PROC-{NNN} | PROC-001, PROC-002 |
| Owner reports | directory.json | WR-{NNN} | WR-001, WR-002 |
| Vendors | directory.json | VENDOR-{NNN} | VENDOR-001, VENDOR-002 |

When creating a new entry, find the highest existing number and increment by 1. Lock the number immediately (same pattern as daily report numbering).



## Report History Schema

See `references/report-history-schema.md` for the full schema. Each daily report saves a structured entry to `daily-report-data.json`:

```json
{
  "report_date": "2026-02-12",
  "report_number": "MOSC-005",
  "weather": {
    "readings": [...],
    "narrative": "...",
    "impact": "none|minor|major",
    "conditions": ["clear", "rain", "snow", "wind", "fog"]
  },
  "crew": {
    "subs": [...],
    "total_headcount": 45,
    "expected_subs_missing": [...]
  },
  "materials": [...],
  "equipment": [...],
  "schedule": {
    "current_phase": "...",
    "percent_complete": "...",
    "delays": [...],
    "milestones_hit": [...]
  },
  "inspections": [...],
  "photos": [...],
  "notes": "...",
  "open_items": [...]
}
```



## Additional Validation Rules (New Data Types)

### RFI Log Validation (rfi-log.json)
- `drawing_references` must exist in loaded documents (`project-config.json` → documents_loaded) → Flag unknown sheets
- `spec_references` must match active `spec_sections` (`specs-quality.json`) → Flag unknown sections
- `addressed_to` should match project team (`project-config.json` → project_basics) → Suggest if blank
- Status transitions: draft → issued → response_received → resolved (no skipping)

### Submittal Log Validation (submittal-log.json)
- `spec_section` must match active `spec_sections` (`specs-quality.json`) → Flag unknown sections
- `submitting_sub` should match subcontractor directory (`directory.json`) → Fuzzy match
- If `submittal_required` = true on a spec section but no submittal exists → Flag missing submittal
- Resubmissions must reference original via `resubmission_of` and increment `revision_number`

### Procurement Log Validation (procurement-log.json)
- `spec_section` must match active `spec_sections` (`specs-quality.json`) → Flag unknown sections
- `submittal_id` should match an approved submittal (`submittal-log.json`) → Warn if ordering before approval
- `expected_delivery` must be before `schedule_activity_linked` start date (`schedule.json`) → Flag late deliveries
- `certs_required` vs `certs_received` → Flag incomplete cert packages

### Vendor Database Validation (directory.json)
- No duplicate company names (fuzzy match for similar names)
- `capabilities` should map to project material needs
- Flag vendors with no quotes in > 12 months as "stale"

### ASI Log Validation (project-config.json → asi_log)
- ASI numbers must be sequential (ASI-001, ASI-002, ASI-003, etc.)
- `affected_drawings` must reference sheets that exist in plan set
- `affected_spec_sections` must match CSI sections in `specs-quality.json`
- Linked `affected_submittals` must have matching submittal IDs in `submittal-log.json`
- Linked `affected_change_orders` must exist in `change-order-log.json`
- `scope_type` must be one of: "additive", "deductive", "clarification"
- `date_issued` must be between project NTP and completion date

### Pay Application Log Validation (pay-app-log.json)
- `pay_application_number` must be sequential (PA-001, PA-002, etc.)
- `payment_period_end_date` must be within contract date range
- `total_amount_requested` should not exceed contract value (if original, not with COs)
- Submitting contractor must exist in `directory.json`
- `retainage_rate` should match W Principles standard (10% flat) unless contract specifies otherwise
- Sum of `schedule_of_values` across all line items must equal or approximate contract value
- Lien waivers should be received before final payment approval

### Delay Log Validation (delay-log.json)
- `delay_event_id` must be sequential or unique identifiers
- `start_date` and `end_date` must be within project schedule dates
- `duration_days` must be consistent with start/end dates
- `affected_activities` should reference activities in `schedule.json`
- `responsible_party` must be one of: "contractor", "owner", "weather", "supplier", "concurrent"
- `documentation` should reference daily reports or other project files
- `approved_delay_days` should be ≤ `duration_days` (some delays may not be approved)
- For concurrent delays, flag if impact calculation differs between responsible parties



## Additional Resources

- **`references/config-schema.md`** — Full project intelligence config schema (organized by file)
- **`references/report-history-schema.md`** — Full report history entry schema

## Data Versioning

Track changes to key data points over time in `project-config.json` → `version_history`. When data is updated in ANY file (new schedule, revised milestone dates, updated sub list), log the change:

```json
{
  "version_history": [
    {
      "date": "2026-02-12",
      "source": "revised_schedule_020126.pdf",
      "changes": [
        {
          "field": "schedule.milestones.substantial_completion",
          "old_value": "2026-06-15",
          "new_value": "2026-07-01",
          "reason": "Schedule update from P6 revision 3"
        }
      ]
    }
  ]
}
```

This history is valuable for:
- Schedule narrative in daily reports ("Substantial completion date revised from 06/15 to 07/01 per schedule update dated 02/01/2026")
- Dashboard trending (milestone drift over time)
- Audit trail (when did we first know about a delay?)


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


