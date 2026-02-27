# Construction Document Intelligence - Extraction Rules

**COMPREHENSIVE EXTRACTION SYSTEM FOR CONSTRUCTION DOCUMENTS**

This system captures deep, field-actionable intelligence from construction documents. Every data point should serve these purposes:
1. Enable auto-completion in daily reports and project management
2. Validate field installations against design
3. Track progress, productivity, and schedule performance
4. Flag required inspections, hold points, and quality requirements
5. Support procurement, coordination, and cost tracking
6. Enable analytics and predictive project intelligence

---

## Table of Contents

### Foundational Reference (read first)
- **[Construction Document Conventions](construction-document-conventions.md)** - How drawings are organized, sheet numbering navigation, cross-reference symbols, scale/measurement, quantity calculation formulas, contour/grading/site work calculations, line types, hatch patterns, abbreviations

### Core Extraction Rules (this file)
- [Document Classification](#document-classification)
- [Extraction Principles](#extraction-principles)
- [Quality & Confidence](#quality-and-confidence)

### Specialized Deep-Dive References
- **[Plans & Drawings Deep Extraction](plans-deep-extraction.md)** - Complete schedules, specs, MEP systems
- **[Specifications Deep Extraction](specifications-deep-extraction.md)** - All CSI divisions with specific values
- **[Schedule Deep Extraction](schedule-deep-extraction.md)** - Sequencing logic, float, constraints, resources
- **[Civil & Site Deep Extraction](civil-deep-extraction.md)** - Utilities, grading, paving with exact values
- **[Compliance Deep Extraction](compliance-deep-extraction.md)** - Geotech, safety, SWPPP, inspections
- **[Project Documents Deep Extraction](project-docs-deep-extraction.md)** - Contracts, subs, RFIs, submittals, subcontracts, POs
- **[PEMB Deep Extraction](pemb-deep-extraction.md)** - Reactions, anchor bolts, framing, erection, panels, accessories
- **[Submittals Deep Extraction](submittals-deep-extraction.md)** - Mix designs, hardware, shop drawings, MEP equipment, finishes
- **[ASI Deep Extraction](asi-extraction.md)** - Architect's supplemental instructions, revised drawings, scope changes, impact assessment
- **[DXF Spatial Extraction](dxf-extraction.md)** - CAD geometry, blocks, hatches, dimensions, material areas (parse_dxf.py)
- **[Visual Plan Analysis](visual-extraction-reference.md)** - OCR, line/wall detection, symbols, material zones, dimensions, scale (visual_plan_analyzer.py)
- **[Material Testing Reports Deep Extraction](material-testing-extraction.md)** - Concrete compression, steel MTRs, soil compaction, welding inspection, special inspections
- **[Warranty Documentation Deep Extraction](warranty-documentation-extraction.md)** - Equipment warranties, material warranties, workmanship warranties, performance guarantees
- **[As-Built Drawings Deep Extraction](as-built-extraction.md)** - As-built drawing sets, record drawings, red-line markups, field measurement notations
- **[Testing & Commissioning Deep Extraction](testing-and-commissioning-extraction.md)** - HVAC TAB reports, fire protection tests, electrical tests, generator load tests, plumbing pressure tests
- **[O&M Manuals Deep Extraction](o-and-m-manual-extraction.md)** - Equipment O&M manuals, system operation manuals, maintenance procedures, parts catalogs
- **[Fire Protection Deep Extraction](fp-deep-extraction.md)** - Sprinkler systems, fire alarm, riser diagrams, fire rated assemblies, FDC, NFPA 13 compliance, firestopping

---

## Document Classification

### Pass 0: File Type Detection

Before any content analysis, check the file extension:

| Extension | Action | Reference |
|-----------|--------|-----------|
| .dxf | **Direct DXF extraction** — run `parse_dxf.py` for exact spatial data (coordinates, blocks, hatches, dimensions). DXF data takes priority over PDF-estimated values. | [dxf-extraction.md](dxf-extraction.md) |
| .dwg | **Attempt conversion** — run `convert_dwg.py` which uses ODA File Converter to produce .dxf, then extracts. If ODA is not available, prompt user to request .dxf export from architect. | [dxf-extraction.md](dxf-extraction.md) |
| .ifc | **FUTURE** — IFC/BIM extraction not yet implemented. Document and note for future support. | [dxf-extraction.md](dxf-extraction.md) |
| .pdf | Continue to Pass 1 below for PDF-based extraction. | This file |
| .xlsx, .xls, .csv | Tabular data — likely schedule, sub list, RFI log, or submittal log. | [project-docs-deep-extraction.md](project-docs-deep-extraction.md) |
| .docx, .doc | Document — likely spec, contract, minutes, or report. | [specifications-deep-extraction.md](specifications-deep-extraction.md) or [project-docs-deep-extraction.md](project-docs-deep-extraction.md) |

### Pass 1: Metadata Extraction

Extract PDF metadata programmatically before reading content:
- Title, Author, Subject, Keywords (PDF properties)
- Creator application (strong signal for document type)
- Creation/modification dates
- Page count and dimensions
- File size

**Creator Application Signals:**

| Creator | Likely Type | Confidence |
|---------|-------------|------------|
| AutoCAD, Revit, Bluebeam | Plans/Drawings | High |
| Primavera P6, MS Project, Asta | Schedule | High |
| Microsoft Word | Spec, contract, minutes | Medium |
| Microsoft Excel | Sub list, logs, bid tab | Medium |
| Adobe InDesign | Spec book, manual | High |

### Pass 2: Structural Analysis

Scan for structural patterns that confirm document type:

**Sheet Index / Drawing List:**
- Extract all sheet numbers and titles
- Sheet prefixes indicate discipline:

| Prefix | Discipline | Extract |
|--------|-----------|---------|
| G | General | Cover, code, life safety |
| C | Civil | Site, grading, utilities |
| L | Landscape | Planting, irrigation, hardscape |
| A | Architectural | Floor plans, rooms, finishes, doors, windows |
| S | Structural | Grid, foundation, framing, details |
| M | Mechanical | HVAC, plumbing, equipment |
| E | Electrical | Power, lighting, panels |
| P | Plumbing | Fixtures, systems, fire protection |
| FP | Fire Protection | Sprinklers, standpipes, FDC |

**Table of Contents (Specs):**
- Extract all CSI division/section numbers and titles
- Maps full scope without deep-reading every section

**Headers & Footers:**
- Project name, number, date, revision
- Cross-reference with project basics

**Tables:**
- Detect tabular data (sub lists, schedules, logs)
- Parse column headers before extracting rows

### Pass 3: Content Extraction

Based on document type from Passes 1-2, extract specific intelligence following the specialized deep-dive references.

**Content Signals for Classification:**

| Signal | Type |
|--------|------|
| Grid lines, elevation callouts, scale bars, north arrow | Plans |
| CSI numbers, "PART 1 - GENERAL", "PART 2 - PRODUCTS" | Specifications |
| Activity IDs, durations, predecessor/successor | Schedule |
| "AGREEMENT", "CONTRACT", articles/sections | Contract |
| Company names + trade/scope columns | Sub list |
| RFI numbers, status, response dates | RFI log |
| Submittal numbers, spec sections, review status | Submittal log |
| "MEETING MINUTES", attendees, action items | Minutes |
| Bearing capacity, boring logs, water table | Geotech |
| BMP locations, SWPPP, erosion control | Environmental |
| Fall protection, confined space, hot work | Safety |
| Column reactions, anchor bolt layout, eave height, bay spacing, Nucor/BlueScope/VP letterhead | PEMB Reaction Drawing |
| Mix ID, f'c, w/c ratio, slump, air content, cement content, aggregate, lab letterhead | Concrete Mix Design |
| Hardware set numbers (HW-1), cut sheets with product images, keying schedule, Div 08 71 00 | Hardware Submittal |
| "SUBCONTRACT AGREEMENT", scope exhibit, retainage, signature pages, insurance exhibit | Executed Subcontract |
| "PURCHASE ORDER", PO number, line items with quantities/prices, delivery dates, shipping terms | Purchase Order |
| "ASI", "Architect's Supplemental Instruction", cover sheet, affected drawings list, superseded drawings | ASI / Supplemental Instruction |
| "compressive strength", "ASTM C39", "mill certificate", "MTR", "compaction report", "proctor", "nuclear gauge", "soil density", "welding inspection", "NDT", "special inspection" | Material Testing Report |
| "WARRANTY", "GUARANTEE", "CERTIFICATE OF WARRANTY", warranty duration language, exclusions sections, claim procedures, registration forms | Warranty Documentation |
| "AS-BUILT", "RECORD DRAWING", "AS-CONSTRUCTED", red-line markups, cloud/revision marks, field measurement notations | As-Built Drawings |
| "TAB report", "air balance", "hydrostatic test", "megger test", "insulation resistance", "generator load test", "pressure test", "commissioning", "functional performance test" | Testing & Commissioning |
| "Operation and Maintenance", "O&M Manual", "maintenance schedule", "preventive maintenance", "parts list", "troubleshooting", "sequence of operation", "emergency procedures" | O&M Manual |
| "NFPA 13", "sprinkler", "fire alarm", "fire protection", "fire rated", "FDC", "riser diagram", "fire damper", "smoke damper", "hydrostatic test", "fire alarm control panel" | Fire Protection |

---

## Extraction Principles

### Depth vs. Breadth

**When to Extract Deep:**
- Documents actively used in field (plans, specs, schedule)
- Data with specific measurable values (PSI, elevations, dimensions)
- Compliance requirements (hold points, testing frequencies)
- Coordination data (grid lines, room numbers, equipment marks)

**When to Extract Broad:**
- Reference documents (minutes, correspondence)
- Historical data (old RFIs, closed submittals)
- Descriptive content without actionable values

### Extract for Purpose

Every extraction should answer one of these questions:

**Daily Reporting:**
- "Formed and poured footings at Grids C-D, 3-4" → Need grid lines
- "Installed VCT in Room 107" → Need room schedule and finish schedule
- "Alexander Construction erected PEMB columns" → Need sub directory
- "Ambient temp 45°F (above 40°F threshold)" → Need weather thresholds

**Field Verification:**
- "Is this 4,000 PSI concrete correct?" → Need concrete specs
- "Are these #5 bars at 12\" o.c. right?" → Need rebar details
- "Does this panel location match the drawings?" → Need electrical panel schedule

**Progress Tracking:**
- "Completed Room 101-105 drywall (5 of 47 rooms)" → Need complete room count
- "PEMB dried-in milestone achieved (3 days ahead)" → Need milestone dates
- "SOG curing day 5 of 7" → Need curing duration requirement

**Procurement & Coordination:**
- "RTU-3 delivery delayed, impacts schedule" → Need equipment schedule with lead times
- "Awaiting door hardware submittal approval" → Need submittal log
- "Wells Concrete 12 CY delivered" → Need sub contact info

### Confidence Levels

Assign confidence to every extraction:

- **High**: Explicit and unambiguous (e.g., "4,000 PSI" in note)
- **Medium**: Inferred from context but reasonable (e.g., grid spacing calculated from dimensions)
- **Low**: Assumed based on typical practice (e.g., "likely 95% compaction" - not stated)
- **Vision Required**: Content needs image analysis (north arrow graphic, color-coded MEP)

**Flag low-confidence extractions** for user verification.

### Progressive Disclosure

Extract in layers:

1. **Always extract**: Core spatial framework (grids, floors, building areas)
2. **Extract when present**: Schedules, equipment lists, detailed specs
3. **Extract on demand**: Supporting details, historical data, reference info

### Cross-Referencing

Link extracted data across documents:

- Room 107 (floor plan) → VCT flooring (finish schedule) → Spec 09 65 00
- Grid C-3 footing (foundation plan) → 4,500 PSI concrete (structural notes) → Spec 03 30 00
- PEMB erection (schedule) → Alexander Construction (sub list) → SC-825021-06 (contract)

### Merge Strategy — Append-Only

When extracting data that may overlap with existing records:
- **Never overwrite** existing data with new extraction results
- **Append new records** alongside existing ones
- **Flag conflicts** when new data contradicts existing data (log to `action-items.json` for PM review)
- **Preserve provenance**: Every record tracks its source document, page, and extraction phase
- Old data preserved with `"superseded_by"` reference when revised documents arrive
- PM confirms before old data is archived

This prevents data loss from re-extraction and ensures human review of discrepancies.

---

## Quality and Confidence

### Explicit vs. Inferred Data

**Prefer explicit** over inferred:
- Explicit: Grid line labeled "A" on drawing
- Inferred: Grid line position suggests "A" (flag as medium confidence)

### Coverage Tracking

For each document processed, track:

```json
{
  "populated": ["grid_lines", "floor_levels", "hold_points"],
  "empty": ["room_schedule", "MEP_equipment"],
  "needs_vision": ["compass_orientation", "color_coded_zones"],
  "low_confidence": ["compaction_density (assumed typical)"]
}
```

### Extraction Completeness

Target completeness varies by document type:

**Plans:**
- Grid lines: 100% (critical for spatial reference)
- Room schedule: 100% (all rooms for progress tracking)
- Door schedule: 100% (procurement and coordination)
- Finishes: 100% if present (room-by-room tracking)
- Structural notes: Extract all specific values (PSI, rebar sizes, embedments)
- MEP equipment: Extract all if schedules present

**Schedule:**
- Milestones: 100%
- Critical path: 100%
- All activities: Extract key data (ID, name, dates, duration, float)
- Sequencing: Extract for critical and near-critical activities

**Specifications:**
- Active sections: 100% (CSI divisions used on project)
- Deep-read priority sections: Division 01, 03, 05, 07, plus trade-specific
- Extract specific measurable values (not just "per spec")

---

## Integration with Project Management

Extracted intelligence feeds multiple systems:

### Daily Reports
- Auto-complete location references (grids, rooms, areas)
- Verify sub names and spell correctly
- Flag weather threshold conflicts
- Track milestone progress
- Reference spec sections and hold points

### Project Dashboards
- Phase completion percentages (rooms, floors, systems)
- Schedule health (critical path, float consumption)
- Procurement status (equipment delivery, submittal approval)
- Quality metrics (test results, inspection pass rates)

### Predictive Analytics
- Resource loading and site congestion prediction
- Weather impact forecasting (weather-sensitive activities)
- Procurement risk assessment (long-lead items)
- Cost variance trends

---

## Multi-Document Processing

When processing multiple documents at once:

1. **Classify all first** (Pass 1 + 2 for each)
2. **Present to user**: "I see structural drawings, a spec book, and a CPM schedule. Sound right?"
3. **Process in priority order** (earlier provides context for later):
   - Plans/drawings first (spatial framework)
   - Specs second (adds material/quality to spatial framework)
   - Schedule third (adds time dimension)
   - Contract fourth (adds constraints)
   - Sub list fifth (adds personnel)
   - Support docs last (RFIs, submittals, minutes)

---

## Extraction Output Format

Structure extraction results for consumption by project-data storage:

```json
{
  "document": {
    "filename": "One Senior Care Conformance Set 01.22.26.pdf",
    "type": "plans",
    "discipline": "multi-discipline",
    "metadata": {
      "creator": "Bluebeam Revu",
      "created": "2026-01-16",
      "modified": "2026-01-16",
      "pages": 50,
      "title": "Conformance Set"
    }
  },
  "extracted": {
    "grid_lines": {
      "columns": ["1", "2", "3", "4", "5", "6"],
      "rows": ["A", "B", "C", "D", "E", "F", "G", "H"],
      "spacing": "Variable typical for PEMB",
      "notes": "Rectangular grid layout"
    },
    "building_areas": [...],
    "floor_levels": [...],
    "room_schedule": [...],
    "finish_schedule": [...],
    "door_schedule": [...],
    "window_schedule": [...],
    "mep_equipment": [...],
    "structural_specs": {...},
    "hold_points": [...],
    "weather_thresholds": [...]
  },
  "coverage": {
    "populated": ["grid_lines", "room_schedule", "structural_specs"],
    "empty": ["submittal_log"],
    "needs_vision": ["north_arrow_graphic"],
    "low_confidence": []
  },
  "confidence": "high"
}
```

---

## Using the Specialized References

This file provides the framework. For detailed extraction rules by category, see:

### [Plans & Drawings Deep Extraction](plans-deep-extraction.md)
**When to use**: Processing architectural, structural, civil, MEP, or landscape drawings

**Contains**:
- Complete room schedules (all 50+ rooms with numbers, names, sizes, departments)
- Finish schedules (floor, wall, base, ceiling by room with manufacturers and colors)
- Door schedules (all doors with sizes, types, fire ratings, hardware groups)
- Window schedules (types, sizes, glazing, U-values)
- MEP equipment schedules (HVAC units, electrical panels, plumbing fixtures, lighting)
- Structural general notes (exact concrete PSI, rebar grades, steel specs, embedments, tolerances)
- Site layout with coordinates (laydown areas, trailers, crane pads, parking counts)

### [Specifications Deep Extraction](specifications-deep-extraction.md)
**When to use**: Processing spec books or individual spec sections

**Contains**:
- Division 01 (working hours, submittal procedures, quality control, closeout)
- Division 03 (concrete mixes with exact PSI, w/c ratio, slump, air content, weather thresholds)
- Division 05 (steel grades, bolt torque, weld specs, fireproofing thickness)
- Division 06-09 (wood, insulation, roofing, finishes with specific products and R-values)
- Division 21-28 (MEP systems with sizing and performance criteria)
- All divisions (testing frequencies, hold/witness points, tolerances with numbers)

### [Schedule Deep Extraction](schedule-deep-extraction.md)
**When to use**: Processing CPM schedules (P6, MS Project, Asta)

**Contains**:
- Activity-level data (ID, name, duration, start, finish, float, calendars)
- Predecessor/successor relationships (FS, SS, FF, SF with lags)
- Critical path identification (activities with zero float)
- Near-critical activities (float < 5 days)
- Constraints (SNET, SNLT, MSO, MFO)
- Work breakdown structure (WBS) and activity codes
- Resource loading (crew sizes, equipment, materials)
- Baseline vs. current comparison (variance tracking)
- Weather-sensitive activity identification

### [Civil & Site Deep Extraction](civil-deep-extraction.md)
**When to use**: Processing civil/site drawings or site plans

**Contains**:
- Site layout with exact coordinates (laydown, trailers, crane pads, parking)
- Grading with spot elevations (FFE, corners, entries, slopes)
- Storm drainage (pipe sizes, slopes, invert elevations IN/OUT, rim elevations)
- Sanitary sewer (sizes, slopes, inverts, manhole rims, tie-in points)
- Water system (sizes, meter location, backflow preventer, hydrants, fire service)
- Paving sections (asphalt thickness, base course, subgrade compaction)
- Striping layout (counts, widths, types, ADA compliance)
- Landscaping (species, quantities, sizes)

### [Compliance Deep Extraction](compliance-deep-extraction.md)
**When to use**: Processing geotech reports, safety plans, SWPPP, inspection docs

**Contains**:
- Geotechnical (bearing capacity PSF, water table depth, frost depth, compaction density %, lift thickness, testing frequency)
- Safety (fall protection heights, confined spaces, hot work areas, crane exclusions, PPE by zone, competent persons)
- SWPPP (permit number, BMP locations with coordinates, rainfall threshold, inspection frequency, corrective action timeline)
- Special inspections (hold vs. witness points, testing frequencies with numbers, inspector qualifications)

### [Project Documents Deep Extraction](project-docs-deep-extraction.md)
**When to use**: Processing contracts, sub lists, RFI logs, submittal logs, meeting minutes, executed subcontracts, purchase orders

**Contains**:
- Contract terms (NTP, completion dates, liquidated damages $/day, working hours, noise limits)
- Subcontractor details (company, trade, scope, foreman, phone, email, contract value, dates)
- RFI tracking (number, date, subject, drawing/spec ref, blocking work flag, status, response)
- Submittal tracking (number, section, type, dates, status, lead time, critical path flag)
- Meeting minutes (action items, owner directives, design decisions, coordination issues)
- Executed subcontracts (scope inclusions/exclusions, value, retainage, insurance, key clauses)
- Purchase orders (PO number, line items, quantities, prices, delivery dates, certifications)

### [PEMB Deep Extraction](pemb-deep-extraction.md)
**When to use**: Processing PEMB manufacturer documents (Nucor, BlueScope, VP, Metallic Building Co.)

**Contains**:
- Building envelope (width, length, bay spacing, eave height, roof slope, ridge height)
- Column reactions by grid (vertical, horizontal, moment, uplift, all load cases)
- Primary framing (rigid frame type, profiles, splice locations, knee connections)
- Secondary framing (purlin/girt type, size, gauge, spacing by zone, lap lengths)
- Anchor bolt layout per column (diameter, embedment, projection, pattern, grade, template)
- Erection sequence (crane requirements, bracing sequence, safety, wind limits)
- Connection details (moment, ridge, base plate — bolt sizes, grades, torque)
- Wall/roof panels (type, profile, gauge, color, insulation R-value, fastening)
- Accessories (gutters, downspouts, trim, openings, ventilation)
- Design codes and loads (IBC, ASCE 7, wind speed, seismic, snow)
- QC checkpoints (anchor bolt tolerance, column plumb, bracing, panel overlap)

### [Submittals Deep Extraction](submittals-deep-extraction.md)
**When to use**: Processing submittal packages (product data, mix designs, cut sheets, shop drawings)

**Contains**:
- Concrete mix designs (mix ID, f'c, w/c, slump, air, cement, aggregates, admixtures, weather mixes)
- Door hardware submittals (hardware sets, items per set, manufacturer/model, finish, keying, ADA)
- Structural steel shop drawings (piece marks, sizes, connections, camber, bill of materials)
- MEP equipment submittals (HVAC units, electrical panels, plumbing fixtures, fire protection)
- Finish material submittals (flooring, paint, ceiling — products, colors, performance data)
- Waterproofing/roofing submittals (system, warranty, installation requirements)
- Spec compliance verification (manufacturer approval, performance criteria, fire rating, ADA)

### [ASI (Architect's Supplemental Instruction) Deep Extraction](asi-extraction.md)
**When to use**: Processing Architect's Supplemental Instructions, change directives, and revised drawings

**Contains**:
- ASI cover sheet parsing (ASI number, date issued, description, issuing architect)
- Affected drawing sheet list (original sheets superseded or modified)
- Affected spec sections (specifications clarified or changed)
- Scope change classification (additive, deductive, clarification-only)
- Revised drawing comparison (what changed between original and ASI revision)
- Impact assessment (schedule, cost, submittal revisions needed, procurement changes, inspection points)
- Cross-reference integration (updated plans-spatial.json if dimensions/layouts changed, flag affected submittals, update change order tracking)

### [DXF Spatial Extraction](dxf-extraction.md)
**When to use**: Processing .dxf or .dwg CAD files (direct geometry extraction)

**Contains**:
- Layer mapping (AIA standard prefixes → disciplines: A-, S-, M-, E-, P-, F-, C-)
- Block attribute extraction (doors, rooms, equipment, fixtures — structured key-value data)
- Hatch pattern → material mapping (AR-CONC, DOTS, CROSS, INSUL, etc. → concrete, VCT, tile, insulation)
- Closed polyline area/perimeter calculation (room boundaries, building footprint, paving)
- Dimension entity extraction (measured values with reference points)
- Text extraction with locations
- Material area aggregation (total SF by material type from hatches)
- parse_dxf.py pipeline script (ezdxf-based, outputs JSON)
- convert_dwg.py wrapper (.dwg → .dxf via ODA File Converter, or user prompt for .dxf export)
- DXF vs. PDF data priority rules (DXF takes precedence for spatial data)
- Cross-reference guidance (match DXF blocks against PDF-extracted schedules)

### [ASI (Architect's Supplemental Instruction) Deep Extraction](asi-extraction.md)
**When to use**: Processing Architect's Supplemental Instructions, change directives, and document revisions

**Contains**:
- ASI cover sheet parsing (ASI number, date issued, description, list of affected sheets)
- Revised drawing comparison (what changed between original and ASI revision)
- Scope change identification (additive, deductive, clarification only)
- Impact assessment checklist (schedule, cost, submittals, procurement, inspections)
- Cross-referencing with existing project intelligence to flag cascading impacts
- Integration with change order tracking
- Submittal impact flagging (which submittals may need revision)
- Procurement impact flagging (which material orders affected)
- Schedule impact analysis (does change affect critical path?)

### [Visual Plan Analysis](visual-extraction-reference.md)
**When to use**: Processing plan sheet PDFs as images (complements text-based extraction)

**Visual extraction method priority:**
1. **Claude Vision (primary)** — Always available, no dependencies. Render page to 300 DPI PNG via PyMuPDF, then analyze with Claude's native multimodal capability. Handles room labels, dimensions, symbols, material zones, notes, and spatial relationships in a single pass.
2. **Tesseract OCR (supplement)** — Use alongside Claude Vision for small text that benefits from dedicated OCR (fine-print notes, dense dimension strings, title block fields).
3. **Python CV pipeline (optional enhancement)** — `visual_plan_analyzer.py` with OpenCV for precise coordinate extraction, line detection, and material zone quantification. Not required for standard extraction; use when exact pixel coordinates or automated area calculations are needed.

**Contains**:
- Claude Vision analysis checklist (layout, text, symbols, materials, dimensions, scale, cross-references)
- Tesseract OCR for supplemental small-text extraction
- Optional Python CV pipeline (OpenCV line detection, symbol recognition, material zone texture analysis)
- Scale calibration (graphic scale bars and text-format scales like 1/4" = 1'-0")
- Accuracy expectations by extraction type (OCR 85-95%, walls 80-90%, symbols 70-85%)
- Integration rules: merge visual results with text/DXF data, source attribution, conflict resolution
- symbol_templates/ directory for template matching customization

### [Material Testing Reports Deep Extraction](material-testing-extraction.md)
**When to use**: Processing concrete compression test reports, steel mill test reports (MTRs), soil compaction test reports, third-party inspection certificates, welding inspection reports

**Contains**:
- Concrete compression test parsing (ASTM C39 results, f'c values, break dates, cylinder IDs, age at break, cure method, lab certification)
- Steel mill test reports / MTRs (heat numbers, chemical composition, tensile/yield strength, elongation, Charpy impact, specification compliance)
- Soil compaction test reports (proctor results, in-place density, nuclear gauge readings, moisture content, percent compaction, lift number, test location)
- Welding inspection reports (NDT method, weld joint ID, pass/fail, defect type, inspector certification, WPS/PQR reference)
- Special inspection certificates (inspection type, code reference, inspector name/cert number, results, conformance statement)
- Cross-reference integration (link test results to spec requirements in specs-quality.json, flag failures against spec thresholds, tie to grid/location in plans-spatial.json)

### [Warranty Documentation Deep Extraction](warranty-documentation-extraction.md)
**When to use**: Processing manufacturer equipment warranties, material warranties, workmanship warranties, roofing/waterproofing system warranties, performance guarantees

**Contains**:
- Warranty identification parsing (warranty type, warrantor, project name, effective date, expiration date, duration)
- Coverage scope extraction (covered components, covered defects, performance criteria, coverage limits)
- Exclusion parsing (excluded conditions, excluded uses, maintenance requirements for warranty validity, environmental limitations)
- Claim procedures (notification requirements, time limits for claims, required documentation, contact information, claim submission process)
- Registration requirements (registration deadlines, required forms, installation certification, commissioning documentation)
- Cross-reference integration (link warranties to equipment in plans-spatial.json, tie to spec sections in specs-quality.json, flag expiration dates for closeout tracking)

### [As-Built Drawings Deep Extraction](as-built-extraction.md)
**When to use**: Processing as-built drawing sets, record drawings, red-line markups

**Contains**:
- As-built identification parsing (sheet number, discipline, revision date, marked-up-by, original drawing reference)
- Red-line markup extraction (change type — addition/deletion/relocation, affected element, new dimensions/locations, markup color coding)
- Cloud and revision mark detection (revision number, revision date, description of change, affected area/grid reference)
- Field measurement notations (actual vs. design dimensions, field-verified elevations, as-installed equipment locations)
- Deviation tracking (design vs. as-built comparison, dimensional variances, relocated element mapping)
- Cross-reference integration (update plans-spatial.json with as-built dimensions, flag deviations from original design, link to RFIs/ASIs that drove changes via rfi-log and drawing-log)

### [Testing & Commissioning Deep Extraction](testing-and-commissioning-extraction.md)
**When to use**: Processing HVAC TAB reports, fire protection test reports, electrical test reports, generator load bank tests, plumbing pressure tests, building envelope tests

**Contains**:
- HVAC TAB report parsing (air balance data — design CFM vs. actual CFM, water balance — design GPM vs. actual GPM, terminal unit readings, duct static pressures, fan performance curves)
- Fire protection test reports (hydrostatic test pressures, flow test results, alarm/supervisory device tests, trip test results, inspection certificates)
- Electrical test reports (megger/insulation resistance readings, ground fault impedance, breaker trip tests, protective relay settings, power quality measurements)
- Generator load bank tests (load steps, voltage/frequency stability, transfer switch operation, run time, fuel consumption, governor response)
- Plumbing pressure tests (test pressure, duration, medium, pass/fail, system identification, witness signature)
- Building envelope tests (air infiltration, water penetration, thermal imaging results, window/curtain wall test reports)
- Cross-reference integration (link test results to equipment in plans-spatial.json, verify against spec performance criteria in specs-quality.json, flag deficiencies for punch-list tracking, tie to commissioning milestones in schedule.json)

### [O&M Manuals Deep Extraction](o-and-m-manual-extraction.md)
**When to use**: Processing equipment O&M manuals, system operation manuals, maintenance procedure documents, parts catalogs

**Contains**:
- Equipment identification parsing (manufacturer, model number, serial number, installation date, location, serving area, spec section reference)
- Operating procedures extraction (startup sequence, normal operation, shutdown sequence, emergency procedures, seasonal changeover)
- Maintenance schedule parsing (preventive maintenance tasks, frequency/intervals, required parts, estimated duration, skill level required)
- Parts list extraction (part numbers, descriptions, quantities, suppliers, lead times, recommended spares inventory)
- Troubleshooting guide parsing (symptom, probable cause, corrective action, required tools, safety precautions)
- Sequence of operation extraction (control logic, setpoints, interlocks, alarm conditions, override procedures)
- Warranty cross-reference (link to warranty-documentation-extraction.md for warranty terms affecting maintenance requirements)
- Cross-reference integration (link equipment to plans-spatial.json locations, tie maintenance requirements to specs-quality.json, flag critical spares for procurement tracking, associate with closeout documentation requirements)

### [Fire Protection Deep Extraction](fp-deep-extraction.md)
**When to use**: Processing fire protection drawings (FP sheets), sprinkler plans, fire alarm plans, riser diagrams, fire rated assembly schedules, Division 21/28 specifications

**Contains**:
- Sprinkler system identification (wet, dry, pre-action, deluge per zone, hazard classification)
- Sprinkler head schedule (type, temperature rating, K-factor, coverage area, finish, quantity by floor)
- Pipe sizing and material (mains, cross-mains, branch lines, risers — black steel, CPVC, thin-wall)
- Riser and valve extraction (riser locations, FCA per floor, OS&Y valves, alarm check/dry pipe valves)
- Fire department connection (FDC location, type — Siamese/Storz, systems served, signage, hydrant proximity)
- Fire rated assembly schedules (wall ratings with UL design numbers, floor/ceiling ratings, construction details)
- Penetration firestopping (UL system numbers, penetrant types, sealant/device, manufacturer)
- Fire damper and smoke damper locations and ratings
- Fire alarm system (FACP location/model, initiating device counts by type and floor, notification appliance counts, addressable vs. conventional)
- NFPA 13 spacing compliance checks (standard spray, extended coverage, obstruction rules, storage requirements)
- Testing and inspection hold points (hydrostatic test 200 PSI/2 hr, trip test, alarm verification, fire alarm acceptance, rough-in, firestopping)
- Cross-reference integration (link to quality-data.json for FP inspections, plans-spatial.json for system layout, specs-quality.json for hold points and thresholds)

---

## Extraction Workflow — 5-Phase Adaptive Model

Extraction follows a 5-phase pipeline. Each phase has distinct entry/exit criteria and validation gates.

### Phase 1 — Index & Classify
- Title blocks, sheet index, document classification, dependency graph
- Lightweight processing (text only)
- **Validation**: Schema validation only

### Phase 2 — Extract
- Structured data extraction, adaptive intensity per page (2-6 passes based on content density)
- Inline gleaning + batch consistency validation
- Tentative entity IDs assigned (finalized in Phase 3)
- **Validation**: Inline gleaning + batch consistency

### Phase 3 — Cross-Reference
- Entity resolution (tentative IDs → canonical IDs), bidirectional linking, reference graph validation
- Medium intensity (LLM-assisted comparison across documents)
- **Validation**: Reference integrity + entity consistency

### Phase 4 — Remediate
- Targeted re-extraction of items flagged by Phase 2-3 validation
- Only flagged items are reprocessed (not full re-extraction)
- **Validation**: Before/after comparison

### Phase 5 — Normalize
- N1-N8 normalization patterns via `/data-health fix`, computed fields, final confidence scoring
- Deterministic (scripted, no LLM required)
- **Validation**: Full-corpus consistency

> **Reference**: `commands/process-docs.md` Step 3 for complete phase definitions, entry/exit criteria, and processing refinements.

---

## Notes for Other Plugins

This extraction system is designed to be modular and reusable across different construction management plugins:

- **Daily Reports**: Focuses on field-actionable data for report generation
- **Project Management**: Emphasizes schedule, cost, and resource tracking
- **Quality Control**: Prioritizes specs, testing, and inspection requirements
- **Procurement**: Highlights equipment schedules, submittal status, long-lead items
- **Cost Management**: Extracts quantities, contract values, change order impacts

Each plugin can use the full extraction system or subset based on needs. The specialized reference files are organized by domain for easy selective use.

---

## ENHANCED VALIDATION RULES

### V-DIM: Dimension Chain Validation
- **Rule**: For every dimension string chain, sum individual dimensions and compare to overall
- **Tolerance**: ±1" for architectural, ±1/8" for structural
- **Action**: Flag `DIMENSION_MISMATCH` with chain location, individual values, sum, overall value, and difference
- **Priority**: HIGH — dimension errors cause field layout problems

### V-KEY: Keynote Orphan Detection
- **Rule**: Every keynote bubble number visible on a drawing must have a corresponding entry in the keynote legend/schedule
- **Action**: Flag `ORPHAN_KEYNOTE` with bubble number, location on drawing, and which keynote legend was checked
- **Priority**: MEDIUM — orphan keynotes leave field crews without installation guidance

### V-SCHED: Schedule Completeness
- **Rule**: Every tag visible on plan drawings (door marks, window marks, equipment tags, wall type tags) must have a corresponding entry in the relevant schedule
- **Action**: Flag `ORPHAN_TAG` with tag value, tag type (door/window/equipment/wall), and location
- **Priority**: HIGH — missing schedule entries mean incomplete specification

### V-RCP: RCP vs. Finish Schedule Conflict
- **Rule**: Ceiling height shown on RCP must match ceiling height in finish schedule for the same room
- **Tolerance**: Exact match required
- **Action**: Flag `CEILING_HEIGHT_MISMATCH` with room number, RCP height, finish schedule height
- **Priority**: HIGH — ceiling height conflicts affect MEP coordination and material ordering

### V-FIX: Fixture Count Verification
- **Rule**: Count of fixture type marks on RCP/floor plan should match total quantity in fixture schedule
- **Tolerance**: Exact match
- **Action**: Flag `FIXTURE_COUNT_MISMATCH` with fixture type, plan count, schedule count
- **Priority**: MEDIUM — count mismatches affect procurement quantities

### V-FIRE: Fire-Rated Assembly Validation
- **Rule**: Every opening in a fire-rated wall must have a fire-rated door/window assembly
- **Rule**: Fire door rating must be ≤ wall rating − 45 minutes (standard rule: 3/4 of wall rating)
- **Rule**: Every HVAC penetration through a rated wall must have a fire damper
- **Action**: Flag `FIRE_RATING_VIOLATION` with wall type, location, and specific violation
- **Priority**: CRITICAL — fire rating violations are code violations

### V-ADA: Accessibility Compliance
- **Rule**: At least one accessible route must connect: parking → building entry → all public/common areas → accessible restrooms
- **Rule**: Accessible restroom clearances must meet ADA minimums (60" turning radius, grab bars at correct heights)
- **Action**: Flag `ADA_VIOLATION` with specific requirement and location
- **Priority**: HIGH — ADA violations are code violations requiring remediation
