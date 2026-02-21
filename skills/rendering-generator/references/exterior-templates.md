# Exterior Rendering Templates

Complete prompt templates for every exterior angle and view type. These templates are dynamically filled with project-specific data to create precise, consistent architectural renderings.

## Camera Specifications Reference

Before applying templates, review the camera parameters for each view type:

| Angle | Focal Length | Distance | Height | Vertical Angle | Lens Type |
|---|---|---|---|---|---|
| South elevation | 35mm equivalent | 60-80 feet | 5 feet | +2° | Standard architectural |
| North elevation | 35mm equivalent | 60-80 feet | 5 feet | +2° | Standard architectural |
| East endwall | 50mm equivalent | 40-50 feet | 5 feet | +2° | Tighter perspective |
| West endwall | 50mm equivalent | 40-50 feet | 5 feet | +2° | Tighter perspective |
| Aerial/drone | 16mm wide | 200+ feet altitude | Elevated | -45° | Wide aerial view |
| 3/4 southeast | 24mm equivalent | 80-100 feet | 5 feet | +5° | Dynamic composition |
| 3/4 southwest | 24mm equivalent | 80-100 feet | 5 feet | +5° | Dynamic composition |
| Street approach | 35mm equivalent | 100+ feet | 5 feet | +1° | Distant context view |
| Entry close-up | 85mm equivalent | 20-30 feet | 5 feet | 0° (level) | Detail emphasis |

## Master Exterior Template

All exterior renderings follow this structure, with placeholders filled from project data:

```
{SHOT_TYPE_CAMERA}. {BUILDING_SUMMARY}. {STRUCTURAL_SYSTEM_VISUAL}. The building features {WALL_CLADDING}, {ROOF_MATERIAL}, {TRIM_AND_FASCIA}. {BASE_AND_FOUNDATION}. {FENESTRATION_DOORS}. {ENTRY_DESCRIPTION}. {SITE_CONTEXT}. {LANDSCAPE_VEGETATION}. {HARDSCAPE_PARKING}. {SCALE_REFERENCES}. {LIGHTING_CONDITIONS}. {SKY_AND_ATMOSPHERE}. {STYLE_AND_QUALITY}. {AVOIDANCE_TERMS}.
```

## View-Specific Templates

### South Elevation

**Camera Position:** Eye-level architectural photograph, 35mm lens equivalent, standing at parking lot 70 feet south of main building. Slight upward angle (2-3 degrees) to show roof profile. Accurate linear perspective, centered composition showing full building width.

**Base Template:**
Photorealistic architectural rendering of the south elevation of a {BUILDING_TYPE} facility. The building is {OVERALL_DIMENSIONS}: {FOOTAGE} SF, {STORIES}, {STRUCTURAL_SYSTEM}. Camera positioned at eye level, 70 feet distance, slight upward angle showing full facade. The south-facing facade features {WALL_CLADDING_COLOR_PATTERN}. Roof: {ROOF_MATERIAL_COLOR}, {ROOF_SLOPE} pitch, {EAVE_HEIGHT}. Base: {FOUNDATION_VISIBLE} with {TRIM_COLOR} aluminum or {BASE_MATERIAL} coping. Fenestration: {WINDOW_TYPE_QUANTITY} {WINDOW_COLOR} frame windows, {GLAZING_TYPE}. Entry: {ENTRY_TYPE} with {ENTRY_FEATURES}, accessible ramp/entry features visible. Site context: {PARKING_CONFIGURATION} in foreground, {LANDSCAPING_TYPE} along building foundation. {ADJACENT_BUILDINGS_OR_OPEN_CONTEXT}. Lighting: {LIGHTING_TIME_OF_DAY}, {SHADOW_DIRECTION_AND_LENGTH}, {COLOR_TEMPERATURE}. Professional architectural photography quality, 4K resolution, sharp focus, accurate perspective, realistic materials texture. {AVOIDANCE_TERMS}.

### North Elevation

**Camera Position:** Eye-level architectural photograph, 35mm lens equivalent, standing 70 feet north of building. This is typically the rear/service elevation. Show full building profile from opposite side.

**Base Template:**
Photorealistic architectural rendering of the north elevation (rear facade) of a {BUILDING_TYPE} facility. {BUILDING_SUMMARY_DIMENSIONS}. Camera positioned at eye level, 70 feet distance, north side of building. The north-facing facade features {WALL_CLADDING_REAR}. Roof: {ROOF_MATERIAL_REAR_VIEW}, {ROOF_SLOPE}. Service elements: {SERVICE_ENTRIES_LOADING}, {MECHANICAL_VISIBLE}, {UTILITIES_VISIBLE}. Fenestration: {NORTH_WINDOWS_QUANTITY_TYPE}. Site context: {NORTH_SIDE_CONTEXT}. {LOADING_OR_SERVICE_FEATURES}. Lighting: {LIGHTING_TIME_OF_DAY}, {NORTH_SHADOW_CHARACTERISTICS}. Professional architectural photography quality, accurate perspective. {AVOIDANCE_TERMS}.

### East Endwall

**Camera Position:** Eye-level photograph, 50mm lens equivalent, standing 50 feet east of endwall. This view shows the building's profile and depth from east side.

**Base Template:**
Photorealistic architectural rendering of the east endwall elevation. {BUILDING_SUMMARY_DIMENSIONS}. Camera positioned at eye level, 50 feet distance, centered on endwall. The east endwall features {ENDWALL_CLADDING_COLOR}. Roof profile: {ROOF_PITCH_AND_OVERHANG} visible in profile. Architectural features: {ENDWALL_DETAILS}. Windows/vents: {ENDWALL_FENESTRATION}. Site context: {EAST_SIDE_CONTEXT}. Lighting: {LIGHTING_TIME_OF_DAY}, appropriate shadow characteristics for east-facing surface. Professional architectural photography quality, true linear perspective, accurate building proportions. {AVOIDANCE_TERMS}.

### West Endwall

**Camera Position:** Eye-level photograph, 50mm lens equivalent, standing 50 feet west of endwall. Mirror of east endwall view from opposite side.

**Base Template:**
Photorealistic architectural rendering of the west endwall elevation. {BUILDING_SUMMARY_DIMENSIONS}. Camera positioned at eye level, 50 feet distance, centered on endwall. The west endwall features {ENDWALL_CLADDING_COLOR_WEST}. Roof profile: {ROOF_PITCH_AND_OVERHANG} visible in profile. Architectural elements: {ENDWALL_DETAILS_WEST}. Fenestration: {WEST_ENDWALL_WINDOWS}. Site context: {WEST_SIDE_CONTEXT}. Lighting: {LIGHTING_TIME_OF_DAY}, appropriate for west-facing surface. Professional architectural photography quality. {AVOIDANCE_TERMS}.

### Aerial View (Drone Perspective)

**Camera Position:** Aerial drone photograph, 45-degree angle looking down, approximately 200 feet altitude. Wide 16mm lens equivalent. Shows full building footprint, parking lot, site perimeter, surrounding context.

**Base Template:**
Aerial architectural rendering (drone photograph) of {BUILDING_TYPE} facility and surrounding site. Camera altitude 200 feet, 45-degree angle looking down and forward, showing complete footprint and context. Building: {FOOTPRINT_DIMENSIONS}, {ROOF_COLOR_APPEARANCE} roof, {OVERALL_VISUAL_CHARACTER_FROM_ABOVE}. Parking: {PARKING_LAYOUT} with accessible spaces, vehicle circulation clearly visible. Landscaping: {LANDSCAPE_VISIBLE_FROM_ABOVE}. Site utilities: {UTILITIES_VISIBLE_FROM_ABOVE}. Grading: {GRADING_VISIBLE}. Adjacent context: {SURROUNDING_LAND_USE}. Lighting: {LIGHTING_TIME_OF_DAY}, {SHADOW_DIRECTION_FROM_ABOVE}. Professional drone photography quality, sharp focus, accurate perspective, clean composition. {AVOIDANCE_TERMS}.

### 3/4 Southeast Perspective

**Camera Position:** Classic 3/4 presentation angle showing south facade + east endwall. 24mm lens equivalent, positioned southeast of building corner at 90-100 feet distance. Hero angle showing maximum building character.

**Base Template:**
Photorealistic architectural rendering of {BUILDING_TYPE}, southeast three-quarter perspective. Camera positioned southeast of building, 100 feet distance, eye level, 24mm equivalent lens, dynamic composition showing both south elevation and east endwall. Building: {COMPLETE_BUILDING_DESCRIPTION}. South facade: {SOUTH_CLADDING_AND_DETAILS}. East endwall: {EAST_ENDWALL_CLADDING_AND_PROFILE}. Roof: {ROOF_COMPLETE_PROFILE}. Base: {FOUNDATION_VISIBLE_3QUARTER}. Entry and features: {ENTRY_PROMINENCE}, {ARCHITECTURAL_CHARACTER_FEATURES}. Fenestration: {WINDOW_PATTERN_3QUARTER}. Site integration: {FOREGROUND_LANDSCAPING}, parking visible on right side. Lighting: {LIGHTING_TIME_OF_DAY}, {3QUARTER_SHADOW_CHARACTERISTICS}. Professional architectural photography, vibrant colors, rich detail, compelling composition. {AVOIDANCE_TERMS}.

### 3/4 Southwest Perspective

**Camera Position:** Classic 3/4 from southwest showing south facade + west endwall. Same parameters as southeast but from opposite corner.

**Base Template:**
Photorealistic architectural rendering of {BUILDING_TYPE}, southwest three-quarter perspective. Camera positioned southwest of building, 100 feet distance, eye level, 24mm equivalent lens showing south elevation and west endwall. Building: {COMPLETE_BUILDING_DESCRIPTION}. South facade: {SOUTH_CLADDING_AND_DETAILS}. West endwall: {WEST_ENDWALL_CLADDING_AND_PROFILE}. Roof: {ROOF_PROFILE_SOUTHWEST}. Foundation: {FOUNDATION_VISIBLE_SOUTHWEST}. Architectural character: {ENTRY_AND_FEATURES}. Fenestration: {WINDOW_PATTERN_SOUTHWEST}. Site context: {FOREGROUND_AND_CONTEXT_SOUTHWEST}, parking on left side. Lighting: {LIGHTING_TIME_OF_DAY}, {SOUTHWEST_SHADOW_CHARACTERISTICS}. Professional architectural presentation, clean composition, accurate perspective. {AVOIDANCE_TERMS}.

### Street Approach View

**Camera Position:** Eye-level photograph, 35mm lens equivalent, standing on street/approach road 100+ feet from building. Shows how building presents to public.

**Base Template:**
Photorealistic architectural rendering showing {BUILDING_TYPE} as viewed from public street approach. Camera positioned on approach road approximately 120 feet from main entrance. This view shows public perception of the building. Building profile: {BUILDING_SILHOUETTE_FROM_APPROACH}. Visible facades: {FACADES_VISIBLE_FROM_STREET}. Entry and wayfinding: {ENTRY_PROMINENCE_AND_SIGNAGE}, accessible features visible. Foreground: {APPROACH_ROAD_CONDITIONS}, parking lot, landscaping along approach. Site context: {SITE_CHARACTER_FROM_APPROACH}. Neighboring context: {ADJACENT_BUILDINGS_OR_OPEN_SPACE}. Lighting: {LIGHTING_TIME_OF_DAY}, {APPROACH_VIEW_SHADOW_CONDITIONS}. Professional architectural photography, welcoming appearance, clear wayfinding. {AVOIDANCE_TERMS}.

### Entry Close-up

**Camera Position:** Eye-level photograph, 85mm lens equivalent (portrait/telephoto), standing 25 feet from entry. Tight framing showing entry portico, doors, signage, hardware.

**Base Template:**
Photorealistic architectural rendering of main entry portico, detailed close-up view. Camera positioned 25 feet from entry, eye level, 85mm telephoto lens, centered composition emphasizing entry detail and quality. Entry design: {ENTRY_TYPE_DETAIL}. Doors: {DOOR_DESCRIPTION}. Signage: {SIGNAGE_DESCRIPTION}. Accessible features: {ACCESSIBLE_ENTRY_DETAILS}. Materials close-up: {MATERIALS_VISIBLE_AT_ENTRY}. Lighting: {ENTRY_LIGHTING}, {GOLDEN_HOUR_ACCENT_LIGHT}. Weather-stripping and sealing: {WEATHER_PROTECTION_VISIBLE}. Professional architectural photography quality, sharp detail, welcoming appearance, emphasis on accessible design. {AVOIDANCE_TERMS}.

## Template Usage Instructions

1. **Identify Rendering Type**: Determine which view (south elevation, 3/4 perspective, aerial, etc.)
2. **Select Template**: Use corresponding template above
3. **Gather Data**: Extract from project-config.md, plans-spatial.md, specs-quality.md, visual-context.json, site-context.json
4. **Fill Placeholders**: Replace all `{PLACEHOLDER}` with specific project data using descriptive visual language
5. **Add Lighting**: Select from lighting-conditions.md based on user input
6. **Add Avoidance Terms**: Append from avoidance-terms.md
7. **Review Coherence**: Ensure natural flow and no contradictions
8. **Execute**: Pass final prompt to selected API

## Example Placeholder Values (MOSC Example)

**Building Dimensions:**
- `{OVERALL_DIMENSIONS}` → "9,980 SF, 1-story, 75 feet wide by 132 feet deep"
- `{STRUCTURAL_SYSTEM}` → "pre-engineered metal building (PEMB) system with clear-span rigid frames"

**Cladding & Materials:**
- `{WALL_CLADDING_COLOR_PATTERN}` → "champagne/tan vertical metal panels, matte finish, subtle weathered patina"
- `{ROOF_MATERIAL_COLOR}` → "charcoal gray standing seam metal roofing with crisp vertical rib lines"
- `{FOUNDATION_VISIBLE}` → "dark red masonry plinth base with soldier course detail, 4 feet visible"

**Fenestration:**
- `{WINDOW_TYPE_QUANTITY}` → "16 large storefront windows"
- `{GLAZING_TYPE}` → "insulated low-E clear glass, 1-inch air space"

**Entry:**
- `{ENTRY_TYPE}` → "glass and aluminum storefront entry with covered portico"
- `{ENTRY_FEATURES}` → "accessible ramp with handrail, automatic sliding doors, 12-foot covered canopy"

**Parking & Site:**
- `{PARKING_CONFIGURATION}` → "25-space asphalt parking lot with 4 accessible spaces near entry"
- `{LANDSCAPING_TYPE}` → "mature deciduous trees (oaks, maples), mixed shrub plantings"

**Lighting:**
- `{LIGHTING_TIME_OF_DAY}` → "golden hour (6:00 PM), late afternoon warm directional light"
- `{SHADOW_DIRECTION_AND_LENGTH}` → "warm amber light from southwest, long shadows extending east"
- `{COLOR_TEMPERATURE}` → "warm amber golden tones, 3500K color temperature"

## Quality Checkpoints

Before passing prompt to API, verify:
- [ ] All placeholders filled with specific data (no generic terms)
- [ ] Building dimensions match actual project
- [ ] Materials match specification documents
- [ ] Camera position appropriate for view type
- [ ] Lighting direction and time of day clear and consistent
- [ ] Avoidance terms present
- [ ] Prompt reads naturally
- [ ] No contradictions (e.g., "snowy winter" + "green vegetation")
- [ ] Color names specific ("charcoal gray", not "gray")
- [ ] Scale references present (parking lot width, human figures, etc.)
