# Public Feature State Machine

Every public capability must have an explicit machine-readable lifecycle.

## States

- IDEA — proposed concept.
- DESIGNED — public contract and acceptance criteria exist.
- IMPLEMENTED — code/configuration exists.
- TESTED — automated tests pass against acceptance criteria.
- DEPLOYED — released to the intended environment.
- OBSERVED — post-deployment behavior has been monitored.
- MAINTAINED — operational ownership, monitoring and recovery are defined.
- BLOCKED — a dependency, safety, legal or technical gate is unmet.
- RETIRED — intentionally removed from public service.

## Rules

Documentation alone cannot move a feature to DEPLOYED. CI success cannot by itself establish VERIFIED research claims. AI-generated output cannot be treated as independent human evidence without an appropriate evidence contract. Financial, justice, identity, health, safety and other high-impact capabilities require additional controls. Every deployed feature needs an owner, dependency record, monitoring signal, rollback/recovery path and user-facing failure behavior.

## Public categories

The registry should cover Social, Research, Education, AI, Music/Media, Freelancing, Employment, Business, Digital Store, Economy, Currency research, Justice research, Community, Nature/Humanity, Verification/Trust, Creator Studio, Dashboard and Support.

## Success measurement

Use separate metrics for availability, latency, successful task completion, user satisfaction, safety incidents, appeals, transaction success, research verification status and environmental indicators. Do not collapse these into one overall percentage.
