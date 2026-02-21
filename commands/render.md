---
description: Generate AI architectural renderings
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [type] [options]
---

Generate architectural renderings using AI image generation, guided by project data and visual context.

Read the rendering-generator skill at `${CLAUDE_PLUGIN_ROOT}/skills/rendering-generator/SKILL.md` before proceeding. Also read `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` for project data retrieval patterns. If the MCP image generation server is available, also read `${CLAUDE_PLUGIN_ROOT}/skills/image-generation-mcp/SKILL.md` for AI image generation capabilities.

## Step 1: Load Data

Read all available project data:
- `project-config.json` for basics
- `plans-spatial.json` for building data
- `specs-quality.json` for materials
- `visual-context.json` for site and interior context
- `rendering-log.json` for previous renderings

If no visual-context.json exists, warn: "No visual context found. Renderings will use generic site assumptions. Run /site-context for better results."

## Step 2: Parse Arguments

Parse $ARGUMENTS for rendering type and options:
- Type: exterior-south, exterior-north, exterior-aerial, exterior-3quarter, interior-bedroom, interior-{room_number}, progress-{phase}, site-plan, schematic
- Options: --style=, --lighting=, --api=, --season=

Default: exterior-south, photorealistic, golden_hour, gemini

## Step 3: Build Prompt

Using the reference templates in `${CLAUDE_PLUGIN_ROOT}/skills/rendering-generator/references/`:

1. Select the appropriate template file based on rendering type
2. Assemble the prompt by filling template variables from project data:
   - Building dimensions, type, structure from spatial data
   - Materials and finishes from specs and visual context
   - Site context from visual-context.json
   - Camera angle from camera-angles.md
   - Lighting from lighting-conditions.md
   - Style modifiers from style-guides.md
   - Avoidance terms from avoidance-terms.md
3. Translate spec terms to visual language using material-vocabulary.md
4. Apply building-type adjustments from building-types.md

## Step 4: Select API

Based on rendering type and --api option:
- SVG types (site-plan, grid, schematic) → Built-in SVG generator (no API needed)
- Quick concept → Gemini (fast, cheap)
- Quality rendering → Gemini Pro (default for most)
- Final presentation → Flux 2 (best photorealistic)
- User override with --api flag

## Step 5: Generate

**For API-based rendering:**
1. Check if image generation MCP tools are available
2. If not → suggest SVG mode or MCP setup
3. Call appropriate MCP tool with assembled prompt
4. Save image to 10 - Project Photos/Renderings/
5. Filename: {PROJECT_CODE}_render_{type}_{date}_{sequence}.png

**For SVG rendering:**
1. Read spatial data
2. Generate SVG using built-in logic
3. Save as .svg file

## Step 6: Log and Present

Add entry to rendering-log.json with: id, file path, type, style, lighting, api used, full prompt, timestamp, visual context version.

Present the rendering to the user with the file path. Suggest related renderings they might want to generate next.

Update `project-config.json` version_history:
```
[TIMESTAMP] | render | [type] | [filename]
```
