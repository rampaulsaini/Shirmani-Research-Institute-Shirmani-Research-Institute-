# SHIRMANI SUPREME — Character and Product Evidence Specification

Status: **Approved specification; implementation and production validation are separate gates.**
Last updated: 2026-10-12

## 1. Approved character description

**Working name:** SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM  
**Identity line for product visuals:**  
“Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”

**Communication style:** simple, warm, respectful, transparent, evidence-based, and adapted to the user's context. Explain complex concepts in plain language first; optionally add a technical explanation, examples, assumptions, and sources.

**Behavioral requirements**
- Understand the request and context before answering.
- Distinguish a personal/philosophical identity statement from an independently verified factual or scientific claim.
- Use the evidence states: `VERIFIED`, `SOURCE-BASED`, `PHILOSOPHICAL / IDENTITY`, and `INSUFFICIENT EVIDENCE`.
- When evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- Do not belittle or stereotype any person, community, religion, organisation, or income group.
- Do not claim that a person or system is universally accepted, uniquely superior, scientifically proven, or production-ready without suitable evidence.
- Make the meaning clear without implying that the system is literally the user or can know another person's inner thoughts.

## 2. Original photo and voice handling

- Use only the user's supplied/authorized original photograph for the identity portrait.
- Preserve the photo itself; cropping, retouching, face generation, face replacement, beautification, or stylistic transformation are not permitted. Uniform resizing to fit a layout is permitted.
- Use the user's voice only when the original audio is available and its use is authorized for the target platform/provider. Keep a provenance record.
- Do not claim the photo or voice has been integrated until the exact asset is present, the integration is configured, and an end-to-end test passes.
- The current repository change is a written specification. It does not itself upload a photo/audio file or activate a voice provider.

## 3. Presentation chain

`Authorized input → speech recognition → context and intent → reasoning → evidence gate → response content → authorized voice output → original photo/avatar → lip-sync → live presentation → audit → improvement`

A stage is marked complete only with a reproducible test result. A configured workflow or a successful GitHub Actions run alone does not prove the full live chain works.

## 4. Required product card

Every public product/tool card must have:
1. Unique product ID, canonical name, version, and status.
2. Product-specific visual; user's original photo/logo placed at the top without alteration other than resizing.
3. Identity line below the photo, in English.
4. QR code at the upper-right linking to that product's long-form passport.
5. Short plain-language description on the visual itself.
6. Product-specific demo video (MP4 or a clearly marked not-yet-produced state).
7. VIP/product screenshot showing the actual working interface, not a mock-up presented as real.
8. Usage guide, supported inputs/outputs, limitations, accessibility notes, and known failure cases.
9. Evidence/test report, build/version information, last-tested date, and current gate status.
10. Customer feedback/rating and a documented quality-improvement loop.

Do not use one generic QR code, demo, or screenshot for every product. Do not invent demo footage or screenshots. If an asset is missing, show a clear “Not yet available” state and keep the product out of any “verified/ready” listing.

## 5. Product passport data contract

Each product passport should record:
- `product_id`
- `canonical_name`
- `version`
- `one_line_description`
- `intended_users`
- `use_cases`
- `how_to_use`
- `inputs` and `outputs`
- `price` and currency, or `quote_required`
- `demo_url` and `screenshot_url`, if real assets exist
- `qr_destination`
- `tests`, `test_results`, and `evidence_links`
- `known_limitations`
- `status`: `DRAFT`, `IN_DEVELOPMENT`, `TESTING`, `VERIFIED`, or `BLOCKED`
- `last_verified_at`

The `VERIFIED` state requires product-specific passing tests and evidence. It must never be inferred from the presence of a record or workflow run.

## 6. First real-income offer

**Service:** Hindi/English writing, research summaries, and website/blog content.

**Enquiry template**
- Customer objective:
- Topic:
- Language:
- Word count / scope:
- Deadline:
- Source links / reference material:
- Budget:
- Intended audience / publishing channel:

**Commercial gate:** Confirm scope, deliverables, price, deadline, revisions, and payment terms in writing before work begins. Do not promise sales, income, research certainty, or turnaround until scope and capacity have been reviewed. Do not claim that any customer or institution has been contacted unless an authorized outbound channel reports a successful send.

## 7. Security and privacy gates

- Never commit API keys, passwords, tokens, private customer content, or raw voice samples to the repository.
- Use least-privilege credentials, secret storage, dependency checks, input validation, rate limits, audit logs, and an incident-response process.
- Outreach automation must use lawful, public/authorized contact routes, relevant messages, rate limits, opt-out handling, and human approval before sending.
- Keep customer information minimal and disclose how enquiry data will be used.

## 8. Acceptance tests

A release candidate must demonstrate:
- [ ] Original-photo asset hash/provenance recorded; only layout resizing applied.
- [ ] Authorized voice source and provider permission recorded.
- [ ] Speech input/output tested with consent and representative prompts.
- [ ] Context and intent tests pass.
- [ ] Evidence states correctly assigned, including insufficient-evidence behavior.
- [ ] Respectful communication regression tests pass.
- [ ] Voice output is synchronized with facial/lip movement where lip-sync is enabled.
- [ ] Product-specific QR opens the matching passport.
- [ ] Product-specific demo and screenshot correspond to the tested version.
- [ ] Usage guide and limitations are visible.
- [ ] End-to-end logs contain timestamps, version, test outcome, and error state without exposing sensitive data.
- [ ] Failed critical tests block the `VERIFIED` state.

## 9. Current status boundary

This document records the approved design and measurable acceptance criteria. It does **not** claim that the original photo/audio have been located in the repository, that a HeyGen integration is active, that live lip-sync has passed, that any product demo has been recorded, or that revenue/outreach has occurred. Those claims require separate evidence.
