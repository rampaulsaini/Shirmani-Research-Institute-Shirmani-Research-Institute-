# SHIRMANI SUPREME — Character & Product Presentation Specification

Status: **Approved design specification; implementation and production tests remain pending.**

## 1. Character description

**Shirmani Supreme is a calm, warm, clear, respectful, evidence-aware presentation character.** It communicates in simple, natural language, adapts to the audience and situation, and explains difficult ideas with everyday examples before adding technical detail. It treats people equally and does not demean any person, community, religion, organisation, profession, or level of education.

It distinguishes:
- **Verified:** supported by adequate independent evidence or a reproducible test.
- **Source-based:** attributed to an identified source, but not independently verified by this system.
- **Personal philosophy / identity:** a viewpoint or self-description, not automatically a scientific finding.
- **Insufficient evidence:** clearly says, “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” / “There is not enough evidence available yet.”

It does not invent credentials, scientific proof, customer reviews, sales, outreach, live activity, or completed tests. It can explain the founder's stated philosophy respectfully while separating it from independently established facts.

## 2. Founder photo and voice

- Use the founder-provided original photo **unchanged**; only proportional resizing/cropping needed for layout is permitted. Do not generate a replacement face, beautify, recolour, or alter identity-defining features.
- Use only audio supplied by the founder or an explicitly authorised voice integration. Do not claim a voice integration is active until an end-to-end test succeeds.
- Keep original source assets and record filenames, provenance, permitted use, and version. Do not embed or redistribute private assets without the owner's approval.
- If the original photo/audio is not available in the repository or current working context, mark it **MISSING — REQUEST ORIGINAL**; never substitute a generated lookalike or guessed file.

## 3. Product showroom card requirements

Every product gets a distinct identity and product-specific card:
1. Product name and stable product ID.
2. Founder photo as a small logo/portrait, preserving the original image.
3. Short, readable on-image description.
4. Product-specific QR code linking to its own long description, usage guide, version, and demo page.
5. Real demo video or clearly labelled **Demo pending** placeholder.
6. Product screenshot or clearly labelled **Preview pending** placeholder.
7. Version, status, known limitations, accessibility text, and last verified date.
8. Customer feedback and quality-improvement log only when real feedback exists.

Do not reuse one QR code across products. QR destinations must be tested and must not point to unpublished or unrelated pages. Use responsive scaling without distorting the photo or product artwork.

## 4. Demo and evidence states

Use these explicit states in catalogue data and public UI: draft, asset_pending, demo_pending, ready_for_review, tested, verified, published, needs_fix.

A workflow run alone does not establish that a product works. **tested** requires a recorded test result; **verified** requires defined acceptance criteria and evidence. Never display verified merely because a file, workflow, or page exists.

## 5. Voice-to-live presentation chain

Voice input → authorised speech recognition → context and intent → source/evidence gate → answer → authorised voice output → original photo/avatar presentation → lip-sync → timing/quality checks → audit record.

Before production activation, test Hindi/English comprehension, expected answers and evidence labels, insufficient-evidence handling, voice authorisation and consent, photo fidelity, lip-sync and timing, accessibility, latency, respectful-language regression, failure logging, and text fallback.

Until a real provider is configured and tests pass, mark voice generation, lip-sync, and live presentation **NOT INTEGRATED / NOT VERIFIED**.

## 6. Product quality loop

Authentic customer review (with consent) → triage → reproducible bug report → prioritisation → fix → regression test → release notes → updated product passport and demo. Do not fabricate ratings, reviews, QR scan counts, customers, revenue, or quality percentages.

## 7. Security and privacy

- Never commit API keys, passwords, voice-provider secrets, customer personal data, or private source audio.
- Use least-privilege tokens and documented secret storage.
- Require human approval before sending external sales messages, publishing sensitive media, or spending money.
- Distinguish outreach states: drafted, approved, sent, reply_received. Only provider-confirmed events may be marked sent/replied.
- Respect provider terms, anti-spam rules, consent, and applicable privacy law.

## 8. Release checklist

- [ ] Original founder photo received and provenance recorded.
- [ ] Authorised voice asset/provider configured.
- [ ] Product-specific QR destination resolves correctly.
- [ ] Short description readable at mobile size.
- [ ] Product screenshot exists or is labelled pending.
- [ ] Demo video plays or is labelled pending.
- [ ] Usage guide and version passport are available.
- [ ] Automated checks pass and manual acceptance test is recorded.
- [ ] Public status matches evidence.
- [ ] No secrets or unauthorised personal data are exposed.

## 9. Measurable first release

Start with one real product/service, not a claim of 5,000 finished products. Publish one truthful catalogue entry for **Hindi/English Writing & Research** with an enquiry form, scope confirmation, written deliverables, deadline, and payment terms. Add its own QR, screenshot, and demo only when those assets exist and have been tested. Track enquiries, qualified leads, quotes sent, paid orders, delivery time, revisions, and customer feedback from actual records.

**Status:** specification written; photo/audio assets, QR routing, demo media, integrations, and production tests are not certified by this document alone.
