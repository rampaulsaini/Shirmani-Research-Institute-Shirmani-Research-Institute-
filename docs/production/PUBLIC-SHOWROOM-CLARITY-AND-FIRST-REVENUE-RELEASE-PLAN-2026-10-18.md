# Public Showroom Clarity & First-Revenue Release Plan

Status: implementation plan committed on a feature branch; not a claim that the live site or external services have changed.
Owner: Shirmani Research Institute
Principles: preserve existing work; do not delete source material to make the interface look simpler; separate verified behavior from plans; do not claim sales, security, AI, voice, or video success without evidence.

## 1. Public-facing information architecture

The public entry page should answer, in this order:

1. **What is Shirmani Research Institute?** A research, writing and digital-product workshop.
2. **What can a visitor do now?** Browse working browser-local demos, request Hindi/English writing or research, and inspect product limitations.
3. **How do I start?** One prominent “Request a quote” route, plus “Explore products” and “Try a demo”.
4. **What is ready?** Each card carries one of: Working demo, Enquiry available, Integration pending, or Verified release. Avoid ambiguous “live” claims.
5. **How is trust established?** Show scope, version, evidence, limitations, privacy notes, price/quote status, support route and last-checked date.

### Recommended top-to-bottom page order

- **Hero:** one plain-language promise, two primary actions (Explore products / Request writing & research).
- **Three current services:** Hindi/English writing; research summary with sources; website/blog content. Make clear that scope, price, delivery date and payment terms are agreed before work starts.
- **Try before buying:** searchable catalogue with filters for Writing & Research, Learning, Presentation, Product Media, Production & Security.
- **Featured demos:** show a small curated set first; link to the complete catalogue rather than dumping every tool into the landing page.
- **How it works:** Browse → Try demo → Confirm scope/quote → Pay under agreed terms → Receive deliverable → Feedback/revision.
- **Proof and limitations:** real screenshots/files/test records only; no invented testimonials, sales, security certification or external integration status.
- **Heart-View Preview:** explain the communication design and evidence rules; link to the separate voice/video verification ledger.
- **Research archive and library:** categories, search, provenance/source notes, date and rights/licensing metadata. Do not imply all world books or copyrighted works are available.
- **For institutions:** separate future-facing institutional offerings from currently orderable services.
- **Footer:** contact/enquiry, privacy, terms, accessibility, product support and feedback.

## 2. Product catalogue rules

Every product card should contain: name, user problem, what it actually does today, 3-step demo, sample output, intended user, language, requirements, limitations, price or “quote required”, version, support/feedback link, and readiness label.

Do not put every internal tracker, research note, unfinished idea, and public product on the same visual level. Keep all material, but route it into clearly named sections: Public Products, Try-it Demos, Research & Archive, In Development, Internal Operations. “Filter” means navigation and status-based visibility, not deletion. Archive duplicates only after reference checking, with a recoverable record.

## 3. First measurable revenue path

Start with the service already described in the repository: Hindi/English writing, research summaries, and website/blog content. Avoid waiting for the full global platform to be complete.

### Quote workflow

1. Capture customer goal, topic, language, word/page range, intended audience, sources/links, deadline and budget.
2. Review feasibility and source quality.
3. Send a human-reviewed written quote stating deliverables, exclusions, price, timeline, revision count, payment terms and cancellation/refund terms.
4. Start only after written acceptance and agreed payment milestone.
5. Deliver the file/link; record acceptance and requested revisions.
6. Record actual revenue only from payment evidence, and actual delivery only from a sent deliverable/acceptance record.

### Seven-day operating targets (targets, not results)

- Day 1: verify enquiry path and publish 2–3 clearly labelled sample deliverables.
- Days 2–3: identify 20 relevant organisations/prospects from official public sources; record source URL and why the offer fits.
- Days 3–5: prepare and human-review 10 tailored messages; send only through authorised channels, respecting privacy and anti-spam rules.
- Days 5–7: follow up once where appropriate; log replies, qualified leads, quotes, accepted scopes, payments and deliveries.

Measure: prospects researched, messages reviewed, messages actually sent, replies, qualified enquiries, quotes sent, quotes accepted, payments received, deliverables sent, acceptance, revision rate and time spent. Initial values are zero/unknown until evidenced; never backfill invented activity.

## 4. Voice, avatar, video and live Q&A evidence chain

Track each stage independently:
- Source voice/photo: provenance, permission and approved asset identifier.
- Voice generation: provider, job ID, settings, output audio and listener review.
- Script/content: exact version, language and source/evidence ledger.
- Avatar/video: provider job/result ID, actual rendered file and playback result.
- Lip-sync: sampled frame/time checks plus audio alignment review.
- Live Q&A: dated test prompts, actual responses, latency, failures and repeat test.
- External service: provider-side result and reproducible request/response evidence.
- Release: human approval, privacy review, rollback route and version.

A saved URL, prompt, plan or setup page is not proof of a successful test. Until artifacts exist, label the stage “Pending evidence”. Keep the previously supplied HeyGen URL as a reference; do not ask the owner to re-upload material already supplied.

## 5. Multi-layer safety and continuity

- **Layer 1 — source preservation:** branch/PR workflow; no bulk deletions; protect main.
- **Layer 2 — dependency and secrets hygiene:** least privilege, secret scanning, pinned/reviewed actions where feasible, no secrets in browser code.
- **Layer 3 — build and tests:** run existing checks; record failed jobs and actionable errors.
- **Layer 4 — public interface QA:** desktop/mobile, keyboard navigation, clear labels, broken-link scan, enquiry path test.
- **Layer 5 — backup/rollback:** retain prior published version and a clear revert path.
- **Layer 6 — claim/evidence gate:** no “verified”, “secure”, “live”, “AI-powered”, “lip-sync passed”, “sale” or “income” claim without matching evidence.

Do not call a checklist a security scan or security certification. Never expose API keys, credentials, private customer details or unapproved voice/image assets.

## 6. Acceptance checklist for this plan

- [ ] Public home has one clear primary action and a simple top-to-bottom journey.
- [ ] Catalogue filters separate customer-facing products from internal operations.
- [ ] Each card shows what works now and what remains pending.
- [ ] Writing/research enquiry can be drafted without implying automatic sending or payment.
- [ ] Quote acceptance and payment evidence are distinct from delivery evidence.
- [ ] Voice, audio, script, avatar/video, lip-sync, Q&A and provider status have separate evidence fields.
- [ ] All changes preserve existing content and provide a rollback path.
- [ ] Mobile and accessibility checks are recorded before release.

## 7. Implementation boundary

This document is a concrete repository artifact and prioritisation contract. It does not itself redesign the deployed pages, send outreach, integrate a payment processor, contact institutions, verify HeyGen, prove live Q&A, or produce income. Those outcomes require code changes, authorised external actions and recorded tests.
