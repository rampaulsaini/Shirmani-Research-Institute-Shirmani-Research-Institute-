# Guest service evidence storage — readiness boundary

## Current implementation status

The guest service-order API stores opaque `private://...` locators in PostgreSQL. These values are **references only**. The production API does not implement binary upload, object storage, encryption-at-rest configuration, signed download URLs, malware scanning, retention/deletion jobs, or provider-side access logs.

A syntactically valid `private://` value is not proof that an object exists, is private, or is retrievable by an authorized person. Do not upload real customer evidence or treat these locators as verified storage.

A provider-neutral adapter shape contract now exists at `server/src/evidence-storage/contract.js`. It requires `put`, `get`, `delete`, and `close` methods and is deliberately not imported by production routes. The disposable test fixture at `server/test/helpers/test-evidence-storage.js` conforms to that contract and is imported only by `server/test/evidence-storage.test.js`. It writes synthetic bytes to a temporary directory, uses random opaque keys, computes SHA-256, enforces a 5 MiB size ceiling and a small MIME allowlist, checks owner-and-order identity on read/delete, and removes its temporary data during cleanup. The shared contract checks interface shape only; it does not certify security or durability. The fixture is a test harness—not a production storage adapter. Its MIME check is not file-signature inspection, and it does not provide malware scanning, durable storage, or encryption-at-rest guarantees.

## Required production controls before accepting real evidence

1. Select and explicitly approve an object-storage provider and region; document data residency and subprocessors.
2. Use a private bucket/container with public access disabled and least-privilege service credentials.
3. Generate opaque server-side object keys; never accept client-supplied bucket URLs or arbitrary storage keys.
4. Enforce upload size, MIME allowlist, file-signature inspection, malware scanning, and safe filename handling.
5. Encrypt in transit and at rest; keep credentials in the deployment secret store, never in Git or the database.
6. Authorize every read/download against the owning service order and owner/customer permissions; use short-lived signed URLs only after authorization.
7. Keep evidence bytes and signed URLs out of public status, logs, audit metadata, and analytics.
8. Define retention, deletion, backup expiry, access audit, incident response, and customer data export procedures.
9. Test unauthorized reads, cross-order access, expired links, oversized files, spoofed MIME types, and deletion/retention behavior.
10. Obtain explicit human approval and a reviewed provider configuration before production enablement.

## Phase A status

- [x] Provider-neutral adapter method contract defined.
- [x] Disposable temporary-directory fixture conforms to the contract.
- [x] Contract-shape and fixture behavior tests added.
- [ ] Production provider adapter intentionally not selected or implemented.
- [ ] Production routes remain disconnected; real evidence upload remains disabled.


## Phase B — customer acceptance token (test-gated; not identity verification)

A delivered guest service order can now receive a single-use acceptance bearer token through the owner-only endpoint `POST /api/owner/service-orders/:orderId/acceptance-invitations`. The raw token is returned once to the owner; only its SHA-256 hash is stored. Tokens expire after 72 hours, issuing a replacement revokes the previous active token, and a successful customer POST consumes the token. The customer action is `POST /api/service-order-acceptance` with `{"token":"<one-time-token>","accepted":true}`; the token is sent in the request body, not the URL, to reduce URL/log exposure.; it is deliberately a POST so link-preview bots do not consume invitations.

**Important boundary:** no email/SMS/customer messaging provider is configured. The owner must manually share the token through a private out-of-band channel. The token proves possession of a bearer secret, not the recipient's legal identity, account identity, or independent confirmation. Do not describe this as customer identity authentication. The old owner-only route that accepted `customer_confirmed: true` is fail-closed with HTTP 410. The new method records `single_use_token` and does not fabricate a `private://` evidence-file locator.

- [x] Hash-only token storage; raw token returned once to the owner.
- [x] 72-hour expiry, one active token per order, replacement revocation, one-time consumption.
- [x] Public acceptance endpoint requires explicit POST confirmation and is rate-limited.
- [x] Tests cover pre-delivery issuance rejection, malformed token, missing confirmation, expiry, replacement revocation, replay, and completion.
- [ ] Automated customer delivery channel not configured.
- [ ] Recipient identity verification and independent audit not implemented.

## Release gate

Until the controls above are implemented and independently reviewed, production evidence upload and customer evidence collection must remain disabled. The separate acceptance-token flow may record a one-time customer action, but must not be represented as identity-verified acceptance. The existing guest-order lifecycle tests validate state transitions and locator syntax; the new test-only fixture validates isolated temporary storage behavior only. Neither validates a production object-storage provider, recipient identity, or independent payment verification. The token flow validates single-use bearer-token possession only; it is not customer identity authentication.
