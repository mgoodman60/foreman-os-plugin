# quality-management — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the quality-management skill.



## Checklist Data Model (JSON Schema)

All quality checklists conform to this data structure for consistency, searchability, and integration with QMS reporting.

```json
{
  "checklist": {
    "checklist_id": "QC-03-001",
    "checklist_type": "three_phase",
    "trade": "Concrete - Foundation",
    "csi_division": "03 30 00",
    "phase": "pre_installation",
    "location": {
      "area": "Foundation",
      "grid_reference": "A1-A3, B1-B3",
      "building_section": "Entire footprint"
    },
    "project_info": {
      "project_code": "MOSC-825021",
      "project_name": "Morehead One Senior Care",
      "date_created": "2026-02-15",
      "scheduled_work_date": "2026-02-17"
    },
    "personnel": {
      "inspector": {
        "name": "Miles Goodman",
        "title": "Superintendent",
        "company": "W Principles"
      },
      "trade_foreman": {
        "name": "TBD",
        "company": "Walker Construction / W Principles"
      },
      "witness": {
        "title": "Building Official / Terracon",
        "present": false,
        "notes": "Hold point — requires witness before concrete pour"
      }
    },
    "items": [
      {
        "item_number": 1,
        "section": "Formwork & Substrate",
        "description": "Formwork alignment and bracing verified",
        "acceptance_criteria": "Within 1/4 inch tolerance per ACI 117 standard",
        "spec_reference": "Section 03 30 00, Para 3.02.A",
        "drawing_reference": "S-101, Sheet 1",
        "measurement_method": "Laser level transit, straightedge measurement",
        "pass_fail": true,
        "result": "pass",
        "measurement_value": "1/8 inch maximum deviation",
        "notes": "Formwork braced with diagonal cross-bracing, spreader bars secure",
        "photo_reference": [
          "QC-03-001-P001.jpg",
          "QC-03-001-P002.jpg"
        ],
        "timestamp": "2026-02-15T14:30:00Z",
        "inspector_signature": "MG"
      },
      {
        "item_number": 2,
        "section": "Reinforcing Steel",
        "description": "Rebar spacing verified at footing perimeter",
        "acceptance_criteria": "Within ±1/4 inch of plan dimension; minimum 2 inch concrete cover to edge",
        "spec_reference": "Section 03 20 00, ACI 315",
        "drawing_reference": "S-102 Detail 3",
        "measurement_method": "Measurement tape; depth gauge for cover verification",
        "pass_fail": true,
        "result": "pass",
        "measurement_value": "Spacing 12 inch ±1/8 inch, cover 2.25 inch",
        "notes": "All rebar tied and secured; wire ties spaced 18 inch apart as required",
        "photo_reference": ["QC-03-001-P003.jpg"],
        "timestamp": "2026-02-15T15:15:00Z",
        "inspector_signature": "MG"
      },
      {
        "item_number": 3,
        "section": "Embedments",
        "description": "Anchor bolt template alignment verified",
        "acceptance_criteria": "Location within 1/2 inch of template; plumb within 1/8 inch",
        "spec_reference": "Section 05 12 00; Nucor dwg S25R0990A-3",
        "drawing_reference": "S-103 Anchor Bolt Detail",
        "measurement_method": "Laser transit verification against template",
        "pass_fail": true,
        "result": "pass",
        "measurement_value": "All bolts within 3/8 inch of template; plumb 1/16 inch",
        "notes": "Template secured to formwork; bolts staggered and braced. Terracon observation required before placement.",
        "hold_point": true,
        "hold_point_status": "awaiting_witness",
        "photo_reference": ["QC-03-001-P004.jpg"],
        "timestamp": "2026-02-15T16:00:00Z",
        "inspector_signature": "MG"
      },
      {
        "item_number": 4,
        "section": "Materials",
        "description": "Concrete mix design approval — Wells Concrete formula",
        "acceptance_criteria": "4000 PSI 28-day strength interior, 4500 PSI exterior; slump 4-5 inch; 4-6% air",
        "spec_reference": "Section 03 30 00; Wells Mix Design #WC-3950",
        "drawing_reference": "Project Specifications Div 03",
        "measurement_method": "Documentation review; mill certs on file",
        "pass_fail": true,
        "result": "pass",
        "notes": "Mix design includes RSA-10 air entrainer and FINISHEASE water reducer per spec. Approved by engineer.",
        "document_reference": ["WellsConcrete_MixDesign_WC-3950.pdf"],
        "timestamp": "2026-02-14T10:00:00Z",
        "approver_signature": "MG"
      },
      {
        "item_number": 5,
        "section": "Environmental",
        "description": "Weather conditions verified for placement",
        "acceptance_criteria": "Min 40F rising temperature; no rain forecast within 24 hours; max 90F ambient",
        "spec_reference": "ACI 305 Cold Weather; ACI 306 Hot Weather",
        "measurement_method": "Weather forecast review; thermometer reading on-site",
        "pass_fail": true,
        "result": "pass",
        "measurement_value": "Current: 48F rising; Forecast: clear 48-65F for 48 hours",
        "notes": "Curing compound staged on site for immediate application. Cold weather procedures not required.",
        "timestamp": "2026-02-15T08:00:00Z",
        "inspector_signature": "MG"
      }
    ],
    "hold_points": [
      {
        "hold_point_id": "HP-003",
        "description": "Anchor Bolt Template Verification",
        "trigger": "Before concrete pour",
        "responsible_parties": ["Superintendent", "Nucor Erection Team Lead"],
        "verification_method": "Laser transit survey; visual inspection of template",
        "release_criteria": "All anchor bolts plumb and within 1/2 inch of template; photo documentation complete",
        "status": "pending",
        "scheduled_date": "2026-02-17"
      }
    ],
    "summary": {
      "total_items": 5,
      "items_passed": 5,
      "items_failed": 0,
      "items_conditional": 0,
      "pass_rate": 1.0,
      "overall_status": "approved_with_hold_point",
      "status_notes": "Pre-installation checklist approved pending HP-003 witness verification"
    },
    "deficiencies": [],
    "corrective_actions": [],
    "signatures": {
      "inspector": {
        "name": "Miles Goodman",
        "date": "2026-02-15",
        "time": "16:30:00Z"
      },
      "superintendent": {
        "name": "",
        "date": "",
        "time": ""
      },
      "trade_foreman": {
        "name": "",
        "date": "",
        "time": ""
      },
      "witness_required": true,
      "witness": {
        "title": "Building Official / Geotechnical Engineer",
        "date": "",
        "time": ""
      }
    },
    "attachments": {
      "photos": ["QC-03-001-P001.jpg", "QC-03-001-P002.jpg", "QC-03-001-P003.jpg", "QC-03-001-P004.jpg"],
      "documents": ["WellsConcrete_MixDesign_WC-3950.pdf", "Terracon_BearingVerification.pdf"],
      "calculations": []
    },
    "follow_up": {
      "next_checklist": "QC-03-002",
      "next_phase": "installation",
      "scheduled_date": "2026-02-17T08:00:00Z",
      "notes": "Installation checklist to monitor slump, air content, vibration, and curing during placement"
    }
  }
}
```

---



## Inspection and Test Plan (ITP) Master Schedule

The Inspection and Test Plan defines every required inspection, hold point, witness requirement, and test for the project. It maps to the critical path and ensures nothing is missed.

| Activity | CSI Div | Hold Point | Witness | Inspection Method | Frequency | Acceptance Criteria | Schedule |
|----------|---------|-----------|---------|------------------|-----------|-------------------|----------|
| Foundation Excavation | 31 | HP-001 | Terracon | Proof-roll / visual | After 500 CY | No rutting >1" | 01/27 - 02/01 |
| Footing Rebar | 03 20 | HP-002 | Building Official | Measurement / visual | 100% | Cover, spacing ±1/4" | 02/10 |
| Anchor Bolt Template | 05 12 | HP-003 | Nucor + Super | Transit survey | 1 per frame | ±1/2" of template | 02/15 |
| Footing Concrete | 03 30 | — | — | Slump, air, temp, cylinders | Per truck | Per Wells mix design | 02/17 |
| Stem Wall Rebar | 03 20 | HP-004 | Building Official | Measurement / visual | 100% | Cover, spacing | 02/21 |
| Stem Wall Concrete | 03 30 | — | — | Slump, air, temp, cylinders | Per truck | Per Wells mix design | 02/23 |
| Anchor Bolt Survey | 05 12 | HP-005 | Surveyor | Transit survey final | 1 survey | ±1/4" of PEMB requirement | 03/01 |
| SOG Reinforcing | 03 20 | HP-006 | Building Official | Measurement / visual | 100% | Spacing, cover per plan | 03/10 |
| SOG Concrete | 03 30 | HP-007 | Building Official | Moisture test, slump, cylinders | Per truck / per 50 CY | 4000 PSI interior / 4500 exterior | 03/12 |
| PEMB Erection | 05 | — | — | Bolt torque, plumb, connections | Per frame | ±1/4" plumb, bolts tight | 03/23 - 04/10 |
| PEMB Connections (welds) | 05 | — | Welder | Visual / UT if req'd | Per joint | Per AISC D1.1 | 03/23 - 04/10 |
| Roof Substrate Moisture | 07 | HP-008 | Mfr Rep | Calcium chloride test | 1 per 5000 SF | <3 lbs/1000 SF | 04/15 |
| Roof Installation | 07 31 | HP-009 | Mfr Rep | Visual / peel test / flood test | Per 500 SF | Seams sealed, no leaks | 04/18 - 04/25 |
| CFS Framing | 09 22 | — | — | Spacing, plumb, bracing | Per 500 SF | 16" OC ±1/8", plumb ±1/4" | 04/21 - 05/15 |
| GWB Installation | 09 29 | — | — | Fastener spacing, joint inspection | Per 1000 SF | Spacing per spec, smooth joints | 04/28 - 05/20 |
| GWB Finish L4 | 09 29 | — | — | Rake light inspection | 100% | L4 per spec requirement | 05/25 - 06/10 |
| MEP Rough-In | 21-28 | HP-010 | Building Official | Routing per plans, pressure test | Per run / per system | Per code and spec | 04/21 - 05/29 |
| MEP Penetration Sealing | 21/07 | HP-011 | Building Official | Visual / caulk verification | 100% penetrations | Fire-rated sealing complete | 05/20 - 06/01 |
| Paint Preparation | 09 91 | — | — | Surface prep inspection | 100% | L3/L4 finish ready | 06/02 - 06/10 |
| Paint Application | 09 91 | — | — | Mil thickness, coverage, color | Per 500 SF | Per spec mil thickness & coverage | 06/11 - 06/25 |
| Flooring Installation | 09 65 | — | — | Seam inspection, adhesive verification | Per 500 SF | Seams bonded, pattern correct | 06/15 - 07/05 |
| Door & Hardware | 08 | — | — | Operation, keying, fire rating | 100% | Smooth operation, fire assembly complete | 06/20 - 07/10 |
| Final Systems Test | 21-28 | HP-012 | Building Official | Pressure test, functional test, balance | 100% | All systems pass spec requirements | 07/15 - 07/20 |
| Punch-List Final | — | — | GC/Architect | Visual walkdown | 100% | All items complete and acceptable | 07/25 - 07/29 |

---



## Corrective Action Tracking System

When non-conformance is detected, a formal Corrective Action (CA) is initiated. The system tracks the issue from identification through closure.

### Severity Classification

| Severity | Definition | Response Time | Example |
|----------|-----------|----------------|---------|
| **Minor** | Cosmetic defect, no code impact | 5 business days | Paint run, corner bead lippage, touch-up needed |
| **Major** | Specification non-conformance, possible code issue | 2 business days | Rebar cover 1.5" instead of 2", joint compound thin |
| **Critical** | Code violation, life-safety risk, structural concern | 24 hours | Anchor bolt 1" out of template, fire-rated assembly incomplete, electrical clearance violation |

### Corrective Action Form (JSON)

```json
{
  "corrective_action": {
    "ca_number": "CA-03-001",
    "date_issued": "2026-02-18",
    "severity": "major",
    "discovery_source": "Quality inspection checklist QC-03-002",

    "finding": {
      "description": "Concrete test cylinders not cast for footing pour on 2026-02-17",
      "location": "Grid A1-A3 footings",
      "specification_violated": "Section 03 30 00, Para 3.04.B — 1 set per 50 CY minimum",
      "impact": "Unable to verify 7-day and 28-day concrete strength; potential delay to stem wall construction",
      "discovered_by": "Miles Goodman",
      "discovery_date": "2026-02-18T08:30:00Z"
    },

    "root_cause_analysis": {
      "analysis_method": "Five Whys",
      "primary_cause": "Concrete supplier (Wells Concrete) did not receive testing instruction until day-of placement",
      "contributing_factors": [
        "Testing requirement not included in pre-pour quality briefing",
        "Concrete contract did not explicitly include testing scope",
        "No written test plan communicated to supplier"
      ],
      "analysis_date": "2026-02-18T10:00:00Z",
      "analyst": "Andrew Eberle"
    },

    "corrective_action": {
      "action_1": {
        "description": "Issue amended concrete testing specification to Wells Concrete; require cylinders for all future pours",
        "responsible_party": "Andrew Eberle (PM)",
        "target_completion": "2026-02-18",
        "status": "complete",
        "completion_date": "2026-02-18T11:00:00Z",
        "verification": "Email sent to Wells Concrete project manager with testing requirements"
      },
      "action_2": {
        "description": "Conduct pre-pour quality briefing for stem wall concrete (2026-02-23); include testing scope",
        "responsible_party": "Miles Goodman (Super)",
        "target_completion": "2026-02-21",
        "status": "pending",
        "notes": "Brief to include Wells Concrete foreman, W Principles concrete crew, PM, and GC inspection"
      },
      "action_3": {
        "description": "Cast supplemental test cylinders from stem wall pour to validate footing strength assumption",
        "responsible_party": "Wells Concrete",
        "target_completion": "2026-02-23",
        "status": "pending",
        "notes": "Use same mix design and procedures as footing pour; test at 7 and 28 days"
      }
    },

    "prevention_measure": {
      "description": "Develop concrete testing matrix for all future pours; include in pre-construction quality briefing",
      "responsibility": "PM to develop and communicate",
      "implementation": "Integrate into project quality manual and pre-pour checklist"
    },

    "verification": {
      "verification_method": "Inspection of supplemental cylinders; strength report review",
      "verified_by": "Miles Goodman",
      "verification_date": "",
      "status": "pending"
    },

    "closure": {
      "status": "open",
      "closure_date": "",
      "closure_approval": "",
      "notes": ""
    }
  }
}
```

### CA Workflow

1. **Discovery**: Non-conformance identified during inspection or observation
2. **Documentation**: CA form filled out with finding, location, spec reference
3. **Root Cause Analysis**: 5 Why analysis conducted within 24 hrs of critical finding
4. **Action Plan**: Corrective and preventive actions defined with responsible parties
5. **Implementation**: Actions executed per target dates
6. **Verification**: Inspector confirms actions taken and finds resolved
7. **Closure**: PM or GC authorizes closure; CA logged and archived

---



## Quality Metrics & Performance Reporting

### Key Performance Indicators (KPIs)

#### 1. First-Pass Inspection Rate (FPIR)

**Definition**: Percentage of inspections that pass on first attempt without rework or correction.

**Formula**: (# inspections with no defects / total # inspections) × 100%

**Target**: >90% for well-managed projects

**Calculation Example**:
- Week ending 02/19: 23 inspections conducted
- Passed on first attempt: 21
- Required rework: 2
- FPIR = 21/23 = 91.3%

**Tracking**: Monitor weekly; trend toward 95%+

#### 2. Rework Rate

**Definition**: Total rework cost as percentage of project contract value.

**Formula**: (Cost of rework / Total contract value) × 100%

**Target**: <2.0% (benchmark: 4-5% for typical projects)

**Categories**:
- Design error rework: 0.3%
- Submittal revision rework: 0.5%
- Quality deficiency rework: 0.7%
- Change order rework: 0.8%

#### 3. Deficiency Density

**Definition**: Number of deficiencies per 1,000 square feet.

**Formula**: (Total deficiencies found / Building SF) × 1,000

**Target**: <5 deficiencies per 1,000 SF

**Example**: 9,980 SF building
- 30 deficiencies found in final walkdown
- Density = (30 / 9,980) × 1,000 = 3.0 per 1,000 SF ✓ ACCEPTABLE

#### 4. Quality Cost Index (QCI)

**Definition**: Total cost of quality (prevention + appraisal + failure) as % of contract value.

**Components**:
- **Prevention Cost** (10-15% of QCI): Inspection labor, testing, consulting, training
- **Appraisal Cost** (40-50% of QCI): Inspections, tests, documentation
- **Failure Cost** (35-50% of QCI): Rework, scrap, claims, delays

**Formula**: [(Prevention + Appraisal + Failure costs) / Total contract value] × 100%

**Target**: 3-5% (well-managed quality = lower failure costs offset by prevention/appraisal)

#### 5. Schedule Impact from Quality Issues

**Definition**: Days of schedule delay attributable to quality rework.

**Target**: Zero critical path delays; <2% float consumption

**Example**: If concrete cylinders fail strength test, cure extension + retest = 14-day delay; must be absorbed in float.

### Weekly Quality Scorecard Example

```json
{
  "quality_scorecard": {
    "week_ending": "2026-02-19",
    "reporting_period": "02/16 - 02/19",

    "kpis": {
      "fpir": {
        "value": 91.3,
        "unit": "%",
        "target": 90,
        "status": "green",
        "trend": "stable",
        "notes": "2 reinspections required (concrete cylinders, anchor bolt survey)"
      },
      "rework_rate": {
        "value": 0.45,
        "unit": "%",
        "target": 2.0,
        "status": "green",
        "trend": "improving",
        "notes": "Rework to date: $3,600 (supplemental cylinders, brief redesign)"
      },
      "deficiency_density": {
        "value": 0.0,
        "unit": "per 1000 SF",
        "target": 5,
        "status": "green",
        "trend": "na",
        "notes": "Phase 1 (foundation) - too early for punch-list deficiencies"
      },
      "qci": {
        "value": 2.3,
        "unit": "%",
        "target": 5.0,
        "status": "green",
        "trend": "good",
        "breakdown": {
          "prevention": 0.8,
          "appraisal": 1.2,
          "failure": 0.3
        }
      }
    },

    "quality_activities": {
      "inspections_conducted": 23,
      "inspections_passed_first_attempt": 21,
      "inspections_requiring_rework": 2,
      "hold_points_released": 2,
      "hold_points_pending": 3,
      "corrective_actions_open": 1,
      "corrective_actions_closed": 0
    },

    "trades_active": [
      "Foundation / Excavation (Walker)",
      "Concrete (W Principles self-perform)"
    ],

    "trade_quality_summary": [
      {
        "trade": "Concrete - Foundation",
        "inspections": 10,
        "pass_rate": 100,
        "deficiencies": 0,
        "status": "on_track"
      },
      {
        "trade": "Concrete - Stem Walls",
        "inspections": 8,
        "pass_rate": 87.5,
        "deficiencies": 1,
        "status": "needs_attention",
        "issue": "Test cylinders - CA-03-001 in progress"
      },
      {
        "trade": "Excavation / Sitework",
        "inspections": 5,
        "pass_rate": 100,
        "deficiencies": 0,
        "status": "on_track"
      }
    ],

    "top_deficiencies_this_week": [
      {
        "rank": 1,
        "description": "Missing test cylinders - footing pour 02/17",
        "severity": "major",
        "status": "corrective_action_in_progress",
        "ca_number": "CA-03-001"
      }
    ],

    "upcoming_hold_points": [
      {
        "hold_point_id": "HP-004",
        "activity": "Stem Wall Rebar Inspection",
        "scheduled_date": "2026-02-21",
        "witness": "Building Official",
        "status": "on_schedule"
      },
      {
        "hold_point_id": "HP-005",
        "activity": "Anchor Bolt Survey Verification",
        "scheduled_date": "2026-03-01",
        "witness": "Licensed Surveyor",
        "status": "on_schedule"
      }
    ],

    "quality_concerns": [
      {
        "concern": "Concrete test cylinder procedure needs reinforcement",
        "action": "Add to quality briefing; include supplier in pre-pour meeting",
        "owner": "Andrew Eberle",
        "target_date": "2026-02-21"
      }
    ],

    "recommendations": [
      "Continue strong FPIR trajectory; monitor for Phase 2 (PEMB erection)",
      "Ensure stem wall pour (02/23) includes full testing protocol per amended spec",
      "Brief Alexander Construction (PEMB erection) on quality expectations and hold points by 03/10"
    ],

    "reported_by": "Miles Goodman",
    "report_date": "2026-02-19",
    "approval": {
      "approved_by": "Andrew Eberle",
      "approval_date": ""
    }
  }
}
```

---



## Command Reference: /quality

### /quality checklist [trade] [phase]

Generate or display a three-phase inspection checklist for a specific trade.

**Syntax**:
```
/quality checklist concrete pre_installation
/quality checklist pemb installation
/quality checklist paint post_installation
```

**Output**: Populated checklist form ready for field inspector to complete. Links to specification sections and drawings automatically.

---

### /quality itp

Display the full Inspection and Test Plan master schedule. Filter by trade, date, or hold point status.

**Syntax**:
```
/quality itp
/quality itp --trade pemb --status pending
/quality itp --from 03/01 --to 03/31
/quality itp --hold-points-only
```

**Output**: Table or Gantt view of all inspections and hold points with witness requirements and acceptance criteria.

---

### /quality report

Generate comprehensive quality performance report by week, month, or project phase.

**Syntax**:
```
/quality report --week
/quality report --month
/quality report --phase foundation
/quality report --kpi-only
```

**Output**: Scorecard with FPIR, rework rate, deficiency density, QCI, and trend analysis. Exportable to PDF.

---

### /quality deficiency [add|update|close]

Manage deficiency items identified during inspection or punch-list.

**Syntax**:
```
/quality deficiency add --location "Grid C4 wall" --description "Gypsum board joint lippage at corner" --severity minor --trade drywall
/quality deficiency update CA-09-002 --status corrected_awaiting_verification
/quality deficiency close CA-09-002 --verified-by "Miles Goodman" --verification-date 2026-06-15
```

**Output**: Deficiency logged in QMS; triggers corrective action workflow if severity >minor.

---

### /quality metrics

Display current quality metrics with trend analysis.

**Syntax**:
```
/quality metrics
/quality metrics --fpir
/quality metrics --rework
/quality metrics --chart
```

**Output**: FPIR, rework rate, deficiency density, QCI with weekly/monthly trends and comparisons to target.

---



## Integration Points

### inspection-tracker

Quality checklists trigger hold-point inspections in the inspection-tracker system. Failed items create deficiency records automatically. When an HP is released, the next inspection phase is unlocked.

**Integration Example**:
- QC-03-001 (concrete pre-install) completed with hold point HP-003
- Inspector flags HP-003 as "Ready for Release" in quality checklist
- System notifies Nucor erection team and surveyor
- Surveyor releases HP-003 with transit survey
- QC-03-002 (concrete installation) checklist unlocked for pour day

### sub-performance

First-Pass Inspection Rate and rework metrics feed into the sub-performance scoring system. Quality dimension weights FPIR and deficiency density as key trade performance indicators.

**Integration Example**:
- Walker Construction excavation: FPIR 100% (score: 100 pts)
- W Principles concrete: FPIR 87.5% (score: 87.5 pts)
- Rework cost tracking: <0.5% contribution to quality score

### document-intelligence

Automatically extracts acceptance criteria from contract specifications and links them to inspection checklist items. When spec is updated via ASI, acceptance criteria refreshes in active checklists.

**Integration Example**:
- Spec says "Rebar cover min 2 inches, max 2.5 inches"
- System auto-populates checklist item with these values
- Inspector can verify against design requirement, not memorized spec

### daily-report-format

Quality observations logged in daily reports link to active quality checklists. When a concern is noted ("Concrete air looks high today"), it can be traced to QC-03-002 checklist for formal measurement and corrective action if needed.

### punch-list

Failed post-installation inspection items (Phase 3) are automatically converted to punch-list entries. Punch list is organized by CSI division and severity for efficient closeout execution.

**Integration Example**:
- QC-09-091-001 (paint post-install): Item 5 fails "Paint runs on east wall face"
- Automatically creates Punch Item PI-09-091-001
- Assigned to painter for rework; tracked to completion

### drawing-control

Each inspection checklist references current drawing revision. If a drawing is updated during construction, affected checklists are flagged for review and potential acceptance criteria updates.

### submittal-intelligence

Approved submittals (mix designs, equipment specs, material certs) provide the authoritative acceptance criteria for quality checklists. Submittals also trigger ITP entry updates with equipment-specific test requirements.

**Integration Example**:
- Submittal SUB-001 (Wells Concrete mix design) approved
- QC-03 checklists automatically updated with approved mix design numbers and slump/air target values
- Test cylinder strength target updated to 4000 PSI (interior)

---



## Rework Tracking Subsystem

Rework is construction's silent cost driver. The QMS tracks every rework item from cause through completion.

### Rework Item Structure

```json
{
  "rework_item": {
    "rework_id": "RW-09-001",
    "date_identified": "2026-06-15",
    "original_activity": "Gypsum board finishing (Phase 2)",
    "trade": "Drywall / CFS Framing (EKD)",

    "defect_description": {
      "location": "Grid C4, east wall, height 8 feet",
      "issue": "Drywall joint compound lippage at corner bead, 3/16 inch raised edge",
      "discovery_method": "Final L4 finish inspection (rake light)"
    },

    "root_cause": {
      "primary_cause": "Over-application of joint compound, insufficient sanding between coats",
      "contributing_factors": ["Foreman underestimated finish level requirement", "Wet weather delayed drying time"],
      "assigned_responsibility": "EKD finisher crew"
    },

    "rework_scope": {
      "description": "Sand corner bead area to flush surface, apply finish coat, sand final",
      "materials_required": ["Joint compound (0.5 bag)", "Sandpaper (220 grit)"],
      "labor_hours": 2.5,
      "cost_breakdown": {
        "labor": 250,
        "materials": 35,
        "equipment_rental": 0,
        "total": 285
      }
    },

    "schedule_impact": {
      "delay_days": 1,
      "impact_on_critical_path": false,
      "impact_reason": "Float available; does not delay finishes phase"
    },

    "execution": {
      "rework_start_date": "2026-06-16",
      "rework_completion_date": "2026-06-17",
      "completed_by": "EKD finisher crew",
      "status": "complete"
    },

    "verification": {
      "final_inspection": "Rake light inspection; surface uniform, no lippage",
      "verified_by": "Miles Goodman",
      "verification_date": "2026-06-18",
      "status": "accepted"
    },

    "prevention": {
      "action": "Add finish level (L3 vs L4) definition to pre-drywall briefing; clarify acceptance criteria for corner bead straightness"
    },

    "cost_coding": {
      "charged_to": "EKD contract allowance for rework",
      "cost_tracking": true
    }
  }
}
```

### Rework Pareto Analysis (Monthly)

**Example Report (June 2026)**

| Rank | Root Cause | Count | Cost | % of Total Rework | Action |
|------|-----------|-------|------|------------------|--------|
| 1 | Specification misunderstanding | 8 | $3,200 | 45% | Improve pre-work briefings; provide written spec summary to trades |
| 2 | Installation error / workmanship | 5 | $2,100 | 30% | Quality audit of EKD crew; increase inspection frequency |
| 3 | Material defect | 2 | $900 | 13% | Material QA review with supplier (Schiller) |
| 4 | Drawing coordination issue | 2 | $800 | 12% | RFI review process; improve constructability comments |
| **Total** | — | **17** | **$7,000** | **100%** | — |

**Analysis**: 45% of rework due to spec/communication gaps → Focus on prevention (training, briefings, written guidance).

---



## Best Practices for Construction Quality Management

### 1. Pre-Construction Quality Planning

**Timing**: Developed during contract negotiation and finalized before mobilization.

**Deliverables**:
- Project Quality Manual (defines QMS approach, responsibilities, standards)
- Inspection and Test Plan (all hold points and witness requirements)
- Specification Summary (one-page guide per major trade)
- Pre-work Quality Briefing schedule

**Responsibility**: PM in coordination with GC superintendent and architect.

### 2. Pre-Phase Quality Briefing

**Timing**: 3-5 days before major trade activity begins.

**Attendees**: Sub foreman, GC superintendent, PM, relevant trades (for coordination).

**Content**:
- Specification highlights (acceptance criteria)
- Drawings and details relevant to upcoming work
- Quality checklist walk-through
- Hold points and witness requirements
- Material staging and coordination

**Outcome**: Signed attendance sheet; all parties understand expectations.

### 3. Daily Quality Observation

**Process**: Superintendent conducts 15-min quality walk-down each morning during active work.

**Checklist Items**:
- Materials staged correctly
- Crew familiar with quality expectations
- Yesterday's work acceptable
- Environmental conditions (weather, temperature) suitable
- Upcoming work scope and quality plan understood

**Output**: Brief note in daily report; escalate any concerns immediately.

### 4. Real-Time Measurement & Testing

**Principle**: Catch problems before they become big rework.

**Examples**:
- Concrete slump tested per truck (not 1 per day)
- Rebar spacing verified before placing concrete
- Formwork bracing checked before placement
- Drywall joint compound sampled before final coat
- Paint mil thickness verified during application (not after)

### 5. Hold Point Release Protocol

**Sequence**:
1. Trade completes work to spec
2. Field inspector (GC super or PM) verifies via checklist
3. Witness (if required) inspects and approves
4. All sign checklist
5. Photo documentation filed
6. Next phase unlocked

**Key**: No release by GC alone if witness is specified in contract.

### 6. Deficiency Resolution Efficiency

**Target Response Times**:
- Critical: 24 hours
- Major: 2-3 business days
- Minor: 5 business days

**Process**:
- Identify → Log → Assign → Execute → Verify → Close
- Deficiency assigned to responsible trade (not GC)
- GC verifies completion before closing
- Punch-list deficiencies separated from in-phase rework

### 7. Quality Metrics Discipline

**Tracking**:
- FPIR weekly (not monthly)
- Rework costs monthly
- Deficiency density at each phase-end
- QCI calculated at project end

**Communication**: Include QMS data in weekly progress meetings and owner/architect reports.

### 8. Rework Prevention Investment

**Most Effective Prevention Spending** (in order of ROI):
1. Specification clarity and communication (briefings, written guides) — 5:1 ROI
2. Material testing and verification — 4:1 ROI
3. Enhanced inspection frequency (FPIR >95%) — 3:1 ROI
4. Coordination meetings (MEP / structural / finishes) — 3:1 ROI

**Least Effective** (high cost, low ROI): Rework remediation after final inspection.

### 9. Quality Documentation Discipline

**File Organization**:
- Checklists filed by CSI division
- Photos linked to checklist items
- Test reports with traceability (material → batch → location)
- Corrective actions with closure evidence
- As-built data verified before O&M handoff

**Retention**: All QMS documents retained per contract (typically 3-7 years post-completion).

### 10. Continuous Improvement Cycle

**Monthly Quality Review** (PM, Super, QC lead, sub reps):
- Review Pareto analysis of rework
- Identify top 3 process improvement opportunities
- Assign action items for next phase
- Update quality procedures if needed
- Communicate learnings to trade teams

**Example**: If rebar cover is consistently tight, hold a 15-min meeting with concrete crew to review cover measurement technique and tolerance band.

---



## Data Store: quality-data.json Schema

All quality information is stored in a single hierarchical JSON structure for integration across Foreman OS.

```json
{
  "quality_management": {
    "project_id": "MOSC-825021",
    "project_name": "Morehead One Senior Care",
    "qms_version": "1.0.0",
    "last_updated": "2026-02-19T16:30:00Z",

    "checklists": [
      { "checklist_id": "QC-03-001", "..." : "..." }
    ],

    "itp": [
      { "activity": "...", "hold_point": "HP-001", "..." : "..." }
    ],

    "corrective_actions": [
      { "ca_number": "CA-03-001", "..." : "..." }
    ],

    "rework_items": [
      { "rework_id": "RW-09-001", "..." : "..." }
    ],

    "quality_metrics": {
      "fpir_current": 91.3,
      "fpir_target": 90.0,
      "fpir_trend": "stable",

      "rework_rate_current": 0.45,
      "rework_rate_target": 2.0,
      "rework_cost_ytd": 3600,

      "deficiency_density_current": 0.0,
      "deficiency_density_target": 5.0,

      "qci_current": 2.3,
      "qci_target": 5.0,
      "qci_breakdown": {
        "prevention_cost": 0.8,
        "appraisal_cost": 1.2,
        "failure_cost": 0.3
      }
    }
  }
}
```

---



## Conclusion

The Quality Management System ensures that every aspect of construction—from foundation to finishes—meets specification and design intent. By combining three-phase inspections, rigorous hold-point management, real-time measurement, and disciplined deficiency tracking, the QMS minimizes rework, accelerates schedule, and delivers a building that exceeds owner expectations.

**Success Metrics**:
- FPIR >90% (target 95%)
- Rework rate <2% (target 1%)
- Zero code violations at final inspection
- Project completion on schedule
- Owner satisfaction with built quality

---

**End of SKILL.md**


