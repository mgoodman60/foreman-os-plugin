---
name: vision-pipeline
description: Multi-provider vision processing with three-pass pipeline and smart routing for construction documents. Use when working on document processing, vision extraction, or image analysis.
---

# Vision Pipeline

## When to Use This Skill
- Modifying document processing or vision extraction
- Debugging failed page extractions
- Adding new extraction categories
- Tuning quality thresholds or timeouts
- Working on the three-pass pipeline (Gemini + Opus)
- Adding smart routing logic for different document types

## Architecture Overview

### Single-Page Vision (Chat/Ad-hoc)
```
analyzeWithLoadBalancing(image, prompt)
    │
    ├── Round-robin primary ──► callClaudeOpusVision() or callGPT52Vision()
    │                              ├── Quality check (score >= 50)
    │                              └── Return if passed
    │
    └── Fallback ──► analyzeWithMultiProvider()
                        ├── Opus (3 retries, 600s timeout)
                        └── GPT-5.2 (3 retries, 90s timeout)
```

### Batch Document Processing (Three-Pass Pipeline)
```
analyzeWithThreePassPipeline(pdfBuffer, prompt, processorType, page)
    │
    ├── Pass 1: callGeminiPro3Vision() ──► Gemini 3 Pro Preview
    │     Fast visual extraction, ThinkingLevel.LOW, 8192 tokens
    │
    ├── Pass 2: callGeminiVision() ──► Gemini 2.5 Pro
    │     Validates Pass 1, fills gaps, thinkingBudget: 1024
    │
    ├── Pass 3: callOpusInterpretation() ──► Claude Opus 4.6
    │     Text-only validation, correction, enrichment
    │     Fallback: callGPT52Interpretation() ──► GPT-5.2
    │
    └── Full fallback: analyzeWithSmartRouting()
          Routes by document classification (visual/text-heavy/mixed)
```

### Smart Routing
```
analyzeWithSmartRouting(pdfBuffer, prompt, processorType)
    │
    ├── 'visual' ──► Rasterize → analyzeWithLoadBalancing()
    │                  Fallback: analyzeWithDirectPdf(VISION_MODEL)
    │
    ├── 'text-heavy' ──► analyzeWithDirectPdf()
    │                      Fallback: Rasterize → analyzeWithLoadBalancing()
    │
    └── 'mixed' ──► analyzeWithDirectPdf() first
                     Fallback: Rasterize → compare quality scores
```

## Core Patterns

### Provider Configuration

```typescript
// lib/vision-api-multi-provider.ts
type VisionProvider = 'gemini-3-pro-preview' | 'gemini-2.5-pro' | 'claude-opus-4-6' | 'gpt-5.2' | 'claude-sonnet-4-5';

const PROVIDERS: ProviderConfig[] = [
  { name: 'claude-opus-4-6', maxRetries: 3, baseDelay: 1000 },
  { name: 'gpt-5.2', maxRetries: 3, baseDelay: 1000 },
  { name: 'claude-sonnet-4-5', maxRetries: 3, baseDelay: 1000 },
];
```

### PDF Detection and Native Processing

```typescript
// Claude supports native PDF via document type
export function isPdfContent(base64: string): boolean {
  return base64.startsWith('JVBERi');  // %PDF- magic number
}

// PDF content always routes to Opus (no GPT-5.2 fallback for PDFs)
if (isPdf) {
  logger.info('VISION_API', 'PDF native content — using Claude Opus');
}
```

### Timeout Strategy

| Provider | Image Timeout | PDF Timeout |
|----------|--------------|-------------|
| Claude Opus | 600s | 600s (retry once) |
| Claude Sonnet | 45s | 45s |
| GPT-5.2 | 90s | N/A (no PDF support) |
| Gemini Pro 3 | 90s | 300s |
| Gemini 2.5 Pro | 90s | 300s |
| Direct PDF (Opus) | 120s | 120s |

### Quality Validation

```typescript
// lib/vision-api-multi-provider.ts — validateQuality()
function validateQuality(content: string): QualityMetrics {
  let score = 0;
  if (/sheet[\s-]*\w+/i.test(content)) score += 30;     // Has sheet number
  if (content.length > 200) score += 30;                  // Substantial content
  if (content.includes(':') && content.includes('{')) score += 40;  // Structured data
  return { score, hasSheetNumber, hasContent, hasStructuredData, contentLength };
}
```

Minimum quality threshold: 50 (default). Content failing quality check triggers fallback to next provider.

### Three-Pass Pipeline Details

**Pass 1 — Gemini 3 Pro Preview (Extraction)**
- Model: `gemini-3-pro-preview`
- Purpose: Fast, cheap visual extraction of raw JSON
- Config: `maxOutputTokens: 8192, temperature: 0.1, thinkingLevel: LOW`
- Sees: The image/PDF directly

**Pass 2 — Gemini 2.5 Pro (Validation)**
- Model: `gemini-2.5-pro`
- Purpose: Validates Pass 1 output, fills gaps
- Config: `maxOutputTokens: 8192, temperature: 0.1, thinkingBudget: 1024`
- Sees: The image/PDF AND Pass 1's JSON output

**Pass 3 — Opus/GPT Interpretation (Text-Only)**
- Model: `claude-opus-4-6` (fallback: `gpt-5.2`)
- Purpose: Correct errors, enrich metadata, add confidence scores
- Sees: JSON only (no image) — purely text validation
- This is the cheapest pass since no vision tokens are consumed

### Cost per Page

| Pipeline | Cost |
|----------|------|
| Three-pass (Gemini + Opus) | ~$0.16 |
| GPT-5.2 fallback interpretation | ~$0.11 |
| Extraction-only (no interpretation) | ~$0.05 |

### Retry and Backoff

All providers use exponential backoff: `baseDelay * 2^retryCount`

```typescript
// Exponential backoff pattern used across all providers
if (retryCount < config.maxRetries) {
  const delay = config.baseDelay * Math.pow(2, retryCount);
  await new Promise(resolve => setTimeout(resolve, delay));
  return callProvider(imageBase64, prompt, retryCount + 1);
}
```

Special cases:
- Cloudflare blocks: immediate failover (no retry)
- Timeouts on Opus PDFs: one retry, then fail
- GPT-5.2 PDF content: fail fast (no PDF support)
- Gemini safety blocks: no retry

### Load Balancing

```typescript
// Round-robin across Opus and GPT-5.2 for images
let providerRoundRobinIndex = 0;
function getNextProviderIndex(): number {
  const index = providerRoundRobinIndex % PROVIDERS.length;
  providerRoundRobinIndex = (providerRoundRobinIndex + 1) % PROVIDERS.length;
  return index;
}
// PDFs always use Opus (skip round-robin)
```

## Configuration

### Key Files
| File | Purpose |
|------|---------|
| `lib/vision-api-multi-provider.ts` | Multi-provider vision wrapper, smart routing |
| `lib/document-processor-batch.ts` | Three-pass pipeline, batch processing |
| `lib/vision-api-quality.ts` | Quality validation extensions |
| `lib/model-config.ts` | Gemini model constants |
| `lib/discipline-prompts.ts` | 8 discipline-specific extraction prompts |
| `lib/pdf-to-image-raster.ts` | PDF rasterization (canvas native) |
| `lib/pdf-to-image-serverless.ts` | Single-page PDF extraction |

### Pipeline Mode

```typescript
type PipelineMode = 'discipline-single-pass' | 'three-pass-legacy';
// Controlled by env var PIPELINE_MODE, defaults to 'discipline-single-pass'
```

## Anti-Patterns

- **Never send PDFs to GPT-5.2** — it does not support native PDF content
- **Never skip quality validation** — low-quality extractions propagate bad data to RAG
- **Never hardcode timeouts** — use the provider config constants
- **Never retry on Cloudflare blocks** — switch providers immediately
- **Never use Sonnet for active vision** — it is a secondary fallback only

## Quick Reference

```typescript
import { analyzeWithLoadBalancing, analyzeWithSmartRouting, analyzeWithDirectPdf } from '@/lib/vision-api-multi-provider';

// Single image analysis (chat)
const result = await analyzeWithLoadBalancing(imageBase64, prompt, pageNumber);

// PDF with smart routing (batch)
const result = await analyzeWithSmartRouting(pdfBuffer, prompt, 'claude-opus-vision', pageNumber);

// Direct PDF processing
const result = await analyzeWithDirectPdf(pdfBase64, prompt, startPage, endPage);
```
