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

## Current status
Schema migration and design only. Not applied to any database. No mailbox connected, no email imported, no production route enabled.
