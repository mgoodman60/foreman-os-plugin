---
name: nextauth-rbac
description: ForemanOS NextAuth.js authentication and RBAC patterns. Use when writing API routes, auth checks, or role-based access control.
---

# NextAuth RBAC (ForemanOS)

NextAuth.js with JWT strategy (no session adapter), CredentialsProvider, and multi-tier RBAC.

## When to Use This Skill
- Writing new API route handlers
- Adding authentication checks
- Implementing role-based access control
- Working with guest/PIN-based auth
- Modifying the auth flow or session data

## Core Patterns

### Auth Configuration (`lib/auth-options.ts`)

Key architectural decisions:
- **JWT-only sessions** — no database adapter (reduces DB load by 90%)
- **CredentialsProvider** — username/email + password (case-insensitive lookup)
- **Guest PIN system** — password-less login for `role === 'guest'` users
- **Session lifetime**: 30 days, updated every 24 hours
- **Login page**: `/login`

### API Route Auth Check

Every API route MUST start with `getServerSession`:

```typescript
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth-options';

export async function GET(req: NextRequest) {
  try {
    const session = await getServerSession(authOptions);
    if (!session?.user?.email) {
      return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
    }

    // Access user data from session
    const userId = session.user.id;
    const role = session.user.role;
    const username = session.user.username;

    // ... business logic
  } catch (error) {
    return NextResponse.json({ error: 'Internal error' }, { status: 500 });
  }
}
```

Or with `apiError` helper (preferred for new routes):

```typescript
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth-options';
import { apiError, apiSuccess } from '@/lib/api-error';

export async function GET(req: NextRequest) {
  try {
    const session = await getServerSession(authOptions);
    if (!session?.user?.email) {
      return apiError('Unauthorized', 401, 'UNAUTHORIZED');
    }

    // Admin-only check
    if (session.user.role !== 'admin') {
      return apiError('Admin access required', 403, 'FORBIDDEN');
    }

    const data = await fetchData();
    return apiSuccess({ data });
  } catch (error) {
    return apiError('Failed to fetch data', 500, 'INTERNAL_ERROR');
  }
}
```

### JWT Token Shape

The JWT token carries these custom fields (set in `lib/auth-options.ts`):
```typescript
token.id                                           // User CUID
token.username                                     // Display name
token.role                                         // 'admin' | 'client' | 'guest'
token.Project_User_assignedProjectIdToProjectId    // Assigned project (for guests)
token.subscriptionTier                             // Subscription tier
token.loginLogged                                  // Flag to prevent duplicate login DB ops
```

Session shape accessible in API routes:
```typescript
session.user.id              // string
session.user.username        // string
session.user.role            // string
session.user.assignedProjectId  // string | undefined
session.user.subscriptionTier   // string | undefined
```

### Middleware (`middleware.ts`)

Uses `withAuth` from `next-auth/middleware`:
- Protected routes: `/dashboard/*`, `/projects/*`, `/admin/*`, `/profile/*`, `/settings/*`, `/chat/*`, `/api/*`
- Public API patterns bypass auth: `/api/auth/*`, `/api/webhooks/*`, `/api/cron/*`, `/api/documents/presigned-url`
- Unauthenticated users redirected to `/login`

### Role System

**Three-tier access control** (`lib/access-control.ts`):

| Role | Access Level |
|------|-------------|
| `admin` | Full access to all documents and features |
| `client` | Client + guest documents (no financial restrictions) |
| `guest` | Guest documents only (plans, specs, schedule — no budget/cost data) |

```typescript
import { hasDocumentAccess, isRestrictedQuery } from '@/lib/access-control';

// Check document access
if (!hasDocumentAccess(userLevel, documentName)) {
  return apiError('Access denied', 403, 'FORBIDDEN');
}

// Check if query touches restricted content (budget, costs)
if (isRestrictedQuery(query, userLevel)) {
  return apiError(getAccessDenialMessage(), 403, 'FORBIDDEN');
}
```

### Daily Report RBAC (`lib/daily-report-permissions.ts`)

Four-tier role hierarchy for field operations:

| Role | Create | Edit Own | Edit All | Submit | Approve | Delete |
|------|--------|----------|----------|--------|---------|--------|
| VIEWER | No | No | No | No | No | No |
| REPORTER | Yes | Draft/Rejected | No | Own | No | No |
| SUPERVISOR | Yes | Yes | Yes | Yes | Yes | No |
| ADMIN | Yes | Yes | Yes | Yes | Yes | Yes |

```typescript
import {
  getDailyReportRole,
  canCreateReport,
  canEditReport,
  canApproveReport,
  type DailyReportRole,
} from '@/lib/daily-report-permissions';

const role = await getDailyReportRole(userId, projectId);
if (!role || !canCreateReport(role)) {
  return apiError('Insufficient permissions', 403, 'FORBIDDEN');
}
```

Status state machine: `DRAFT -> SUBMITTED -> APPROVED | REJECTED -> DRAFT`

### Guest PIN System (`lib/guest-pin-utils.ts`)

PINs are namespaced per owner to prevent collisions:
```typescript
import { namespacePIN, stripPINPrefix } from '@/lib/guest-pin-utils';

// Storage: "{ownerId}_{pin}" e.g., "clx123_Job456"
const storedPin = namespacePIN(ownerId, 'Job456');

// Display: strips prefix to show user-facing PIN
const displayPin = stripPINPrefix(storedPin); // "Job456"
```

Login flow: user types their PIN as username, auth-options.ts finds the user via `endsWith` match on namespaced username.

### XSS Sanitization

Always sanitize user text input in daily reports:
```typescript
import { sanitizeText } from '@/lib/daily-report-permissions';

const cleanInput = sanitizeText(userInput);
// Strips HTML tags, script content, decodes entities
```

## Anti-Patterns

- **Never** skip `getServerSession(authOptions)` in API routes — middleware is a first pass, routes must re-check
- **Never** trust `session.user.role` without importing `authOptions` — passing wrong options gives stale data
- **Never** use `getSession()` (client-side) in API routes — use `getServerSession()` (server-side)
- **Never** store passwords for guest accounts — guests authenticate without passwords
- **Never** allow password-less login for non-guest roles — security check exists in auth-options.ts

## Quick Reference

| Pattern | Import |
|---------|--------|
| Server auth check | `import { getServerSession } from 'next-auth'` |
| Auth config | `import { authOptions } from '@/lib/auth-options'` |
| API error helper | `import { apiError, apiSuccess } from '@/lib/api-error'` |
| Access control | `import { hasDocumentAccess } from '@/lib/access-control'` |
| DR permissions | `import { getDailyReportRole, canCreateReport } from '@/lib/daily-report-permissions'` |
| Guest PINs | `import { namespacePIN, stripPINPrefix } from '@/lib/guest-pin-utils'` |
| Input sanitization | `import { sanitizeText } from '@/lib/daily-report-permissions'` |
