# SHIRMANI SUPREME — Implementation Gate Tracker

**Updated:** 2026-10-13  
**Purpose:** Convert the approved character brief into verifiable implementation work. This tracker records requirements, not completed integrations.

## Current verified repository fact
- The approved character brief exists at `docs/production/SHIRMANI-SUPREME-FINAL-CHARACTER-BRIEF-2026-10-12.md` on the implementation branch.
- This file alone does not prove original photo/audio assets are available, nor that voice, lip-sync, live presentation, product demos, QR scans, sales, or outreach are operational.

## Gate 0 — Asset provenance
- [ ] Locate the exact owner-authorised original portrait in an approved repository/workspace.
- [ ] Record its path/reference, provenance, authorisation and checksum where practical.
- [ ] Confirm only proportional resize/display scaling/framing; no face edits or generated replacement.
- [ ] Locate the owner-authorised original voice recording.
- [ ] Record its path/reference, provenance, authorisation and permitted-use scope.
- [ ] If either asset is missing, mark it `PHOTO ASSET REQUIRED` or `VOICE ASSET REQUIRED`; do not substitute generated media.

## Gate 1 — Plain-language and evidence tests
- [ ] Prepare a versioned test set covering simple questions, ambiguous requests, specialist questions, corrections and sensitive disagreements.
- [ ] Verify the four evidence states: `INDEPENDENTLY VERIFIED`, `SOURCE-BASED`, `PHILOSOPHICAL / PERSONAL PERSPECTIVE`, `INSUFFICIENT EVIDENCE`.
- [ ] Verify unsupported prompts return exactly: `अभी पर्याप्त प्रमाण उपलब्ध नहीं है।`
- [ ] Record test inputs, expected behaviour, actual output, pass/fail, date and reviewer.
- [ ] Test comprehension with five readers; record results without coaching. Target: at least four accurately paraphrase the core message.

## Gate 2 — Voice and presentation
- [ ] Confirm provider, credentials, authorisation and consent before enabling voice services.
- [ ] Test speech recognition and context-aware Q&A.
- [ ] Test authorised voice output end-to-end and preserve the resulting artefact reference.
- [ ] Test original-photo/avatar fidelity, facial timing and lip-sync against recorded speech.
- [ ] Test live streaming and MP4 export separately.
- [ ] Record latency, failure cases, limitations, test date and artefact links.
- [ ] Keep every untested capability `NOT VERIFIED`; block production claims after any critical failure.

## Gate 3 — Per-product showroom package
For every product/version, require:
- [ ] Unique product ID, name and version.
- [ ] Dedicated product passport page and unique QR destination.
- [ ] Mobile QR scan test with recorded result.
- [ ] Short product-specific description on the cover.
- [ ] Original authorised portrait/logo only if the asset has passed Gate 0.
- [ ] English identity line in a legible footer/responsive layout.
- [ ] Actual VIP screenshot, or label `ILLUSTRATIVE MOCK-UP`.
- [ ] Actual recorded demo video, or label `STORYBOARD — NOT RECORDED`.
- [ ] Usage guide, supported uses, limitations, QC state and version history.
- [ ] Product-specific review and quality-improvement loop.

## Gate 4 — Outreach and income integrity
- [ ] List only real services currently deliverable: Hindi/English writing, research summaries and website/blog content.
- [ ] Confirm scope, deliverables, price, deadline and payment terms in writing before work starts.
- [ ] Use verified official contact details and authorised sending channels.
- [ ] Log each outbound message only after the channel confirms it was sent.
- [ ] Report enquiries, replies, paid orders and revenue only from actual records; never infer sales from page views or workflow runs.

## Release decision
A gate passes only when its evidence links and dated pass/fail record are present. Workflow success, a green badge, a mock-up, a specification or a planned integration is not proof that the underlying capability works.
