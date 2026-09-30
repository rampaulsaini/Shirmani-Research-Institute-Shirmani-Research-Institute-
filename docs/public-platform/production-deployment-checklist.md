# Production Deployment Checklist — Yatharth Global Platform

This checklist is a deployment gate, not a claim that the repository is currently globally live.

## Infrastructure
- [ ] Managed PostgreSQL configured and migration set applied.
- [ ] HTTPS endpoint configured.
- [ ] CORS restricted to approved production origins.
- [ ] JWT secret stored in a secret manager.
- [ ] Object storage configured for media binaries.
- [ ] Backups and restore test completed.
- [ ] Monitoring, logs and alerting configured.
- [ ] Rate limits reviewed for production traffic.

## Identity and privacy
- [ ] Account recovery and email verification implemented.
- [ ] Privacy/export/delete/correction workflows tested.
- [ ] Session/token rotation and revocation policy reviewed.
- [ ] Abuse prevention and moderation escalation configured.
- [ ] Appeals process documented and staffed.

## Commerce and work
- [ ] Payment provider integration configured and webhook signatures verified.
- [ ] Refund/dispute handling tested.
- [ ] Payout/KYC/legal requirements reviewed for the deployment jurisdiction.
- [ ] Order records are not treated as proof of payment, income, delivery or satisfaction.
- [ ] Employment/freelancing status is represented as a user/platform record, not independently verified employment unless evidence exists.

## AI / Automission
- [ ] Agent registry loaded.
- [ ] Each agent has a bounded scope.
- [ ] AI task events are auditable.
- [ ] High-impact actions require the documented human gate.
- [ ] Agent output cannot silently change verification status.
- [ ] Failure/retry/rollback paths tested.

## Research and independent verification
- [ ] Canonical source preserved.
- [ ] Stable claim IDs assigned.
- [ ] Supporting and counter-evidence indexed.
- [ ] Reproducible tests documented where applicable.
- [ ] Independent human review completed where required.
- [ ] Only then may the applicable claim status change under the evidence contract.

## Yatharth Currency
- [ ] Keep as research/design/testnet until legal, regulatory, technical and operational requirements are independently reviewed.
- [ ] Do not represent a conceptual design as legal tender, a payment instrument, or an investment.

## Status rule
A successful CI run means the tested code passed its CI checks. It does not by itself establish LIVE, AUTOMATED, financially operational, legally compliant, or INDEPENDENTLY_VERIFIED status.

## Schema source of truth
- [ ] Apply `server/sql/schema.sql` as the canonical baseline.
- [ ] Do not deploy the deprecated `server/schema.sql` reduced schema.
- [ ] Apply migrations in order and record the deployed migration state.

## Payment webhook gate
- [ ] Configure an external payment provider and a secret in the deployment secret manager.
- [ ] Verify provider signatures before changing order state.
- [ ] Test success, failure, refund, duplicate-event and replay handling.
- [ ] Never accept a client-supplied `paid` flag as payment proof.
