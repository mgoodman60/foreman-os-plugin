# project-visual-context — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the project-visual-context skill.



## Phase 3: Photo Documentation

### Step 3.1: Review Uploaded Photos

If photos were uploaded in Phase 1, display them:

```
UPLOADED PHOTOS
[photo 1 filename] — [category] — [AI analysis]
[photo 2 filename] — [category] — [AI analysis]
...
```

Ask: "Would you like to upload **additional inspiration or reference photos**?" (yes/no)

If yes:
- Invite user to upload more photos
- Accept categories: aerial, street, adjacent, terrain, vegetation, conditions, interior_reference, inspiration
- For each new photo:
  - Capture filename, category, direction (if applicable)
  - Use AI vision to generate description
  - Store in visual-context.json

### Step 3.2: Photo Descriptions

For each uploaded photo, the skill uses AI vision to generate a detailed description capturing:
- **Scene composition** — what's in the photo, scale, perspective
- **Materials visible** — colors, textures, conditions
- **Atmospheric qualities** — lighting, weather, time of day
- **Context clues** — adjacent structures, vegetation, hardscape, utilities visible
- **Notable features** — architectural details, landscape elements, construction progress

Store descriptions in visual-context.json under `exterior.photos[].analysis`.

Example:
```
{
  "id": "photo_001",
  "file": "site_aerial_02_2026.jpg",
  "type": "aerial",
  "direction": "north",
  "analysis": "Aerial view of 10-acre rural site in winter condition. Building footprint is cleared and graded, with concrete foundation work in progress. Mature deciduous trees line the southern and eastern property boundaries. Open rolling topography slopes gently northward. Gravel access road enters from the west. No adjacent structures visible within 500 feet. Overcast sky, ground conditions appear slightly moist."
}
```

### Step 3.3: Missing Photos Alert

If Phase 3 completes with few/no photos uploaded, ask:

"No photos uploaded yet. For best rendering results, would you like to upload **site photos** now? (yes/no/skip)"

If no: "You can always re-run `/site-context` to add photos later."

### End of Phase 3

Summarize photos:
```
PHOTO DOCUMENTATION
Total Photos: [count]
Categories: [aerial: 2, street: 1, terrain: 1, ...]
AI Descriptions Generated: [count]
```

---



## Finalizing and Saving

### Step 4.1: Final Review

Display the complete visual-context summary:

```
═══════════════════════════════════════════════════════════
VISUAL CONTEXT COMPLETE
═══════════════════════════════════════════════════════════

PROJECT: [project_code]
Last Updated: [timestamp]

EXTERIOR CONTEXT
  Setting: [type]
  Terrain: [description]
  Adjacent Structures: [N/S/E/W summary]
  Vegetation: [description]
  Climate: [zone/region] — [default season]
  Building Orientation: Faces [direction] | Entry [direction]
  Photos: [count] uploaded

INTERIOR DESIGN
  Character: [type]
  Colors: [primary] | [secondary] | [accent]
  Room Types: [count] documented
  Special Notes: [summary or "none"]

DOCUMENTATION
  Total Photos: [count]
  Next Steps: Ready for `/render` command
═══════════════════════════════════════════════════════════
```

Ask: "Does everything look correct? (yes/edit/add)"

If user selects edit or add:
- Ask: "Which section would you like to update? (exterior / interior / photos / all)"
- Jump to relevant phase and allow incremental updates

If yes:
- Proceed to save

### Step 4.2: Save visual-context.json

The skill generates visual-context.json following the schema in `/references/visual-context-schema.json`.

Structure:
```json
{
  "version": "1.0.0",
  "project_code": "[from project-config]",
  "last_updated": "[ISO 8601 timestamp]",
  "exterior": {
    "setting": { ... },
    "vegetation": { ... },
    "climate": { ... },
    "orientation": { ... },
    "photos": [ ... ],
    "construction_status": { ... }
  },
  "interior": {
    "design_character": "...",
    "color_palette": { ... },
    "materials_by_room_type": { ... },
    "furniture_by_room_type": { ... },
    "brand_standards": "...",
    "special_notes": "..."
  }
}
```

Save to: `AI - Project Brain/visual-context.json`

Display confirmation:
```
✓ visual-context.json saved to: AI - Project Brain/
```

### Step 4.3: Next Steps

Display guidance:

```
NEXT STEPS

1. RUN RENDERINGS
   Use `/render` command with specific elevation, view, or space.
   Example: /render elevation=south, phase=frame-erection, season=summer

2. ITERATE & REFINE
   If rendering quality isn't meeting expectations:
   - Re-run `/site-context` to update specific sections
   - Upload additional reference photos
   - Clarify design details

3. ARCHIVE PROGRESS
   Visual context is now available for the rendering-generator skill.
   Export renderings to stakeholders for design review and approvals.
```

---



## Incremental Updates

If visual-context.json **already exists**, the skill workflow changes:

### Initial Prompt

```
Visual context already exists for this project (last updated: [date]).

What would you like to do?
  1. Update specific section (exterior / interior / photos)
  2. Full refresh (re-run entire interview)
  3. View current context
  4. Cancel

Select: (1/2/3/4)
```

### Workflow: Update Specific Section

If user selects "Update specific section":

Ask: "Which section?"
- **Exterior** — site setting, terrain, adjacent structures, climate, orientation, construction status
- **Interior** — design character, color palette, materials, furniture, special features
- **Photos** — add/replace photos and descriptions

Based on selection:
- Load current section from visual-context.json
- Display current values
- Ask: "What would you like to change?"
- Collect updates
- Merge into existing visual-context.json
- Re-save with updated `last_updated` timestamp

### Workflow: Full Refresh

If user selects "Full refresh":
- Clear visual-context.json
- Run the complete 3-phase interview as described above

### Workflow: View Current Context

If user selects "View current context":
- Display the entire visual-context.json in formatted, readable summary
- Ask: "Would you like to update anything?" (yes/no)
- If yes, return to "Update specific section" workflow

---



## Error Handling & Edge Cases

### Missing Project Data
If required project files don't exist (project-config.json, plans-spatial.json):
- Display warning: "Some project data is missing. The skill will work, but may require more manual input."
- Allow user to proceed
- Skip auto-population steps and ask for manual input instead

### No Room Types Found
If plans-spatial.json doesn't provide room types:
- Ask user to manually list major room types (e.g., "bedroom, bathroom, living area, kitchen")
- Proceed with materials/furniture interview for those types

### Single-Story vs. Multi-Story
If building has multiple stories:
- Ask: "Are material finishes the **same on all floors**? (yes/no)"
- If no: "Please specify any differences by floor" (e.g., "Residential finishes: warm residential, public areas: institutional")
- Adjust interview accordingly

### Renovation vs. New Construction
If project is a renovation:
- Ask: "Should we document **existing conditions**? (yes/no)"
- If yes: "Describe existing materials/finishes you plan to preserve or replace"
- Include in special_notes

### Photo Upload Failures
If user attempts to upload photos but upload fails:
- Display error: "Photo upload failed. Please check file format (JPEG, PNG accepted)."
- Offer to continue interview without photos (can add later)
- Provide retry option

---



## Universal Design Principles

This skill is designed to work for **ANY building type and project phase**.

### Building Type Adaptation
- **Healthcare/Senior Care** (e.g., MOSC) → Emphasizes clinical finishes, accessibility features, wayfinding
- **Commercial Office** → Emphasizes corporate character, brand standards, flexible spaces
- **Retail** → Emphasizes product display, customer experience, dynamic lighting
- **Educational** → Emphasizes collaborative spaces, durability, accessibility
- **Industrial** → Downplays residential warmth; emphasizes functional industrial aesthetic
- **Residential** → Full warm_residential focus; emphasizes comfort and livability

The skill adapts room types, material questions, and design character options based on the building type from project-config.json.

### Project Phase Adaptation
- **Schematic Design** → Focus on design intent, no construction details yet
- **Foundation/Sitework** — Emphasize site context, existing conditions, terrain
- **Frame Erection** → Include construction photos, current building progression
- **Finishes** → Deep dive into material finishes, color palette, furniture placement
- **Punch/Closeout** → Document final conditions and lessons learned

Construction status is auto-populated from schedule.json to reflect current phase.

### Multi-Story Adaptation
For buildings with 2+ stories:
- Ask if finishes differ by floor
- Collect separate material/furniture specs for each floor type if needed
- Store in materials_by_room_type with floor identifier (e.g., "Bedroom-L2" vs. "Bedroom-L1")

---



## Tips for Best Results

### For Site Photos:
- **Aerial** — Shows overall site context, topography, adjacent structures
- **Street level approach** — Shows how building appears to visitors/clients
- **Cardinal directions** — One photo from each direction gives rendering engine full context
- **Existing conditions** — If renovation, document current state

### For Design Intent:
- **Be specific with colors** — "warm gray" is better than "gray"; "sage green" better than "green"
- **Reference images** — Upload 3-5 inspiration photos if available for design character
- **Material samples** — If you have physical samples, describe accurately
- **Budget/Premium tiers** — If finishes vary (e.g., "entry is high-end marble, corridors are polished concrete"), specify

### For Best Renderings:
- Run this skill **before** major design decisions are locked
- Allow time to gather reference photos and finishes information
- Update context as design evolves (materials, color palette changes, design character shifts)
- Use renderings in design reviews to validate direction with stakeholders

---



## File Reference

**Reads from:**
- `project-config.json` — project basics, address, building type
- `plans-spatial.json` — room types, areas, dimensions, door schedule
- `specs-quality.json` — finish schedule, material specs
- `schedule.json` — current phase, milestone dates
- `directory.json` — architect, owner contacts

**Writes to:**
- `AI - Project Brain/visual-context.json` — complete visual context output

**References:**
- `/references/visual-context-schema.json` — JSON schema validation

---



## Commands & Quick Reference

```
/site-context              Start visual context interview (new or update existing)
/render                    Generate AI renderings using visual context
/visual-context-view       Display current visual-context.json
/visual-context-export     Export context to PDF or HTML report
```

---



## Troubleshooting

**Q: "I don't have photos. Can I skip this phase?"**
A: Yes. You can skip photo upload and add photos later by re-running `/site-context` → "Update specific section" → "Photos."

**Q: "Can I update just the color palette without re-doing the whole interior section?"**
A: If visual-context.json exists, yes. Run `/site-context` → "Update specific section" → "Interior," then ask to update only color palette.

**Q: "What if I don't know the design character yet?"**
A: The skill provides clear descriptions of each character type. Choose the closest fit. You can always update later.

**Q: "How detailed should material descriptions be?"**
A: Detailed enough to guide visual rendering — e.g., "polished concrete with gray sealer" rather than just "concrete." Include finish, sheen, approximate color.

**Q: "Should I provide room-by-room material specs?"**
A: No. The skill groups by room TYPE (e.g., "Bedroom," "Bathroom," "Corridor"). If a room type varies significantly, note that in special_notes.

---



## Version History

**v1.0.0** — Initial release for Foreman OS v3.0
- 3-phase interview: Exterior → Interior → Photos
- Auto-population from existing project data
- Incremental update support
- Universal design for any building type and project phase
- AI-powered photo analysis
- visual-context.json output for rendering-generator skill


