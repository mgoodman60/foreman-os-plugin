---
name: project-visual-context
description: >
  Gather site context, exterior conditions, and interior design intent for AI rendering. Trigger phrases include "site context", "visual context", "gather context", "rendering context". Dependencies: project-config, plans-spatial, specs-quality, schedule, directory.
version: 1.0.0
---

# Project Visual Context Skill

## Overview

The **project-visual-context** skill guides you through a structured interview to gather comprehensive visual context about your construction project. This context enables the rendering-generator skill to produce accurate, photorealistic AI renderings at any project phase.

Visual context includes:
- **Exterior conditions**: site setting, terrain, adjacent structures, vegetation, climate, orientation
- **Interior design intent**: design character, color palette, materials by room type, furniture, special features
- **Photo documentation**: site photos with AI-generated descriptions for reference

## When to Use

**Trigger:** `/site-context` command

**Timing:**
- Run BEFORE `/render` for best results
- Re-run at major project phases to update context as conditions change
- Partial updates welcome — update only what's changed

**Best Results:** Run after project kick-off, before major design/construction phases

## How the Skill Works

The skill operates in **3 phases** over a single session:

1. **Exterior Context** — Gather site setting, terrain, adjacent structures, vegetation, climate, orientation, construction status
2. **Interior Design Intent** — Gather design character, color palette, finishes, furniture, and special features by room type
3. **Photo Documentation** — Process uploaded site/inspiration photos with AI analysis

At the end, the skill generates **visual-context.json** saved to `AI - Project Brain/` folder.

## Starting the Skill

### Initial Setup

When you trigger `/site-context`:

1. The skill checks if **visual-context.json** already exists
   - **If EXISTS:** Load it and ask "What would you like to update? (exterior / interior / photos / all)" → Jump to incremental update workflow
   - **If NEW:** Proceed with full interview below

2. The skill auto-populates data from existing project files:
   - **project-config.json** → `project_code`, building type, address, occupancy
   - **plans-spatial.json** → room types, areas, dimensions, door schedule
   - **specs-quality.json** → finish schedule, material specs, casework specs
   - **schedule.json** → current phase
   - **directory.json** → architect, owner contacts (for design preferences)

Pre-populated data is shown to the user for confirmation/correction.

---

## Phase 1: Exterior Context

### Step 1.1: Confirm Building Basics

Display pre-populated data:
```
Project: [project_code]
Address: [address]
Building Type: [type] ([occupancy] occupants)
Building Size: [SF]
Current Phase: [phase from schedule]
```

Ask: "Are these details correct? (yes/no/edit)"

If user edits, update the displayed values.

### Step 1.2: Setting Type

Ask: "What best describes the **site setting**?"
- **Rural** — farmland, open countryside, minimal nearby structures
- **Suburban** — residential neighborhoods, scattered commercial, green space
- **Urban** — dense development, city block, multiple adjacent buildings, minimal green
- **Industrial** — manufacturing area, warehouses, commercial corridors, paved surfaces
- **Campus** — institutional grounds (hospital, university, corporate), multiple buildings with open space
- **Mixed** — combination of above characteristics

Capture response.

### Step 1.3: Terrain Description

Ask: "Describe the **terrain** around the building:"
- Flat — level ground
- Sloping/Rolling — gentle elevation changes
- Hillside — significant elevation change, building may be cut into slope
- Valley — building in low point
- Elevated/Promontory — building on high ground

Ask for any additional details (e.g., "hillside with rock outcrops," "flat cleared site in forest").

Capture response.

### Step 1.4: Adjacent Structures

Ask: "Describe buildings/structures **adjacent** to this site in each direction:"

For each cardinal direction (North, South, East, West):
- Type of adjacent structure (residential, commercial, industrial, open land, water, etc.)
- Distance (immediate neighbor, across street, far away)
- Height relative to this building (taller, similar, shorter)
- Any notable features (parking lots, vegetation screening, etc.)

Capture responses for each direction.

### Step 1.5: Vegetation & Landscaping

Ask: "Describe **existing vegetation** on or near the site:"
- Types of trees (deciduous, conifer, mixed)
- Density (sparse, scattered, dense forest)
- Ground cover (grass, shrubs, bare soil, paved)
- Any significant vegetation to be preserved or removed

Ask: "Is **landscaping planned** for this project? (yes/no/unknown)"

If yes: "Describe the landscaping intent" (e.g., "native plantings, bioswale screening to south, street trees along entry drive")

Capture responses.

### Step 1.6: Climate & Season

Ask: "Select the **climate zone** for this location:"

Display options based on address (or ask user):
- **Four-season** (temperate) — spring, summer, fall, winter
- **Mild winter** — cool season, rarely freezes, year-round green
- **Tropical** — warm, high humidity, distinct wet/dry seasons
- **Arid/Desert** — dry, minimal precipitation, extreme temperature swings
- **Mediterranean** — warm dry summer, cool wet winter
- **Monsoon** — distinct rainy season, dry season

Capture response.

Ask: "What is the **region/zone**?" (e.g., "USDA Zone 6a," "Sonoran Desert," "Pacific Northwest")

Ask: "For rendering purposes, which **season** best represents this project?"
- Spring (greening, fresh, moderate light)
- Summer (full foliage, bright, warm light)
- Fall (color change, golden light, clear skies)
- Winter (bare trees, diffuse light, snow possible)

Capture response.

Ask: "What is the **prevailing weather** you expect to show in renderings?" (e.g., "clear skies," "partly cloudy," "dramatic storm clouds," "morning fog")

Capture response.

### Step 1.7: Building Orientation

Ask: "**Which direction does the main entry face?**" (N, NE, E, SE, S, SW, W, NW)

Ask: "Which elevation faces **north**?" (e.g., "long side," "short side," "corner")

Ask: "Where is **parking** located?" (e.g., "south and east," "detached lot to north," "below building")

Ask: "Describe the **sun path** in your region during the default season you selected" (e.g., "low southern sun, dramatic shadows," "high overhead sun, minimal shadows," "strong western afternoon glare")

Capture responses.

### Step 1.8: Construction Status

Auto-populate from schedule if available:
```
Current Phase: [phase]
Expected Visible Work: [construction activities in progress]
Equipment on Site: [cranes, formwork, trailers, etc.]
```

Ask: "Are these details accurate? Anything to add or correct about the current construction status?"

Capture any corrections.

### Step 1.9: Site Photo Upload

Ask: "Would you like to upload **site photos** for reference? (yes/no)"

If yes:
- Invite user to upload photos in these categories:
  - **Aerial view** — drone/satellite view of site
  - **Street level** — approach view from public street
  - **Adjacent contexts** — nearby structures, street context
  - **Terrain** — ground conditions, slopes, drainage
  - **Vegetation** — trees, landscaping, ground cover
  - **Current conditions** — construction progress, existing site conditions
  - **Interior reference** — existing spaces for design intent

For each uploaded photo:
- Capture filename and category
- Use AI vision to analyze and generate description (e.g., "Mature oak trees lining the south property line, 40+ feet tall, dense canopy. Open lawn area extends north toward building site.")
- Store in visual-context.json

Ask: "Any other details about the **exterior/site context** we should capture?" (free-form text)

Capture response.

### End of Phase 1

Summarize exterior context to user:
```
EXTERIOR CONTEXT SUMMARY
Setting: [type]
Terrain: [description]
Adjacent (N/S/E/W): [cardinal descriptions]
Vegetation: [description]
Climate: [zone/region/seasons]
Building Faces: [direction] | Entry: [direction]
Parking: [location]
Photos Uploaded: [count]
```

Ask: "Ready to proceed to **Interior Design Intent**?" (yes/continue)

---

## Phase 2: Interior Design Intent

### Step 2.1: Design Character

Ask: "What is the **design character** of this project?"

Display options and explain:
- **warm_residential** — comfortable, residential aesthetic, lived-in feeling
- **modern** — clean lines, minimalist, contemporary materials
- **clinical** — healthcare/lab aesthetic, hygienic, functional, bright
- **hospitality** — hotel/restaurant aesthetic, welcoming, refined, service-oriented
- **institutional** — public building aesthetic, durable, formal, rule-based
- **industrial** — factory/warehouse aesthetic, raw materials, exposed systems
- **corporate** — office aesthetic, professional, polished, branded
- **educational** — school/university aesthetic, flexible, inspiring, activity-focused
- **retail** — commercial aesthetic, product-focused, dynamic, customer-facing

Capture response.

### Step 2.2: Color Palette

Ask: "Describe the **primary color** for the interior" (e.g., "warm gray," "soft white," "warm beige," "sage green," "charcoal blue")

Ask: "What is the **secondary color**?" (e.g., "light gray," "warm cream," "natural wood tone," "accent blue")

Ask: "What is the **accent color** for highlights and features?" (e.g., "warm copper," "deep teal," "warm orange," "muted sage")

Ask: "Do you have **inspiration photos** or color references? (yes/no)"

If yes:
- Invite user to upload reference images
- Store filenames in color_palette.reference_images

Capture all color responses.

### Step 2.3: Materials by Room Type

Load room types from plans-spatial.json (e.g., "Bedroom," "Common Area," "Kitchen," "Restroom," "Corridor," "Mechanical," etc.)

For each major room type, ask:

**"For [Room Type] spaces, please provide:"**

#### Flooring
Ask: "What **flooring material**?" (e.g., "polished concrete," "ceramic tile," "luxury vinyl plank," "natural wood," "rubber")

Ask: "What **finish/color**?" (e.g., "light gray," "warm oak," "matte," "polished")

#### Walls
Ask: "How are **walls finished**?" (e.g., "painted gypsum board," "tile wainscot + paint," "wood paneling," "exposed CMU," "vinyl wallcovering")

Ask: "What **color/material**?" (e.g., "soft white," "warm gray," "natural wood tone")

#### Ceiling
Ask: "What is the **ceiling type**?" (e.g., "gypsum board," "suspended acoustic tile," "exposed structure," "open beam," "coffered," "drop ceiling")

Ask: "What **color/finish**?" (e.g., "bright white," "light gray," "natural wood," "black exposed steel")

#### Base
Ask: "What **base/trim material** and finish?" (e.g., "painted wood base," "cove base rubber," "natural wood trim," "anodized aluminum")

#### Casework / Millwork
*Only ask if applicable for room type (e.g., yes for kitchens, bathrooms, offices; no for open corridors)*

Ask: "Describe **casework, cabinets, built-ins**" (e.g., "natural wood cabinetry, soft-close drawers, open shelving in entry," "stainless steel shelving in prep area")

#### Countertops
*Only ask if applicable (kitchens, bathrooms, nursing stations)*

Ask: "What **countertop material and finish**?" (e.g., "quartz counters, white," "solid surface, warm gray," "stainless steel," "sealed wood")

#### Hardware Finish
Ask: "What is the **hardware finish**?" (e.g., "polished chrome," "brushed nickel," "bronze," "oil-rubbed bronze," "stainless steel")

#### Furniture & Fixtures
Ask: "Describe the **furniture style** for [Room Type]" (e.g., "modern minimalist," "warm residential," "clinical institutional," "hospitality-grade")

Ask: "Any **special features or equipment**?" (e.g., "picture rails," "display niches," "accent lighting," "accent wall," "window seat," "fireplace")

### Step 2.4: Brand Standards & Owner Preferences

Ask: "Are there **brand standards, owner preferences, or design guidelines** we should know about?" (yes/no/text)

If yes: "Please describe" (e.g., "Must use warm wood tones," "Specific furniture brand," "Accessible/universal design priorities," "Sustainable materials preference")

Capture response.

### Step 2.5: Special Notes

Ask: "Any **special design notes** or unique features to capture?" (free-form text)

Examples:
- "Historic renovation — preserve original exposed beams"
- "High-end hospitality — luxury finishes throughout"
- "Adaptable spaces — movable walls and flexible furniture"
- "Daylit atrium — important focal point"
- "Outdoor living emphasis — indoor-outdoor flow"

Capture response.

### End of Phase 2

Summarize interior design to user:
```
INTERIOR DESIGN SUMMARY
Character: [type]
Color Palette: [primary] / [secondary] / [accent]
Room Types Documented: [count]
Brand/Owner Notes: [yes/no]
Special Features: [summary]
```

Ask: "Ready to proceed to **Photo Documentation**?" (yes/continue)

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.
