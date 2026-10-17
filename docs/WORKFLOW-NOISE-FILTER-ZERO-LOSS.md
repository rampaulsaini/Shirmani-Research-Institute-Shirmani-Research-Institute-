# SHIRMANI Workflow Noise Filter — Zero-Loss Policy

## Purpose
Reduce avoidable automation noise and duplicated work without damaging useful production, security, persistence, or recovery behavior.

## Current tool
Run the read-only inventory from the repository root:

\`\`\`bash
python scripts/workflow_noise_audit.py > workflow-noise-audit.json
python -m unittest tests/test_workflow_noise_audit.py -v
\`\`\`

The report inventories \`.github/workflows/*.yml\` and \`*.yaml\`, computes SHA-256 fingerprints, flags exact-content duplicates, duplicate workflow names, manual-dispatch-only workflows, write permissions, cancellation behavior, critical-review hints, concurrency groups, and local \`workflow_run\` dependency references. These are review leads, not deletion recommendations.

## Zero-loss rules
1. No workflow or file is automatically deleted, disabled, or rewritten by the audit.
2. Keep security scanning, deployment, persistence, data-integrity, backups, rollback, and recovery paths unless a replacement is demonstrated and independently verified.
3. A workflow that is skipped because its event filter did not match is not necessarily broken or useless.
4. A cancelled workflow is not the same as a failed workflow. Inspect its event, concurrency group, run history, and downstream dependencies.
5. Duplicate-looking workflows may have different triggers, permissions, environments, or operational purposes. Compare full behavior before consolidation.
6. Any retirement proposal must include a dependency map, replacement evidence, branch-only test, reviewer approval, and rollback plan.
7. Run the audit in pull requests and manually; do not commit generated reports to the production branch automatically.
8. Do not treat a keyword-based criticality hint or a local dependency match as complete proof. Review reusable workflows, scripts, artifact producers/consumers, external repositories, schedules, and runtime dependencies separately.

## Interpretation
- **Exact-content duplicate:** likely redundant file contents, but references and workflow identity still need review.
- **Duplicate name:** a signal to compare triggers and jobs, not proof of duplicate behavior.
- **Manual-dispatch-only:** may be an intentional fallback or emergency operation.
- **Write permission:** review least privilege; do not remove needed persistence permissions blindly.
- **Cancel-in-progress:** inspect the concurrency group. Cancelling stale read-only checks may be fine; cancelling production writers or deployments can be harmful.
- **Critical-review hint:** keyword-based triage aid only; a human must confirm the actual role and blast radius.
- **Workflow-run dependency:** local name mapping only. An unresolved name may refer to a renamed, external, or otherwise non-local workflow; investigate before changing it.

## Safe optimization cycle
1. Inventory workflow paths, declared names, triggers, permissions, concurrency groups, workflow-run dependencies, and file hashes.
2. Compare recent run outcomes and durations, including pending, skipped, cancelled, failed, and successful states.
3. Map outputs to real consumers and user-facing product outcomes.
4. Select one low-risk candidate; record expected runtime reduction and coverage risks.
5. Test the proposed change on a branch and compare before/after behavior.
6. Require review and a rollback path before any disablement or removal.
7. Confirm the latest required production, security, persistence, and deployment checks actually ran and have evidence.

## Scope boundary
This tool inventories workflow files in the current repository only. It does not claim to audit all repositories, external providers, production secrets, deployed services, live user journeys, or every dependency. It does not execute workflows, inspect run history, delete files, or certify production health. Those require separate evidence.
