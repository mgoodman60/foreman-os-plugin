---
name: rag-system
description: Construction document RAG architecture with multi-pass retrieval, scoring, and intelligence enrichment. Use when working on document search, context building, or RAG pipeline.
---

# RAG System

## When to Use This Skill
- Modifying document retrieval or search behavior
- Tuning relevance scoring or keyword matching
- Working on the context builder for chat
- Adding new query intent types or retrieval strategies
- Debugging "wrong document found" issues
- Extending Phase A/B/C intelligence integration

## Architecture Overview

```
User Query
    │
    ├── Query Classification (classifyQueryIntent)
    │     └── 9 types: requirement, measurement, counting, location,
    │         room_specific, mep, takeoff, daily_report, general
    │
    ├── Primary Retrieval (retrieveRelevantDocuments)
    │     ├── Project isolation (MUST filter by projectSlug)
    │     ├── Role-based access (admin/client/guest)
    │     ├── Keyword extraction with synonym expansion
    │     └── 1000+ point scoring system
    │
    ├── Enhanced Retrieval (twoPassRetrieval)
    │     ├── Pass 1: Precision (exact identifiers)
    │     ├── Pass 2: Notes-first (requirements)
    │     └── Pass 3: Context (keyword matching)
    │
    ├── Cross-Reference Bundling (bundleCrossReferences)
    │     └── Door/window tags, detail callouts, schedule refs
    │
    ├── MEP Retrieval Ordering (mepRetrievalOrder)
    │     └── Schedule → Notes → Plan → Diagram → Spec
    │
    └── Intelligence Enrichment
          ├── Phase A: Title blocks, legends, scales, drawing types
          ├── Phase B: Callouts, dimensions, annotations, symbols
          └── Phase C: Spatial correlation, MEP intelligence
```

## Core Patterns

### Project Isolation (Critical Security Pattern)

```typescript
// lib/rag/document-retrieval.ts — ALWAYS filter by project first
if (projectSlug) {
  const projects = await prisma.project.findMany({
    where: { slug: projectSlug },
    select: { id: true }
  });
  whereClause.projectId = { in: projects.map((p) => p.id) };
} else {
  return { chunks: [], documentNames: [] };  // No project = no results
}
```

### Role-Based Access Control

```typescript
if (userRole === 'guest') {
  whereClause.accessLevel = 'guest';
} else if (userRole === 'client') {
  whereClause.accessLevel = { in: ['client', 'guest'] };
}
// Admin: no accessLevel filter (sees everything)
```

### Relevance Scoring System

The scoring engine in `calculateRelevanceScore()` uses additive scoring:

| Scoring Factor | Points | Cap |
|---------------|--------|-----|
| Exact phrase match | 150 | - |
| Plans.pdf document | 60 | - |
| Construction phrase match | 50-95 | per phrase |
| Schedule/legend on counting query | 100 | - |
| Tabular data on counting query | 60 | - |
| Measurement patterns | 15-30 each | 150 total |
| Keyword proximity (within 10 words) | 0-30 | per pair |
| Individual keyword match | 12 | per occurrence |
| Domain-specific terms | 8-25 | per term |
| Sheet number references | 40 | per sheet + discipline boost |
| Notes section patterns | 25-90 | capped at 3x per pattern |
| Uppercase content (>40%) | 30 | - |

### Keyword Extraction with Synonyms

```typescript
// lib/rag/document-retrieval.ts — extractKeywords()
const synonyms: Record<string, string[]> = {
  'footer': ['footing', 'footer', 'footings', 'foundation', 'base'],
  'rebar': ['rebar', 'reinforcement', 'reinforcing', 'steel', 'bar'],
  'hvac': ['hvac', 'mechanical', 'heating', 'cooling', 'ventilation'],
  'receptacles': ['receptacles', 'outlets', 'duplex', 'plug'],
  // 60+ construction synonym groups
};
```

### Query Intent Classification

```typescript
// lib/rag/query-classification.ts — classifyQueryIntent()
interface QueryIntent {
  type: 'requirement' | 'measurement' | 'counting' | 'location' |
        'room_specific' | 'mep' | 'takeoff' | 'daily_report' | 'general';
  requiresNotes: boolean;       // Should fetch notes sections
  requiresCrossRef: boolean;    // Should bundle cross-references
  requiresRegulatory: boolean;  // Should fetch regulatory docs
  mepTrade?: 'hvac' | 'plumbing' | 'electrical' | 'fire_alarm';
  roomNumber?: string;
  isTakeoff?: boolean;
  takeoffScope?: string;
}
```

### Two-Pass Retrieval Strategy

```typescript
// lib/rag/retrieval-strategies.ts — twoPassRetrieval()
// Pass 1: Precision — exact identifiers (sheet numbers, door tags, equipment tags)
const identifiers = extractIdentifiers(query);  // "S-001", "D-101", "AHU-1"

// Pass 2: Notes-first — if query requires specifications/requirements
// Searches for: GENERAL NOTES, STRUCTURAL NOTES, SHALL, REQUIRED

// Pass 3: Context — keyword matching with expanded synonyms
const keywords = extractKeywords(query);
```

### Cross-Reference Bundling

```typescript
// lib/rag/retrieval-strategies.ts — bundleCrossReferences()
// Scans existing chunks for cross-reference patterns:
// - Door/window marks: /\b[DW]-?\d{1,3}\b/gi
// - Detail callouts: /\b\d+\/[A-Z]-?\d{1,3}\b/gi
// - "See schedule" references
// Then fetches related chunks from the database
```

### MEP-Specific Retrieval Order

For MEP queries, chunks are reordered by priority:
1. Schedule rows (equipment, fixture, panel, lighting)
2. System keynotes and general notes
3. Plan views with equipment tags
4. Diagrams (riser, isometric, one-line, schematic)
5. Specification references

### Intelligence Enrichment Phases

**Phase A** — Title blocks, legends, scales, drawing types:
```typescript
enrichWithPhaseAMetadata(chunks, projectSlug)
// Adds: titleBlock data, legend entries, dimension data, discipline
```

**Phase B** — Callouts, dimensions, annotations:
```typescript
retrievePhaseBContext(query, projectSlug, chunks)
// Adds context sections: DETAIL CALLOUTS, EXTRACTED DIMENSIONS,
// ANNOTATIONS & REQUIREMENTS, SYMBOL DEFINITIONS
```

**Phase C** — Spatial and MEP intelligence:
```typescript
generateEnhancedContext(query, projectSlug, chunks, corrections)
// Adds: SPATIAL INTELLIGENCE (grid references, sheet matches)
// Adds: MEP INTELLIGENCE (system elements, routing)
```

## Configuration

### Key Files
| File | Purpose |
|------|---------|
| `lib/rag/document-retrieval.ts` | Primary retrieval, scoring, keyword extraction |
| `lib/rag/retrieval-strategies.ts` | Two-pass retrieval, cross-ref bundling, MEP ordering |
| `lib/rag/query-classification.ts` | Query intent detection, identifier extraction |
| `lib/rag/intelligence-queries.ts` | Phase A/B/C intelligence integration |
| `lib/rag/core-types.ts` | DocumentChunk, ChunkMetadata, ScoredChunk types |
| `lib/rag/types.ts` | EnhancedChunk, TakeoffItem, SymbolLegend, etc. |
| `lib/rag.ts` | Barrel re-export (5 modules) |
| `lib/rag-enhancements.ts` | Barrel re-export (14 modules) |
| `lib/chat/processors/context-builder.ts` | Chat pipeline RAG orchestration |

### RAG Module Inventory (25 files in `lib/rag/`)

| Module | Purpose |
|--------|---------|
| `core-types.ts` | Base types from rag.ts |
| `types.ts` | Enhanced types from rag-enhancements.ts |
| `document-retrieval.ts` | Primary retrieval + scoring |
| `retrieval-strategies.ts` | Two-pass, cross-ref, MEP ordering |
| `query-classification.ts` | Intent detection + identifier extraction |
| `intelligence-queries.ts` | Phase A/B/C context enrichment |
| `context-generation.ts` | Context prompt formatting |
| `regulatory-retrieval.ts` | Code/standard document retrieval |
| `mep-entities.ts` | MEP equipment tag patterns |
| `mep-coordination.ts` | MEP conflict detection |
| `compliance-checking.ts` | Code compliance analysis |
| `takeoff-extraction.ts` | Material takeoff generation |
| `takeoff-verification.ts` | Takeoff quality validation |
| `measurement-extraction.ts` | Dimension parsing |
| `scale-detection.ts` | Scale info extraction |
| `spatial-analysis.ts` | Grid-based spatial referencing |
| `symbol-legend.ts` | Symbol legend parsing |
| `symbol-learning.ts` | Adaptive symbol recognition |
| `abbreviations.ts` | Construction abbreviation dictionary |
| `diagram-analysis.ts` | One-line/riser diagram parsing |
| `system-topology.ts` | MEP system flow analysis |
| `isometric-views.ts` | Isometric view interpretation |
| `advanced-conflicts.ts` | Multi-system clash detection |
| `phase3-context.ts` | Phase 3C context assembly |
| `export-utilities.ts` | CSV/Excel export formatting |

## Anti-Patterns

- **Never return documents without project filtering** — cross-project leakage is a security violation
- **Never skip role-based access control** — guests must not see admin documents
- **Never hardcode scoring weights inline** — use the centralized scoring functions
- **Never fetch all chunks at once** — use `limit` parameter and pagination
- **Never ignore `skipForRag` metadata flag** — these chunks contain failed extractions

## Quick Reference

```typescript
import { retrieveRelevantDocuments } from '@/lib/rag/document-retrieval';
import { twoPassRetrieval, bundleCrossReferences } from '@/lib/rag/retrieval-strategies';
import { classifyQueryIntent, extractIdentifiers } from '@/lib/rag/query-classification';

// Basic retrieval
const { chunks, documentNames } = await retrieveRelevantDocuments(
  query, 'admin', 12, projectSlug
);

// Enhanced retrieval with two-pass
const { chunks, retrievalLog } = await twoPassRetrieval(
  query, projectSlug, 'admin', 12
);

// Query classification
const intent = classifyQueryIntent("how many receptacles on sheet E-101?");
// → { type: 'counting', requiresNotes: false, requiresCrossRef: true }
```
