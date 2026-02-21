# drawing-control — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the drawing-control skill.



## 6. Drawing Index by Discipline

Construction drawing packages follow standard conventions. The drawing-control skill organizes sheets by discipline and enforces naming standards.

### Standard Sheet Series Organization

```
G-SERIES: GENERAL SHEETS
  G-001       Title Sheet & General Notes
  G-101       Abbreviations & Symbols

C-SERIES: CIVIL & SITE
  C-001       Site Plan & Site Utilities
  C-101       Grading & Drainage Plan
  C-102       Utility Plans
  C-103       Stormwater Management
  C-201       Landscape & Hardscape
  C-301       Demolition Plan (if applicable)

L-SERIES: LANDSCAPE (if separate from Civil)
  L-101       Landscape Master Plan
  L-102       Planting Details & Schedule

A-SERIES: ARCHITECTURAL
  A-101       Floor Plans - Level 1
  A-102       Floor Plans - Level 2 (if multi-story)
  A-103       Reflected Ceiling Plan
  A-104       Door & Hardware Schedule
  A-105       Finish Schedule
  A-201       Exterior Elevations
  A-202       Exterior Elevations (continued)
  A-301       Wall Sections
  A-302       Building Details - Part 1
  A-303       Building Details - Part 2

S-SERIES: STRUCTURAL
  S-001       Foundation Plan
  S-101       Framing Plans
  S-102       Framing Details
  S-201       Anchor Bolt Schedule
  S-202       Connection Details
  S-301       Roof Framing Plan
  S-302       Roof Details

M-SERIES: MECHANICAL
  M-001       HVAC System Diagram
  M-101       HVAC Plans
  M-102       Equipment Schedule
  M-103       Ductwork Details

P-SERIES: PLUMBING
  P-001       Plumbing System Diagram
  P-101       Plumbing Plans
  P-102       Fixture Schedule

E-SERIES: ELECTRICAL
  E-001       Power & Lighting Diagram
  E-101       Power Plans
  E-102       Lighting Plans
  E-103       Panel & Device Schedule

FP-SERIES: FIRE PROTECTION
  FP-001      Fire Alarm & Detection Plan
  FP-101      Fire Protection Plans
  FP-102      Fire Suppression Details
```

### Naming Convention Rules

```
[Series]-[Group]-[Sheet].[ext]
Example: A-101-Rev1.pdf

Rules:
  • Series: Two-letter code (G, C, L, A, S, M, P, E, FP)
  • Group: Three-digit sheet grouping (001-999 within each series)
  • Sheet: Single digit if multi-sheet (omit if single sheet)
  • Revision: Rev 0, Rev 1, Rev 2, etc. (or omit if stored separately)
  • Extension: .pdf, .dwg, .rfa as appropriate
```

---



## 7. Integration Points

The drawing-control skill feeds data to and receives triggers from other Foreman OS skills.

### Upstream Integrations (Sources of Drawing Data)

| Skill | Integration | Data Flow |
|-------|-------------|-----------|
| **document-intelligence** | Extraction pipeline | Scans incoming PDFs for sheet numbers, revision blocks, ASI references; flags missing metadata |
| **project-config** | Project setup | Reads project-config.json to cross-reference ASI log; updates with drawing links |
| **morning-brief** | Daily alerts | Receives new-revision triggers; includes in superintendent's briefing |

### Downstream Integrations (Consumers of Drawing Data)

| Skill | Integration | Data Flow |
|-------|-------------|-----------|
| **rfi-preparer** | RFI drafting | Auto-populates current revision when referencing drawings; suggests relevant sections |
| **daily-report-format** | Field documentation | Validates all drawing references against current set; warns on superseded sheets |
| **submittal-intelligence** | Submittal review | Cross-references drawing details; checks submittal specs against drawing notes |
| **look-ahead-planner** | Schedule integration | Tracks drawing deliverable dates (e.g., PEMB shop drawings due by 3/2) |
| **payment-app-manager** | Payment tracking | Verifies that work listed in pay apps matches current drawing scope |

---



## 8. Commands

The drawing-control skill is invoked via the `/drawings` command with subcommands for common tasks.

### `/drawings status`

Display the current set by discipline with revision and distribution status.

```bash
/drawings status [--discipline ARCH | --format table | json]
```

**Output**: Current Set Report (see Section 3)

---

### `/drawings add`

Register a new drawing in the log. Triggered manually or by document-intelligence when a new PDF is detected.

```bash
/drawings add
  --sheet-number A-101
  --title "Floor Plan"
  --discipline Arch
  --revision Rev 0
  --received-from "Smith Architects"
  --file-path /drawings/A-101-Rev0.pdf
  --notes "Initial design release"
```

**Validation**:
- Duplicate sheet number detection
- Revision numbering sequence check
- File existence verification

---

### `/drawings revise`

Record a new revision for an existing sheet. Automatically updates revision history and marks previous as superseded.

```bash
/drawings revise
  --sheet-number A-101
  --new-revision Rev 1
  --description "Door swing corrections per ASI-001"
  --asi-reference ASI-001
  --received-from "Smith Architects"
  --date-received 2026-01-15
  --file-path /drawings/A-101-Rev1.pdf
  --distribute-to "Super, PM, EKD, Stidham"
```

**Automatic Actions**:
- Marks previous revision as superseded
- Extracts revision cloud data (if available)
- Queues distribution notification
- Updates project-config.json ASI log

---

### `/drawings asi [number]`

Process an ASI and update all affected sheets in one command.

```bash
/drawings asi ASI-001
  --date-received 2026-01-15
  --issued-by "Smith Architects"
  --sheets "A-101, A-102, A-103"
  --description "Floor plan revisions"
  --file-paths "/drawings/A-101-Rev1.pdf, /drawings/A-102-Rev1.pdf, /drawings/A-103-Rev1.pdf"
  --distribute true
```

**Automatic Actions**:
- Increments revision for all listed sheets
- Marks prior revisions as superseded
- Cross-references ASI log in project-config.json
- Generates distribution notice
- Triggers notifications to field team

---

### `/drawings audit`

Compare field documentation against current drawing set. Scans daily reports, RFIs, and submittals for obsolete references.

```bash
/drawings audit [--from-date 2026-02-01] [--include-submittals true]
```

**Output**:
```
Field Set Audit — 2026-02-19

✓ 12 documents scanned
⚠ 2 ISSUES FOUND:

  Issue #1: Daily Report (2026-02-18) references S-202 Rev 0
    Current: S-202 Rev 1 (2026-02-06)
    Recipient: Walker Construction
    Action: Notify crew to retrieve latest revision

  Issue #2: RFI-003 references M-102 Rev 0
    Current: M-102 Rev 0 (no change)
    Status: OK — Reference is current
```

---

### `/drawings search [term]`

Search drawing log by sheet number, title, discipline, or keyword.

```bash
/drawings search "door"
  --discipline Arch
  --revision "Rev 1 or newer"
  --status current
```

**Output**:
```
Search Results: "door" (3 matches)

1. A-103 — Door & Hardware Schedule (Arch, Rev 1, current)
2. A-301 — Building Details (Arch, Rev 0, current) — includes door details
3. M-103 — Ductwork Details (Mech, Rev 0, current) — no matches on keyword
```

---



## 9. Data Store

The drawing log is stored as a JSON file in the Foreman OS AI output folder, making it accessible to all skills and portable for backup/archive.

### Storage Location

```
{{folder_mapping.ai_output}}/drawing-log.json
```

### Example drawing-log.json (4-Drawing Sample)

```json
{
  "project_id": "MOSC-825021",
  "project_name": "Morehead One Senior Care",
  "drawing_log_version": "1.0.0",
  "last_updated": "2026-02-19T14:30:00Z",
  "updated_by": "Andrew Eberle (PM)",
  "drawings": [
    {
      "drawing_id": "A-101-001",
      "sheet_number": "A-101",
      "title": "Floor Plan - Level 1",
      "discipline": "Arch",
      "current_revision": "Rev 1",
      "revision_date": "2026-01-15",
      "revision_history": [
        {
          "revision": "Rev 0",
          "date": "2025-12-10",
          "received_from": "Smith Architects, LLC",
          "description": "Initial design issue",
          "asi_number": null,
          "revision_clouds": null
        },
        {
          "revision": "Rev 1",
          "date": "2026-01-15",
          "received_from": "Smith Architects, LLC",
          "description": "Door swing corrections in Patient Rooms 101-102. Furniture layout adjusted for ADA path of travel.",
          "asi_number": "ASI-001",
          "revision_clouds": {
            "summary": "Three revision clouds marking door swings, casework depth, and corridor furniture",
            "grid_locations": ["3/B-C", "4/C-D", "2/A-B"],
            "change_type": "moderate"
          }
        }
      ],
      "date_received": "2025-12-10",
      "date_distributed": "2025-12-11",
      "distribution_list": [
        {
          "recipient": "W Principles (Super)",
          "role": "Super",
          "date_sent": "2025-12-11",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2025-12-11"
        },
        {
          "recipient": "EKD (Framing Sub)",
          "role": "Sub",
          "date_sent": "2026-01-16",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2026-01-16"
        }
      ],
      "superseded_revisions": [
        {
          "revision": "Rev 0",
          "marked_void_date": "2026-01-16",
          "reason": "Superseded by Rev 1 per ASI-001"
        }
      ],
      "status": "current",
      "file_reference": "/project/02-Contract Documents/Drawings/A-101-Rev1.pdf",
      "file_size_mb": 2.4,
      "total_sheets": 1,
      "notes": "Critical sheet; multiple subs reference for layout verification.",
      "linked_submittals": ["SUB-002"],
      "linked_rfi": ["RFI-003"]
    },
    {
      "drawing_id": "S-201-001",
      "sheet_number": "S-201",
      "title": "Anchor Bolt Schedule",
      "discipline": "Struct",
      "current_revision": "Rev 1",
      "revision_date": "2026-02-06",
      "revision_history": [
        {
          "revision": "Rev 0",
          "date": "2025-12-10",
          "received_from": "Yeiser Structural",
          "description": "Initial design with 1-1/4 primary and 3/4 secondary bolts",
          "asi_number": null,
          "revision_clouds": null
        },
        {
          "revision": "Rev 1",
          "date": "2026-02-06",
          "received_from": "Yeiser Structural",
          "description": "Anchor bolt layout corrected per Nucor PEMB approval; all column locations verified",
          "asi_number": "ASI-002",
          "revision_clouds": {
            "summary": "Revised anchor bolt grid layout; 6 revised locations marked",
            "grid_locations": ["1/A", "3/C", "5/D", "6/H"],
            "change_type": "major"
          }
        }
      ],
      "date_received": "2025-12-10",
      "date_distributed": "2026-02-07",
      "distribution_list": [
        {
          "recipient": "W Principles (Super)",
          "role": "Super",
          "date_sent": "2026-02-07",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2026-02-07"
        },
        {
          "recipient": "Alexander Construction (PEMB Erection)",
          "role": "Sub",
          "date_sent": "2026-02-07",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2026-02-08"
        },
        {
          "recipient": "Nucor Building Systems",
          "role": "Supplier",
          "date_sent": "2026-02-07",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2026-02-07"
        }
      ],
      "superseded_revisions": [
        {
          "revision": "Rev 0",
          "marked_void_date": "2026-02-07",
          "reason": "Superseded by Rev 1 per ASI-002; PEMB approval required before installation"
        }
      ],
      "status": "current",
      "file_reference": "/project/02-Contract Documents/Drawings/S-201-Rev1.pdf",
      "file_size_mb": 1.8,
      "total_sheets": 1,
      "notes": "Critical path item. Anchor bolts must be set per this revision before PEMB erection on 3/23/26.",
      "linked_submittals": [],
      "linked_rfi": ["RFI-001"]
    },
    {
      "drawing_id": "M-102-001",
      "sheet_number": "M-102",
      "title": "HVAC Equipment Schedule & Details",
      "discipline": "Mech",
      "current_revision": "Rev 0",
      "revision_date": "2025-12-10",
      "revision_history": [
        {
          "revision": "Rev 0",
          "date": "2025-12-10",
          "received_from": "Mechanical Engineer (TBD)",
          "description": "Initial design; 3 AHUs, 2 condensers, ERV equipment specified",
          "asi_number": null,
          "revision_clouds": null
        }
      ],
      "date_received": "2025-12-10",
      "date_distributed": "2025-12-15",
      "distribution_list": [
        {
          "recipient": "Davis and Plomin (HVAC Sub)",
          "role": "Sub",
          "date_sent": "2025-12-15",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2025-12-15"
        }
      ],
      "superseded_revisions": [],
      "status": "current",
      "file_reference": "/project/02-Contract Documents/Drawings/M-102-Rev0.pdf",
      "file_size_mb": 1.2,
      "total_sheets": 1,
      "notes": "Awaiting equipment submittals from Davis and Plomin. No changes anticipated pending supplier quotes.",
      "linked_submittals": ["SUB-007"],
      "linked_rfi": []
    },
    {
      "drawing_id": "C-001-001",
      "sheet_number": "C-001",
      "title": "Site Plan & Site Utilities",
      "discipline": "Civil",
      "current_revision": "Rev 0",
      "revision_date": "2026-01-20",
      "revision_history": [
        {
          "revision": "Rev 0",
          "date": "2026-01-20",
          "received_from": "Civil Engineer (TBD)",
          "description": "Site plan with utilities, stormwater, parking, and access road layout",
          "asi_number": null,
          "revision_clouds": null
        }
      ],
      "date_received": "2026-01-20",
      "date_distributed": "2026-01-20",
      "distribution_list": [
        {
          "recipient": "W Principles (Super)",
          "role": "Super",
          "date_sent": "2026-01-20",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2026-01-20"
        },
        {
          "recipient": "Walker Construction (Sitework)",
          "role": "Sub",
          "date_sent": "2026-01-20",
          "method": "email",
          "confirmed_receipt": true,
          "receipt_date": "2026-01-20"
        },
        {
          "recipient": "Ferguson (Utilities Supplier)",
          "role": "Supplier",
          "date_sent": "2026-01-20",
          "method": "email",
          "confirmed_receipt": false,
          "receipt_date": null
        }
      ],
      "superseded_revisions": [],
      "status": "current",
      "file_reference": "/project/02-Contract Documents/Drawings/C-001-Rev0.pdf",
      "file_size_mb": 3.1,
      "total_sheets": 1,
      "notes": "Follow up with Ferguson on receipt confirmation. Currently active for excavation and utility rough-in.",
      "linked_submittals": [],
      "linked_rfi": []
    }
  ],
  "summary": {
    "total_drawings": 32,
    "total_sheets": 32,
    "disciplines": {
      "Arch": 7,
      "Struct": 6,
      "Civil": 5,
      "Mech": 4,
      "Elec": 4,
      "Plumb": 3,
      "Fire": 2,
      "General": 1
    },
    "revisions_in_circulation": 30,
    "void_sheets": 1
  }
}
```

---



## 10. Error Handling & Validation

The drawing-control skill validates all inputs and alerts on data quality issues that could impact construction.

### Validation Rules

#### Duplicate Sheet Number Detection

```
ERROR: Duplicate sheet number detected
  Existing:  A-101, Rev 1, received 2026-01-15
  Attempting to add: A-101, Rev 1, received 2026-02-19
Action: Use /drawings revise instead to create a new revision
```

#### Missing Revision History Gaps

```
WARNING: Revision history gap detected
  Sheet: S-201
  History: Rev 0 (2025-12-10) → Rev 2 (2026-02-06)
  Missing: Rev 1
  Action: Verify revision sequence; contact sender if Rev 1 exists
```

#### ASI Reference Without Revision

```
ERROR: ASI reference without corresponding revision
  ASI: ASI-001 (2026-01-15)
  Cross-reference: No new revision issued for sheets A-101, A-102, A-103
  Action: Verify ASI was received; request drawings if revision is pending
```

#### Superseded Sheet Reference in Active Documents

```
ALERT: Superseded drawing referenced in current document
  Document: Daily Report (2026-02-18)
  References: S-202 Rev 0
  Current Revision: S-202 Rev 1 (2026-02-06)
  Issued to: Walker Construction
  Action: Notify crew; retrieve latest revision from SharePoint/trailer
  Severity: HIGH — This may impact foundation/PEMB accuracy
```

#### Missing Distribution Confirmation

```
WARNING: Distribution confirmation pending
  Sheet: C-001, Rev 0
  Recipient: Ferguson (Utilities)
  Sent: 2026-01-20
  Confirmed: Not yet
  Days Outstanding: 30
  Action: Follow up with Ferguson to confirm receipt by 2026-02-20
```

---



## 11. Best Practices for Drawing Management on Construction Sites

### Phase 1: Pre-Construction Setup

1. **Create Drawing Index** → Organize all issued-for-construction drawings by discipline using standard sheet numbering (G, C, A, S, M, P, E, FP series).
2. **Establish Distribution List** → Identify all trades, subs, suppliers, and consultants who need each drawing; assign roles (Super, PM, Foreman, Sub, Supplier, Other).
3. **Digitize Everything** → Scan hard-copy drawing sets; store PDFs in project-config folder with metadata (sheet number, revision, date received).
4. **Set Up Drawing Control Room** → Designate one location (trailer, office, or shared drive) as the official source; post large-format prints of current sheets.
5. **Conduct Pre-Con Drawing Review** → Walk subs through plan, details, and specs. Identify questions early (RFI phase).

### Phase 2: During Construction

6. **Centralize ASI Receipt** → When ASI arrives, immediately flag it in Foreman OS; trigger drawing-control to update revisions and re-distribute.
7. **Daily Drawing Verification** → Inspect active work areas to ensure crews are using current revisions. Conduct weekly field set audits.
8. **Track Superseded Sheets** → Collect void revisions from trailers, job boxes, and site offices. Ensure old prints don't circulate.
9. **Link Submittals to Drawings** → When a sub submits shop drawings, equipment specs, or samples, cross-reference against current construction drawings; flag conflicts in submittal-intelligence.
10. **Document in Daily Reports** → Reference sheet numbers and revisions in daily reports (drawing-control will validate against current set).
11. **Manage Drawing Changes** → If A/E issues an ASI or RFI clarification, don't let crews "just add a note" — issue a formal revision and re-distribute.

### Phase 3: Closeout

12. **Compile Record Drawings** → As-builts are recorded, update drawing-log with final revisions and mark obsolete sheets as archived.
13. **Generate Current Set Report** → Export final drawing log for owner's manuals and warranty documentation.
14. **Archive Everything** → Store digital drawing log, all revisions, and distribution records in project-config for future reference or change orders.

### Field-Proven Tips

- **Print Matters** → Always print and post the current drawing in the work area. Digital-only leads to mistakes.
- **Revision Blocks** → Insist that A/E mark revision blocks clearly; if missing, request clarification.
- **Color Coding** → On printed sets, use highlighter or tape to flag revised sections; makes field scanning easier.
- **Weekly Handout** → Distribute a 1-page "Current Drawing Set" summary every Friday so crews always know what's active.
- **Sub Sign-Off** → Require subs to sign off on drawing receipt and confirm they've discarded old revisions.
- **RFI Before Build** → If a drawing is unclear, issue an RFI *before* work starts, not after rework.
- **Revision Cloud Review** → Walk subs through revision clouds and change summaries; don't assume they'll spot deltas.

---



## 12. Integration with Foreman OS Workflow

The drawing-control skill operates as part of a larger ecosystem. Here's how it fits into typical daily operations:

### Morning Briefing (`/morning-brief`)

```
Morning Brief — Friday, 2026-02-19

Drawings Status:
  ✓ Current Set: 32 sheets (A-101 Rev 1, S-201 Rev 1, rest Rev 0)
  ⚠ Pending Revisions: ASI-003 drawings from Davis HVAC (awaiting)
  ⚠ Distribution Alert: Ferguson receipt unconfirmed for C-001 (30 days)

Action Items:
  • Follow up with Ferguson on C-001 receipt by COB today
  • Review ASI-002 revision clouds (S-201, S-202) with Alexander Construction
```

### RFI Preparation (`/rfi-preparer`)

When drafting an RFI, the rfi-preparer skill auto-populates current drawing references:

```
RFI-004: Clarification on HVAC rough-in locations

References:
  Drawing: M-102 (HVAC Equipment Schedule & Details), Rev 0, current
  Sections: East AHU location, Grid 5/C
  Notes: Drawing is current per drawing-control

Question: Equipment dimensions exceed available space per Plan. Confirm location tolerance.
```

### Daily Report Validation (`/daily-report-format`)

When a crew member writes a daily report mentioning a drawing, the skill validates it:

```
Daily Report (2026-02-19) — Walker Construction

✓ "Excavation progressed per C-001 site plan" — current revision verified
✓ "Footing layout confirmed against S-001" — current revision verified
✓ "Utility rough-in per C-102 utility plans" — current revision verified

All drawing references are CURRENT. No alerts.
```

### Drawing-to-Submittal Cross-Reference

When a submittal arrives, the skill links it to relevant drawings:

```
Submittal Review: SUB-003 (Schiller — Door Hardware)

Specification Sources:
  A-103 Door & Hardware Schedule, Rev 1 (current) ← Schiller referenced correctly
  Finishes: Match specification
  Hardware: 3 items substituted; review against schedule ⚠
  Approval: Pending hardware cross-check against current drawing
```

---



## 13. Technical Specifications

### System Requirements

- **Data Format**: JSON (UTF-8)
- **Storage**: File-based at {{folder_mapping.ai_output}}/drawing-log.json
- **File Size Handling**: Supports up to 500+ drawings per log (typical max for most projects)
- **API Integration**: RESTful read/write via Foreman OS skill interface
- **Backup**: Auto-backup triggered on each update (versioned snapshots)

### Performance Targets

- Drawing lookup: < 100 ms (sheet number, revision, status)
- Audit scan (12 documents): < 5 seconds
- ASI processing (5 sheets): < 2 seconds (includes extraction and distribution queue)
- Status report generation: < 2 seconds

### Data Retention

- **Active Project**: Retain all revisions and distribution records
- **Closeout**: Archive drawing-log with as-built markups for 7 years (per AIA standard)
- **Historical Access**: Query log by date range; version control maintained

---



## 14. Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Sheet number not found in log | Drawing not yet registered | Use `/drawings add` to register sheet; check file naming |
| Revision history gap (Rev 0 → Rev 2) | Missing intermediate revision | Verify with A/E that Rev 1 doesn't exist; contact if lost |
| Distribution list incomplete | Recipient added after initial distribution | Use `/drawings revise` to re-distribute and manually notify late recipients |
| ASI not cross-referenced in project-config | ASI received before drawing update | Run `/drawings asi [number]` to link ASI and update revisions |
| Field crew using old revision | Void sheets not collected from site | Conduct field audit; physically remove old prints and post current |
| Submittal references wrong drawing revision | Submittal received before drawing updated | Notify sub and request resubmittal against current drawing |

---



## 15. Glossary

- **ASI (Architect/Engineer Supplemental Instruction)**: Formal directive issued by A/E after construction begins; requires drawing revisions and field distribution.
- **Revision Block**: Table on drawing corner noting revision number, date, and change description.
- **Revision Cloud**: Dashed cloud shape drawn on revised drawing to highlight changed areas.
- **Superseded Sheet**: Previous revision marked void when newer revision issued.
- **Void Sheet**: Drawing that is no longer current and must not be used; physically collected and destroyed.
- **Current Set**: Complete set of all latest-revision drawings for the project.
- **Distribution List**: Record of who received which drawing revision and when.
- **Field Set Audit**: Inspection of physical drawings on site compared against digital log to ensure currency.
- **Change Delta**: Summary of differences between two drawing revisions.

---



## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-19 | Initial release; full feature set for ASI processing, revision tracking, and field auditing |

---



## Contact & Support

For questions on drawing management, ASI processing, or integration with other Foreman OS skills, consult the project memory (CLAUDE.md) or contact the Superintendent and PM.

**Project**: Morehead One Senior Care (MOSC-825021)
**Super**: Miles Goodman
**PM**: Andrew Eberle
**Skill Owner**: Foreman OS Drawing Control Module
**Last Updated**: 2026-02-19


