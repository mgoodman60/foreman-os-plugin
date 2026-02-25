# Drawing Reference Resolution Guide

## Overview

The Drawing Reference Resolution system translates casual, conversational location descriptions from site personnel into precise, technical drawing references. When a user says "the wall on the east side of the second floor," this module resolves that to specific grid lines, building areas, floor levels, and then matches those to actual drawing sheet numbers from the loaded documents.

This is essential for RFIs and submittal transmittals, which must reference exact drawings to be actionable by the design team.

## Location Hierarchy

Drawing references follow a hierarchical resolution process:

```
User's Casual Description
    ↓
Building Area (East Wing, West Wing, Main Lobby, etc.)
    ↓
Grid Lines (A, B, C... and 1, 2, 3...)
    ↓
Floor Level (Level 1, Level 2, Ground Floor, etc.)
    ↓
Sheet Numbers (A-201, S-204, M-301, etc.)
    ↓
Final Reference: "Sheet A-201 (Second Floor Plan), Grid E-G, Level 2"
```

## Sheet Numbering Conventions

Standard AIA drawing sheet numbering prefixes identify the discipline and content:

### Architectural Plans (A-xxx)
- **A-101**: Site Plan, Site Context
- **A-201, A-202, A-203**: Floor Plans (Levels 1, 2, 3, etc.)
- **A-301, A-302, A-303**: Exterior Elevations (North, East, South, West)
- **A-401**: Sections
- **A-5XX**: Details and Schedules
- **A-6XX**: Interior Elevations, Finishes Plans

### Structural Plans (S-xxx)
- **S-101**: Basement/Foundation Plan
- **S-201, S-202, S-203**: Structural Floor Plans (Levels 1, 2, 3, etc.)
- **S-301, S-302**: Structural Sections
- **S-4XX**: Details
- **S-5XX**: Connection Details, Schedules

### Mechanical/HVAC (M-xxx)
- **M-101**: HVAC System Diagram
- **M-201, M-202, M-203**: HVAC Plans (Levels 1, 2, 3, etc.)
- **M-4XX**: Details, Equipment Schedules

### Electrical/Power (E-xxx)
- **E-101**: Electrical Service/Panel Schedule
- **E-201, E-202, E-203**: Electrical Plans (Levels 1, 2, 3, etc.)
- **E-4XX**: Details, Schedules

### Plumbing (P-xxx)
- **P-101**: Water/Sewer Main Plan
- **P-201, P-202, P-203**: Plumbing Plans (Levels 1, 2, 3, etc.)
- **P-4XX**: Details, Schedules

### Civil/Site (C-xxx)
- **C-101**: Site Survey, Existing Conditions
- **C-201**: Site Development Plan, Grading
- **C-301**: Utilities, Drainage
- **C-4XX**: Details, Specifications

## Data Sources

### documents_loaded
The primary data source for available drawings. Requires:
- Sheet number (e.g., "A-201")
- Sheet title (e.g., "Second Floor Plan")
- Discipline code (A, S, M, E, P, C)
- Floor level (if applicable) (e.g., "Level 2")
- Building area coverage (if mapped) (e.g., "East Wing, West Wing, Full Building")
- Grid references (if marked) (e.g., "Grid A-D, Grid 1-5")
- Page count (number of sheets in set)

**Example documents_loaded entry**:
```json
{
  "sheet_number": "A-201",
  "title": "Second Floor Plan",
  "discipline": "A",
  "floor_level": "2",
  "areas_covered": ["East Wing", "West Wing", "Main Lobby"],
  "grid_references": "A-D, 1-6",
  "status": "loaded",
  "uploaded_date": "2025-01-15"
}
```

### grid_lines
Defines the building's column/structural grid system.

**Example grid_lines data**:
```json
[
  {
    "type": "column_line",
    "label": "A",
    "orientation": "vertical",
    "description": "West edge of building"
  },
  {
    "type": "column_line",
    "label": "1",
    "orientation": "horizontal",
    "description": "South property line"
  },
  {
    "type": "column_line",
    "label": "G",
    "orientation": "vertical",
    "description": "East Wing/Main Lobby boundary"
  }
]
```

### building_areas
Defines named zones within the project.

**Example building_areas data**:
```json
[
  {
    "name": "East Wing",
    "grids_x": ["E", "F", "G"],
    "grids_y": ["1", "2", "3"],
    "floors": ["1", "2", "3"],
    "description": "Office space above retail"
  },
  {
    "name": "Main Lobby",
    "grids_x": ["C", "D", "E"],
    "grids_y": ["4", "5", "6"],
    "floors": ["1"],
    "description": "Two-story entry hall"
  }
]
```

### floor_levels
Maps floor names to numbers and vice versa.

**Example floor_levels data**:
```json
[
  {
    "level_name": "Ground Floor",
    "level_number": "1",
    "elevation": "0'0\"",
    "description": "Retail and lobby"
  },
  {
    "level_name": "Level 2",
    "level_number": "2",
    "elevation": "13'0\"",
    "description": "Office space"
  },
  {
    "level_name": "Level 3",
    "level_number": "3",
    "elevation": "26'0\"",
    "description": "Office space, ending here"
  }
]
```

### room_schedule
Detailed breakdown of individual rooms/spaces.

**Example room_schedule entry**:
```json
{
  "room_number": "201",
  "room_name": "Conference Room B",
  "floor_level": "2",
  "building_area": "East Wing",
  "grids": "E-F, 2-3",
  "area_sf": 450,
  "use": "Conference",
  "finishes": "Carpet, Drywall, Acoustic Ceiling"
}
```

## Resolution Logic

### Step 1: Parse User Description

Extract location clues from the user's casual description:

**User says**: "That wall on the east side of the second floor between the mechanical room and the main lobby"

**Parsed elements**:
- Direction: "east side"
- Floor: "second floor"
- Rooms: "mechanical room", "main lobby"

### Step 2: Match Building Area

Use parsed elements to identify relevant building area(s):

**Lookup logic**:
1. If user mentions specific room name → Search room_schedule for that room → Extract building_area
2. If user mentions directional reference ("east side", "north wing") → Search building_areas for name containing that keyword
3. Match on floor level to narrow results

**From example**:
- "mechanical room" → Search room_schedule → Found in "East Wing", Level 2
- "main lobby" → Search room_schedule → Found in "Main Lobby", Level 1
- Result: Need drawings covering both East Wing (Level 2) and Main Lobby (Level 1)
- Primary area: "East Wing" (since the conflict is described as being on the "east side")

### Step 3: Match Grid Lines

Determine grid coordinates from building area:

**Lookup logic**:
1. If user mentions specific grid line (e.g., "Grid G") → Use directly
2. If building_area defined → Extract associated grids from building_areas record
3. If user mentions compass direction and no building_area → Search grid_lines for descriptions containing that direction

**From example**:
- Building Area "East Wing" → Associated grids from building_areas: E-F (vertical), 2-3 (horizontal)
- "Main Lobby" grids: C-D (vertical), 4-5 (horizontal)
- Where they meet: Grid boundary is at G and 3 (between East Wing and Main Lobby)
- Refined grid reference: "Grid E-G, Lines 1-3" (covering both areas)

### Step 4: Match Floor Level

Determine floor level number from name:

**Lookup logic**:
1. If user says "second floor" → Search floor_levels for level_name matching "second" or "Level 2" → Extract level_number = "2"
2. If user says "ground floor" or "first floor" → level_number = "1"
3. If user says "Level 3" → level_number = "3"
4. If ambiguous, use current construction level

**From example**:
- "second floor" → floor_levels lookup → level_number = "2"

### Step 5: Find Matching Sheets

Search documents_loaded for sheets covering the identified building area, grids, and floor level:

**Lookup logic**:
1. Filter documents_loaded by discipline (A for architectural, S for structural, etc.)
2. Filter by floor_level (matching step 4)
3. Filter by areas_covered (matching step 2)
4. Return all matching sheets

**From example**:
- Architectural plans covering Level 2: Filter documents_loaded for discipline "A" AND floor_level = "2"
  - Result: "A-201" (Second Floor Plan)
  - Check areas_covered: ["East Wing", "West Wing", "Main Lobby"] ✓
  - Grid references: "A-D, 1-6" (covers E-G? Check if E-G extends beyond) ✓
- Structural plans covering Level 2: Filter for discipline "S" AND floor_level = "2"
  - Result: "S-201" (Structural Floor Plan, Level 2)
- Result set: [A-201, S-201]

### Step 6: Return Resolution

Compile final formatted reference:

**Output**:
```
Drawing Reference(s):
  • Sheet A-201 (Second Floor Plan), Grid E-G, Level 2
  • Sheet S-201 (Structural Floor Plan), Level 2
```

## Matching Logic: Common Patterns

### Directional References

| User Says | Resolves To | Logic |
|-----------|-------------|-------|
| "East side" | Building Area with "East" in name or grids E-G | Direction keyword match or grid position |
| "North wall" | Grid line A or area name containing "North" | Compass direction + grid_lines description |
| "Southeast corner" | Grids E-G, 1-3 (example coordinates) | Both compass directions narrowed to specific quadrant |
| "Back of house" | Building Area matching typical back-of-house terms | Keyword match (mechanical, service, loading, kitchen) |
| "Front entrance" | Main Lobby or similar primary entry area | Keyword match (entry, entrance, lobby) |

### Floor References

| User Says | Resolves To | Logic |
|-----------|-------------|-------|
| "Ground floor" | Level 1 | floor_levels lookup |
| "First floor" | Level 1 (in US convention) | floor_levels lookup |
| "Second floor" | Level 2 | floor_levels lookup |
| "Basement" | Level B1 or B2 (if exists) | floor_levels lookup, special naming |
| "Roof" | Highest level (if exists) | floor_levels lookup, special naming |
| "Upper level" | Current level + 1 | Relative reference, requires context |

### Room/Space References

| User Says | Resolves To | Logic |
|-----------|-------------|-------|
| "Conference Room B" | room_schedule lookup → Extract floor, area, grids | Room name exact match |
| "Bathroom on Level 2" | room_schedule lookup, filter by room_type = "Restroom", floor = 2 | Room type + floor |
| "The stairwell" | room_schedule or building_areas for "Stair" | Fuzzy match on function |
| "Mechanical room" | room_schedule or building_areas for "Mechanical" | Fuzzy match, often central to building |
| "Elevator lobby" | room_schedule for "Elevator", usually Level 1 | Specific space match |

### Fuzzy Matching for Common Spaces

When exact matches aren't found, apply fuzzy matching:

#### Bathroom / Restroom
- Keywords: "bathroom", "toilet", "restroom", "WC"
- Match: room_schedule entries with room_type = "Restroom" or "Toilet" or name containing these
- Result: Grid coordinates of most likely bathroom (typically near core)

#### Lobby / Entry
- Keywords: "lobby", "entry", "entrance", "foyer"
- Match: building_areas or room_schedule with primary entry designation
- Result: Usually large, central space on Level 1

#### Stairwell
- Keywords: "stairwell", "stair", "stairs", "staircase"
- Match: room_schedule entries with room_type = "Stairwell" or "Stairs"
- Result: Coordinates typically appear on multiple floor plans

#### Elevator
- Keywords: "elevator", "lift", "elevator lobby"
- Match: room_schedule entries with room_type = "Elevator" or name containing "Elevator"
- Result: Usually central location, appears on all floor plans

#### Mechanical Room
- Keywords: "mechanical room", "mech room", "MEP room", "equipment room"
- Match: room_schedule entries with room_type = "Mechanical" or building_areas with "Mechanical"
- Result: Often central or peripheral, typically access point for building systems

## Handling Multiple Matching Sheets

When a location description matches multiple sheets, list all relevant:

**Example**: User describes "The wall between the mechanical room and lobby"

**Results**:
```
Drawing Reference(s):
  • Sheet A-201 (Second Floor Plan), Grid C-G, Levels 1-2
  • Sheet A-301 (Exterior Elevations), East Elevation
  • Sheet S-201 (Structural Floor Plan), Level 2
  • Sheet M-201 (HVAC Plan, Level 2), Mechanical Room Area
  • Sheet P-201 (Plumbing Plan, Level 2), Service Wall Area
```

**Rationale**:
- Architectural plans show wall location and extent (A-201)
- Elevation shows wall height and appearance (A-301)
- Structural shows support and connections (S-201)
- Mechanical shows ductwork and equipment interfacing (M-201)
- Plumbing shows any piping routing (P-201)

The RFI preparer can then help the user select which are most relevant, or include all with emphasis on primary reference.

## Cross-Reference with room_schedule

Room-specific references bypass the grid matching:

**User says**: "What size is Conference Room B?"

**Resolution**:
1. Search room_schedule for room_name = "Conference Room B"
2. Found: Room 201, Floor Level 2, East Wing, Grids E-F, Lines 2-3, Area 450 SF
3. Determine relevant drawings:
   - Architectural floor plan (A-202 or A-201 depending on numbering) for room layout
   - Lighting and power plans (E-202) for electrical service
   - HVAC plans (M-202) for temperature control
   - Finishes plan (A-601) for flooring, wall treatments
4. Return refined drawing references with exact room location

## Examples with Before/After

### Example 1: Wall Assembly Conflict

**BEFORE** (User's casual description):
"There's a conflict on the second floor on the east side. The architecture says one thing and the structure says something different about the wall between the mechanical room and the main space."

**PARSING**:
- Floor: "second floor" → Level 2
- Direction: "east side" → E-G grid range
- Rooms: "mechanical room", "main space" → Cross-reference room_schedule
  - Mechanical Room: East Wing, Grid F, Line 3
  - Main Space (likely office): East Wing, Grid E-G, Lines 1-3

**RESOLUTION STEPS**:
1. Building Area: "East Wing" (from room location) OR spans "East Wing" to central area
2. Grid Lines: E-G (vertical), 1-3 (horizontal) — intersection of mechanical and main areas
3. Floor Level: 2
4. Sheet lookup (documents_loaded):
   - Architectural: A-201 (Second Floor Plan), covers Levels 1-2, Areas "East Wing, West Wing, Main Lobby"
   - Structural: S-201 (Structural Floor Plan, Level 2)
   - Mechanical: M-201 (HVAC Plan, Level 2)
   - All sheets show Grid E-G, Lines 1-3 ✓

**AFTER** (Professional reference):
```
Drawing Reference(s):
  • Sheet A-201 (Second Floor Plan), Grid E-G, Lines 1-3, Level 2
  • Sheet S-201 (Structural Floor Plan), Grid E-G, Lines 1-3, Level 2
  • Sheet A-301 (Exterior Elevations), East Elevation (wall shown)
  • Sheet M-201 (HVAC Plan, Level 2), Mechanical Equipment Area
```

---

### Example 2: Bathroom Finishes Question

**BEFORE**:
"What's the tile pattern in the upstairs bathrooms? I need to know before we order."

**PARSING**:
- Location: "upstairs bathrooms" → Multiple rooms, likely Level 2 (if "upstairs" is second floor)
- Room type: "bathrooms" → room_schedule entries with type "Restroom"

**RESOLUTION STEPS**:
1. Search room_schedule for room_type = "Restroom" AND floor_level = "2"
2. Found: Rooms 202, 204, 206 (three restrooms on Level 2, East Wing area)
3. Grid Lines from room locations: Average Grid E-F, Lines 2, 4, 5
4. Sheet lookup:
   - Finishes Plan: A-601 (Interior Elevations & Finishes Details), Level 2, Restrooms
   - Architectural Plan: A-201 (Second Floor Plan), shows restroom locations
   - Details: A-502 (Bathroom Fixture & Tile Details)

**AFTER**:
```
Drawing Reference(s):
  • Sheet A-601 (Finishes Plan, Level 2), Restroom Areas (Rooms 202, 204, 206)
  • Sheet A-502 (Bathroom Details), Detail 4 – Tile Base & Wall Pattern
  • Sheet A-201 (Second Floor Plan), Restroom Locations
```

---

### Example 3: Stairwell Construction Detail

**BEFORE**:
"How's the stairwell constructed? We need to order the handrails."

**PARSING**:
- Location: "stairwell" → Spans multiple levels
- System: "handrails" → Metal fabrication question (also relates to code)

**RESOLUTION STEPS**:
1. Search room_schedule for "Stairwell" → Found: Central stairwell, all Levels 1-3, Grids C-D, Lines 4-5
2. Sheet lookup:
   - Architectural Plans: A-201, A-202, A-203 (Floor Plans, Levels 1-3) showing stair location
   - Sections: A-401 (Building Sections) showing stair profile, rise/run
   - Details: A-502 (Stair Details), showing handrail profiles, connections, material specs
   - Architectural Elevations: A-301 (if stair visible in exterior elevation)

**AFTER**:
```
Drawing Reference(s):
  • Sheet A-401 (Building Sections), Section 2 – Central Stairwell (all levels)
  • Sheet A-502 (Stair Details), Details 1-6 – Handrail profiles, fasteners, materials
  • Sheets A-201, A-202, A-203 (Floor Plans, Levels 1-3), Stairwell location
  • Sheet A-301 (Exterior Elevations), if stair visible at facade
```

---

### Example 4: Exterior Mechanical Equipment

**BEFORE**:
"Where does the HVAC unit go on the roof? And can it be seen from the street?"

**PARSING**:
- Location: "roof" → Top level (Level 3 or Roof level)
- System: "HVAC unit" → Mechanical equipment
- Visibility: "seen from street" → Relates to architectural appearance

**RESOLUTION STEPS**:
1. Determine roof level from floor_levels → Level 3 (or "Roof")
2. Sheet lookup:
   - Mechanical Plans: M-301 or M-Roof (Rooftop HVAC Equipment Plan)
   - Architectural Roof Plan: A-301 (if not mechanical) showing equipment locations and screening
   - Elevations: A-301 (North, South, East, West), showing HVAC and screening visibility
   - Details: A-503 or M-401 (Equipment Screening & Support Details)

**AFTER**:
```
Drawing Reference(s):
  • Sheet M-301 (Rooftop HVAC Equipment Plan), Equipment locations and connections
  • Sheet A-301 (Exterior Elevations), all four elevations – shows equipment screening
  • Sheet A-502 (Roof Equipment Details), Detail 7 – Equipment Screening Enclosure
  • Sheet M-401 (HVAC Support Details), Foundation and fastening details
```

---

## Resolution Confidence Levels

When displaying resolved drawing references, indicate confidence level:

### HIGH (100% Confidence)
- Exact room name matched in room_schedule
- Grid lines explicitly mentioned by user
- Drawing list contains documented sheet for that floor and area
- **Display**: Direct reference without caveats

### MEDIUM (75-90% Confidence)
- Location inferred from directional reference
- Building area matched by keyword but not explicit
- Multiple sheets could be relevant; picking most likely
- **Display**: Reference with note: "(Primary reference; review for related sheets)"

### LOW (50-75% Confidence)
- Fuzzy match on room function (e.g., "a bathroom" → generic restroom)
- Multiple possible interpretations
- **Display**: Show alternatives: "Drawing references could include: A-201 (if restroom is on Level 2) or A-202 (if on Level 3). Please confirm floor level."

## Implementation Tips

1. **Progressive Disclosure**: Start with highest-confidence matches, offer user to add related sheets
2. **User Confirmation**: Always show resolved references to user before finalizing RFI; allow edits
3. **Logging**: Record what was resolved and any ambiguities for future reference and learning
4. **Refresh Documents**: Periodically validate that documents_loaded entries still exist (drawings may be superseded)
5. **Shorthand Support**: Accept both formal ("Grid E-G, Lines 2-4") and casual ("east side") inputs
6. **Partial Data Handling**: If grid_lines or building_areas are not fully populated, fall back to user confirmation mode
7. **Multi-Discipline**: For complex issues, suggest multiple-discipline sheets (Arch + Structural + MEP) as related references

