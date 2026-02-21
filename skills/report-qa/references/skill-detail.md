# report-qa — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the report-qa skill.



## QA Output Format

Present findings to the user in three tiers:

### Flags (Must Address)
Issues that should be resolved before finalizing the report. These represent potential documentation gaps that could be problematic.

### Notes (Should Consider)
Items the user should be aware of but can choose to skip. These improve report quality but aren't critical.

### Passes (All Good)
Categories where everything checked out. Brief summary to show the QA ran and found no issues.

### Example Output

```
Report QA Complete — 2 flags, 3 notes

FLAGS:
• Cold weather concrete: Temperature hit 35°F at 7 AM. Concrete placement documented
  but no cold weather plan noted. Per Section 03 30 00, protection required below 40°F.
  → Add cold weather measures to the concrete work description?

• Missing sub: "Johnson Electric" not in sub directory. New sub?
  → Add to directory or correct the name?

NOTES:
• Foundation Complete milestone is 8 days away. Consider mentioning in Schedule Updates.
• No photos of today's compaction testing. Recommended for records.
• General Notes section is empty.

PASSES:
✓ All other subs match directory
✓ Schedule percent complete is consistent
✓ Inspection documented for backfill compaction
✓ Equipment status fully documented
```



## QA Data for Dashboard

Save QA results in the report history entry so the dashboard can track report quality over time:

```json
{
  "qa_results": {
    "report_type": "daily|weekly",
    "flags": 2,
    "notes": 3,
    "passes": 4,
    "categories_checked": ["subs", "weather_thresholds", "inspections", "schedule", "photos", "completeness", "swppp", "safety", "delay_documentation", "claims_compliance"],
    "flags_resolved": 1,
    "flags_skipped": 1
  }
}
```


