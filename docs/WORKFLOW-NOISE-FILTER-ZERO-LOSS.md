# SHIRMANI Workflow Noise Filter — Zero-Loss Policy

## Purpose
Reduce avoidable automation noise and duplicated work without damaging useful production, security, persistence, or recovery behavior.

## Current tool
Run the read-only inventory from the repository root:

```bash
python scripts/workflow_noise_audit.py > workflow-noise-audit.json
python -m unittest tests/test_workflow_noise_audit.py -v
```

The report inventories `.github/workflows/*.yml` and `*.yaml`, computes SHA-256 fingerprints, and flags exact-content duplicates, duplicate workflow names, manual-dispatch-only workflows, write permissions, and cancellation behavior. These are review leads, not deletion recommendations.

## Zero-loss rules
1. No workflow or file is automatically deleted, disabled, or rewritten by the audit.
2. Keep security scanning, deployment, persistence, data-integrity, backups, rollback, and recovery paths unless a replacement is demonstrated and independently verified.
3. A workflow that is skipped because its event filter did not match is not necessarily broken or useless.
4. A cancelled workflow is not the same as a failed workflow. Inspect its event, concurrency group, run history, and downstream dependencies.
5. Duplicate-looking workflows may have different triggers, permissions, environments, or operational purposes. Compare full behavior before consolidation.
6. Any retirement proposal must include a dependency map, replacement evidence, branch-only test, reviewer approval, and rollback plan.
7. Run the audit in pull requests and manually; do not commit generated reports to the production branch automatically.

## Interpretation
- **Exact-content duplicate:** likely redundant file contents, but references and workflow identity still need review.
- **Duplicate name:** a signal to compare triggers and jobs, not proof of duplicate behavior.
- **Manual-dispatch-only:** may be an intentional fallback or emergency operation.
- **Write permission:** review least privilege; do not remove needed persistence permissions blindly.
- **Cancel-in-progress:** inspect the concurrency group. Cancelling stale read-only checks may be fine; cancelling production writers or deployments can be harmful.

## Scope boundary
This tool inventories workflow files in the current repository only. It does not claim to audit all repositories, external providers, production secrets, deployed services, or live user journeys. Those require separate evidence.
