# environmental-compliance — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the environmental-compliance skill.



## Waste Management

### C&D Waste Stream Categories

| Waste Stream | Examples | Recycling Potential | Typical Diversion Method |
|--------------|----------|--------------------|----|
| Concrete/Masonry | Broken concrete, block, brick, stone | High (95%+) | Crush on-site or haul to concrete recycler |
| Wood | Framing lumber, plywood, pallets, formwork | Moderate (50-80%) | Biomass fuel, mulch, pallet recycling |
| Metals | Rebar, steel studs, copper pipe, ductwork, flashing | Very High (98%+) | Scrap metal recycler (revenue potential) |
| Drywall | Gypsum board scrap, damaged sheets | Moderate (60-80%) | Gypsum recycler (must be clean, no paint/tape contamination) |
| Cardboard | Packaging, boxes, wrapping | Very High (95%+) | Cardboard recycler or mixed paper stream |
| Plastic | Packaging film, pipe scraps, wrap | Low-Moderate (30-50%) | Clean film recycling; rigid plastic limited |
| Asphalt/Roofing | Asphalt shingles, built-up roofing | Moderate (70%) | Asphalt recycler (shingle-to-road programs) |
| Mixed C&D | Unsegregated construction debris | Variable (30-60%) | Commingled recycling facility |
| Land-clearing | Trees, stumps, brush, soil | High (80%+) | Mulch, compost, clean fill |

### Segregation vs. Commingled Recycling

**On-Site Segregation**:

| Pros | Cons |
|------|------|
| Higher diversion rates (cleaner streams) | Requires space for multiple containers |
| Lower per-ton recycling cost | Requires worker training and enforcement |
| Revenue from metals scrap | More coordination with multiple haulers |
| Better documentation for LEED | Daily monitoring needed |

**Commingled Recycling (Single-Stream)**:

| Pros | Cons |
|------|------|
| Single container on-site (less space) | Lower diversion rates (contamination) |
| Simpler for workers (one dumpster) | Higher per-ton processing cost |
| Less site coordination | Facility diversion rate may not meet LEED target |
| Fewer hauler relationships | Less control over actual recycling outcomes |

**Decision Factors**:
- LEED project requiring 75% diversion: **Segregation strongly recommended**
- Tight site with no space for multiple bins: **Commingled with verified recycling facility**
- Urban infill with limited staging: **Commingled or off-site segregation at transfer station**
- Large site with space: **On-site segregation for cost savings and higher diversion**

### Diversion Rate Tracking

**Monthly Tracking Template**:

| Month | Concrete (tons) | Wood (tons) | Metal (tons) | Drywall (tons) | Cardboard (tons) | Other Recycled (tons) | Landfilled (tons) | Diversion Rate |
|-------|----------------|-------------|--------------|-----------------|-------------------|-----------------------|--------------------|----|
| Jan | 12.5 | 3.2 | 1.8 | 0.0 | 0.5 | 0.3 | 4.2 | 81.3% |
| Feb | 8.0 | 5.1 | 2.3 | 1.2 | 0.8 | 0.4 | 5.5 | 76.4% |
| Cumulative | 20.5 | 8.3 | 4.1 | 1.2 | 1.3 | 0.7 | 9.7 | 78.8% |

**Calculation**:
```
Monthly Diversion Rate = Sum of All Recycled Streams / (Sum Recycled + Landfilled) x 100%
Cumulative Diversion Rate = Project Total Recycled / (Project Total Recycled + Project Total Landfilled) x 100%
```

**Documentation Requirements**:
- Weight tickets from each hauler (date, weight, material type, destination)
- Hauler recycling facility certification
- Facility diversion rate documentation (for commingled loads)
- Monthly summary spreadsheet
- Cumulative project diversion rate tracker
- Photos of segregation setup on-site

### Hazardous Waste Management

**Identification — Characteristic vs. Listed Waste**:

| Type | Description | Examples |
|------|-------------|----------|
| Characteristic — Ignitability (D001) | Flash point < 140 degrees F | Waste solvents, paint thinner, fuel |
| Characteristic — Corrosivity (D002) | pH < 2 or > 12.5 | Acid cleaners, caustic solutions |
| Characteristic — Reactivity (D003) | Unstable, explosive, generates gas | Certain adhesives, oxidizers |
| Characteristic — Toxicity (D004-D043) | Fails TCLP for listed metals/organics | Lead paint chips, contaminated soil |
| Listed — F-list | Non-specific source | Spent halogenated solvents (F001-F005) |
| Listed — K-list | Specific source | Industry-specific process waste |
| Listed — P/U-list | Discarded commercial chemicals | Unused chemicals disposed |

**Manifesting Requirements (EPA Form 8700-22)**:
- Required for ALL hazardous waste shipments from construction site
- Generator (contractor) must sign manifest before transport
- Transporter must be licensed and sign manifest
- Receiving facility confirms receipt
- Generator retains copy for 3 years minimum
- Exception report required if manifest copy not returned within 35 days (large quantity generator)

**Storage Time Limits**:

| Generator Status | Maximum Storage | Quantity Threshold |
|------------------|-----------------|--------------------|
| Large Quantity Generator (LQG) | 90 days | > 2,200 lbs/month |
| Small Quantity Generator (SQG) | 180 days | 220 - 2,200 lbs/month |
| Very Small Quantity Generator (VSQG) | No time limit (but must ship eventually) | < 220 lbs/month |

**Construction Site Hazardous Waste Best Practices**:
- Designate a hazardous waste accumulation area (signed, secured, secondary containment)
- Weekly inspections of storage area
- Label all containers: "Hazardous Waste," contents, accumulation start date
- Keep containers closed except when adding/removing waste
- Do not mix incompatible wastes
- Train all workers on hazardous waste identification and proper handling

### Universal Waste

**Common Universal Wastes on Construction Sites**:

| Waste Type | Examples | Collection Method | Disposal |
|------------|----------|-------------------|----------|
| Fluorescent lamps | T8, T12 tubes, CFL bulbs | Intact in original boxes or lamp recycling boxes | Licensed lamp recycler |
| Batteries | Lead-acid, lithium, NiCd, alkaline | Separate containers by chemistry | Battery recycler |
| Mercury devices | Thermostats, switches, gauges | Sealed containers, labeled | Mercury recycler |
| Pesticides | Unused herbicides, insecticides | Original containers | Hazardous waste facility |
| Electronics | Computer equipment, controls | Separate collection | E-waste recycler |

**Universal Waste Rules**:
- Label containers with "Universal Waste — [type]"
- Accumulate for up to 1 year (mark accumulation start date)
- Do not treat, dispose, dilute, or discharge
- Train employees who handle universal waste
- Ship to authorized recycler or destination facility

---



## Dust and Air Quality

### Regulatory Limits

**National Ambient Air Quality Standards (NAAQS)**:

| Pollutant | Standard | Averaging Time | Construction Relevance |
|-----------|----------|----------------|----------------------|
| PM10 | 150 ug/m3 | 24-hour | Dust from earthwork, demolition, concrete cutting |
| PM2.5 | 35 ug/m3 | 24-hour | Fine dust from grinding, cutting, welding fumes |
| PM2.5 | 12 ug/m3 | Annual | Long-term site operations near sensitive receptors |

**When Construction Triggers Monitoring**:
- Project within 500 feet of sensitive receptors (schools, hospitals, residential)
- Air quality management district requires monitoring
- LEED project requiring documentation
- Large-scale earthwork or demolition projects
- Jurisdictions with specific construction dust rules (e.g., Maricopa County, Clark County)

### Dust Suppression Methods

| Method | Effectiveness | Application | Cost |
|--------|---------------|-------------|------|
| Water truck | High (70-90% reduction) | Active grading, haul roads, stockpiles | Moderate (water + labor) |
| Chemical stabilizer | Very High (80-95%) | Haul roads, long-term exposed areas | Higher upfront, lower maintenance |
| Wind fencing | Moderate (50-70%) | Stockpiles, site perimeter | Low-Moderate |
| Covered loads | Required | All trucks leaving site | Minimal (tarps) |
| Stabilized construction entrance | Required | Site entrance/exit points | Moderate (gravel + maintenance) |
| Hydroseeding/mulch | High (long-term) | Inactive disturbed areas (>14 days) | Moderate |
| Track-out prevention | Required | Stabilized entrance + street sweeping | Moderate |
| Speed limits | Moderate (30-50%) | Internal haul roads (15 MPH max) | None |
| Minimized disturbance | Preventive | Phase grading, limit exposed area | None (planning) |

### Silica Exposure (OSHA Table 1)

**Regulatory Framework**: 29 CFR 1926.1153 — Respirable Crystalline Silica in Construction.

**Permissible Exposure Limit (PEL)**: 50 ug/m3 as 8-hour TWA.

**OSHA Table 1 — Common Construction Activities and Required Controls**:

| Activity | Equipment/Task | Required Controls | Respiratory Protection |
|----------|---------------|-------------------|----------------------|
| Concrete cutting (stationary) | Stationary masonry saw | Continuous water feed to blade | None if water used effectively |
| Concrete cutting (handheld) | Handheld power saw | Continuous water feed to blade | None if water used effectively |
| Concrete grinding | Handheld grinder | Shroud + HEPA vacuum attachment | None if vacuum effective |
| Concrete core drilling | Core drill | Continuous water feed | None if water used |
| Demolition (concrete) | Jackhammer, breaker | Continuous water spray on point of impact | APF 10 respirator |
| Tuck-pointing/mortar removal | Grinder | Shroud + HEPA vacuum | APF 10 respirator |
| Mixing concrete/morite | Bag mixing | Use pre-mixed or enclosed mixing | APF 10 if visible dust |
| Drywall finishing (sanding) | Manual or power sander | Wet methods or HEPA vacuum sander | APF 10 if dust visible |

**Medical Surveillance Requirements**:
- Required for workers exposed at or above action level (25 ug/m3) for 30+ days/year
- Initial medical exam within 30 days of initial assignment
- Periodic exam every 3 years
- Includes chest X-ray, pulmonary function test, TB test
- Physician determines work fitness

> **Cross-Reference**: For detailed silica exposure prevention procedures and PPE requirements, see `references/hazmat-awareness-guide.md`.

### Air Quality Management Plan for Sensitive Receptors

**When Required**: Project within 500 feet of schools, hospitals, nursing homes, daycare facilities, or dense residential areas.

**Plan Elements**:
1. **Receptor identification**: Map all sensitive receptors within 500-foot radius
2. **Baseline monitoring**: Establish ambient air quality before construction
3. **Activity-specific controls**: Enhanced dust suppression for high-dust activities
4. **Monitoring plan**: PM10/PM2.5 monitors at site boundary nearest receptors
5. **Action levels**: Site-specific thresholds triggering enhanced controls
6. **Notification protocol**: Advance notice to sensitive receptors for high-dust activities
7. **Complaint response**: Document and respond to dust complaints within 24 hours

---



## Noise Compliance

### Typical Municipal Noise Limits

| Zone | Daytime (7AM - 10PM) | Nighttime (10PM - 7AM) | Notes |
|------|----------------------|------------------------|-------|
| Residential | 65 dBA | 55 dBA | At property line or nearest receptor |
| Commercial | 70 dBA | 60 dBA | At property line |
| Industrial | 80 dBA | 70 dBA | At property line |
| Mixed-Use | 65-70 dBA | 55-60 dBA | Depends on adjacent use |

**Measurement Method**:
- Sound level meter (Type 2 minimum, Type 1 preferred) at property line or nearest receptor
- Measurement height: 4-5 feet above ground
- A-weighted scale (dBA) — standard for environmental noise
- Measurement duration: minimum 1-minute Leq (equivalent continuous sound level)

### Common Construction Noise Levels

| Equipment/Activity | Typical dB at 50 feet | Notes |
|--------------------|-----------------------|-------|
| Pile driver (impact) | 95 - 105 dBA | Highest construction noise source |
| Pile driver (vibratory) | 80 - 95 dBA | Significantly quieter than impact |
| Concrete saw | 90 - 95 dBA | Continuous high-frequency noise |
| Jackhammer/breaker | 85 - 95 dBA | Impact noise, intermittent |
| Excavator | 80 - 85 dBA | Continuous during operation |
| Backhoe | 75 - 85 dBA | Varies with load |
| Concrete pump | 80 - 85 dBA | Engine + hydraulic noise |
| Generator | 75 - 85 dBA | Continuous; depends on size |
| Backup alarm | 97 - 112 dBA | Intentionally loud; most common complaint |
| Crane | 75 - 85 dBA | Engine + winch noise |
| Pneumatic tools | 85 - 95 dBA | Compressor + tool |
| Concrete vibrator | 75 - 80 dBA | Lower than most equipment |

**Sound Attenuation with Distance**:
```
dB reduction = 20 x log10(distance2 / distance1)

Example: Excavator at 85 dBA at 50 feet
  At 100 feet: 85 - 20 x log10(100/50) = 85 - 6 = 79 dBA
  At 200 feet: 85 - 20 x log10(200/50) = 85 - 12 = 73 dBA
  At 500 feet: 85 - 20 x log10(500/50) = 85 - 20 = 65 dBA
```

### Noise Mitigation Strategies

| Strategy | Noise Reduction | Application |
|----------|-----------------|-------------|
| Equipment selection (quieter models) | 5 - 15 dBA | Specify low-noise equipment in procurement |
| Temporary noise barriers (plywood/mass wall) | 10 - 15 dBA | Between source and receptor |
| Sound blankets on equipment | 5 - 10 dBA | Wrap generators, compressors |
| Operational restrictions (time-of-day) | N/A | Limit noisy work to permitted hours |
| Broadband backup alarms | 10 - 20 dBA reduction vs. tonal | Replace beep alarms with white-noise alarms |
| Mufflers and silencers | 5 - 15 dBA | Require on all combustion equipment |
| Vibration isolation pads | 3 - 8 dBA | Under compressors, generators |
| Notification to neighbors | N/A | Advance notice reduces complaints |

### Variance Procedures for Out-of-Hours Work

**When Needed**: Night work, weekend work, or work exceeding noise ordinance limits.

**Typical Variance Application Process**:
1. Apply to municipal authority (building department or environmental office) **14-30 days** in advance
2. Provide: project description, noise sources, duration, mitigation measures, justification
3. Notify adjacent property owners (certified mail or door-to-door) per local requirement
4. Public comment period (some jurisdictions)
5. Permit issued with conditions (specific hours, noise limits, monitoring requirements)
6. Superintendent maintains variance permit on-site
7. Document compliance with conditions

**Common Conditions on Noise Variances**:
- Limited hours (e.g., Saturday 8AM-5PM only, no Sunday/holiday work)
- Maximum noise level at property line
- Real-time noise monitoring during work
- Complaint hotline number posted and operational
- Designated contact person for noise complaints
- Enhanced mitigation (barriers, equipment restrictions)
- Duration limit (variance typically for specific activity, not open-ended)

---



## Environmental Incident Response

### Spill Response

**Spill Kit Locations and Contents**:

Each construction site should have spill kits at:
- Equipment fueling areas
- Chemical/material storage areas
- Near waterways or storm drains
- In each work vehicle carrying fuel or chemicals

**Standard Spill Kit Contents**:

| Item | Quantity | Purpose |
|------|----------|---------|
| Absorbent pads (oil-only) | 20 | Absorb petroleum on water or hard surfaces |
| Absorbent booms (oil-only) | 4 x 10-foot | Contain petroleum spills on water |
| Granular absorbent (kitty litter or clay) | 2 x 25-lb bags | Absorb spills on soil and pavement |
| Nitrile gloves | 4 pairs | Hand protection during cleanup |
| Safety goggles | 2 pairs | Eye protection |
| Plastic bags (6-mil) | 10 | Containerize used absorbent for disposal |
| Drain covers (neoprene or poly) | 2 | Cover storm drain inlets during spill |
| Shovel | 1 | Remove contaminated soil |
| Emergency contact card | 1 | NRC, EPA, state agency, fire department numbers |

### Immediate Response Protocol

```
SPILL OCCURS
    │
    ├─ 1. SAFETY FIRST: Eliminate ignition sources; evacuate if fumes/vapors
    │
    ├─ 2. CONTAIN: Deploy absorbent booms/pads around spill perimeter
    │     └─ PROTECT STORM DRAINS: Cover nearest drain inlet with drain cover
    │
    ├─ 3. NOTIFY: Alert superintendent immediately
    │     └─ Superintendent determines if reportable quantity (see below)
    │
    ├─ 4. STOP SOURCE: If safe, stop the leak (close valve, right container, plug hole)
    │
    ├─ 5. CLEAN UP: Absorb with pads/granular absorbent; shovel contaminated soil
    │     └─ Do NOT wash spill into storm drain or waterway
    │
    ├─ 6. DOCUMENT: Photos, measurements (area, depth), material type, quantity estimate
    │     └─ Record timeline: discovery time, response actions, notification times
    │
    └─ 7. DISPOSE: Used absorbent material as hazardous waste if contaminated with hazardous substance
          └─ Or as solid waste if petroleum-only and below hazardous thresholds
```

### Reportable Quantity Thresholds

**CERCLA Reportable Quantities** (trigger NRC notification):

| Substance | Reportable Quantity (RQ) | Common Construction Source |
|-----------|--------------------------|---------------------------|
| Petroleum (to navigable water) | Any amount creating sheen | Fuel spills, hydraulic fluid |
| Diesel fuel (to water) | Any visible sheen | Equipment fueling |
| Gasoline | 0 lbs (any to water) | Fuel storage |
| Motor oil (to water) | Any visible sheen | Equipment leaks |
| Lead compounds | 10 lbs | Lead paint removal |
| Asbestos (friable) | 1 lb | Demolition/renovation |
| Sulfuric acid | 1,000 lbs | Battery acid |
| Acetone | 5,000 lbs | Solvent/cleaner |
| Paint thinner/MEK | 5,000 lbs | Coatings |

**Note**: Spills to navigable waters, including storm drains that discharge to waterways, have the lowest thresholds. Petroleum sheens on water are always reportable.

### Agency Notification Requirements

| Condition | Agency | Contact | Timeline |
|-----------|--------|---------|----------|
| Reportable quantity release | NRC (National Response Center) | 1-800-424-8802 | Immediate (as soon as practicable) |
| Spill to water or storm drain | State environmental agency | State-specific hotline | Immediate (same day) |
| Hazmat release with fire/explosion | Local fire department | 911 | Immediate |
| Asbestos release | EPA regional office | Regional number | Within 24 hours |
| Oil spill creating sheen on water | NRC + state | See above | Immediate |
| CERCLA hazardous substance release | NRC + state + EPA | See above | Immediate |

### Incident Documentation Requirements

**Environmental Incident Report Contents**:
1. Date, time, and location of incident
2. Material released (name, quantity estimate, CAS number if known)
3. Source of release (equipment failure, container breach, operational error)
4. Environmental media affected (soil, water, air)
5. Photos of spill area, affected media, cleanup progress
6. Estimated area and depth of contamination
7. Response actions taken (containment, cleanup, notification)
8. Timeline of events (discovery through cleanup completion)
9. Agencies notified (name, contact, time of notification)
10. Cleanup verification (photos, sampling results if required)
11. Root cause analysis and corrective actions
12. Waste disposal documentation (manifest if hazardous)

---



## Environmental Compliance Data Model

### environmental-log.json Schema

```json
{
  "project": "PROJECT_CODE",
  "last_updated": "2026-02-19T08:00:00Z",
  "leed": {
    "certification_target": "Gold",
    "credits": [
      {
        "id": "SS-C1",
        "name": "Construction Activity Pollution Prevention",
        "status": "in_progress",
        "target_points": 1,
        "documentation_complete": false,
        "notes": "SWPPP active; weekly inspections ongoing",
        "last_review": "2026-02-19"
      },
      {
        "id": "MR-P1",
        "name": "Construction & Demolition Waste Management",
        "status": "in_progress",
        "target_points": 2,
        "current_diversion_rate": 78.8,
        "documentation_complete": false,
        "notes": "On track for 75% diversion (2 points)",
        "last_review": "2026-02-19"
      },
      {
        "id": "EQ-C3",
        "name": "Construction IAQ Management",
        "status": "in_progress",
        "target_points": 1,
        "iaq_plan_in_place": true,
        "documentation_complete": false,
        "notes": "SMACNA guidelines followed; duct protection in place",
        "last_review": "2026-02-19"
      }
    ],
    "product_tracking": [
      {
        "product_name": "Interior Latex Paint - Flat",
        "manufacturer": "Sherwin-Williams",
        "voc_content_gL": 45,
        "voc_limit_gL": 50,
        "compliant": true,
        "area_installed": "Building Interior - Walls",
        "date_installed": "2026-03-15",
        "epd": false,
        "hpd": false,
        "data_sheet_filed": true
      }
    ]
  },
  "swppp": {
    "permit_number": "CGP-2026-XXXXX",
    "noi_filed": "2026-01-15",
    "permit_effective": "2026-02-01",
    "not_filed": null,
    "status": "active",
    "inspections": [
      {
        "id": "SWPPP-INS-001",
        "date": "2026-02-14",
        "type": "routine_weekly",
        "inspector": "Superintendent Name",
        "findings": "All BMPs functional. Silt fence intact along south perimeter.",
        "deficiencies": [],
        "corrective_actions": [],
        "rainfall_24hr": 0.0,
        "photos": ["swppp-2026-02-14-001.jpg", "swppp-2026-02-14-002.jpg"]
      },
      {
        "id": "SWPPP-INS-002",
        "date": "2026-02-17",
        "type": "post_storm",
        "inspector": "Superintendent Name",
        "findings": "0.45 inches rainfall overnight. Minor sediment accumulation at inlet protection.",
        "deficiencies": ["Inlet protection at CB-3 partially displaced"],
        "corrective_actions": [
          {
            "action": "Reposition and reinforce inlet protection at CB-3",
            "responsible": "Site crew",
            "deadline": "2026-02-18",
            "status": "completed",
            "completion_date": "2026-02-17"
          }
        ],
        "rainfall_24hr": 0.45,
        "photos": ["swppp-2026-02-17-001.jpg"]
      }
    ]
  },
  "waste_management": {
    "plan_in_place": true,
    "diversion_target": 75,
    "monthly_tracking": [
      {
        "month": "2026-01",
        "streams": {
          "concrete": 12.5,
          "wood": 3.2,
          "metal": 1.8,
          "drywall": 0.0,
          "cardboard": 0.5,
          "other_recycled": 0.3,
          "landfilled": 4.2
        },
        "total_recycled": 18.3,
        "total_landfilled": 4.2,
        "diversion_rate": 81.3
      }
    ],
    "cumulative_recycled": 36.4,
    "cumulative_landfilled": 9.7,
    "cumulative_diversion_rate": 78.9,
    "hauler_certifications": [
      {
        "company": "Green Recycling Inc.",
        "certification": "C&D Recycling Facility Permit #12345",
        "verified_date": "2026-01-10",
        "diversion_capability": 85
      }
    ]
  },
  "hazmat": {
    "events": [
      {
        "id": "HAZMAT-001",
        "date": "2026-02-10",
        "type": "asbestos_survey",
        "description": "Pre-demolition asbestos survey completed for existing outbuilding. No ACM identified.",
        "action_taken": "Survey report filed. Demolition cleared to proceed.",
        "status": "closed",
        "documentation": ["asbestos-survey-report-2026-02-10.pdf"]
      }
    ],
    "active_hazards": [],
    "training_records": [
      {
        "topic": "Hazmat Awareness (asbestos, lead, mold, contaminated soil)",
        "date": "2026-02-01",
        "attendees": 8,
        "trainer": "Environmental Consultant"
      }
    ]
  },
  "dust_noise": {
    "dust_monitoring": [
      {
        "date": "2026-02-18",
        "location": "South property line (nearest receptor)",
        "pm10_reading": 85,
        "pm10_limit": 150,
        "compliant": true,
        "conditions": "Active grading, water truck operating",
        "notes": "Below threshold. Continued monitoring during earthwork."
      }
    ],
    "noise_monitoring": [
      {
        "date": "2026-02-18",
        "location": "East property line (residential)",
        "reading_dba": 72,
        "limit_dba": 65,
        "compliant": false,
        "source": "Concrete saw operation",
        "mitigation_applied": "Relocated saw behind noise barrier",
        "post_mitigation_dba": 63,
        "post_mitigation_compliant": true
      }
    ],
    "noise_variances": [],
    "complaints": []
  },
  "incidents": [
    {
      "id": "ENV-INC-001",
      "date": "2026-02-12",
      "type": "spill",
      "material": "Diesel fuel",
      "quantity_estimate": "2 gallons",
      "location": "Equipment staging area, south lot",
      "cause": "Hydraulic line failure on excavator",
      "environmental_media_affected": ["soil"],
      "response_actions": [
        "Absorbent pads deployed immediately",
        "Contaminated soil excavated (approx 0.5 CY)",
        "Storm drain 50 feet away covered as precaution"
      ],
      "reportable": false,
      "agencies_notified": [],
      "cleanup_verified": true,
      "waste_disposal": "Contaminated soil and absorbent disposed as non-hazardous solid waste",
      "root_cause": "Aged hydraulic hose — maintenance schedule updated",
      "corrective_actions": [
        "All excavator hydraulic hoses inspected and replaced if worn",
        "Pre-shift hydraulic inspection added to daily equipment check"
      ],
      "status": "closed",
      "photos": ["env-inc-001-spill.jpg", "env-inc-001-cleanup.jpg"]
    }
  ],
  "version_history": [
    {
      "timestamp": "2026-02-19T08:00:00Z",
      "action": "environmental-log created",
      "user": "superintendent"
    }
  ]
}
```

---



## Integration with Other Skills

### safety-management
- Hazmat events (asbestos, lead, silica exposure) cross-reference safety incident tracking
- Silica exposure monitoring feeds into safety metrics and OSHA recordkeeping
- Spill incidents may involve safety response (PPE, evacuation) documented in safety-log.json
- Toolbox talks on environmental topics (spill response, dust control) logged in safety-management

### daily-report-format
- Daily environmental observations captured in daily report (weather, BMP status, dust, noise)
- Environmental incidents auto-populate in daily report environmental section
- SWPPP inspections referenced in daily report when conducted
- Waste hauling activity noted in daily report

### inspection-tracker
- SWPPP inspections tracked in environmental-log.json (separate from building inspections in inspection-log.json)
- Environmental permits (NPDES, air quality, noise variance) can be tracked alongside building permits
- Failed SWPPP inspections generate corrective actions tracked to closure

### field-reference/bmp-field-guide
- BMP installation specifications and maintenance procedures
- This environmental-compliance skill handles the permit and documentation side
- BMP field guide handles the physical installation and maintenance side
- Both reference the same SWPPP document

### closeout-commissioning
- LEED documentation package compiled for project closeout
- Waste diversion final report required for LEED submittal
- IAQ testing results documented for closeout
- Environmental permits closed out (NOT filed for SWPPP)
- Hazmat clearance documentation filed with closeout package

### project-data
- Environmental log stored alongside project configuration
- Project config includes environmental compliance requirements and targets
- Version history tracks all environmental data changes

---



## Trigger Phrases

Use this skill when user says:
- "LEED documentation" / "LEED credit tracking" / "waste diversion for LEED"
- "SWPPP inspection" / "stormwater inspection" / "BMP inspection"
- "Environmental compliance" / "environmental report"
- "Hazmat" / "asbestos found" / "lead paint" / "mold discovered"
- "Contaminated soil" / "unexpected contamination"
- "Waste management" / "diversion rate" / "recycling report"
- "Dust control" / "air quality" / "PM10 reading"
- "Noise complaint" / "noise variance" / "noise monitoring"
- "Spill" / "diesel spill" / "chemical spill" / "environmental incident"
- "VOC tracking" / "low-emitting materials"
- "EPD" / "HPD" / "environmental product declaration"
- "Silica" / "silica exposure" / "Table 1"
- "Universal waste" / "hazardous waste" / "manifest"
- "Waste weight tickets" / "hauler certification"

---



## References

**Federal Regulations**:
- 40 CFR Part 61, Subpart M (NESHAP — Asbestos)
- 40 CFR Part 745 (EPA RRP Rule — Lead)
- 40 CFR Parts 260-268 (RCRA — Hazardous Waste)
- 40 CFR Part 273 (Universal Waste)
- 40 CFR Part 122 (NPDES — Clean Water Act)
- 29 CFR 1926.1153 (OSHA Silica Standard)
- 40 CFR Part 302 (CERCLA — Reportable Quantities)
- 40 CFR Part 355 (EPCRA — Emergency Planning)

**LEED Standards**:
- LEED v4.1 BD+C Rating System (USGBC)
- ANSI/SMACNA 008-2008 (IAQ Guidelines for Occupied Buildings Under Construction)
- SCAQMD Rules 1113, 1168 (VOC Limits)
- CARB ATCM (Composite Wood — Formaldehyde)

**Industry Standards**:
- EPA Construction General Permit (CGP)
- ASTM E1527 (Phase I ESA)
- ASTM E1903 (Phase II ESA)

---

End of Environmental Compliance Skill Documentation

## Hazardous Materials

### Asbestos (NESHAP Compliance)

**Regulatory Framework**: National Emission Standards for Hazardous Air Pollutants (NESHAP), 40 CFR Part 61, Subpart M.

**Pre-Demolition/Renovation Survey**:
- **Required** before any demolition or renovation of existing structures
- Must be conducted by a **state-certified asbestos inspector**
- Survey identifies all asbestos-containing materials (ACM) and presumed ACM (PACM)
- Building owner responsible for survey; results provided to contractor
- If ACM found: abatement required before demolition/renovation can proceed

**Common ACM Locations in Buildings**:
- Floor tiles (9"x9" vinyl tiles commonly contain asbestos)
- Pipe insulation and boiler wrapping
- Popcorn/textured ceiling coatings (pre-1980)
- Roof felts and mastics
- Transite (cement-asbestos) siding, panels, pipe
- Fireproofing spray (vermiculite-based)
- Joint compound and texture compounds
- Window glazing and caulk

**EPA Notification Requirements**:
- Notify EPA regional office (or delegated state agency) **10 working days** before demolition
- Notify **10 working days** before renovation if regulated amount of ACM involved
- Regulated amount: >260 linear feet of pipe insulation, >160 SF of surfacing material, or >35 CF of other ACM

**Abatement Procedures**:
1. Area isolation (negative air pressure enclosure)
2. Wet methods (keep material saturated to prevent fiber release)
3. HEPA-filtered negative air units running continuously
4. Workers in Tyvek suits, half-face or full-face respirators with P100 cartridges
5. Decontamination unit at enclosure exit (equipment room, shower, clean room)
6. Waste double-bagged in labeled 6-mil poly bags
7. Air monitoring during and after abatement (PCM or TEM analysis)
8. Clearance testing: <0.01 fibers/cc by PCM (aggressive air sampling)
9. Disposal at licensed asbestos landfill with proper manifesting

> **Cross-Reference**: For detailed asbestos identification and field procedures, see `references/hazmat-awareness-guide.md`.

### Lead Paint (RRP Rule Compliance)

**Regulatory Framework**: EPA Renovation, Repair, and Painting Rule (40 CFR 745).

**Applicability**: Pre-1978 buildings (residential or child-occupied facilities).

**Testing Requirements**:
- Test with EPA-recognized test kit (XRF analyzer preferred) OR
- Assume all paint is lead-containing and follow RRP procedures
- Positive result: lead content > 1.0 mg/cm2 (XRF) or > 0.5% by weight (lab)

**EPA-Certified Renovator Requirements**:
- Firm must be EPA-certified (or state-certified where applicable)
- Certified renovator must be assigned to each job
- Renovator certification: 8-hour initial training, 4-hour refresher every 5 years
- Certified renovator trains and directs uncertified workers

**Containment Procedures**:
- Interior: 6-mil poly on floors, extending 6 feet beyond work area; seal doorways and HVAC vents
- Exterior: 6-mil poly ground cover extending 10 feet from building; vertical containment if wind
- HEPA vacuum all surfaces after work
- Wet scraping, wet sanding only (no dry methods)

**Prohibited Practices**:
- Open flame burning or torching of lead paint
- Power sanding, grinding, or needle gunning without HEPA vacuum attachment
- Operating a heat gun above 1100 degrees F
- Dry scraping more than 2 SF per room
- Using chemical paint strippers containing methylene chloride

**Clearance Standards**:
- Floors: < 10 ug/SF (micrograms per square foot)
- Interior window sills: < 100 ug/SF
- Window troughs: < 400 ug/SF
- Clearance by certified lead inspector or risk assessor (NOT the renovator)

### Mold Prevention During Construction

**Source Control Strategy**:

| Phase | Risk | Prevention |
|-------|------|------------|
| Foundation | Water intrusion through foundation walls | Waterproofing, drainage, dewatering |
| Framing | Rain exposure to framing lumber | Dry-in within 72 hours of framing; cover materials |
| Drywall | Moisture trapped behind finished walls | Install after building is dried-in; verify moisture content < 15% |
| MEP rough-in | Condensation on cold pipes and ducts | Insulate before HVAC startup; control humidity |
| Finishes | Humidity during cure of paint, joint compound | Ventilate during application; dehumidify |

**Material Storage Requirements**:
- All absorptive materials stored off ground on pallets or dunnage (minimum 4 inches)
- Cover with waterproof tarps or plastic sheeting
- Store in enclosed area after dry-in when possible
- Drywall, insulation, ceiling tile: store inside only after building is weather-tight
- Verify moisture content with pin-type meter before installation (wood < 19%, drywall < 1%)

**Mold Discovery Response Protocol**:
1. **Stop work** in affected area immediately
2. **Isolate area** with plastic sheeting to prevent spore spread
3. **Notify PM and owner** — mold remediation is typically owner's responsibility
4. **Hire Indoor Environmental Professional (IEP)** to assess extent and species
5. **Develop remediation plan** per IEP recommendations
6. **Do not attempt cleanup** without professional guidance (can spread contamination)
7. **Document** with photos, moisture readings, timeline
8. **Post-remediation verification** by IEP before work resumes

### Contaminated Soil Procedures

**Phase I/II ESA Awareness**:
- Phase I Environmental Site Assessment: historical review (no sampling)
- Phase II ESA: soil and groundwater sampling if Phase I identifies potential contamination
- Owner typically provides ESA results; superintendent should review for known contamination

**Unexpected Contamination Discovery Protocol**:
```
STOP WORK in affected area
    │
    ├─ Secure area (barricade, signage)
    │
    ├─ Notify PM and project owner immediately
    │
    ├─ Contact environmental consultant
    │
    ├─ Do NOT attempt to remove or handle unknown material
    │
    ├─ Document: photos, location (GPS if possible), depth, visual description
    │   - Color, odor, staining pattern, container/debris type
    │   - Approximate volume
    │
    ├─ If petroleum sheen on water: deploy absorbent booms around affected area
    │
    └─ Await consultant direction before resuming work
```

**Indicators of Contaminated Soil**:
- Unusual color (dark staining, discoloration different from surrounding soil)
- Chemical odor (petroleum, solvent, chemical smell)
- Buried drums, tanks, containers, or debris
- Petroleum sheen on groundwater
- Stressed or dead vegetation in localized area
- Fill material with debris, ash, or industrial waste

**Excavation and Disposal of Contaminated Soil**:
- Soil testing required to classify waste (characteristic or listed hazardous waste)
- Manifest required for all contaminated soil transport (EPA Form 8700-22)
- Disposal at permitted facility (RCRA Subtitle C for hazardous; Subtitle D for non-hazardous)
- Air monitoring during excavation if volatile contaminants suspected
- Worker PPE: Tyvek, nitrile gloves, respiratory protection per exposure level

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


