# inspection-tracker — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the inspection-tracker skill.



## Output Formatting & Routing

### Status Report Display
```
INSPECTION STATUS REPORT
Generated: 2025-03-15 10:30 AM

UPCOMING (Next 7 Days):
┌─────────────┬──────────────────────┬────────────┬──────────────┬──────────────┐
│ ID          │ Type                 │ Date       │ Inspector    │ Location     │
├─────────────┼──────────────────────┼────────────┼──────────────┼──────────────┤
│ INSP-045    │ Rebar                │ 3/16 9 AM  │ John Smith   │ Bldg A L2    │
│ INSP-046    │ Electrical Rough-In  │ 3/18 1 PM  │ Jane Doe     │ Bldg B       │
└─────────────┴──────────────────────┴────────────┴──────────────┴──────────────┘

OVERDUE:
┌─────────────┬──────────────────────┬────────────┬───────────────────┐
│ ID          │ Type                 │ Scheduled  │ Days Overdue       │
├─────────────┼──────────────────────┼────────────┼───────────────────┤
│ INSP-042    │ Concrete Pre-place   │ 3/10 9 AM  │ 4 DAYS             │
└─────────────┴──────────────────────┴────────────┴───────────────────┘

RECENT RESULTS (Last 14 Days):
[Green] INSP-040: Foundation ✓ PASS (3/12)
[Red]   INSP-041: Formwork ✗ FAIL (3/13) → Re-inspect INSP-044 scheduled 3/15
[Yellow] INSP-039: Rebar ⚠ CONDITIONAL (3/11) → Awaiting verification

PERMIT STATUS:
[Active] PERMIT-001: Building Permit BP-2025-4521 (Exp: 2026-02-20)
[Yellow] PERMIT-003: Electrical Permit EP-2025-1847 (Exp: 3/25 — 10 days)
```

### Export to AI Output
Inspection status exportable to `folder_mapping.ai_output/inspection_reports/`:
- `inspection_status_YYYY-MM-DD.json` (machine-readable)
- `inspection_summary.md` (stakeholder report)
- `permit_tracking.xlsx` (expiration tracking)


