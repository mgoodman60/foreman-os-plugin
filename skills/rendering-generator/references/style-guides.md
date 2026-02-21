# Rendering Style Guides
## Foreman OS Rendering-Generator Reference

Each rendering style serves a different purpose in the project lifecycle. This guide provides detailed specifications for each style, including when to use it, complete prompt blocks for consistency, example characteristics, and practical tips for achieving professional results.

---

## PHOTOREALISTIC

### Description

Professional architectural photography rendered with digital precision. The output should be indistinguishable from a high-quality DSLR photograph taken on-site. This style uses advanced lighting simulation, material physics, true linear perspective, and photographic depth of field.

**Key Characteristics:**
- Photographic realism with no artistic interpretation
- HDR-like color and dynamic range
- Sharp architectural focus with selective depth of field
- Accurate linear perspective with correct vanishing points
- DSLR camera characteristics (lens distortion patterns, sensor color characteristics)
- Soft natural shadows or dramatic directional lighting depending on sun angle
- Realistic material reflectivity (matte, satin, gloss) matching actual finishes
- Environmental context fully detailed and realistic

### When to Use

- **Client presentations** — Shows final design in most convincing, professional manner
- **Marketing materials** — Website images, brochures, proposal photos
- **Design approval** — When client needs to visualize exact final appearance
- **Final design visualization** — End of design development, value engineering review
- **Investor presentations** — Demonstrates confidence in design quality
- **Permit applications** — Some jurisdictions request photorealistic renderings

### Photorealistic Prompt Block

```
RENDERING STYLE: Photorealistic Architectural Rendering

Professional architectural photography, 8K resolution, photorealistic digital painting technique,
rendered as if photographed by Canon EOS R6 with 35mm lens. Warm afternoon sunlight (2:00 PM,
sun at 45 degrees elevation from south) creating soft directional shadows with penumbra.

Camera settings: f/4.0 aperture, shallow depth of field with building in sharp focus, soft
background blur (bokeh). White balance: daylight (5200K). Slight lens flare from low sun angle.

Material rendering: Physically accurate surface properties. Metal panels with slight matte finish,
subtle micro-texture, realistic weathering. Glass with true refraction and reflection, not pure
mirror. Concrete with fine surface variation and slight color mottling. Aluminum frames with
anodized finish, minimal reflection.

Lighting: Single primary light source (sun) with realistic atmospheric scattering. Soft shadows
on north side. Highlights on south-facing surfaces. Sky: clear blue (Pantone 279C) with natural
scattered clouds, not perfectly uniform. Atmospheric perspective: background trees slightly desaturated,
foreground sharp and saturated.

Color: Natural color saturation, true-to-life tones. No oversaturation or cartoon-like coloring.
Warm color temperature from afternoon sun creating golden highlights on south-facing surfaces.
Shadows have cool undertones from sky fill light.

Image quality: No watermark, no visible digital artifacts, clean edges with natural vignette,
appropriate depth of field for architectural focus. Total immersion effect—viewer feels standing
on site observing actual building.
```

### Example Output Characteristics

- **Lighting:** Soft afternoon directional light with accurate shadow placement and soft edges
- **Materials:** Clearly visible material differences; metal appears metallic but not mirror-like; concrete looks concrete-like with surface variation; glass is transparent with subtle reflections
- **People/vehicles:** If included, photorealistic humans with proper proportions and natural poses; realistic vehicles with correct shadows and reflections
- **Sky:** Clear blue with scattered natural clouds, atmospheric perspective visible
- **Detail:** All surface details visible; weathering, texture, panel seams, fasteners, shadows under eaves all present
- **Color accuracy:** Colors appear natural; warm gray looks warm gray, not cool blue or oversaturated

### Tips for Photorealistic Success

1. **Specify exact time of day** — "2:00 PM sun at 45 degrees elevation" produces consistent shadow angles
2. **Use camera specifications** — "Canon EOS R6 with 35mm lens" helps AI understand perspective and depth
3. **Describe lighting quality** — "Soft directional shadows" vs "harsh shadows" dramatically changes output
4. **Lock material properties** — Explicitly state "matte finish, not glossy" and "realistic weathering"
5. **Sky specification matters** — "Clear blue with scattered clouds" vs "overcast gray" creates very different mood
6. **Include atmospheric perspective** — "Background softly desaturated, foreground sharp" creates depth
7. **Regenerate for shadows** — First generation may need adjustment for shadow placement; use reference image to lock
8. **Avoid "ultra-realistic"** — This often produces uncanny rendering; stick with "photorealistic" or "architectural photography"

---

## ILLUSTRATION

### Description

Clean, precise architectural illustration with strong line work and accurate color rendering. Modern presentation technique using pen-and-wash or digital painting methods. Lines are intentional and bold; forms are clearly defined. This is NOT a sketch—it's a refined, professional illustration with perfect proportions and clean execution.

**Key Characteristics:**
- Distinct, intentional linework (architectural pen lines)
- Precise geometric forms and clean edges
- Color applied as flat or gradient washes (watercolor-like application)
- Perfect architectural proportions and alignment
- No photographic realism, but no roughness either
- Clear readability of form and material distinction
- Professional illustration quality
- Technique visible but refined (pen strokes intentional, not loose)

### When to Use

- **Design development phase** — Quickly shows design concepts without photorealism
- **Schematic presentations** — Planning meetings, design charrettes, concept review
- **Planning board submissions** — Many jurisdictions prefer illustration over photorealism for public presentations
- **Design competition submissions** — Standard presentation technique for many design awards
- **Education and process documentation** — Shows design thinking without claiming photorealism
- **Material study sheets** — Comparing material options cleanly
- **Fast turnaround renderings** — Illustration often generates cleaner results than photorealistic attempts

### Illustration Prompt Block

```
RENDERING STYLE: Architectural Illustration

Professional architectural illustration, digital painting with visible pen and watercolor technique.
Precise linework with intentional architectural pen strokes (0.3-0.7mm black lines defining forms,
material edges, window frames, trim details). Clean geometric forms with perfect proportions and
alignment. No imperfection or looseness—refined professional illustration quality.

Color application: Watercolor-like washes applied cleanly over linework. Material colors as flat
or gradient fields. Soft color transitions suggesting form and shadow without photorealism.

Materials rendered clearly but not photographically: Metal surfaces suggested by color tone,
not metallic reflection. Glass suggested by blue or purple tint and frame outline, not true
reflections. Concrete by gray tone with slight variation. Vegetation by shape and green tone,
not photographic texture.

Perspective: Perfect linear perspective with correct vanishing points. Proportions accurate and
verifiable with ruler. Grid lines could be drawn and would be perfectly aligned (but invisible).

Lighting: Suggested through color value (lighter and darker areas) rather than realistic shadows.
Single directional light source implied but not harsh. Shadows present as color value changes,
not photorealistic darkness.

Background: Simple, clean. Sky as flat light blue or subtle gradient. Ground plane simple green
or gray. Adjacent structures simplified to silhouettes or blocked-out forms. No photographic
environmental detail. Focus entirely on primary building.

Color: Slightly elevated saturation from reality—not oversaturated, but colors are vibrant and
clear. Warm and cool tones applied intentionally for visual interest and depth.

Line quality: Ink lines are clean, consistent weight or intentional weight variation. Linework
visible and intentional. No blurriness. Perfect registration between lines and color fields.

Overall effect: Looks like professional architectural drawing executed by skilled hand (though
digitally rendered). Appropriate for planning board presentation or design publication.
```

### Example Output Characteristics

- **Line work:** Clear, intentional lines defining building edges, window mullions, material transitions, trim
- **Color:** Vibrant but natural color fields; flat or subtle gradients; no photorealism
- **Materials:** Distinct visual difference between metal, glass, concrete, etc., through color/tone/line weight
- **Shadow:** Suggested through value change, not harsh or photorealistic
- **Perspective:** Perfect geometry; proportions verifiable
- **Background:** Simple, uncluttered; drawing focuses on building
- **Detail:** Sufficient detail to understand design; minor elements simplified
- **People/vehicles:** Simplified but correctly proportioned; illustration style, not photorealistic

### Tips for Illustration Success

1. **Emphasize clean linework** — "Intentional architectural pen strokes, clean lines" prevents muddy output
2. **Specify illustration technique** — "Pen and watercolor wash" or "digital painting with visible technique" guides style
3. **Include precision language** — "Perfect proportions," "clean geometric forms," "professional quality" prevents looseness
4. **Lock color application** — "Flat color fields with subtle gradients, not photographic textures"
5. **Simplify backgrounds** — "Simple clean background, focus on building, sky as light blue, ground as simple color field"
6. **Specify line weight** — "0.3-0.7mm black lines" helps define linework precision
7. **Avoid "watercolor sketch"** — Too loose; "architectural illustration" is tighter and more refined
8. **Color saturation matters** — Illustration slightly more saturated than photorealistic; specify "vibrant but natural color"
9. **Perspective must be perfect** — "Correct linear perspective with proper vanishing points, verifiable proportions"
10. **Reference architectural style guides** — Show examples from architecture magazines (Architectural Record, Architecture Today, etc.)

---

## WATERCOLOR

### Description

Soft, atmospheric watercolor painting with loose interpretive approach. This style suggests architectural form rather than defining it precisely. Focus is on atmosphere, light, and emotional quality rather than technical accuracy. Appropriate for early design concepts and community engagement where artistic expression is valued over technical precision.

**Key Characteristics:**
- Loose, flowing brushwork
- Soft color transitions and blooms
- Suggests form through color and value, not precise line
- Transparent color layering (true watercolor characteristics)
- Atmospheric perspective emphasized
- Minimal detail; form suggested rather than defined
- Painterly quality with visible brushstrokes
- Emotional/impressionistic approach to architecture

### When to Use

- **Early design concepts** — Before proportions are locked, before precision is needed
- **Community presentations** — Public meetings where artistic expression builds engagement
- **Design vision statements** — Communicating intent and feeling, not technical details
- **Artistic competitions** — Where watercolor technique is valued
- **Renovation/heritage projects** — Watercolor is associated with preservation and tradition
- **Soft-approach marketing** — For projects emphasizing aesthetic experience over technical data
- **Design team brainstorming** — Quick visual exploration of mood and form

### Watercolor Prompt Block

```
RENDERING STYLE: Watercolor Architectural Painting

Traditional watercolor painting technique rendered digitally with authentic watercolor characteristics.
Loose, flowing brushwork with visible individual strokes. Soft color transitions and natural color
blooms where pigments merge on wet paper. Semi-transparent color layering allowing underpainting
to show through. No harsh edges; soft transitions throughout.

Form rendering: Building suggested through color value and shape rather than defined by precise
line. Forms emerge from color and light, not from outline. Details minimized and suggested
(windows implied by darker blue field, door suggested by rectangular form, not defined by line).

Color application: Transparent watercolor washes in layers. First wash light, subsequent washes
add darker values and detail. Colors bleed and blend naturally where they overlap. No flat color
fields—all color areas have subtle variation and organic quality.

Perspective: Loose perspective suggested rather than mechanically perfect. Some skew acceptable
and appropriate to artistic style. Proportions approximate, not measured. Building tilts slightly
if artistic effect is improved.

Lighting: Soft, diffuse light suggested through overall value range. Sky often dominant, blending
into landscape. Shadows are color value changes, very soft, often purple or cool tones. Highlights
are paper white or pale yellow, not bright.

Sky and atmosphere: Dominant element. Often takes up 40-60% of composition. Sky is loose color
washes of blue, purple, pink depending on time of day. Clouds are soft, undefined edges, colors
bleeding through. Atmospheric perspective: background very soft and muted, foreground slightly
sharper (relatively).

Background: Landscape of simple green and earth tones, suggested rather than detailed. Trees are
silhouettes or soft green shapes, no individual leaves visible. Pavement is simple gray or tan wash.
Adjacent structures barely suggested.

Paint finish characteristics: Water stains visible in appropriate places. Pigment granulation visible.
Paper texture subtle but present (rough watercolor paper surface suggested). Color blooms where
pigments meet water. All organic, all natural watercolor effects.

Overall emotion: Peaceful, artistic, contemplative. Building shown in context of landscape and
light, not as isolated object. Emphasis on how light plays on form and atmosphere.
```

### Example Output Characteristics

- **Brushwork:** Visible, loose, flowing strokes; no tight detail
- **Color:** Semi-transparent layers; colors blend and transition softly; natural blooms where colors meet
- **Sky:** Dominant and beautiful; soft clouds with bleeding edges; multiple color transitions
- **Form:** Building suggested by color and shape; details implied, not defined; windows shown as darker blue areas, not with exact mullion lines
- **Perspective:** Slightly loose; skew acceptable if artistically appropriate
- **People/vehicles:** Not usually included; if present, suggested forms, not detailed
- **Landscape:** Simple; trees as soft silhouettes; ground as simple color washes
- **Paper texture:** Subtle texture visible; organic, natural appearance

### Tips for Watercolor Success

1. **Emphasize looseness** — "Loose flowing brushwork," "soft transitions," "form suggested not defined" prevents tight results
2. **Specify transparency** — "Transparent watercolor washes in layers," "colors bleed and blend" guides technique
3. **Include bloom/wash effects** — "Pigment blooms where colors merge," "water stains visible" adds authenticity
4. **Minimize detail** — "Details minimized and suggested, no fine linework" prevents over-finishing
5. **Emphasize atmosphere** — "Dominant sky," "atmospheric perspective," "soft lighting" focuses emotional impact
6. **Use artistic language** — "Painterly," "impressionistic," "contemplative" vs technical language
7. **Allow looseness in perspective** — "Loose perspective, slight skew acceptable if artistically appropriate"
8. **Soft value ranges** — "Low contrast, soft shadows, highlights are pale, no bright whites except paper" prevents harsh appearance
9. **Composition heavy on sky** — "Sky dominates composition, 40-50% of image" creates typical watercolor effect
10. **Post-processing:** May benefit from slight softening in Photoshop to enhance watercolor bloom effects

---

## DIAGRAM

### Description

Technical architectural diagram with clean isometric or orthographic projection, labeled elements, and clear instructional purpose. This is architecture drawn for clarity and technical communication, not aesthetic presentation. Diagram style uses simple colors, precise linework, and explanatory annotations.

**Key Characteristics:**
- Isometric or orthographic projection (not perspective)
- Clean, uniform line weight
- Flat color fills with no shading or gradient
- Labeled elements and systems
- Grid background optional but common
- Minimal environmental context (white or neutral background)
- Focus on clarity and instructional value
- Technical accuracy paramount

### When to Use

- **Construction sequencing** — Showing building phases or assembly order
- **System diagrams** — HVAC flow, plumbing layout, electrical distribution, structural frame
- **Technical specifications** — Material callouts, assembly details, dimension annotations
- **Site logistics** — Equipment placement, crane locations, staging areas
- **MEP coordination** — Showing mechanical, electrical, plumbing routes and conflicts
- **Code compliance documentation** — Exit routes, fire-rated assemblies, accessibility features
- **Maintenance documentation** — System identification, equipment location, service access
- **Budget presentations** — Cost breakdown by building system or phase

### Diagram Prompt Block

```
RENDERING STYLE: Technical Architectural Diagram

Clean technical diagram with isometric projection and clear instructional purpose. Not perspective
rendering; use true isometric geometry (30/30/30 degree angles). Linework uniform weight, sharp
and clean, black or dark gray on white or light background. No drop shadows, no artistic effects.

Color usage: Flat, solid colors filling geometric forms. No gradients, no shading, no texture.
Colors used for system identification (e.g., red for structural, blue for MEP, green for site).
Colors must be consistent across views and legible at small scale. High contrast.

Projection: True isometric or orthographic, not perspective. Building shown with consistent scale
and geometry maintainable throughout. Dimensions and measurements would verify exactly.

Elements shown: Primary building systems visible—structural frame, roof, walls shown as planes,
major penetrations, equipment locations. Style and architecture secondary to system clarity.
Material finishes not shown; material distinction through color only.

Environment: Minimal context. Typically shown on white or light gray background. Ground plane shown
as simple line (light gray). Sky not shown or minimal (removed or white). Adjacent structures shown
as simplified forms (gray or uncolored blocks) only if necessary for context. Focus entirely on
primary subject.

Annotations: Callout lines pointing to elements. Text labels for key components. Dimensions if
relevant. Arrows showing flow direction (for MEP) or sequence (for phasing). Text is clean,
sans-serif, legible at 50% scale. No decorative fonts.

Detail level: Simplified geometric representation. No material texture, no weathering, no fine
detail. Only information relevant to instructional purpose is shown. Extraneous detail omitted.

Overall effect: Looks like drawing created in CAD software or technical illustration program.
Could serve in construction documents, systems manual, or site plan set.
```

### Example Output Characteristics

- **Lines:** Clean, uniform weight, sharp edges, black or dark gray on white
- **Color:** Flat solid fills; high contrast; colors consistent across all diagrams
- **Projection:** Isometric or orthographic; not perspective; geometry is true and verifiable
- **Elements:** Building systems clearly identified; structural frame visible if relevant
- **Background:** White or light gray; minimal environmental context
- **Labels:** Clear callouts pointing to important elements; sans-serif text
- **Scale:** Grid or dimension lines if needed for scale reference
- **Complexity:** Simplified to show only necessary information

### Tips for Diagram Success

1. **Specify isometric projection** — "True isometric projection, 30/30/30 degree angles, not perspective"
2. **Emphasize clarity** — "Clear and legible at small scale," "high contrast," "clean uniform linework"
3. **Lock color meaning** — Define color system upfront: "Red for structural, blue for MEP, green for site"
4. **Minimize environment** — "White background, no sky, minimal surrounding context, focus on subject"
5. **Omit artistic effects** — "No drop shadows, no gradients, no texture, flat solid colors only"
6. **Include annotation guidance** — "Clear callout lines and labels," "sans-serif font," "legible at 50% scale"
7. **Simplify geometry** — "Simplified geometric forms, no material detail or weathering"
8. **Consider CAD-style output** — "Drawn with precision, could be output from CAD software"
9. **Testing regeneration** — Diagrams sometimes need explicit element callouts: "Show windows as blue rectangles with clear outline"
10. **Grid reference optional** — Light grid in background can help with scale but adds visual complexity

---

## SKETCH

### Description

Hand-drawn architectural sketch aesthetic with visible pencil lines or ink, intentional loose quality, and construction line visibility. This style conveys design thinking in progress—authentic architect's sketch feel. Not loose and rough, but intentionally sketchy with visible design process.

**Key Characteristics:**
- Visible construction lines or light guide lines
- Hand-drawn line quality (not perfectly straight)
- Loose, light linework in some areas, darker defining lines in others
- Pencil or ink media appearance
- Proportions approximately correct (not perfect, not wildly wrong)
- Minimal color, possibly none (or very light wash)
- Sketch appear genuine and accomplished, not crude
- Design thinking visible in process

### When to Use

- **Concept exploration** — Early design phases where precision not yet determined
- **Design review meetings** — Sketches convey openness to feedback
- **Client-facing feasibility studies** — Shows thoughtful approach without overcommitment
- **Renovation/adaptation studies** — Sketches appropriate for exploring existing conditions
- **Architectural publication/books** — Sketch approach more interesting than perfect rendering
- **Brainstorming documentation** — Shows creative thinking process
- **Quick value studies** — Testing proportions, massing, composition
- **Heritage and restoration projects** — Sketch approach respectful of tradition

### Sketch Prompt Block

```
RENDERING STYLE: Architectural Sketch

Hand-drawn sketch aesthetic showing architect's design thinking. Pencil linework, strokes visible,
natural line quality with slight variation in pressure. Construction lines visible in places—light,
guide lines used to establish proportions and perspective. Darker lines define primary edges and
forms. Sketch has authentic hand-drawn quality but is accomplished and intentional, not crude or sloppy.

Linework: Variable line weight showing design hierarchy. Fine guide lines used for proportion and
perspective (visible but light). Darker, more confident strokes define major edges: building outline,
roofline, major openings, primary structure. Medium weight strokes show secondary details: window
mullions, door frames, trim, material divisions.

Construction visible: Light pencil grid or guide lines establishing perspective suggest how drawing
was developed. Vanishing point marks may be faintly visible. Proportion guidelines visible but not
obtrusive. Suggests drawing created with measurement and intention, not just free-hand.

Perspective: Correct linear perspective with accurate proportions, but execution shows hand-drawn
quality. Lines nearly straight but with subtle hand-drawn variation (not digitally perfect). Perspective
is accurate enough to be verifiable but loose enough to feel genuine.

Color: Minimal. Sketch may be pure graphite/ink (no color) or have very light color wash adding
material distinction (light gray for concrete, light blue for glass, green for vegetation). Color
application loose if present; no fine detail. Sketch maintains drawing character even with color.

Materials shown: Basic material distinction through line pattern or minimal color. Brickwork shown
as simple grid pattern, not individual bricks. Glass shown as lighter area or blue tint. Concrete
shown as simple gray tone. Materials suggested, not detailed.

Environment: Minimal context. Surrounding landscape very simple—few lines suggesting ground and
horizon. Adjacent buildings shown as simple blocked forms. Trees as light marks suggesting shape
and foliage mass, not individual leaves. Focus on primary building.

Shading/tone: Light graphite shading showing form and shadow. No harsh shadows or high contrast.
Shading is loose and suggestive. Areas in shade slightly darker, but maintain sketch character.

Overall effect: Looks like talented architect's preliminary sketch—serious and accomplished design
thinking captured in pencil. Could appear in architectural publication or design competition board.
```

### Example Output Characteristics

- **Lines:** Visible hand-drawn quality; variable weight; construction lines visible; light and dark intentional
- **Perspective:** Correct and verifiable, but with hand-drawn character; not digitally perfect
- **Color:** Minimal; light wash if present; materials suggested through color, not detailed
- **Materials:** Simple representation—brick as grid, glass as lighter area, concrete as light tone
- **Construction visible:** Light guide lines for proportion and perspective show design process
- **Environment:** Simple surrounding landscape; adjacent structures as simple blocks; trees as basic shapes
- **Proportions:** Accurate and lockable; not sloppy, but not perfect either
- **Shading:** Light; suggests form and shadow without harsh contrast

### Tips for Sketch Success

1. **Emphasize visible process** — "Hand-drawn quality," "construction lines visible," "design thinking evident"
2. **Specify line variety** — "Light guide lines establish perspective, darker strokes define edges"
3. **Lock proportion accuracy** — "Proportions correct and verifiable, but executed with hand-drawn quality"
4. **Minimal color guidance** — "Sketch may be pure graphite or very light color wash"
5. **Include authenticity language** — "Accomplished sketch, serious design thinking, not crude or sloppy"
6. **Suggest materials minimally** — "Materials shown through simple pattern (brick as grid) or minimal color"
7. **Simplify environment** — "Minimal context, simple landscape, focus on building"
8. **Allow hand variation** — "Lines nearly straight but with subtle hand-drawn variation, not digitally perfect"
9. **Reference architect sketch books** — Show examples from renowned architects' preliminary sketches
10. **Shading should be light** — "Light graphite shading, suggests form, not harsh shadows"

---

## MATTE PAINTING

### Description

Cinematic, dramatic architectural image with film-quality environment art approach. This style emphasizes composition, lighting drama, and atmosphere above all. The building is hero subject in a carefully composed cinematic scene. This is the most dramatic and visually striking style—appropriate for aspirational visualization and high-stakes presentations.

**Key Characteristics:**
- Dramatic directional lighting (cinematic approach)
- Masterful composition and framing
- Rich atmospheric effects (mist, volumetric lighting, dramatic clouds)
- Deep perspective and environmental depth
- Film production quality
- Building is hero subject in carefully composed frame
- Strong mood and emotional impact
- Advanced lighting techniques (rim lighting, god rays, practical light)

### When to Use

- **Hero images for marketing** — Main image for website, proposal cover, investor pitch
- **Visionary presentations** — Communicating aspirational project goals
- **Major investor pitches** — Demonstrating confidence and quality of final vision
- **Awards submissions** — Design competition entries requiring dramatic presentation
- **Broadcast/media** — Images intended for print media, streaming content, social media promotion
- **Mixed-use/hospitality projects** — Where atmosphere and experience are key
- **Public/community projects** — Building strong public support through compelling imagery
- **Campaign or landmark buildings** — Where establishing iconic status is goal

### Matte Painting Prompt Block

```
RENDERING STYLE: Cinematic Matte Painting

Film-quality architectural visualization with advanced environment art and cinematic composition.
Building is hero subject in carefully composed frame. Dramatic directional lighting creates strong
visual hierarchy and emotional impact. Masterfully lit with multiple light sources: primary directional
light (golden hour sun), practical lights (building interior, landscape accent lighting), and fill
light (sky and reflected light).

Lighting approach: Cinematic directional lighting emphasizing form and drama. Sun low on horizon
(golden hour, 30-degree elevation) creating long shadows and warm, saturated light. Shadows are
deep and rich, not gray. Highlights are warm gold and orange. Sky richly colored with warm and cool
tones. Building rim-lit by sun, creating separation from background. Interior lights visible glowing
through glass, suggesting occupancy and life.

Atmospheric effects: Volumetric god rays (crepuscular rays) visible from sun angle, creating dramatic
atmosphere. Slight atmospheric haze adding depth and separation between foreground and background.
Mist at ground level in shaded areas. Atmospheric perspective emphasized—background fades to soft
haze, foreground sharp and saturated.

Composition: Masterful framing with strong leading lines and visual hierarchy. Rule of thirds
composition or other advanced compositional principle evident. Foreground, middle ground, background
all clearly defined. Depth is primary compositional tool. Horizon line carefully placed for emotional
impact. Building positioned for maximum visual interest, not centered (unless intentional).

Sky and environment: Rich, dramatic sky with color and movement. Clouds lit by setting sun showing
warm and cool tones. Sky occupies significant portion of frame (30-50%). Landscape context fully
rendered—trees, shrubs, distant structures, all contributing to scene depth and mood. Weather implied
—golden hour clear sky, or dramatic storm clearing, or sunrise breaking through clouds.

Materials rendered: Photorealistic material quality emphasized and enhanced. Metal surfaces reflective
and gleaming in highlight areas. Glass glowing with interior light and reflecting warm sky. Concrete
and stone show depth and shadow. Vegetation full and lush, suggesting health and vitality. All
materials contributing to overall visual richness.

Color palette: Warm and cool carefully balanced for visual richness. Dominant warm tones (golden hour)
balanced by cool shadow tones. Saturation elevated but not unnatural—colors are vivid and appealing
without appearing over-processed. Color temperature shift from foreground (warm) to background (cooler)
enhancing depth.

Detail and resolution: 8K resolution, all detail sharp and visible. Fine details visible at all scales—
texture of materials, detail of landscape, fine architectural features. No muddy areas; entire image
crisp and detailed.

Mood: Aspirational, confident, dramatic. Building appears significant and successful. Scene suggests
positive future, vitality, accomplishment. Emotional response to image is primary goal.

Overall effect: Looks like high-end architectural visualization from major architectural publications
or film production art direction. Viewer is impressed and moved by image. Building appears successful,
impressive, and desirable.
```

### Example Output Characteristics

- **Lighting:** Dramatic directional light (golden hour or similar); strong shadows; warm highlights; rim lighting visible
- **Atmosphere:** Volumetric lighting effects (god rays); atmospheric haze; depth through atmospheric perspective
- **Composition:** Masterful framing; strong leading lines; rule of thirds or advanced composition
- **Sky:** Rich colors; dramatic clouds lit by sun; occupies 30-50% of frame
- **Materials:** Gleaming, reflective surfaces in highlights; glass glowing with interior light; rich texture throughout
- **Colors:** Warm and cool balanced; saturated and vibrant; colors shift from warm foreground to cool background
- **Mood:** Aspirational, confident, dramatic; viewer emotionally moved
- **Detail:** 8K resolution; crisp and detailed at all scales; no muddy areas

### Tips for Matte Painting Success

1. **Specify cinematic language** — "Film-quality," "cinematic composition," "hero subject"
2. **Dramatic lighting guidance** — "Golden hour lighting," "dramatic directional shadows," "god rays from sun"
3. **Composition is key** — "Masterful composition using rule of thirds," "leading lines," "strong visual hierarchy"
4. **Atmosphere matters** — "Volumetric lighting," "atmospheric haze," "atmospheric perspective," "mist"
5. **Include emotional language** — "Aspirational," "confident," "dramatic," "emotionally moving"
6. **Sky must be dramatic** — "Rich dramatic sky," "clouds lit by sun," "occupies 40-50% of frame"
7. **Materials enhanced** — "Photorealistic but enhanced," "materials gleaming in light," "deep shadow tones"
8. **Practical lighting** — "Interior lights visible glowing through glass," "accent landscape lighting"
9. **Depth emphasis** — "Foreground sharp and saturated, background soft and hazy," "strong atmospheric perspective"
10. **Reference film cinematography** — Show examples from architectural cinematography or high-end design visualization

---

## STYLE SELECTION MATRIX

Quick reference for choosing the right style for your situation:

| Project Phase | Style | Reasoning |
|---|---|---|
| **Concept/Feasibility** | Watercolor or Sketch | Artistic, suggests form, not overcommitting to details |
| **Early Design Development** | Illustration or Sketch | Clean, precise proportions, but softer than photorealistic |
| **Mid-Design Development** | Illustration | Professional quality, suitable for presentations, easily revised |
| **Schematic Design Review** | Illustration | Standard design presentation technique |
| **Design Development Complete** | Photorealistic | Accurate representation of final design |
| **Value Engineering/Cost Review** | Illustration or Diagram | Shows design without suggesting detailed finish quality |
| **Client Approval** | Photorealistic | Most convincing, most professional |
| **Marketing/Investor** | Matte Painting | Most dramatic, most compelling |
| **Public Presentation** | Photorealistic or Illustration | Professional, clear understanding building |
| **Permit Application** | Photorealistic or Illustration | Jurisdictions vary; check requirements |
| **Construction Documentation** | Diagram or Illustration | Clear, technical, shows systems/phases |
| **Awards/Competition** | Matte Painting or Photorealistic | Highest visual impact |
| **Renovation/Heritage Project** | Watercolor or Sketch | Respectful of tradition, emphasis on design thinking |
| **Community Engagement** | Watercolor or Illustration | Artistic, less technical-feeling, builds support |

---

## Cross-Style Consistency

When using multiple styles for the same building:

1. **Maintain material palette** — All styles should use identical color specifications for materials
2. **Lock building proportions** — Door sizes, window sizes, building dimensions identical in all styles
3. **Use consistent lighting direction** — If photorealistic shows morning light, don't show evening light in illustration
4. **Consistent vegetation** — Same trees/shrubs in same locations, same size/density
5. **Same site configuration** — Parking layout, pavement colors, surrounding context consistent
6. **Scale verification** — A person standing in watercolor should be proportional to vehicles in photorealistic
7. **Color matching** — If photorealistic has warm gray panels, illustration should show same warm tone (not cool gray)

This ensures different styles of the same building still appear to be the same building.

