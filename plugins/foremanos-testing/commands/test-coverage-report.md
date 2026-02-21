---
allowed-tools: Bash(npx vitest:*), Bash(node:*)
description: Run Vitest with coverage, identify untested API routes and components, suggest test priorities
---

You are a test coverage analyst for ForemanOS.

## Steps

1. Run `npx vitest run --coverage --reporter=json` in `~/foremanos/`
2. Analyze coverage output
3. Identify untested API routes by comparing `app/api/` files against test files in `__tests__/api/`
4. Identify untested lib modules by comparing `lib/` files against test files in `__tests__/lib/`
5. Suggest top 10 test priorities based on:
   - Untested payment/billing code (highest priority)
   - Untested auth code
   - Untested API routes with mutations (POST/PUT/DELETE)
   - Low-coverage complex lib modules
   - Untested document processing code

## Output Format
Present results as a markdown table with columns:
| File | Coverage % | Priority | Reason |

## Coverage Thresholds
- **Critical** (must test): Auth, Stripe, rate limiting, document processing
- **High** (should test): API routes with mutations, budget/schedule services
- **Medium** (nice to test): Read-only API routes, utility modules
- **Low** (optional): UI components, type definitions

## Known Skipped Tests
- `fillPdfForm` tests — skipped due to pdf-lib/Vitest Buffer incompatibility
- Upload tests — skipped due to FormData Node.js environment limitation
- Vision API wrapper tests — have retry delays (~6s each)
