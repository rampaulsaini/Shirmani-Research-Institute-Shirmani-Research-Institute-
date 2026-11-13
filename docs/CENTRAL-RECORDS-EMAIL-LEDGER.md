# SRI Central Records & Email Ledger

## Purpose
One owner-controlled record system for communications, enquiries, bulk orders, quotations, payment evidence, deliveries, customer acceptance, and automation/audit events.

## Data model
- `communication_messages`: message envelope, provider/thread IDs, direction, timestamps, delivery state, encrypted message content.
- `communication_attachments`: attachment metadata and private object-storage key; bytes must be encrypted before upload.
- `record_links`: connects email threads to enquiries, customers, orders, payments, and deliveries without duplicating records.
- Existing `client_enquiries`, `orders`, `transactions`, and `audit_events` remain the source records for their domains.
- `audit_checkpoints`: periodic digest/count checkpoints for exported audit ranges.

## Security and retention requirements
1. Encrypt message bodies and attachment bytes before database/object-storage writes. Store key version, never the key.
2. Never store passwords, OTPs, payment PINs, session cookies, or full card/bank credentials.
3. Restrict all message and customer-record APIs to the configured owner identity; deny by default.
4. Verify provider webhook signatures and OAuth state; encrypt refresh tokens in a separate secrets store.
5. Deduplicate imports by provider + mailbox + provider message ID.
6. Preserve inbound/outbound direction, message/thread IDs, timestamps, sender/recipients, subject, delivery/bounce status, and attachment hashes.
7. Record every create/update/status transition in `audit_events`; do not provide audit update/delete APIs.
8. Use private storage, access logs, retention rules, export, and tested backups. Never expose message bodies or attachments publicly.

## Rollout gates
- Migration reviewed and applied to a non-production database first.
- Unit/integration tests for duplicate imports, encryption, owner-only access, webhook verification, attachment limits, and audit writes.
- Gmail/SMTP provider connection authorized by the account owner; historical sync is bounded and resumable.
- Verify backup/restore and export before production enablement.
- No automatic email sending without explicit owner approval until a separate policy is approved.

## Message-content encryption implementation
- `server/src/communication-crypto.js` uses Node.js AES-256-GCM with a fresh 96-bit nonce per message and an authenticated 128-bit tag.
- Configure `EMAIL_CONTENT_KEY` as canonical base64 for exactly 32 random bytes and `EMAIL_CONTENT_KEY_VERSION` as a non-secret version label (for example, `v1`) in the runtime secret manager. Never commit either value.
- Generate a key locally with `openssl rand -base64 32`; enter it only in the hosting provider's protected environment-variable UI. Do not paste it into chat, source control, logs, or database rows.
- Persist the returned `encryptedContent` bytes, `contentKeyVersion`, and `contentSha256` together. Decryption must select the key by the stored version; fail closed if the matching key is unavailable.
- Rotation requires retaining the old key in a protected secret store until all content encrypted with that version has been re-encrypted and verified. Do not overwrite a key version in place.
- Unit tests cover round-trip, nonce uniqueness, authentication failure on tampering, wrong keys, and invalid configuration. These tests do not prove production key management or mailbox integration.

## Current status
Schema migration and design only. Not applied to any database. No mailbox connected, no email imported, no production route enabled.
