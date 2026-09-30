# AI / ML / NLP / Automission Operating Model

## Objective

Provide a bounded autonomous operating model for the Yatharth public platform while preserving human agency, safety, auditability and independent verification.

## Agent layers

### L1 — Intake
Ingest user content, product records, reports, telemetry and approved research inputs.

### L2 — NLP understanding
Language detection, transcription, entity/concept extraction, semantic classification, summarization and multilingual normalization.

### L3 — Trust and safety
Spam, abuse, fraud indicators, unsafe content and policy-routing signals. High-impact decisions require defined review and appeal paths.

### L4 — Discovery and matching
Search indexing, recommendations, creator discovery, course discovery, service matching and marketplace relevance.

### L5 — Research intelligence
Claim extraction, evidence mapping, counter-evidence mapping, source provenance and comparison support.

### L6 — Commerce intelligence
Catalog quality, permitted marketplace matching, transaction-state reconciliation and customer-support routing.

### L7 — Education intelligence
Learning-path generation, tutoring assistance, translation, assessment assistance and accessibility support.

### L8 — Creative intelligence
Music/audio/video assistance, multilingual transformation and creator workflow support.

### L9 — Automission supervisor
Schedules agents, checks dependencies, records receipts, detects failures, retries bounded jobs and escalates exceptions.

### L10 — Audit and verification gate
Maintains immutable-ish audit records, status transitions, evidence contracts and independent-review queues.

## Autonomy boundaries

Automission may autonomously perform routine, reversible operations with defined contracts.

It must not silently make irreversible high-impact decisions about:

- legal rights or justice outcomes;
- large or exceptional financial actions;
- permanent account removal without an appeal path;
- independent scientific verification;
- medical diagnosis or treatment;
- political persuasion or electoral targeting;
- access to essential services.

## Human-in-the-loop controls

High-impact actions require an appropriate human authority, reviewer or appeal process. The system should expose:

- reason codes;
- evidence used;
- action history;
- confidence/uncertainty where meaningful;
- appeal route;
- rollback or remediation path where technically possible.

## ML lifecycle

Collect only necessary data → quality check → label/provenance → train/evaluate → bias/error testing → staged deployment → monitoring → drift detection → rollback.

A model is not treated as verified merely because it passes a software CI workflow.

## NLP quality

Track language coverage, transcription quality, extraction precision/recall where measurable, ambiguity, hallucination/error reports and human-review disagreement.

## Automission health

Track separately:

- scheduled jobs;
- successful jobs;
- failed jobs;
- retried jobs;
- blocked jobs;
- human escalations;
- latency;
- stale queues;
- unresolved incidents.

Do not collapse these into a single “truth” or “verification” percentage.

## Security

Secrets stay in approved secret stores and are never written to source, issues or logs. Agent permissions should follow least privilege. Every action should have a traceable actor/agent identity and scope.

## Deployment states

Architecture → Prototype → Tested → Staged → Limited Live → Live → Monitored.

Workflow success proves automation execution, not product readiness or independent verification.
