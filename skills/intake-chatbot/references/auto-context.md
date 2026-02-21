# Auto-Context Rules

When the user logs an entry, the system can proactively suggest related information that's commonly documented together. These are gentle prompts — never require a response.

## Context Triggers

### Crew Entry → Weather Check
If the first log entry of the day is about crew/work, and no weather has been logged:
"Got it. What's the weather like out there today?"

Only ask once per day. If the user ignores it, move on.

### Concrete Work → Temperature + Inspection
If concrete placement is logged:
- Check today's weather entries. If temp is below cold weather threshold: "Heads up — [temp] is below the cold weather threshold ([threshold]). Is a cold weather plan in effect?"
- If no pre-placement inspection logged: "Was there a pre-placement inspection before the pour?"

### Backfill/Compaction → Testing
If backfill or compaction work is logged:
- "Was a compaction test run on today's fill?"

### Equipment Down → Schedule Impact
If equipment is logged as down:
- "Is this causing any schedule impact?"

### Equipment Mobilized → Duration + Purpose
If new equipment is logged as mobilized or arriving for the first time:
- "New [equipment] on site — how long is it expected to be here?"

### Equipment Demobilized → Replacement
If equipment is logged as demobilized or leaving:
- "Is [equipment] being replaced, or is that phase of work complete?"

### Sub Missing → Reason + Impact
If a sub is expected based on schedule dates but hasn't been logged:
- After the third log entry of the day without that sub: "Was [sub name] on site today? They're scheduled to be here this week."
- If the user confirms absence: "Any reason they weren't here? (material delay, weather, manpower, scheduling, etc.)"
- If a reason is given: "Is this causing any delay to the schedule?"
- If delay confirmed → also classify as delay_event with type: Sub Performance
- Only prompt about ONE missing scheduled sub per session

### Delivery → Condition + Storage
If a material delivery is logged without condition info:
- "Material in good condition?"

### Inspection Fail → Next Steps
If an inspection is logged as failed:
- "What's the plan for the re-inspection?"

### Rain → SWPPP
If rain is logged in weather and the project has SWPPP data:
- If rainfall exceeds the SWPPP inspection trigger: "Rain triggered a SWPPP inspection per the plan ([threshold]). Was a BMP inspection conducted?"

### Work at Height → Safety
If work on upper floors or elevated areas is logged and safety zones exist:
- "Any fall protection notes for the work at [location]?"

## Prompting Behavior

- Ask at most ONE follow-up question per log entry
- Prioritize the most relevant prompt (safety > inspection > weather > other)
- Accept "no", "nah", "skip" as valid responses — log nothing and move on
- Never ask the same prompt twice in a day
- Keep prompts under 20 words when possible
