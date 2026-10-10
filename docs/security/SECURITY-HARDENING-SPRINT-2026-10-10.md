# Shirmani Research Institute — Security Hardening Sprint
**Date:** 2026-10-10  
**Status:** Implementation plan committed for review; this is not a claim that the platform is already secure.

## Priority order

1. **Account:** enable/passkey or 2FA, review active sessions and authorized OAuth/GitHub Apps, remove unknown access, and keep recovery codes offline.
2. **Repository:** use least-privilege workflow permissions; require review for production changes where practical; review branch protections, deploy keys and collaborators.
3. **Automation:** never place API keys, passwords, mail credentials, payment secrets, voice-provider keys or personal data in source, logs, artifacts, issues or public Pages. Use GitHub Actions secrets/environments only for workflows that need them. Never print secrets.
4. **Showroom:** treat static-page forms as browser-local unless a real backend is configured; never imply a message was sent or payment completed without provider confirmation.
5. **Production chain:** Institute research → Factory build → QC/evidence gate → Showroom release. Keep drafts, QC-passed products, independently verified claims and paid orders as separate states.
6. **Customer trust:** collect only necessary information, obtain permission before email/WhatsApp outreach, respect opt-outs and rate limits, and do not scrape private contact details or mass-spam institutions.

## Release gate

- [ ] Unique product ID, version, purpose, owner, supported/unsupported uses and known limitations.
- [ ] Page accurately labels prototype vs. live integration.
- [ ] Demo video or reproducible walkthrough exists; otherwise label “demo pending.”
- [ ] Current screenshot matches the actual product.
- [ ] Usage guide and support/contact route are published.
- [ ] Price, offer expiry, refund/support terms and licence are clear; no fabricated guarantees.
- [ ] QR resolves to canonical public page and contains no secrets or personal data.
- [ ] QC results and dispatch decision are recorded; failed critical gates block release.
- [ ] Reviews are consented and converted into traceable improvement tasks.
- [ ] No credentials, private keys, tokens, customer data or internal logs are exposed.
- [ ] Accessibility, mobile layout, broken links and keyboard operation are checked.
- [ ] Sales copy distinguishes demonstrated features from planned features.

## Four-layer operating model

| Layer | Required output | Promotion rule |
|---|---|---|
| Institute / Research | source-linked brief, hypothesis, scope and limitations | Research is not automatically a product |
| Factory | runnable artifact, version, README and demo plan | Empty directories and names are not products |
| QC / Gate | test record, risk notes, QR target and gate ID | Failed or missing critical tests block dispatch |
| Showroom / Sale | real screenshot, demo, usage guide, clear price and terms | Listing is not proof of a sale or revenue |

## Metrics to publish each run

- Workflows checked / total workflows
- Workflows with explicit least-privilege permissions
- Secret-scanning alerts open / resolved (from GitHub's actual security view)
- Dependency/code-scanning alerts open / resolved (when enabled)
- Product pages checked / total product pages
- Broken demo/QR links
- Products blocked by release gates
- Confirmed paid orders (payment-provider records only)

Do not substitute workflow-run counts for security posture, product completion or independent verification.

## Next 48-hour queue

1. Review Actions permissions and each workflow's declared permissions.
2. Enable GitHub secret scanning / push protection and code scanning if available for this repository and plan.
3. Review third-party Actions and pin them to full commit SHAs after checking upstream releases.
4. Run a secret-history scan and rotate any credential that may have been committed; deleting it from the latest file is insufficient.
5. Check Pages deployment permissions; only intended branches/workflows should publish.
6. Finish one income product (Hindi/English writing and research), a public listing and a sample deliverable; then send individually reviewed, relevant proposals with permission-aware outreach.
7. Publish evidence-backed progress and record blockers explicitly.

## Limits

This is a hardening plan, not a penetration-test report, certification, live infrastructure scan, legal opinion, or proof that alerts are resolved. Static GitHub Pages cannot safely keep private credentials or reliably process payments alone. Real email, WhatsApp, voice, avatar/lip-sync, live streaming and payment integrations require authorized provider accounts, backend services, consent and end-to-end tests.
