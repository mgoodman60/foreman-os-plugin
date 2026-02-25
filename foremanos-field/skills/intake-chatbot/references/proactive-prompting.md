# Proactive Prompting Rules

Smart follow-up questions based on what's been logged vs. what's typically expected in a complete daily report.

## Gap Analysis Prompting

After the user has logged 3+ entries, the system can start noticing gaps. These prompts are low-priority — only ask at natural breaks in the conversation.

### Section Coverage Gaps

If by mid-afternoon (or after 5+ entries) the following are missing:

| Missing Section | Prompt (only if user seems done) |
|---|---|
| Weather | "What was the weather like today?" |
| Equipment | "Any equipment to note today?" |
| Schedule | "Any schedule updates or milestones to mention?" |
| Visitors/Inspections | "Any visitors or inspections today?" |
| Notes | "Anything else worth documenting?" |

### Never Prompt For
- Materials (no delivery is normal on many days)
- Photos (not always available or relevant)
- Safety (only prompt if safety-sensitive work was documented)
- SWPPP (only prompt if rain was documented)

## Time-Based Prompting

### Morning (before 10 AM)
- If first /log of the day: ask about weather
- If weather provided: acknowledge and wait for more

### Midday (10 AM - 2 PM)
- Normal logging period, no proactive prompts unless auto-context triggers fire

### Afternoon (after 2 PM)
- If fewer than 3 entries: "Slow day? Anything to log?"
- If no weather logged: "What was the weather like today?"

### End of Day (after 4 PM)
- If user logs something: "Almost done for the day? Run /daily-report when you're ready — it'll show you a summary of what's logged before generating."

## Intelligence-Driven Prompting

### Sub Attendance
If the project has scheduled subs and some haven't been logged:
- Don't list them all — that's annoying
- After the user seems done logging crew: "Was [most notable missing sub] on site? They're scheduled this week."
- At most prompt about ONE missing sub per session

### Milestone Awareness
If a milestone is within 5 days:
- When the user logs schedule info: "FYI — [milestone] is [X] days out. On track?"
- If they already mentioned it: don't repeat

### Inspection Reminders
If hold-point work was logged (concrete, compaction, etc.) and no inspection was documented:
- "Was there an inspection for [work type]? It's a hold point per the spec."
- Only ask once per work type per day

## Prompting Etiquette

1. **One prompt at a time** — never stack questions
2. **Accept silence** — if the user doesn't respond to a prompt, don't repeat it
3. **Accept dismissals** — "no", "nah", "nope", "skip", "nothing" all mean stop asking
4. **Time your prompts** — ask at natural pauses, not in the middle of a data dump
5. **Prioritize** — safety prompts > inspection prompts > coverage gap prompts
6. **Track what you've asked** — never ask the same category twice in a session
