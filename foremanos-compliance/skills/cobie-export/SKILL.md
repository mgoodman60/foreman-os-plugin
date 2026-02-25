---
name: cobie-export
description: >
  Generate Construction Operations Building Information Exchange (COBie) compliant spreadsheets from existing project intelligence data. Maps extracted data into the 18 standard COBie worksheet format for facility management handover. Critical for healthcare facilities where ongoing maintenance and asset management are regulatory requirements. Exports as multi-tab Excel workbook. Triggers: "COBie", "COBie export", "facility handover", "asset register", "O&M data", "building information exchange", "commissioning data", "facility management data", "asset data", "COBie spreadsheet", "handover data", "building handover".
version: 1.0.0
---

# cobie-export Skill Documentation

## Overview

COBie (Construction Operations Building Information Exchange) is a data format and structured approach for delivering building information and documenting construction handover data for facility management operations. It standardizes the transition of critical asset, system, and operational data from the design and construction phases directly into the operations and maintenance (O&M) phase.

This skill maps all extracted Foreman OS project intelligence — from spatial data, equipment schedules, submittals, inspections, and project documentation — into the standard COBie spreadsheet format. The export generates a multi-tab Excel workbook conforming to NBIMS-US COBie v2.4, enabling seamless facility management system integration and compliance with healthcare facility regulations (Joint Commission, CMS, and state licensing).

### Why COBie Matters for Foreman OS

In construction projects, especially healthcare facilities, critical operational data is scattered across dozens of sources: specification documents, equipment submittals, O&M manuals, commissioning reports, and maintenance schedules. COBie consolidates this intelligence into a single, structured handover document that facility managers can immediately import into their CMMS (Computerized Maintenance Management System), reducing administrative overhead and improving asset lifecycle management.

For Morehead One Senior Care (MOSC) and similar healthcare projects:
- **Regulatory Compliance**: Joint Commission and state inspectors expect documented handover of all medical equipment, fire/life safety systems, and maintenance procedures
- **Warranty Tracking**: COBie captures manufacturer warranties, service dates, and contact information
- **Asset Management**: Room-to-equipment mapping enables quick O&M lookup ("What systems serve Bedroom 5?")
- **Maintenance Scheduling**: Manufacturer-recommended maintenance intervals are embedded in the data
- **Spare Parts Management**: Predefined spare parts inventory for critical assets

---

## 4. Data Mapping Engine

The cobie-export skill implements a systematic mapping engine that:

### 4.1 Data Extraction Phase

1. **Scan All Data Stores**: Load all available JSON files from the project-data directory
   - project-config.json (building metadata)
   - directory.json (contacts)
   - plans-spatial.json (spaces, zones, grids)
   - specs-quality.json (equipment, systems, maintenance)
   - submittal log + document-intelligence results (approved spec sheets, manuals, warranties)
   - closeout-inspection.json (installation dates, serial numbers)
   - commissioning-data.json (startup dates, test results)
   - punch-list.json (open deficiencies)
   - rfi-log.json (design clarifications)
   - audit-trail.json (timestamps, creators)

2. **Validate Data Quality**: Check for required fields, format errors, referential integrity
   - Flag missing primary key data
   - Identify broken foreign key references
   - Warn on data type mismatches

3. **Build Reference Maps**: Create lookup tables for all primary keys
   - Contact-Email → Contact row (for Contact.Email unique index)
   - Space-Name → Space row (for Space.SpaceName unique index)
   - Type-Name → Type row (for Type.TypeName unique index)
   - Component-Name → Component row (for Component.Name unique index)

### 4.2 Mapping Phase

For each COBie worksheet:

1. **Define Field Mapping**: Associate each COBie field with source JSON path
2. **Apply Transformation Rules**: Convert data formats, handle nulls, validate references
3. **Build Row Data**: Construct each worksheet row with mapped values
4. **Apply Business Logic**:
   - Auto-generate missing IDs where needed
   - Resolve circular references
   - Calculate derived fields (e.g., "AreaNetRoom" = "AreaGrossRoom" - walls/fixtures)

### 4.3 Validation Phase

1. **Referential Integrity Checks**:
   - Component.TypeName must exist in Type.TypeName
   - Component.Space must exist in Space.SpaceName
   - Zone.Spaces must reference valid Space.SpaceName values
   - Job.Location must reference valid Space.SpaceName

2. **Format Validation**:
   - Email fields match email regex
   - Dates in ISO 8601 format (YYYY-MM-DD)
   - Numeric fields are numeric
   - Enum values match allowed set

3. **Completeness Scoring**: Calculate percentage of filled fields per worksheet

### 4.4 Handling Missing Data

COBie allows "n/a" for optional fields, but required fields must have values:

**If data is unavailable**:
- Mark as "n/a" (per COBie v2.4 spec)
- Log missing data for completeness report
- Suggest data collection source

**Example**: Type.WarrantyGuarantorParts is optional; if not available, set to "n/a" and note "Contact supplier for warranty details"

---

## 5. Export Workflow

### Step 1: Initiate Export

```
/cobie export
```

Triggers these actions:

1. Check for existing COBie export in process (prevent concurrent exports)
2. Create export working directory: /project-data/cobie-export/[timestamp]/
3. Initialize export log file
4. Scan all data stores for availability

### Step 2: Data Completeness Assessment

```
/cobie status
```

Generates pre-export completeness report:

```
COBie Completeness Assessment — 2026-02-19T10:30:00Z

Facility Data:
  ✓ Project name (Morehead One Senior Care)
  ✓ Building identification (MOSC-001)
  ✓ Site address (Morehead, KY)
  ~ Coordinates (lat/long available but GPS survey pending)
  ~ Site area and utilities routing (partial)

Space Data:
  ✓ Room schedule from plans (16 bedrooms + 5 common areas)
  ~ Room finishes (design specs available, as-built finishes pending)
  ~ Occupancy counts (design intent available, operational TBD)

Equipment (MEP):
  ~ HVAC equipment types defined, serial numbers/installation dates pending closeout
  ~ Plumbing fixtures scheduled, equipment data sheets pending supplier approval
  ~ Electrical panels and circuits defined, but circuits not fully detailed
  ~ Fire alarm system scheduled, commissioning data pending

Systems:
  ✓ HVAC system scope defined
  ✓ Plumbing system scope defined
  ✓ Electrical system scope defined
  ~ Fire protection scope conditional on design decisions

Documentation:
  ~ Submittals in progress (Schiller doors 24 days in review, Wells concrete mix 17 days in review)
  ~ O&M manuals pending closeout delivery
  ~ Commissioning reports pending project progress

Overall Readiness: 45% (design/construction phase)
  — Full readiness expected at substantial completion (07/29/26)
```

### Step 3: Execute Mapping & Export

1. **Load all data sources** into memory
2. **Generate Contact worksheet** from directory.json
3. **Generate Facility worksheet** from project-config.json
4. **Generate Floor/Space/Zone worksheets** from plans-spatial.json
5. **Generate Type/Component/System/Assembly worksheets** from specs-quality.json + submittals
6. **Generate Connection worksheet** from coordination data
7. **Generate Spare/Resource/Job worksheets** from O&M manuals
8. **Generate Impact worksheet** from energy/sustainability data
9. **Generate Document worksheet** from document-intelligence + submittal log
10. **Generate Attribute worksheet** from all extracted custom data
11. **Generate Coordinate worksheet** from site survey + building grid
12. **Generate Issue worksheet** from punch-list + RFI log
13. **Create multi-tab Excel workbook** using xlsx skill

### Step 4: Schema Validation

```
/cobie validate [optional: path-to-previous-export.xlsx]
```

Runs comprehensive COBie schema checks:

- Primary key uniqueness per worksheet
- Foreign key integrity (Component.TypeName exists in Type sheet, etc.)
- Enum value validation (Status must be one of: New/Existing/Planned/Obsolete/Unknown)
- Data type conformance
- Required field completion
- Log all validation warnings and errors

### Step 5: Generate Completeness Summary

```
Data Completeness Report:

Contact Worksheet: 95% (11/12 contacts with all required fields)
Facility Worksheet: 90% (building name, code, category complete; GPS pending)
Floor Worksheet: 100% (single floor, complete)
Space Worksheet: 85% (16 bedrooms scheduled; finishes and occupancy counts 60% complete)
Zone Worksheet: 70% (HVAC zones 100%, fire zones 50%, plumbing zones pending)
Type Worksheet: 65% (HVAC/plumbing equipment 80%; electrical/fire equipment 50%)
Component Worksheet: 20% (will reach 95% at substantial completion when serial numbers populated)
System Worksheet: 70% (HVAC, plumbing, electrical defined; fire protection pending)
Assembly Worksheet: 50% (HVAC assemblies defined; others pending)
Connection Worksheet: 30% (HVAC connections defined; other systems pending)
Spare Worksheet: 40% (pending O&M manual delivery)
Resource Worksheet: 35% (pending product data sheet delivery)
Job Worksheet: 45% (based on standard maintenance; customizations pending)
Impact Worksheet: 60% (energy model available; water/waste pending)
Document Worksheet: 55% (3/5 major equipment submittals under review)
Attribute Worksheet: 50% (standard attributes populated; custom fields pending)
Coordinate Worksheet: 90% (grid system 100%; GPS coordinates pending site survey)
Issue Worksheet: 85% (6 known submittals overdue, 7 daily reports logged)

Overall COBie Readiness: 58% (design/construction phase)
Next Milestone: 85% at foundation complete (03/20/26)
Full Readiness: 98% at substantial completion (07/29/26)
```

---

## 6. Data Completeness Scoring

### Per-Worksheet Completeness

Each worksheet has a completeness percentage calculated as:

```
Completeness % = (Populated required fields + Populated optional fields) / Total fields
```

### Overall COBie Readiness

```
COBie Readiness % = (Sum of all worksheet completeness %) / 18 worksheets
```

### Phased Data Collection Timeline

**Phase 1: Design & Permitting (Pre-Construction)**
- Facility, Floor, Space, Zone, Type definitions: 90%+ complete
- System scope: 80%+ complete
- Document references (spec sheets): 70%+ in submittal queue
- Coordinate (grid system): 95%+ complete
- Issue tracking (RFIs): 100% captured

**Phase 2: Construction & Closeout (Foundation through Finishes)**
- Component serial numbers: 0% → 95% (populated at closeout)
- Installation dates: 0% → 100% (captured at final inspection)
- System connections: 50% → 95% (refined during coordination)
- Spare parts/resources: 30% → 80% (from approved O&M manuals)
- Job (maintenance schedule): 40% → 90% (from manuals + commissioning)
- Document completeness: 55% → 95% (all submittals, commissioning reports, warranties)
- Issue closure: 85% → 10% (punch list resolved)

**Phase 3: Commissioning & Handover (Substantial Completion)**
- All documents: 98%+ complete
- All components with serial numbers, installation dates, startup dates
- All maintenance jobs scheduled
- All systems tested and documented (commissioning reports)
- All issues closed (punch list empty)
- Overall COBie readiness: 95%+

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
