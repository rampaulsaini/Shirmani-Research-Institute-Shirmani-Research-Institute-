# AI/ML/NLP/Automission Operating Model

## Agent layers
L1 Intake; L2 Identity/Permission; L3 NLP Understanding; L4 Semantic/Knowledge; L5 Evidence/Provenance; L6 Safety/Abuse Detection; L7 Recommendation/Discovery; L8 Marketplace Matching; L9 Education; L10 Creative/Media; L11 Research/Comparison; L12 Customer Support; L13 Verification Gate; L14 Audit; L15 Automission Supervisor; L16 Federation; L17 Resilience/Recovery; L18 Public Status.

## Continuous loop
Observe -> classify -> act within policy -> record evidence -> validate -> monitor -> recover -> audit -> improve.

## Fail-closed requirements
Workflow success must never be labelled independent verification. Missing evidence, malformed provenance, unavailable credentials, failed policy checks and uncertain high-impact decisions enter a safe review state.

## Learning boundary
Evaluate ML/NLP using held-out tests, drift monitoring, error analysis and human review. Distinguish generated content from sourced evidence and author testimony.

## Security
Secrets remain in protected secret stores and never in prompts, public issues, logs or source files. Require least privilege, signed artifacts, audit logs and recovery procedures.
