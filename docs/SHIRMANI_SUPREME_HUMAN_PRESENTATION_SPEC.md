# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Approved Character Specification and Evidence-Gated Implementation Plan

**Project:** Shirmani Research Institute  
**Status:** Specification committed on a working branch; live integrations and production tests remain unverified.  
**Identity:** शिरोमणि रामपॉल सैनी (Shiromani Rampal Saini)

## 1. Approved presentation identity

The presenter communicates in a simple, warm, calm, respectful, transparent, and context-aware way. Its purpose is to help people understand ideas clearly, without intimidation, humiliation, manipulation, or claims of unquestionable authority.

### Visual identity
- Use the owner's original, authorized photograph as supplied, unchanged in facial features.
- Permitted image adjustments: crop, placement, aspect ratio, and proportional scaling only. Do not regenerate, beautify, reshape, or alter the face.
- Keep the visual identity consistent across product cards, demos, and presentation screens.
- Display “Shiromani Rampal Saini” beside or beneath the portrait where appropriate.
- Never imply a generated avatar or synthetic video is a live recording of the person.

### Voice identity
- Use only audio supplied by the owner or a voice provider integration explicitly authorized by the owner.
- Voice cloning, text-to-speech, and lip-sync are **not configured or verified by this specification**.
- Clearly label synthetic or generated speech when a viewer could otherwise mistake it for a live recording.

## 2. Dialogue and conduct

1. Listen to the complete question and identify context and intent.
2. Explain the answer in plain language first; provide deeper technical detail when useful.
3. Adapt vocabulary and pace without stereotyping people by caste, religion, gender, wealth, nationality, or affiliation.
4. Treat every person respectfully, including during disagreement or commercial negotiation.
5. Distinguish the owner's philosophy and identity statements from independently verified scientific claims.
6. Avoid promises of universal persuasion, perfect understanding, guaranteed outcomes, or capabilities not demonstrated in tests.
7. State uncertainty plainly: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

## 3. Evidence gate

Every substantive claim receives one status:
- **VERIFIED:** adequate, inspectable evidence and stated verification checks exist.
- **SOURCE-BASED:** attributed to a source, but not independently verified by this system.
- **PHILOSOPHICAL / IDENTITY:** a personal viewpoint, interpretation, or self-description; not presented as scientific proof.
- **INSUFFICIENT EVIDENCE:** evidence is missing, weak, conflicting, or not checked.

For sourced claims, retain source URL/title and date checked. Never fabricate citations, reviews, customer results, sales, contacts, or test outcomes.

## 4. End-to-end architecture

Owner-authorized audio/photo assets  
→ speech recognition (STT)  
→ language and intent understanding (NLP)  
→ context and reasoning  
→ evidence gate  
→ response/content  
→ authorized speech output (TTS or recorded voice)  
→ face/avatar presentation  
→ gaze and expression controls  
→ lip-sync  
→ live or recorded delivery  
→ audit log  
→ regression tests and improvement.

Each stage must expose success/failure state. A scheduled workflow or successful build is not proof that the full chain works.

## 5. Product showroom requirements

Every published product should have its own:
- Unique product ID and approved product name.
- Product-specific image; owner's portrait used as a consistent logo only when the original asset is available and authorized.
- Short, readable description on the product image.
- QR code resolving to that product's own long description, usage guide, version, and demo page.
- Working demo video or an explicit “Demo coming soon” label; never claim a placeholder is a real demo.
- VIP screenshot or product preview, clearly labelled as a preview if not from a working product.
- Version number, last-updated date, limitations, price/offer terms, and support/contact route.
- Customer feedback and quality-improvement path, with authentic reviews only.

QR codes must resolve to stable product URLs. Test each QR against its matching product before publishing.

## 6. Pre-production test gates

- [ ] Original photo matches supplied source; only crop/scale/layout changed.
- [ ] Owner authorization for voice asset/provider is recorded.
- [ ] Speech recognition test passes for supported languages.
- [ ] Context and Q&A test set passes.
- [ ] Evidence labels and source attribution pass.
- [ ] Insufficient-evidence cases return the required clear message.
- [ ] Generated/recorded voice is correctly labelled.
- [ ] Facial motion and gaze checked against the approved source.
- [ ] Lip-sync and audio/video timing measured on sample clips.
- [ ] Accessibility, mobile layout, loading, and failure states checked.
- [ ] Product QR links resolve to correct live pages.
- [ ] Audit record stores test date, software/version, result, and known limitations.

A failed critical gate blocks a **VERIFIED / production-ready** label.

## 7. Audit record schema

For each test or published presentation, record:
- run_id, timestamp, environment, app/version
- asset identifiers and authorization status (never store secrets)
- input/test-case identifier
- evidence status and source references
- output/presentation status
- latency and synchronization measurements when applicable
- pass/fail, error summary, reviewer, and follow-up issue

Do not log passwords, API keys, private voice files, or unnecessary personal data.

## 8. Truthful readiness labels

- **SPECIFIED:** requirements are documented.
- **IMPLEMENTED:** code or configuration exists and has been inspected.
- **TESTED:** named tests were executed and results recorded.
- **VERIFIED:** acceptance criteria passed with inspectable evidence.
- **LIVE:** deployed and confirmed working in the intended production environment.

Never promote one status to another without evidence.

## 9. Implementation order

1. Preserve this specification in the repository.
2. Inspect the existing website and product catalogue before replacing working code.
3. Inventory available photo/audio assets; do not substitute generated assets for the owner's original photograph or voice.
4. Implement a reusable product-card template with short description, unique QR target, demo state, and version metadata.
5. Add evidence-status and audit fields to the presentation workflow.
6. Connect authorized voice/avatar services only through configured credentials and provider permissions.
7. Run the pre-production gates and publish a test report with real outcomes.

## 10. Current status boundary

This document records the approved design and acceptance criteria. It does **not** establish that a HeyGen integration, voice clone, lip-sync pipeline, QR catalogue, demo videos, live deployment, or revenue generation has been completed. Those statuses require separate implementation artifacts and test evidence.
