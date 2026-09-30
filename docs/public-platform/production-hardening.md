# Production Hardening — Yatharth Global Platform

This layer strengthens the existing API architecture without representing a repository branch as a globally live service.

## Durable primitives

The next database migration adds media metadata, bounded AI-agent registry and task-event history, privacy request tracking, and evidence records that distinguish primary sources, secondary sources, counter-evidence, reproducible tests, and human review.

## Automation boundary

Automission and AI agents may assist with classification, deduplication, source indexing, translation, routine health observation, and recovery preparation.

They must not independently certify a Yatharth claim as true, resolve consequential disputes, execute financial payouts merely because an order exists, turn a listing into proof of employment/income/delivery/satisfaction, or silently change verification status.

## Production gates

A capability is LIVE only after its external dependencies are actually configured and tested, including HTTPS, managed database, authentication/recovery, privacy/deletion, monitoring, backups, incident response, moderation/appeals, and required payment or storage providers.

INDEPENDENTLY_VERIFIED requires the applicable evidence contract and independent review. CI success, workflow completion, hashes, and AI output are not substitutes.

## Operational sequence

Preserve → Normalize → Compare → Test → Independently Review → Verify

For platform capabilities: Architecture → MVP → Tested → Deployment-Gated → Live → Automated

These are separate dimensions; one status must never be inferred from another.


## Readiness endpoint

The API exposes `GET /v1/platform/readiness` as an explicit deployment gate. It reports database/auth/CORS configuration and deliberately returns `production_live: false` and `independent_verification: false`. A configured environment is readiness evidence only; it is not proof of global deployment or truth verification.
