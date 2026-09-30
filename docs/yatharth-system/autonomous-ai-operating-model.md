# Autonomous AI / ML / NLP / Automission Operating Model

## Objective
Create a continuously operating, fail-closed automation layer for the public Yatharth platform.

## Agent planes
1. Intake Agent — receives content, profiles, requests, products, reports.
2. NLP Agent — language detection, extraction, classification, summarization, translation.
3. Safety Agent — abuse, fraud, privacy, security, harmful-content signals.
4. Knowledge Agent — semantic linking, retrieval, source provenance.
5. Evidence Agent — evidence discovery and evidence/counter-evidence mapping.
6. Marketplace Agent — buyer/seller/service matching.
7. Education Agent — learning pathways and adaptive resources.
8. Creator Agent — media, music, publishing and product assistance.
9. Customer Care Agent — multilingual support and resolution routing.
10. Audit Agent — continuous quality, traceability and anomaly checks.
11. Federation Agent — coordinates repositories and services.
12. Automission Supervisor — schedules, observes, retries, escalates and records outcomes.

## ML/NLP requirements
- multilingual text and speech processing
- semantic search and entity/concept linking
- recommendation with user controls
- anomaly and fraud detection
- quality and duplicate detection
- model/version provenance
- evaluation datasets and regression tests

## Fail-closed rules
Automation must not mark a claim VERIFIED merely because an AI model, workflow, citation, hash, or CI check succeeds. Independent verification remains a separate evidence contract.

## Human control
Account suspension, major financial actions, legal/justice outcomes, safety escalations and independent verification must have appropriate human review and appeal pathways.

## Operational states
PLANNED -> BUILT -> TESTED -> STAGED -> LIVE -> MONITORED -> DEGRADED -> RECOVERY.

The architecture must expose actual state rather than claiming future capability is already deployed.
