# Edge Cases

How to handle ambiguous, contradictory, or unusual input during field intake.

## Ambiguous Sub References

### Multiple Possible Matches
**Input**: "the steel guys"
**Problem**: Could be structural steel erectors OR miscellaneous metals sub

**Resolution**:
1. Check which subs are scheduled to be on site this week
2. Check recent report history — who's been showing up?
3. If still ambiguous: "Steel guys — do you mean [Iron Workers Inc.] or [Misc Metals LLC]?"
4. If only one steel-trade sub exists in the directory, use that one

### No Match At All
**Input**: "Johnson was on site"
**Problem**: No sub named Johnson in the directory

**Resolution**:
1. Log with the name as-is
2. Flag as unresolved: "I don't have a 'Johnson' in the sub directory. New sub, or different name?"
3. Accept whatever the user says and move on
4. If it's a new sub, add a note that /process-docs or /set-project should be updated

## Contradictory Information

### Same Entry, Same Session
**Input 1**: "Walker had 6 guys"
**Input 2** (later): "actually Walker had 4 guys and 2 were from Metro"

**Resolution**: Update the Walker entry to 4, add Metro entry with 2. Confirm: "Updated — Walker (4), Metro (2)."

### Contradicts Previous Day
**Input**: "foundation is 60% done"
**Previous report**: "foundation is 80% done"

**Resolution**: Log as stated. The QA step will catch the regression and flag it. Don't challenge the user during intake — they're in the field and may have context you don't.

### Duplicate Sub Entries

**Same Sub, Incremental Work**
- Input 1: "Walker had 6 guys doing backfill"
- Input 2 (later): "Walker also had 2 guys doing grading on the west side"
- Resolution: If locations differ, keep as separate line items. If same location, merge to 8 workers.

**Same Sub, Equipment vs Crew**
- Input 1: "Walker had 6 guys backfilling"
- Input 2: "Walker brought the excavator and the roller"
- Resolution: Crew entry stays in "crew"; equipment entries go to "equipment." Link by sub name but don't merge.

**Ambiguous Update vs Addition**
- Input 1: "Walker had 6 guys"
- Input 2: "Walker had 8 guys"
- Resolution: No qualifier → treat as CORRECTION (update to 8). With qualifier ("also", "plus") → treat as ADDITION. When ambiguous, ask.

## Vague Input

### Too Vague to Classify
**Input**: "it was a good day"
**Resolution**: Log in notes as "Productive day — no significant issues." Prompt: "Anything specific to document?"

**Input**: "same as yesterday"
**Resolution**: Cannot replicate without loading yesterday's data. Ask: "Can you give me the subs and headcounts? I want to make sure I get it right."

**Input**: "the usual crew"
**Resolution**: If recent report history shows a consistent crew: "Last report had [sub list with headcounts]. Same today?" If no history: "Who was on site?"

### Partial Information
**Input**: "poured concrete"
**Resolution**: Log what you know (concrete placement). Prompt ONE follow-up: "How much and where?"

If the user doesn't elaborate: log as-is and move on. The /daily-report command can fill gaps later.

## Time References

### Relative Time Conversion

| User Input | Default Time | Basis |
|---|---|---|
| "this morning" / "first thing" | 7:00 AM | Standard shift start |
| "mid-morning" | 9:30 AM | |
| "around noon" / "at lunch" | 12:00 PM | |
| "after lunch" | 1:00 PM | Standard lunch return |
| "mid-afternoon" | 2:30 PM | |
| "end of day" / "close of business" | 4:00 PM | Standard shift end |
| "late afternoon" | 3:30 PM | |

**Override**: If `project-config.json` defines `shift_start` or `shift_end`, use those as the basis. All other relative times shift proportionally.

**Rule**: These are defaults for when the user gives no specific time. If the user provides any specific time ("around 2", "about 10:30"), use their time.

### Ambiguous Dates
- "yesterday" → previous calendar day
- "last week" → flag: this is for today's report. Ask: "Is this something that happened today, or are you noting something from last week?"
- "tomorrow" → log as upcoming/planned, not completed work

## Numbers

### Headcount Confusion
**Input**: "Walker 6, Metro 8, 45 total"
**Problem**: Walker (6) + Metro (8) = 14, but total is 45. That means there are more subs.
**Resolution**: Log Walker and Metro. Note total of 45. Prompt: "45 total — who else was on site besides Walker and Metro?"

### Quantity Without Context
**Input**: "12 loads today"
**Resolution**: Check recent context. If a material was just mentioned, apply to that. Otherwise ask: "12 loads of what?"

## Photos Without Context

### Photo Uploaded With No Text
**Resolution**: Analyze the image, generate a caption, classify into a section. Confirm: "Got a photo of [what I see]. That look right?"

### Photo Contradicts Text
**Input**: "here's the backfill" + photo clearly shows concrete formwork
**Resolution**: Trust the user's label. They know what they're documenting. Caption can note both: "Formwork area adjacent to backfill operations at [location]."

## After-Hours Logging

### Entries After Normal Work Hours
If a log entry comes in after 6 PM:
- Accept it normally — some supers log at the end of the day or from home
- Don't comment on the timing

### Entries for a Different Day
If the user says "forgot to log yesterday — Walker had 5 guys doing grading"
- If there's an intake log for yesterday that hasn't been consumed: add to it
- If yesterday's report was already generated: tell them to use /amend-report
- If no yesterday log exists: create one for that date

## System Errors

### Can't Read Config File
- Log entries without enrichment. Note: "Logging without project intelligence — sub names and locations won't be auto-resolved."

### Intake File Corrupted
- Start a fresh intake file for today
- Tell the user: "Starting a fresh log for today. If you had previous entries, you may need to re-log them."
