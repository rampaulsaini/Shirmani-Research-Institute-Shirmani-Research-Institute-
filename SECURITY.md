# Security Policy

## Security principles

This repository follows a preserve-first, least-privilege approach:

- Never commit passwords, API keys, access tokens, private keys, session credentials, or other private secrets.
- Store operational credentials only in GitHub Secrets, repository/environment secrets, or another approved secret store.
- Never print secret values, authentication headers, or credential-bearing URLs in workflow logs or generated artifacts.
- Workflows must request only the GITHUB_TOKEN permissions they actually need.
- Untrusted pull-request or external payload content must never be executed as trusted code.
- Federation inputs are treated as data until validated; no untrusted payload is executed automatically.
- Human review remains required before irreversible actions and before any research material is promoted to a verified status.
- Generated research, drafts, metrics, and automation output must not be represented as independently verified facts unless the verification record explicitly supports that status.

## GitHub Actions safety

Changes to workflows should preserve:

1. Explicit least-privilege permissions.
2. Safe handling of repository dispatch and workflow-dispatch inputs.
3. No execution of code supplied by untrusted forks or external payloads in a privileged workflow.
4. No exposure of repository or cross-repository credentials.
5. Deterministic, traceable generated artifacts.
6. Fail-closed integrity and verification gates where appropriate.

Third-party actions should be reviewed before adoption and kept up to date. Where practical, security-sensitive workflows should pin third-party actions to reviewed commit SHAs.

## Private information

Do not place personal, authentication, financial, credential, or other confidential information in source files, generated public JSON/JSONL, GitHub Pages documentation, issue/PR comments, workflow logs, or committed configuration files.

If private information is accidentally committed, rotate the affected credential first and then remove the exposed material using an appropriate history-remediation process. Removing a file from the latest commit alone does not make an exposed credential safe.

## Reporting a vulnerability

For a suspected security vulnerability or accidental secret exposure, avoid publishing sensitive details in a public issue. Use GitHub repository security reporting/private vulnerability reporting facilities when available, or contact the repository owner through a private channel.

Please include only the minimum information needed to reproduce the issue.

## Integrity boundary

Automation may prepare, validate, package, archive, and route material. Automation must not silently convert unverified material into a verified research claim.

> Preserve first. Reason second. Verify third. Transform only as a traceable derivative.
