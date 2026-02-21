---
name: redis-caching
description: ForemanOS Redis caching and rate limiting patterns. Use when adding caching, rate limiting, or working with Redis.
---

# Redis Caching (ForemanOS)

Redis via `ioredis` with graceful in-memory fallback. Used for query caching, rate limiting, and shared cache in multi-instance deployments.

## When to Use This Skill
- Adding cache to an API endpoint or service
- Implementing rate limiting
- Working with the query cache system
- Debugging Redis connection issues
- Setting up multi-instance shared state

## Core Patterns

### Two Redis Modules

ForemanOS has two Redis modules — use the right one:

| Module | Purpose | Import |
|--------|---------|--------|
| `lib/redis.ts` | General-purpose caching and rate limiting | `import { getCached, setCached, isRedisAvailable } from '@/lib/redis'` |
| `lib/redis-client.ts` | Connection manager for multi-instance deployments | `import { connectRedis, getRedisClient } from '@/lib/redis-client'` |

**Most code should use `lib/redis.ts`** — it handles the singleton, fallback, and error handling.

### Basic Cache Operations (`lib/redis.ts`)

```typescript
import { getCached, setCached, deleteCached, isRedisAvailable } from '@/lib/redis';

// Check availability first (optional — functions fail gracefully)
if (isRedisAvailable()) {
  // Set with TTL (seconds)
  await setCached('my-key', { data: 'value' }, 3600); // 1 hour

  // Get typed value
  const data = await getCached<{ data: string }>('my-key');

  // Delete
  await deleteCached('my-key');
}
```

Key behaviors from actual implementation:
- Initialized via `REDIS_URL` environment variable
- `enableOfflineQueue: false` — fail fast when Redis is down
- `lazyConnect: true` — connects on first command
- All operations return `null`/`false`/`0` when Redis is unavailable (never throws)
- Auto-serializes to JSON via `JSON.stringify`/`JSON.parse`

### Pattern-Based Invalidation

```typescript
import { clearCachePattern } from '@/lib/redis';

// Delete all keys matching a glob pattern
const deletedCount = await clearCachePattern('cache:projectId:*');
```

### Rate Limiting (`lib/rate-limiter.ts`)

Uses Redis counters with in-memory fallback:

```typescript
import {
  checkRateLimit,
  RATE_LIMITS,
  getRateLimitIdentifier,
  getClientIp,
  createRateLimitHeaders,
} from '@/lib/rate-limiter';

export async function POST(req: NextRequest) {
  const session = await getServerSession(authOptions);
  const ip = getClientIp(req);
  const identifier = getRateLimitIdentifier(session?.user?.id || null, ip);

  const rateLimit = await checkRateLimit(
    `chat:${identifier}`,
    RATE_LIMITS.CHAT
  );

  if (!rateLimit.success) {
    return NextResponse.json(
      { error: 'Rate limit exceeded' },
      { status: 429, headers: createRateLimitHeaders(rateLimit) }
    );
  }

  // ... proceed with request
}
```

Predefined rate limits:
```typescript
RATE_LIMITS.CHAT     // 20 messages/minute
RATE_LIMITS.UPLOAD   // 10 uploads/minute
RATE_LIMITS.API      // 60 requests/minute
RATE_LIMITS.AUTH     // 5 login attempts/5 minutes
RATE_LIMITS.RENDER   // 5 renders/10 minutes
```

### Redis Counter Operations

```typescript
import { incrementCounter, getCounter } from '@/lib/redis';

// Increment with TTL (for rate limiting)
const count = await incrementCounter('ratelimit:user:123', 60); // 60s TTL
// Returns number or null if Redis unavailable

const current = await getCounter('ratelimit:user:123');
```

### Redis Cache Adapter (`lib/redis-cache-adapter.ts`)

For structured cache with prefix namespacing and stats:

```typescript
import { RedisCacheAdapter } from '@/lib/redis-cache-adapter';

const cache = new RedisCacheAdapter('myfeature', 3600000); // prefix, TTL in ms

await cache.set('key', { data: 'value' });
const result = await cache.get<{ data: string }>('key');
await cache.delete('key');
await cache.invalidatePattern(/project-.*-budget/);

const stats = await cache.getStats();
// { size, entries, hits, misses, hitRate, evictions }
```

Cache adapter details:
- Wraps values in `CacheEntry<T>` with `{ value, expiresAt, size }`
- Uses `redis.setex()` with seconds-based TTL
- Uses `SCAN` instead of `KEYS` for pattern operations (safe for production)
- Tracks hit/miss stats in memory

### Query Cache (`lib/query-cache.ts`)

Specialized cache for LLM query responses with Redis + in-memory redundancy:

```typescript
import { getCachedResponse, cacheResponse } from '@/lib/query-cache';

// Check cache before calling LLM
const cached = await getCachedResponse(query, projectId, documentIds);
if (cached) return cached;

// Cache response after LLM call
await cacheResponse(query, response, projectId, documentIds, complexity, model);
```

Features: semantic similarity matching (Jaccard > 0.7), construction term normalization, dynamic TTL (48h standard, 72h high-value), LRU eviction prioritizing low-value entries.

## Anti-Patterns

- **Never** import `ioredis` directly in feature code — use `lib/redis.ts` or `lib/redis-client.ts`
- **Never** use `redis.keys('*')` in production — use `SCAN` with count limits
- **Never** assume Redis is available — always handle the `null`/`false` return
- **Never** store large blobs (>1MB) in Redis — use S3/R2 for file storage
- **Never** create new Redis connections per request — use the singleton

## Quick Reference

| Pattern | Import |
|---------|--------|
| Basic cache | `import { getCached, setCached, deleteCached } from '@/lib/redis'` |
| Availability check | `import { isRedisAvailable } from '@/lib/redis'` |
| Rate limiting | `import { checkRateLimit, RATE_LIMITS } from '@/lib/rate-limiter'` |
| Counter ops | `import { incrementCounter, getCounter } from '@/lib/redis'` |
| Structured cache | `import { RedisCacheAdapter } from '@/lib/redis-cache-adapter'` |
| Pattern clear | `import { clearCachePattern } from '@/lib/redis'` |
| Connection manager | `import { connectRedis, getRedisClient } from '@/lib/redis-client'` |
| Query cache | `import { getCachedResponse, cacheResponse } from '@/lib/query-cache'` |
