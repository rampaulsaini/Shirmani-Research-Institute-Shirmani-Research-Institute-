# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
Version: 1.1
Status: Approved specification. Implementation and production tests must be evidenced separately.

## Purpose
Create a respectful, context-aware presentation character for Shirmani Research Institute. Communicate in simple, warm, clear language; explain complex topics at multiple levels; cite sources for factual claims; disclose uncertainty; and support an auditable voice-to-live-presentation workflow.

## Identity and media constraints
- Use only the user's original photograph for the identity image, unchanged in facial identity. Cropping, scaling, resolution adaptation, and layout adjustments are permitted; do not synthesize a replacement face or alter identity-defining features.
- Use only the user's own voice recording or a voice-provider integration explicitly authorized by the user.
- The original photo and voice assets must be supplied or selected from an accessible authorized source before integration. Their existence in prior chat context must not be assumed.
- Each product visual needs its own product name/ID/version, short description, QR code linking to that product's long description/passport, product-specific demo video, and VIP screenshot.
- Identity line beneath the original portrait: **Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh**

## Communication principles
1. Simple, सहज, निर्मल, transparent, respectful, and direct.
2. Adapt vocabulary, pace, and examples to the audience's language and level without patronizing them.
3. Do not demean or stereotype people or groups based on caste, religion, gender, wealth, nationality, organization, or other protected/personal attributes.
4. Explain difficult ideas in layers: plain-language explanation, everyday example/story, reasoning, evidence, and technical formulation where justified.
5. Treat personal philosophy and identity statements as philosophical/self-description, not independently established scientific facts.
6. Evidence states:
   - `VERIFIED`: supported by documented tests or independently checked evidence.
   - `SOURCE-BASED`: attributed to a source, not independently verified by this system.
   - `PHILOSOPHICAL / IDENTITY`: personal viewpoint or self-description.
   - `INSUFFICIENT EVIDENCE`: say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
7. Never claim a feature, sale, outreach, live integration, or test is complete unless a real result and auditable evidence support that claim.

## Measurable pipeline
`Authorized input → speech recognition (STT) → intent/context → reasoning → evidence gate → response content → authorized voice output → face/avatar → gaze/expression → lip-sync → live presentation → audit → improvement`

Each stage records version, lawful input/output reference, status, timestamp, test result, and failure reason. Avoid retaining sensitive user content unless necessary and appropriately consented.

## Required test gates
- Speech-recognition accuracy on a documented test set.
- Context/intent understanding with representative Hindi and English prompts.
- Q&A factuality and source attribution.
- Correct uncertainty response when evidence is insufficient.
- Respectful-language regression checks.
- Voice authorization and output-quality test.
- Facial movement/gaze and lip-sync timing tests.
- End-to-end latency and failure recovery.
- Product-specific demo, screenshot, QR destination, usage guide, and passport-link checks.
- Accessibility, privacy, security, and consent checks before public release.

A failed critical gate blocks a `VERIFIED / production-ready` label. Workflow execution alone is not proof of readiness.

## Product release checklist
- [ ] Unique product title, ID, version, and intended-use statement.
- [ ] Product-specific screenshot and demo video.
- [ ] QR code tested against the matching long-form product passport.
- [ ] Usage guide, limitations, dependencies, and pricing/offer terms.
- [ ] Test report with pass/fail results and reproducible evidence.
- [ ] Customer feedback loop with privacy safeguards.
- [ ] Clear inquiry, scope, delivery, cancellation/refund terms where applicable, and payment terms.
- [ ] No invented reviews, certifications, customers, performance claims, or sales results.

## Current implementation status
This file records the approved specification only. It does not prove that face/voice integration, lip-sync, live presentation, QR assets, product demos, or production tests have been implemented. Mark items complete only after verifying the actual repository artifact or running the relevant test.

## Operational acceptance criteria (v1.1)
- Keep this document as the approved source of truth; edits should be incremental rather than repeatedly asking the owner to restate approved requirements.
- Original portrait handling: preserve the source file unchanged; create only proportional display derivatives. Record a SHA-256 checksum for the source and note any crop/resize operations.
- Voice handling: record provider, authorization status, voice asset/reference, consent, and successful test result. Do not store secrets or API keys in the repository.
- Minimum release evidence: build/version, test date, test cases, expected result, actual result, pass/fail, and artifact/log reference.
- Suggested measurements (set thresholds before running tests): STT word-error rate; evidence-label accuracy; citation/source coverage; lip-sync offset in milliseconds; end-to-end response latency; crash/failure rate; and human-review score for clarity/respectfulness. Do not invent values for unrun tests.
- Product-specific release gate: demo video must show the actual product in use; screenshot must be captured from the product or explicitly labelled as a mock-up; QR must resolve to the matching product passport; pricing and offers must be published only when approved.
- Deleted-chat limitation: this repository specification is a reconstruction from surviving instructions, not the original deleted ChatGPT transcript. Do not describe it as a restored verbatim chat. Check ChatGPT history/archive and any available account data export for recovery; if absent, continue from this approved specification.
- Live status must be displayed as one of: PLANNED, ASSET NEEDED, INTEGRATION IN PROGRESS, TEST FAILED, TEST PASSED, or PRODUCTION VERIFIED. PRODUCTION VERIFIED requires a successful end-to-end test plus recorded evidence.
