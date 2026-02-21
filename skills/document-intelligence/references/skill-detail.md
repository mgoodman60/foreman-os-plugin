# document-intelligence — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the document-intelligence skill.



## Examples

### Example 1: Processing Plan Set

**User**: "Process this conformance plan set and extract all project intelligence"

**Your response**:
1. Read `references/extraction-rules.md` (framework)
2. Read `references/plans-deep-extraction.md` (detailed plan extraction guide)
3. Extract systematically:
   - Grid lines: 1-6, A-H
   - Complete room schedule: ALL 50+ rooms
   - Complete finish schedule: Floor/base/wall/ceiling for EVERY room
   - Complete door schedule: ALL doors with sizes, types, ratings
   - Structural specs: Concrete PSI by element, rebar grades, steel grades
   - MEP equipment: ALL HVAC units, panels, fixtures
   - Site layout: Coordinates, parking counts
   - Storm drainage: Pipe sizes, slopes, inverts
4. Cross-reference and report results

### Example 2: Processing Specifications

**User**: "Extract concrete requirements and weather thresholds from the spec book"

**Your response**:
1. Read `references/extraction-rules.md`
2. Read `references/specifications-deep-extraction.md`
3. Deep-read Division 03 Section 03 30 00:
   - Extract EXACT VALUES for each mix (PSI, w/c, slump, air content)
   - Weather thresholds: Cold <40°F (maintain 50°F for 72 hrs), Hot >90°F (ice in mix)
   - Curing: 7 days wet for slabs
   - Testing: 1 set per 50 CY, 4 cylinders
   - Tolerances: FF 35/FL 25
   - Hold points: Pre-placement, subgrade
4. Extract other weather-sensitive specs (roofing, painting)

### Example 3: Processing Schedule

**User**: "Analyze this P6 schedule for critical path and milestones"

**Your response**:
1. Read `references/extraction-rules.md`
2. Read `references/schedule-deep-extraction.md`
3. Identify critical path (float = 0):
   - Mobilization → Utilities → Footings → SOG → PEMB → Final completion
4. Extract milestones with dates and constraints
5. Identify near-critical activities (float 1-4 days)
6. Extract predecessor/successor logic
7. Flag weather-sensitive activities

---



## Best Practices

1. **Always read the base extraction rules first**: `references/extraction-rules.md`

2. **Read specialized references before extracting**: Follow the detailed guides

3. **Extract specific values, not descriptions**: "4,000 PSI" not "per spec"

4. **Extract complete schedules, not samples**: ALL rooms, ALL doors, ALL equipment

5. **Cross-reference across documents**: Link room numbers, equipment marks, spec sections

6. **Track extraction quality**: Report populated, missing, vision-needed, low-confidence

7. **Structure output for reuse**: JSON format for downstream consumption

8. **Flag conflicts**: If data conflicts across documents, alert user

9. **Verify completeness**: Extract 100% of critical items

10. **Cross-reference with MasterFormat knowledge**: After extracting spec sections, consult `references/masterformat-reference.md` to annotate extracted data with best-practice context — sequencing notes, common QC issues, hold points, testing requirements, and weather sensitivities for each CSI division. This enriches the project intelligence so downstream skills (daily-report-format, report-qa, morning-brief) can surface relevant best practices automatically.

---



## Reflected Ceiling Plan (RCP) Extraction

Reflected ceiling plans are a critical extraction target that has been missing from the standard pipeline. RCPs provide the overhead spatial model -- ceiling heights, fixture placement, HVAC diffuser locations, sprinkler coverage, and material zones -- that completes the three-dimensional picture of every room. Without RCP extraction, the spatial model is incomplete: you have floor plans (horizontal at floor level) and elevations (vertical slices), but no overhead plane data. This section closes that gap.

### Why RCP Extraction Matters for Field Operations

1. **MEP Coordination**: Light fixtures, HVAC diffusers, sprinkler heads, and speakers all compete for ceiling space. Extracted RCP data enables clash detection before installation begins.
2. **Ceiling Material Procurement**: ACT tile types, GWB areas, specialty ceilings, and exposed structure zones must be quantified for accurate material orders.
3. **Finish Tracking**: Room-by-room ceiling completion tracking requires knowing what ceiling type goes where.
4. **Inspection Readiness**: Above-ceiling rough-in must be complete before ceiling grid installation -- RCP data identifies which rooms need which above-ceiling trades.
5. **Height Transitions**: Soffits, bulkheads, and ceiling height changes create coordination challenges at transitions that must be identified early.

### RCP Sheet Identification

RCP sheets follow predictable naming conventions:
- **Sheet prefix**: RCP, A-5xx series (A-501, A-502, etc.), or A-1xx-RCP suffix
- **Title block keywords**: "Reflected Ceiling Plan", "RCP", "Ceiling Plan"
- **Scale**: Typically 1/8" = 1'-0" (matching floor plan scale)
- **Floor designation**: "Level 1 RCP", "Second Floor Reflected Ceiling Plan"

**Classification signals**:
- Dashed grid lines overlaid with ceiling fixture symbols
- Light fixture symbols (rectangles for troffers, circles for downlights)
- Room labels with ceiling height callouts (e.g., "9'-0" AFF" or "CLG @ 10'-0"")
- Ceiling material boundary lines with material tags

### Extraction Targets

#### Ceiling Heights by Room
For EVERY room shown on the RCP:
- **Room number**: Cross-reference to floor plan room number
- **Ceiling height**: Height above finished floor (AFF) in feet-inches
- **Height source**: Noted on RCP vs. inferred from finish schedule vs. standard height
- **Multiple heights**: If a room has stepped or sloped ceilings, extract all heights and transition locations

**Output format**:
```json
{
  "rcp_ceiling_heights": [
    {"room": "101", "name": "Office", "ceiling_height": "9'-0\" AFF", "ceiling_type": "ACT", "notes": "Standard height"},
    {"room": "102", "name": "Conference", "ceiling_height": "10'-0\" AFF", "ceiling_type": "GWB", "notes": "Raised ceiling at projector area"},
    {"room": "103", "name": "Corridor", "ceiling_height": "8'-6\" AFF", "ceiling_type": "ACT", "notes": "Soffit at 7'-6\" over door frames"},
    {"room": "104", "name": "Lobby", "ceiling_height": "12'-0\" AFF", "ceiling_type": "Exposed structure", "notes": "Painted exposed deck, utilities visible"}
  ]
}
```

#### Light Fixture Locations, Types, and Quantities
For each room, extract every light fixture shown:
- **Fixture type mark**: Cross-reference to lighting fixture schedule (Type A, Type B, etc.)
- **Fixture description**: 2x4 troffer, 2x2 troffer, downlight, linear strip, pendant, wall sconce, exit sign, emergency light
- **Quantity per room**: Count of each fixture type in the room
- **Grid reference**: Location by ceiling grid intersection or room zone (e.g., "centered in room", "over work surface", "along corridor centerline")
- **Switching/circuit**: If noted on RCP (e.g., "circuit L1-3", "switch S1")
- **Special fixtures**: Exit signs with emergency battery, emergency egress lighting, night lights

**Output format**:
```json
{
  "rcp_lighting": [
    {
      "room": "101",
      "fixtures": [
        {"type": "A", "description": "2x4 LED troffer", "qty": 4, "placement": "2x2 grid centered in room", "switching": "Switch by door"},
        {"type": "EX", "description": "Exit sign with emergency", "qty": 1, "placement": "Above door 101", "switching": "Emergency circuit"}
      ]
    }
  ]
}
```

#### HVAC Diffuser and Return Locations
For each room, extract all HVAC ceiling devices:
- **Supply diffusers**: Type (square, round, linear slot, perforated face), size (e.g., "24x24", "12\" round", "4' linear slot"), quantity per room
- **Return air grilles**: Type (egg crate, perforated, linear bar), size, quantity per room
- **Exhaust grilles**: Typically in restrooms, kitchens, janitor closets -- note CFM if shown
- **Grid reference**: Position relative to room layout or ceiling grid

**Output format**:
```json
{
  "rcp_hvac_devices": [
    {
      "room": "105",
      "supply_diffusers": [
        {"type": "Square ceiling diffuser", "size": "24x24", "qty": 2, "location": "Centered north and south halves"}
      ],
      "return_grilles": [
        {"type": "Egg crate return", "size": "24x24", "qty": 1, "location": "Adjacent to corridor wall"}
      ],
      "exhaust": null
    },
    {
      "room": "106",
      "supply_diffusers": [
        {"type": "Linear slot diffuser", "size": "4' length", "qty": 1, "location": "Along window wall"}
      ],
      "return_grilles": [],
      "exhaust": [
        {"type": "Exhaust grille", "size": "12x12", "qty": 1, "cfm": "75 CFM", "location": "Centered in ceiling"}
      ]
    }
  ]
}
```

#### Sprinkler Head Locations and Coverage
For each room or zone:
- **Sprinkler head type**: Pendant, concealed, sidewall, upright
- **Coverage pattern**: Standard spacing (typically 12'-15' max per NFPA 13), extended coverage
- **Quantity per room**: Count of heads visible on RCP
- **Escutcheon type**: Flush, recessed, semi-recessed (affects ceiling finish coordination)
- **Notes**: "Sprinkler heads shown for reference only -- see FP drawings for exact layout"

#### Ceiling Material Zones
Extract material boundaries from the RCP:
- **ACT (Acoustical Ceiling Tile)**: Type 1 (standard offices), Type 2 (moisture-resistant for restrooms), wet-area ACT
- **GWB (Gypsum Wallboard)**: Locations, finish level, paint specification
- **Exposed structure**: Painted exposed deck, exposed bar joists, exposed ductwork zones
- **Specialty ceilings**: Wood slat, metal panel, acoustic cloud/raft, stretched fabric, linear metal
- **Boundary lines**: Where ceiling materials transition (note grid line references for boundaries)

**Output format**:
```json
{
  "rcp_ceiling_materials": [
    {"zone": "Offices (101-110)", "material": "ACT Type 1", "product": "Armstrong Sahara 2x2", "grid": "White 15/16\" exposed", "area_sf": 2400},
    {"zone": "Restrooms (111-114)", "material": "ACT Type 2", "product": "Armstrong Ceramaguard", "grid": "White 15/16\" exposed", "area_sf": 600},
    {"zone": "Lobby (120)", "material": "GWB", "finish": "Level 5, paint SW 7050", "height": "12'-0\"", "area_sf": 450},
    {"zone": "Break Room (115)", "material": "Exposed structure", "finish": "Painted black, exposed ductwork", "height": "Varies 11'-14'", "area_sf": 350}
  ]
}
```

#### Ceiling Height Transitions and Soffits
Extract transition geometry:
- **Soffit locations**: Grid line references, dimensions (width x depth x length)
- **Bulkhead locations**: Typically at corridor-to-room transitions or to conceal ductwork
- **Ceiling height changes**: Where ceiling steps up or down, with dimensions at both levels
- **Cove/valance details**: Indirect lighting coves, window valances at ceiling level
- **Cloud/raft elements**: Suspended acoustic panels or clouds with dimensions and heights

#### Access Panel Locations
Extract maintenance access points:
- **Access panel locations**: Grid reference, size (e.g., "24x24 access panel")
- **Purpose**: HVAC valve access, plumbing shutoff, electrical junction, fire damper access
- **Frequency**: Note if access panels are required at every fire damper, every VAV box, etc.

### RCP-to-Floor-Plan Cross-Reference

**Critical rule**: Every room on the RCP MUST match a room on the floor plan. After extraction:
1. Compare RCP room list to floor plan room schedule -- flag any discrepancies
2. Verify ceiling heights on RCP match finish schedule ceiling entries
3. Cross-reference RCP grid lines to structural grid -- they must align
4. Link RCP fixture counts to lighting fixture schedule totals for validation
5. Verify sprinkler coverage against fire protection drawings (FP sheets)

### Integration with Downstream Systems

**Daily Reports**: "Installed ACT grid in Rooms 101-105 (Type 1, Armstrong Sahara 2x2). 4 rooms complete, 10 remaining."

**Morning Briefs**: "Today's ceiling work: Grid installation Rooms 106-108. Verify above-ceiling rough-in complete before grid."

**Procurement**: "RCP extraction shows 3,200 SF ACT Type 1 + 600 SF ACT Type 2 + 450 SF GWB ceiling. Order tile quantities with 10% waste."

**MEP Coordination**: "Room 115 has 2 supply diffusers, 1 return grille, 3 light fixtures, and 2 sprinkler heads in a 350 SF ceiling. Verify clearances before grid."

---



## Specification Conflict Detection

Construction documents are produced by multiple design firms across months or years. Conflicts between specifications and plan notes are inevitable. This section establishes a systematic process for detecting, classifying, and resolving specification conflicts during document extraction.

### Why Specification Conflict Detection Matters

1. **RFI Prevention**: Detecting conflicts during extraction means the superintendent can issue RFIs before work starts, not after rework is needed.
2. **Safety**: Structural and fire-rating conflicts are safety-critical -- using the wrong concrete strength or missing a fire-rated assembly can have catastrophic consequences.
3. **Cost Control**: Catching a "4,000 PSI vs. 3,500 PSI" conflict before the concrete pour avoids change orders, testing disputes, and potential demolition.
4. **Schedule Protection**: Unresolved conflicts cause field stoppages. Early detection keeps work moving.
5. **Liability Documentation**: A documented conflict report creates a paper trail showing the GC identified the issue and sought clarification.

### Conflict Detection Methodology

#### Step 1: Extract Values with Source Attribution
Every extracted numerical value must carry its source:
```json
{
  "parameter": "concrete_strength_footings",
  "value": "4,000 PSI",
  "source": "Spec Section 03 30 00, page 3, paragraph 2.1.A",
  "source_type": "specification"
}
```

Compare the same parameter extracted from different sources:
```json
{
  "parameter": "concrete_strength_footings",
  "value": "3,500 PSI",
  "source": "Sheet S-001, Structural General Notes, item 4",
  "source_type": "plan_note"
}
```

#### Step 2: Automated Cross-Reference
After extraction, compare values across these source pairs:
- **Spec section vs. plan general notes**: Most common conflict source (e.g., Division 03 spec says 4,000 PSI but structural general notes say 3,500 PSI)
- **Spec division vs. spec division**: Cross-division conflicts (e.g., Division 03 concrete strength vs. Division 31 foundation requirements referencing different concrete strengths)
- **Plan sheet vs. plan sheet**: Architectural dimension vs. structural dimension for the same element
- **Spec vs. schedule**: Specification material requirements vs. what is shown in the project schedule activity descriptions
- **Spec vs. submittal**: Specified product requirements vs. submitted product data sheets

#### Step 3: Flag and Classify Conflicts
When values disagree, classify the conflict:

### Conflict Severity Levels

**CRITICAL (Safety/Structural)** -- Requires immediate resolution before work proceeds:
- Concrete design strength disagreements (affects structural capacity)
- Rebar grade or size conflicts (affects load-carrying capacity)
- Fire rating discrepancies (life safety)
- Structural steel grade conflicts
- Anchor bolt size/embedment disagreements
- Foundation bearing capacity vs. design load conflicts
- Seismic detailing discrepancies

**MAJOR (Performance)** -- Requires resolution before procurement or installation:
- Insulation R-value conflicts (energy code compliance)
- Waterproofing membrane thickness disagreements
- HVAC equipment capacity conflicts (affects occupant comfort and code compliance)
- Window U-value/SHGC specification vs. schedule conflicts
- Electrical panel sizing conflicts
- Pipe material or size disagreements between plumbing and mechanical drawings
- Finish material conflicts that affect durability or maintenance requirements

**MINOR (Aesthetic/Cosmetic)** -- Resolve before installation, but do not delay preceding work:
- Paint color code disagreements between spec and finish schedule
- Ceiling tile product specification vs. finish schedule product
- Hardware finish disagreements (spec says 626, hardware schedule says 625)
- Grout color conflicts between spec and tile layout drawing
- Trim profile or color discrepancies
- Casework hardware style conflicts

### Common Conflict Patterns by Discipline Pair

**Architectural vs. Structural**:
- Slab thickness: architectural floor plan note vs. structural section detail
- Opening sizes: architectural elevation vs. structural framing plan
- Floor elevation: architectural FFE vs. structural top-of-slab elevation
- Wall thickness: architectural plan dimension vs. structural detail dimension

**Architectural vs. MEP**:
- Ceiling height: architectural RCP height vs. mechanical ductwork clearance requirements
- Wall chase dimensions: architectural plan vs. plumbing riser space needed
- Floor penetration locations: architectural floor plan vs. plumbing/mechanical riser locations
- Electrical panel locations: architectural room layout vs. electrical plan panel placement

**Specification vs. Plan Notes**:
- Material strengths: spec paragraph vs. general note on drawing
- Testing frequencies: spec requirement vs. note on drawing that states different frequency
- Weather thresholds: spec weather limitation vs. general conditions note on plans
- Curing requirements: spec curing duration vs. structural note curing duration

**Specification vs. Specification (Cross-Division)**:
- Division 03 (Concrete) vs. Division 31 (Earthwork): Foundation concrete strength
- Division 07 (Roofing) vs. Division 22 (Plumbing): Roof penetration flashing requirements
- Division 08 (Openings) vs. Division 09 (Finishes): Door/frame paint specifications
- Division 09 (Finishes) vs. Division 12 (Furnishings): Casework finish specifications
- Division 23 (HVAC) vs. Division 26 (Electrical): Equipment electrical requirements

### Conflict Report Output

When conflicts are detected, generate a structured conflict report:

```json
{
  "specification_conflicts": [
    {
      "conflict_id": "CONF-001",
      "parameter": "Footing concrete design strength",
      "value_a": {"value": "4,000 PSI", "source": "Spec 03 30 00, para 2.1.A", "source_type": "specification"},
      "value_b": {"value": "3,500 PSI", "source": "Sheet S-001, General Note 4", "source_type": "plan_note"},
      "severity": "CRITICAL",
      "category": "structural_capacity",
      "recommended_action": "Issue RFI to structural engineer of record. Do not proceed with footing concrete placement until resolved. Use the more conservative (higher) value for mix design submittal pending resolution.",
      "rfi_draft": "Structural general notes on S-001 indicate 3,500 PSI concrete for footings. Specification Section 03 30 00, paragraph 2.1.A requires 4,000 PSI. Please clarify required design strength for footing concrete.",
      "affected_activities": ["Footing concrete placement", "Concrete mix design submittal"],
      "detected_date": "2026-02-19"
    },
    {
      "conflict_id": "CONF-002",
      "parameter": "Corridor wall paint sheen",
      "value_a": {"value": "Semi-gloss", "source": "Spec 09 91 00, para 3.2.B", "source_type": "specification"},
      "value_b": {"value": "Eggshell", "source": "Finish Schedule on A-601", "source_type": "plan_schedule"},
      "severity": "MINOR",
      "category": "aesthetic",
      "recommended_action": "Clarify with architect at next OAC meeting. Semi-gloss is typical for high-traffic corridors. Procure semi-gloss pending clarification.",
      "rfi_draft": null,
      "affected_activities": ["Corridor painting"],
      "detected_date": "2026-02-19"
    }
  ]
}
```

### Spec-to-Submittal Validation

When submittal data has been extracted (via the submittals-deep-extraction pipeline), automatically compare submitted product data against specification requirements:

**Comparison framework**:
1. Extract spec requirement: "Concrete mix design: 4,000 PSI at 28 days, w/c 0.45 max, slump 4+/-1, air 5.5%+/-1.5%"
2. Extract submittal data: "Proposed mix: 4,200 PSI at 28 days, w/c 0.42, slump 4, air 5.0%"
3. Compare each parameter:
   - Strength: 4,200 >= 4,000 -- PASS (exceeds minimum)
   - W/C ratio: 0.42 <= 0.45 -- PASS (below maximum)
   - Slump: 4.0 within 4+/-1 range -- PASS
   - Air content: 5.0% within 5.5%+/-1.5% range (4.0%-7.0%) -- PASS
4. Overall result: COMPLIANT

**Non-compliant example**:
- Spec requires "R-25 wall insulation"
- Submittal shows "R-21 batt insulation"
- Result: FAIL -- submitted product does not meet minimum R-value
- Action: Reject submittal, request resubmission with compliant product

**"Or Equal" handling**:
- If spec says "Armstrong Sahara or approved equal" and submittal proposes USG Radar
- Compare: NRC rating, fire rating, edge detail, size compatibility, moisture resistance
- Flag for architect review with comparison table

### Resolution Workflow

```
Conflict Detected
       |
       v
Classify Severity (CRITICAL / MAJOR / MINOR)
       |
       +-- CRITICAL --> Stop affected work --> Issue RFI immediately
       |                                        --> Use conservative value pending response
       |                                        --> Notify project manager and owner
       |
       +-- MAJOR ----> Flag for next OAC meeting --> Issue RFI within 48 hours
       |                                           --> Procure to more restrictive value
       |
       +-- MINOR ----> Log in conflict register --> Clarify at next coordination meeting
                                                 --> Proceed with spec value (spec governs)
```

**Resolution priority rules**:
1. Specification governs over plan notes (unless plan note is more restrictive)
2. Most restrictive value controls when safety is involved
3. More recent document revision takes precedence (check revision dates)
4. Addenda and ASIs supersede original contract documents
5. When in doubt, issue an RFI -- do not assume or interpret

---



## Quantity Validation Workflow

The document intelligence pipeline extracts quantities from multiple sources: DXF/DWG spatial data, visual analysis of plan sheets, text-parsed schedules, and manual takeoff entries. When these sources produce different quantities for the same item, the current system flags a >10% discrepancy but provides no structured resolution process. This section establishes that resolution workflow.

### The Multi-Source Quantity Problem

Consider extracting "number of 2x4 LED troffers" for a project:
- **DXF extraction**: 247 fixtures (from block counts in the DXF lighting layer)
- **Visual analysis**: 239 fixtures (from symbol recognition on RCP sheet images)
- **Text-parsed schedule**: 244 fixtures (from the lighting fixture schedule table)
- **Manual takeoff**: 252 fixtures (superintendent counted from prints)

These four numbers are close but not identical. Which one drives the material order? What if the discrepancy is 30% instead of 3%? The validation workflow answers these questions.

### Source Priority Rules

When multi-source quantities disagree, trust sources in this order:

1. **DXF/DWG Data (Highest Priority)**: CAD files contain exact block counts and polyline areas. A block named "2x4_troffer" counted across all relevant layers gives the most precise fixture count. Hatch areas in DXF give exact square footages for flooring, concrete, roofing.

2. **Manual Takeoff (Field-Verified)**: A superintendent counting from current-revision prints catches things CAD misses (added fixtures in ASIs, hand-drawn additions on field markups). Especially trusted when the person doing the takeoff is experienced with the trade.

3. **Visual Analysis (Image-Based)**: The visual_plan_analyzer.py pipeline uses symbol recognition and OCR. Accuracy is high for distinct symbols (doors, outlets) but lower for items that look similar (different diffuser types). Good for validation but subject to OCR errors and resolution limitations.

4. **Text-Parsed (Schedule Tables)**: Quantities parsed from schedule tables (e.g., "Qty: 244" in a fixture schedule) are reliable when the table is complete and correctly parsed. However, tables may be truncated, split across pages, or have formatting that causes parse errors.

### Discrepancy Thresholds

| Discrepancy Range | Classification | Action |
|-------------------|---------------|--------|
| 0-5% | **Normal variance** | Use highest-priority source. Log variance for record. |
| 5-10% | **Review recommended** | Compare sources, identify likely cause. Use highest-priority source unless cause identified. |
| 10-25% | **Investigation required** | Stop and investigate before ordering. Likely cause: missed sheet, revision difference, scope boundary mismatch. |
| >25% | **Critical discrepancy** | Do not proceed. Likely cause: wrong document, scope error, major extraction failure. Re-extract from source documents. |

### Structured Resolution Process

When a discrepancy exceeds 10%:

#### Step 1: Present the Discrepancy
```
QUANTITY DISCREPANCY DETECTED
Item: 2x4 LED Troffer (Type A)
  DXF extraction:      247 fixtures  (Source: electrical.dxf, layer E-LITE-FIX)
  Visual analysis:     189 fixtures  (Source: E-101 through E-104 PNG analysis)
  Text-parsed schedule: 244 fixtures (Source: E-001 Fixture Schedule)
  Manual takeoff:      Not available

  Maximum variance: 30.7% (DXF vs. Visual)
  Classification: CRITICAL DISCREPANCY
```

#### Step 2: Identify Likely Cause
Common causes of quantity discrepancies:

- **Missing sheets**: Visual analysis may have only processed sheets E-101 to E-103, missing E-104. Check sheet coverage.
- **Revision mismatch**: DXF may be Rev 3 while PDFs used for visual analysis are Rev 2. Check document dates.
- **Scope boundary**: DXF includes site lighting, but visual analysis only captured interior RCP sheets.
- **Symbol confusion**: Visual analysis may have confused 2x4 troffers with 2x4 return air grilles (similar rectangular shapes).
- **Layer filtering**: DXF extraction may include fixtures on a "DEMO" or "FUTURE" layer that should be excluded.
- **Schedule incompleteness**: Text-parsed fixture schedule may list types and quantities but omit fixtures added by addendum.
- **Duplicate counting**: DXF blocks nested inside other blocks may cause double-counting.

#### Step 3: Recommend Action

Based on the identified cause:
- **Issue RFI**: If the discrepancy cannot be resolved from available documents
- **Re-extract**: If a source was processed incompletely (missing sheets, wrong revision)
- **Field verify**: If documents are ambiguous, send someone to physically count in the field (for existing conditions or partially installed work)
- **Use conservative value**: For material ordering, use the higher quantity plus waste factor until resolved
- **Reconcile scope**: If the issue is scope boundary (e.g., interior vs. interior+exterior), align all sources to the same scope definition

### Quality Gates

Material procurement should not proceed past these gates without validation:

**Gate 1 -- Extraction Complete**:
- All relevant sheets processed (check sheet index against processed sheets)
- All relevant spec sections extracted
- DXF processed (if available)
- Visual analysis run on all plan sheets

**Gate 2 -- Cross-Source Validation**:
- Quantities compared across all available sources
- Discrepancies >10% investigated and resolved or documented
- Source priority applied for final quantities

**Gate 3 -- Field Measurement Confirmation**:
- For high-value items (structural steel, mechanical equipment, electrical switchgear): field verify before ordering
- For bulk materials (concrete, masonry, drywall): extracted quantities acceptable with waste factor
- For finish materials (flooring, ceiling tile, paint): visual analysis validated against DXF or field measurement

**Gate 4 -- Procurement Release**:
- Final quantities confirmed through quality gates
- Waste factors applied (typically: 5% mechanical/electrical, 10% drywall/framing, 10-15% tile/flooring, 5% concrete CY)
- Lead times checked against schedule requirements
- Budget confirmation (quantities x unit cost within budget line)

### Validation Checkpoints by Project Phase

**Pre-Construction / Buyout Phase**:
- Extract all quantities from bid documents
- Flag incomplete data: "Window schedule has 12 types but only 10 have sizes specified"
- Preliminary material budgets based on extracted quantities
- Long-lead item identification from extracted schedules + lead time data

**Foundation / Substructure Phase**:
- Concrete CY validated: DXF footing volumes vs. structural schedule vs. hand calculation
- Rebar tonnage: DXF bar counts vs. structural details vs. rebar shop drawing takeoff
- Earthwork CY: DXF grading surfaces vs. civil quantity table vs. geotech boring volumes
- Gate: Do not order rebar or concrete until DXF or field-verified quantities confirm plan data

**Superstructure / Shell Phase**:
- Structural steel tonnage: DXF member counts vs. structural schedule vs. fabricator shop drawing
- Metal deck area: DXF boundary polylines vs. plan SF calculation
- Exterior cladding SF: DXF elevation areas vs. manual takeoff from elevation sheets
- Gate: Confirm steel tonnage with fabricator before erection sequence approval

**Interior Finish Phase**:
- Drywall SF by type: DXF wall polylines vs. visual wall detection vs. manual takeoff
- Flooring SF by material: DXF hatch areas vs. room schedule areas vs. visual material zone detection
- Ceiling SF by type: RCP extraction areas vs. room schedule areas
- Door/window counts: DXF block counts vs. schedule table counts vs. visual symbol counts
- Gate: Do not release finish material orders until at least two sources agree within 10%

**MEP Rough-In Phase**:
- Fixture counts: DXF blocks vs. schedule tables vs. visual symbol counts
- Panel counts and sizes: DXF vs. electrical schedule
- HVAC equipment: DXF vs. mechanical schedule vs. submittal data
- Pipe runs: DXF lengths vs. isometric drawing quantities

### Material Procurement Workflow

The validated quantity feeds directly into procurement:

```
Extracted Quantity (from highest-priority validated source)
        |
        v
Apply Waste Factor (trade-specific: 5-15%)
        |
        v
Generate Order Quantity
        |
        v
Cross-Reference to Submittal Status (approved product? approved equal?)
        |
        v
Check Lead Time vs. Schedule Need Date
        |
        v
Generate Purchase Requisition with:
  - Item description (from spec extraction)
  - Quantity (validated + waste)
  - Required delivery date (from schedule extraction - lead time)
  - Approved product (from submittal extraction)
  - Spec section reference (from spec extraction)
  - Budget line reference (from contract extraction)
        |
        v
Track: Ordered Qty vs. Delivered Qty vs. Installed Qty vs. Extracted Qty
```

### Output Format

```json
{
  "quantity_validations": [
    {
      "item": "2x4 LED Troffer (Type A)",
      "csi_division": "26",
      "validated_qty": 247,
      "unit": "EA",
      "primary_source": "DXF",
      "source_comparison": {
        "dxf": {"qty": 247, "source_file": "electrical.dxf", "layer": "E-LITE-FIX", "confidence": "high"},
        "visual": {"qty": 239, "source_sheets": ["E-101", "E-102", "E-103", "E-104"], "confidence": "medium"},
        "text_parsed": {"qty": 244, "source_sheet": "E-001", "confidence": "high"},
        "manual_takeoff": null
      },
      "max_variance_pct": 3.3,
      "status": "validated",
      "waste_factor": 0.05,
      "order_qty": 260,
      "procurement_status": "pending_submittal_approval"
    }
  ]
}
```

---



## Schedule-to-Field Automation

The CPM schedule contains a wealth of data that, when combined with extracted document intelligence, can drive automated field operations. This section defines the automation rules that connect schedule data to daily field management.

### Today's Work Generation

Every morning, the superintendent needs a clear answer to: "What work is scheduled for today?" This automation extracts the answer directly from CPM data.

#### Auto-Generation Process

1. **Query schedule data** for activities where today's date falls within the activity's start-to-finish range
2. **Filter by status**: Include only activities with status "In Progress" or "Should Start Today" (planned start = today)
3. **Enrich with extracted data**:
   - Activity "Install ACT ceiling Rooms 101-110" --> pull room details from room_schedule, ceiling type from RCP extraction, material from spec extraction
   - Activity "Pour footings Grid C-D/3-4" --> pull concrete mix from spec extraction, rebar from structural notes, weather thresholds from weather_thresholds
4. **Sort by trade/area** for logical crew assignment
5. **Flag critical path activities** with zero float marker

**Output for morning briefing**:
```
TODAY'S SCHEDULED WORK - Wednesday, February 19, 2026

CRITICAL PATH:
  [!] Pour concrete footings Grid C-D/3-4 (Day 3 of 5)
      Mix: 3,000 PSI per Spec 03 30 00
      Weather check: Current 45F > 40F minimum -- OK to pour
      Testing: 1 set per 50 CY -- testing lab notified
      Hold point: Rebar/formwork inspection REQUIRED before pour

ACTIVE WORK:
  Mechanical rough-in Rooms 201-208 (Day 2 of 4)
      Trade: ABC Mechanical
      Above-ceiling work -- coordinate with electrical before ceiling grid
  Drywall framing Rooms 105-110 (Day 1 of 3)
      Trade: XYZ Drywall
      Wall types: See structural details S-301 for rated assemblies
  Site grading -- parking lot north (Day 4 of 6)
      Trade: Site Solutions Inc.
      Compaction: 95% Standard Proctor per Spec 31 23 00
      Weather: Rain forecast Thursday -- consider accelerating

SHOULD START TODAY:
  Electrical panel installation Room 112 (Duration: 2 days)
      Panel LP-1: 120/208V, 225A main
      Pre-install meeting required per Spec 26 24 00

LOOK-AHEAD (Next 3 days):
  Thursday: Roofing membrane Section A (weather dependent -- check wind)
  Friday: ACT grid installation Rooms 101-105
  Monday: Fire protection rough-in Rooms 201-208
```

### Weather Threshold Alerts

Combine daily weather data with extracted weather thresholds from specifications:

#### Monitored Thresholds

**Concrete Operations**:
- Minimum ambient temperature: Extracted from Spec 03 30 00 (typically 40F)
- Maximum ambient temperature: Extracted from Spec 03 30 00 (typically 90F)
- Minimum concrete temperature at placement: (typically 50F)
- Maximum concrete temperature at placement: (typically 90F)
- Wind speed for exposed slabs: (typically 15 mph for evaporation rate concerns)
- Rain forecast: Any precipitation within curing window (typically 24 hours after placement)

**Roofing Operations**:
- Wind speed maximum: Extracted from Spec 07 50 00 (typically 15-25 mph depending on system)
- Minimum temperature for adhesive application: (typically 40F for most systems)
- Moisture: No roofing on wet substrates
- Rain forecast: Cannot apply roofing membrane in rain or when rain expected within application window

**Earthwork / Excavation**:
- Frost depth: Cannot compact frozen soil
- Rain saturation: Optimum moisture content for compaction (typically OMC +/- 2%)
- Standing water: Cannot place fill in standing water
- Temperature for asphalt paving: Minimum ambient typically 40-50F, minimum surface typically 40F

**Painting (Exterior)**:
- Minimum temperature: Extracted from Spec 09 91 00 (typically 50F and rising)
- Maximum humidity: (typically 85% RH)
- Rain forecast: Surface must be dry, no rain within drying window (typically 4-8 hours)
- Wind speed: Spray application wind limits (typically 10-15 mph)

**Waterproofing / Sealants**:
- Minimum temperature: Extracted from Spec 07 90 00 (typically 40F)
- Moisture: Substrates must be dry
- Rain forecast: No application when rain expected within cure window

**Masonry**:
- Cold weather: Below 40F -- heat mortar water, protect work
- Hot weather: Above 90-100F -- shade materials, fog mist CMU
- Wind: May affect mortar joint quality, no specific threshold but flag high wind days
- Rain: Cannot lay masonry in rain

#### Alert Generation

Each morning, check the daily weather forecast against all applicable thresholds for today's scheduled activities:

```
WEATHER ALERT - February 19, 2026
Forecast: High 38F, Low 25F, Wind 12 mph NW, 40% chance rain after 2 PM

[STOP] CONCRETE POUR (Grid C-D/3-4):
  Temperature will be BELOW 40F minimum at start of day.
  Spec 03 30 00 requires: Ambient >40F, concrete temp >50F at placement.
  REQUIRED: Cold weather protection plan -- insulated blankets, heated enclosure,
  or POSTPONE pour until temperature rises above threshold.
  Decision needed by 6:00 AM for batch plant and pump coordination.

[CAUTION] EXTERIOR PAINTING (South elevation):
  Temperature at 38F is BELOW 50F minimum for latex application.
  Spec 09 91 00 requires: 50F and rising.
  RECOMMEND: Postpone exterior painting. Interior painting can proceed.

[OK] DRYWALL FRAMING (Interior):
  No weather-sensitive thresholds for interior framing. Proceed as scheduled.

[OK] MECHANICAL ROUGH-IN (Interior):
  No weather-sensitive thresholds. Proceed as scheduled.

[WATCH] SITE GRADING (Parking lot):
  Rain forecast at 40% after 2 PM. If rain materializes, soil moisture
  will exceed optimum range for compaction.
  RECOMMEND: Compact early in day. Have roller and proof-roll ready by noon.
  Spec 31 23 00 requires 95% Standard Proctor at OMC +/- 2%.
```

### Inspection Trigger Automation

Schedule activities automatically trigger inspection and testing notifications:

#### Trigger Rules

**Concrete placement triggers**:
- 48 hours before: Notify testing laboratory (required by most specs)
- 24 hours before: Rebar/formwork inspection request to building official / special inspector
- Day of pour: Confirm testing lab technician will be on site
- 7 days after: Schedule 7-day cylinder breaks (if specified)
- 28 days after: Schedule 28-day cylinder breaks (required)

**Structural steel erection triggers**:
- Before erection begins: Special inspection notification for bolted and welded connections
- During erection: Weld inspection scheduling (daily if continuous welding)
- Connection completion: Torque verification inspection for slip-critical bolts
- After erection: As-built survey for plumb and alignment verification

**Underground utility triggers**:
- Before backfill: Utility inspection (building official or utility company)
- Before concrete encasement: Pipe pressure test verification
- After backfill: Compaction testing over utility trenches

**Fire protection triggers**:
- Rough-in complete: Above-ceiling inspection before ceiling closure
- System charged: Hydrostatic test scheduling
- Final: Fire marshal inspection before occupancy

**Insulation / Vapor Barrier triggers**:
- Before drywall: Insulation inspection (energy code compliance)
- Before concrete slab: Vapor barrier inspection

**Roofing triggers**:
- Deck complete: Roof deck inspection before membrane
- Membrane applied: Flood test or electronic leak detection scheduling
- Warranty: Manufacturer's rep final inspection

#### Output Format

```json
{
  "inspection_triggers": [
    {
      "trigger_activity": "Pour concrete footings Grid C-D/3-4",
      "trigger_date": "2026-02-19",
      "inspections_required": [
        {
          "type": "Pre-placement rebar/formwork inspection",
          "required_by": "Spec 03 30 00, Building Code",
          "notify": "Building Official, Special Inspector",
          "timing": "Must pass BEFORE concrete placement",
          "hold_point": true,
          "notification_sent": false
        },
        {
          "type": "Concrete testing -- field cylinders",
          "required_by": "Spec 03 30 00 -- 1 set per 50 CY",
          "notify": "ABC Testing Lab",
          "timing": "Technician on site during placement",
          "hold_point": false,
          "notification_sent": true,
          "notification_date": "2026-02-17"
        }
      ]
    }
  ]
}
```

### Look-Ahead Constraint Identification

Extract constraints from schedule data that affect upcoming work (typically 2-week and 6-week look-ahead windows):

**Constraint types to identify**:
- **Predecessor dependencies**: "Cannot start X until Y is complete" -- flag if Y is behind schedule
- **Resource constraints**: Two activities need the same crane, same area, same trade -- flag scheduling conflicts
- **Submittal constraints**: Activity requires approved submittal -- flag if submittal is still under review
- **Long-lead material constraints**: Activity requires material with lead time -- flag if material not yet ordered or not yet delivered
- **Permit/inspection constraints**: Activity requires permit approval or passed inspection -- flag if pending
- **Weather constraints**: Activity is weather-sensitive -- flag if scheduled during historically bad weather period
- **Access constraints**: Activity requires area access that may be blocked by other work

**Output format**:
```
2-WEEK LOOK-AHEAD CONSTRAINTS (Feb 19 - Mar 5, 2026)

[CRITICAL] Roofing membrane Section A (Feb 24)
  Constraint: Submittal for TPO membrane still under review (submitted Jan 28)
  Risk: 27 days in review vs. 14-day spec requirement. May delay start.
  Action: Escalate submittal review with architect. Request expedited response.

[WARNING] ACT ceiling installation Rooms 101-105 (Feb 21)
  Constraint: Above-ceiling mechanical rough-in must be complete first
  Status: Mechanical rough-in at 60% complete (2 of 4 scheduled days remaining)
  Risk: If mechanical slips 1 day, ceiling start delays 1 day (zero float)
  Action: Coordinate with ABC Mechanical for overtime to maintain schedule.

[WATCH] Electrical switchgear installation (Mar 3)
  Constraint: Switchgear has 12-week lead time, ordered Dec 8
  Status: Manufacturer confirms ship date Feb 28, delivery Mar 2
  Risk: 1-day buffer before scheduled install. Confirm delivery tracking.
  Action: Call manufacturer for updated ship tracking. Confirm delivery logistics.

[INFO] Parking lot paving (Mar 5)
  Constraint: Weather-sensitive activity. Historical March temps may be marginal.
  Status: 10-day forecast shows temps above 45F. Appears feasible.
  Action: Monitor forecast daily starting Mar 1. Have backup date identified.
```

### Milestone Proximity Alerts

When the schedule shows a milestone approaching, generate a pre-work checklist from extracted document data:

**Milestone: Substantial Completion (60 days out)**:
```
MILESTONE ALERT: Substantial Completion in 60 days (April 20, 2026)

PRE-MILESTONE CHECKLIST (auto-generated from extracted requirements):
[ ] All punch list items from Owner walkthrough resolved
[ ] All building inspections passed (fire, electrical, plumbing, elevator, ADA)
[ ] Fire alarm system tested and commissioned
[ ] HVAC system balanced and commissioned
[ ] Elevator inspection certificate received
[ ] Fire marshal approval obtained
[ ] Certificate of Occupancy application submitted
[ ] Owner training sessions scheduled (Spec 01 77 00: 4 hours HVAC, 2 hours fire alarm)
[ ] O&M manuals compiled and delivered (Spec 01 78 00)
[ ] As-built drawings submitted
[ ] Warranty letters from all subcontractors collected
[ ] Final cleaning complete (Spec 01 74 00)
[ ] Site restoration and landscaping final inspection

SCHEDULE STATUS:
  Critical path float: 8 days (as of today)
  At-risk activities: Elevator final inspection (waiting on state inspector scheduling)
  Behind schedule: Landscape irrigation (3 days behind -- weather delays)
```

### Trade Coordination Alerts

When the schedule shows two or more trades working in the same area on the same day, automatically generate a coordination alert:

**Detection logic**:
1. Parse schedule activities for location information (room numbers, grid references, floor levels, building areas)
2. Identify overlapping date ranges for activities in the same location
3. Generate coordination alert with trade contacts from the project directory

**Example output**:
```
TRADE COORDINATION ALERT - February 20, 2026

AREA: Rooms 201-208, Second Floor
  [1] Mechanical rough-in (ABC Mechanical, foreman: J. Smith, 555-0101)
      Duration: Feb 18-21, 4 workers
  [2] Electrical rough-in (DEF Electric, foreman: M. Johnson, 555-0202)
      Duration: Feb 19-22, 3 workers
  [3] Fire protection rough-in (GHI Fire, foreman: T. Williams, 555-0303)
      Duration: Feb 20-21, 2 workers

  COORDINATION REQUIREMENTS:
  - All three trades working above ceiling in same rooms
  - Sequence: Mechanical ductwork first (largest), then electrical conduit, then fire protection piping
  - Pre-coordination meeting recommended Feb 19 afternoon
  - Confirm ceiling closure date with all trades: target Feb 24

AREA: Grid C-D/3-4, Ground Floor
  [1] Concrete curing in progress (protective blankets on footings)
  [2] Plumbing underground rough-in (JKL Plumbing, foreman: R. Davis, 555-0404)
      Duration: Feb 20-22, 2 workers

  COORDINATION REQUIREMENTS:
  - Plumbing crew working adjacent to curing concrete
  - Do not disturb protective blankets or vibrate adjacent soil
  - Mark curing zone with caution tape before plumbing crew arrives
```

### Integration with Existing Skills

**Morning Brief skill**: Consumes today's work generation, weather alerts, inspection triggers, and coordination alerts to produce the daily morning briefing.

**Daily Report skill**: Uses today's scheduled work as the baseline for tracking actual vs. planned progress. Auto-populates "work performed today" fields with scheduled activities for the superintendent to confirm or modify.

**Look-Ahead skill**: Uses constraint identification data to generate the standard 2-week and 6-week look-ahead reports with constraint flags.

**Material Tracker skill**: Uses inspection triggers (especially testing lab notifications) and procurement workflow data to track material status from order through delivery through installation.

**Report QA skill**: Cross-references daily report entries against schedule data to verify that reported work aligns with scheduled activities and flags discrepancies (e.g., "Daily report says 'poured footings' but schedule shows footings not starting until next week").

## Construction Schedule Generation

When the user asks about schedules extracted from plans ("show me the door schedule", "generate hardware schedule", "finish schedule", "room schedule"):

1. Load `plans-spatial.json` (room_schedule, drawing index) and `specs-quality.json` (spec_sections)
2. Determine which schedule type(s) to generate:
   - **door**: Door schedule (from room_schedule + Division 08)
   - **hardware**: Hardware schedule (from Division 08 71 00)
   - **fixture**: Plumbing fixture schedule (from Division 22)
   - **finish**: Finish schedule (from room_schedule + Division 09)
   - **plumbing**: Plumbing connections/equipment (from Division 22)
   - **equipment**: Mechanical/electrical equipment (from Divisions 23, 26)
   - **room**: Room schedule (from room_schedule)
   - **all**: Generate all available schedules
3. Extract data from the appropriate config sections
4. Format as HTML tables with professional styling (Navy headers, alternating rows)
5. Include spec section references for each line item
6. Flag incomplete data clearly ("DATA INCOMPLETE — requires plan review")
7. Save as `{PROJECT_CODE}_{schedule_type}_Schedule.html`

If schedule data doesn't exist for the requested type: "No schedule data available for [type]. Run /process-docs with relevant plan sheets to extract this data."



## Resources

This skill includes comprehensive reference documentation:

### references/
Domain-specific extraction guides that inform the extraction process:

- **extraction-rules.md** - Framework and classification system (ALWAYS read first)
- **plans-deep-extraction.md** - Complete extraction guide for plans/drawings
- **specifications-deep-extraction.md** - All CSI divisions with exact extraction requirements
- **schedule-deep-extraction.md** - CPM schedule sequencing and logic extraction
- **civil-deep-extraction.md** - Site utilities, grading, and paving extraction
- **compliance-deep-extraction.md** - Geotech, safety, SWPPP extraction
- **project-docs-deep-extraction.md** - Contracts, subs, RFIs, submittals, subcontracts, POs extraction
- **pemb-deep-extraction.md** - PEMB reactions, anchor bolts, framing, erection, panels, accessories
- **submittals-deep-extraction.md** - Concrete mixes, door hardware, shop drawings, MEP equipment, finishes
- **dxf-extraction.md** - DXF/DWG spatial extraction: layers, blocks, hatches, polylines, dimensions
- **visual-extraction-reference.md** - Visual plan analysis: OCR, line detection, symbols, materials, dimensions, scale
- **parse_dxf.py** - Python pipeline script for extracting structured data from .dxf files
- **convert_dwg.py** - .dwg → .dxf conversion wrapper (requires ODA File Converter)
- **visual_plan_analyzer.py** - 7-pass visual analysis pipeline for plan sheet images (PaddleOCR + OpenCV)
- **symbol_templates/** - Construction symbol template library for template matching (Pass 4)

These references contain the detailed "how-to" for extracting comprehensive, field-actionable data from each document type.



## Document Register & Transmittal Tracking

The document register provides a single source of truth for all project documents and their revision history. Every drawing, specification, submittal, RFI, and change order flows through this register to ensure field teams always use current documents.

### Document Register Data Model

The document register is stored in `project-config.json` under the `document_register` key as an array of document records:

```json
{
  "document_register": [
    {
      "doc_id": "DWG-A1.0",
      "title": "Architectural Floor Plan — Level 1",
      "type": "drawing | specification | submittal | rfi | change_order | correspondence | report | contract",
      "discipline": "architectural | structural | mechanical | electrical | plumbing | fire_protection | civil | general",
      "current_revision": "3",
      "revision_history": [
        { "revision": "3", "date": "2026-02-10", "issued_by": "ABC Architects", "description": "ASI-003 incorporated" },
        { "revision": "2", "date": "2026-01-15", "issued_by": "ABC Architects", "description": "Permit set corrections" }
      ],
      "status": "issued_for_construction | under_review | approved | superseded | void",
      "distribution": ["GC", "Owner", "Architect", "Structural"],
      "file_path": "05 - Plans/Arch_Plans_Rev3.pdf"
    }
  ]
}
```

**Document Register Fields:**
- `doc_id`: Unique document identifier (e.g., DWG-A1.0, SPEC-03, RFI-0045)
- `title`: Full document title or description
- `type`: Document classification (drawing, specification, submittal, rfi, change_order, correspondence, report, contract)
- `discipline`: Engineering discipline (architectural, structural, mechanical, electrical, plumbing, fire_protection, civil, general)
- `current_revision`: Current revision letter or number
- `revision_history`: Array of all revisions issued, earliest to latest
  - `revision`: Revision identifier (1, 2, 3 or A, B, C)
  - `date`: Revision issue date (ISO 8601)
  - `issued_by`: Originating firm or person
  - `description`: Summary of changes (e.g., "ASI-003 incorporated", "Permit corrections", "RFI-042 response")
- `status`: Document lifecycle status (issued_for_construction, under_review, approved, superseded, void)
- `distribution`: Array of parties receiving the document (GC, Owner, Architect, Structural, MEP, subcontractors, etc.)
- `file_path`: Relative path to document storage location in project folder structure

### Transmittal Tracking Data Model

Transmittals document formal distribution of documents with acknowledgment tracking:

```json
{
  "transmittals": [
    {
      "id": "TX-001",
      "date": "2026-02-10",
      "from": "ABC Architects",
      "to": "Morehead Construction",
      "cc": ["Owner PM"],
      "documents": ["DWG-A1.0 Rev 3", "DWG-A1.1 Rev 3"],
      "purpose": "issued_for_construction | for_review | for_approval | for_information | as_requested",
      "action_required": "Distribute to field",
      "acknowledged": false,
      "acknowledged_date": null
    }
  ]
}
```

**Transmittal Fields:**
- `id`: Unique transmittal identifier (TX-NNN format)
- `date`: Transmittal issue date (ISO 8601)
- `from`: Originating firm (architect, engineer, contractor, etc.)
- `to`: Primary recipient
- `cc`: Array of other recipients receiving copies
- `documents`: Array of documents included in transmittal (with revision identifiers)
- `purpose`: Purpose of transmittal (issued_for_construction, for_review, for_approval, for_information, as_requested)
- `action_required`: Specific action required by recipient (e.g., "Distribute to field", "Review and comment", "Approve for construction")
- `acknowledged`: Boolean; true when recipient confirms receipt
- `acknowledged_date`: Date transmittal was acknowledged (ISO 8601)

### Revision Control Workflow

**Standard Document Lifecycle:**

1. **New Document Received**: Architect issues drawing or spec document
2. **Log in Register**: Create document register entry with Revision 1, current_revision = "1", status = "issued_for_construction"
3. **Update Revision**: When new revision received, add entry to revision_history array, increment current_revision
4. **Distribute via Transmittal**: Create transmittal record documenting distribution list and action required
5. **Confirm Receipt**: Update transmittal `acknowledged` = true when GC confirms
6. **Supersede Old Revision**: Mark previous revision status as "superseded" in register; current document is the only active record
7. **Field Access**: Field teams query register for current_revision before accessing documents

**Status Progression:**
```
[issued_for_construction] → [approved] or [under_review] → [approved]
                                                              ↓
                                                        [superseded] (when newer revision issued)
                                                        [void] (if cancelled)
```

### Current Document Identification

**Critical Rule**: Field teams MUST verify they are using the current revision before starting work.

**Best Practice Workflow:**
1. Superintendent checks document register for current_revision (NOT guessing or using printed copy)
2. If current_revision differs from what's on site, STOP and get updated document from office
3. Each morning brief surfaces any document revisions issued in past 24 hours
4. Daily report includes note: "All work performed per [DOC-ID] Rev [X] dated [DATE]"

**Misfiled Document Prevention:**
- Register provides single source of truth for which revision is current
- Old revisions should be physically marked "VOID" or filed separately
- Digital document storage enforces current_revision path (e.g., `Plans/DWG-A1.0_Rev3/`)

### Auto-Population: Document Processing Integration

When `/process-docs` processes a new document:

1. **Scan Metadata**: Extract title, revision, date, creator from PDF metadata or filename
2. **Check Register**: Look up doc_id in existing document_register
   - If NEW: Create new register entry with revision = extracted revision, status = "issued_for_construction"
   - If EXISTING: Add entry to revision_history, update current_revision, update status
3. **Create/Update Record**: Automatically populate register entry with extraction data
4. **Log in Version History**: Add version_history entry in project-config.json noting document addition/update
5. **Notify PM**: Flag in morning brief if new revision supersedes older version

**Example Auto-Population Scenario:**
```
User processes: "Architectural_Plans_Rev3_02-10-2026.pdf"
Extract: title = "Architectural Floor Plan", revision = "3", date = "2026-02-10"
Register lookup: doc_id "DWG-A1.0" exists with current_revision = "2"
Action: Add new revision_history entry, update current_revision to "3", set status to "issued_for_construction"
Notify: Morning brief alerts "DWG-A1.0 Rev 3 issued 2026-02-10 — Rev 2 now superseded"
```

### Integration with Project Management

**Morning Brief Integration:**
- Display new/updated documents issued in past 24 hours
- Alert if document status changed (e.g., approved, superseded)
- Surface pending transmittal acknowledgments

**Daily Report Integration:**
- Auto-complete document references (suggest current revisions)
- Flag if work performed per superseded document revision
- Cross-reference work location to affected drawings

**Change Order Tracking:**
- Link COs to triggering documents (e.g., RFI response, ASI, new specification requirement)
- Reference document revisions in CO description
- Track CO impact on future revisions

**Quantity & Schedule Extraction:**
- Pull room schedules from architectural drawings (document_register links to extracted room_schedule)
- Pull equipment lists from MEP drawings
- Cross-reference spec sections extracted from specifications documents

### Document Register as Coordination Tool

**Discipline Cross-Reference:**
- Query register by discipline (e.g., "all electrical documents") to identify coordination gaps
- Flag missing documents (e.g., no MEP coordination drawings issued)
- Alert if architectural changes not reflected in structural/MEP documents

**Specification Cross-Reference:**
- Link spec divisions to relevant drawings
- Flag conflicts when spec requires something not shown on drawings
- Track when spec sections updated due to RFI responses

**Distribution Verification:**
- Report: which parties have acknowledged each transmittal
- Alert: if GC hasn't acknowledged critical document transmittal
- Audit trail: full distribution and acknowledgment history for each document

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


