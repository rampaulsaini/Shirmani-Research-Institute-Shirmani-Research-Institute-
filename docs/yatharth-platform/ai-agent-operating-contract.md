# Yatharth AI/ML/NLP Agent Operating Contract

## Objective
Provide a bounded autonomous control plane for the public platform while preserving human agency, safety, auditability and independent verification.

## Agent layers
1. Intake Agent — accepts structured and unstructured user events.
2. NLP Agent — language detection, transcription, extraction and normalization.
3. Semantic Agent — concepts, entities, topics and relationships.
4. Safety Agent — policy, abuse, fraud and risk signals.
5. Trust Agent — provenance, reputation signals and evidence links.
6. Discovery Agent — search, recommendation and personalization.
7. Creator Agent — drafting, transformation, translation and production assistance.
8. Commerce Agent — catalog, pricing rules, order routing and fulfillment signals.
9. Education Agent — learning paths, tutoring and assessment support.
10. Research Agent — source discovery, comparison and research packet generation.
11. Verification Agent — evidence-contract checks; never self-awards independent verification.
12. Support Agent — multilingual user support and case triage.
13. Automation Agent — schedules, queues, retries, dependency management and recovery.
14. Federation Agent — cross-repository/service orchestration with least privilege.

## Control model
Every agent action has:
- actor/agent identity
- input provenance
- policy context
- allowed capability scope
- action/result record
- confidence/uncertainty where meaningful
- rollback or appeal path where applicable

## Fail-closed actions
Require explicit human review or an independently governed process before irreversible/high-impact actions such as:
- account termination
- significant financial holds or releases
- legal/justice outcomes
- safety-critical interventions
- changes to independent verification status
- changes to canonical author-source records

## Continuous operation
Automission may continuously ingest, classify, queue, execute bounded tasks, test, audit, retry transient failures, escalate exceptions, publish approved status and generate recovery tasks.

It must not silently convert a planned capability into a live capability.

## ML/NLP lifecycle
Collect lawful/consented data -> preprocess -> train/evaluate -> bias/error tests -> deployment gate -> monitoring -> drift detection -> rollback.

## Privacy and security
Use data minimization, purpose limitation, access control, secrets isolation, audit logs, encryption where appropriate and user-facing privacy controls.

## Verification boundary
AI output, CI success, workflow counts, hashes and generated reports are engineering evidence. They are not by themselves independent human/scientific verification.

## Production readiness
A service is LIVE only after implementation, tests, deployment, monitoring, documentation and user-facing availability are all recorded.
