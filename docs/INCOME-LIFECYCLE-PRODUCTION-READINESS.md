# Income Lifecycle — Production Readiness Design

**Status:** Design proposal only — not implemented, not deployed, and not approval to activate payments.

**Scope:** Close the three production gaps identified in PR #3796 while preserving the free-first hosting policy and keeping GitHub Pages as the public source of truth.

## 1. Private evidence storage

### Required behavior
- Replace acceptance of a syntactically valid `private://...` string as sufficient evidence with a storage-adapter contract.
- Upload bytes through an authenticated server endpoint; never accept a client-supplied storage key as proof that an object exists.
- Generate opaque object keys server-side. Keep the bucket/container private; never expose public object URLs.
- Persist metadata: object key, SHA-256, byte length, detected content type, uploader, purpose, linked order/proof, created time, and retention/deletion state.
- Enforce maximum upload size, allowlisted content types, safe filenames, authorization on every read, and audit access.
- Retrieval must use a short-lived signed URL or authenticated streaming endpoint. Do not log signed URLs or raw evidence.
- Add retention policy, deletion workflow, and backup/deletion documentation before real customer evidence is accepted.

### Low-cost implementation path
- First build and test a storage interface with a disposable local test adapter. CI must prove upload, checksum, authorization denial, retrieval, and deletion.
- Production adapter must be private object storage (S3-compatible or equivalent) with credentials held only in server-side environment secrets.
- Do not use an ephemeral Render filesystem as durable evidence storage. Do not store sensitive evidence in a public Git repository, GitHub Pages, or public static assets.
- Keep production evidence upload disabled until a private bucket, credentials, retention policy, and access tests are configured. Do not select or provision a paid storage plan without approval.

## 2. Customer-authenticated consent and acceptance

### Required behavior
- Keep owner-only routes for owner operations, but do not let an owner-supplied boolean such as `customer_confirmed: true` stand in for customer authentication.
- Generate a cryptographically random, high-entropy, single-use token for each customer action. Store only its hash.
- Bind token to one order, one action (consent or acceptance), and the exact displayed order version/scope/amount where applicable.
- Set a short expiry; invalidate on use, order changes, cancellation, or replacement. Enforce rate limits and generic responses to reduce token enumeration.
- Send the link only to the enquiry's verified email address. Verify control of that address before issuing action links. Do not expose customer PII in public status.
- Customer endpoint must validate token hash, expiry, action, order state, and unused status in one database transaction; record timestamp, token id, and event audit.
- Owner may view the result but must not be able to manufacture the customer's confirmation through the customer endpoint.

### Tests required
- Wrong, expired, already-used, revoked, wrong-order, wrong-action and altered-order-version tokens are rejected.
- Two simultaneous submissions yield at most one successful use.
- Unauthenticated owner/customer access boundaries and rate limits are tested.
- Email delivery failure leaves the order in a pending state and exposes no confirmation link publicly.

## 3. Payment verification model

### Manual pilot (honest interim state)
- If using bank/UPI transfer without a provider integration, label the result **Owner-attested bank match — not independently verified**.
- Require the owner to record amount, currency, transaction reference, matching statement date/reference, and who checked it. Avoid storing full bank statements or unnecessary account data.
- Public counters may call this owner-attested revenue only if the UI clearly labels the method and never describes it as provider-confirmed or independently audited.
- Keep pending, rejected, refunded, disputed and verified states distinct. Add idempotency and immutable audit history.

### Provider-confirmed option (later, explicit approval required)
- A payment provider integration must verify signed webhooks server-side, validate provider order/payment IDs, amount, currency, merchant account, capture status, and event freshness.
- Store webhook event IDs and enforce idempotency. Never trust a browser redirect or client-supplied success flag.
- Reconcile provider settlements/refunds separately from payment capture. Do not claim settlement until matched to settlement records.
- Keep provider integration disabled until merchant onboarding, credentials, webhook secret, test-mode integration tests, and explicit production activation approval are complete.

## 4. Suggested phased delivery

| Phase | Deliverable | Release gate |
|---|---|---|
| A | Storage adapter interface + disposable test adapter | CI tests pass; no production credentials |
| B | Private storage provider adapter + metadata migration | Private ACL, checksum, read/delete and retention tests pass |
| C | Customer token issuance and single-use consent/acceptance | Token lifecycle, email ownership, concurrency and abuse tests pass |
| D | Manual payment audit improvements | Public labels accurately say owner-attested |
| E | Optional payment-provider sandbox | Signed webhook, idempotency, amount/currency and refund tests pass |
| F | Production activation review | Separate explicit approval; deployment and live payments remain off until then |

## 5. Global safety and release gates
- No production database migration, deployment, payment activation, or customer data mutation as part of this design document.
- No paid service or plan is assumed. Confirm current free-tier limits and data residency/security requirements before choosing a provider.
- Use disposable PostgreSQL in CI; tests must not connect to production.
- Keep PR #3796 Draft until implementation and independent review of the three gaps are complete.
- Update public status language so test/owner-attested records cannot be confused with independent verification.
- Add rollback steps and verify backups before any future production migration.

## Current assessment
PR #3796 CI success establishes that the implemented owner-operated lifecycle passes its disposable PostgreSQL tests. It does **not** establish durable private evidence storage, customer-authenticated acceptance, or independent/provider-confirmed payment verification. This document proposes the next work only; none of those capabilities is represented as implemented.
