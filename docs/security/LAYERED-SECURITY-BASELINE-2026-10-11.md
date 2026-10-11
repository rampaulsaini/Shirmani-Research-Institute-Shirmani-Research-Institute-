# Layered Security Baseline — Initial Release

## What this automation does

The workflow `.github/workflows/layered-security-baseline.yml` runs GitHub CodeQL static analysis for JavaScript/TypeScript and Python on pushes and pull requests to `main`, weekly, and on manual dispatch. It uses the `security-extended` query suite and uploads findings to GitHub code scanning when repository settings and plan support it.

## Security layers and next actions

1. **Static analysis (automated here):** review CodeQL alerts; triage each finding and fix confirmed issues.
2. **Secrets:** enable GitHub secret scanning and push protection in repository settings where available; rotate any exposed credential immediately. Never put tokens in source files or logs.
3. **Dependencies and actions:** inventory direct dependencies; pin third-party actions to full commit SHAs before production use; add dependency review to pull requests when dependency manifests exist.
4. **Workflow permissions:** default to least privilege; individual workflows should request only permissions they need. Review any workflow that writes branches, publishes Pages, sends messages, or accesses secrets.
5. **Public input/output safety:** validate user input, escape output, avoid unsafe DOM sinks, and do not store customer briefs or private contact data in public artifacts.
6. **Recovery:** keep an owner-reviewed recovery procedure and verify that generated production state can be rebuilt from source.

## Honest status

- Workflow file: added to the proposed change branch.
- Scan execution: **pending a GitHub Actions run**; this change alone is not evidence that a scan completed.
- Findings: **not yet assessed**; do not report the repository as secure until a run is completed and alerts are triaged.
- This is defensive scanning of the user's own repository, not a penetration test and not authorization to test third-party systems.

## Release gates

- [ ] Workflow completes successfully on GitHub Actions.
- [ ] CodeQL findings reviewed and assigned severity/owner.
- [ ] Critical/high confirmed findings fixed or documented with a time-bound exception.
- [ ] Secret scanning/push protection settings reviewed.
- [ ] Write-enabled workflows reviewed for least privilege and branch safety.
- [ ] Public showroom still builds and all changed links resolve.
