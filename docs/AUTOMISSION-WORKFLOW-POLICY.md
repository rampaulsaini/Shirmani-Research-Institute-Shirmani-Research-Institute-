# Automission Workflow Policy

## Objective

Keep automation fast without creating duplicate schedulers, hidden retries, or false
success signals.

## Canonical control plane

1. `shirmani-multi-automation-supervisor.yml` — bounded orchestration and retry.
2. `shirmani-resilience-watchdog.yml` — bounded recovery for selected critical flows.
3. `shirmani-supreme-ai-ml-nlp-quality.yml` — deterministic quality gate.
4. `independent-verification-gate.yml` — independent verification boundary.
5. `failure-intelligence.yml` — diagnostics only; it must not promote records to verified.

## Retry policy

- Retry only scheduled/manual first-attempt failures.
- Never treat a rerun as independent verification.
- Do not create retry storms.
- Keep failures visible in machine-readable diagnostics.

## Cleanup policy

Obsolete duplicate workflow definitions should be deleted from source control rather
than merely ignored. Historical failed GitHub Actions runs are retained by GitHub and
are not erased by deleting a YAML workflow file.

## Accuracy policy

No workflow may claim perfect accuracy merely because deterministic tests pass.
Scores are quality indicators; evidence and independent verification remain separate.

## Multimodal NLP policy

Sensor, image, audio, bioelectric, environmental, or other measurable signals may be
translated into plain language. The system must distinguish:
- measurement,
- detected pattern,
- model classification,
- hypothesis,
- confidence,
- independently supported conclusion.

A signal-to-NLP translation must not be presented as proof of subjective experience
without appropriate evidence.
