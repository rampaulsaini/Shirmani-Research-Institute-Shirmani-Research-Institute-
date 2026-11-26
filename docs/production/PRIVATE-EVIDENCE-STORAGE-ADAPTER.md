# Private evidence storage adapter boundary

Status: local contract and tests only. No storage provider is configured or connected.

## Purpose

`server/src/private-storage.js` defines a provider-neutral server-side boundary for private evidence objects. A future adapter may implement the four required operations:

- `putObject({ key, body, contentType, sha256 })`
- `headObject(key)`
- `getObject(key)`
- `deleteObject(key)`

The adapter must keep objects private and must not return public object URLs. The wrapper validates opaque object keys, allowed declared content types, byte limits, SHA-256 checksums, and the metadata/bytes returned by the adapter.

## Security boundary

- Authentication and per-order authorization must happen in the calling API route before `get` or `delete`. This module is not an authorization system.
- No upload/download HTTP route is added by this change.
- No presigned URL, public URL, or bearer grant is issued by this change.
- Declared MIME types are allowlisted but are not content-sniffed; a production upload route must independently inspect file signatures and enforce request limits.
- A production adapter must use a private bucket/container, least-privilege credentials, TLS, encryption at rest, safe object-key scoping, and provider-side access controls.
- Audit-event creation, retention/deletion policy, malware scanning, and customer identity/consent provenance remain separate production gates.
- The in-memory adapter in tests is disposable test code, not a production storage implementation.

## Required verification before provider selection

1. Test private write/read/delete behavior against an isolated local or disposable provider environment.
2. Verify unauthorized callers cannot obtain object bytes or object metadata.
3. Verify cross-order key access is denied by the API authorization layer.
4. Verify checksum, content-signature, size, MIME, retention, and audit behavior.
5. Review provider costs, account ownership, region, credentials, backups, and recovery.
6. Obtain explicit authorization before creating a bucket, storing customer evidence, or enabling a provider.

Passing unit tests proves only the local adapter contract. It does not prove a provider is configured, an object exists, a bucket is private, or production evidence is independently verified.
