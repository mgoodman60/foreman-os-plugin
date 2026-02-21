---
name: field-reference
description: >
  Construction field reference knowledge base with 21 reference documents providing practical numbers, tolerances, decision frameworks, and best practices that superintendents need in the field. Covers heavy equipment selection and production rates, concrete operations (standard and advanced), structural steel, earthwork, stormwater BMPs, MEP coordination, fire protection, building envelope, site logistics, formwork and shoring, scaffolding, masonry, waterproofing systems, underground utilities, paving and flatwork, crane lift planning, construction surveying, temporary facilities, multi-story coordination, and cross-trade coordination. This is a reference skill — no dedicated command. Other skills and commands call into it, and superintendents can query it conversationally.
version: 1.0.0
---

# Field Reference Skill

## Overview

The Field Reference skill is the plugin's standalone construction knowledge base — practical field data that a superintendent needs when they don't have a spec book in hand. It contains the numbers, tolerances, rules of thumb, and decision frameworks that drive daily field decisions.

This skill is NOT a document extraction tool (that's document-intelligence). It's a knowledge base — the kind of information an experienced superintendent carries in their head.

## Reference Document Index

| Reference Document | What It Covers | When to Use |
|---|---|---|
| `references/equipment-selection-guide.md` | Excavators, dozers, cranes, loaders, compactors, pumps, generators, lifts — sizing rules, selection decision trees, rental specs, mobilization, production rate tables, hauling capacity, fleet balancing | Superintendent asks about equipment sizing, crane capacity, production rates, truck fleet sizing, or what machine to use for a task |
| `references/concrete-field-operations.md` | Slump ranges, air entrainment, cold/hot weather protocols, cylinder testing, pour cards, ACI 301/318 field requirements, common defects | Any concrete-related question: placement, testing, weather protection, mix design interpretation |
| `references/advanced-concrete-guide.md` | Post-tensioning, tilt-up, precast, mass concrete, architectural concrete, self-consolidating concrete, fiber-reinforced, underwater placement | Advanced concrete operations beyond standard CIP: specialty pours, PT stressing, tilt-up erection, precast connections |
| `references/structural-steel-field-guide.md` | Bolt torque (A325/A490), installation methods, erection tolerances, connections, weld inspection, piece mark tracking | Steel erection, bolt-up, inspection, connection type identification |
| `references/earthwork-compaction-guide.md` | Compaction standards by location, Proctor tests, moisture control, proof rolling, nuclear gauge, soil classification, swell/shrinkage | Earthwork operations, fill placement, subgrade prep, compaction testing |
| `references/bmp-field-guide.md` | Silt fence specs, inlet protection, stabilized entrance, concrete washout, erosion control by slope, SWPPP compliance, maintenance | Stormwater management, erosion control, SWPPP inspections, BMP installation/maintenance |
| `references/mep-coordination-guide.md` | Ceiling cavity depths, pipe sleeves, fire-stopping, electrical clearances, plumbing slopes, HVAC duct sizing, trade sequencing, ductwork/piping/electrical installation standards | MEP rough-in coordination, trade sequencing, above-ceiling work, code clearances, system installation verification |
| `references/fire-protection-field-guide.md` | Sprinkler spacing/coverage, fire-rated assemblies, penetration fire-stopping, standpipes, fire alarm systems, smoke control, emergency power integration, fire pump testing | Fire protection installation verification, fire-rated wall inspections, device spacing checks, alarm system commissioning |
| `references/building-envelope-guide.md` | Foundation waterproofing, roofing systems (TPO/EPDM/built-up/metal), flashing, rough openings, air/vapor barriers | Waterproofing, roofing, window/door installation, building envelope continuity |
| `references/site-logistics-guide.md` | Crane placement, material staging, temporary power, dewatering, dust control, traffic control, temporary fencing | Site setup, logistics planning, temporary facilities, environmental controls |
| `references/formwork-shoring-guide.md` | ACI 347 formwork design, formwork types (plywood, aluminum, engineered), shoring loads, reshoring, stripping times, inspection checklists | Formwork selection, shoring design verification, stripping time determination, multi-story reshoring |
| `references/scaffolding-guide.md` | Frame, system, tube-and-clamp, mast climbing, suspended scaffolds — load capacity, OSHA 1926.450-454, erection/inspection, tag system | Scaffold erection oversight, daily inspections, load capacity verification, competent person duties |
| `references/masonry-field-guide.md` | CMU types/sizes/grades, mortar types (M/S/N/O), bond patterns, grouting, rebar placement, brick veneer, stone anchoring, cold/hot weather masonry | Masonry installation, mortar selection, grouting operations, veneer systems, weather protection |
| `references/waterproofing-systems-guide.md` | Below-grade systems (bentonite, spray, sheet, crystalline), traffic coatings, plaza decks, joint sealants, air/vapor barriers, water testing | Waterproofing system selection, installation verification, leak testing, sealant selection |
| `references/underground-utilities-guide.md` | Water, sanitary, storm, gas, electric, telecom — trench specs, bedding/backfill (ASTM D2321), pipe materials, pressure testing, crossings | Utility installation, trench excavation, pipe bedding, pressure testing, utility crossings and separations |
| `references/paving-flatwork-guide.md` | Asphalt (HMA types, lift thickness, temperature, compaction), concrete flatwork (finishing, joints, FF/FL), ADA accessibility, curb/gutter | Paving operations, concrete flatwork finishing, joint layout, ADA compliance, seasonal restrictions |
| `references/crane-lift-planning-guide.md` | Lift Director responsibilities, critical lift criteria, pre-lift planning, rigging hardware/capacity, signal person requirements, crane inspections, multi-crane lifts | Lift planning, critical lift documentation, rigging selection, crane inspection verification, signal person coordination |
| `references/construction-surveying-guide.md` | Benchmark establishment, control networks, layout procedures (total station, GPS/RTK), staking, elevation verification, as-built surveys | Survey layout verification, benchmark checks, cut/fill calculations, as-built documentation, survey error resolution |
| `references/temporary-facilities-guide.md` | Temporary power (load calc, distribution, GFCI), temp water, heating/cooling, winter protection, dewatering systems, temporary enclosures | Temporary facility planning, winter protection, temp power sizing, dewatering selection, enclosure requirements |
| `references/multi-story-coordination-guide.md` | Floor-by-floor sequencing, vertical transportation, tower crane logistics, material hoisting, concrete pumping for high-rise, multi-trade stacking | Multi-story building coordination, vertical logistics, floor cycle planning, high-rise operations |
| `references/cross-trade-coordination-guide.md` | Pre-installation meetings, above-ceiling coordination, slab penetration management, sequence of operations, trade stacking rules, conflict resolution | Trade coordination meetings, above-ceiling rough-in sequencing, penetration layout, trade conflict resolution |

## How Other Skills/Commands Use This Skill

### Integration Pattern

When another command or skill needs field reference knowledge, it should read the relevant reference document from this skill. The lookup table above maps topics to files.

**Example integrations:**

| Calling Command/Skill | When | Which Reference to Read |
|---|---|---|
| `/morning-brief` | Surfacing today's activities with QC reminders | concrete-field-operations.md, structural-steel-field-guide.md (based on today's scheduled work) |
| `/morning-brief` | Weather threshold enrichment | concrete-field-operations.md (cold/hot weather), bmp-field-guide.md (rain triggers) |
| `/daily-report` | Enriching work descriptions with proper trade language | concrete-field-operations.md, structural-steel-field-guide.md, earthwork-compaction-guide.md |
| `/look-ahead` | Sequencing and constraint analysis | mep-coordination-guide.md (trade sequence), site-logistics-guide.md (crane/staging) |
| `report-qa` | Validating report accuracy against field standards | Any reference matching the day's work types |
| `/log` (intake-chatbot) | Enriching field observations with technical context | Based on observation topic |
| `/process-docs` | Cross-referencing extracted specs against field standards | concrete-field-operations.md (verify spec values), earthwork-compaction-guide.md (compaction reqs) |

### Conversational Queries

The superintendent can ask field reference questions at any time without running a command:

- "What size excavator do I need for a 12-foot trench?"
- "What's the cold weather concrete protocol?"
- "A325 bolt torque for 3/4 inch?"
- "Silt fence post spacing?"
- "Minimum sprinkler head distance from wall?"
- "Trade sequence for above-ceiling rough-in?"
- "Compaction requirement under footings?"

When Claude receives these questions, it should read the appropriate reference document and provide the specific answer with the source data.

## Maintenance Notes

- These references contain **industry-standard** data (ACI, AISC, NFPA, OSHA, EPA standards). They should be updated when code editions change.
- Project-specific requirements (from specs, geotech, etc.) always override these general references. The reference docs note this where applicable.
- The references are intentionally **practical, not academic** — they focus on what a superintendent needs to know in the field, not exhaustive code commentary.
