# Yatharth Mudra Honour Verification v1

This module defines a voluntary, evidence-aware honour review. It is **not** a token, financial product, scientific psychometric test, medical assessment, or proof of a person's inner state.

## Files
- `yatharth-mudra-verification.json`: policy, seven levels, reviewer and issuance gates.
- `yatharth-mudra-verification.schema.json`: JSON Schema contract for a case/certificate record.
- `yatharth-mudra-verification.sql`: PostgreSQL starter migration.

## Seven levels
The weights are 10, 15, 15, 15, 15, 20 and 10 percent (100% total). They are rubric weights for evidence review, not a measured percentage of a person's heart, consciousness or realization. The creator-defined 99.9999% / 0.0001% framing is preserved as philosophical metadata only.

## Mandatory issuance gates
1. Subject consent is recorded.
2. Evidence is supplied for all seven levels.
3. 365-day continuity is documented where applicable; no fasting, deprivation, isolation, silence or self-harm is required.
4. Three distinct reviewers authenticate, check conflicts and independently accept the same evidence digest.
5. Canonical JSON uses RFC 8785 JCS; SHA-256 detects payload changes. A hash proves integrity, not truth or reviewer identity.
6. A human-controlled issuance action creates the certificate. No scheduled workflow or AI agent can self-approve or mint it.
7. Corrections, appeals and revocations are recorded as new audit events.

## Privacy and safety
Do not publish private diaries, health information, contact details, identity documents or minors' data. Store sensitive evidence outside the public repository with access controls; publish only minimal metadata and hashes. A person may withdraw consent. Hardship, complaints, food insecurity or asking for help never reduce a score.

## Value statement
The proposed INR 1,000,000,000 figure is only a creator-declared symbolic honour reference. It is not legal tender, a market valuation, an investment, redeemable, guaranteed or payable. This module does not create a debt or payment obligation.

## Not yet production-ready
Before connecting a live database: review SQL with a database administrator, configure least-privilege roles and row-level security, add authenticated reviewer identity/signature verification, private evidence storage, retention/deletion procedures, appeal workflow, tests and legal/privacy review. No database has been provisioned or connected by this PR.
