# Guarded AI Code Agent

## Purpose
Reduce repetitive manual engineering by proposing one small, evidence-based API improvement per scheduled run.

## Execution
- GitHub Actions runs daily at 10:00 Asia/Kolkata and on manual dispatch.
- It waits while API safety PR #3690 is open to avoid overlapping changes.
- It requires the repository secret `OPENAI_API_KEY`. Optional repository variable `OPENAI_CODE_AGENT_MODEL` selects an enabled model; default is `gpt-5-codex`.
- Missing API key causes a safe skip; no patch is made.
- The agent receives only tracked Node API source and tests, and may propose one patch at most.
- Only `server/src/index.js` and `server/test/*.test.js` are permitted.
- Syntax check and the complete Node test suite must pass before a Draft PR is created or updated.

## Hard safety boundaries
- Never merge, deploy, change secrets, alter production data, run migrations, or enable payment-provider/webhook acceptance.
- Preserve `paid_orders` as canonical income evidence; do not invent or infer sales.
- Keep health liveness independent from database readiness.
- Fail closed if output is malformed, patch paths are outside the allowlist, patch does not apply, or tests fail.
- Human review and explicit approval are required for merge and deployment.

## Evidence labels
A successful workflow means only that the patch passed the configured checks. It does not prove production deployment, public availability, independent verification, actual sales, payment, dispatch, or delivery.
