# Shirmani Supreme — Layered Security Baseline
**Date:** 2026-10-14  
**Status:** Proposed baseline committed on a feature branch; it is not yet merged or confirmed passing.

## Goal
Protect the repository and customer-facing production pipeline before expanding AI, avatar, voice, outreach, and commerce features. This is a practical baseline, not a claim of complete security or certification.

## Layers
1. **Repository access:** enable MFA for maintainers; use least-privilege GitHub roles; protect the default branch; require pull requests and passing checks; restrict force-push and deletion.
2. **Secrets:** keep provider keys in GitHub Actions secrets or an approved secret manager; never place credentials in source, issue comments, demos, screenshots, QR payloads, or public logs. Rotate any key exposed in chat or commits.
3. **Workflow isolation:** minimal workflow permissions; disable persisted checkout credentials where possible; pin third-party actions to reviewed full commit SHAs before production hardening; use concurrency and timeouts.
4. **Static analysis:** run CodeQL for JavaScript/TypeScript and a lightweight committed-secret-pattern guard. The guard has limited coverage and can produce false positives/negatives; add a dedicated secret scanner and dependency/SBOM checks before calling the layer mature.
5. **Web application:** validate inputs, escape untrusted content, use safe DOM APIs, avoid unsafe HTML injection, set a restrictive Content Security Policy where hosting permits, and never place customer-submitted private information in public assets.
6. **Supply chain:** inventory dependencies, check licenses and known vulnerabilities, generate an SBOM for releases, and review dependency update PRs.
7. **AI/provider integration:** use authorised APIs only; store keys server-side; set usage limits; validate provider responses; isolate untrusted prompt/content; document retention and consent for voice/photo assets.
8. **Release/QC gate:** block publication when a critical security defect, broken demo, incorrect QR target, missing terms, or misleading capability claim remains unresolved.
9. **Monitoring and recovery:** keep dated run results, issue/incident log, backup and restore instructions, and a named response owner.

## New GitHub workflow
`.github/workflows/supreme-security-baseline.yml` is intended to run on pushes/PRs to main/master, weekly, and manually. It performs a narrow repository hygiene check and CodeQL JavaScript/TypeScript analysis.

## Required manual settings
- Protect `main` (or the actual default branch) and require this workflow's checks.
- Enable GitHub secret scanning and push protection if available for the account/repository.
- Review action versions and pin actions to full commit SHAs before treating the workflow as hardened.
- Add dependency review, lockfile checks, SBOM generation, and a dedicated secret scanner.
- Confirm the actual default branch name and workflow permissions in repository settings.

## Acceptance criteria
- [ ] Workflow appears in Actions and completes successfully at least once.
- [ ] CodeQL results are visible and reviewed.
- [ ] A harmless test fixture confirms the secret-pattern guard detects expected patterns without committing any real credential.
- [ ] Default branch protection is enabled and required checks are configured.
- [ ] Secrets are absent from repository history and logs; any exposed credentials are revoked/rotated.
- [ ] Restore procedure has been tested.

## Honest status
A workflow file in a branch does not prove the controls are active. Until merged, configured in repository settings, and run successfully, mark this layer **IMPLEMENTED IN BRANCH — NOT YET VERIFIED IN PRODUCTION**.
