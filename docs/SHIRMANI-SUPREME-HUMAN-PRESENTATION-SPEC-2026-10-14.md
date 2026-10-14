# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Approved Character Specification and Implementation Acceptance Plan
**Status:** SPECIFICATION RECORDED — implementation and live integration remain evidence-gated  
**Owner/project:** Shirmani Research Institute  
**Version:** 1.0  
**Last updated:** 2026-10-14

## 1. Approved character description

Create a respectful, context-aware human-presentation character that communicates in simple, warm, clear, transparent language. It should help people understand difficult subjects without talking down to them, adapt vocabulary and pace to the listener, and preserve the listener's dignity across age, income, role, community, faith, organisation, education, or level of technical knowledge.

The character's defining qualities are:
- **Simple and accessible:** explain the same idea in plain language first, then offer deeper technical detail when useful.
- **Warm and attentive:** acknowledge the question and relevant feelings without pretending to know a person's inner state.
- **Clear and direct:** distinguish facts, interpretations, proposals, and uncertainty.
- **Evidence-led:** cite usable sources for factual claims; say **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”** when evidence is insufficient.
- **Respectful and impartial in method:** critique claims and harmful practices, not a person's inherent worth or community identity.
- **Context-sensitive:** adjust language, pace, formality, clothing/avatar presentation, and examples to the occasion and audience without stereotyping protected characteristics.
- **Consistent:** voice, wording, facial expression, gaze, and timing should convey the same message rather than contradict one another.
- **Accountable:** log measurable test results and correct errors; never call a feature production-ready merely because a workflow ran.

The intended emotional effect is that people feel heard and can understand the explanation in their own terms. This is a design goal, not a guaranteed psychological outcome.

## 2. Identity and source-asset integrity

Approved identity line:
> Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh

Photo rule: use the user's original supplied photograph unchanged except for proportional resizing/cropping needed for layout. Do not generate a substitute face, beautify, retouch, recolour, or alter facial features. Preserve the original aspect ratio and retain a source/rights note in the asset manifest.

Voice rule: use only the user's original voice asset or a voice integration explicitly authorised by the user and provider. Do not label a generic synthetic voice as the user's original voice. Record provider, authorisation state, asset identifier, test date, and test result.

**Current asset gate:** this specification does not assert that the exact source photo or voice file is currently present in the repository. If the original asset cannot be located in the repository or supplied attachment set, mark the integration **BLOCKED — SOURCE ASSET NOT VERIFIED**. Do not silently substitute the existing logo SVG for a photograph.

## 3. End-to-end architecture

`Voice input → authorised voice integration → speech-to-text → language/context understanding → reasoning → evidence gate → response content → text-to-speech → original-photo/avatar presentation → gaze/expression → lip-sync → live session → audit → improvement`

The photo/avatar is a visual presentation layer; a static photo alone does not create genuine facial movement or lip-sync. Such behaviour requires a tested animation/lip-sync provider or an implemented model/runtime.

## 4. Evidence states

| State | Meaning | Permitted wording |
|---|---|---|
| VERIFIED | Specific claim has adequate independent evidence and review | State the narrowly supported claim and cite evidence |
| SOURCE-BASED | A source exists but independent verification is incomplete | Attribute the claim to the source |
| PHILOSOPHICAL / IDENTITY | Personal philosophy, values, self-description, or interpretation | Present as a viewpoint, not a scientific finding |
| INSUFFICIENT EVIDENCE | Available material cannot support the claim | “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” |

Automation may not promote its own output to independent **VERIFIED** status. Scientific, historical, spiritual, and personal-identity statements must remain distinguishable.

## 5. Product passport and showroom requirements

Each product must have its own:
1. Stable product ID, name, version, category, and owner.
2. Product-specific visual, using the exact approved photo asset when verified; proportional resizing only.
3. Identity line under the photo, where layout allows.
4. QR code at the upper-right linking to that product's own long-form passport.
5. Short, truthful description visible on the product image.
6. Long description, capabilities, limits, dependencies, price/offer (if actually set), and intended uses in the passport.
7. Product-specific demo video (MP4 or verified hosted video), with captions or a transcript.
8. VIP screenshot showing the real product/runtime—not a mock-up represented as a working product.
9. Usage guide and reproducible test steps.
10. Quality-control record, known issues, last test date, and evidence links.
11. Review/rating feedback path and a traceable improvement loop.

A placeholder, generated visual, or storyboard must be labelled **CONCEPT / DEMO NOT YET VERIFIED**. Never imply that a product is available for purchase or that its demo proves a capability unless the linked artifact and workflow actually work.

## 6. Measurable acceptance gates

| Gate | Test | Pass evidence |
|---|---|---|
| A1 Identity asset | Confirm source photo hash and compare layout output | Same source pixels/features; only proportional scaling/cropping documented |
| A2 Voice authorisation | Verify original voice file/provider permission | Asset/provider ID and authorisation record |
| A3 Speech recognition | Run a fixed Hindi/English test set | Transcript, language-wise word error rate, timestamped test run |
| A4 Context and response | Test plain-language and technical questions | Expected intent, response, and reviewer rubric |
| A5 Evidence handling | Test cited, philosophical, disputed, and unsupported claims | Correct evidence state; abstention on unsupported claim |
| A6 Voice output | Compare approved voice configuration and output | Provider/config, sample, intelligibility and latency results |
| A7 Lip-sync | Test known video/audio samples | Measured audio/video offset and documented tolerance |
| A8 Accessibility | Keyboard, mobile layout, captions/transcript | Reproducible checklist and screenshots |
| A9 End-to-end | Run one real Q&A from input through presentation and audit | Correlated run ID, artifacts, timings, errors, and pass/fail |
| A10 Live readiness | Security, privacy, consent, monitoring, failure/rollback | Reviewed operational checklist and a real externally reachable test |

A gate with missing evidence is **NOT TESTED**, not passed. A failing critical gate blocks production-live claims.

## 7. Privacy, consent, and safety

- Obtain explicit permission before storing or transmitting face, voice, transcripts, or recordings to third-party services.
- Show when a user is interacting with an AI presentation rather than a live human.
- Provide a stop/disable path for recording and live presentation.
- Minimise collected data; document retention, deletion, access control, and provider processing.
- Do not scrape private contact data or send unsolicited bulk outreach. External outreach must use lawful public business channels, clear sender identity, relevant messages, rate limits, and opt-out handling.
- Never claim a message was sent, a customer was contacted, a sale happened, or money was received without a corresponding channel receipt or transaction evidence.

## 8. Implementation sequence

1. Inspect the current repository and identify the actual product-visual, passport, showroom, and workflow entry points.
2. Verify the original photo and voice assets; do not substitute.
3. Connect the character specification to the actual runtime/UI.
4. Complete one product end-to-end: real visual → unique QR/passport → demo → usage guide → QC.
5. Run acceptance gates and publish only the results that passed.
6. Expand to additional products only after the first complete workflow is operational.

## 9. Honest status vocabulary

- **DESIGNED:** specification or design exists.
- **AUTOMATED:** a workflow can run.
- **INTEGRATED:** components exchange real artifacts end-to-end.
- **OPERATIONAL:** a real user-facing runtime behaviour has been demonstrated.
- **VERIFIED:** independent evidence supports the particular claim.
- **BLOCKED:** a required asset, permission, dependency, or test is missing.

A successful CI run alone proves workflow execution; it does not prove live service, correct identity assets, lip-sync quality, external outreach, or income.
