# Interior Rendering Templates

Complete prompt templates for interior spaces with specific camera positions, lighting scenarios, and finish details. Interior renderings emphasize spatial volume, finishes, fixtures, and lighting quality.

## Camera Positions by Room Type

Standard camera positions for different space types ensure consistency and professional presentation:

| Room Type | Focal Length | Distance | Height | Vertical Angle | Composition |
|---|---|---|---|---|---|
| Bedroom | 24mm | 12-15 feet | 5 feet | 0° | Corner to opposite corner, furniture visible |
| Common area | 20mm | 20-25 feet | 5 feet | -5° | Entry perspective, full room depth |
| Kitchen/prep | 24mm | 12 feet | 5 feet | 0° | Pass-through view, counters and equipment |
| Restroom | 28mm | 8-10 feet | 5 feet | 0° | Entry view, fixtures prominent |
| Corridor | 20mm | 30+ feet | 5 feet | 0° | One end looking through length |
| Lobby/entry | 20mm | 25 feet | 5 feet | -2° | Entry perspective, wayfinding visible |
| Mechanical room | 28mm | 15 feet | 5 feet | 0° | Equipment arrangement clear |
| Dining/common | 20mm | 20 feet | 5 feet | -3° | Tables, seating arrangement clear |

## Master Interior Template

All interior renderings follow this structure with placeholders filled from project data:

```
{CAMERA_POSITION_AND_DESCRIPTION}. {SPACE_NAME_AND_DIMENSIONS}. {SPACE_DESCRIPTION}. The room features {FLOORING}, {WALL_TREATMENT}, {CEILING_SYSTEM}. {BASE_TRIM}. {CASEWORK_AND_MILLWORK}. {COUNTERTOPS_AND_SURFACES}. {LIGHTING_FIXTURES}. {PLUMBING_FIXTURES}. {HVAC_VISIBLE}. {FURNITURE_AND_EQUIPMENT}. {SPECIALTIES_AND_ACCESSORIES}. {ATMOSPHERE_AND_CHARACTER}. {STYLE_AND_QUALITY}. {AVOIDANCE_TERMS}.
```

## Space-Specific Templates

### Typical Bedroom

**Camera Position:** Standing at doorway looking into room, 24mm lens equivalent, 12-15 feet from entry, eye level (5 feet height). Composition shows entry perspective with bed, furnishings, window/light source visible.

**Base Template:**
Photorealistic interior rendering of a typical bedroom in a {BUILDING_TYPE} facility. Camera positioned at doorway looking in, showing full room context. Room dimensions: {ROOM_DIMENSIONS}. Flooring: {FLOORING_TYPE_COLOR} with {BASE_TRIM_TREATMENT}. Wall finish: {WALL_COLOR_SHEEN}, {WALL_QUALITY}. Ceiling: {CEILING_TYPE_COLOR}, grid pattern and light fixtures visible. Casework: {CLOSET_DETAILS}, {BUILT_INS}. Bed: {BED_TYPE_SIZE} with {BEDDING_COLOR_PATTERN}. Additional furniture: {BEDROOM_FURNITURE}. Lighting: {LIGHTING_SCENARIO}, {LIGHT_FIXTURES_QUANTITY_TYPE}. Window treatment: {WINDOW_TREATMENTS}. Accessories: {ROOM_ACCESSORIES}. Atmosphere: {BEDROOM_CHARACTER}. Interior design quality professional, 4K resolution, accurate materials and proportions. {AVOIDANCE_TERMS}.

### Bedroom with Specific Room Number

**Camera Position:** Same as typical bedroom, but labeled with specific room number from floor plan.

**Base Template:**
Photorealistic interior rendering of bedroom 101 (or specific room number) in a {BUILDING_TYPE} facility. {ROOM_LOCATION_DESCRIPTION} (e.g., "southeast corner, double windows on south and east walls"). Room dimensions: {ROOM_DIMENSIONS}. Flooring: {FLOORING_TYPE_COLOR}. Wall finish: {WALL_COLOR}. Ceiling: {CEILING_TYPE}, {LIGHT_FIXTURES}. Bed: {BED_CONFIGURATION}. Furniture: {SPECIFIC_ROOM_FURNITURE}. Windows: {WINDOW_CHARACTERISTICS} (size, orientation, view to exterior). Lighting: {LIGHTING_SCENARIO}. Window treatments: {TREATMENTS}. Special features: {ROOM_SPECIFIC_DETAILS}. Professional interior visualization, accurate finishes and lighting. {AVOIDANCE_TERMS}.

### Common Area / Lounge

**Camera Position:** Corner perspective, 20mm wide lens, 20-25 feet from entry, eye level. Composition shows full room volume, seating arrangement, circulation paths, entry/exit visible.

**Base Template:**
Photorealistic interior rendering of a common area / lounge in a {BUILDING_TYPE} facility. Camera positioned at corner showing full room volume and seating arrangement. Room type: {COMMON_AREA_TYPE} (e.g., "social lounge", "activity center", "TV lounge"). Dimensions: {ROOM_DIMENSIONS}. Flooring: {FLOORING_TYPE}, {FLOORING_COLOR}, {FLOORING_PATTERN} visible throughout. Wall finish: {WALL_COLOR_AND_TREATMENT}, {WALL_QUALITY}. Ceiling: {CEILING_TYPE} with {CEILING_HEIGHT_APPARENT}. Lighting: {LIGHTING_SCENARIO}, {LIGHTING_QUALITY}. Fixtures: {LIGHT_FIXTURES_TYPE_QUANTITY}. Furniture arrangement: {SEATING_CONFIGURATION}, {FURNITURE_STYLE}, upholstery in {FABRIC_COLOR}. Tables: {TABLE_TYPE_AND_FINISH}. Accessories: {DECORATIVE_ELEMENTS}, artwork/signage. Entertainment: {ENTERTAINMENT_EQUIPMENT}. Accessibility features: {ACCESSIBLE_DESIGN_ELEMENTS}. Atmosphere: {COMMON_AREA_CHARACTER}. Professional hospitality-quality interior visualization. {AVOIDANCE_TERMS}.

### Kitchen / Food Service Area

**Camera Position:** Standing at pass-through or entry, 24mm lens, 12 feet from furthest counter, eye level. Composition shows countertop work surfaces, appliances, cabinetry, prep areas clearly.

**Base Template:**
Photorealistic interior rendering of kitchen / food service area. Camera positioned at pass-through showing work surfaces and equipment layout. Dimensions: {KITCHEN_DIMENSIONS}. Flooring: {KITCHEN_FLOORING_TYPE}, {FLOORING_COLOR}, {MAINTENANCE_APPEARANCE}. Wall finish: {WALL_TREATMENT_KITCHEN}, {CLEANABILITY}. Ceiling: {CEILING_TYPE}, {CEILING_HEIGHT}, open to adjacent space or enclosed. Cabinetry: {CABINET_TYPE}, {CABINET_COLOR}, {HARDWARE_STYLE}. Countertops: {COUNTERTOP_MATERIAL_COLOR}, {COUNTERTOP_FINISH}, work surface appearance. Appliances: {APPLIANCES_LIST} (range, refrigerator, dishwasher, microwave). Sink: {SINK_TYPE}, {SINK_FAUCET}. Equipment: {PREP_EQUIPMENT} (prep tables, warming equipment, serving surfaces). Backsplash: {BACKSPLASH_MATERIAL_COLOR}, tile pattern visible. Lighting: {KITCHEN_LIGHTING}, {TASK_LIGHTING} at work surfaces. Storage: {STORAGE_VISIBLE}. Atmosphere: {KITCHEN_CHARACTER}, clean professional appearance. Professional kitchen visualization, accurate equipment scale. {AVOIDANCE_TERMS}.

### Restroom / Toilet Room

**Camera Position:** Standing at entry looking into room, 28mm lens, 8-10 feet from furthest fixture, eye level. Composition shows all fixtures (toilet, sink, accessories) and layout clearly.

**Base Template:**
Photorealistic interior rendering of a restroom / toilet room in a {BUILDING_TYPE} facility. Camera positioned at entry showing full fixture layout. Dimensions: {RESTROOM_DIMENSIONS}. Flooring: {RESTROOM_FLOORING}, {FLOORING_COLOR}, {SLIP_RESISTANCE_APPARENT}. Wall finish: {WALL_TREATMENT_RESTROOM}, {DURABILITY_APPEARANCE}, {WALL_COLOR}. Ceiling: {CEILING_TYPE}, height and finish. Toilet: {TOILET_TYPE}, {TOILET_COLOR}, accessible design visible (grab bars, space). Sink: {SINK_TYPE}, {SINK_MATERIAL_COLOR}, {COUNTER_HEIGHT}. Faucet: {FAUCET_TYPE}, accessible controls, soap/paper dispenser visible. Mirror: {MIRROR_SIZE_AND_FRAME}, appropriate lighting above. Accessories: {ACCESSORY_TYPES} (toilet paper holder, hand towel dispenser, soap dispenser, trash receptacle). Grab bars: {GRAB_BAR_LOCATION}, {GRAB_BAR_FINISH}. Lighting: {LIGHTING_TYPE}, {LIGHT_QUANTITY}, appropriate illumination for grooming tasks. Ventilation: {EXHAUST_VISIBLE}. Signage: {ACCESSIBLE_SIGNAGE}. Color coordination: {COLOR_HARMONY}. Professional healthcare-quality finishes. {AVOIDANCE_TERMS}.

### Corridor / Hallway

**Camera Position:** Standing at one end looking through length of corridor, 20mm wide lens, 30+ feet to furthest end, eye level. Composition shows full circulation path, doorways, lighting, wayfinding.

**Base Template:**
Photorealistic interior rendering of circulation corridor in a {BUILDING_TYPE} facility. Camera positioned at one end looking through full length of corridor. Dimensions: {CORRIDOR_DIMENSIONS} (length x width x ceiling height). Flooring: {CORRIDOR_FLOORING}, {FLOORING_COLOR}, {FLOORING_PATTERN}, sweep visible into distance. Base trim: {BASE_TREATMENT}, {BASE_COLOR}, cove or straight edge. Wall finish: {WALL_COLOR}, {WALL_TREATMENT}, continuity along full length visible. Ceiling: {CEILING_TYPE}, grid spacing visible, continuous to far end. Lighting: {CORRIDOR_LIGHTING_TYPE}, {LIGHT_SPACING}, even illumination along length. Doorways: {DOORWAY_DETAILS}, {DOOR_QUANTITY}, doors open/closed/vision panels visible. Room identification: {SIGNAGE_VISIBLE}, room numbers/names clear. Handrails: {HANDRAIL_LOCATION}, {HANDRAIL_COLOR}, graspability apparent. Accessibility: {ACCESSIBLE_WIDTH}, no obstructions, clear wayfinding. Wall-mounted items: {WALL_ACCESSORIES} (extinguisher, electrical outlets, wayfinding graphics). Perspective: {VANISHING_POINT_CHARACTER}, proper linear perspective showing corridor depth. Atmosphere: {CORRIDOR_CHARACTER}. Professional architectural visualization. {AVOIDANCE_TERMS}.

### Lobby / Entry

**Camera Position:** Standing at exterior entry looking into lobby space, 20mm wide lens, 25 feet into lobby, eye level with slight upward angle (-2°) to show ceiling/entry canopy relationship.

**Base Template:**
Photorealistic interior rendering of entry lobby in a {BUILDING_TYPE} facility. Camera positioned at main entry doors looking into lobby. Dimensions: {LOBBY_DIMENSIONS}. Flooring: {ENTRY_FLOORING}, {FLOORING_COLOR}, {FLOORING_PATTERN}, entrance matting visible. Wall finish: {WALL_COLOR}, {WALL_TREATMENT}, feature walls visible. Ceiling: {CEILING_HEIGHT_AND_TYPE}, architectural feature elements if present. Entry vestibule: {VESTIBULE_CHARACTER}, glass/transparent doors visible, weather protection. Reception area: {RECEPTION_DESK_LOCATION}, {DESK_TYPE}, {DESK_FINISH}. Seating: {ENTRY_SEATING} if present. Signage: {SIGNAGE_PROMINENT}, facility name/branding visible. Wayfinding: {WAYFINDING_SYSTEM}, directory, directional signage. Lighting: {ENTRY_LIGHTING}, {LIGHT_QUALITY}, welcoming appearance. Landscape/décor: {ENTRY_DÉCOR}, planters, artwork, architectural finishes. Accessibility: {ACCESSIBLE_ENTRY_FEATURES} (wide entry, grab rails, level surfaces). Atmosphere: {ENTRY_CHARACTER}, professional, welcoming. First impression quality. {AVOIDANCE_TERMS}.

### Mechanical Room

**Camera Position:** Standing at doorway looking into mechanical room, 28mm lens, 15 feet into room, eye level. Composition shows equipment arrangement, ductwork, piping, electrical systems clearly.

**Base Template:**
Photorealistic interior rendering of mechanical room showing equipment layout. Camera positioned at entry showing full equipment arrangement. Room dimensions: {MECHANICAL_DIMENSIONS}. Flooring: {MECHANICAL_FLOORING}, finished or rough concrete. Walls: {MECHANICAL_WALLS}, painted or unfinished. Ceiling: {MECHANICAL_CEILING}, fully visible, no drop ceiling. Structural elements: {STRUCTURAL_BEAMS_VISIBLE}, clear span framing. HVAC equipment: {HVAC_EQUIPMENT_LIST} (AHU units, filters, ductwork, dampers, VAV boxes, ERV). Ductwork: {DUCTWORK_TYPE}, {DUCTWORK_COLOR}, insulation visible, routing logical. Piping: {PIPING_TYPE}, {PIPE_ROUTING}, color-coded visible. Water heater: {WATER_HEATER_TYPE}, {WATER_HEATER_SIZE}, visible location. Electrical: {ELECTRICAL_PANELS}, {DISCONNECT_VISIBLE}, conduit routing. Valves and controls: {VALVE_LOCATIONS}, manual shutoff visible, labeling. Floor drains: {DRAIN_LOCATION} if present. Labeling: {EQUIPMENT_LABELING}, system identification. Organization: {ORGANIZATION_QUALITY}, neat arrangement, clear maintenance access. Lighting: {MECHANICAL_LIGHTING}, adequate task illumination. Professional mechanical room visualization, equipment scale accurate. {AVOIDANCE_TERMS}.

## Interior Finishes Translation Guide

Convert specification language to visual prompt language:

| Specification | Visual Language |
|---|---|
| VCT 12x12 light gray | Light gray commercial vinyl tile in small square pattern, slight matte sheen |
| LVP, medium brown wood grain | Luxury vinyl plank with realistic medium brown wood grain, plank joints visible |
| Acoustical ceiling 2x4 white | White acoustical ceiling tile, 2x4 grid with metal T-bar, soft facial texture |
| Smooth painted drywall, eggshell, white | Smooth painted drywall, eggshell sheen finish, pure white, seamless joints |
| Fiberglass reinforced panels | Glossy white cleanable FRP panels, subtle texture, hygienic appearance |
| Standing seam metal base | Metal trim base, standing seam detail, anodized finish, sharp lines |
| Ceramic tile 12x24 sand | Sand-colored glazed ceramic tile, 12x24 format, grout lines visible, semi-gloss |
| Solid surface, white quartz | Seamless solid surface (Corian-type), white with quartz pattern, non-porous |
| Laminate shaker cabinet | Thermofoil shaker-style cabinet doors, clean panel details, modern hardware |
| Stainless steel backsplash | Stainless steel backsplash, brushed finish, welded seams minimal |
| Rubber cove base 4" | Rubber cove base, 4 inches high, smooth surface, color-matched trim |

## Template Usage Instructions

1. **Identify Room Type**: Determine space being rendered
2. **Select Template**: Use corresponding room template above
3. **Gather Data**: Extract from:
   - Floor plan (room dimensions, layout, location)
   - Room finish schedule (flooring, walls, ceiling)
   - Fixture schedule (lighting, plumbing, equipment)
   - Furnishings list/equipment schedule
   - Interior design notes/visual-context.json
4. **Fill Placeholders**: Replace all `{PLACEHOLDER}` with specific room data
5. **Select Lighting**: Choose appropriate scenario (daylight, artificial, mixed)
6. **Add Avoidance Terms**: Append quality control language
7. **Review**: Ensure spatial logic, scale accuracy, finish consistency
8. **Execute**: Pass prompt to Gemini or Flux 2 API

## Quality Checkpoints

Before passing interior prompt to API:
- [ ] Room dimensions match floor plan (proportions correct)
- [ ] All finish materials match specification (flooring, walls, ceiling)
- [ ] Fixtures match equipment/fixture schedule
- [ ] Furniture matches room program (bedroom furniture in bedroom, etc.)
- [ ] Lighting scenario appropriate (natural if windows, artificial if interior)
- [ ] Colors specific ("light gray", not "gray")
- [ ] Scale references present (human figure, furniture size)
- [ ] Spatial logic correct (doorways, circulation, layout)
- [ ] Accessibility features noted if applicable
- [ ] Atmosphere/character matches building type
- [ ] Prompt reads naturally without placeholder artifacts
