# Avoidance Terms & Quality Modifiers
## Foreman OS Rendering-Generator Reference

This guide provides positive-framed language to prevent common AI image generation artifacts. Modern AI models (Flux 2, Gemini) respond better to positive framing than negative prompts. Instead of "no distorted perspective," we say "accurate linear perspective." This document is organized by category with positive reframes and a master quality block for appending to any prompt.

---

## GEOMETRY & PERSPECTIVE

### Artifact: Warped, Distorted Perspective

**Prevents:** Fish-eye distortion, impossible angles, perspective that doesn't follow architectural rules, building appearing to curve or tilt unnaturally.

**Positive Reframe:**
```
Accurate linear perspective with correct vanishing points. Perspective follows architectural
rules and is verifiable with ruler. Straight lines remain straight; edges are parallel or
converge correctly to single vanishing point. No fish-eye distortion or curved perspective.
```

### Artifact: Incorrect Architectural Proportions

**Prevents:** Building appearing impossibly tall, impossibly short, or with wrong aspect ratio. Windows appearing too large or too small relative to wall. Doors appearing child-sized or giant-sized.

**Positive Reframe:**
```
Correct architectural proportions and realistic scale relationships. Building dimensions verifiable
as accurate. Door height relative to wall height correct and consistent. Window size appropriate
to openings. Proportions lockable with architectural standards (doors 7 feet tall, windows 4 feet wide, etc.).
```

### Artifact: Randomly Placed or Inconsistent Windows

**Prevents:** Windows scattered irregularly across facade, window spacing inconsistent, same elevation showing different window patterns when viewed from different angles.

**Positive Reframe:**
```
Consistent window spacing and alignment. Windows arranged in regular pattern, spaced equally,
aligned on same horizontal line per row. Window pattern regular and verifiable. Same number of
windows on each similar section of facade.
```

### Artifact: Structurally Illogical Elements

**Prevents:** Floating building with no visible foundation, impossible cantilevers, walls not supported, roof structures floating in air, columns not aligned with structural load.

**Positive Reframe:**
```
Structurally logical construction. Building sits firmly on ground with visible foundation. Roof
structure clearly supported by walls and columns. Columns aligned with structural loads. No
floating or unsupported elements. Construction logic apparent and verifiable.
```

### Artifact: Distorted Door/Window Frames

**Prevents:** Door frames that appear twisted or skewed, window mullions that don't align, glass panes that appear to have impossible geometry.

**Positive Reframe:**
```
Geometrically accurate door and window frames. Frames square and true, not twisted. Mullions
straight and at correct angles. Glass panes rectangular with correct proportions. Frame geometry
verifiable with right angle.
```

---

## MATERIALS & SURFACES

### Artifact: Plastic-Looking Surfaces

**Prevents:** All materials appearing to be made of plastic or painted plastic, loss of material distinction, surfaces appearing too uniform and artificial.

**Positive Reframe:**
```
Realistic material textures with natural surface variation. Metal shows appropriate sheen and
micro-texture. Concrete shows surface variation and fine grain. Wood shows grain variation and
natural weathering. Glass shows transparency and slight color. Fabric/textiles show weave. Each
material appears authentically what it is.
```

### Artifact: Everything Appearing Equally Glossy or Reflective

**Prevents:** Matte materials appearing shiny, all surfaces reflecting like mirrors, loss of distinction between glossy and matte finishes.

**Positive Reframe:**
```
Accurate material reflectivity appropriate to finish type. Matte finishes show minimal reflection,
appearing dull and light-absorbing. Satin finishes show subtle sheen. Glossy finishes show strong
reflection but appropriate to material (glass more reflective than glossy paint). Reflectivity
varies by material type, appropriate to architectural specifications.
```

### Artifact: Oversaturated or Cartoonish Colors

**Prevents:** Colors appearing vivid and unnatural, exaggerated color saturation that doesn't match real materials, candy-colored appearance, loss of material realism.

**Positive Reframe:**
```
Natural color saturation, true-to-life tones. Colors appear as they would in natural daylight.
Gray materials appear gray, not purple or blue. Color saturation matches photographed materials
of same type. Oversaturation avoided; colors are vibrant but realistic. Color temperature
appropriate to lighting conditions (warm in golden hour light, cool in overcast).
```

### Artifact: Material Shifting or Inconsistency Mid-Surface

**Prevents:** A wall panel that appears one color on left side and different color on right side, material changing appearance across single surface, inconsistent finish across single element.

**Positive Reframe:**
```
Consistent material appearance across all surfaces. Single material maintains consistent color
and finish across entire visible surface. Color variation limited to natural weathering or
intentional design pattern (not random shifts). Material identity remains clear and consistent
across entire building elevation.
```

### Artifact: Unrealistic Metal Finishes

**Prevents:** Anodized aluminum appearing chrome-bright, stainless steel appearing pewter, metal appearing plastic.

**Positive Reframe:**
```
Realistic metal finishes for specified material type. Anodized aluminum shows appropriate satin
or matte finish with subtle sheen. Bronze anodize appears warm and subdued. Stainless steel shows
appropriate reflectivity. Painted steel appears as painted, not glossy. Metal finishes appropriate
to architectural specification.
```

### Artifact: Unrealistic Glass Appearance

**Prevents:** Glass appearing opaque, glass appearing as solid mirror, glass showing no transparency, glass showing incorrect reflection/refraction, glass appearing plastic.

**Positive Reframe:**
```
Realistic glass appearance. Clear glass shows true transparency with visible interior depth. Glass
shows appropriate reflection of sky and surroundings without appearing as mirror. Tinted glass shows
color tint but remains transparent. Interior view visible through clear glass. Glass reflections and
refractions follow physical light laws.
```

### Artifact: Concrete Appearing Dirty or Stained When Should Be Clean

**Prevents:** New concrete appearing weathered and dark, clean concrete appearing covered in moss and stains, fresh concrete work appearing years old.

**Positive Reframe:**
```
Appropriate concrete finish and age. Fresh concrete shows light gray color, smooth finish, clean
appearance. If weathered appearance intended, specify age (5-year-old concrete shows moderate
weathering, not extreme staining). Concrete color and finish match architectural intent.
```

---

## HUMAN ELEMENTS

### Artifact: Distorted or Unnaturally Proportioned People

**Prevents:** People appearing with disproportionate limbs, wrong number of fingers, twisted anatomy, proportions that defy physics.

**Positive Reframe:**
```
Realistically proportioned people for scale. Human figures anatomically correct with proper head,
torso, limb proportions. Hands show correct number of fingers with correct proportions. No twisted
anatomy or impossible poses. Proportions verifiable against established scale (person 5.5 feet tall).
```

### Artifact: Uncanny Valley Expressions or Poses

**Prevents:** People with strange expressions, poses that appear unnatural, movement that doesn't match human capability, stiff zombie-like appearance.

**Positive Reframe:**
```
Natural poses and appropriate attire. People shown in realistic, comfortable postures. Expressions
natural and confident (if faces visible). Clothing appropriate to season and context (professional
attire for office building, casual for residential). Poses verifiable as physically possible and
naturally human.
```

### Artifact: People at Wrong Scale Relative to Buildings

**Prevents:** Giant people towering over door frames, tiny people that appear to be dolls, inconsistent scale between people in foreground vs background.

**Positive Reframe:**
```
People at correct scale relative to doors and building elements. Door opening 7 feet tall, person
5.5 feet tall, proportions show clear scale relationship. People in background scaled correctly
with atmospheric perspective. No giant people or doll-sized people. Scale of all figures verifiable
against architectural dimensions.
```

### Artifact: Too Many or Too Few People

**Prevents:** Overcrowded scene with unrealistic density, overly empty scene, people appearing from nowhere, inconsistent occupancy logic.

**Positive Reframe:**
```
Appropriate occupancy density matching building context. Healthcare facility shows moderate occupancy
and activity appropriate to building type. People in logical locations (entries, parking, terraces).
Density feels realistic—not crowded, not empty. Occupancy consistent with building program.
```

---

## ENVIRONMENTAL

### Artifact: Psychedelic or Unnatural Sky

**Prevents:** Sky showing impossible colors (neon green, electric purple), sky appearing cartoonish, clouds that defy physics, lightning or weather phenomena that don't match lighting.

**Positive Reframe:**
```
Natural sky with realistic cloud formations. Sky color appropriate to atmospheric conditions (clear
blue, overcast gray, golden hour warm, etc.). Clouds show realistic form and structure—cumulus
clouds puffy and defined, stratocumulus layered, cirrus thin and wispy. Sky color verifiable against
real-world atmospheric color at specified time and location.
```

### Artifact: Tropical Plants in Wrong Climate

**Prevents:** Palm trees in northern latitude, tropical vegetation in temperate zone, species appearing in climatically incorrect location, vegetation clearly out of place.

**Positive Reframe:**
```
Appropriate vegetation scale and species. Plants selected for building climate zone. Temperate
project shows native or established ornamental species appropriate to region—serviceberry, oakleaf
hydrangea, ornamental grasses, not palms or tropical plantings. Vegetation type, size, and form
appropriate to geographic context.
```

### Artifact: Building Floating in Space with No Ground

**Prevents:** Building appearing to hover above ground, no visible foundation or grade, building disconnected from landscape, unclear where building meets earth.

**Positive Reframe:**
```
Ground plane extends naturally to horizon. Building clearly sits on ground plane. Grade clearly
visible, sloping naturally away from building. Foundation visible where appropriate. Building
connects firmly to landscape. Horizon line clear and level. No floating buildings.
```

### Artifact: Contradictory Shadows from Multiple Light Sources

**Prevents:** Shadows falling in impossible directions, shadows longer/shorter than light angle suggests, shadows too dark or too bright, conflicting shadow directions.

**Positive Reframe:**
```
Realistic shadows consistent with single primary light source. Shadow direction matches sun angle
(morning sun casts long shadows to west, afternoon sun casts shadows to east). Shadow length
consistent with sun elevation angle. Shadow darkness appropriate to ambient fill light. Shadows
clearly from single dominant light source (plus subtle fill from sky).
```

### Artifact: Unnatural Pavement or Site Appearance

**Prevents:** Parking lot with impossible striping, pavement color not matching asphalt, site features appearing floating or detached, parking spaces wrong size or orientation.

**Positive Reframe:**
```
Realistic site features and pavement. Asphalt pavement shows authentic color and slight texture.
Parking striping regular and logical—parallel lines for linear spaces, diagonal/radial for angled
spaces. Parking spaces 9 feet wide. Curbs, landscaping, and site features sit naturally on ground
plane. Site features appear built and placed, not floating.
```

### Artifact: Weather Phenomena Not Matching Lighting

**Prevents:** Bright sunny sky but rain appearing to fall, clear conditions but stormy dark lighting, snow on ground but summer vegetation, inconsistent weather.

**Positive Reframe:**
```
Coherent weather conditions. Sky appearance, lighting, ground conditions all consistent with single
weather scenario. Clear sky with bright directional sun and sharp shadows. Overcast sky with soft
diffuse light and soft shadows. Rain/snow conditions with appropriate dark sky and wet pavement.
Vegetation state matches season (spring growth, summer full, autumn color, winter bare).
```

### Artifact: Unnatural Atmosphere or Air Appearance

**Prevents:** Air appearing murky or polluted when should be clear, clarity changing abruptly, haze appearing in patches, fog appearing at wrong density.

**Positive Reframe:**
```
Clear or appropriately atmospheric air. Clear conditions show sharp edges and good visibility to
distance. Atmospheric conditions (haze, fog, pollution) consistent across entire image. Volumetric
lighting (god rays, mist) appears natural and consistent. Atmospheric perspective natural—
background progressively softer and desaturated with distance.
```

---

## COMPOSITION

### Artifact: Multiple Buildings Merged or Confused

**Prevents:** Building geometry unclear, multiple buildings appearing to merge together, confused architectural identity, viewer unsure what building is subject.

**Positive Reframe:**
```
Single coherent architectural subject. Building clearly defined as single, distinct structure.
Architectural identity unmistakable. If adjacent structures shown, clearly separated and secondary
to primary subject. Building reads clearly as one unified form.
```

### Artifact: Abrupt Image Edges or Awkward Framing

**Prevents:** Building cut off unnaturally at edge, composition feeling cramped or awkward, horizon at edge creating tension, important elements cut off.

**Positive Reframe:**
```
Clean image edges with natural vignette. Composition natural and well-framed. Horizon line at
aesthetically appropriate position (not at center, typically). Building positioned for visual
interest. Important architectural features fully visible. Image edges feel intentional, not
accidental. Slight vignetting (edges slightly darker) natural and appropriate.
```

### Artifact: Depth of Field Inappropriate or Confusing

**Prevents:** Entire image blurry (everything out of focus), entire image equally sharp (no sense of focus), focus on wrong element (background sharp, building soft).

**Positive Reframe:**
```
Appropriate depth of field for architectural photography. Building in crisp architectural focus.
Foreground and immediate surroundings in focus. Background progressively softer, creating depth
sense. Depth of field shallow enough to feel photographic (not everything in focus), but deep enough
that entire building readable (not micro-focus).
```

### Artifact: Poor Composition or Unbalanced Framing

**Prevents:** Building placed at edge, composition feel random, no visual hierarchy, confusing focal point, composition appears accidental.

**Positive Reframe:**
```
Masterful composition with visual hierarchy. Building positioned for optimal visual interest (rule
of thirds or similar compositional principle). Leading lines guide eye to building. Composition
feels intentional and aesthetic. Foreground, middle ground, background clearly separated. Focal
point clear and compelling.
```

### Artifact: Awkward Viewing Angle or Perspective

**Prevents:** Bird's-eye view when should be eye-level, extreme worm's-eye view, Dutch angle tilting horizon, viewing angle unclear or disorienting.

**Positive Reframe:**
```
Natural viewing angle appropriate to context. Eye-level perspective for most presentations (viewer
standing at ground level observing building). Horizon line level and true. If elevation angle
different (slightly elevated for wide view, or slightly down from hill), intentional and clear.
Viewing angle comfortable and immersive.
```

---

## MATERIALS & FINISHES - ADVANCED

### Artifact: Inconsistent or Floating Material Seams

**Prevents:** Panel seams appearing in wrong locations, seams floating in space, panel pattern not matching building dimensions, seams appearing unnaturally.

**Positive Reframe:**
```
Regular and logical material pattern. Metal panel seams at correct spacing matching building
dimensions. Seams aligned vertically and horizontally. Panel coursing regular and consistent.
Seams appear structural, not floating. Pattern verifiable against building grid.
```

### Artifact: Unrealistic Weathering

**Prevents:** Weathering appearing painted-on rather than natural, extreme weathering on new-appearing materials, no weathering on visibly old materials, stains and corrosion appearing random.

**Positive Reframe:**
```
Appropriate weathering for material age and environment. New materials show minimal weathering.
Mature materials show realistic patina appropriate to age and material type. Metal shows oxidation
patterns natural to exposure (horizontal streaks from water runoff, etc.). Concrete shows weathering
concentrated in areas of high water flow. Weathering patterns follow physical laws.
```

### Artifact: Unrealistic Vegetation Appearance

**Prevents:** Trees appearing fuzzy and undefined, shrubs appearing plastic, vegetation color unnatural, foliage appearing painted-on.

**Positive Reframe:**
```
Realistic vegetation with natural form and color. Deciduous trees show recognizable branch structure
and natural foliage silhouette. Evergreen trees show natural conical or spreading form. Shrubs show
depth and natural growth form. Vegetation color appropriate to species and season (not cartoonish).
Foliage shows texture and natural variation.
```

---

## MASTER QUALITY BLOCK

**Append this paragraph to the end of any rendering prompt to prevent the most common artifacts:**

```
Quality and Technical Specifications:
Render with accurate linear perspective, correct vanishing points, no distortion. All architectural
proportions verifiable and correct—doors are 7 feet, windows are properly scaled, building dimensions
are accurate. Materials appear authentically realistic: metal shows appropriate finish (matte or satin,
not plastic), glass appears transparent and reflective, concrete shows surface variation, each material
clearly distinct. Colors are natural and true-to-life; gray materials appear gray, not cartoonish tones.
Consistent material appearance across all surfaces, no mid-surface color shifts. Shadows consistent
with single primary light source, shadow direction and length matching sun angle. Sky realistic with
natural cloud formations, no impossible colors. Vegetation appropriate to climate zone and season.
Ground plane extends naturally with no floating elements. Building sits firmly on visible foundation.
People (if shown) anatomically correct and at proper scale relative to building elements. Composition
natural with appropriate depth of field and visual hierarchy. No merged or confused building forms—
single clear subject. Image appears professional architectural visualization.
```

---

## CATEGORY-SPECIFIC QUALITY BLOCKS

### For Photorealistic Renderings:

```
PHOTOREALISTIC QUALITY BLOCK:
8K resolution, sharp focus, photorealistic digital painting. Accurate linear perspective with
correct vanishing points. Material finishes physically accurate: metal with appropriate micro-
sheen, glass with true transparency and reflection, concrete with natural surface texture,
brick with individual unit variation. Color saturation natural and true-to-life, no oversaturation.
Realistic shadows with soft penumbra matching sun angle. Sky blue and clear or appropriately
overcast, with natural cloud formations. Vegetation lush and naturalistic for season. Depth of
field appropriate to photography (building sharp, background softly blurred). No watermark,
no visible digital artifacts.
```

### For Illustration Renderings:

```
ILLUSTRATION QUALITY BLOCK:
Clean architectural illustration with intentional linework and precise proportions. Perfect
linear perspective with correct vanishing points, proportions verifiable with ruler. Flat color
fields with clean application (no gradient photorealism). Line work uniform weight and sharp—
0.3-0.7mm black lines defining all edges. No photographic texture or weathering. Materials suggested
through color and line pattern, not photographically detailed. Background simple and uncluttered,
allowing building to read clearly. Professional architectural drawing quality.
```

### For Watercolor Renderings:

```
WATERCOLOR QUALITY BLOCK:
Authentic watercolor characteristics: transparent layered washes, soft color transitions, visible
brushstrokes, natural pigment blooms where colors merge. Form suggested through color value rather
than precise line. Loose, flowing technique with painterly quality. Proportions approximately correct
(not perfect, not sloppy). Minimal detail; emphasis on atmosphere and light. Soft shadows as color
value changes, not harsh. Paper texture subtly visible.
```

### For Diagram Renderings:

```
DIAGRAM QUALITY BLOCK:
Technical architectural diagram with clean isometric or orthographic projection (not perspective).
Uniform line weight, sharp and clean, black on white or light background. Flat solid colors for
system identification (no gradients). Elements simplified to primary geometric forms. Clear labeling
with sans-serif font, legible at 50% scale. No decorative effects, drop shadows, or artistic treatment.
Could be output from technical CAD software.
```

### For Sketch Renderings:

```
SKETCH QUALITY BLOCK:
Hand-drawn architectural sketch with visible pencil linework. Construction lines visible showing
design process. Variable line weight with light guide lines and darker defining strokes. Proportions
accurate and verifiable but with natural hand-drawn quality. Perspective correct but not digitally
perfect. Minimal color if present (light wash only). Genuine architect's sketch appearance—serious
and accomplished, not crude.
```

### For Matte Painting Renderings:

```
MATTE PAINTING QUALITY BLOCK:
Film-quality cinematic visualization with dramatic lighting. Masterful composition using leading
lines and visual hierarchy. Volumetric lighting effects (god rays visible). Rich dramatic sky occupying
30-50% of frame. Deep atmospheric perspective with foreground sharp and background softly hazed.
Warm and cool tones balanced for visual richness. Materials enhanced and gleaming in highlights.
Entire image sharp and detailed at 8K resolution. Aspirational, confident, emotionally moving quality.
```

---

## TESTING REGENERATION LANGUAGE

When regenerating an image to fix artifacts, use these positive reframes:

**Instead of:** "This looks plastic"
**Say:** "Materials need realistic texture and appropriate surface reflectivity. Metal should show subtle sheen, not glossy plastic. Concrete should show fine surface variation."

**Instead of:** "The perspective is wrong"
**Say:** "Perspective should be accurate linear perspective with correct vanishing points. Straight lines should remain straight. Building proportions should be verifiable."

**Instead of:** "The colors are too bright"
**Say:** "Use natural color saturation with true-to-life tones. Gray should appear gray, not oversaturated. Color temperature appropriate to lighting conditions."

**Instead of:** "Windows are in wrong places"
**Say:** "Windows should have consistent spacing and alignment. Same number of windows per elevation section. Window pattern should be regular and verifiable."

**Instead of:** "The sky looks weird"
**Say:** "Sky should show natural blue color with realistic scattered clouds. Cloud formations should follow physical cloud structure (cumulus puffy, stratocumulus layered). No impossible colors."

**Instead of:** "The shadow direction is wrong"
**Say:** "Shadows should be consistent with single primary light source. Shadow direction and length should match specified sun angle. All shadows should point same direction."

---

## PREVENTING COMMON REGENERATION CYCLES

**Problem:** After 3 regenerations, colors have drifted from original. Sky was blue, now appears purple.

**Solution:** Use reference image workflow. Upload original approved render and state: "Use identical colors as this reference image. Render new [angle] showing same color palette."

**Problem:** Material finishes keep shifting between matte and glossy.

**Solution:** Be explicit in every prompt: "Matte finish throughout—metal composite panels, concrete, trim all matte, no glossy surfaces. Not reflective."

**Problem:** Building proportions inconsistent across elevations.

**Solution:** Include exact dimension specs in every prompt: "Building 75 feet wide x 132 feet deep, 16-foot eave, doors 3 feet x 7 feet, windows 4 feet x 4 feet."

**Problem:** Site context drifting—parking configuration changing between renders.

**Solution:** Lock site spec in "master prompt" used for all renders: "Parking: angled stalls, 9-foot wide, white stripe lines, sedans and SUVs parked."

---

## GEMINI-SPECIFIC QUALITY LANGUAGE

Gemini responds well to positive, aspirational language:

✓ "Professional architectural visualization with museum-quality detail"
✓ "Award-winning architectural rendering quality"
✓ "Masterful composition and lighting design"
✓ "Physically accurate and cinematically lit"

Avoid language that suggests you're worried about errors:

✗ "Make sure the perspective isn't distorted"
✗ "Don't mess up the colors"
✗ "Try not to make weird mistakes"

---

## FLUX 2-SPECIFIC QUALITY LANGUAGE

Flux 2 is very responsive to style and technical modifiers:

✓ "8K digital painting, physically accurate materials, sharp focus"
✓ "Clean isometric projection with uniform line work"
✓ "Loose watercolor technique with transparent washes"
✓ "Cinema-grade lighting and composition"

Flux 2 does NOT support negative prompts, so always use positive reframes.

---

## SUMMARY: THE QUALITY PROTOCOL

When writing any rendering prompt:

1. ✓ Include specific dimensional specs for accuracy
2. ✓ Describe materials with finish details (matte, satin, glossy)
3. ✓ Specify color with reference or brand name
4. ✓ Describe lighting with sun angle and quality
5. ✓ Specify perspective and composition approach
6. ✓ Use the Master Quality Block as safety net
7. ✓ For style-specific renders, use category-specific quality block
8. ✓ Use positive, aspirational language throughout
9. ✓ Avoid negative framing ("don't," "no," "avoid")
10. ✓ When regenerating, use positive reframe of the problem

This systematic approach ensures high-quality, consistent renderings across all project visualizations.

