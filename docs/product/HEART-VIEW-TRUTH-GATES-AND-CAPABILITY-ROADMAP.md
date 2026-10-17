# SHIRMANI Heart-View — Truth Gates & Product Capability Roadmap

**Status:** planning and acceptance specification, not a claim that all listed features exist or are production-ready.
**Repository context:** merged Heart-View preview commit `e18cb2570d7a007c0114e7d4f2a3cda08033cb96`; public preview source: `showroom/shirmani-supreme-heart-view-preview.html`.

## 1. Product promise

Build a Hindi-first, multilingual, evidence-led understanding and presentation workbench that helps people explain difficult subjects clearly, respectfully, and impartially. Its differentiator should be measurable: transparent sources, uncertainty labels, accessible explanations at multiple levels, user-controlled memory, repeatable tests, privacy protections, and a verifiable production status—not an unprovable claim that no one can copy it.

The Heart-View model is a product design philosophy. Personal ratios such as **99.9999% heart-view / 0.0001% mind-intellect view** may be represented as the user's proposed reflective parameter, but must not be described as scientifically measured human capacity, a validated psychological scale, or an established comparative fact about Gautama Buddha or other people without independent evidence and a valid measurement method. Do not rank or diagnose people from this ratio.

## 2. Required architecture layers

1. **Input & consent:** text, authorised uploads, and optional authorised voice input; clear purpose, retention, and consent.
2. **Understanding:** detect language, user intent, audience, requested depth, ambiguity, and safety needs. Ask a concise clarification when required.
3. **Impartiality & evidence:** separate sourced fact, interpretation, hypothesis, personal philosophy, and unknowns. Provide source links where available; never fabricate citations.
4. **Multi-compound views:** explain the same idea in plain language, story/example, structured reasoning, technical/scientific framing, and limitations. Label metaphor and speculation.
5. **Learning & feedback:** capture only user-approved corrections and preference updates; allow review, export, correction, and deletion through supported controls. Do not claim infinite memory.
6. **Response generation:** tailor tone and language without pretending to know a person's private inner state.
7. **Presentation:** text/script → authorised voice → rendered media → lip-sync/QC → optional live Q&A. Each connection is a separate integration gate.
8. **Product showroom:** demo, exact feature list, limitations, version, accessibility, price/terms, privacy, support, and feedback/upgrade path.
9. **Measurement:** versioned evaluation set, quality metrics, failures, regression checks, and release decision.

## 3. Capability states — never collapse them

Use these exact states in UI, product catalogue, and automation records:

- `IDEA`: proposal only.
- `PROTOTYPE`: local or mocked interaction; provider-backed capability not implied.
- `INTEGRATION_PENDING`: provider or service connection not yet verified.
- `TESTED`: a documented test passed in a specified environment and version.
- `PRODUCTION_VERIFIED`: end-to-end test passed against the released deployment with reproducible evidence.
- `BLOCKED`: prerequisite, permission, or evidence missing.
- `DEGRADED`: previously working feature has a current failure or material limitation.

A successful repository workflow does not automatically upgrade a feature's capability state.

## 4. Human-presentation chain and acceptance gates

| Gate | Required evidence | Fail-closed behaviour |
|---|---|---|
| Voice source | Provider/source, authorised asset or consent record, input hash where appropriate | Do not claim voice cloning or ownership verification |
| Voice generation | Request ID, output asset, duration, status, error handling | Mark pending/failed if no output artifact |
| Content/Q&A | Versioned Hindi/English test set, expected behaviour, recorded results | Do not claim live Q&A from a static script |
| Image/avatar | Approved source, rights/consent, original asset provenance | Do not substitute an unapproved face or image |
| Lip-sync | Actual rendered output and documented visual/audio QC | No PASS from a storyboard or API acceptance alone |
| Video render | Provider job status, downloadable output, checksum, playback check | Distinguish accepted request from completed render |
| Live presentation | Authenticated end-to-end session, latency/errors, Q&A transcript with privacy controls | Keep live capability NOT VERIFIED until exercised |
| Release | All required gates passed, reviewer and build/version recorded | Block production readiness claim when any mandatory gate is missing |

The previously supplied HeyGen URL and avatar identifiers are references supplied by the owner, not proof that the linked assets are accessible, authorised, rendered, or integrated. Do not repeatedly ask the owner to resend the same link. Use the existing reference and report any connector/access limitation precisely.

## 5. Quality evaluation for the understanding engine

Maintain a versioned test set covering:
- Hindi, English, and mixed-language input;
- simple and advanced explanations of the same subject;
- source-backed factual questions and source gaps;
- ambiguity, contradictory evidence, and uncertainty;
- neutral treatment of religious, philosophical, scientific, and political viewpoints;
- respectful handling of strongly held personal beliefs without affirming unverifiable claims as established facts;
- consent, privacy, memory correction, and opt-out;
- harmful or physically dangerous experimental instructions;
- accessibility and mobile presentation.

Measure:
- source correctness and citation validity;
- unsupported-claim rate;
- uncertainty calibration;
- comprehension across beginner and expert test readers;
- translation consistency;
- user correction rate;
- response latency and error rate;
- privacy/safety regression count.

Set baseline measurements before claiming improvement. A target is not a measured result.

## 6. Phased delivery

### Phase 0 — protect the working system
- Inventory existing assets and workflow responsibilities.
- Apply the non-destructive work-relevance filter.
- Keep security, backup, deployment, integrity, and revenue gates unless a replacement is proven.
- Resolve the cause of cancelled or queued runs before rerunning or disabling them.

### Phase 1 — deliver a truthful demo
- Test the deployed Heart-View page on mobile and desktop.
- Run the browser interaction checklist and keyboard/accessibility checks.
- Add examples for plain, story-based, evidence-based, and technical explanations.
- Ensure all simulated functions are labelled as simulations.

### Phase 2 — prove one commercial service
- Reuse the existing Hindi/English writing and research enquiry assets.
- Reconcile conflicting public price menus before publishing binding prices.
- Qualify leads using verified official public contact routes; human approval before any outreach.
- Track replies, quotes, orders, cleared payments, accepted delivery, and refunds as separate events.

### Phase 3 — prove one provider integration
- Select one bounded feature (voice OR video render OR live Q&A) and one authorised provider.
- Document credential handling, consent, cost limits, timeout/retry behaviour, privacy, and rollback.
- Test the full path in a non-production environment; record evidence before release.

### Phase 4 — productise reusable tools
- For each tool, publish a versioned capability contract, demo, limits, tests, support path, upgrade policy, and commercial terms.
- Build only after a real user need and acceptance test are identified.
- Use original research, code, documentation, provenance, access controls, trademarks where appropriate, and iteration to build defensible differentiation. Do not promise perfect or impossible-to-copy protection.

### Phase 5 — scale responsibly
- Load-test before making capacity claims.
- Add localisation, accessibility, privacy review, abuse prevention, reliability objectives, support operations, and cost accounting.
- Do not claim support for 195 countries, 8.5 billion users, every social network, or enterprise/government procurement until each relevant capability, legal requirement, service level, and capacity is verified.

## 7. Definition of done for every feature

A feature is done only when it has:
- an owner and named user problem;
- a working implementation in the stated environment;
- acceptance tests with recorded results;
- security/privacy and accessibility review appropriate to its risk;
- known limitations and failure states;
- versioned documentation and rollback path;
- a demo that matches the actual capability;
- a price/terms and support route if offered commercially;
- a feedback loop that does not silently collect more data than necessary.

**Truth rule:** distinguish proposed, built, tested, deployed, used by a customer, accepted, and paid. Never infer one state from another.
