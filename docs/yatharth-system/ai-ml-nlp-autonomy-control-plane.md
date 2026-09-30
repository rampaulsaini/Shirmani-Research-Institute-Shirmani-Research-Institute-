# AI/ML/NLP Autonomy Control Plane

## Objective
Provide a unified control plane for autonomous routine operations across the Yatharth public platform while preserving safety, auditability, and human agency.

## Agent layers
1. Intake Agent — receives events and user submissions.
2. NLP Agent — extracts language, entities, claims, topics, sentiment, and intent.
3. Policy Agent — applies published platform rules.
4. Safety Agent — detects abuse, fraud indicators, security anomalies, and harmful patterns.
5. Knowledge Agent — links content to the research and evidence graph.
6. Marketplace Agent — routes products, services, buyers, sellers, and support requests.
7. Education Agent — recommends learning pathways and resources.
8. Creative Agent — assists permitted music, audio, video, and publishing workflows.
9. Verification Agent — prepares evidence packets; it cannot independently certify its own output.
10. Audit Agent — records decisions, provenance, failures, and reversals.
11. Federation Agent — coordinates approved repositories/services.
12. Recovery Agent — detects failed automations and safely retries or escalates.

## ML/NLP functions
Potential production functions include semantic retrieval, classification, entity/concept linking, recommendation, anomaly detection, duplicate detection, multilingual translation, ranking with transparent criteria, fraud-risk signals, quality prediction, and personalization with privacy controls.

## Automission state machine
INTAKE -> UNDERSTAND -> CHECK -> ROUTE -> ACT -> VERIFY -> AUDIT -> COMPLETE

Failure path:
ANY_STATE -> SAFE_HALT -> DIAGNOSE -> RETRY_OR_ESCALATE

## Human-control boundaries
The system must not silently make irreversible high-impact decisions. Examples requiring stronger controls include account termination, large financial holds, legal/judicial determinations, denial of essential services, identity disputes, and independent scientific verification.

These require documented criteria, notification, appeal, and human oversight as appropriate.

## No false autonomy claim
A GitHub Actions workflow, successful CI run, or generated document does not by itself prove that the full AI/ML/NLP system is operational. Production readiness requires deployed services, tests, monitoring, security controls, data governance, and observed end-to-end behavior.

## Public status
The public dashboard should expose separate states for architecture, implementation, testing, deployment, automation, verification, human review, and incidents.

This prevents planned capabilities from being presented as live capabilities.
