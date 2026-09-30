# AI/ML/NLP + Automission Operating Model

## Objective

Define the machine-operating layer behind the public Yatharth platform. This is an architecture and implementation contract, not a claim that all components are already deployed.

## Agent layers

### L0 — Policy and safety kernel
Defines platform rules, permissions, privacy boundaries, escalation thresholds and fail-closed behavior.

### L1 — Identity and account agent
Handles account lifecycle, profile configuration, permissions, recovery signals and abuse-resistant onboarding.

### L2 — Content/NLP agent
Ingests text, audio transcripts, metadata and multilingual content; extracts topics, entities, claims, language and provenance.

### L3 — Semantic knowledge agent
Builds relationships among people, concepts, products, research records, educational resources and evidence.

### L4 — Research/evidence agent
Finds candidate sources, maps evidence and counter-evidence, detects missing citations and prepares research packets.

### L5 — Creator agent
Assists with writing, audio, music, video, translation, packaging, publishing and product metadata.

### L6 — Education agent
Builds learning paths, explains concepts, creates practice material and tracks learning progress without fabricating credentials.

### L7 — Marketplace agent
Matches buyers, sellers, freelancers, jobs, services, products and learning resources.

### L8 — Trust/safety agent
Detects spam, fraud, impersonation, coordinated abuse, unsafe content and suspicious marketplace behavior; routes high-impact cases to review.

### L9 — Recommendation agent
Provides user-controlled discovery and recommendations. It must expose meaningful controls and avoid manipulative engagement optimization.

### L10 — Customer-support agent
Provides multilingual first-line support, identifies unresolved issues and escalates according to policy.

### L11 — Automission supervisor
Coordinates jobs, retries, dependencies, health checks, queues, federation and recovery across repositories and services.

### L12 — Audit/verification gate
Maintains immutable-ish provenance records, decision logs and independent-review states. It cannot mark a claim VERIFIED merely because an AI model or workflow succeeds.

## ML/NLP capabilities

The architecture may support:
- multilingual classification;
- semantic search and embeddings;
- clustering and topic discovery;
- entity linking;
- contradiction detection;
- recommendation;
- anomaly detection;
- quality prediction;
- fraud signals;
- personalization with user controls;
- speech-to-text/text-to-speech;
- translation;
- content moderation.

Model outputs remain probabilistic. Critical actions require policy checks and appropriate review.

## Autonomy levels

- A0: manual
- A1: AI suggestion
- A2: AI execution with confirmation
- A3: bounded autonomous execution
- A4: autonomous execution with continuous monitoring
- A5: cross-system autonomous orchestration

Each action must declare its autonomy level. Financial, legal, account-removal, justice and independent-verification decisions must have stricter controls.

## Observability

Every automated action should have:
- actor/agent identity;
- timestamp;
- input/output references;
- policy version;
- model/version identifier where applicable;
- confidence or uncertainty where meaningful;
- escalation status;
- audit reference.

## Fail-closed rules

When provenance, authorization, policy or critical evidence is missing, the system must stop or downgrade the action rather than inventing certainty.
