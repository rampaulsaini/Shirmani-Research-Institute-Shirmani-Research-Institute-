# SHIRMANI Platform — Production Security Baseline
Version: 1.0
Status: implementation checklist; controls are not claimed enabled until independently checked.

## Purpose
Apply a practical security baseline to the repository, GitHub Actions, public showroom, product factory, customer enquiry paths, and future integrations. “AI”, “quantum”, or “ethical hacking” labels are not security controls. Only documented settings, tested behavior, and evidence count.

## Immediate repository controls
- [ ] Require pull requests for changes to the default branch; prohibit direct pushes for routine changes.
- [ ] Require at least one review for workflow, authentication, payment, customer-data, and release-gate changes.
- [ ] Require successful CI checks before merge; protect workflow files, release scripts, and dependency manifests with review rules where available.
- [ ] Enable secret scanning and push protection if available; rotate exposed credentials immediately.
- [ ] Set GitHub Actions permissions explicitly and default to contents: read.
- [ ] Pin third-party Actions to full commit SHAs; review updates and do not expose secrets to untrusted pull-request code.
- [ ] Use GitHub OIDC and scoped cloud roles rather than long-lived cloud keys wherever supported.
- [ ] Keep tokens, SMTP credentials, WhatsApp/API keys, signing keys, and payment secrets out of source, logs, generated artifacts, and public pages.
- [ ] Enable dependency alerts/security updates and dependency review where available; lock dependencies and remove abandoned packages.
- [ ] Publish SECURITY.md with a reporting route, response owner, severity process, and disclosure expectations.

## Public website and product factory
- [ ] Treat browser form inputs, uploads, generated text, and external source data as untrusted.
- [ ] Render user content as text; avoid unsafe HTML injection and dynamic code execution.
- [ ] Add a restrictive Content Security Policy, nosniff, Referrer-Policy, and appropriate frame restrictions after testing actual integrations.
- [ ] Use HTTPS-only official endpoints; never collect passwords or payment-card data in static pages.
- [ ] Minimize personal data; define purpose, retention, access, deletion, and consent rules before launching accounts or reviews.
- [ ] Validate file types and sizes for future uploads; scan files before processing and isolate parsers/renderers.
- [ ] Rate-limit server-backed APIs, authenticate admin operations, and prevent abuse/cost-exhaustion.
- [ ] Keep demos isolated from production credentials, customer records, and deployment privileges.

## Product release gates
Each product must have a versioned passport containing product ID/version/owner, intended use, prerequisites, limitations, licence, working demo or reproducible steps, screenshots and an actual demo video when advertised, acceptance criteria, dated test results, privacy/security notes, data flow, dependencies, support contact, approved price/fulfilment/refund/update terms, and QC/dispatch ID.
Do not issue “QC passed” or “secure” labels before the checks have run.

## Safe ethical-security testing
- [ ] Define written authorization, scope, test window, rate limits, data-handling rules and stop conditions before testing external systems.
- [ ] Test owned staging environments first; do not scan or exploit third-party systems without explicit permission.
- [ ] Prioritize dependency scanning, static analysis, secret scanning, accessibility, input-validation and configuration review.
- [ ] Record finding, severity, reproduction steps, remediation owner, fix commit and retest evidence.
- [ ] Never put exploit payloads, credentials, personal data or sensitive logs into public issues.

## Incident response
1. Triage and preserve minimal relevant evidence.
2. Revoke/rotate compromised credentials and disable affected integrations.
3. Identify impacted workflows, products, users and data.
4. Patch and retest in a controlled branch.
5. Notify affected parties when required by law or contract.
6. Document root cause, corrective action and a dated follow-up owner.

## Security status reporting
Report each control as PASS, FAIL, NOT CHECKED, or NOT APPLICABLE, with an evidence link and check date. A document or scheduled workflow alone is not proof that a control is enabled. Never claim the whole platform is fully secure; report tested scope and remaining risks.