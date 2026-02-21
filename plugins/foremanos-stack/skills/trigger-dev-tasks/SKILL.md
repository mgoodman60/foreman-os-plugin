---
name: trigger-dev-tasks
description: ForemanOS Trigger.dev v3 task patterns. Use when creating background tasks, long-running jobs, or document processing pipelines.
---

# Trigger.dev Tasks (ForemanOS)

Trigger.dev v3 for long-running background tasks. Used primarily for document processing that exceeds Vercel's serverless timeout limits.

## When to Use This Skill
- Creating new background tasks
- Modifying the document processing pipeline
- Adding long-running operations (>60s)
- Working with task retries and error handling
- Debugging task execution issues

## Core Patterns

### Configuration (`trigger.config.ts`)

```typescript
import { defineConfig } from "@trigger.dev/sdk/v3";
import { prismaExtension } from "@trigger.dev/build/extensions/prisma";

export default defineConfig({
  project: "proj_gwelfqscrhdgtzzmqgxk",
  runtime: "node",
  logLevel: "log",
  maxDuration: 7200, // 2 hours
  retries: {
    enabledInDev: true,
    default: {
      maxAttempts: 3,
      minTimeoutInMs: 1000,
      maxTimeoutInMs: 10000,
      factor: 2,
      randomize: true,
    },
  },
  dirs: ["./src/trigger"],
  build: {
    extensions: [
      prismaExtension({
        mode: "legacy",
        schema: "prisma/schema.prisma",
        version: "6.7.0",
        migrate: false,
      }),
    ],
  },
});
```

Key config details:
- Task files live in `src/trigger/`
- Prisma extension uses `mode: "legacy"` with explicit version `6.7.0`
- `migrate: false` — migrations are handled separately
- Global `maxDuration: 7200` (2 hours) for large document processing

### Task Definition Pattern

From `src/trigger/process-document.ts`:

```typescript
import { task, logger as triggerLogger } from "@trigger.dev/sdk/v3";
import { prisma } from "@/lib/db";
import { Prisma, ProcessingQueueStatus } from "@prisma/client";
import { logger } from "@/lib/logger";

interface ProcessDocumentPayload {
  documentId: string;
  totalPages: number;
  processorType?: string;
  batchSize?: number;
}

export const processDocumentTask = task({
  id: "process-document",
  maxDuration: 7200,
  retry: {
    maxAttempts: 2,
    factor: 2,
    minTimeoutInMs: 5000,
    maxTimeoutInMs: 30000,
  },
  run: async (payload: ProcessDocumentPayload) => {
    const { documentId, totalPages, processorType = 'vision-ai' } = payload;

    // 1. Verify resource still exists (may have been deleted while queued)
    const docCheck = await prisma.document.findUnique({
      where: { id: documentId },
      select: { id: true },
    });
    if (!docCheck) {
      return { documentId, status: 'cancelled' as const };
    }

    // 2. Business logic with progress tracking
    // ...

    // 3. Return structured result
    return {
      documentId,
      pagesProcessed,
      totalPages,
      status: finalStatus,
      errors: errors.length > 0 ? errors : undefined,
    };
  },
});
```

### Error Handling in Tasks

**Sanitize errors** to strip API keys:
```typescript
function sanitizeError(error: unknown): string {
  const message = error instanceof Error ? error.message : String(error);
  return message
    .replace(/sk-[a-zA-Z0-9]{20,}/g, '[REDACTED_KEY]')
    .replace(/key-[a-zA-Z0-9]{20,}/g, '[REDACTED_KEY]')
    .replace(/Bearer\s+[a-zA-Z0-9._-]+/g, 'Bearer [REDACTED]')
    .substring(0, 500);
}
```

**Classify Prisma errors** for retry decisions:
```typescript
function classifyPrismaError(error: unknown) {
  if (error instanceof Prisma.PrismaClientKnownRequestError) {
    if (['P2025', 'P2003', 'P2002'].includes(error.code)) {
      return { isRetryable: false, code: error.code };
    }
    if (['P2024', 'P1001', 'P1002'].includes(error.code)) {
      return { isRetryable: true, code: error.code };
    }
  }
  return { isRetryable: true }; // Unknown errors are retryable
}
```

### Parallel Batch Processing

The document processing task processes pages in parallel batches:

```typescript
const PARALLEL_PAGES = parseInt(process.env.PARALLEL_PAGES || '4', 10);

for (let batchStart = 1; batchStart <= totalPages; batchStart += PARALLEL_PAGES) {
  const pageNumbers = Array.from(
    { length: Math.min(PARALLEL_PAGES, totalPages - batchStart + 1) },
    (_, i) => batchStart + i
  );

  // Process pages in parallel with per-page retry
  const results = await Promise.allSettled(
    pageNumbers.map(async (page) => {
      for (let attempt = 1; attempt <= MAX_PAGE_RETRIES; attempt++) {
        try {
          const result = await processPage(documentId, page);
          if (result.success) return { page, result };
          // Retry with exponential backoff
          await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 1000));
        } catch (error) {
          if (attempt === MAX_PAGE_RETRIES) throw error;
          await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 1000));
        }
      }
    })
  );

  // Single DB progress update per batch (reduces writes by ~4x)
  await prisma.$transaction([
    prisma.document.update({ where: { id: documentId }, data: { pagesProcessed } }),
    prisma.processingQueue.update({ where: { id: queueEntry.id }, data: { ... } }),
  ]);
}
```

### Timeout Protection

```typescript
const taskStartTime = Date.now();
const MAX_DURATION_SECONDS = 7200;

// Check at batch boundaries
const elapsedSeconds = (Date.now() - taskStartTime) / 1000;
if (elapsedSeconds > MAX_DURATION_SECONDS * 0.8) {
  logger.warn('TRIGGER', `Approaching timeout: ${Math.round(MAX_DURATION_SECONDS - elapsedSeconds)}s remaining`);
}
```

### Dual Logging

Tasks use both Trigger.dev's logger AND the app logger:

```typescript
import { logger as triggerLogger } from "@trigger.dev/sdk/v3";
import { logger } from "@/lib/logger";

// Trigger.dev dashboard visibility
triggerLogger.log(`Processing page ${page}/${totalPages}`, { documentId });

// Application logs (Vercel/server logs)
logger.info('TRIGGER_PROCESS', `Page ${page} completed`, { documentId });
```

### Post-Processing Pattern

After main work completes, run non-critical follow-ups in try/catch:

```typescript
// Main processing completed successfully
if (!allPagesFailed) {
  try {
    await runDocumentPostProcessing(documentId, pagesProcessed, true);
  } catch (postError) {
    // Log but don't fail — vision extraction already succeeded
    logger.error('TRIGGER_PROCESS', 'Post-processing failed', postError as Error);
  }
}
```

### Fatal Error Recovery

On fatal errors, update database status before re-throwing:

```typescript
catch (error) {
  try {
    await prisma.$transaction([
      prisma.processingQueue.updateMany({
        where: { documentId },
        data: { status: 'failed', lastError: sanitizeError(error) },
      }),
      prisma.document.update({
        where: { id: documentId },
        data: { queueStatus: 'failed', lastProcessingError: sanitizeError(error) },
      }),
    ]);
  } catch (dbError) {
    // Handle case where document was deleted mid-processing
    if (classifyPrismaError(dbError).code === 'P2025') {
      return { documentId, status: 'cancelled' };
    }
  }
  throw error; // Re-throw for Trigger.dev retry
}
```

## Anti-Patterns

- **Never** import from `@trigger.dev/sdk` (v2) — use `@trigger.dev/sdk/v3`
- **Never** use `console.log` in tasks — use `triggerLogger` + `logger`
- **Never** log API keys or sensitive data — always sanitize error messages
- **Never** skip the "resource still exists?" check at task start — resources may be deleted while queued
- **Never** update DB on every page — batch progress updates to reduce writes
- **Never** let post-processing failures fail the main task — wrap in try/catch

## Quick Reference

| Pattern | Import |
|---------|--------|
| Task definition | `import { task } from "@trigger.dev/sdk/v3"` |
| Trigger logger | `import { logger as triggerLogger } from "@trigger.dev/sdk/v3"` |
| App logger | `import { logger } from "@/lib/logger"` |
| Prisma client | `import { prisma } from "@/lib/db"` |
| Prisma types | `import { Prisma, ProcessingQueueStatus } from "@prisma/client"` |
| Task directory | `src/trigger/` |
| Config file | `trigger.config.ts` |
