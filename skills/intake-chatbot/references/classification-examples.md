# Classification Examples

Training examples for the intake classifier. Each example shows raw input and the correct classification.

> **Note**: These examples show how to CLASSIFY input into report sections. For how to TRANSFORM classified input into professional report language, see `language-standards.md`.

## Single-Section Examples

### Weather
| Input | Section | Key Data |
|---|---|---|
| "35 degrees this morning" | weather | temp: 35°F, time: morning |
| "rained from 8 to noon" | weather | conditions: rain, duration: 8AM-12PM |
| "wind is crazy today, 30mph gusts" | weather | wind: 30 mph gusts |
| "site is a mud pit after last night" | weather | site_impact: wet/muddy conditions |
| "perfect day out there" | weather | conditions: clear, impact: none |
| "frozen ground, couldn't dig" | weather | conditions: frozen, impact: major, delay |
| "hot as hell, 95 degrees by lunch" | weather | temp: 95°F, time: noon |
| "snowed about 2 inches overnight" | weather | conditions: snow, accumulation: 2" |

### Crew / Work
| Input | Section | Key Data |
|---|---|---|
| "Walker had 6 guys" | crew | sub: Walker, headcount: 6 |
| "poured footings today" | crew | work: concrete placement, type: footings |
| "electricians pulling wire on 2" | crew | trade: electrical, work: wire pull, location: Level 2 |
| "3 iron workers setting rebar at grid C" | crew | trade: iron workers, headcount: 3, work: rebar, location: Grid C |
| "nobody from the plumber today" | crew | trade: plumbing, headcount: 0, note: absent |
| "framing crew knocked out the whole north wall" | crew | trade: framing, work: wall framing, location: north |
| "concrete guys stripped forms on the west side" | crew | trade: concrete, work: formwork removal, location: west |
| "HVAC running duct on level 2" | crew | trade: HVAC/mechanical, work: ductwork, location: Level 2 |

### Materials
| Input | Section | Key Data |
|---|---|---|
| "got a load of rebar" | materials | material: rebar |
| "concrete delivery at 9am, 4 trucks" | materials | material: concrete, time: 9AM, quantity: 4 trucks |
| "wrong size pipe showed up" | materials | material: pipe, condition: incorrect |
| "lumber delivery, everything looked good" | materials | material: lumber, condition: good |
| "12 tons of structural steel from fabricator" | materials | material: structural steel, quantity: 12 tons |
| "drywall came in, stacked it on level 2" | materials | material: drywall, location: Level 2 |
| "short 2 bundles on the rebar order" | materials | material: rebar, issue: short shipment |

### Equipment
| Input | Section | Key Data |
|---|---|---|
| "excavator broke down" | equipment | equipment: excavator, status: down |
| "crane is set up on the NE corner" | equipment | equipment: crane, location: NE corner, status: active |
| "roller ran 8 hours" | equipment | equipment: roller, hours: 8, status: active |
| "bobcat just sitting there all day" | equipment | equipment: skid steer, status: idle |
| "new generator mobilized this morning" | equipment | equipment: generator, status: mobilized |
| "pump ran all night for dewatering" | equipment | equipment: pump, work: dewatering, status: active |

### Schedule
| Input | Section | Key Data |
|---|---|---|
| "we're at about 20%" | schedule | percent_complete: 20% |
| "foundation should be done Friday" | schedule | milestone: foundation complete, target: Friday |
| "steel delivery pushed to next week" | schedule | delay: steel delivery, type: material |
| "ahead of schedule on framing" | schedule | status: ahead, activity: framing |
| "concrete pour got pushed to Monday" | schedule | delay: concrete pour, new_date: Monday |
| "starting MEP rough-in next week" | schedule | upcoming: MEP rough-in, timing: next week |

### Inspections
| Input | Section | Key Data |
|---|---|---|
| "inspector passed the footings" | inspections | type: footing inspection, result: pass |
| "owner walked the site at 2" | inspections | type: visitor, person: owner, time: 2PM |
| "failed the compaction test" | inspections | type: compaction, result: fail |
| "architect came by to look at the storefront detail" | inspections | type: visitor, person: architect, purpose: storefront |
| "fire marshal inspection at 10" | inspections | type: fire marshal, time: 10AM |

### Notes
| Input | Section | Key Data |
|---|---|---|
| "talked to architect about the stair RFI" | notes | category: rfi, topic: stair detail |
| "pre-pour meeting tomorrow at 7" | notes | category: upcoming, event: pre-pour meeting |
| "need to get the crane permit" | notes | category: upcoming, item: crane permit |
| "owner wants us to work Saturday" | notes | category: directive, content: Saturday work |

## Multi-Section Examples

| Input | Sections |
|---|---|
| "Walker had 6 guys backfilling, got a load of fill from Martin Marietta, and the compaction tester passed us" | crew + materials + inspections |
| "rained until 10, then the concrete guys got 3 trucks and poured the east footings" | weather + crew + materials |
| "crane is down, waiting on a part, steel erection stopped until it's fixed" | equipment + schedule |
| "inspector failed the compaction, Walker has to re-do the lift and we'll retest tomorrow" | inspections + schedule + notes |
| "electricians pulled wire on level 2, plumber ran underground on the west side, 45 guys total on site" | crew (x2) + crew (total) |

## Edge Cases

| Input | Classification | Notes |
|---|---|---|
| "nothing happened today" | notes | Log as "No significant activity" |
| "same as yesterday" | notes | Flag: cannot replicate without knowing yesterday's data. Ask for specifics. |
| "the usual" | notes | Flag: too vague. Ask: "Can you give me the subs and headcounts?" |
| "see photos" | photos | Process uploaded images if present |
| "RFI 47 is holding up the east wall" | notes + schedule | RFI reference + schedule delay |

### Delays / Impacts

| Input | Section(s) | Key Data |
|---|---|---|
| "couldn't pour because of the cold" | delay_event + crew | delay_type: Weather, activities: concrete placement |
| "owner shut us down on the east wall" | delay_event + notes | delay_type: Owner-Directed, location: east wall |
| "waiting on the architect for the stair detail" | delay_event + notes | delay_type: Design/Spec, linked: RFI |
| "sprinkler sub didn't show, held up drywall" | delay_event + crew | delay_type: Sub Performance, sub: sprinkler contractor |
| "can't work in the south wing, no permit yet" | delay_event | delay_type: Permit/Regulatory, location: south wing |
| "hit rock where we expected soil" | delay_event + crew | delay_type: Differing Site Conditions |

### Claims-Mode Examples

| Input | Section | Key Data | Claims Detail |
|---|---|---|---|
| "Walker had 6 guys — John, Mike, Pete, Dave, Tom, and Rick — 7 to 3:30" | crew | sub: Walker, headcount: 6 | worker_names: [6 names], start: 7:00 AM, end: 3:30 PM |
| "crane was on standby 4 hours waiting for the steel truck" | equipment + delay_event | equipment: crane, status: Idle | standby_hours: 4, reason: material delivery delay |
| "rebar showed up at 11:30, was supposed to be here at 8" | materials + delay_event | material: rebar, delivery: late | scheduled: 8:00 AM, actual: 11:30 AM, variance: 3.5 hrs |
