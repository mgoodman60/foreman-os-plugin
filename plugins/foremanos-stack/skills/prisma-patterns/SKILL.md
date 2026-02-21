---
name: prisma-patterns
description: ForemanOS Prisma 6.7 patterns. Use when writing database queries, creating models, or working with transactions.
---

# Prisma Patterns (ForemanOS)

Prisma 6.7 with PostgreSQL (Neon serverless). 112 models, `@prisma/client` generated to `node_modules/.prisma/client`.

## When to Use This Skill
- Writing or modifying Prisma queries
- Adding or changing schema models
- Working with transactions
- Fixing database connection issues
- Writing database helper utilities

## Core Patterns

### Prisma Client Singleton (`lib/db.ts`)

The Prisma client uses a global singleton with lazy construction. Always import from `@/lib/db`:

```typescript
import { prisma } from '@/lib/db';
```

Key details from the actual implementation:
- Uses `globalThis` to preserve a single instance across hot reloads in development
- Lazy construction: skips `PrismaClient` creation when `DATABASE_URL` is missing (happens during Trigger.dev Docker build indexing)
- Falls back to a `Proxy` that throws on any property access when `DATABASE_URL` is not configured
- Production logging: `['error']` only. Development: `['error', 'warn']`
- Graceful shutdown via `process.on('beforeExit'|'SIGINT'|'SIGTERM')`

### Schema Conventions

From `prisma/schema.prisma`:

```prisma
generator client {
  provider      = "prisma-client-js"
  output        = "../node_modules/.prisma/client"
  binaryTargets = ["native", "debian-openssl-1.1.x"]
}

datasource db {
  provider  = "postgresql"
  url       = env("DATABASE_URL")
  directUrl = env("DIRECT_DATABASE_URL")
}
```

Model conventions observed across 112 models:
- **IDs**: `@id @default(cuid())` — always CUID strings
- **Timestamps**: `createdAt DateTime @default(now())` and `updatedAt DateTime @updatedAt`
- **Soft delete**: `deletedAt DateTime?` (used on DailyReport)
- **Indexes**: Always add `@@index` for foreign keys and frequently queried fields
- **Compound indexes**: `@@index([budgetId, isActive])` for filtered queries
- **Unique constraints**: `@@unique([provider, providerAccountId])` for compound uniqueness
- **Cascade deletes**: `onDelete: Cascade` for child records, `onDelete: SetNull` for optional refs
- **Enums**: PascalCase names, SCREAMING_SNAKE values (e.g., `ChangeOrderStatus`, `PENDING`)

### Transaction Patterns

Two transaction styles used in the codebase:

**Batch transaction** (for independent operations):
```typescript
// From src/trigger/process-document.ts — multiple updates that must succeed together
await prisma.$transaction([
  prisma.document.update({
    where: { id: documentId },
    data: { queueStatus: 'processing' },
  }),
  prisma.processingQueue.update({
    where: { id: queueEntry.id },
    data: {
      status: ProcessingQueueStatus.processing,
      updatedAt: new Date(),
    },
  }),
]);
```

**Interactive transaction** (when operations depend on each other):
```typescript
// From lib/document-processor.ts
await prisma.$transaction(async (tx) => {
  // Use tx instead of prisma inside the callback
  const doc = await tx.document.findUnique({ where: { id } });
  await tx.documentChunk.create({ data: { ... } });
});

// From app/api/projects/invitations/[id]/accept/route.ts
await prisma.$transaction(async (tx: any) => {
  // Accept invitation and create project member atomically
});
```

### Query Patterns

**Case-insensitive search** (used in auth):
```typescript
const user = await prisma.user.findFirst({
  where: {
    OR: [
      { username: { equals: identifier, mode: 'insensitive' } },
      { email: { equals: identifier, mode: 'insensitive' } },
    ],
  },
  include: {
    Project_User_assignedProjectIdToProject: true,
  },
});
```

**Selective fields with `select`**:
```typescript
const project = await prisma.project.findUnique({
  where: { id: projectId },
  select: { ownerId: true },
});
```

**Increment pattern**:
```typescript
await prisma.document.update({
  where: { id: documentId },
  data: { processingCost: { increment: batchCost } },
});
```

### Database Retry Helper (`lib/db-helpers.ts`)

For operations that may fail due to connection issues:

```typescript
import { withRetry } from '@/lib/db-helpers';

const result = await withRetry(
  () => prisma.document.findMany({ where: { projectId } }),
  'fetch project documents'
);
```

Retryable Prisma error codes: `P2024` (connection pool timeout), `P1001` (unreachable), `P1002` (timeout), `P1008` (operations timeout), `P1017` (connection closed).

### Prisma Error Classification

From the Trigger.dev task (`src/trigger/process-document.ts`):
```typescript
import { Prisma } from '@prisma/client';

if (error instanceof Prisma.PrismaClientKnownRequestError) {
  // P2025 = record not found — NOT retryable
  // P2003 = foreign key constraint — NOT retryable
  // P2002 = unique constraint violation — NOT retryable
  // P2024, P1001, P1002 = connection errors — retryable
}
```

## Anti-Patterns

- **Never** import `PrismaClient` directly — always use `import { prisma } from '@/lib/db'`
- **Never** use `prisma.$connect()` in API routes — the singleton handles connections
- **Never** create new `PrismaClient` instances in request handlers
- **Never** use `findUnique` with non-unique fields — use `findFirst` instead
- **Never** omit `@@index` on foreign key fields — all foreign keys must be indexed
- **Never** use `autoincrement()` for IDs — always use `cuid()`

## Quick Reference

| Pattern | Import |
|---------|--------|
| Prisma client | `import { prisma } from '@/lib/db'` |
| Database health | `import { dbHealth } from '@/lib/db'` |
| Retry wrapper | `import { withRetry } from '@/lib/db-helpers'` |
| Error handling | `import { withErrorHandling } from '@/lib/db-helpers'` |
| Health check | `import { checkDatabaseHealth } from '@/lib/db-helpers'` |
| Prisma types | `import { Prisma, ProcessingQueueStatus } from '@prisma/client'` |
