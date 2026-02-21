# Project Visual Context - Complete Workflow Reference

## Quick Navigation

- **Trigger:** `/site-context`
- **Output:** `visual-context.json` → AI - Project Brain/
- **Powers:** `/render` command for AI photorealistic renderings

---

## Workflow: New Project (First Time)

```
User: /site-context
  ↓
Skill checks: visual-context.json exists?
  ├─ NO → Proceed with full 3-phase interview
  │
  └─ YES → Ask what to update (see "Incremental Updates" below)

PHASE 1: EXTERIOR CONTEXT (Auto-populated + Guided)
├─ Step 1.1: Confirm building basics
│   └─ Display: Project code, address, type, occupancy, phase
│       User confirms/corrects
│
├─ Step 1.2: Setting type
│   └─ Ask: Rural/suburban/urban/industrial/campus/mixed?
│
├─ Step 1.3: Terrain
│   └─ Ask: Flat/rolling/hillside/valley/elevated?
│       + Details: slopes, elevation change, etc.
│
├─ Step 1.4: Adjacent structures
│   └─ Ask for each cardinal direction (N/S/E/W):
│       - Type of structure
│       - Distance
│       - Height relative to building
│       - Notable features
│
├─ Step 1.5: Vegetation & landscaping
│   └─ Ask: Types of trees, ground cover, landscaping plans?
│
├─ Step 1.6: Climate & season
│   └─ Auto-detect region from address
│   └─ Ask: Climate zone? Default rendering season?
│   └─ Ask: Prevailing weather?
│
├─ Step 1.7: Building orientation
│   └─ Ask: Main entry direction?
│   └─ Ask: Which elevation faces north?
│   └─ Ask: Parking location?
│   └─ Ask: Sun path characteristics?
│
├─ Step 1.8: Construction status
│   └─ Display: Current phase (from schedule)
│   └─ Ask: Accurate? Anything to add?
│
├─ Step 1.9: Photo upload
│   └─ Ask: Upload site photos? (optional)
│   └─ Accept categories: aerial, street, adjacent, terrain, vegetation, conditions, interior_reference
│   └─ For each: Use AI vision to generate description
│
└─ Summary → Confirm before proceeding

PHASE 2: INTERIOR DESIGN INTENT (Adapted to Building Type)
├─ Step 2.1: Design character
│   └─ Ask: Which character?
│       (9 options: warm_residential, modern, clinical, hospitality, institutional, 
│        industrial, corporate, educational, retail)
│
├─ Step 2.2: Color palette
│   └─ Ask: Primary color?
│   └─ Ask: Secondary color?
│   └─ Ask: Accent color?
│   └─ Ask: Inspiration photos? (optional)
│
├─ Step 2.3: Materials by room type
│   └─ Load room types from plans-spatial.json
│   └─ For EACH room type, ask:
│       ├─ Flooring (material, finish, color)
│       ├─ Walls (material, color)
│       ├─ Ceiling (type, color/finish)
│       ├─ Base/trim (material, finish)
│       ├─ Casework (if applicable)
│       ├─ Countertop (if applicable)
│       ├─ Hardware finish
│       └─ Furniture style + special features
│
├─ Step 2.4: Brand standards & owner preferences
│   └─ Ask: Any brand guidelines? (yes/no)
│   └─ If yes: Describe
│
├─ Step 2.5: Special design notes
│   └─ Ask: Any special features we should capture?
│       (Examples: historic elements, high-end finishes, accessibility focus, etc.)
│
└─ Summary → Confirm before proceeding

PHASE 3: PHOTO DOCUMENTATION
├─ Step 3.1: Review uploaded photos
│   └─ Display photos uploaded in Phase 1
│   └─ Ask: Add more inspiration photos? (yes/no)
│   └─ If yes: Accept additional photos
│
├─ Step 3.2: AI photo analysis
│   └─ For EACH photo, generate description capturing:
│       ├─ Scene composition
│       ├─ Materials visible
│       ├─ Atmospheric qualities
│       ├─ Context clues
│       └─ Notable features
│
├─ Step 3.3: Missing photos alert
│   └─ If no photos uploaded: Offer to add now
│       (Can skip and add later)
│
└─ Summary → Complete

FINALIZATION
├─ Step 4.1: Final review
│   └─ Display complete visual-context summary
│   └─ Ask: Everything correct? (yes/edit/add)
│   └─ If edit: Jump to relevant phase for updates
│
├─ Step 4.2: Save
│   └─ Generate visual-context.json
│   └─ Validate against schema
│   └─ Save to AI - Project Brain/
│
└─ Step 4.3: Next steps
    └─ Display guidance: Ready for /render command
```

---

## Workflow: Updating Existing Project

```
User: /site-context (visual-context.json already exists)
  ↓
Skill displays current context (loaded from file)
  ↓
Ask: "What would you like to do?"
  ├─ Option 1: Update specific section
  │   ├─ Ask: Which section? (exterior / interior / photos)
  │   ├─ Load current values from visual-context.json
  │   ├─ Ask: What to change?
  │   ├─ Collect updates
  │   ├─ Merge with existing data
  │   └─ Re-save with updated timestamp
  │
  ├─ Option 2: Full refresh
  │   └─ Clear visual-context.json
  │   └─ Run complete 3-phase interview (see above)
  │
  ├─ Option 3: View current context
  │   ├─ Display formatted visual-context.json
  │   └─ Ask: Update anything?
  │       ├─ If yes: Go to "Update specific section" above
  │       └─ If no: Exit
  │
  └─ Option 4: Cancel (no changes)
```

---

## Auto-Population Sources

When skill runs, it auto-loads from these files (if they exist):

| File | Data Auto-Populated | Used In |
|------|-------------------|---------|
| **project-config.json** | project_code, address, building_type, occupancy, SF | Step 1.1 |
| **plans-spatial.json** | room_types, areas, dimensions | Step 2.3 (materials by room type) |
| **specs-quality.json** | finish_schedule, material_specs, casework_specs | Step 2.3 (defaults) |
| **schedule.json** | current_phase, milestone_dates | Step 1.8 (construction status) |
| **directory.json** | architect, owner, contacts | Design preference context |

**Display Pattern:**
```
Pre-populated Data:
  Project: PJ-825021
  Address: Morehead, KY
  Type: Healthcare / Senior Care (149 occupants)
  Size: 9,980 SF
  Current Phase: Foundation / Sitework

Are these correct? (yes/no/edit)
```

If user edits, updated values carry through interview.

---

## Interview Questions by Phase

### PHASE 1: EXTERIOR CONTEXT (40+ questions)

**Step 1.2: Setting Type**
- "What best describes the site setting?"
  - Rural — farmland, open countryside, minimal nearby structures
  - Suburban — residential neighborhoods, scattered commercial, green space
  - Urban — dense development, city block, multiple adjacent buildings, minimal green
  - Industrial — manufacturing area, warehouses, commercial corridors, paved surfaces
  - Campus — institutional grounds, multiple buildings with open space
  - Mixed — combination of above

**Step 1.3: Terrain**
- "Describe the terrain around the building"
  - Flat / Sloping/Rolling / Hillside / Valley / Elevated/Promontory
  - "Any additional details?" (free-form)

**Step 1.4: Adjacent Structures (4 cardinal directions)**
For North, South, East, West:
- "Type of adjacent structure?" (residential, commercial, industrial, open land, water, etc.)
- "Distance?" (immediate neighbor, across street, far away, not applicable)
- "Height relative to building?" (taller, similar, shorter)
- "Notable features?" (parking lots, vegetation screening, etc.)

**Step 1.5: Vegetation**
- "Describe existing vegetation on or near site"
  - Types of trees (deciduous, conifer, mixed)
  - Density (sparse, scattered, dense forest)
  - Ground cover (grass, shrubs, bare soil, paved)
- "Is landscaping planned?" (yes/no/unknown)
  - If yes: "Describe the landscaping intent"

**Step 1.6: Climate**
- "Select the climate zone" (Four-season, Mild winter, Tropical, Arid, Mediterranean, Monsoon)
- "What is the region/zone?" (e.g., "USDA Zone 6a")
- "Which season best represents this project?" (Spring, Summer, Fall, Winter)
- "What is the prevailing weather?" (clear skies, partly cloudy, dramatic clouds, fog, etc.)

**Step 1.7: Building Orientation**
- "Which direction does the main entry face?" (N, NE, E, SE, S, SW, W, NW)
- "Which elevation faces north?" (long side, short side, corner)
- "Where is parking located?" (south and east, detached lot, below building, etc.)
- "Describe the sun path in your region" (low southern sun, high overhead, western glare, etc.)

**Step 1.8: Construction Status**
- "Are these details accurate?" (current phase, visible work, equipment)
- "Anything to add or correct?"

**Step 1.9: Site Photos**
- "Would you like to upload site photos?" (yes/no)
- If yes: "Upload in these categories" (aerial, street, adjacent, terrain, vegetation, conditions, interior_reference)
- "Any other exterior details to capture?" (free-form)

---

### PHASE 2: INTERIOR DESIGN INTENT (25+ questions)

**Step 2.1: Design Character**
- "What is the design character?"
  - warm_residential — comfortable, lived-in feeling
  - modern — clean lines, minimalist, contemporary
  - clinical — healthcare aesthetic, hygienic, functional
  - hospitality — welcoming, refined, service-oriented
  - institutional — durable, formal, rule-based
  - industrial — raw materials, exposed systems
  - corporate — professional, polished, branded
  - educational — flexible, inspiring, activity-focused
  - retail — product-focused, dynamic, customer-facing

**Step 2.2: Color Palette**
- "Describe the primary color" (e.g., "warm gray")
- "What is the secondary color?" (e.g., "light gray")
- "What is the accent color?" (e.g., "warm copper")
- "Do you have inspiration photos?" (yes/no)

**Step 2.3: Materials by Room Type**
For each room type in plans (e.g., Bedroom, Bathroom, Corridor, Kitchen, etc.):

*Flooring*
- "What flooring material?" (polished concrete, ceramic tile, vinyl plank, natural wood, rubber, etc.)
- "What finish/color?" (light gray, warm oak, matte, polished, etc.)

*Walls*
- "How are walls finished?" (painted gypsum, tile wainscot, wood paneling, exposed CMU, vinyl, etc.)
- "What color/material?" (soft white, warm gray, natural wood, etc.)

*Ceiling*
- "What is the ceiling type?" (gypsum board, acoustic tile, exposed structure, beam, coffered, etc.)
- "What color/finish?" (bright white, light gray, natural wood, black steel, etc.)

*Base*
- "What base/trim material and finish?" (painted wood, cove base rubber, natural wood, anodized aluminum, etc.)

*Casework* (if applicable)
- "Describe casework, cabinets, built-ins" (natural wood, shaker style, stainless steel, open shelving, etc.)

*Countertops* (if applicable)
- "What countertop material and finish?" (quartz white, solid surface gray, stainless steel, sealed wood, etc.)

*Hardware*
- "What is the hardware finish?" (polished chrome, brushed nickel, bronze, oil-rubbed bronze, stainless, etc.)

*Furniture*
- "Describe furniture style for [Room Type]" (modern minimalist, warm residential, clinical institutional, etc.)
- "Any special features or equipment?" (picture rails, niches, accent lighting, accent wall, fireplace, etc.)

**Step 2.4: Brand Standards**
- "Are there brand standards or design guidelines?" (yes/no)
- If yes: "Please describe" (brand requirements, owner preferences, sustainability focus, etc.)

**Step 2.5: Special Notes**
- "Any special design notes or unique features?" (free-form)
  - Examples: historic preservation, high-end hospitality, adaptable spaces, daylit atrium, etc.

---

### PHASE 3: PHOTO DOCUMENTATION (8+ questions)

**Step 3.1: Review Uploaded Photos**
- "Would you like to upload additional inspiration or reference photos?" (yes/no)
- If yes: Accept categories (aerial, street, adjacent, terrain, vegetation, conditions, interior_reference, inspiration)

**Step 3.2: AI Analysis**
- For each photo: "Analyzing..." → Generate description
  - Captures: scene composition, materials, atmospheric qualities, context, features

**Step 3.3: Missing Photos**
- If no photos: "Would you like to upload site photos now?" (yes/no/skip)

---

## Data Flow Diagram

```
Input Sources:
  ├─ project-config.json ─┐
  ├─ plans-spatial.json   │
  ├─ specs-quality.json   │
  ├─ schedule.json        ├──→ Auto-Populate in Interview
  ├─ directory.json       │
  └─ User Interview ──────┘

Interview Process:
  Phase 1 (Exterior) ──┐
  Phase 2 (Interior) ──┼──→ Skill Logic ──→ Validation ──→ Merge
  Phase 3 (Photos) ────┘                         ↓
                                          visual-context.json
                                                 ↓
                                    AI - Project Brain/ folder

Output Uses:
  visual-context.json ──→ rendering-generator skill ──→ /render command
                       ──→ visual-context-view
                       ──→ visual-context-export
```

---

## Validation & Saving

Before saving, visual-context.json is validated against schema:

```json
{
  "version": "1.0.0" ✓ (required, const)
  "project_code": "PJ-825021" ✓ (required, string)
  "last_updated": "2026-02-19T14:30:00Z" ✓ (required, ISO 8601)
  "exterior": { ✓ (required)
    "setting": { ... } ✓ (required if exterior exists)
    "vegetation": { ... }
    "climate": { ... }
    "orientation": { ... }
    "photos": [ ... ]
    "construction_status": { ... }
  },
  "interior": { ✓ (required)
    "design_character": "clinical" ✓ (required, enum)
    "color_palette": { ... }
    "materials_by_room_type": { ... }
    "furniture_by_room_type": { ... }
    "brand_standards": "..."
    "special_notes": "..."
  }
}
```

Save path: `/AI - Project Brain/visual-context.json`

Success message:
```
✓ visual-context.json saved to: AI - Project Brain/

NEXT STEPS:
1. Use /render command to generate AI renderings
2. Share renderings with stakeholders for design review
3. Return to /site-context to update context as project evolves
```

---

## Special Cases & Adaptations

### Multi-Story Buildings
1. Ask: "Are material finishes the same on all floors?"
2. If no: "Specify differences by floor"
3. Store in materials_by_room_type with floor identifiers:
   ```
   "Bedroom-L1": { ... }
   "Bedroom-L2": { ... }
   "Common_Area-Ground": { ... }
   "Common_Area-L2": { ... }
   ```

### Renovation Projects
1. Ask: "Should we document existing conditions?"
2. If yes: "Describe existing materials you plan to preserve/replace"
3. Store in special_notes:
   ```
   "Preserve: Original 1950s wood beam ceiling in entry
    Replace: Existing vinyl flooring with polished concrete
    Add: New interior partition walls for flexible layout"
   ```

### Healthcare Buildings (MOSC Example)
- Emphasize clinical character questions
- Ask about accessibility features
- Include wayfinding and patient flow
- Note infection control material requirements
- Ask about staff/resident color preferences

### Industrial Buildings
- Downplay warm_residential character
- Emphasize industrial materials (raw steel, concrete, polished metal)
- Ask about equipment visibility
- Note durability requirements
- Ask about safety markings/wayfinding

---

## Error Recovery

| Error | Recovery |
|-------|----------|
| Missing project files | Proceed with manual input; skip auto-population |
| No room types found | Ask user to manually list room types |
| Photo upload fails | Error message + retry option; can skip and add later |
| Invalid JSON generated | Display validation error; ask user to review conflicting data |
| Multi-story ambiguity | Ask "Same finishes on all floors?" to clarify |
| Incomplete data at save | Show missing required fields; offer to fill in before saving |

---

## Post-Interview

After visual-context.json saves:

```
Display:
  ✓ VISUAL CONTEXT COMPLETE
    Project: [code]
    Updated: [timestamp]
    Sections: Exterior (6 sub-sections), Interior (6 properties)
    Photos: [count] uploaded
    Status: Ready for /render command

Offer:
  - View current context (/visual-context-view)
  - Export report (/visual-context-export)
  - Generate renderings (/render)
  - Update specific section (/site-context)
  - Close
```

---

## Tips for Best Results

**Site Photos:**
- Aerial view shows overall context and topography
- Street-level shows building approach
- Cardinal directions show all sides
- Existing conditions important for renovations
- Close-ups show vegetation, terrain, materials

**Design Intent:**
- Be specific with colors ("warm gray" not just "gray")
- Include 3-5 inspiration photos
- Describe finishes precisely (e.g., "polished concrete, light gray" not just "concrete")
- Note if finishes vary by area (e.g., "entry high-end marble, corridors polished concrete")

**Timing:**
- Run after project kickoff, before design freezes
- Update at major phase changes
- Use renderings to validate direction with stakeholders

---

## Version History

**v1.0.0** (Feb 2026)
- Initial release for Foreman OS v3.0
- 3-phase interview: Exterior → Interior → Photos
- Auto-population from project files
- Incremental update support
- Universal design for any building type
- AI-powered photo analysis
