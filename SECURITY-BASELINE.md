# Shirmani Research Institute — Security Baseline

Updated: 2026-10-10

## Scope and honest status
This baseline adds repeatable repository-level checks. It does **not** prove that the live website, accounts, third-party providers, APIs, payment flow, or every dependency is secure. No claim of complete protection, penetration testing, or “100% secure” status is made.

## Defense layers
1. **Account and repository access:** enable passkeys/2FA on GitHub; use least-privilege collaborators; review Actions permissions and branch protection.
2. **Secret handling:** never commit API keys, provider tokens, passwords, private customer data, or voice-provider credentials. Store required secrets in GitHub Actions Secrets; rotate exposed credentials immediately.
3. **Build/workflow safety:** pin third-party Actions to reviewed full commit SHAs before production use; set minimal permissions; avoid `pull_request_target` with untrusted code; review workflow changes.
4. **Web application:** use HTTPS, a restrictive Content Security Policy, secure form handling, output encoding, dependency updates, and no payment-card collection on a static page. Use a reputable hosted checkout provider when ready.
5. **AI/voice safety:** use voice/face assets only with permission; disclose synthetic media where appropriate; do not clone third parties without authorization; keep user input separate from system instructions; never expose secrets in prompts or logs.
6. **Evidence and production:** distinguish generated artifacts from tested artifacts. Record tool version, source, timestamp, test result, and limitations. Never mark a product “verified” solely because a workflow passed.
7. **Recovery:** retain version history, document rollback, and test restore procedures.

## Release gates
- [ ] Review a dedicated secret scan and triage false positives.
- [ ] Review dependency and workflow changes.
- [ ] Confirm public pages contain no credentials or private customer data.
- [ ] Confirm forms disclose what is collected and where it is sent.
- [ ] Use hosted checkout; do not store card data in this repository.
- [ ] Ensure product demos are real, product-specific, and labelled if simulated.
- [ ] Establish a private security-reporting route before inviting external testing.

## Incident response
If a credential is exposed: revoke/rotate it first, review access/logs, then clean history if needed. Deleting a secret from the latest commit alone does not make it safe.

## Current implementation boundary
The repository is a public static GitHub Pages site plus GitHub Actions workflows. A static site cannot securely hold server secrets or independently process protected payments. Production payment, authenticated customer accounts, private email delivery, large-scale video rendering, and real-time avatar/lip-sync require authorized external services or a backend and must not be represented as active unless an end-to-end test proves it.
