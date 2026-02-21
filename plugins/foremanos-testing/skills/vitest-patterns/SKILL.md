---
name: vitest-patterns
description: ForemanOS Vitest testing conventions. Use when writing or fixing unit tests, setting up mocks, or configuring test infrastructure.
---

# Vitest Patterns for ForemanOS

## When to Use This Skill
- Writing new unit tests for lib modules or API routes
- Debugging failing tests or mock issues
- Setting up test infrastructure (mocks, helpers, fixtures)
- Understanding the project's test conventions

## Vitest Configuration

ForemanOS uses this `vitest.config.ts`:

```typescript
import { defineConfig } from 'vitest/config';
import path from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'jsdom',
    pool: 'forks',
    include: ['__tests__/**/*.test.ts', '__tests__/**/*.test.tsx'],
    exclude: ['**/node_modules/**', '**/e2e/**'],
    testTimeout: 30000,
    setupFiles: ['__tests__/setup.ts'],
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './'),
    },
  },
});
```

Key settings:
- `pool: 'forks'` — Required for Node.js v25 compatibility (not `threads`)
- `environment: 'jsdom'` — DOM APIs available in all tests
- `globals: true` — `describe`, `it`, `expect` available without import (but always import from `vitest` anyway for clarity)
- `testTimeout: 30000` — 30s timeout per test
- `@` alias maps to project root

## Core Patterns

### Pattern 1: vi.hoisted() for Mocks Before Imports

Use `vi.hoisted()` when mock values are referenced in `vi.mock()` factory functions. This ensures the mocks exist before module imports.

```typescript
import { describe, it, expect, vi, beforeEach } from 'vitest';

// Hoisted mocks — created before any module imports
const mockSend = vi.hoisted(() => vi.fn());
const mockGetBucketConfig = vi.hoisted(() => vi.fn());

const MockS3Client = vi.hoisted(() => {
  return class S3Client {
    send = mockSend;
    config = { region: 'auto' };
    constructor() {}
  };
});

const mockLogger = vi.hoisted(() => ({
  debug: vi.fn(),
  info: vi.fn(),
  warn: vi.fn(),
  error: vi.fn(),
}));

// Module mocks — reference hoisted values
vi.mock('@aws-sdk/client-s3', () => ({
  S3Client: MockS3Client,
  PutObjectCommand: vi.fn().mockImplementation((input: any) => ({ input })),
  GetObjectCommand: vi.fn().mockImplementation((input: any) => ({ input })),
  DeleteObjectCommand: vi.fn().mockImplementation((input: any) => ({ input })),
}));

vi.mock('@/lib/logger', () => ({
  logger: mockLogger,
}));

// Import AFTER mocks are set up
import { uploadFile } from '@/lib/s3';
```

### Pattern 2: Grouped vi.hoisted() Object

For complex test files, group all mocks into a single hoisted object:

```typescript
const mocks = vi.hoisted(() => ({
  prisma: {
    conversation: { findUnique: vi.fn(), update: vi.fn() },
    project: { findUnique: vi.fn() },
    document: { create: vi.fn() },
    chatMessage: { findMany: vi.fn() },
  },
  getFileUrl: vi.fn(),
  uploadFile: vi.fn(),
  createScopedLogger: vi.fn(() => ({
    info: vi.fn(), error: vi.fn(), warn: vi.fn(),
  })),
  ReactPDF: { renderToBuffer: vi.fn() },
  React: { createElement: vi.fn() },
}));

vi.mock('@/lib/db', () => ({ prisma: mocks.prisma }));
vi.mock('@/lib/s3', () => ({
  getFileUrl: mocks.getFileUrl,
  uploadFile: mocks.uploadFile,
}));
vi.mock('@/lib/logger', () => ({
  createScopedLogger: mocks.createScopedLogger,
}));
```

### Pattern 3: Inline Prisma Mocks (Simple Tests)

For simpler tests that don't need shared mocks:

```typescript
const prismaMock = {
  user: {
    findFirst: vi.fn(),
    create: vi.fn().mockResolvedValue(mockNewUser),
    delete: vi.fn().mockResolvedValue(mockNewUser),
  },
};

vi.mock('@/lib/db', () => ({
  prisma: prismaMock,
}));
```

### Pattern 4: Shared Mocks File

For tests sharing common mocks (Stripe, auth, Prisma), import from `__tests__/mocks/shared-mocks.ts`:

```typescript
import {
  prismaMock,
  constructEventMock,
  subscriptionsRetrieveMock,
  headersMock,
  mockStripeSubscription,
} from '../../mocks/shared-mocks';
```

The shared mocks file pre-configures:
- NextAuth (`getServerSession`)
- Prisma (user, project, document, paymentHistory, markup models)
- Stripe (webhooks, subscriptions, checkout)
- S3 (upload, getFileUrl, download)
- Rate limiter, email service, audit log, logger
- Password validator, bcrypt, virus scanner

### Pattern 5: Dynamic Import for Route Handlers

API route tests use dynamic import inside each test to get fresh module instances:

```typescript
it('should return 401 when not authenticated', async () => {
  getServerSessionMock.mockResolvedValue(null);

  const { GET } = await import('@/app/api/projects/[slug]/budget/route');
  const request = new NextRequest('http://localhost/api/projects/test-project/budget');
  const response = await GET(request, { params: { slug: 'test-project' } });

  expect(response.status).toBe(401);
});
```

### Pattern 6: beforeEach with vi.clearAllMocks()

Every `describe` block resets mocks and sets sensible defaults:

```typescript
beforeEach(() => {
  vi.clearAllMocks();
  // Set defaults for happy path
  getServerSessionMock.mockResolvedValue(mockSession);
  checkRateLimitMock.mockResolvedValue({
    success: true, limit: 5, remaining: 4,
    reset: Math.floor(Date.now() / 1000) + 300,
  });
  prismaMock.user.findFirst.mockResolvedValue(null);
});
```

## Test Helpers

The project has test utilities in `__tests__/helpers/test-utils.ts`:

```typescript
// Create mock NextRequest
createMockNextRequest(method, body, headers, url)

// Create mock text body request (e.g., Stripe webhooks)
createMockTextRequest(body, headers, url)

// Create mock FormData request for file uploads
createMockFormDataRequest(formData, url)

// Create mock File object
createMockFile(content, name, type)

// Stripe mock factories
createMockStripeEvent(type, data, id)
createMockCheckoutSession(overrides)
createMockStripeSubscription(overrides)
createMockStripeInvoice(overrides)

// Prisma mock factories
createMockPrismaUser(overrides)
createMockPrismaDocument(overrides)

// Response parsing
extractResponseData(response)
```

## Key Files

| File | Purpose |
|------|---------|
| `vitest.config.ts` | Vitest configuration (jsdom, forks, 30s timeout) |
| `__tests__/setup.ts` | Global setup file |
| `__tests__/helpers/test-utils.ts` | Mock factories and test utilities |
| `__tests__/mocks/shared-mocks.ts` | Shared mock definitions for auth, Prisma, Stripe, S3 |
| `__tests__/lib/` | 75+ lib module test files |
| `__tests__/api/` | API route test files (auth, stripe, projects, documents) |
| `__tests__/smoke/` | Smoke tests (auth, serverless routes) |
| `e2e/` | Playwright E2E tests (23 spec files, separate from Vitest) |

## Anti-Patterns

- **Never use `pool: 'threads'`** — Causes issues with Node.js v25. Always use `pool: 'forks'`.
- **Never reference hoisted mocks before `vi.hoisted()`** — The mock must be created inside the `vi.hoisted()` callback.
- **Never import modules before `vi.mock()` calls** — Vitest hoists `vi.mock()` but module imports must come after.
- **Don't skip `vi.clearAllMocks()` in `beforeEach`** — Stale mock state causes flaky tests.
- **Don't mock `@prisma/client` directly for route tests** — Mock `@/lib/db` instead: `vi.mock('@/lib/db', () => ({ prisma: prismaMock }))`.
- **Don't use `describe.skip` casually** — Only skip tests with documented compatibility issues (e.g., `fillPdfForm` tests skipped due to pdf-lib/Vitest Buffer incompatibility).

## Quick Reference

```bash
# Run all tests
npm test -- --run

# Run specific test file
npm test -- __tests__/lib/s3.test.ts --run

# Run tests matching pattern
npm test -- --run -t "should upload file"

# Run smoke tests only
npm test -- __tests__/smoke --run

# Run with coverage
npx vitest run --coverage

# Watch mode
npm run test:watch
```

Test file naming: `__tests__/lib/<module-name>.test.ts` for lib modules, `__tests__/api/<path>/route.test.ts` for API routes.
