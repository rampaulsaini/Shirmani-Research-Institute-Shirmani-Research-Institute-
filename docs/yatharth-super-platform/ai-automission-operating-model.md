# AI / ML / NLP / Automission Operating Model

## Agent layers

### L1 — Intake Agent
Accepts structured and unstructured user inputs and routes them to the correct domain.

### L2 — NLP Understanding Agent
Language detection, transcription, entity/concept extraction, summarization, classification and semantic indexing.

### L3 — Trust & Safety Agent
Spam, abuse, fraud indicators, unsafe-content signals, provenance checks and escalation.

### L4 — Discovery Agent
Search, semantic retrieval, recommendations and multilingual discovery.

### L5 — Creator Agent
Assists with drafting, editing, translation, media metadata, product packaging and publishing workflows.

### L6 — Education Agent
Learning-path generation, tutoring, assessment support and accessible explanations.

### L7 — Research Agent
Claim extraction, source mapping, evidence/counter-evidence mapping, comparative analysis and research packets.

### L8 — Commerce Agent
Catalog, matching, order routing, customer support, review analysis and marketplace quality signals.

### L9 — Work Agent
Freelance/project matching, service discovery, job routing and workflow coordination.

### L10 — Verification Gate
Keeps author-source claims, evidence-mapped claims and independently verified claims separate.

### L11 — Automission Supervisor
Schedules, observes, retries and coordinates bounded workflows.

### L12 — Federation Agent
Coordinates approved work across repositories/services and records delivery receipts.

### L13 — Audit & Recovery Agent
Detects failures, records provenance, triggers bounded recovery and reports unresolved exceptions.

## ML/NLP maturity rule

A model, workflow or agent is not considered production-ready merely because it exists in code. Each capability needs:

1. defined input/output contract;
2. evaluation dataset or test cases;
3. safety constraints;
4. quality thresholds;
5. observability;
6. rollback/recovery;
7. privacy/security review;
8. human appeal path for high-impact outcomes.

## Autonomy boundary

Routine, low-impact operations may be automated. Account sanctions, major financial actions, legal disputes, justice decisions, sensitive access changes and independent verification require explicit governance controls and appropriate human oversight.

## Satisfaction objective

Optimize for measurable user value: safety + usefulness + accessibility + quality + fairness + reliability + transparent pricing + responsive support.

Do not optimize solely for time-on-platform.
