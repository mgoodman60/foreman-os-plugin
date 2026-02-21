---
description: Gather visual context for AI renderings
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [site|interior|photos|all]
---

Gather visual context about the project site and interior design intent for use in AI-rendered architectural visualizations.

Read the project-visual-context skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-visual-context/SKILL.md` before proceeding. Also read `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` for project data retrieval patterns.

## Step 1: Load Existing Data

Read project data files to pre-fill what's already known:
- `project-config.json` for project basics (building type, location, dimensions)
- `plans-spatial.json` for building data (rooms, finishes, MEP)
- `specs-quality.json` for material specifications
- `visual-context.json` if it already exists (update mode)

## Step 2: Determine Scope

Based on the argument ($ARGUMENTS):
- `site` → Only gather site/exterior context
- `interior` → Only gather interior design context
- `photos` → Only process uploaded site photos
- `all` or no argument → Full context gathering

## Step 3: Site Context Interview

If gathering site context, ask the user conversationally about:
1. Site setting (rural/suburban/urban, topography)
2. Surroundings (what's adjacent on each side)
3. Vegetation (trees, ground cover, planned landscaping)
4. Climate and typical weather
5. Building orientation (which way does the main entry face)
6. Current construction status (what's visible now)

Pre-fill from project data where possible. Only ask what's unknown.

## Step 4: Photo Processing

If the user uploads site photos:
1. Analyze each photo (Claude can see images)
2. Describe what the photo shows
3. Classify: aerial, street view, adjacent property, terrain, vegetation, site conditions
4. Note direction the camera is facing
5. Store photo metadata in the visual context

## Step 5: Interior Context

If gathering interior context:
1. Determine design character from specs/finish schedule
2. Build materials_by_room_type from finish schedule data
3. Ask about furniture intent, casework style, color palette
4. Ask about any brand standards or owner preferences
5. Note specialties by room type (grab bars, nurse call, signage, etc.)

## Step 6: Save

Save to `visual-context.json` in AI - Project Brain/.
Report what was gathered and what's still missing.
Suggest: "Run /render to generate architectural renderings using this context."

Update `project-config.json` version_history:
```
[TIMESTAMP] | site-context | [scope] | visual-context.json updated
```
