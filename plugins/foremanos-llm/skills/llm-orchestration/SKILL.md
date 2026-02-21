---
name: llm-orchestration
description: Multi-provider LLM abstraction with prefix-based routing and model tier system. Use when working on LLM calls, model selection, or provider configuration.
---

# LLM Orchestration

## When to Use This Skill
- Adding or modifying LLM API calls anywhere in ForemanOS
- Changing model selection, routing, or fallback behavior
- Working with streaming responses
- Debugging provider-specific API issues
- Updating model constants after deprecation events

## Architecture Overview

```
callLLM(messages, options)
    │
    ├── model.startsWith('claude-') ──► callAnthropic()
    │                                    └── api.anthropic.com/v1/messages
    │
    └── default (gpt-*, o3-*, o4-*) ──► callOpenAI()
                                         └── api.openai.com/v1/chat/completions
```

Provider routing is determined by model prefix at call time. There is no fallback chain in `callLLM` itself — callers choose the model explicitly. The vision pipeline has its own multi-provider fallback (see `vision-pipeline` skill).

## Core Patterns

### Unified LLM Interface

All LLM calls use a single interface defined in `lib/llm-providers.ts`:

```typescript
interface LLMMessage {
  role: 'system' | 'user' | 'assistant';
  content: string | Array<LLMMessageContent>;
}

interface LLMOptions {
  model?: string;
  temperature?: number;
  max_tokens?: number;
  stream?: boolean;
  reasoning_effort?: 'light' | 'medium' | 'high' | 'xhigh';
  response_format?: { type: string };
}

interface LLMResponse {
  content: string;
  model: string;
  usage?: { prompt_tokens: number; completion_tokens: number; total_tokens: number };
}
```

### Prefix-Based Routing

```typescript
// lib/llm-providers.ts — callLLM()
export async function callLLM(messages: LLMMessage[], options: LLMOptions = {}): Promise<LLMResponse> {
  const model = options.model || SIMPLE_MODEL;
  if (model.startsWith('claude-')) {
    return callAnthropic(messages, options);
  }
  return callOpenAI(messages, options);  // gpt-*, o3-*, o4-*
}
```

### Model Tier System

All model constants are centralized in `lib/model-config.ts`:

| Constant | Model ID | Use Case |
|----------|----------|----------|
| `DEFAULT_FREE_MODEL` | `gpt-4o-mini` | Free tier simple queries |
| `SIMPLE_MODEL` | `gpt-4o-mini` | Cheap/simple queries |
| `DEFAULT_MODEL` | `claude-sonnet-4-5-20250929` | Paid tier default |
| `PREMIUM_MODEL` | `claude-opus-4-6` | Complex queries |
| `VISION_MODEL` | `claude-opus-4-6` | Vision/drawing analysis |
| `EXTRACTION_MODEL` | `claude-opus-4-6` | Document processing |
| `FALLBACK_MODEL` | `gpt-5.2` | OpenAI fallback |
| `GEMINI_PRIMARY_MODEL` | `gemini-3-pro-preview` | Three-pass extraction |
| `GEMINI_SECONDARY_MODEL` | `gemini-2.5-pro` | Three-pass validation |

### Legacy Model Alias Resolution

```typescript
// lib/model-config.ts — resolveModelAlias()
export function resolveModelAlias(model: string): string {
  const aliases: Record<string, string> = {
    'gpt-4o': FALLBACK_MODEL,           // Deprecated Feb 13, 2026
    'gpt-3.5-turbo': SIMPLE_MODEL,
    'claude-3-5-sonnet-20241022': DEFAULT_MODEL,
    'claude-sonnet-4-5-20251101': DEFAULT_MODEL,
    'claude-3-opus-20240229': PREMIUM_MODEL,
    // ...more aliases
  };
  return aliases[model] || model;
}
```

### Anthropic Format Conversion

Claude requires different message formats. Key conversions in `callAnthropic()`:

1. **System messages** extracted to top-level `system` field
2. **image_url blocks** converted to Claude `image.source` format
3. **PDF data URLs** converted to Claude `document.source` format
4. **response_format: json_object** injected as system prompt instruction
5. **Token key** uses `max_tokens` (not `max_completion_tokens`)

### Reasoning Effort (o3/o4 Models)

```typescript
// Only applied for o3-*/o4-* models
if (options.reasoning_effort && (model.startsWith('o3') || model.startsWith('o4'))) {
  requestBody.reasoning_effort = options.reasoning_effort;  // 'light'|'medium'|'high'|'xhigh'
}
```

### Streaming

```typescript
// lib/llm-providers.ts — streamLLM()
export async function streamLLM(messages, options): Promise<ReadableStream<Uint8Array>> {
  if (model.startsWith('claude-')) return streamAnthropic(messages, options);
  return streamOpenAI(messages, options);
}
```

Both providers return native `ReadableStream<Uint8Array>`. The chat handler in `lib/chat/processors/llm-handler.ts` pipes these directly to the response.

### Complexity-Based Model Selection

```typescript
// lib/chat/processors/llm-handler.ts
const complexityAnalysis = analyzeQueryComplexity(message);
const selectedModel = image ? VISION_MODEL : complexityAnalysis.model;
```

Images always route to `VISION_MODEL` (Opus 4.6). Text queries are routed by complexity analysis from `lib/query-cache.ts`.

## Configuration

### Key Files
| File | Purpose |
|------|---------|
| `lib/llm-providers.ts` | Provider abstraction, routing, streaming |
| `lib/model-config.ts` | Model constants, alias resolution, type guards |
| `lib/chat/processors/llm-handler.ts` | Chat pipeline model selection |
| `lib/query-cache.ts` | Complexity analysis for model routing |

### Environment Variables
| Variable | Required | Purpose |
|----------|----------|---------|
| `ANTHROPIC_API_KEY` | Yes* | Claude API access |
| `OPENAI_API_KEY` | Yes* | OpenAI API access |
| `GOOGLE_API_KEY` | No | Gemini vision pipeline |

*At least one of Anthropic or OpenAI is required.

## Anti-Patterns

- **Never hardcode model IDs** — always import from `lib/model-config.ts`
- **Never call provider APIs directly** — use `callLLM()` or `streamLLM()`
- **Never assume JSON mode works the same across providers** — Claude needs system prompt injection, OpenAI uses `response_format`
- **Never use `gpt-4o`** — deprecated Feb 13, 2026; use `FALLBACK_MODEL` (gpt-5.2)
- **Never set reasoning_effort on non-reasoning models** — only o3/o4 support it

## Quick Reference

```typescript
import { callLLM, streamLLM } from '@/lib/llm-providers';
import { DEFAULT_MODEL, VISION_MODEL, SIMPLE_MODEL } from '@/lib/model-config';

// Simple text query
const result = await callLLM(messages, { model: DEFAULT_MODEL });

// Vision query
const result = await callLLM(messages, { model: VISION_MODEL, max_tokens: 8000 });

// JSON output
const result = await callLLM(messages, {
  model: DEFAULT_MODEL,
  response_format: { type: 'json_object' },
});

// Streaming
const stream = await streamLLM(messages, { model: DEFAULT_MODEL });
```
