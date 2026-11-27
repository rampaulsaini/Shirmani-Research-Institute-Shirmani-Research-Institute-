# Guest service evidence storage — readiness boundary

## Current implementation status

The guest service-order API stores opaque `private://...` locators in PostgreSQL. These values are **references only**. The production API does not implement binary upload, object storage, encryption-at-rest configuration, signed download URLs, malware scanning, retention/deletion jobs, or provider-side access logs.

A syntactically valid `private://` value is not proof that an object exists, is private, or is retrievable by an authorized person. Do not upload real customer evidence or treat these locators as verified storage.

A disposable test fixture now exists at `server/test/helpers/test-evidence-storage.js`. It is imported only by `server/test/evidence-storage.test.js`, not by production routes. It writes synthetic bytes to a temporary directory, uses random opaque keys, computes SHA-256, enforces a 5 MiB size ceiling and a small MIME allowlist, checks owner-and-order identity on read/delete, and removes its temporary data during cleanup. It is a test harness—not a production storage adapter. Its MIME check is not file-signature inspection, and it does not provide malware scanning, durable storage, or encryption-at-rest guarantees.

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

## Release gate

Until the controls above are implemented and independently reviewed, production evidence upload and customer evidence collection must remain disabled. The existing guest-order lifecycle tests validate state transitions and locator syntax; the new test-only fixture validates isolated temporary storage behavior only. Neither validates a production object-storage provider, customer-authenticated acceptance, or independent payment verification.
