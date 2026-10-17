# SHIRMANI Workflow Noise Filter — Zero-Loss Policy

## Purpose
Reduce avoidable automation noise and duplicated work without damaging useful production, security, persistence, or recovery behavior.

## Current tool
Run the read-only inventory from the repository root:

```bash
python scripts/workflow_noise_audit.py > workflow-noise-audit.json
python -m unittest tests/test_workflow_noise_audit.py -v
```

The report fingerprints workflow files with SHA-256, records triggers, schedule expressions, concurrency groups and cancellation settings, and scans likely source/config/documentation paths for literal workflow references. It flags exact-content duplicates, duplicate workflow names, manual-dispatch-only workflows, write permissions, and cancellation behavior. These are review leads, not deletion recommendations.

## Zero-loss rules
1. No workflow or file is automatically deleted, disabled, or rewritten by the audit.
2. Keep security scanning, deployment, persistence, data-integrity, backups, rollback, and recovery paths unless a replacement is demonstrated and independently verified.
3. A workflow that is skipped because its event filter did not match is not necessarily broken or useless.
4. A cancelled workflow is not the same as a failed workflow. Inspect its event, concurrency group, run history, and downstream dependencies.
5. Duplicate-looking workflows may have different triggers, permissions, environments, or operational purposes. Compare full behavior before consolidation.
6. Literal references are leads for dependency review. No detected reference is not proof that a workflow is unused; dynamic references and external callers may not be discoverable by a text scan.
7. Any retirement proposal must include a dependency map, replacement evidence, branch-only test, reviewer approval, preserved history, and rollback plan.
8. Run the audit in pull requests and manually; do not commit generated reports to the production branch automatically.
9. Never enable blanket `cancel-in-progress: true` or blind retry loops to reduce noise. Production writers and deployments require safe serialization and bounded, diagnosed retries.

## Interpretation
- **Exact-content duplicate:** compare references, triggers, required-check identity, permissions and recent run history before considering retirement.
- **Duplicate name:** a signal to compare triggers and jobs, not proof of duplicate behavior.
- **Manual-dispatch-only:** may be an intentional fallback or emergency operation.
- **Write permission:** review least privilege; do not remove needed persistence permissions blindly.
- **Cancel-in-progress:** inspect the concurrency group. Cancelling stale read-only checks may be fine; cancelling production writers or deployments can be harmful.
- **Schedule and concurrency metadata:** provide context for human review; this audit does not prove run-time health or estimate savings.

## Scope boundary
This tool inventories workflow files in the checked-out repository and searches likely local text references in `.github`, `scripts`, `docs`, and selected root files. It does not prove that a workflow is unused, audit all repositories, inspect external provider settings/secrets, or verify deployed services and live user journeys. Those require separate evidence.
