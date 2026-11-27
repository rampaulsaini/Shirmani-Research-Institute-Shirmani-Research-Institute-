# Guest service evidence storage — readiness boundary

## Current implementation status

The guest service-order API stores opaque `private://...` locators in PostgreSQL. These values are **references only**. The repository does not currently implement binary upload, object storage, encryption-at-rest configuration, signed download URLs, malware scanning, retention/deletion jobs, or provider-side access logs.

A syntactically valid `private://` value is not proof that an object exists, is private, or is retrievable by an authorized person. Do not upload real customer evidence or treat these locators as verified storage.

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

## Safe next test stage

A future test-only adapter may use an ephemeral temporary directory or in-memory object map, random opaque keys, and deterministic cleanup. It must be injected only in test mode, reject production startup, contain synthetic fixtures only, and never return raw object contents from public routes.

## Release gate

Until the controls above are implemented and independently reviewed, evidence upload and customer evidence collection must remain disabled. The existing guest-order lifecycle tests validate state transitions and locator syntax only; they do not validate object storage, customer-authenticated acceptance, or independent payment verification.
