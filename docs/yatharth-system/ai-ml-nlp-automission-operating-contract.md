# AI/ML/NLP/Automission Operating Contract

## Objective

Build toward a continuously operating AI-assisted platform while preserving fail-closed controls, observability and human appeal.

## Agent layers

1. Intake Agent — receives structured events and user content.
2. NLP Agent — language detection, extraction, summarization and semantic normalization.
3. Safety Agent — policy, abuse, privacy and security checks.
4. Knowledge Agent — retrieval and evidence linkage.
5. Recommendation Agent — discovery and personalization with user controls.
6. Commerce Agent — listings, catalog quality and transaction workflow assistance.
7. Education Agent — learning-path and resource assistance.
8. Creator Agent — media and creative workflow assistance.
9. Research Agent — claim/evidence/comparison packet generation.
10. Verification Gate Agent — enforces evidence-state transitions without declaring unsupported claims verified.
11. Federation Agent — coordinates approved repository/platform events.
12. Audit Agent — continuous health, traceability and anomaly reporting.
13. Recovery Agent — bounded retry, rollback and incident escalation.
14. Human Review Router — routes high-impact or ambiguous cases to human review.

## ML/NLP requirements

Models and pipelines should record version, input class, output class, confidence where meaningful, policy decision, evidence references and failure state.

## Automission loop

Sense → classify → plan → act within permissions → test → record → audit → recover/escalate → repeat.

## Autonomous-operation boundary

Routine low-impact tasks may be automated. Actions affecting legal rights, substantial financial value, account termination, safety-critical decisions, justice/dispute outcomes or independent verification require bounded authority and human appeal/review.

## Fail-closed rules

If required evidence, policy context, authorization, identity of the acting service, or audit trail is missing, the action must stop or downgrade to review.

## Production truth

CI success means the tested software path succeeded. It does not prove that the social, economic, scientific or philosophical outcome is true or beneficial.
