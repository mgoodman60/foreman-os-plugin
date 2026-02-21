---
name: prompt-patterns
description: Construction-domain prompt engineering patterns including discipline-specific extraction, JSON mode, and system message conventions. Use when writing prompts for LLM calls or extraction tasks.
---

# Prompt Patterns

## When to Use This Skill
- Writing new LLM prompts for construction document analysis
- Adding extraction prompts for new document types
- Configuring JSON mode output across providers
- Building system messages for the chat pipeline
- Extending discipline-specific extraction categories

## Architecture Overview

```
Prompt Selection
    │
    ├── Chat Pipeline ──► System message + RAG context + user query
    │     └── lib/chat/processors/context-builder.ts
    │
    ├── Vision Extraction ──► Discipline-specific prompts
    │     └── lib/discipline-prompts.ts (8 disciplines)
    │
    ├── Interpretation ──► Text-only validation prompts
    │     └── lib/document-processor-batch.ts
    │
    └── Feature Extraction ──► Domain-specific prompts
          └── Various lib/ service modules
```

## Core Patterns

### Discipline-Specific Extraction Prompts

ForemanOS uses 8 discipline-specific prompts in `lib/discipline-prompts.ts`:

```typescript
export function getDisciplinePrompt(
  discipline: string,    // 'Architectural', 'Structural', etc.
  drawingType: string,   // 'floor_plan', 'schedule', etc.
  fileName: string,
  pageNum: number,
  symbolHints: string    // Pre-loaded symbol context
): string
```

| Discipline | Sheet Prefix | Key Extraction Priorities |
|-----------|-------------|--------------------------|
| Architectural | A- | Rooms, doors, windows, wall types, keynotes |
| Structural | S- | Members, rebar, elevations, concrete strength |
| Mechanical | M- | Equipment tags, ductwork, CFM values |
| Electrical | E- | Panels, circuits, receptacles, lighting |
| Plumbing | P- | Fixtures, pipe sizes, GPM, waste/vent |
| Civil | C- | Grading, utilities, stormwater |
| Schedule | Various | Tabular data extraction |
| Generic | Any | Fallback for unclassified sheets |

### Prompt Structure Convention

All extraction prompts follow this structure:

```
[DISCIPLINE] PLAN EXTRACTION - Page [N] of [filename]

You are analyzing a [discipline] drawing.

EXTRACT IN THIS PRIORITY ORDER:

1. SHEET IDENTIFICATION:
   - Sheet number, title, scale(s)

2. [HIGHEST PRIORITY CATEGORY]:
   - Domain-specific items with examples

3-N. [ADDITIONAL CATEGORIES BY PRIORITY]

RESPOND WITH VALID JSON:
{
  "sheetNumber": "",
  "discipline": "[Discipline]",
  "drawingType": "[type]",
  // ... structured fields
}
```

Every prompt ends with:
```
IMPORTANT: Extract EVERYTHING visible. Omit categories with no data rather than including empty arrays.
```

### JSON Mode Across Providers

```typescript
// OpenAI: Native response_format
const result = await callLLM(messages, {
  model: SIMPLE_MODEL,
  response_format: { type: 'json_object' },
});

// Claude: Injected via system prompt (handled by callAnthropic)
// When response_format.type === 'json_object', the provider adds:
// "You must respond with valid JSON only. No markdown, no explanation, no code fences."
```

Files using JSON mode: `lib/progress-detection-service.ts`, `lib/earthwork-extractor.ts`, `lib/dimension-intelligence.ts`, `lib/annotation-processor.ts`, `lib/scale-data-extractor.ts`, `lib/detail-callout-extractor.ts`, `lib/daily-report-enhancements.ts`.

### System Message Pattern

System messages are extracted and handled differently per provider:

```typescript
// OpenAI: system role in messages array
messages: [
  { role: 'system', content: systemPrompt },
  { role: 'user', content: userMessage },
]

// Claude: system field at top level (extracted by callAnthropic)
{
  system: systemPrompt,
  messages: [
    { role: 'user', content: userMessage },
  ],
}
```

### Chat System Message Construction

The chat pipeline builds system messages with RAG context in `lib/chat/processors/context-builder.ts`:

```
Base system prompt (construction AI assistant identity)
  + RAG document context (scored chunks with citations)
  + Phase A context (legends, scales, drawing types)
  + Phase B context (callouts, dimensions, annotations)
  + Phase C context (spatial, MEP intelligence)
  + Daily report context (if daily_report query type)
  + Web search results (if enabled)
  + Citation instructions
```

### Context Prompt Generation

```typescript
// lib/rag/document-retrieval.ts — generateContextPrompt()
export function generateContextPrompt(chunks: DocumentChunk[]): string {
  let prompt = 'Based on the following project documents:\n\n';
  for (const chunk of chunks) {
    const docName = chunk.metadata?.documentName || 'Unknown Document';
    const pageRef = chunk.pageNumber ? ` (Page ${chunk.pageNumber})` : '';
    const sheetRef = isPlans ? ` [Sheets: ${sheetNumbers.join(', ')}]` : '';
    prompt += `[${docName}${pageRef}${sheetRef}]\n${chunk.content}\n\n`;
  }
  prompt += 'IMPORTANT: When providing information from Plans.pdf, ALWAYS cite the sheet number...';
  return prompt;
}
```

### Vision Prompt Parameters

Standard vision extraction parameters:

```typescript
// Extraction (vision + image)
{ model: VISION_MODEL, max_tokens: 8000, temperature: 0.1 }

// Interpretation (text-only validation)
{ model: VISION_MODEL, max_tokens: 4000, temperature: 0.1 }

// Chat (streaming)
{ model: selectedModel, temperature: 0.3, max_tokens: 4000 }

// Gemini extraction
{ maxOutputTokens: 8192, temperature: 0.1, thinkingLevel: LOW }
```

### Symbol Context Injection

Prompts can include pre-loaded symbol context from the project's legend library:

```typescript
const prompt = getDisciplinePrompt(discipline, drawingType, fileName, pageNum, symbolHints);
// symbolHints is appended after the main prompt body
// Format: "KNOWN SYMBOLS FROM PROJECT LEGENDS:\n- SYM1: Description\n- SYM2: ..."
```

### RAG Instruction Prompts

Phase A and B add structured instructions to the system prompt:

```typescript
// Phase A instructions (lib/rag/intelligence-queries.ts)
getPhaseARAGInstructions()
// Rules 30-32: Title block intelligence, legend/symbol recognition, sheet navigation

// Phase B instructions
getPhaseBRAGInstructions()
// Rules 33-37: Detail callouts, dimension intelligence, annotations, symbols, visualization
```

These include embedded JSON card formats for rich responses:
```json
// Callout card
{"callouts":[{"type":"detail","detailNumber":"3","sheetReference":"A-201"}]}

// Dimension card
{"dimensions":[{"originalText":"12'-6\"","value":12.5,"unit":"ft","critical":true}]}

// Annotation card
{"annotations":[{"type":"warning","text":"Fire-rated assembly required","priority":"critical"}]}
```

## Configuration

### Key Files
| File | Purpose |
|------|---------|
| `lib/discipline-prompts.ts` | 8 discipline-specific extraction prompts |
| `lib/document-processor-batch.ts` | Interpretation prompt templates |
| `lib/chat/processors/context-builder.ts` | Chat system message construction |
| `lib/rag/document-retrieval.ts` | Context prompt generation |
| `lib/rag/intelligence-queries.ts` | Phase A/B RAG instruction prompts |

## Anti-Patterns

- **Never use `response_format: json_object` with Claude directly** — it is handled by `callAnthropic()` via system prompt injection
- **Never omit the "Extract EVERYTHING" suffix** — extraction prompts need it to prevent sparse outputs
- **Never hardcode temperature above 0.1 for extraction** — higher values cause inconsistent JSON
- **Never put system messages in the messages array for Claude** — they must be at the top level
- **Never skip symbol hints when available** — they significantly improve extraction accuracy

## Quick Reference

```typescript
import { getDisciplinePrompt } from '@/lib/discipline-prompts';
import { generateContextPrompt } from '@/lib/rag/document-retrieval';
import { getPhaseARAGInstructions, getPhaseBRAGInstructions } from '@/lib/rag/intelligence-queries';

// Get discipline prompt for vision extraction
const prompt = getDisciplinePrompt('Architectural', 'floor_plan', 'Plans.pdf', 3, symbolHints);

// Generate context for chat
const context = generateContextPrompt(retrievedChunks);

// Get RAG instruction sets
const phaseAInstructions = getPhaseARAGInstructions();
const phaseBInstructions = getPhaseBRAGInstructions();
```
