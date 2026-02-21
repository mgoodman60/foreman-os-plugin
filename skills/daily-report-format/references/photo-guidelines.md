# Photo Captioning and Smart Placement Guidelines

Rules for AI analysis, captioning, and placement of construction site photos in daily reports.

## Photo Analysis Process

When the user uploads photos, analyze each image for:

1. **Subject matter** — What is the primary focus? (excavation, concrete, framing, equipment, delivery, etc.)
2. **Work phase** — What phase of construction does this show? (sitework, foundation, structural, envelope, MEP, finishes)
3. **Location clues** — Grid line markers, room numbers, floor levels, building wings, compass orientation
4. **Condition** — Is this documenting progress, a problem, a delivery, an inspection, weather impact?
5. **People/Equipment** — Are workers or equipment visible? Which trade?

## Caption Format

Structure every caption as:

**"[Description of what's shown]. [Location]. [Direction/orientation if determinable]."**

### Caption Examples

| Photo shows | Caption |
|-------------|---------|
| Excavator digging a trench | "Foundation excavation in progress at Building A east wing. Looking north from Grid Line 3." |
| Concrete being poured into forms | "Concrete placement for Level 1 slab-on-grade, Section B. Approximately 30 CY placed at time of photo." |
| Stack of lumber on site | "Framing lumber delivered and staged at south laydown area. Material in good condition." |
| Workers installing rebar | "Rebar installation for grade beam at Grid Lines C-D, between Lines 2-4. Looking west." |
| Muddy site conditions | "Site conditions following overnight rain. Standing water at southeast corner of building pad." |
| Inspection sticker/tag | "Footing inspection passed. City of [name] inspector approved foundation at Grid A-1 through A-5." |
| Crane on site | "80-ton crane positioned at northeast corner for structural steel erection. Outriggers deployed." |
| Damaged delivery | "Damaged drywall shipment received from [supplier]. Approximately [X] sheets with water damage. Material segregated for return." |

## Smart Placement Rules

Place each photo in the most relevant report section based on its content:

| Photo content | Place in section |
|---------------|-----------------|
| Weather, site conditions, mud, snow, ice | **Weather Conditions** (below narrative) |
| Workers, trades doing work, progress | **Crew on Site** (after the crew table) |
| Deliveries, material staging, stockpiles | **Materials Received** (after materials table) |
| Equipment, cranes, excavators, lifts | **Equipment on Site** (after equipment table) |
| Progress overview, milestone completion | **Schedule Updates** (after schedule narrative) |
| Inspector, owner, architect on site | **Visitors / Inspections** (after visitor table) |
| General conditions, issues, misc | **General Notes** (at the end) |

### Tiebreaker Rules

If a photo could go in multiple sections:
1. Choose the most **specific** section (a photo of a delivery truck with lumber goes in Materials, not Equipment)
2. If equally specific, choose the section the user was **talking about** when they uploaded it
3. If no context, place in the section that appears **later** in the report (photos add more value to less text-heavy sections)

## Photo Layout Rules

### Single photo in a section
- Center horizontally
- Max width: 5.5 inches
- Maintain aspect ratio
- Caption centered below, 4pt gap

### Two photos in a section
- Place side by side
- Each ~3 inches wide
- Align tops
- Individual captions below each

### Three or more photos in a section
- First photo: full width (5.5")
- Remaining: paired side by side (3" each)
- Or use a 2×2 grid for four photos

### Photo ordering within a section
1. Wide/overview shots first
2. Detail/close-up shots after
3. Problem/issue photos last (they draw attention)

## Photo Quality Notes

If a photo is:
- **Blurry**: Still include it but note in caption: "(Image quality limited)"
- **Dark/backlit**: Include with note: "Interior view" or "Backlit conditions"
- **Duplicate/very similar**: Include the best one, skip the rest. Mention to user: "Skipped [X] similar photos; included the clearest one."

## No Photos Scenario

If no photos are provided for a section, do not include a photo placeholder. Simply omit the photo area. If no photos are provided for the entire report, omit the Site Photos section entirely but mention to the user: "No photos were included in today's report. Want to add any?"
