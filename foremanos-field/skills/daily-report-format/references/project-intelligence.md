# Project Intelligence Extraction Guide

How to extract, structure, and use project knowledge from construction documents. This guide is used by both `/set-project` and `/process-docs`.

## Extraction Philosophy

The goal is to build a "project brain" that makes daily reports context-aware. Instead of the user having to say "poured concrete at Grid A through C, Lines 1 through 5 on the east wing foundation," they can say "poured the east side foundation" and the report fills in the specifics.

Every piece of extracted data should serve at least one of these purposes:
1. **Auto-complete details** in daily reports (grid lines, room names, floor levels)
2. **Validate consistency** (correct sub names, proper spec references)
3. **Track progress** against schedule (milestone dates, phase status)
4. **Provide context** for photo captions and notes (compass direction, building areas)

## Document Type Extraction Guides

### Plans and Drawings

**What to look for:**

Grid lines:
- Column grids (typically letters: A, B, C or A.1, A.2)
- Row grids (typically numbers: 1, 2, 3)
- Grid spacing if noted
- Any offset or skewed grids

Building areas:
- Named wings (North Wing, South Wing, Tower, Podium)
- Building phases (Phase 1, Phase 2)
- Separate structures (Main Building, Garage, Utility Building)
- Additions vs. existing

Floor levels:
- Level naming convention (Level 1, Floor 1, Ground, Basement, B1, Mezzanine, Roof)
- Floor-to-floor heights if noted
- Finished floor elevations if noted

Room schedule:
- Room numbers and names from architectural floor plans
- Department or zone groupings
- Large or notable spaces (gymnasium, cafeteria, lobby, OR suite)

Site layout:
- North arrow orientation (north is at top, rotated, etc.)
- Construction entrance locations
- Material laydown areas
- Trailer/office locations
- Parking areas (construction vs. permanent)
- Haul routes
- Dumpster locations
- Crane locations or pick zones

**Storage format:**
```json
{
  "grid_lines": {
    "columns": ["A", "B", "C", "D", "E", "F", "G"],
    "rows": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    "spacing": "Columns at 24'-0\" o.c., Rows at 30'-0\" o.c.",
    "notes": "Grid A is west side, Grid G is east side. Grid 1 is south, Grid 10 is north."
  },
  "building_areas": [
    {"name": "East Wing", "grids": "E-G / 1-10", "floors": "1-2", "use": "Patient rooms"},
    {"name": "West Wing", "grids": "A-C / 1-10", "floors": "1-2", "use": "Common areas"},
    {"name": "Central Core", "grids": "C-E / 4-7", "floors": "1-2", "use": "Elevators, stairs, MEP"}
  ],
  "floor_levels": [
    {"name": "Level 1", "elevation": "100'-0\"", "description": "Ground floor"},
    {"name": "Level 2", "elevation": "114'-0\"", "description": "Upper floor"},
    {"name": "Roof", "elevation": "128'-0\"", "description": "Roof level"}
  ]
}
```

### Specifications

**What to look for:**

Active spec sections:
- Which CSI divisions are included (Division 03 - Concrete, Division 05 - Metals, etc.)
- Specific sections with key requirements

Key materials:
- Concrete mix designs and strengths (e.g., 4000 PSI at 28 days, 5000 PSI for post-tension)
- Rebar grade (Grade 60, epoxy coated)
- Structural steel (A992, A500)
- Roofing system type and manufacturer
- Waterproofing products
- Window/curtain wall systems
- Fire protection requirements

Testing/inspection requirements:
- Concrete testing frequency (1 set per X CY)
- Steel inspection requirements (shop welds, field connections)
- Fireproofing inspections
- Special inspections required by code
- Third-party testing agency name if listed

**Storage format:**
```json
{
  "active_spec_sections": [
    {"division": "03", "section": "03 30 00", "title": "Cast-in-Place Concrete", "key_req": "4000 PSI min, w/c ratio 0.45 max"},
    {"division": "05", "section": "05 12 00", "title": "Structural Steel", "key_req": "A992 Grade 50, shop primed"}
  ],
  "key_materials": [
    {"material": "Concrete (foundations)", "spec": "4000 PSI at 28 days, Type I/II cement"},
    {"material": "Concrete (elevated slabs)", "spec": "5000 PSI at 28 days, lightweight aggregate"},
    {"material": "Rebar", "spec": "ASTM A615 Grade 60, epoxy coated below grade"},
    {"material": "Structural steel", "spec": "ASTM A992 wide flange, A500 Grade B HSS"}
  ],
  "testing_requirements": [
    {"test": "Concrete cylinders", "frequency": "1 set per 50 CY or per day, whichever is more", "agency": "TBD"},
    {"test": "Compaction testing", "frequency": "Every 2 feet of fill or lift", "agency": "TBD"},
    {"test": "Structural steel connections", "frequency": "Special inspection per IBC", "agency": "TBD"}
  ]
}
```

### Project Schedule

**What to look for:**

Current phase and status:
- What activities are currently in progress
- Overall project percent complete

Milestones:
- Building permit / start date
- Foundation complete
- Steel/structure topping out
- Building dried in / weathertight
- MEP rough-in complete
- Inspection milestones (framing, insulation, final)
- Substantial completion
- Final completion
- Move-in / occupancy

Critical path:
- Activities currently on the critical path
- Float status of near-critical activities
- Activities that could become critical

Schedule risks:
- Long-lead items and their expected delivery dates
- Weather-sensitive activities
- Inspection-dependent sequences

**Storage format:**
```json
{
  "schedule": {
    "current_phase": "Foundation / Structural",
    "percent_complete": "15%",
    "milestones": [
      {"name": "Building Permit", "date": "2026-01-15", "status": "complete"},
      {"name": "Foundation Complete", "date": "2026-03-15", "status": "in_progress"},
      {"name": "Steel Topping Out", "date": "2026-05-01", "status": "upcoming"},
      {"name": "Substantial Completion", "date": "2026-10-15", "status": "upcoming"}
    ],
    "critical_path": [
      "Foundation excavation → Footings → Foundation walls → Backfill → SOG → Steel erection"
    ],
    "long_lead_items": [
      {"item": "Structural steel", "supplier": "TBD", "expected_delivery": "2026-04-01"},
      {"item": "Elevator equipment", "supplier": "TBD", "expected_delivery": "2026-06-15"}
    ]
  }
}
```

### Contract Documents

**What to look for:**
- Contract dates (NTP, substantial completion, final completion)
- Liquidated damages clause and daily rate
- Working hours and restrictions (no work before 7 AM, no Sunday work, etc.)
- Noise restrictions
- Owner-required documentation (daily reports specifically, photo requirements, etc.)
- Allowances and unit prices
- Key contract provisions affecting field operations

### Subcontractor Information

**What to look for:**
- Sub company name (exact legal name for reports)
- Trade / scope of work
- Foreman or site contact name
- Phone number
- Sub contract value (if available, for context on scope size)
- Scheduled start and finish dates

**Storage format:**
```json
{
  "subcontractors": [
    {
      "name": "Walker Construction",
      "trade": "Excavation / Sitework",
      "scope": "Excavation, grading, underground utilities, backfill, paving",
      "foreman": "John Walker",
      "phone": "555-0100",
      "start_date": "2026-02-01",
      "end_date": "2026-04-15"
    }
  ]
}
```

## How Daily Reports Use This Intelligence

### Auto-filling Location Details
When the user mentions a general area, the report can reference specific grid lines:
- User: "poured the east foundation" → Report: "Concrete placed for east wing foundation, Grid Lines E-G / 1-5, Level 1."

### Validating Sub Names
When the user mentions a sub casually, match it to the official name:
- User: "Walker was on site" → Report: "Walker Construction" (3 workers)

### Schedule Context
Daily reports can reference milestones:
- "Foundation work continues. Foundation Complete milestone scheduled for 03/15/2026."

### Material Specifics
When documenting concrete pours or material work:
- User: "poured footings" → Report: "Concrete placed per Section 03 30 00, 4000 PSI mix design."

### Photo Captioning
Use grid lines and compass orientation for accurate captions:
- "Foundation excavation at Grid C / Line 5, looking north toward East Wing."

### Inspection Awareness
Know what inspections are required for current work:
- If footings are being poured, note: "Footing inspection required prior to concrete placement per special inspection requirements."
