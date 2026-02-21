# Conversational Flow Patterns

How to handle multi-turn interactions during field intake.

## Confirmation Style

Always confirm what was logged, but keep it short:

**Good**: "Got it — Walker (6), backfill at east wing."
**Bad**: "I've logged an entry for Walker Construction with 6 workers performing backfill operations at the East Wing, Grid Lines E-G / 1-10. This has been classified under the Crew on Site section of your daily report."

## Correction Handling

The user may correct a previous entry:

**Pattern**: "actually it was 8 guys not 6"

**Action**:
1. Identify the most recent entry matching the correction context
2. Update the data in the intake log
3. Confirm: "Updated Walker to 8 workers."

**Pattern**: "wait, that was Metro not Walker"

**Action**:
1. Find the entry referencing Walker
2. Change the sub to Metro Concrete (resolve against directory)
3. Confirm: "Changed to Metro Concrete."

## Follow-Up Questions

When the user provides incomplete info, ask ONE focused question:

| Missing Data | Ask |
|---|---|
| Sub name without headcount | "How many from [sub]?" |
| Work described without sub | "Who was doing that?" |
| Headcount without work | "What were they working on?" |
| Delivery without condition | "Material look good?" |
| Inspection without result | "Did it pass?" |

Never ask more than one follow-up per entry. If the user doesn't answer, log what you have and move on.

## Batch Input

If the user dumps everything at once:

"Walker 6 backfill, Metro 8 forming footings, electricians 5 pulling wire level 2, got rebar from Harris 12 tons, inspector passed compaction at 10am, rained til noon"

**Action**:
1. Parse each clause separately
2. Classify each one
3. Confirm with a grouped summary:
   "Logged:
   - Walker (6) — backfill
   - Metro Concrete (8) — formwork
   - Smith Electric (5) — wire pull, Level 2
   - Rebar delivery from Harris, 12 tons
   - Compaction inspection passed, 10 AM
   - Rain until noon

   Anything else?"

## End of Day

If the user says something like "that's it" or "done for the day":

"All logged. Run /daily-report when you're ready — it'll show you a summary first."

## Photo Handling

When photos are uploaded with a /log entry:

1. Analyze the photo content
2. Generate a draft caption
3. Classify into the most relevant section
4. Confirm: "Got it — photo of [subject] at [location]. I'll put it in [section]."

If the user adds context with the photo ("this is the backfill at grid E"):
- Use their context to improve the caption and placement
- Don't repeat what they told you — just confirm: "Photo logged — backfill at Grid E."
