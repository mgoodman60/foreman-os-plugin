# Rendering Consistency Guide
## Foreman OS Rendering-Generator Reference

Maintaining visual consistency across multiple renderings of the same building is critical. A south elevation should look like the same building as a 3/4 view. A winter scene should show the same materials as a summer scene. This guide provides a systematic approach to ensuring architectural consistency across all project renderings.

---

## 1. Master Specification Concept

The foundation of consistent renderings is a single "hero" or "master" rendering that establishes all building characteristics. This becomes the source of truth for all subsequent renderings.

### Implementation:

1. **Generate the hero rendering first** — typically a comprehensive 3/4 view showing the most building complexity
2. **Document the exact prompt** used to generate it, including:
   - Full building description block (materials, colors, dimensions, style)
   - All quality and style modifiers
   - Composition and framing specifications
   - Environmental context (season, lighting, time of day)
3. **Store this prompt as a "Building Identity Block"** in a project reference document
4. **Reuse this block verbatim** in every subsequent rendering prompt
5. **Only modify the specific view/angle/condition** between renders; preserve the core description

### Example Building Identity Block:

```
Building Description (REUSE IN ALL PROMPTS):
The building is a 1-story, modern healthcare facility, 75 feet wide by 132 feet deep,
with a 16-foot eave height and 1:12 roof slope. Pre-engineered metal building (Nucor)
with galvanized steel frames. Exterior: metal composite panels in warm gray with light
chamfer detail, 36-inch tall glass storefront entries with dark aluminum frames,
recessed 2 feet from facade. Roof: light gray standing seam metal. Foundation:
poured concrete with 24-inch tall stem walls visible, medium gray finish.
Site: asphalt paving, landscape beds with low seasonal vegetation.
```

This exact block appears in every prompt, ensuring the building remains visually identical regardless of view.

---

## 2. Material Consistency

Materials must be specified with precision. Vague descriptions like "metal" or "gray" lead to inconsistency between renders. Use specific, replicable color and finish descriptions.

### Color Specification Strategy:

**Use specific color references rather than common names:**
- ❌ "gray metal siding"
- ✓ "warm gray composite panels (similar to Benjamin Moore HC-159 Ashwood Gray), with slight warm undertone"

**Include finish type in material description:**
- ❌ "glass doors"
- ✓ "clear annealed glass storefronts with dark bronze anodized aluminum frames, matte finish"

**Specify texture when relevant:**
- ❌ "brick walls"
- ✓ "face brick in medium brown with slight texture variation, 4 inches tall, running bond pattern"

### Material Consistency Checklist:

- [ ] Roof color/finish identical across all views
- [ ] Siding/cladding color identical, including warmth/coolness of tone
- [ ] Window frame color identical (aluminum type, anodize finish)
- [ ] Door color and frame material identical
- [ ] Foundation color and texture consistent
- [ ] Trim and accents the same color in every render
- [ ] Gutter and downspout color matches
- [ ] Metal flashing color consistent

### Implementation:

Create a "Material Palette" reference that lists every material on the building with its specification:

```
MATERIAL PALETTE FOR PROJECT:
- Roof: Light gray standing seam metal (Pantone Cool Gray 3), matte finish
- Wall Cladding: Warm gray composite panels (Benjamin Moore HC-159), slight champagne undertone
- Entry Storefronts: Clear annealed glass, dark bronze anodized aluminum frames (Duranodic 615)
- Overhead Doors: White painted steel (Sherwin-Williams 7005), matte
- Foundation: Concrete, medium gray finish, slightly weathered appearance
- Trim: Dark gray aluminum angles (Duranodic 700), matches window frames
```

Paste this into every prompt as a reference.

---

## 3. Site Consistency

The environment surrounding the building must be stable unless intentionally varied for seasonal or conditional comparisons.

### Environmental Constants:

For all renderings of the same condition, maintain:

**Time of Day:**
- Establish a default (e.g., "mid-afternoon, sun at 35 degrees elevation from south")
- Use consistent shadow angles across all views
- If varying time of day intentionally, note it clearly in the prompt

**Season & Vegetation:**
- Specify vegetation state: "early spring with deciduous trees showing new foliage, ground cover dormant brown"
- Use consistent species: "native ornamental grasses, serviceberry shrubs, not tropical plants"
- Same shrub size and density across views

**Weather & Sky:**
- Default sky condition: "clear blue sky with natural scattered clouds"
- Consistent cloud distribution in same region of sky
- If showing storm/snow/other conditions, make it intentional and consistent

**Parking & Site Features:**
- Specify parking lot fill pattern, color, line marking color
- Consistent vehicle placement (color, type, angle) if shown
- Same landscaping bed configuration and mulch color
- Consistent pavement color if showing hardscape

**Lighting Quality:**
- Same sun direction and intensity across views
- Consistent shadow length and density
- If using artificial lighting (dusk scene), maintain consistent light colors and positions

### Site Consistency Reference Block:

```
SITE CONTEXT (REUSE IN ALL PROMPTS):
Season: Late Spring. Vegetation: Native deciduous shrubs with full green foliage (serviceberry,
oakleaf hydrangea), landscape beds with bark mulch, ornamental grasses. Sky: Clear blue,
scattered white clouds. Sun: South-facing, mid-afternoon (35° elevation), warm quality light.
Pavement: Asphalt, medium gray, fresh striping. Parking configuration: Angled stalls,
vehicles parked (sedans, SUVs, hospital visitor vehicles), white stripe lines.
No people visible. Atmosphere: Clear, 75F conditions implied.
```

---

## 4. Scale Consistency

Scale errors destroy consistency. A door that's 3 feet tall in one render but looks 4 feet in another immediately signals an error.

### Reference Dimensions to Lock:

Establish these in the master spec and maintain across all views:

- **Building footprint dimensions** (e.g., "75' wide x 132' deep")
- **Eave height** (e.g., "16 feet from grade")
- **Entry door height** (typically 7'-6" for commercial, 6'-8" for standard)
- **Window dimensions** (e.g., "4 feet wide x 4 feet tall")
- **Storefront height** (e.g., "10 feet floor-to-sill of transom")
- **Parking spaces** (typically 9 feet wide)
- **Landscape shrub mature height** (e.g., "serviceberry 12-15 feet tall")

### Proportion Verification:

After generating a new view, visually compare:
- Door width relative to wall section (should be consistent ratio)
- Window count per elevation matches other views
- Roofline height compared to entry height
- Vehicle length compared to parking space
- Shrub height compared to building height

### Scale Reference Block:

```
SCALE SPECIFICATIONS (INCLUDE IN ALL PROMPTS):
Building: 75 feet wide, 132 feet deep, 16-foot eave height, 1:12 roof slope.
Entry doors: 3 feet wide x 7 feet 6 inches tall, recessed 2 feet.
Windows: Storefront 4 feet wide x 4 feet tall, transom 3 feet wide x 18 inches tall.
Landscape shrubs: Mature 12-15 feet tall (serviceberry, hydrangea).
Vehicles: Standard SUVs and sedans, 15 feet long, parked in 9-foot wide spaces.
```

---

## 5. Style Consistency

The rendering style and quality level must remain constant unless intentionally changing style for a different use case (e.g., sketch for design phase, photorealistic for final presentation).

### Style Dimensions to Control:

- **Rendering technique** (photorealistic, illustration, watercolor, etc.)
- **Quality level** (8K detail, or intentionally softer)
- **Saturation** (natural color, or slightly enhanced)
- **Lighting drama** (flat architectural lighting, or cinematic dramatic lighting)
- **Detail level** (every material variation visible, or simplified geometric forms)
- **Camera characteristics** (DSLR lens simulation, wide-angle perspective, etc.)

### Style Lock for Project:

```
RENDERING STYLE (INCLUDE IN ALL PROMPTS):
Professional photorealistic architectural rendering, 8K quality, sharp architectural focus,
linear perspective with correct vanishing points, warm afternoon sunlight creating soft shadows,
slight depth of field keeping building in crisp focus. Digital painting technique with photographic
realism. Color saturation slightly enhanced for presentation clarity. No artistic abstraction.
```

If this block is identical in every prompt, the stylistic quality will remain consistent.

---

## 6. Color Matching Precision

Color inconsistency is the most visible consistency failure. A wall that looks warm gray in one render but cool gray in another is immediately jarring.

### Color Specification Hierarchy:

1. **Use paint brand/color codes** (Sherwin-Williams SW 7005, Benjamin Moore HC-159)
2. **Include descriptive modifiers** ("warm gray" vs "cool gray", "champagne undertone")
3. **Add reference** ("similar to concrete sidewalk gray" or "matching aluminum window frames")
4. **Specify saturation** ("natural matte finish" vs "lustrous eggshell")

### Example Color Blocks:

```
Colors (EXACT SPECIFICATION FOR CONSISTENCY):
- Roof metal: Pantone Cool Gray 3, standing seam pattern, matte finish
- Wall composite panels: Benjamin Moore HC-159 Ashwood Gray, warm champagne undertone, matte
- Entry frames: Dark bronze anodized aluminum (Duranodic 615)
- Glass: Clear annealed, slight green tint from thickness
- Foundation concrete: Medium gray (slightly darker than panels), weathered matte finish
- Trim: Matches window frames, dark bronze, matte
- Pavement: Asphalt medium gray, 50-foot-wide with center yellow line
```

### Color Matching in AI Generation:

When regenerating a view:
- Include the exact color block from the master render
- If the AI produces slightly different color, use subsequent regenerations with explicit "match the warm gray tone from the south elevation" guidance
- Gemini and Flux both allow reference image input — show the hero render and ask "use the same colors as this image"

---

## 7. Reference Image Workflow

Gemini supports reference images in prompts. This is a powerful consistency tool.

### Process:

1. Generate and approve the hero rendering
2. Save it locally
3. For subsequent views, upload the hero rendering to Gemini and reference it explicitly:

```
"Generate a west elevation view of this building.
Reference image shows the approved color palette and style.
Use identical materials, finishes, and colors. Only the viewing angle changes."
```

4. This dramatically improves consistency because the AI has visual reference for exact colors and proportions

### When to Use Reference Images:

- ✓ When generating variations (different view angle, different season, different time of day)
- ✓ When color accuracy is critical
- ✓ When scale and proportion must match exactly
- ✗ Not needed for first render (hero image)
- ✗ Not necessary if style/materials will intentionally change

---

## 8. Post-Generation QA Checklist

After generating each new rendering, immediately verify consistency:

### Geometric Verification:

- [ ] Building footprint matches master spec (e.g., 75' x 132')
- [ ] Eave height appears correct relative to entry door height (16' should be ~2x door height)
- [ ] Roof slope visible and correct angle (1:12 = very shallow)
- [ ] Window dimensions consistent with other views
- [ ] Door heights match across all views
- [ ] Building doesn't appear wider/narrower than other angles
- [ ] Foundation depth (stem wall height) visible and consistent

### Material Verification:

- [ ] Roof color matches hero rendering exactly
- [ ] Wall cladding color matches (warm vs cool gray, saturation level)
- [ ] Entry frame color matches other views
- [ ] Glass reflection quality and color consistent
- [ ] Foundation color matches (not too light, not too dark)
- [ ] Trim and accent colors consistent
- [ ] No unexpected material appearances (sudden different texture, color shift mid-surface)

### Environmental Verification:

- [ ] Sky color and cloud pattern appropriate for season
- [ ] Shadow angles consistent with established sun direction
- [ ] Vegetation density and type matches other views
- [ ] Vegetation color appropriate for established season
- [ ] Pavement color consistent
- [ ] Vehicles (if shown) same type and color as other renders
- [ ] Overall lighting warmth/coolness matches established time of day

### Composition Verification:

- [ ] Building is single coherent subject (not merged with adjacent structures)
- [ ] Viewing angle clearly labeled or documented
- [ ] Depth of field appropriate (building sharp, background soft)
- [ ] Sky-to-building ratio appropriate
- [ ] Image framing natural, no abrupt cutoffs
- [ ] Horizon line level (not tilted unless intentional)

### Comparison Verification:

- [ ] When compared to master render, materials appear identical
- [ ] When compared to other elevations, proportions match
- [ ] Color appears same when rendering placed side-by-side with hero image
- [ ] Style and quality level matches (same photorealism level, same saturation)

---

## 9. Common Consistency Failures and Prevention

### Failure: Roof Color Shifts

**Symptom:** South elevation shows light gray roof, east elevation shows medium gray or even warm tan roof.

**Cause:** AI interprets "gray roof" differently in each prompt, or light angle makes color appear different.

**Prevention:**
- Always use specific color code: "Light gray standing seam metal, Pantone Cool Gray 3, matte finish"
- Include exact color in every prompt, not just in initial brief
- Use reference image showing approved roof color
- In prompt, explicitly state: "Roof color must match the south elevation"

### Failure: Window Count or Spacing Inconsistency

**Symptom:** South elevation has 6 windows evenly spaced, but west elevation shows 5 windows with different spacing.

**Cause:** AI doesn't understand architectural layout consistency.

**Prevention:**
- Include facade rhythm in building spec: "Storefront windows 4 feet wide x 4 feet tall, spaced 3 feet apart"
- For each elevation, count windows in the previous render and include in new prompt: "This elevation has 6 entry storefronts matching the south facade"
- Use reference image from previous elevation

### Failure: Entry Recess Changes Depth

**Symptom:** Hero render shows 2-foot entry recess, but next elevation shows either flush entry or 4-foot recess.

**Cause:** Depth/perspective confusion in AI.

**Prevention:**
- Lock the recess depth in building spec: "Entries recessed 2 feet from facade plane"
- Include in every prompt: "Entry storefronts are 2 feet recessed from outer wall plane"
- Use reference image if available

### Failure: Foundation Height Inconsistency

**Symptom:** One render shows barely visible 12-inch stem wall, another shows prominent 36-inch stem wall.

**Cause:** Viewpoint and grading assumptions vary.

**Prevention:**
- Specify exactly: "24-inch tall poured concrete stem walls visible above grade"
- Include in every prompt
- Verify in reference image workflow

### Failure: Material Surface Appearance Changes

**Symptom:** Wall panels look smooth and matte in one render, then appear plasticky and glossy in another.

**Cause:** AI's interpretation of finish varies.

**Prevention:**
- Specify finish explicitly: "Matte finish, not glossy, realistic slight weathering and surface variation"
- Include in every prompt: "Material finishes: matte, not reflective"
- Use reference image

### Failure: Color Temperature Shift

**Symptom:** Hero image has warm champagne undertone in gray panels, but next elevation appears cool blue-gray.

**Cause:** AI applies different color temperature interpretation.

**Prevention:**
- Be explicit: "Warm gray composite panels with champagne undertone, NOT cool blue-gray"
- Include warm/cool descriptor in every prompt
- Use reference image to anchor color temperature
- In follow-up regeneration, state: "Use the warm color tone from the reference image, not cool blue-gray"

### Failure: Scale Drift

**Symptom:** Doors that look right-sized in one view appear disproportionately tall or short in another.

**Cause:** AI doesn't maintain consistent scale relationships between elements.

**Prevention:**
- Lock scale in building spec: "Entry doors 3 feet wide x 7 feet 6 inches tall, storefront windows 4 feet wide x 4 feet tall, building 16-foot eave, 75 feet wide"
- Include scale specs in every prompt
- Use reference image showing correct proportions
- Manually verify door-to-window ratio, door-to-eave ratio, etc. after generation

---

## 10. Session-Based Prompt Management

For a project with many renderings, maintain a master prompt document that evolves with each approved render.

### Template Structure:

```
PROJECT: [Project Name]
STATUS: Building Identity LOCKED as of [Date]
HERO RENDER: [Image reference, date approved]

═══════════════════════════════════════════════════════════════

BUILDING IDENTITY BLOCK (COPY INTO EVERY PROMPT):

[Full building description with all materials, colors, dimensions, scales]

═══════════════════════════════════════════════════════════════

MATERIAL PALETTE (COPY INTO EVERY PROMPT):

[Exact color specifications, finishes, brands]

═══════════════════════════════════════════════════════════════

SITE CONTEXT (COPY INTO EVERY PROMPT):

[Season, vegetation, sky, sun angle, parking, pavement]

═══════════════════════════════════════════════════════════════

SCALE SPECIFICATIONS (COPY INTO EVERY PROMPT):

[Building dimensions, door sizes, window sizes, vehicle sizes, landscape sizing]

═══════════════════════════════════════════════════════════════

RENDERING STYLE (COPY INTO EVERY PROMPT):

[Style, quality level, camera characteristics, lighting approach]

═══════════════════════════════════════════════════════════════

QUALITY MODIFIERS (APPEND TO EVERY PROMPT):

[See avoidance-terms.md master quality block]

═══════════════════════════════════════════════════════════════

APPROVED RENDERS (FOR REFERENCE):

1. Hero - South 3/4 View [Date] - APPROVED
   - Prompt hash: [identifier]
   - Colors locked
   - Materials locked
   - Scale verified

2. West Elevation [Date] - APPROVED
   - Prompt hash
   - Color comparison to hero: MATCH
   - Scale comparison to hero: MATCH

[Continue list for each approved render]

═══════════════════════════════════════════════════════════════

CURRENT GENERATION (IN PROGRESS):

View: [e.g., North Elevation]
Prompt: [Full prompt template with only view-specific changes]
Reference image: [Hero render uploaded]
Status: [Awaiting generation / Reviewing / Approved]

Notes: [Any consistency concerns, regeneration requests, etc.]

═══════════════════════════════════════════════════════════════
```

### Usage Workflow:

1. Start project with hero render generation using full building spec
2. Once hero approved, lock the Building Identity Block
3. For each new view, copy the entire locked blocks and only modify the view/angle section
4. Maintain the "Approved Renders" log with comparison notes (color match? scale match?)
5. If consistency issues arise, update the Building Identity Block and regenerate all renders
6. Document any revisions to materials/colors and the date of approval

---

## Summary: The Consistency Protocol

**For every rendering beyond the hero image:**

1. ✓ Copy the entire locked Building Identity Block into the new prompt
2. ✓ Copy the Material Palette block
3. ✓ Copy the Site Context block
4. ✓ Copy the Scale Specifications block
5. ✓ Copy the Rendering Style block
6. ✓ Upload hero render as reference image if available
7. ✓ Change ONLY the view/angle/time-of-day specification
8. ✓ Generate and immediately run QA checklist
9. ✓ If issues found, regenerate with explicit correction ("match the warm gray from the hero image")
10. ✓ Log the approved render with comparison notes

This systematic approach ensures that a south elevation, west elevation, north elevation, and 3/4 view all appear to be the same building — because they are, built from the identical specification.

