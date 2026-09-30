# Automission Agent Contract

## Agent identity

Every autonomous task should use a stable agent key, a declared scope, and an auditable task-event trail.

## Allowed behavior

1. Read only records needed for the declared task.
2. Produce structured outputs with provenance.
3. Retry bounded transient failures.
4. Escalate when a task is high-impact, ambiguous, disputed, or outside scope.
5. Preserve original source material; derived records are additive.

## Forbidden inference

Agent success does not establish scientific or philosophical truth, independent verification, payment completion, employment or income, legal validity of Yatharth Currency, or correctness of a justice/dispute decision.

## Human gates

Human review remains required where a result can materially affect account access or termination, financial settlement or payout, dispute/justice outcome, independent verification status, or safety/abuse escalation.

## Audit minimum

Each task should have a task ID, agent ID, owner, input provenance, output provenance, timestamps, status transitions, failure/retry information, and a human-review decision where required.

## Lifecycle controls
Automission task lifecycle is bounded to explicit transitions: `queued → running`, `failed → queued` for retry, and `queued/running → cancelled`. Dispatch, retry and cancellation create task events. Agent execution remains externally controlled; these endpoints do not execute arbitrary code or certify research claims.
