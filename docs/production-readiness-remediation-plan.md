# Production-readiness remediation plan — guest service orders

**Status:** Design proposal only — not implemented, not deployed, and not approved for production.
**Prepared against:** PR #3796 head `b1c0906be3c916059ea74d3f428b8e545d1c9857` (2026-11-26).
**Scope:** Private evidence handling, customer-authenticated consent/acceptance, and truthful payment-verification states.

## Non-negotiable safety boundaries

- Keep PR #3796 Draft and unmerged until implementation and review gates pass.
- Do not run production migrations, change Render settings, create paid resources, activate Razorpay/webhooks, or alter production data as part of this plan.
- Do not commit credentials, tokens, customer data, evidence, or real payment references.
- Keep GitHub Pages as the public static surface; private evidence must never be stored in the repository or served from a public static path.
- A passing CI test is not proof of provider, storage, or production readiness.
- Preserve the current distinction between owner-recorded facts and independently/provider-verified facts.

## 1. Private evidence storage

### Proposed design

Introduce a small storage adapter boundary rather than coupling route handlers to one vendor:

- `EvidenceStorage.put()`: accept a validated upload and write to a private bucket/container.
- `EvidenceStorage.head()`: confirm object existence, byte length, content type, and checksum metadata.
- `EvidenceStorage.openForOwner()`: authorize the owner and issue a short-lived download URL or stream.
- `EvidenceStorage.delete()`: support retention expiry and approved deletion.
- Persist only opaque object keys and metadata in PostgreSQL; never persist public URLs or long-lived signed URLs.

The initial provider should be selected only after a read-only comparison of existing account/provider capabilities, free-tier limits, data region, egress/operation costs, lifecycle/retention controls, and access logging. Prefer an existing eligible private object-storage entitlement if it meets the requirements. Do not assume that a free tier is permanent or sufficient. Do not create a paid resource without explicit approval.

### Required controls

- Private-by-default bucket; public ACLs and public listing disabled.
- Server-side authorization on every upload, metadata, and download request.
- Short-lived upload/download authorization; random unguessable object keys.
- Allowlisted content types and extensions, maximum upload size, and content-signature checks (do not trust the browser MIME header).
- SHA-256 calculated server-side; persist checksum, size, detected media type, uploader, purpose, order ID, and timestamps.
- Verify object existence and checksum before accepting an evidence reference into a lifecycle transition.
- Never log file bytes, signed URLs, access tokens, or sensitive customer content.
- Define retention and deletion rules before accepting real customer documents; document backup expiry and deletion behavior.
- Add malware scanning/quarantine before enabling arbitrary customer uploads. Until that exists, restrict uploads to a narrow, documented file policy and do not describe the system as malware-scanned.

### Data model proposal

Add an evidence metadata table with: UUID, opaque object key (unique), order ID, purpose enum, uploader identity/type, detected content type, byte size, SHA-256, storage state, created time, retention/deletion timestamps, and audit metadata. Store no customer document contents in PostgreSQL. Use foreign keys and indexes; prevent one evidence item from being silently reassigned to another order or purpose.

Replace syntactic `private://...` checks with database-backed evidence lookups that verify ownership, order binding, purpose, storage state, and object existence. Keep a compatibility path only for historical records and label those references as legacy/unverified; do not silently treat them as uploaded evidence.

## 2. Customer-authenticated consent and acceptance

### Proposed flow

1. Owner prepares the exact service order: scope, INR amount, deadline, revision limit, and a human-readable order summary.
2. Server creates a cryptographically random, high-entropy token for the guest and stores only its hash. Bind it to the enquiry/order, action (consent or acceptance), and a digest of the exact terms.
3. Send the link to the contact address already supplied by the guest, using a configured transactional email provider. Do not expose the raw token in logs, analytics, or audit metadata.
4. Link expires after a short defined period, is single-use, and can be revoked/reissued by the owner. Rate-limit token attempts and avoid revealing whether an email/order exists.
5. Guest opens the link, sees the exact order/terms, and explicitly confirms or declines. Confirmation records timestamp, action, terms digest, token ID, and a minimal audit event.
6. For delivery acceptance, send a separate one-time link only after delivery is recorded. Guest may accept or raise a dispute; do not let an owner-supplied boolean complete the order.
7. Provide a manual fallback that remains explicitly labelled **owner-recorded, not customer-authenticated**. It must not share the authenticated acceptance status.

### Token safety

- Generate at least 256 bits of cryptographic randomness; store a one-way hash only.
- Enforce expiry, single-use, action binding, order binding, and terms-digest binding in a database transaction with row locking.
- Consume the token atomically; concurrent replay attempts must result in at most one successful confirmation.
- Do not put PII or order details in the URL. Use HTTPS and a restrictive referrer policy.
- Do not send a confirmation email until the customer-facing flow and email provider are configured and tested.
- Email-link possession proves access to that mailbox, not legal identity or a qualified electronic signature. Label it accurately as email-link authenticated confirmation.

### State model

Keep distinct values for `owner_recorded`, `customer_email_link_confirmed`, `customer_declined`, and `disputed`. A guest's explicit acceptance must be stored separately from the owner's action log. Do not infer acceptance from delivery, email open, or an owner-entered checkbox.

## 3. Payment verification model

### Immediate safe behavior

Keep the current manual process, but label it consistently as **owner-attested bank-statement match**. The `confirm_bank_match` request is an owner attestation, not an external verification signal. Public counters and receipts must not call this independently verified or provider-verified income.

### Future provider integration (separate approval required)

If a payment provider is selected later:

- Use provider-generated payment/order identifiers; bind provider amount and currency to the service order.
- Verify webhook signatures using a secret held only in deployment secrets.
- Enforce idempotency and persist provider event IDs uniquely.
- Handle duplicate, delayed, reordered, refunded, reversed, and disputed events.
- Reconcile provider status against server-side provider API when supported; never trust browser redirect/query parameters.
- Keep webhook event payloads minimized and redact secrets/PII from logs.
- Test signature failure, replay, duplicate event, wrong amount/currency, wrong order, refund, and provider outage.
- Show separate statuses: `pending`, `owner_attested_bank_match`, `provider_verified`, `refunded`, `reversed`, and `disputed`. Do not collapse these into a single generic “verified” flag.

No payment provider, webhook, live key, or payment activation is selected or configured by this document.

## 4. Test and release gates

| Area | Required tests before merge |
|---|---|
| Storage | Private bucket ACL; unauthorized owner/customer access denied; cross-order key rejected; nonexistent object rejected; checksum mismatch rejected; size/type spoof rejected; signed URL expires; delete/retention behavior verified |
| Evidence lifecycle | Upload metadata transaction rollback; duplicate object key rejected; evidence purpose mismatch rejected; historical locator labelled legacy/unverified; no public URL or file bytes in API response |
| Customer tokens | Expired, revoked, malformed, wrong-action, wrong-order, wrong-terms, and replay tokens rejected; concurrent replay has exactly one winner; rate limit works; no PII in token URL/logs |
| Consent | Customer sees exact scope/price/deadline/revisions; decline does not create paid/order-complete state; order terms changed after token issue invalidates token |
| Acceptance | Owner cannot set customer-authenticated acceptance; customer token works only for delivered order; dispute path blocks completion; manual owner-recorded fallback remains visibly distinct |
| Payments | Owner attestation label remains explicit; provider webhook bad signature/replay/duplicate/wrong amount/wrong currency/refund/reversal tests; browser-only success cannot mark paid |
| Privacy | Public status exposes aggregates only; owner inbox remains owner-only; evidence download is authorized and no-store; logs redact tokens, signed URLs, payment details, and PII |
| Operations | Backup/restore test; retention/deletion runbook; provider outage behavior; secret rotation; rate limits; audit trail review |

Run all tests against disposable PostgreSQL and a fake/local storage adapter first. Provider sandbox tests are a separate stage and must not use live keys. Production smoke tests, if ever approved, must use a dedicated test record and explicit owner authorization.

## 5. Implementation sequence

1. **Design approval:** agree storage provider and email provider only after reviewing current eligible/free capabilities and limits. No account/resource creation in this phase.
2. **Storage adapter + metadata schema:** local fake adapter tests, private-access tests, migration rollback test.
3. **Customer token service:** token issuance/consumption, consent and acceptance endpoints, replay/concurrency tests, email delivery adapter with test sink.
4. **Payment state separation:** preserve owner-attested status; add provider-verified only alongside a real provider integration and sandbox tests.
5. **Security review:** inspect routes, schema, logs, CORS, rate limits, object ACLs, token lifecycle, and threat model.
6. **Release review:** CI green, independent code review, migration plan/rollback, backup/restore proof, deployment approval. Only then consider removing Draft status; deployment remains a separate explicit decision.

## Current readiness decision

**Not production-ready.** The current PR's successful CI validates the tested API/database lifecycle but does not validate real object storage, guest-authenticated consent/acceptance, or provider-backed payment verification. Keep all existing records and statuses truthful; no live customer evidence should be collected through placeholder `private://` references.
