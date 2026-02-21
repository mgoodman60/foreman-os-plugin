---
name: api-route-testing
description: ForemanOS API route testing patterns. Use when writing tests for Next.js App Router API endpoints with auth, rate limiting, and Prisma.
---

# API Route Testing for ForemanOS

## When to Use This Skill
- Writing tests for Next.js App Router API routes (`app/api/**/route.ts`)
- Testing authentication/authorization flows
- Testing rate limiting behavior
- Testing Stripe webhook handlers
- Testing CRUD operations with Prisma mocks

## Core Patterns

### Pattern 1: Auth + Prisma Mock Setup

Every API route test follows this structure: mock session, mock Prisma, mock supporting services, then test:

```typescript
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { NextRequest } from 'next/server';

// Mock session data
const mockSession = {
  user: {
    id: 'user-1',
    email: 'test@example.com',
    role: 'client',
  },
  expires: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
};

// Prisma mock with relevant models
const prismaMock = {
  project: { findUnique: vi.fn() },
  projectBudget: { findUnique: vi.fn(), create: vi.fn(), update: vi.fn() },
};

vi.mock('@/lib/db', () => ({ prisma: prismaMock }));

// Auth mocks
const getServerSessionMock = vi.fn();
vi.mock('next-auth', () => ({
  getServerSession: getServerSessionMock,
}));
vi.mock('@/lib/auth-options', () => ({ authOptions: {} }));

describe('GET /api/projects/[slug]/budget', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    getServerSessionMock.mockResolvedValue(mockSession);
  });

  it('should return 401 when not authenticated', async () => {
    getServerSessionMock.mockResolvedValue(null);

    const { GET } = await import('@/app/api/projects/[slug]/budget/route');
    const request = new NextRequest('http://localhost/api/projects/test-project/budget');
    const response = await GET(request, { params: { slug: 'test-project' } });

    expect(response.status).toBe(401);
    const data = await response.json();
    expect(data.error).toBe('Unauthorized');
  });
});
```

### Pattern 2: Testing Route Params

Next.js App Router passes route params as a second argument:

```typescript
// Route: app/api/projects/[slug]/budget/route.ts
// Test:
const response = await GET(request, { params: { slug: 'test-project' } });

// Route: app/api/projects/[slug]/documents/[id]/route.ts
// Test:
const response = await GET(request, {
  params: { slug: 'test-project', id: 'doc-1' },
});
```

### Pattern 3: NextRequest Construction

```typescript
// GET request
const request = new NextRequest('http://localhost/api/projects/test-project/budget');

// GET with query params
const request = new NextRequest(
  'http://localhost/api/auth/verify-email?token=valid-token'
);

// POST with JSON body
const request = new NextRequest('http://localhost/api/signup', {
  method: 'POST',
  body: JSON.stringify({ email: 'user@example.com', password: 'SecurePass123!' }),
  headers: { 'Content-Type': 'application/json' },
});

// PUT with JSON body
const request = new NextRequest('http://localhost/api/projects/test-project/budget', {
  method: 'PUT',
  body: JSON.stringify({ totalBudget: 1200000 }),
  headers: { 'Content-Type': 'application/json' },
});
```

### Pattern 4: Rate Limiting Tests

```typescript
const checkRateLimitMock = vi.fn();
const getClientIpMock = vi.fn().mockReturnValue('127.0.0.1');
const createRateLimitHeadersMock = vi.fn().mockReturnValue({
  'X-RateLimit-Limit': '5',
  'X-RateLimit-Remaining': '4',
});

vi.mock('@/lib/rate-limiter', () => ({
  checkRateLimit: checkRateLimitMock,
  getClientIp: getClientIpMock,
  createRateLimitHeaders: createRateLimitHeadersMock,
  RATE_LIMITS: {
    AUTH: { maxRequests: 5, windowSeconds: 300 },
  },
}));

// In beforeEach:
checkRateLimitMock.mockResolvedValue({
  success: true, limit: 5, remaining: 4,
  reset: Math.floor(Date.now() / 1000) + 300,
});

// Test rate limit exceeded:
it('should return 429 when rate limit exceeded', async () => {
  checkRateLimitMock.mockResolvedValue({
    success: false, limit: 5, remaining: 0,
    reset: Math.floor(Date.now() / 1000) + 300,
    retryAfter: 300,
  });

  const { POST } = await import('@/app/api/signup/route');
  const request = new NextRequest('http://localhost/api/signup', {
    method: 'POST',
    body: JSON.stringify(validSignupData),
    headers: { 'Content-Type': 'application/json' },
  });
  const response = await POST(request);

  expect(response.status).toBe(429);
});
```

### Pattern 5: Stripe Webhook Tests

```typescript
import {
  prismaMock,
  constructEventMock,
  subscriptionsRetrieveMock,
  headersMock,
  mockStripeSubscription,
} from '../../mocks/shared-mocks';
import {
  createMockStripeEvent,
  createMockCheckoutSession,
  createMockStripeSubscription,
} from '../../helpers/test-utils';

function createWebhookRequest(body: string, signature?: string): NextRequest {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  };
  if (signature) {
    headers['stripe-signature'] = signature;
  }
  return new NextRequest('http://localhost/api/stripe/webhook', {
    method: 'POST', body, headers,
  });
}

it('should return 400 when signature verification fails', async () => {
  headersMock.mockResolvedValue({
    get: vi.fn().mockReturnValue('invalid_signature'),
  });
  constructEventMock.mockImplementation(() => {
    throw new Error('Invalid signature');
  });

  const request = createWebhookRequest('{}');
  const response = await POST(request);
  expect(response.status).toBe(400);
});

it('should update user subscription on checkout completed', async () => {
  headersMock.mockResolvedValue({
    get: vi.fn().mockReturnValue('valid_signature'),
  });
  const session = createMockCheckoutSession();
  const event = createMockStripeEvent('checkout.session.completed', session);
  constructEventMock.mockReturnValue(event);

  const request = createWebhookRequest(JSON.stringify(event));
  const response = await POST(request);

  expect(response.status).toBe(200);
  expect(prismaMock.user.update).toHaveBeenCalledWith(
    expect.objectContaining({
      where: { id: 'user-1' },
      data: expect.objectContaining({
        stripeCustomerId: 'cus_test123',
        stripeSubscriptionId: 'sub_test123',
      }),
    })
  );
});
```

### Pattern 6: Authorization Tests (Owner/Admin)

```typescript
it('should return 403 when user is not project owner or admin', async () => {
  prismaMock.project.findUnique.mockResolvedValue({
    ...mockProject,
    ownerId: 'different-user',  // Not the session user
  });

  const { POST } = await import('@/app/api/projects/[slug]/budget/route');
  const request = new NextRequest('http://localhost/api/projects/test-project/budget', {
    method: 'POST',
    body: JSON.stringify({ totalBudget: 1000000 }),
    headers: { 'Content-Type': 'application/json' },
  });
  const response = await POST(request, { params: { slug: 'test-project' } });

  expect(response.status).toBe(403);
});

it('should allow admin to create budget for any project', async () => {
  getServerSessionMock.mockResolvedValue({
    user: { ...mockSession.user, role: 'admin' },
    expires: mockSession.expires,
  });
  prismaMock.project.findUnique.mockResolvedValue({
    ...mockProject,
    ownerId: 'different-user',
  });
  prismaMock.projectBudget.create.mockResolvedValue(mockBudget);

  const { POST } = await import('@/app/api/projects/[slug]/budget/route');
  // ...
  expect(response.status).toBe(201);
});
```

### Pattern 7: Testing Response Shape

```typescript
it('should return 201 with user data', async () => {
  const { POST } = await import('@/app/api/signup/route');
  const request = new NextRequest('http://localhost/api/signup', {
    method: 'POST',
    body: JSON.stringify(validSignupData),
    headers: { 'Content-Type': 'application/json' },
  });
  const response = await POST(request);

  expect(response.status).toBe(201);
  const data = await response.json();
  expect(data.requiresEmailVerification).toBe(true);
  expect(data.User).toBeDefined();
  expect(data.User.email).toBe(validSignupData.email);
});
```

### Pattern 8: Rollback / Error Recovery Tests

```typescript
it('should rollback user creation if Stripe checkout fails', async () => {
  checkoutSessionsCreateMock.mockRejectedValue(new Error('Stripe error'));

  const { POST } = await import('@/app/api/signup/route');
  const request = new NextRequest('http://localhost/api/signup', {
    method: 'POST',
    body: JSON.stringify({
      ...validSignupData,
      selectedTier: 'pro',
      billingPeriod: 'monthly',
    }),
    headers: { 'Content-Type': 'application/json' },
  });
  const response = await POST(request);

  expect(response.status).toBe(500);
  expect(prismaMock.user.delete).toHaveBeenCalled();
});
```

## Standard Test Categories

Every API route test should cover these categories:

1. **Authentication** — 401 when not authenticated
2. **Authorization** — 403 when wrong role/ownership
3. **Validation** — 400 for missing/invalid input
4. **Not Found** — 404 when resource doesn't exist
5. **Conflict** — 409 for duplicate creation
6. **Happy Path** — 200/201 with correct response shape
7. **Error Handling** — 500 on database/service errors
8. **Rate Limiting** — 429 when rate limit exceeded (auth routes)
9. **Side Effects** — Verify email sent, audit logged, webhook processed

## Key Files

| File | Purpose |
|------|---------|
| `__tests__/api/signup/route.test.ts` | Signup with Stripe checkout, email verification |
| `__tests__/api/stripe/webhook.test.ts` | Stripe webhook handling (checkout, subscription, invoice) |
| `__tests__/api/auth/verify-email.test.ts` | Email verification flow |
| `__tests__/api/auth/forgot-password.test.ts` | Password reset request |
| `__tests__/api/auth/reset-password.test.ts` | Password reset execution |
| `__tests__/api/projects/budget/route.test.ts` | CRUD with owner/admin auth |
| `__tests__/api/projects/budget/sync.test.ts` | Budget sync operations |
| `__tests__/api/projects/schedules/tasks.test.ts` | Schedule task management |
| `__tests__/mocks/shared-mocks.ts` | Shared mock definitions |
| `__tests__/helpers/test-utils.ts` | Mock factories and utilities |

## Anti-Patterns

- **Don't test route handlers without `await import()`** — Always dynamically import route handlers to get fresh module instances per test.
- **Don't mock `next-auth` without also mocking `@/lib/auth-options`** — The auth options module is imported by routes that call `getServerSession`.
- **Don't use `new Request()` for API route tests** — Use `new NextRequest()` which extends Request with Next.js-specific properties.
- **Don't test Prisma method calls without `expect.objectContaining`** — Prisma calls often include timestamps and generated fields; use matchers.
- **Don't hardcode timestamps in assertions** — Use `expect.any(Date)` or `expect.any(String)` for generated dates/tokens.

## Quick Reference

```bash
# Run all API route tests
npm test -- __tests__/api --run

# Run auth tests
npm test -- __tests__/api/auth --run

# Run Stripe webhook tests
npm test -- __tests__/api/stripe --run

# Run specific test
npm test -- __tests__/api/signup/route.test.ts --run
```
