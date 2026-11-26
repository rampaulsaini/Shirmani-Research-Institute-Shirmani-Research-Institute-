# Private evidence storage contract (provider-neutral test foundation)

## Status

- Provider-neutral evidence service and fake-adapter tests only.
- No cloud provider is selected or connected.
- No bucket, account, credential, signed URL from a real provider, upload route, download route, or production data is created.
- The fake adapter is volatile process memory and is for automated tests only.
- Existing `private://` values in service-order records remain references, not proof that an object exists or is private.
- The service is not wired into the HTTP API or the guest service-order lifecycle.

## Contract

`server/src/private-evidence-storage.js` exposes:

- `store({ ownerId, orderId, purpose, contentType, bytes })`: accepts bytes only, enforces a MIME allowlist and size limit, generates an opaque key, calculates SHA-256, stores owner/order/purpose metadata, then checks the stored object's content type, byte size, digest and owner/order/purpose metadata.
- `createOwnerDownload(...)`: requires an owner-authorization callback, rechecks stored metadata, and asks the injected provider adapter for a short-lived HTTPS download URL (1–300 seconds; default 60), and rejects adapters that do not report the requested expiry.
- `deleteOwnerEvidence(...)`: requires owner authorization and an audit callback, rechecks stored metadata, records the authorization event, requests object deletion, verifies the object is absent, then records the deletion event.

A future adapter must implement private put, metadata head, signed GET creation and delete. Provider credentials must remain server-side. The current fake adapter is test-only and cannot be used for production.

## Deliberate non-claims / remaining gates

This contract does not itself provide durable storage, encryption-at-rest guarantees, object-level IAM, malware scanning, content-disposition controls, real signed URLs, retention enforcement, backups, persistent audit storage, customer identity, or evidence provenance. It also does not prove that a real provider bucket is private.

Before any real provider is connected, separately test private-by-default bucket policy, server-side credential isolation, bounded upload/download grants, checksum consistency, deletion/retention behavior, audit persistence, and authorization parity. Provider selection, account provisioning and credentials require separate review and explicit approval.
