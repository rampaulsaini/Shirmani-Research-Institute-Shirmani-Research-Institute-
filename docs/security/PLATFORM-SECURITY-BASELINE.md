# Platform Security Baseline — Production Work Plan

**Status:** implementation checklist / baseline specification; not a claim that every control is already enabled or independently audited.  
**Scope:** GitHub repository, GitHub Actions, static public showroom, browser-local tools, future AI/voice integrations and customer operations.

## Immediate release blockers

- [ ] Never commit API keys, tokens, passwords, customer private data, or provider credentials. Use GitHub Actions secrets for CI and a proper secret manager for production services.
- [ ] Treat all public form input, imported JSON/CSV, URLs, QR destinations, user reviews and generated AI text as untrusted.
- [ ] Do not render user-supplied strings with `innerHTML`; use `textContent` or DOM APIs. If rich text is required, use a maintained allow-list sanitizer.
- [ ] Validate imported data shape, size, allowed fields and URL schemes. Accept only `https:` (and `http:` only when explicitly needed); reject `javascript:`, `data:` and unknown schemes for links.
- [ ] External links opened in new tabs must use `rel="noopener noreferrer"`.
- [ ] Do not put confidential customer information in browser localStorage. Explain that local records are device/browser-specific and can be lost or read by other users of that browser profile.
- [ ] Do not activate payment, email, WhatsApp, voice cloning, lip-sync or live broadcasting integrations without explicit authorisation, consent, provider credentials, abuse controls and end-to-end tests.

## GitHub repository and automation controls

- [ ] Use pull requests for production changes; require review and successful checks before merge where repository settings allow.
- [ ] Give Actions the minimum permissions required. Set workflow-level `permissions:` explicitly; default to read-only and elevate only for the individual job that needs it.
- [ ] Pin third-party Actions to reviewed full commit SHAs; update pins through a reviewed dependency-update process.
- [ ] Avoid executing untrusted pull-request code with privileged secrets or write tokens. Review `pull_request_target`, artifact handling and checkout/ref usage carefully.
- [ ] Enable secret scanning, push protection, Dependabot alerts/security updates and dependency review where available in repository settings.
- [ ] Add automated checks for HTML/JS syntax, broken internal links, accidental secrets, unsafe DOM sinks, dependency vulnerabilities and product manifest consistency.
- [ ] Keep workflow artifacts free of credentials and private customer data; apply retention limits.
- [ ] Protect the default branch, review deployment permissions and document rollback steps.

## Public showroom and product release gates

Every product must move through the four operational stages:

1. **Institute:** product purpose, intended users, limitations, source/research notes and risk assessment.
2. **Factory:** working implementation, setup/use guide, demo script and test data.
3. **QC / release gate:** functional tests, security review, privacy review, accessibility/mobile check and known-limitations record. A passing workflow alone is not a security certification.
4. **Showroom:** publish only the actual build, clear price/scope, demo or screenshot, usage guide, support/upgrade policy and QR pointing to a controlled HTTPS page. Never invent reviews, warranties, sales, certifications or performance claims.

For customer-submitted ratings/reviews: validate and moderate submissions, prevent script injection, minimise personal data, provide a removal/contact route, and never present unverified testimonials as verified.

## AI / voice / face / live presentation controls

- Require explicit permission for any personal voice or likeness. Store consent scope, allowed uses, expiry/revocation and provenance.
- Label synthetic media where a reasonable audience could mistake it for a real recording. Do not impersonate third parties or bypass a provider's consent checks.
- Separate philosophical/identity statements from source-based and independently verified factual claims.
- Record source links, model/provider version, timestamp and evidence state when appropriate; do not log raw sensitive audio or private conversations by default.
- Add prompt-injection defenses for retrieved content, output validation, rate limits, abuse reporting, human approval for high-impact actions and emergency disable switches.
- Keep production credentials server-side; never expose provider secrets in public HTML/JavaScript.

## Measurable security dashboard

Report actual counts from scans and checks—not invented percentages:

- Critical/high dependency alerts open
- Confirmed secrets in tracked history
- Workflows using explicit least-privilege permissions
- Third-party Actions pinned to full SHAs
- Public pages passing link and script checks
- Products with complete demo, usage guide, privacy notes and release checklist
- Open security issues by severity and age
- Latest successful release-gate run and its commit SHA

## First implementation sequence

1. Review workflows and repository settings; capture the baseline.
2. Scan tracked files and history for exposed secrets; rotate any exposed credential before removing it from code/history.
3. Add lightweight automated static checks and safe-link/input checks to pull requests.
4. Review public tools for unsafe `innerHTML`, URL validation and data-import boundaries.
5. Add a product manifest and release gate to the showroom pipeline.
6. Re-run checks, resolve findings, and publish the exact commit/test evidence.

**Current limitation:** this document defines the control plan. It does not itself enable GitHub settings, run a complete penetration test, prove absence of vulnerabilities, or certify the platform as secure.
