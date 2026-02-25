---
name: bim-coordination
description: >
  BIM coordination and model-based field management for construction superintendents. Manage clash detection workflows, model-to-field verification, 4D scheduling integration, laser scanning and point cloud operations, drone surveys, digital twin closeout handoff, and LOD specification tracking. Track clash reports, model reviews, field verifications, scan records, drone flights, and coordination meetings through a structured data model. Integrates with morning-brief, daily-report, rfi-preparer, look-ahead-planner, closeout-commissioning, and drawing-control. Triggers: "BIM", "model", "clash", "clash detection", "Navisworks", "Revit", "coordination", "4D", "laser scan", "point cloud", "drone", "digital twin", "LOD", "BIM execution plan", "BxP", "model review".
version: 1.0.0
---

# BIM Coordination Skill

## Overview

The **bim-coordination** skill provides Building Information Modeling coordination and management capabilities for construction superintendents and field managers. This is not a skill about creating BIM models -- it is about **using** BIM models and their outputs to build better, faster, and with fewer conflicts in the field.

The construction superintendent's relationship with BIM has fundamentally changed. You are no longer handed a stack of 2D drawings and expected to figure out how everything fits together in three dimensions. Instead, you have access to coordinated 3D models that show exactly how structural, mechanical, electrical, plumbing, and architectural elements relate to each other in space and time.

**Critical distinction**: As a superintendent, you do not model. You USE models and their outputs. Your role is to:
- Verify that what is modeled matches what is built (and vice versa)
- Participate in clash detection workflows and drive field resolution
- Use 4D scheduling visualizations to plan and communicate sequencing
- Coordinate laser scanning and drone surveys for as-built documentation
- Ensure the digital twin handoff at closeout meets owner requirements

### How BIM Changes the Super's Workflow

**Traditional (2D Plan Sets)**:
- Overlay multiple sheets mentally to find conflicts
- Discover clashes during installation (expensive, schedule-killing)
- Rely on RFIs to resolve spatial conflicts after they are found in the field
- As-built documentation through redline markups on paper

**BIM-Based Coordination**:
- Clashes identified digitally before construction begins
- 3D visualization of complex intersections available on tablet in the field
- 4D scheduling ties model elements to activities for visual sequencing
- Laser scanning and drones provide precise as-built verification
- Digital twin handoff gives the owner a living model for facility management

This skill provides:
- BIM Execution Plan (BxP) superintendent responsibilities
- Clash detection workflows from identification through field resolution
- Model-to-field verification methods and tolerances
- 4D scheduling integration for phasing and logistics
- Laser scanning and point cloud management
- Drone survey planning and deliverable management
- Digital twin and closeout handoff requirements
- LOD specification guidance by discipline and phase
- Structured data model for all BIM coordination activities
- Integration with other ForemanOS skills

**Key Principle**: BIM coordination is not a design-phase activity that ends when construction starts. The model is a living document that must be continuously verified against field conditions, updated with as-built information, and handed off as a functional digital twin at project completion.

---

## BIM Execution Plan (BxP) -- Superintendent Responsibilities

### What a BxP Contains

The BIM Execution Plan (also called BxP or BEP) is the project-specific roadmap for how BIM will be used. It is typically produced by the BIM Manager or VDC Manager during preconstruction and covers:

- **Project BIM goals and uses** -- what BIM will be used for (coordination, scheduling, estimating, facility management)
- **Model ownership matrix** -- who creates and maintains each discipline model
- **Model development schedule** -- when models are due at each phase
- **LOD requirements by element** -- level of development expected at each milestone
- **Software and platform standards** -- Revit version, Navisworks version, file naming, exchange formats
- **Coordination process** -- meeting schedule, clash detection rules, resolution workflow
- **Quality control procedures** -- model audit checklists, validation rules
- **Deliverable requirements** -- what the owner receives at closeout
- **File sharing and CDE (Common Data Environment)** -- where models live, access permissions, version control

### Superintendent's BxP Responsibilities

The super does not write the BxP but is responsible for key field-related elements:

1. **Field Verification Protocol**
   - When and how field conditions are checked against the model
   - Who performs verification (super, layout crew, survey team)
   - What tolerances trigger a discrepancy report
   - How deviations are documented and communicated back to the modeling team

2. **Reality Capture Coordination**
   - Scheduling laser scans and drone flights
   - Providing safe access for scanning crews
   - Reviewing scan deliverables for completeness
   - Coordinating scan timing with construction activities (scan before cover-up)

3. **As-Built Model Updates**
   - Documenting field changes that differ from the coordinated model
   - Red-lining model discrepancies for the BIM team to incorporate
   - Verifying as-built model accuracy before closeout submission

4. **BIM Coordination Meeting Participation**
   - Attending weekly (or biweekly) BIM coordination meetings
   - Reporting field conditions that affect model accuracy
   - Providing construction sequence input for 4D scheduling
   - Identifying upcoming work areas that need clash resolution priority

### Model Access -- Viewer Software

The superintendent needs read access to models but does not need full modeling software. Common viewer platforms:

| Platform | Type | Cost | Key Features |
|---|---|---|---|
| Navisworks Freedom | Desktop viewer | Free | View NWD files, basic navigation, saved viewpoints |
| Autodesk Docs / BIM 360 | Cloud platform | Included with project license | Browser/mobile, markup, issues, model coordination |
| Procore BIM | Cloud platform | Included with Procore license | Browser/mobile, linked to Procore workflows |
| Trimble Connect | Cloud platform | Free tier available | Browser/mobile, field overlay, mixed reality |
| Dalux | Cloud/mobile | Subscription | AR field overlay, BIM viewer, quality management |

**Field tip**: Download models for offline viewing before going to areas with poor connectivity. Autodesk Docs and Procore both support offline model caching on tablets.

---

## Clash Detection Workflows

### Types of Clashes

Clash detection identifies conflicts between building systems before they become costly field problems. There are three types:

**1. Hard Clashes (Physical Intersection)**
- Two elements occupy the same physical space
- Example: Ductwork passes through a structural beam
- Example: Conduit runs through a plumbing pipe
- These MUST be resolved before installation -- there is no field fix for two objects in the same space

**2. Soft Clashes (Clearance Violation)**
- Two elements do not physically intersect but violate required clearances
- Example: Ductwork is within 2" of a sprinkler head (needs 18" clearance for NFPA compliance)
- Example: Electrical panel has insufficient working clearance (NEC 110.26 requires 36" minimum)
- Example: Insulated pipe does not have enough space for insulation thickness
- Soft clash tolerances are defined per system and per code requirement

**3. 4D Clashes (Time/Space Conflicts)**
- Two activities require the same space at the same time based on the schedule
- Example: MEP rough-in scheduled in the same area where concrete is being poured
- Example: Crane swing radius conflicts with active work area during the same week
- 4D clashes require schedule adjustment, not model adjustment

### Clash Detection Tools

| Tool | Capability | Typical User |
|---|---|---|
| Navisworks Manage | Full clash detection with Clash Detective | BIM/VDC Manager |
| BIM 360 Model Coordination | Cloud-based automated clash detection | BIM/VDC Manager, PM |
| Solibri | Rule-based model checking and clash detection | BIM Manager |
| Navisworks Simulate | Limited clash detection | Project Engineer |
| Trimble Connect | Basic interference checking | Field team |

**Super's role**: You typically do not run the clash detection software. Your role is to review clash reports, prioritize resolution based on construction sequence, drive field resolution, and verify that resolved clashes are actually resolved in the field.

### Reading Clash Reports

A typical clash report from Navisworks Clash Detective contains:

- **Clash ID**: Unique identifier (e.g., CLH-MEP-STR-0042)
- **Clash Type**: Hard, soft (with tolerance), or 4D
- **Status**: New, Active, Reviewed, Resolved, Approved
- **Elements Involved**: Element 1 (discipline, type, size) vs. Element 2 (discipline, type, size)
- **Grid Location**: Column grid intersection (e.g., between grids C-D / 3-4)
- **Level/Elevation**: Floor and elevation of the clash
- **Distance**: For hard clashes, penetration depth; for soft clashes, clearance shortfall
- **Viewpoint**: Saved camera position showing the clash in the model
- **Date Found**: When the clash was first detected
- **Assigned To**: Trade or person responsible for resolution

### Grouping and Filtering Clash Reports

Raw clash counts can be overwhelming (thousands of clashes in a complex project). Effective management requires:

1. **Group by Zone/Area** -- Focus on areas coming up in the schedule first
2. **Group by Discipline Pair** -- MEP/Structural, MEP/MEP, MEP/Architectural
3. **Filter Duplicates** -- Same elements clashing at multiple points count as one issue
4. **Filter by Tolerance** -- Ignore clashes below meaningful thresholds (e.g., <1/16" penetration)
5. **Prioritize by Schedule** -- Areas with work starting in the next 2-4 weeks get priority

### Superintendent's Role in Field Resolution

When a clash cannot be resolved through model adjustment alone, the super drives field resolution:

1. **RFI Generation** -- When the clash reveals a design conflict, generate an RFI with the clash viewpoint attached
2. **On-Site Resolution** -- When trades can resolve a routing conflict in the field within tolerances, document the agreed-upon solution
3. **Field Routing** -- When the model shows the ideal path but field conditions require adjustment, direct the adjusted routing and document for as-built

### Clash Resolution Meeting Format

**Frequency**: Weekly during active coordination phases, biweekly during less intensive periods

**Agenda**:
1. Review new clashes since last meeting (5 min)
2. Status update on previously assigned clashes (10 min)
3. Walk through highest-priority clashes by area (20 min)
   - Display clash viewpoint in model
   - Identify responsible trades
   - Discuss resolution options
   - Assign resolution owner and deadline
4. Review upcoming work areas needing pre-clash check (5 min)
5. RFI status for design-related clashes (5 min)
6. Action items and next meeting date (5 min)

**Attendees**: Superintendent, BIM/VDC Manager, MEP Coordinator, affected trade foremen, Project Engineer (for RFI tracking)

### Common Clash Categories

**MEP vs. Structural**:
- Ductwork through beams or columns
- Piping through shear walls
- Conduit through post-tension tendons
- Hangers conflicting with structural connections
- Resolution: Typically requires structural engineer review; may need beam penetration sleeves, routing changes, or supplemental framing

**MEP vs. MEP**:
- Ductwork vs. piping (most common)
- Conduit vs. piping
- Cable tray vs. ductwork
- Fire sprinkler vs. everything else
- Resolution: Priority rules apply (gravity drain > pressure pipe > ductwork > conduit > cable tray); coordinate elevation stacking

**MEP vs. Architectural**:
- Ductwork in ceiling plenum exceeding ceiling height
- Piping conflicts with wall framing
- Equipment clearances vs. room dimensions
- Access panel locations vs. finish requirements
- Resolution: May require ceiling height adjustment, soffit additions, room dimension changes, or equipment relocation

### Clash Resolution Documentation

Every resolved clash must be documented with:
- **Clash ID** and original clash report reference
- **Resolution Description** -- what was changed (routing, elevation, size, elimination)
- **Resolution Type** -- model change, field adjustment, design change (RFI), tolerance acceptance
- **Responsible Party** -- who made the change
- **Verification** -- confirmation that the resolution is reflected in the model or documented as field deviation
- **Date Resolved** and **Date Verified**

### Clash Status Tracking

| Status | Definition |
|---|---|
| **New** | Clash detected, not yet reviewed |
| **Active** | Reviewed, assigned to a responsible party for resolution |
| **Reviewed** | Resolution proposed, awaiting approval |
| **Resolved** | Resolution implemented in the model or documented as field deviation |
| **Approved** | Resolution verified in the field and/or model -- closed |

---

## Model-to-Field Verification

### Tablet/Phone Overlay

Modern BIM workflows allow superintendents to overlay the 3D model on the physical job site using augmented reality (AR):

- **Dalux BIM Viewer** -- AR overlay on iOS/Android, point device at installed work to compare against model
- **Trimble Connect AR** -- Mixed reality overlay with Trimble hardware or mobile device
- **OpenSpace** -- 360-degree capture walks linked to model for progress verification
- **HoloBuilder** -- Job walk capture with BIM overlay comparison

**Setup requirements**: Calibrated device, known reference points (survey control), current model version loaded, adequate lighting for camera-based AR.

**Accuracy considerations**: Mobile AR is useful for gross conflict identification (is the duct in the right bay?) but not for precision measurement. Use total station or laser scanning for tolerance verification.

### Layout from BIM Coordinates

BIM models contain precise coordinate data that can be exported directly to layout equipment:

1. **Total Station with BIM Export** -- Export point coordinates from the model, import to total station, lay out points in the field
2. **Robotic Total Station (RTS)** -- One-person layout using BIM coordinates with automated prism tracking
3. **Layout software** -- Trimble Field Link, Topcon MAGNET, Leica iCON -- bridge between BIM and field layout hardware

**Workflow**:
1. BIM coordinator exports layout points from the model (DXF, CSV, or native format)
2. Survey/layout crew imports points to total station controller
3. Points are laid out in the field with paint, tacks, or laser marks
4. As-built points are captured and compared back to the model
5. Deviations outside tolerance are flagged for resolution

### Verification Tolerances by Trade and Element Type

| Trade/Element | Typical Tolerance | Reference |
|---|---|---|
| Structural steel columns | +/- 1/4" plan, +/- 3/8" elevation | AISC Code of Standard Practice |
| Cast-in-place concrete walls | +/- 1/4" plan location | ACI 117 |
| Cast-in-place concrete slabs | +/- 3/4" elevation (FF/FL dependent) | ACI 117 |
| MEP rough-in (horizontal) | +/- 1/2" from model location | Project-specific (check BxP) |
| MEP rough-in (elevation) | +/- 1/4" from model elevation | Project-specific (check BxP) |
| Fire sprinkler heads | +/- 1" from ceiling grid | NFPA 13 / reflected ceiling plan |
| Curtain wall anchors | +/- 1/8" plan, +/- 1/4" elevation | Manufacturer specs |
| Embedded items | +/- 1/4" horizontal, +/- 1/2" vertical | Project-specific |
| Electrical rough-in (boxes) | +/- 1/2" plan, +/- 1/4" elevation | NEC / project specs |
| Plumbing waste/vent | +/- 1/4" for slope verification | UPC / IPC (slope tolerance 1/8"/ft min) |

**Critical note**: Always check the project BxP and specifications for project-specific tolerances. The values above are industry-typical but your project may have tighter or looser requirements.

### Field Discrepancy Reporting

When field conditions deviate from the model beyond tolerance, document using a model-to-field deviation log:

| Field | Description |
|---|---|
| Deviation ID | Unique identifier (e.g., DEV-2024-0015) |
| Date | Date deviation discovered |
| Location | Grid intersection, level, room/area |
| Element | What was measured (e.g., "12" supply duct at grid C-4, Level 3") |
| Modeled Value | What the model shows (position, elevation, size) |
| Field Value | What was measured in the field |
| Deviation | Difference (e.g., "6" south of modeled location") |
| Within Tolerance? | Yes/No based on applicable tolerance standard |
| Impact | Effect on other trades, schedule, function |
| Resolution | Action required (move element, update model, RFI, accept as-is) |
| Status | Open, In Progress, Resolved |

### As-Built Model Updating Workflow

1. **Field Documentation** -- Super documents as-built conditions (photos, measurements, redline sketches)
2. **Deviation Log Entry** -- Discrepancy logged with all required fields
3. **BIM Team Notification** -- Deviation log shared with BIM coordinator/modeler
4. **Model Update** -- BIM team updates model to reflect as-built conditions
5. **Verification** -- Super reviews updated model against field to confirm accuracy
6. **Closeout Integration** -- As-built model becomes the basis for digital twin handoff

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
