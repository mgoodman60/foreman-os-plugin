# bim-coordination — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the bim-coordination skill.



## Laser Scanning and Point Clouds

### When to Scan

Laser scanning provides precise 3D documentation of existing or as-built conditions. Schedule scans for:

1. **Existing Conditions** -- Before construction begins on renovation/addition projects
2. **As-Built Verification** -- After major milestones (structural complete, MEP rough-in complete, above-ceiling close-up)
3. **Pre-Cover Verification** -- Before covering work (above ceiling, in-wall, underground) -- last chance to verify
4. **Progress Documentation** -- Monthly or milestone progress capture
5. **Dispute Resolution** -- When there is disagreement about field conditions
6. **Quality Verification** -- Verify flatness, plumbness, alignment of installed work

### Scanner Types

| Type | Use Case | Range | Accuracy | Speed |
|---|---|---|---|---|
| Terrestrial (tripod) | Interior/exterior, high accuracy | Up to 350m | +/- 1-2mm | 1M+ points/sec |
| Handheld (SLAM) | Quick capture, confined spaces | Up to 100m | +/- 10-30mm | 300K points/sec |
| Drone-mounted (LiDAR) | Site surveys, rooftops, large areas | Varies | +/- 20-50mm | 300K+ points/sec |

**Selection guidance**:
- **Terrestrial** for any work requiring tolerance verification (MEP, structural, curtain wall)
- **Handheld** for quick documentation, progress walks, areas too tight for tripod
- **Drone-mounted** for site-wide surveys, roof conditions, stockpile measurement

### Scan-to-BIM Workflow

1. **Scan** -- Scanning crew captures point cloud data from multiple positions
2. **Register** -- Individual scans are aligned and merged into a unified point cloud (registration)
3. **Clean** -- Remove noise, artifacts, temporary items (scaffolding, workers, equipment)
4. **Compare** -- Overlay point cloud on BIM model; generate deviation map
5. **Report** -- Produce deviation report highlighting out-of-tolerance conditions
6. **Update** -- BIM team updates model where as-built conditions deviate from design

### Tolerance Standards

| Element/System | Typical Scan Tolerance | Notes |
|---|---|---|
| MEP systems | +/- 1/4" (6mm) | Tightest tolerance; critical for coordination |
| Structural elements | +/- 1/2" (12mm) | Columns, beams, connections |
| Concrete surfaces | +/- 1/2" (12mm) | Walls, slabs, foundations |
| Civil/sitework | +/- 1" (25mm) | Grade, paving, utilities |
| Curtain wall/facade | +/- 1/4" (6mm) | Anchors, mullion alignment |
| Floor flatness | FF25/FL20 minimum | Per ACI 117 / project spec |

### Scan Deliverables

| Deliverable | Format | Use |
|---|---|---|
| Point Cloud | E57, RCP, LAS | Raw 3D data for viewing/analysis |
| Deviation Map | PDF, HTML | Color-coded map showing deviations from model |
| As-Built Overlay | NWD, IFC | Point cloud registered to model coordinate system |
| Cross-Sections | PDF, DWG | 2D slices through point cloud at specific locations |
| Measurement Report | PDF, XLSX | Specific dimension checks extracted from point cloud |

### Cost Considerations

Laser scanning is cost-effective when:
- The cost of rework from undetected deviations exceeds the scan cost
- Multiple trades depend on accurate as-built data (scan once, share to all)
- The owner requires as-built model verification at closeout
- Existing conditions are complex and difficult to measure manually (e.g., interstitial MEP)
- Legal or dispute documentation requires precision measurement

**Typical costs** (2024-2025 rates):
- Terrestrial scan: $2,000-5,000 per floor (commercial building)
- Handheld scan: $1,000-3,000 per floor
- Drone scan (site): $1,500-4,000 per flight
- Scan-to-BIM modeling: $3,000-10,000+ per floor (depends on complexity)

---



## Drone Surveys

### Use Cases

| Use Case | Frequency | Deliverable |
|---|---|---|
| Progress photos | Weekly | Orthomosaic, oblique images |
| Volumetric surveys | Monthly | DEM, stockpile volume calculations |
| Roof inspections | As needed | High-resolution imagery, thermal |
| Safety monitoring | As needed | Aerial overview of active work |
| Marketing/owner updates | Monthly/milestone | Time-lapse, rendered flythrough |
| Site logistics | Pre-mobilization, major phase changes | Orthomosaic for logistics planning |
| Facade inspection | Milestone | High-resolution oblique imagery |

### FAA Part 107 Awareness

All commercial drone operations in the United States require compliance with FAA Part 107:

- **Pilot Certification**: Remote pilot must hold a Part 107 certificate (FAA knowledge test)
- **Aircraft Registration**: Drone must be registered with the FAA
- **Airspace Authorization**: Flights in controlled airspace (near airports) require LAANC or waiver
- **Operational Limits**: 400' AGL max altitude, visual line of sight, daylight or civil twilight with anti-collision lights, no flight over non-participating persons without waiver
- **Restrictions**: No flight within 5 miles of an airport without authorization, no flight over stadiums/sporting events, TFRs (Temporary Flight Restrictions) must be checked before every flight

**Super's responsibility**: Ensure the drone operator provides proof of Part 107 certification, insurance, and airspace authorization. Do not allow unlicensed operators to fly on the project site.

### Flight Planning

| Parameter | Definition | Typical Value |
|---|---|---|
| GSD (Ground Sample Distance) | Pixel size on the ground | 1-2 cm for progress, 0.5 cm for detail |
| Front Overlap | Image overlap in flight direction | 75-80% |
| Side Overlap | Image overlap between flight lines | 65-75% |
| Flight Altitude | Height above ground | 200-400' for overview, 50-100' for detail |
| Flight Pattern | Grid, double grid, orbit | Grid for mapping, orbit for 3D models |

### Drone Deliverables

| Deliverable | Description | Use |
|---|---|---|
| Orthomosaic | Stitched, georeferenced aerial image | Site plans, progress overlay, measurement |
| DEM (Digital Elevation Model) | Surface elevation data | Volumetric calculations, grading verification |
| 3D Mesh | Textured 3D surface model | Visual documentation, 3D measurement |
| Point Cloud | LiDAR-derived 3D point data | BIM comparison, precise measurement |
| Stockpile Volumes | Calculated volumes from DEM | Material tracking, pay quantities |
| Thermal Imagery | Infrared capture | Roof inspections, insulation verification, leak detection |

### Frequency Guidelines

| Activity | Recommended Frequency | Notes |
|---|---|---|
| Progress photography | Weekly | Consistent day/time for time-lapse |
| Volumetric survey | Monthly or per pay period | Align with cost reporting cycles |
| Milestone documentation | At each major milestone | Foundation, topping out, enclosure, substantial completion |
| Roof inspection | Before and after roofing | Pre-installation conditions and final verification |
| Safety monitoring | As needed | High-activity periods, crane operations |

---



## Digital Twin and Closeout Handoff

### What a Digital Twin Is (and Isn't)

**A digital twin IS**:
- An accurate 3D representation of the as-built facility
- Linked to real-time or near-real-time operational data (sensors, BMS, IoT)
- A tool for facility management, maintenance planning, and space management
- Continuously updated throughout the building's operational life

**A digital twin is NOT**:
- Just a BIM model (a model is the geometry; a twin is geometry + data + connectivity)
- A one-time deliverable (it must be maintained and updated)
- A replacement for traditional O&M manuals (it supplements them)
- Always necessary (not every project requires a full digital twin)

### Closeout BIM Requirements

At project closeout, the construction team typically delivers:

1. **As-Built BIM Model** -- Updated to reflect actual installed conditions
   - All field deviations incorporated
   - Model reflects what was built, not what was designed
   - Equipment and devices modeled to specified LOD

2. **Equipment Data** -- Embedded in the model or linked through COBie
   - Manufacturer, model number, serial number
   - Installation date
   - Warranty information
   - Maintenance schedule
   - Spare parts list

3. **Maintenance Schedules** -- Linked to equipment elements in the model
   - Preventive maintenance intervals
   - Filter replacement schedules
   - Inspection requirements
   - Calibration schedules

4. **Space Data** -- Room/space information populated in the model
   - Room names, numbers, departments
   - Area calculations
   - Occupancy loads
   - Finish schedules

### COBie Data Requirements

COBie (Construction Operations Building Information Exchange) is the standard format for delivering facility data from the construction BIM:

- **Facility** -- Project-level information (name, address, category)
- **Floor** -- Level/floor information (name, elevation, height)
- **Space** -- Room/space information (name, category, area)
- **Type** -- Equipment/product types (manufacturer, model, warranty)
- **Component** -- Individual instances of equipment (serial number, location, installation date)
- **System** -- Groupings of components into systems (HVAC zones, electrical circuits)
- **Job** -- Maintenance tasks linked to components (PM schedules, procedures)
- **Document** -- Linked documents (O&M manuals, warranties, submittals)

**Super's role in COBie**: Verify that as-built equipment data (serial numbers, installation dates, field-verified locations) is accurate before the BIM team exports COBie spreadsheets.

### FM Handoff -- What the Facilities Team Needs

The facilities management team needs from the construction BIM:

1. **Navigable model** -- Viewable without specialized software (IFC, web viewer)
2. **Equipment locations** -- Find any piece of equipment in the 3D model
3. **System diagrams** -- Trace systems through the model (follow a duct run, trace a circuit)
4. **Access information** -- How to physically reach equipment for maintenance
5. **Space data** -- Accurate room/space information for space management
6. **Document links** -- Click on equipment to access O&M manuals, warranties, submittals
7. **Baseline condition** -- Point cloud or scan data documenting as-built conditions at turnover

### Digital Twin for Operations

Post-construction, the digital twin serves ongoing facility management:

- **Maintenance management** -- Visualize equipment location, access maintenance records
- **Space planning** -- Use accurate floor plans and 3D model for tenant improvements
- **Energy management** -- Link BMS/BAS data to model for energy visualization
- **Emergency response** -- 3D building information for first responders
- **Capital planning** -- Identify renovation and replacement needs in 3D context
- **Tenant communication** -- Visual communication of building systems and planned work

---



## LOD Specifications

### LOD Definitions

LOD (Level of Development) defines how much information is included in model elements at each project phase. The LOD Specification is maintained by the BIM Forum (a buildingSMART alliance initiative).

**LOD 100 -- Conceptual**
- Element is represented as a symbol or generic placeholder
- No geometry detail; represents approximate size, shape, location, or orientation
- Example: A structural column shown as a generic vertical line with approximate height
- Example: An HVAC unit shown as a rectangular block with approximate footprint
- Use: Massing studies, feasibility, early design

**LOD 200 -- Approximate Geometry**
- Element is represented as a generic system or assembly with approximate quantities, size, shape, location, and orientation
- Example: A structural column shown as the correct shape (W-flange) with approximate size
- Example: An air handling unit shown with correct approximate dimensions and location
- Use: Schematic design, early coordination

**LOD 300 -- Precise Geometry**
- Element is represented as a specific system or assembly, accurate in terms of quantity, size, shape, location, and orientation
- Example: A structural column modeled as a W12x65 at the correct grid location and elevation
- Example: An air handling unit modeled with specific manufacturer dimensions, connection points, and clearances
- Use: Design development, construction coordination, clash detection

**LOD 350 -- Construction Detail**
- Element is represented with detailing for construction, including connections, supports, and interfaces with other systems
- Example: A structural column with connection plates, bolts, shims, and base plate
- Example: An air handling unit with vibration isolation, duct connections, piping connections, electrical connections, and maintenance access zones
- Use: Construction documents, fabrication-level coordination, field layout

**LOD 400 -- Fabrication**
- Element is modeled with sufficient detail for fabrication and assembly
- Example: A structural steel connection with exact bolt patterns, weld details, and erection aids
- Example: A prefabricated MEP module with all internal components, connection points, and lifting points
- Use: Shop drawings, fabrication, prefabrication

**LOD 500 -- As-Built / Verified**
- Element is a field-verified representation of the as-built condition
- Verified through survey, laser scan, or direct measurement
- Example: A structural column verified at its actual installed position (may differ from LOD 400)
- Example: An air handling unit with verified location, serial number, and installation date
- Use: Record documents, facility management, digital twin, closeout

### What to Expect at Each Project Phase

| Phase | Typical LOD | What You See in the Model |
|---|---|---|
| Conceptual Design | 100 | Block shapes, no detail |
| Schematic Design | 200 | Generic shapes with approximate sizes |
| Design Development | 300 | Specific elements, accurate sizes and locations |
| Construction Documents | 350 | Construction-level detail with connections |
| Shop Drawing / Fabrication | 400 | Fabrication-ready detail |
| As-Built / Closeout | 500 | Field-verified, actual conditions |

### LOD Matrix by Discipline

| Element | SD (200) | DD (300) | CD (350) | Fabrication (400) | As-Built (500) |
|---|---|---|---|---|---|
| Structural Steel | Generic shapes | Specific members | Connections, stiffeners | Bolt patterns, welds | Field-verified position |
| Concrete | Outline volumes | Specific dims, rebar zones | Rebar, embeds, formwork | Pour sequences, rebar detailing | Scan-verified geometry |
| HVAC Ductwork | Generic routes | Specific sizes, fittings | Supports, hangers, insulation | Fabrication spool sheets | As-built routing verified |
| Plumbing | Generic routes | Specific sizes, fixtures | Slopes, supports, insulation | Fabrication spools | As-built routing verified |
| Electrical | Generic distribution | Panel locations, conduit sizes | Raceway, box locations | Wire pulls, terminations | As-built routing verified |
| Fire Protection | Coverage areas | Main/branch routing | Heads, drops, hangers | Hydraulic calc verification | Verified head locations |
| Architectural | Room outlines | Wall types, openings | Door/window details, finish info | Millwork details, custom elements | Verified dimensions |

### Field Verification at Each LOD

The superintendent's verification responsibilities increase with LOD:

- **LOD 300-350**: Verify that installed elements match the model in location, size, and orientation. Flag deviations that exceed tolerance.
- **LOD 400**: Verify that fabricated elements match shop drawing/model details. Check connections, supports, and interfaces.
- **LOD 500**: Confirm that as-built model reflects actual installed conditions. Sign off on as-built accuracy for closeout.

---



## BIM Coordination Data Model

The bim-coordination skill uses `bim-log.json` to track all BIM coordination activities.

### Schema

```json
{
  "clash_reports": [
    {
      "id": "CR-001",
      "date": "2024-11-15",
      "tool": "Navisworks Manage",
      "model_version": "v2.4.1",
      "total_clashes": 142,
      "resolved": 89,
      "open": 53,
      "by_category": {
        "mep_structural": 38,
        "mep_mep": 67,
        "mep_architectural": 22,
        "structural_architectural": 8,
        "4d_time_space": 7
      },
      "priority_breakdown": {
        "critical": 5,
        "high": 18,
        "medium": 30,
        "low": 0
      },
      "notes": "Focus areas: Level 3 mechanical room, Level 2 corridor ceiling"
    }
  ],
  "model_reviews": [
    {
      "id": "MR-001",
      "date": "2024-11-14",
      "model_version": "v2.4.1",
      "discipline": "MEP Combined",
      "reviewer": "John Smith, Superintendent",
      "findings": [
        "Ductwork at grid C-4 Level 3 conflicts with new beam per SI-042",
        "Fire sprinkler heads not coordinated with reflected ceiling plan in lobby",
        "Electrical panel clearance insufficient at Room 205"
      ],
      "status": "open",
      "action_items": [
        "RFI for beam/duct conflict at C-4",
        "Sprinkler contractor to update model by 11/18",
        "Relocate panel per NEC 110.26 -- discuss at next coordination meeting"
      ]
    }
  ],
  "field_verifications": [
    {
      "id": "FV-001",
      "date": "2024-11-13",
      "location": "Level 2, Grid A-3 to B-5",
      "element": "12\" supply duct main",
      "deviation_type": "elevation",
      "modeled_value": "12'-6\" above FF",
      "measured_value": "12'-2\" above FF",
      "deviation": "4\" low",
      "within_tolerance": false,
      "resolution": "Duct hanger adjustment required -- work order issued to mechanical contractor",
      "status": "in_progress"
    }
  ],
  "scan_records": [
    {
      "id": "SC-001",
      "date": "2024-11-10",
      "type": "terrestrial",
      "location": "Level 3 -- full floor MEP rough-in",
      "scanner": "Leica RTC360",
      "operator": "XYZ Survey Co.",
      "scan_positions": 45,
      "deliverables": ["point_cloud_e57", "deviation_map_pdf", "as_built_overlay_nwd"],
      "tolerance_check": {
        "elements_checked": 128,
        "within_tolerance": 119,
        "out_of_tolerance": 9,
        "max_deviation": "3/4 inch at grid D-6 supply duct"
      },
      "notes": "9 deviations flagged -- 6 minor (accept as-is), 3 require correction"
    }
  ],
  "drone_flights": [
    {
      "id": "DF-001",
      "date": "2024-11-08",
      "pilot": "Jane Doe, Part 107 #1234567",
      "aircraft": "DJI Matrice 350 RTK",
      "purpose": "monthly_progress",
      "flight_altitude": "250 ft AGL",
      "gsd": "1.2 cm/pixel",
      "deliverables": ["orthomosaic", "3d_mesh", "progress_photos"],
      "conditions": {
        "wind": "8 mph",
        "visibility": "10+ miles",
        "cloud_cover": "scattered"
      },
      "airspace_auth": "LAANC approved, Class G",
      "notes": "Full site coverage, 342 images captured"
    }
  ],
  "coordination_meetings": [
    {
      "id": "CM-001",
      "date": "2024-11-14",
      "attendees": [
        "John Smith (Super)",
        "Lisa Chen (BIM Manager)",
        "Mike Johnson (MEP Coordinator)",
        "Tom Brown (Mechanical Foreman)",
        "Sarah Davis (Electrical Foreman)"
      ],
      "model_version_reviewed": "v2.4.1",
      "clashes_reviewed": 25,
      "clashes_resolved": 12,
      "clashes_assigned": 13,
      "decisions": [
        "Mechanical duct at C-4 to be rerouted above beam -- mechanical contractor to update model by 11/18",
        "Electrical panel in Room 205 to be relocated to Room 207 -- RFI required for architect approval",
        "Sprinkler head layout in lobby to follow RCP -- sprinkler contractor to coordinate with architect"
      ],
      "action_items": [
        {"owner": "Tom Brown", "item": "Update mechanical model at C-4", "due": "2024-11-18"},
        {"owner": "John Smith", "item": "Submit RFI for panel relocation", "due": "2024-11-16"},
        {"owner": "Sarah Davis", "item": "Review sprinkler/RCP coordination", "due": "2024-11-18"}
      ],
      "next_meeting": "2024-11-21"
    }
  ]
}
```

---



## Integration

The bim-coordination skill connects with other ForemanOS skills to provide comprehensive project management:

### morning-brief
- Surfaces open clash count and trend (increasing/decreasing)
- Highlights upcoming laser scan and drone flight schedule
- Flags model reviews with open action items past due date
- Notes coordination meetings scheduled for today

### daily-report
- BIM verification activities logged today (field checks, scan reviews, deviation findings)
- Clash resolution progress (resolved today, new today, net change)
- Model review findings that affect today's work
- Scan or drone flight results received

### rfi-preparer
- Clash-driven RFIs: attach clash viewpoint, element IDs, and model version
- Design conflict RFIs originating from coordination meetings
- Field deviation RFIs when as-built conditions require design changes
- Model discrepancy RFIs when the model does not match contract documents

### look-ahead-planner
- 4D phasing data integrated into 3-week look-ahead
- Upcoming work areas flagged for pre-installation clash review
- Scan and drone scheduling aligned with construction milestones
- Model update deadlines tied to upcoming trade installations

### closeout-commissioning
- Digital twin handoff checklist and progress tracking
- COBie data collection status by system
- As-built model verification status by area
- Final scan scheduling for closeout documentation

### drawing-control
- Model version tracking linked to drawing revision log
- Model-to-drawing consistency checks
- Superseded model versions archived with drawing sets
- Coordination drawing extraction from BIM model

## 4D Scheduling Integration

### Linking Schedule Activities to Model Elements

4D BIM connects the 3D model to the project schedule (the fourth dimension is time). Each schedule activity is linked to the corresponding model elements:

- **Activity: "Level 3 Structural Steel Erection"** links to all steel elements on Level 3
- **Activity: "Level 2 MEP Rough-In Zone A"** links to all MEP elements in Zone A on Level 2
- **Activity: "Exterior Curtain Wall South Elevation"** links to curtain wall panels on the south face

**Tools**: Navisworks (TimeLiner), Synchro, Autodesk Docs, Primavera with BIM integration

### Phasing Visualization

4D models allow the superintendent to show trades exactly how work will sequence through the building:

- **Color-coded phasing** -- Each phase/activity shown in a different color as the schedule plays forward
- **Zone-by-zone visualization** -- Walk through the building zone by zone showing installation sequence
- **Trade-specific views** -- Show one trade's entire scope sequenced over time
- **Milestone snapshots** -- "This is what the building should look like on March 15th"

**Field application**: Pull up the 4D model at trade coordination meetings to explain:
- Why Trade A must finish before Trade B starts in a given area
- How the schedule flows through the floor plate
- What the look-ahead plan means spatially (not just on a Gantt chart)

### 4D for Logistics Planning

4D extends beyond installation sequencing to site logistics:

- **Crane Placement** -- Visualize crane reach, swing radius, and pick zones over time as the building rises
- **Material Staging** -- Show where materials should be staged for each phase, avoiding conflicts with active work
- **Access Routes** -- Identify and communicate access paths as the building progresses (entrances close, new routes open)
- **Temporary Structures** -- Show shoring, scaffolding, temporary enclosures in the 4D sequence
- **Site Logistics Plan Animation** -- Combine all logistics elements into a time-lapse site plan

### 4D for Owner Communication

4D models are powerful tools for communicating progress to owners who may not read Gantt charts:

- **Monthly progress visualization** -- Show what was accomplished this month in 3D
- **Schedule comparison** -- Planned 4D sequence vs. actual 4D progress (overlay or side-by-side)
- **Milestone look-ahead** -- Animate upcoming milestones with dates
- **Change impact visualization** -- Show the owner how a change order affects the sequence

### Schedule Simulation for Conflict Identification

Running the 4D simulation before work begins reveals time-space conflicts:

- Two trades scheduled in the same area at the same time (4D clash)
- Material delivery requiring access through an active work zone
- Crane reach limitations during a specific phase
- Elevator/hoist usage conflicts between trades
- Fire watch or hot work conflicts with adjacent operations

**Resolution**: Adjust the schedule (resequence, shift, add lag) rather than the model. Document the conflict and resolution in the coordination log.

### Pull Planning Integration

4D models enhance Last Planner System pull planning sessions:

- **Weekly work plan visualization** -- Show the 3D model filtered to only the work planned for the coming week
- **Constraint identification** -- Visually identify spatial constraints that affect make-ready
- **Handoff visualization** -- Show where one trade's work ends and the next trade begins
- **Progress tracking** -- Compare planned 4D state to actual field progress

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


