---
name: data-fetching
description: ForemanOS client-side data fetching patterns. Use when writing React components that fetch API data or handle mutations.
---

# Data Fetching (ForemanOS)

Client-side data fetching via native `fetch` with `useEffect`. Server-side uses `fetchWithRetry` with exponential backoff. No SWR or React Query — all data fetching is vanilla React patterns.

## When to Use This Skill
- Writing React components that load data from API routes
- Handling form submissions and mutations
- Adding retry logic to network requests
- Working with loading/error states

## Core Patterns

### Client-Side Fetch with useEffect

The standard pattern used across 398 components:

```typescript
'use client';

import { useState, useEffect } from 'react';

export function MyComponent({ projectSlug }: { projectSlug: string }) {
  const [data, setData] = useState<MyData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`/api/projects/${projectSlug}/budget`);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const json = await response.json();
        setData(json);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [projectSlug]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  if (!data) return null;

  return <div>{/* render data */}</div>;
}
```

### Mutation Pattern (POST/PUT/DELETE)

```typescript
async function handleSubmit(formData: FormValues) {
  try {
    setSubmitting(true);
    const response = await fetch(`/api/projects/${slug}/budget`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to save');
    }

    const result = await response.json();
    // Update local state or refetch
    setData(result);
  } catch (err) {
    setError(err instanceof Error ? err.message : 'Unknown error');
  } finally {
    setSubmitting(false);
  }
}
```

### Server-Side Fetch with Retry (`lib/fetch-with-retry.ts`)

For server-side or service-to-service calls with automatic retry:

```typescript
import { fetchWithRetry, fetchJSON } from '@/lib/fetch-with-retry';

// Basic fetch with retry
const response = await fetchWithRetry('/api/external-service', {
  method: 'GET',
  retryOptions: {
    maxRetries: 3,
    initialDelay: 1000,
    maxDelay: 5000,
    backoffFactor: 2,
  },
});

// Typed JSON fetch
const data = await fetchJSON<MyResponseType>('https://api.example.com/data');
```

Default retry config: 3 retries, 1s initial delay, 5s max delay, factor 2 backoff.

### Presigned Upload Pattern

The multi-step upload flow used for document uploads:

```typescript
// 1. Get presigned URL
const presignRes = await fetch('/api/documents/presign', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ fileName, fileType, projectId }),
});
const { uploadUrl, key } = await presignRes.json();

// 2. Upload directly to R2/S3
await fetch(uploadUrl, {
  method: 'PUT',
  body: file,
  headers: { 'Content-Type': file.type },
});

// 3. Confirm upload
await fetch('/api/documents/confirm-upload', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ key, fileName, projectId }),
});
```

### Polling Pattern

For long-running operations like document processing:

```typescript
useEffect(() => {
  if (status !== 'processing') return;

  const interval = setInterval(async () => {
    const res = await fetch(`/api/documents/${documentId}/progress`);
    if (res.ok) {
      const progress = await res.json();
      setProgress(progress);
      if (progress.status === 'completed' || progress.status === 'failed') {
        clearInterval(interval);
      }
    }
  }, 3000); // Poll every 3 seconds

  return () => clearInterval(interval);
}, [documentId, status]);
```

### API Response Format

API routes return consistent JSON shapes:

**Success** (using `apiSuccess`):
```json
{ "data": { ... } }
```

**Error** (using `apiError`):
```json
{ "error": "Human-readable message", "code": "MACHINE_CODE" }
```

Error codes: `UNAUTHORIZED`, `FORBIDDEN`, `NOT_FOUND`, `RATE_LIMITED`, `VALIDATION_ERROR`, `INTERNAL_ERROR`, `SERVICE_UNAVAILABLE`.

## Anti-Patterns

- **Never** use SWR or React Query — the project uses vanilla fetch (no data fetching library is installed)
- **Never** call API routes from server components with `fetch` to localhost — use Prisma directly
- **Never** forget `Content-Type: application/json` header on POST/PUT requests
- **Never** skip error handling on fetch calls — always check `response.ok`
- **Never** use `fetchWithRetry` for client-side browser fetches — it imports `logger` which is server-only

## Quick Reference

| Pattern | Usage |
|---------|-------|
| Client fetch | `useEffect` + `fetch` + `useState` for loading/error/data |
| Mutations | `fetch` with POST/PUT + `response.ok` check |
| Server retry | `import { fetchWithRetry } from '@/lib/fetch-with-retry'` |
| Error format | `{ error: string, code: ApiErrorCode }` |
| Success format | Direct JSON data or `{ data: T }` |
| File upload | Presign -> PUT to R2 -> Confirm |
| Long operations | `setInterval` polling with cleanup |
