---
name: rendering-generator
description: >
  AI architectural rendering system with comprehensive prompt engineering. Constructs precise
  image generation prompts from project data and visual context, orchestrates generation through
  the image-generation-mcp server, and manages the rendering gallery.
version: 1.0.0
---

# Rendering Generator Skill

## Overview

Generate professional architectural renderings from project data using advanced prompt engineering. This skill translates construction specifications into precise visual descriptions that AI image generators understand, maintaining consistency and photorealistic quality across multiple views and phases.

The rendering-generator is the prompt engineering brain of the entire rendering system, responsible for:
- Constructing precise image generation prompts from project data
- Orchestrating generation through the image-generation-mcp server
- Managing the rendering gallery and metadata
- Ensuring consistency across multiple views and construction phases

## Command Syntax

```
/render [type] [options]
```

### Command Types

#### Exterior Renderings

```
/render exterior-south              → South elevation, photorealistic, golden hour
/render exterior-north              → North elevation (rear)
/render exterior-east               → East endwall
/render exterior-west               → West endwall
/render exterior-aerial             → Bird's eye drone view, 45-degree angle
/render exterior-3quarter           → Classic 3/4 southeast perspective
/render exterior-3quarter-sw        → 3/4 southwest perspective
/render exterior-street             → Street approach view
/render exterior-entry              → Main entry close-up detail
```

#### Interior Renderings

```
/render interior-bedroom            → Typical bedroom interior
/render interior-bedroom-101        → Specific room 101
/render interior-common             → Common area (lounge/gathering space)
/render interior-kitchen            → Kitchen area
/render interior-restroom           → Restroom/bathroom
/render interior-corridor           → Typical corridor
/render interior-lobby              → Lobby/reception area
/render interior-office             → Office/administrative space
/render interior-mechanical         → Mechanical room
/render interior-laundry            → Laundry room
```

#### Construction Progress Renderings

```
/render progress-existing           → Existing site conditions
/render progress-excavation         → Active excavation phase
/render progress-foundation         → Foundation forming/concrete
/render progress-steel              → PEMB steel erection
/render progress-dried-in           → Envelope closed, roof complete
/render progress-rough-in           → MEP rough-in phase
/render progress-finishes           → Finishing phase, near complete
/render progress-complete           → Final completed building
```

#### Schematic Renderings

```
/render site-plan                   → Overhead site plan (SVG, deterministic)
/render floor-plan                  → Floor plan with furniture layout (SVG)
/render isometric                   → 3D isometric view (SVG)
/render schematic-diagram           → Architectural schematic (SVG)
```

### Command Options

```
--style=photorealistic|illustration|watercolor|diagram
  Default: photorealistic for exteriors/real interiors, diagram for technical
  Applies appropriate modifiers and rendering approach

--lighting=golden_hour|midday|overcast|dusk|dawn
  Default: golden_hour for hero shots, midday for documentation
  Overrides default based on rendering type

--api=gemini|flux2|svg
  Default: auto-selected based on type (see API Selection Logic below)
  Override default API if needed

--season=spring|summer|fall|winter
  Default: current season or as-designed
  Affects landscape, vegetation, sky conditions

--time-of-day=sunrise|morning|midday|afternoon|golden_hour|dusk|night
  Alias for --lighting parameter
  More specific control than --lighting

--quality=draft|standard|hero
  draft: Quick exploration, lower resolution
  standard: Full quality production rendering
  hero: Maximum quality, potential multi-pass generation
  Default: standard

--reference-from=[previous render ID]
  Use a previous rendering as visual reference for consistency
  Maintains material colors, proportions, architectural details

--camera-distance=distance-multiplier
  Default: 1.0x (standard distance)
  Adjust viewing distance: 0.5x (close detail), 1.5x (wider context)

--occupancy-level=empty|sparsely_occupied|fully_occupied
  Default: depends on context
  Controls visibility of people and furniture
```

## How It Works

### Processing Pipeline

1. **Parse Command**
   - Extract type, target, and all options
   - Apply defaults from project context

2. **Read Project Data**
   - Load from `AI - Project Brain/`:
     - `project-config.json` (project name, code, location, address)
     - `plans-spatial.json` (dimensions, layout, grid)
     - `specs-quality.json` (materials, finishes, quality standards)
     - `schedule-construction.json` (current phase, dates)
     - `building-assembly.json` (PEMB specs, structural details)
     - `mep-equipment.json` (HVAC, plumbing, electrical specs)
     - `project-site-context.json` (terrain, location, climate)

3. **Load Visual Context**
   - If `visual-context.json` exists (generated by `/site-context`):
     - Use site-specific details (terrain, vegetation, adjacent structures)
     - Interior finishes preferences
     - Color palette
     - Architectural character
   - If not exists:
     - Use generic architectural defaults
     - Suggest user run `/site-context` for enhanced results

4. **Select Prompt Template**
   - Choose from `references/` based on rendering type:
     - Exteriors: `exterior-templates.md`
     - Interiors: `interior-templates.md`
     - Progress: `progress-templates.md`
   - Apply building-type adjustments from `building-types.md`
   - Load style modifiers from `style-guides.md`

5. **Assemble Full Prompt**
   - Fill {{variable}} placeholders with:
     - Project data from step 2
     - Visual context from step 3
     - Camera specs from `camera-angles.md`
     - Lighting parameters from `lighting-conditions.md`
     - Material translations from `material-vocabulary.md`
   - Append avoidance terms from `avoidance-terms.md`
   - Apply consistency rules from `consistency-guide.md`

6. **Select API**
   - Based on rendering type and user override (see API Selection Logic)
   - Log selection in rendering-log.json

7. **Generate Image**
   - Call image-generation-mcp server:
     - `generate_image_flux2(prompt, style, dimensions, seed)` for Flux 2
     - `generate_image_gemini(prompt, style, dimensions)` for Gemini
     - `generate_svg(spec)` for vector outputs
   - Handle retries and error conditions

8. **Save Output**
   - File location: `10 - Project Photos/Renderings/`
   - Filename pattern: `{PROJECT_CODE}_render_{type}_{date}_{seq}.{ext}`
     - Example: `MOSC_render_exterior-south_2026-02-19_01.png`
   - Save metadata to `AI - Project Brain/rendering-log.json`

9. **Update Log**
   - Add entry to rendering-log.json with:
     - Timestamp, rendering ID, type, camera angle
     - Full prompt used
     - API used, model version
     - Generation parameters (style, lighting, season)
     - Quality metrics if available
     - User who generated

10. **Display Result**
    - Show rendered image to user
    - Display metadata: camera specs, materials, lighting, generation time
    - Provide gallery link for viewing alongside other renderings
    - Suggest consistency checks if part of a set

## API Selection Logic

| Rendering Type | Default API | Reasoning | Alternative |
|---|---|---|---|
| SVG floor plan, site plan, isometric | Built-in SVG | Deterministic, instant, always available, perfect geometry | N/A |
| Quick concept / exploration | Gemini | Fast (~3s), cost-effective, good for iteration | Flux 2 for higher quality |
| Quality exterior (hero shot) | Gemini | Multi-reference support, excellent 4K output, fine details | Flux 2 for best photorealism |
| Quality interior (finishes detail) | Gemini | Better at material specification details, lighting control | Flux 2 for dramatic interiors |
| Construction progress | Gemini | Good at complex scene composition, equipment detail | Flux 2 for photorealism |
| Final presentation / marketing | Flux 2 | Best overall photorealistic quality, highest fidelity | Gemini as backup |
| Consistency set (multiple angles) | Gemini | Faster generation of full set, reference image support | Flux 2 for hero only |

**User Override:** Any command can specify `--api=flux2` or `--api=gemini` to override default.

**Cost Optimization:**
- For exploration phases: Gemini (faster, cheaper)
- For approval/presentation: Gemini with quality=hero or Flux 2
- For full sets: Gemini for speed, Flux 2 for 1-2 hero shots

## Output Management

### File Organization

```
10 - Project Photos/
├── Renderings/
│   ├── Exteriors/
│   │   ├── MOSC_render_exterior-south_2026-02-19_01.png
│   │   ├── MOSC_render_exterior-south_2026-02-19_01.meta
│   │   ├── MOSC_render_exterior-3quarter_2026-02-19_01.png
│   │   └── ...
│   ├── Interiors/
│   │   ├── MOSC_render_interior-bedroom_2026-02-19_01.png
│   │   ├── MOSC_render_interior-common_2026-02-19_01.png
│   │   └── ...
│   ├── Progress/
│   │   ├── MOSC_render_progress-foundation_2026-02-19_01.png
│   │   ├── MOSC_render_progress-steel_2026-02-19_01.png
│   │   └── ...
│   └── Schematics/
│       ├── MOSC_render_site-plan_2026-02-19_01.svg
│       ├── MOSC_render_floor-plan_2026-02-19_01.svg
│       └── ...

AI - Project Brain/
└── rendering-log.json
```

### Rendering Log Format

```json
{
  "project_code": "MOSC",
  "renders": [
    {
      "id": "render_exterior-south_2026-02-19_001",
      "type": "exterior",
      "subtype": "south-elevation",
      "timestamp": "2026-02-19T14:30:00Z",
      "api_used": "gemini",
      "model_version": "gemini-2.0-flash",
      "style": "photorealistic",
      "lighting": "golden_hour",
      "season": "winter",
      "camera_spec": "35mm equivalent, eye-level, from parking lot, horizontal frame",
      "dimensions": "1920x1080",
      "full_prompt": "[full prompt text used]",
      "generation_time_seconds": 4.2,
      "quality_score": 0.92,
      "generated_by": "andrew@wprinciples.com",
      "file_path": "10 - Project Photos/Renderings/Exteriors/MOSC_render_exterior-south_2026-02-19_01.png",
      "thumbnail_url": "...",
      "notes": "Reference for consistency in other angles",
      "tags": ["hero-shot", "presentation-ready", "golden-hour"]
    }
  ]
}
```

### Gallery Dashboard

Renderings are viewable in `/data` dashboard under **Renderings** section with:
- Thumbnail grid by category (Exteriors, Interiors, Progress, Schematics)
- Filter by type, date, style, lighting
- Consistency checker (flag materials/colors that differ across set)
- Export options (presentations, reports, social media)

## Template-Based & Universal

All prompt templates use {{variable}} placeholder syntax, making this system work for ANY building type:

- **PEMB / Metal Buildings** — Crisp panel lines, clear span structure
- **Healthcare / Senior Care** — Residential scale, accessible features, warm materials
- **Commercial / Retail** — Storefront glazing, brand expression
- **Industrial / Warehouse** — Large scale, functional aesthetic
- **Residential** — Human scale, pitched roofs, neighborhood context
- **Multi-Story** — Vertical composition, floor articulation
- **Renovation / Addition** — Material transitions between existing and new
- **Education** — Campus setting, durable materials
- **Hospitality** — Welcoming entry, landscape quality

Building-type-specific adjustments are loaded from `building-types.md` and applied automatically based on project occupancy type.

## Visual Context Enhancement

### With Visual Context (Recommended)

If `visual-context.json` exists (generated by `/site-context`), prompts are enriched with:
- Specific site terrain and topography
- Real vegetation and landscaping plans
- Adjacent structures and context
- Interior material preferences and color palette
- Architectural character and design intent
- Climate-specific conditions

**Result:** Renderings reflect site-specific character and design intent with accuracy.

### Without Visual Context (Functional Default)

If `visual-context.json` does not exist:
- Use generic architectural defaults
- Apply standard material colors (neutral grays, warm tones)
- Use generic landscaping (appropriate trees/shrubs for climate zone)
- Display message suggesting: *"Run `/site-context` for enhanced results reflecting your specific site and design"*

**Result:** Still produces professional renderings, but less site-specific.

## Consistency Across Rendering Sets

When generating multiple views of the same building:

1. **Generate Hero Rendering First**
   - South elevation, photorealistic, golden hour (default)
   - This becomes the master reference

2. **Store Master Specification**
   - Save exact building description prompt used
   - Log material colors, dimensions, style

3. **Reuse Specifications**
   - Apply identical material/dimension language to all angles
   - Same site context (season, vegetation state)
   - Same weather/sky conditions

4. **Use Reference Images**
   - When available, pass hero rendering as reference image input
   - For Gemini: supports reference images for consistency
   - For Flux 2: reuse seeds when generating variations

5. **Post-Generation Validation**
   - Compare adjacent views for:
     - Material color continuity
     - Fenestration alignment
     - Roof geometry consistency
   - Log any adjustments needed

## Error Handling & Retries

- **Generation Timeout:** Retry up to 3x with slight prompt adjustment
- **API Unavailable:** Fall back to alternative API (Gemini → Flux 2)
- **Invalid Prompt:** Log error, suggest manual refinement
- **Image Quality Issues:** Flag for user review, suggest regeneration with different parameters

## Prompt Engineering Best Practices

### Golden Rules

1. **Specificity** — Use exact measurements, material names, architectural terms
2. **Visual Language** — Translate specs into what AI "sees" (texture, color, reflection, light)
3. **Constraint Clarity** — Describe what SHOULD be visible (accurate geometry, proper proportions)
4. **Reference Grounding** — Use real-world architectural examples and standards
5. **Consistency** — Reuse exact phrasing across related prompts

### Template Variable System

All templates use `{{VARIABLE}}` syntax. During prompt assembly:
- Replace `{{building_width}}` with actual value from project-config.json
- Replace `{{wall_cladding_description}}` with visual translation from material-vocabulary.md
- Replace `{{lighting_description}}` with full lighting parameter set from lighting-conditions.md

### Material Translation Examples

Spec language → Visual language:
- "Standing seam metal roof" → "Standing seam metal roof with crisp vertical rib lines, [color], subtle reflections"
- "VCT flooring" → "Commercial vinyl composition tile, 12x12 grid pattern, slight sheen, neutral tone"
- "Solid surface countertop" → "Solid surface seamless countertop, [color/pattern], integrated backsplash, matte finish"

## Commands Available

- `/render [type] [options]` — Main rendering command
- `/render-list` — Show all available rendering types
- `/render-gallery` — View rendering gallery dashboard
- `/render-log` — View rendering generation log
- `/render-consistency-check [set-id]` — Validate consistency across multiple renders
- `/render-delete [render-id]` — Remove rendering from gallery
- `/render-export [render-id] --format=pdf|pptx|web` — Export for presentations
- `/site-context` — Generate visual context data (prerequisite for enhanced renderings)

## File Structure

```
rendering-generator/
├── SKILL.md                          # Main skill documentation (this file)
├── skill-controller.js               # Main skill execution logic
├── prompt-assembler.js               # Template variable substitution engine
├── api-selector.js                   # API selection logic
├── references/
│   ├── exterior-templates.md         # Complete exterior angle templates
│   ├── interior-templates.md         # Complete interior space templates
│   ├── progress-templates.md         # Construction phase progression
│   ├── building-types.md             # Type-specific adjustments
│   ├── material-vocabulary.md        # Spec-to-visual translation
│   ├── camera-angles.md              # Camera specifications
│   ├── lighting-conditions.md        # Lighting parameter sets
│   ├── consistency-guide.md          # Multi-angle consistency rules
│   ├── style-guides.md               # Style modifier sets
│   └── avoidance-terms.md            # Positive-framed artifact prevention
└── utils/
    ├── gallery-manager.js            # Rendering gallery operations
    ├── log-manager.js                # Rendering log tracking
    └── validators.js                 # Prompt validation
```

## Integration Points

- **Image Generation MCP Server:** `generate_image_flux2()`, `generate_image_gemini()`, `generate_svg()`
- **Project Brain:** Reads from `AI - Project Brain/` for all project data
- **Foreman OS Dashboard:** Displays gallery and metrics in `/data` interface
- **Site Context Skill:** Uses output from `/site-context` when available

## Performance Notes

- Gemini: ~3-4 seconds per rendering
- Flux 2: ~15-20 seconds per rendering
- SVG: <1 second (deterministic)
- Full exterior set (6 views, Gemini): ~20-25 seconds total
- Full exterior set (6 views, Flux 2): ~2-2.5 minutes total

## Version History

- **v1.0.0** (2026-02-19) — Initial release with comprehensive prompt engineering system
