# Per-Page Plan Extraction Checklist

Standard QA checklist for every page of a construction plan set. Run ALL sections against every page — do not skip sections based on assumed discipline.

---

## A. Sheet Identification (every page)

- [ ] Sheet number (e.g., A101, C-110, M1.0)
- [ ] Sheet title
- [ ] Discipline (Architectural, Civil, Structural, Mechanical, Electrical, Plumbing, Fire Protection, Interior Design)
- [ ] Scale(s) — per view (main plan, enlarged plans, details may have different scales)
- [ ] Title block data: engineer/architect name, date, revision number, professional stamp
- [ ] North arrow orientation and location
- [ ] Drawing index (if cover sheet or general notes sheet)
- [ ] Issue/revision date and description
- [ ] Project name and number confirmation

---

## B. Spatial & Geometric Data

- [ ] Grid lines with labels (letters horizontal, numbers vertical typically)
- [ ] Grid spacing dimensions (bay sizes)
- [ ] Dimension strings — AND verify chains (inner dims must sum to overall ±1")
- [ ] Room labels, room numbers, room areas (SF)
- [ ] Door tags with sizes (width × height)
- [ ] Window tags with sizes
- [ ] Building overall dimensions and setbacks
- [ ] Elevation markers (spot elevations, FFE, datum references, BM)
- [ ] Scale calibration:
  - [ ] Graphic scale bar (scan bottom-right → title block → below views)
  - [ ] Text scale notation per view (e.g., "1/4" = 1'-0"")
  - [ ] Multi-scale zone mapping (main plan vs. enlarged vs. details)
  - [ ] Image stretch detection (compare H vs. V calibration)
- [ ] Level/floor designations
- [ ] Column line intersections and labels
- [ ] Building corners and control points

---

## C. Schedules (look for ANY schedule table on the page)

- [ ] Room schedule (room#, name, floor, walls, base, ceiling, height)
- [ ] Door schedule (mark, size, type, frame, hardware group, fire rating, remarks)
- [ ] Window schedule (mark, size, type, glazing, frame material)
- [ ] Hardware schedule / hardware groups (HW-1, HW-2, etc. → items, keying, finishes)
- [ ] Finish schedule (floor type, wall finish, base type, ceiling type per room)
- [ ] Wall type legend / partition schedule (assembly layers, fire rating, STC, UL#, thickness)
- [ ] Fixture schedule (plumbing fixtures — type, manufacturer, model, connection sizes)
- [ ] Lighting fixture schedule (type, lamp, voltage, mounting, description)
- [ ] Equipment schedule (HVAC units, kitchen, medical — tag, capacity, connections)
- [ ] Panel schedule (circuits, breaker sizes, loads, phases)
- [ ] Plant schedule (landscaping species, size, quantity)
- [ ] Keynote legend/schedule (keynote# → description)
- [ ] Abbreviations list
- [ ] Symbol legend

---

## D. Construction Notes & Specifications

- [ ] General notes (structural, architectural, civil, MEP — each discipline)
- [ ] Keynote callouts (numbered bubbles on drawing → keynote schedule)
- [ ] Detail callout references (circle with detail#/sheet# — e.g., 3/A501)
- [ ] Section cut marks (arrows with section#/sheet# — e.g., 1/A301)
- [ ] Elevation reference marks (triangle/circle with elevation#/sheet#)
- [ ] Revision clouds with revision numbers, dates, and descriptions
- [ ] Weather thresholds (min/max temps for concrete, coatings, etc.)
- [ ] Cure times and protection requirements
- [ ] Material specifications and standards references (ASTM, ACI, AISC)
- [ ] Code references (IBC, ADA, NFPA, local amendments, KBC)
- [ ] Spec section references (CSI format — e.g., "per Section 03 30 00")
- [ ] Inspection/hold point callouts
- [ ] Construction sequence notes
- [ ] Special inspection requirements

---

## E. MEP Systems

### Mechanical (HVAC)
- [ ] HVAC equipment tags, locations, tonnage/BTU/CFM ratings
- [ ] Ductwork routing, sizes (width×height or diameter), insulation
- [ ] Diffuser/grille locations and CFM values
- [ ] Thermostat locations
- [ ] Refrigerant line routing and sizing
- [ ] Mechanical room layout and clearances
- [ ] Exhaust fan locations and CFM

### Plumbing
- [ ] Plumbing fixture locations and types (lavatory, WC, sink, etc.)
- [ ] Pipe routing and sizing (water supply, waste, vent, gas)
- [ ] Fixture unit counts
- [ ] Water heater location and capacity
- [ ] Cleanout locations
- [ ] Floor drain locations
- [ ] Riser diagram data

### Electrical
- [ ] Electrical panel locations and designations
- [ ] Circuit assignments and wire sizes
- [ ] Conduit routing and sizes
- [ ] Receptacle locations (standard, GFI, dedicated)
- [ ] Switch locations and switching diagrams
- [ ] Lighting layout (fixture types, circuiting)
- [ ] Emergency/exit lighting
- [ ] Fire alarm devices (pull stations, horns, strobes, detectors)
- [ ] Low voltage systems (data, phone, security, nurse call)

### Fire Protection
- [ ] Sprinkler head locations and types (pendant, upright, sidewall)
- [ ] Sprinkler riser details and location
- [ ] FDC (Fire Department Connection) location
- [ ] Fire/smoke damper locations in ductwork
- [ ] Standpipe connections
- [ ] Fire extinguisher cabinet locations

---

## F. Life Safety & Code

- [ ] Fire-rated walls/assemblies with hourly ratings (1-hr, 2-hr)
- [ ] Fire-rated wall assembly UL numbers
- [ ] Occupancy classifications and load factors per room/zone
- [ ] Egress paths and travel distances (actual vs. max allowed)
- [ ] Exit signs and locations
- [ ] Panic/fire exit hardware locations
- [ ] STC/acoustic ratings on partitions
- [ ] Accessibility routes (ADA paths of travel)
- [ ] Area of rescue assistance / areas of refuge
- [ ] Accessible parking and routes
- [ ] ADA-compliant restroom requirements
- [ ] Guard/handrail requirements
- [ ] Stair details with riser/tread dimensions
- [ ] Fire separation distance
- [ ] Smoke barriers and smoke partitions
- [ ] Maximum floor area per occupancy

---

## G. Site/Civil Data

- [ ] Grading elevations, slopes, drainage patterns
- [ ] Utility routing (storm, sanitary, water, gas, electric, telecom)
- [ ] Pipe sizes and materials
- [ ] Invert elevations and rim elevations at manholes/structures
- [ ] Detention/retention sizing and calculations
- [ ] Parking layout, counts, accessible spaces
- [ ] Drive aisle widths and turning radii
- [ ] BMP/erosion control measures (silt fence, inlet protection, stabilized entrance)
- [ ] Landscaping and planting details
- [ ] Sidewalk locations, widths, and ADA compliance
- [ ] Curb and gutter types
- [ ] Retaining wall locations and heights
- [ ] Property lines and easements
- [ ] Benchmark locations and elevations
- [ ] Site lighting locations
- [ ] Dumpster enclosure location and details
- [ ] Signage locations

---

## H. Calculations to Derive (where data permits on this page)

### Structural/Concrete
- [ ] Concrete CY — footing volumes (L × W × D ÷ 27)
- [ ] Concrete CY — slab area × thickness ÷ 27
- [ ] Concrete CY — grade beams, piers, walls
- [ ] Rebar tonnage — bar count × length × weight/ft (÷ 2000)
- [ ] Anchor bolt count and sizes

### Earthwork
- [ ] Cut volumes from grading data
- [ ] Fill volumes from grading data
- [ ] Trench excavation (L × W × D)
- [ ] Subgrade preparation area

### Interior Finishes
- [ ] Drywall SF — wall perimeter × height − openings (per wall type)
- [ ] Metal stud framing LF — wall lengths by gauge/size
- [ ] Flooring SF by type — room areas grouped by finish
- [ ] Ceiling SF by type — room areas grouped by ceiling type
- [ ] Paint SF — wall + ceiling painted surfaces
- [ ] Base trim LF — room perimeters by base type

### Roofing/Exterior
- [ ] Roofing SF — roof plan area × slope factor
- [ ] Exterior wall cladding SF
- [ ] Flashing LF
- [ ] Gutter/downspout LF

### Code Compliance
- [ ] Occupant load — area ÷ load factor per use
- [ ] Egress width required — occupants × 0.2"/person (stairs: 0.3")
- [ ] Plumbing fixture count required — per IPC Table 403.1
- [ ] HVAC CFM per room — area × ventilation rate
- [ ] Electrical load per panel — connected watts

### Site
- [ ] Stormwater GPM — roof area × rainfall intensity (rational method)
- [ ] Parking required vs. provided (per zoning code)
- [ ] Impervious area SF

---

## I. Cross-Reference Validation (per page)

- [ ] Every detail callout bubble → verify target sheet exists in discovered index
- [ ] Every section cut mark → verify target section sheet exists
- [ ] Every keynote number → verify entry in keynote legend (flag orphans)
- [ ] Every door tag → verify entry in door schedule
- [ ] Every window tag → verify entry in window schedule
- [ ] Every wall type tag → verify entry in wall type legend
- [ ] Every equipment tag → consistent across all sheets seen so far
- [ ] Dimension chain totals → verify inner dims sum to overall (±1")
- [ ] Room numbers → consistent between plan, RCP, finish schedule
- [ ] Elevation references → target elevation sheet exists
- [ ] Spec section references → valid CSI division
- [ ] Grid line labels → consistent with other sheets

---

## Validation Flags

When a cross-reference check fails, log with these codes:
- `XREF-ORPHAN`: Callout references a sheet/detail not found in index
- `XREF-MISMATCH`: Tag on plan doesn't match schedule entry
- `DIM-CHAIN-ERR`: Inner dimensions don't sum to overall (±1" tolerance)
- `KEYNOTE-ORPHAN`: Keynote bubble on drawing but no legend entry
- `SCHED-MISSING`: Tag on plan has no corresponding schedule row
- `SCALE-CONFLICT`: Multiple conflicting scales detected for same view
- `FIRE-RATING-GAP`: Fire-rated wall shown but no rating value visible
- `ADA-FLAG`: Potential accessibility issue detected

---

## Usage

This checklist is applied to EVERY page during extraction, regardless of assumed discipline. Many pages contain data from multiple categories (e.g., an architectural plan may show MEP equipment locations, fire-rated walls, and civil reference points).

After completing the checklist for a page, summarize:
1. Sheet ID and discipline
2. Key data points extracted (count by category)
3. Validation flags raised
4. Calculations derived
5. Cross-reference items to verify against future pages
