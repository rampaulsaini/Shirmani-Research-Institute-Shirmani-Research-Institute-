# SHIRMANI Platform — Heart-View, Public Interface and Verified Delivery Control

**Document type:** additive execution contract  
**Status:** plan and acceptance criteria; not proof of deployed functionality  
**Safety rule:** preserve existing user material. Do not bulk-delete or overwrite assets as “noise” without a reviewed dependency/usage report and recoverable change.

## 1. The single public journey

The public homepage should answer, in this order:

1. **What is Shirmani Research Institute?** A concise, plain-language introduction in Hindi and English.
2. **What can I use today?** Clearly labelled working demos and the currently offered Hindi/English writing and research service.
3. **Explore the showroom.** Searchable categories with product status visible: Available service, Working demo, Prototype, Planned, or Retired.
4. **Try before buying.** Each item links to its own demo, guide, product passport, price/quote terms and evidence status. A concept image is never represented as a real screenshot.
5. **Start an enquiry.** Collect only the information needed to scope the work; explain that a generated brief is not a submitted order.
6. **Create account / sign in.** Show these controls only when a real, secure authentication backend is configured and tested. Never imply a static HTML form creates an account.
7. **Trust and support.** Privacy, accessibility, limitations, contact route, revision/return terms where applicable, and a clear issue-reporting path.

Use a progressive layout: one clear hero, primary actions, service/product categories, featured working demos, the process, trust/evidence, then footer. Avoid placing every project idea on the homepage. Preserve all ideas and unfinished work in a structured roadmap/catalogue reachable from the public navigation.

## 2. Content organization without loss

Use categories rather than deleting items to make the page simpler:

- Writing, research and bilingual content
- AI / ML / NLP tools
- Heart-View / impartial-understanding learning tools
- Avatar, voice, lip-sync and presentation
- Creator studio, video and media
- Education, library and research labs
- Nature, environment and public-interest work
- Commerce, institutional tools and services
- Social/community platform
- Platform infrastructure, security and operations

Every entry must have a stable ID, title, short plain-language description, category, status, canonical path, owner/maintainer if known, last checked date, evidence links, dependencies, and next action. Keep a “planned / not yet built” section so ideas remain visible without being confused with deliverables.

**Removal gate:** before removing any item, record its path/ID, reason, inbound links/dependencies, test evidence, reviewer decision and rollback path. Prefer archive/deprecation and redirects over deletion. Never remove user material just because it is not currently visible on the homepage.

## 3. Heart-View explanation contract

The Heart-View concept should be presented as the Institute's philosophical and educational framework, with the author's wording preserved where appropriate. Explain it at three levels:

- **Simple:** short everyday wording, a relatable example, and a story if useful.
- **Reasoned:** definitions, assumptions, practical implications, counterexamples and limits.
- **Research:** a stated question, method, evidence, source list, results, uncertainty and limitations.

The requested 99.9999% / 0.0001% values are user-defined philosophical parameters unless a reproducible measurement method and validated data are supplied. Do not present them as measured scientific facts, IQ scores, or an established measurement of Mahatma Buddha or other people. If a claim cannot be established from evidence, label it “philosophical/identity statement” or “insufficient evidence”; do not invent quantum equations or statistics to make it appear proven.

## 4. Human-presentation end-to-end evidence chain

Track each stage separately; a passing stage does not imply the next one passed.

| Stage | Minimum evidence | Release condition |
|---|---|---|
| Original photo | Exact source asset reference; identity-preserving crop/resize check | Source verified; no substitute face presented as original |
| Authorized voice | Source audio reference and authorization record | Correct voice asset is actually available and configured |
| Speech / dialogue | Test prompts, expected intent, transcripts and source checks | Correct meaning; unsupported claims flagged |
| Voice output | Actual output recording, intelligibility check and timing | Output is playable and correctly attributed |
| Avatar / lip-sync | Recorded test clip; timestamped visual review of speech alignment | Critical alignment defects absent |
| Live Q&A | Actual external-service session evidence, prompt/response log and failure case | Q&A works with honest fallback on failure |
| End-to-end | Run ID, date, environment, versions, latency, errors and evidence links | All critical gates pass on the same release candidate |
| Privacy/security | Permission review, retention rules, access control and consent | No unresolved critical privacy/security issue |

The supplied HeyGen video URL is a reference asset only. It does not by itself prove live Q&A, authorized voice integration, exact lip-sync quality, or a working end-to-end connection. Never ask the user to re-upload the same reference already supplied; first inspect the repository and configured integration, and record any genuinely missing asset or permission precisely.

## 5. Layered release and continuity checks

Run small, targeted checks in the affected area before broad workflows. Each check records PASS, FAIL, BLOCKED, or NOT RUN; never turn “not run” into “pass”.

1. **Repository integrity:** working tree/change summary, broken links, duplicate canonical paths, missing assets, accidental deletions.
2. **Build/runtime:** syntax, imports, package setup, static-page load, console/network errors where test tooling exists.
3. **Public interface:** mobile and desktop layout, navigation, search/filter, keyboard access, Hindi/English readability.
4. **Product passport:** stable ID, status, version, real demo/guide links, truthful price and availability.
5. **Media:** original asset provenance, actual screenshot/video playback, QR destination resolves to the matching passport.
6. **Security/privacy:** least privilege, secrets not committed, input validation, no unnecessary customer data, external calls disclosed.
7. **Commerce:** enquiry capture, scope approval, quote, payment evidence, delivery and feedback are separate states.
8. **Automation:** inspect failed job logs first; rerun only relevant jobs after fixing a diagnosed cause. Do not repeatedly rerun successful work without a new reason.
9. **Release:** publish only after critical gates pass; provide a concise changelog and rollback path.

A green workflow badge is evidence only for the checks that workflow actually ran. It does not prove global quality, customer demand, external-provider operation, or income.

## 6. First income lane — keep it real and small

The first offer remains limited to services already stated as available:

- Hindi/English source-based research summary
- Hindi/English website/blog content
- Writing, editing and proofreading with agreed scope

Use the existing enquiry and client-pipeline tools before creating another generic sales page. The repository's indicative pilot prices are proposals, not guaranteed market rates or binding quotes. Confirm the exact scope, sources, word limit, deliverables, revisions, deadline, price, tax if applicable, and payment terms in writing before work starts.

### Seven-day operating scoreboard

Record dated evidence for each metric; begin at zero unless a real record exists.

| Metric | Target | Evidence |
|---|---:|---|
| Enquiry page check | 1 mobile + 1 desktop | Dated test checklist |
| Portfolio samples | 2 source-labelled samples | Files, citations and QC checklist |
| Qualified prospects | 20 researched prospects | Official URL, fit reason and public contact source |
| Personalised outreach | Up to 5/day only after an authorized channel is ready | Actual sent-message record |
| Replies / quotes / accepted orders | Count actual events only | Message thread / written acceptance |
| Payments | Count only funds received | Payment receipt/reference, kept private |
| Delivery quality | 100% of accepted pilot jobs on agreed deadline | Agreed scope and delivery timestamp |

A prospect list is not outreach. A drafted message is not sent. A quote is not an order. An invoice is not payment. Do not claim revenue before payment evidence exists.

## 7. Public interface and account creation

A public HTML page may present links and client briefs, but secure accounts require a real authentication service, server-side session handling, password reset, abuse protection, privacy notice, and security testing. Until that exists, label login/sign-up as planned or link to a verified existing provider; do not collect passwords in a static page.

Likewise, global scale (including 8.5 billion users), 24/7 broadcasting, all-social-network aggregation, automatic email outreach, payment processing and a worldwide studio are long-term goals—not present capabilities without tested infrastructure, permissions, operating budget, and capacity evidence.

## 8. Release record template

For every run, record:

- Run ID / date / branch / commit:
- Scope tested:
- Environment and versions:
- Checks: PASS / FAIL / BLOCKED / NOT RUN:
- Evidence links:
- Defects and severity:
- Owner and next action:
- Rollback or recovery:
- Release decision and reviewer:

## 9. Immediate execution order

1. Inventory the current homepage, showroom, service enquiry, pipeline, and human-presentation spec before editing.
2. Fix navigation and category hierarchy without deleting underlying material.
3. Verify the existing writing/research enquiry path and two sample deliverables.
4. Create a dated, evidence-based test record for the actual photo → authorized voice → dialogue → lip-sync → live Q&A chain.
5. Repair only diagnosed blockers; open small reviewable PRs with focused changes.
6. Publish status honestly and maintain one visible “Next verified action” list.
