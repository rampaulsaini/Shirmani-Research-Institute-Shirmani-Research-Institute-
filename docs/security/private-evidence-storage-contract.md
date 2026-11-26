# Private evidence storage contract (test-only foundation)

## Status

- Provider-neutral contract and process-local fake adapter only.
- No cloud provider is selected or connected.
- No bucket, account, credential, signed URL, upload route, download route, or production data is created.
- The fake adapter is volatile process memory and is for automated tests only.
- Existing `private://` values in service-order records remain references, not proof that an object exists or is private.

## Contract

`createPrivateObjectStore({ adapter, maxBytes, allowedMimeTypes })` exposes:

- `put({ body, contentType })`: accepts bytes only, enforces MIME and size allowlists, generates an opaque key, and calculates SHA-256.
- `head(key)`: returns metadata only; never a public URL or object bytes.
- `get({ key, authorize })`: requires a per-object authorization callback and verifies size and SHA-256 after retrieval.
- `delete({ key, authorize })`: requires a per-object authorization callback.

The injected adapter must implement `put`, `head`, `get`, and `delete`. Keys are constrained to generated UUID paths under `evidence/`. Locators use the internal `private://` scheme and are not browser-accessible URLs.

## Deliberate non-claims / remaining gates

This contract does not itself provide durable storage, encryption-at-rest guarantees, object-level IAM, malware scanning, content-disposition controls, signed URL issuance, retention enforcement, backups, audit persistence, customer identity, or evidence provenance. Those must be designed and tested before any real provider is connected.

A future provider adapter must prove private-by-default bucket policy, server-side credential isolation, bounded upload/download grants, checksum consistency, deletion/retention behavior, and authorization parity. Provider selection and provisioning require separate review and explicit approval.
