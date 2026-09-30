# AI Agent, ML, NLP and Automission Operating Contract

## Mission

Coordinate specialized agents as a continuously audited system rather than treating one model as an all-purpose authority.

## Agent layers

### L1 — Intake
Receives user content, marketplace submissions, research material, reports, and platform events.

### L2 — NLP Understanding
Performs language detection, transcription where applicable, entity extraction, claim extraction, semantic normalization, classification, and multilingual alignment.

### L3 — Safety and Policy
Checks content, privacy, abuse, fraud, security, and platform-policy constraints. High-risk actions can be held for human review.

### L4 — Evidence and Research
Finds sources, builds evidence maps, records counter-evidence, tracks provenance, and identifies uncertainty.

### L5 — Personalization and Discovery
Provides search, recommendation, matching, and learning-path functions with user controls and transparency.

### L6 — Commerce and Services
Supports permitted listings, creator services, freelancing, digital delivery, customer support, reviews, and dispute intake.

### L7 — Governance
Applies policy contracts, audit rules, escalation thresholds, access controls, and appeal routes.

### L8 — Verification Gate
Prevents unsupported claims from being promoted to independently verified status.

### L9 — Automission Supervisor
Coordinates queues, retries, dependencies, health checks, federation, and recovery.

### L10 — Public Presentation
Publishes only the status that the underlying evidence and deployment state actually support.

## ML responsibilities

ML systems may classify, rank, detect patterns, forecast operational load, identify anomalies, and improve matching. They must be monitored for drift, false positives, false negatives, unfair outcomes, and degraded performance.

## NLP responsibilities

NLP must preserve source meaning, uncertainty, attribution, language, and provenance. Summarization must not silently convert an author's experience into an independently established fact.

## Fail-closed rules

- Missing provenance → do not mark verified.
- Conflicting evidence → expose the conflict.
- High-impact uncertainty → escalate.
- Safety failure → block or quarantine the action.
- Failed critical dependency → stop the dependent automation.
- Model degradation → fall back to a safer mode.
- User appeal → preserve the record and provide a review path.

## Human oversight

Routine operations may be highly automated. Decisions with significant effects on rights, money, access, safety, account status, disputes, or independent verification require appropriate human oversight and appeal mechanisms.
