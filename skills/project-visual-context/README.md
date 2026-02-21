# Project Visual Context Skill

Build information: Foreman OS v3.0 | Skill v1.0.0

## Overview

The **project-visual-context** skill gathers comprehensive visual context about construction projects to enable accurate AI-powered renderings. It guides users through a structured 3-phase interview to collect:

1. **Exterior Context** — Site setting, terrain, adjacent structures, vegetation, climate, orientation, construction status
2. **Interior Design Intent** — Design character, color palette, materials by room type, furniture, special features
3. **Photo Documentation** — Site and reference photos with AI-generated descriptions

The skill produces `visual-context.json` which powers the rendering-generator skill.

## Files in This Skill

```
project-visual-context/
├── SKILL.md                              (701 lines)
│   └── Complete skill documentation
├── references/
│   └── visual-context-schema.json        (282 lines)
│       └── JSON schema defining visual-context.json structure
└── README.md (this file)
```

## Quick Start

**Trigger:** `/site-context`

**Workflow:**
1. Skill checks if visual-context.json exists
   - If new: Run full 3-phase interview
   - If existing: Offer to update specific sections (exterior/interior/photos) or do full refresh
2. Auto-populate from existing project data (project-config, plans-spatial, specs-quality, schedule, directory)
3. Guide user through interview phases with questions tailored to building type and project phase
4. Accept photo uploads with AI-powered analysis
5. Save visual-context.json to AI - Project Brain/ folder

## How It Works

### Phase 1: Exterior Context
Gathers site setting, terrain, adjacent structures, vegetation, climate region/zone/season, building orientation, construction status, and site photos.

Pre-populated from:
- project-config.json → address, building type
- schedule.json → current phase
- Custom user input

### Phase 2: Interior Design Intent
Gathers design character, color palette (primary/secondary/accent), and material/furniture specifications for each room type found in plans.

Questions adapt based on:
- Building type (healthcare, office, retail, educational, industrial, etc.)
- Room types from plans-spatial.json
- Project phase (schematic vs. finishes)

### Phase 3: Photo Documentation
Processes uploaded site and inspiration photos with AI vision to generate detailed descriptions capturing materials, colors, atmospheric qualities, and context clues.

## Visual Context Schema

The schema (`references/visual-context-schema.json`) defines the complete structure:

```
root
├── version (1.0.0)
├── project_code
├── last_updated (ISO 8601)
├── exterior
│   ├── setting (type, terrain, adjacent N/S/E/W)
│   ├── vegetation (trees, ground cover, landscaping)
│   ├── climate (region, zone, seasons, prevailing weather)
│   ├── orientation (building faces, entry, parking)
│   ├── photos (array of photo objects with AI analysis)
│   └── construction_status (phase, visible work, equipment)
└── interior
    ├── design_character (9 enum options)
    ├── color_palette (primary, secondary, accent)
    ├── materials_by_room_type (flooring, walls, ceiling, base, casework, countertop, hardware)
    ├── furniture_by_room_type (style descriptions)
    ├── brand_standards
    └── special_notes
```

## Universal Design

The skill is designed to work for **any building type and project phase**:

**Building Types Supported:**
- Healthcare & Senior Care (MOSC example)
- Commercial Office
- Retail
- Educational (K-12, Higher Ed)
- Industrial (Manufacturing, Warehouse)
- Residential
- Hospitality (Hotel, Restaurant)
- Mixed-use

**Project Phases Supported:**
- Schematic Design (design intent focus)
- Design Development
- Construction Documents
- Foundation/Sitework (site context focus)
- Frame Erection (construction photos)
- Mechanical/Electrical/Plumbing Rough-In
- Finishes (material detail focus)
- Punch/Closeout

The skill adapts questions and room types based on project-config and schedule data.

## Data Sources

**Reads from:**
- `project-config.json` — Project code, address, building type, occupancy
- `plans-spatial.json` — Room types, areas, dimensions, door schedule
- `specs-quality.json` — Finish schedule, material specifications, casework specs
- `schedule.json` — Current phase, milestone dates
- `directory.json` — Architect, owner contacts for design preferences

**Writes to:**
- `AI - Project Brain/visual-context.json` — Complete visual context output

**References:**
- `references/visual-context-schema.json` — JSON schema validation

## Features

### Incremental Updates
If visual-context.json already exists:
- Option to update specific sections (exterior, interior, photos independently)
- Option for full refresh (re-run entire interview)
- Option to view current context
- Updates merge with existing data, preserving prior entries

### Error Handling
- Graceful fallback if project data files missing
- Photo upload error messages with retry options
- Handles multi-story buildings (asks if finishes differ by floor)
- Handles renovations (documents existing vs. new conditions)
- Handles single-story, multi-story, and complex building configurations

### AI-Powered Photo Analysis
Uploaded photos are analyzed to extract:
- Scene composition, scale, perspective
- Materials visible (colors, textures, conditions)
- Atmospheric qualities (lighting, weather, time of day)
- Context clues (adjacent structures, vegetation, utilities)
- Notable architectural/landscape features

## Output Example

When complete, skill generates visual-context.json structured like:

```json
{
  "version": "1.0.0",
  "project_code": "PJ-825021",
  "last_updated": "2026-02-19T14:30:00Z",
  "exterior": {
    "setting": {
      "type": "rural",
      "terrain": "rolling hills with gentle slopes",
      "elevation_description": "Site slopes northward, 15' elevation change across building footprint",
      "adjacent_north": "open pasture and forest, no structures within 1 mile",
      "adjacent_south": "state highway 60, mature deciduous trees screening views",
      ...
    },
    "climate": {
      "region": "Morehead, Kentucky",
      "zone": "USDA Zone 6a",
      "seasons": "four_season",
      "default_season": "spring",
      "prevailing_weather": "clear to partly cloudy"
    },
    ...
    "photos": [
      {
        "id": "photo_001",
        "file": "site_aerial_north_2026-02-15.jpg",
        "type": "aerial",
        "direction": "north",
        "analysis": "Aerial view showing 10-acre cleared site with foundation work in progress. Building footprint clearly visible with concrete pour scheduled. Mature deciduous trees line southern and eastern boundaries..."
      }
    ]
  },
  "interior": {
    "design_character": "clinical",
    "color_palette": {
      "primary": "soft white",
      "secondary": "warm gray",
      "accent": "warm teal"
    },
    "materials_by_room_type": {
      "Bedroom": {
        "flooring": "luxury vinyl plank, warm oak tone",
        "walls": "painted gypsum board, soft white",
        "ceiling": "gypsum board, bright white",
        "base": "painted wood base, warm gray",
        "hardware_finish": "brushed nickel"
      },
      ...
    }
  }
}
```

## Integration with Other Skills

This skill feeds into:
- **rendering-generator** skill — Uses visual-context.json to generate AI renderings with accurate materials, colors, site context, and seasonal variations

Related skills:
- **project-config** — Provides project basics
- **plans-spatial** — Provides room types and layout
- **specs-quality** — Provides material specifications
- **schedule** — Provides project phase and timeline

## Commands

```
/site-context              Start visual context interview (new or update existing)
/render                    Generate AI renderings using visual context (after /site-context)
/visual-context-view       Display current visual-context.json
/visual-context-export     Export context to PDF or HTML report
```

## Tips for Best Results

### Site Photos
- Upload aerial view (drone/satellite) for overall context
- Capture street-level approach view
- One photo from each cardinal direction
- Document existing conditions if renovation
- Include close-ups of vegetation, terrain, adjacent structures

### Design Intent
- Be specific with colors ("warm gray" not just "gray")
- Upload 3-5 inspiration photos for design character
- Describe materials with finish and sheen (e.g., "polished concrete with gray sealer" not just "concrete")
- Note if finishes vary (e.g., "entry is luxury marble, corridors are polished concrete")

### Timing
- Run AFTER project kickoff, BEFORE major design freezes
- Update at major project phases (design dev, construction start, finish selection)
- Use renderings to validate design with stakeholders

## Troubleshooting

**Q: I don't have photos yet. Can I skip Phase 3?**
A: Yes. Complete phases 1 and 2, skip photos. Re-run `/site-context` later to add photos.

**Q: Can I update just the color palette?**
A: Yes. If visual-context.json exists, run `/site-context` → select "Update specific section" → "Interior" → update only colors.

**Q: What if I don't know the design character yet?**
A: Choose the closest option. The skill explains each. You can update later.

**Q: Should I provide room-by-room specs?**
A: No. Group by room TYPE (Bedroom, Bathroom, Corridor, etc.). If a type varies significantly, note in special_notes.

**Q: How detailed should descriptions be?**
A: Detailed enough to guide rendering engine. Examples: "polished concrete, light gray" vs. just "concrete"; "warm oak" vs. just "oak."

## Version History

**v1.0.0** (Feb 2026)
- Initial release for Foreman OS v3.0
- 3-phase interview workflow (Exterior → Interior → Photos)
- Auto-population from project files
- Incremental update support
- Universal design for any building type and phase
- AI-powered photo analysis
- visual-context.json output
- Complete error handling and edge cases

## Author Notes

This skill is universal by design. It adapts to:
- Any building type (healthcare, office, retail, industrial, residential, etc.)
- Any project phase (from schematic design to finishes to closeout)
- Any building configuration (single-story, multi-story, renovation, new construction)
- Any site context (urban, suburban, rural, industrial campus, etc.)

The skill makes intelligent decisions about which questions to ask based on project configuration, minimizing user burden while maximizing rendering quality.
