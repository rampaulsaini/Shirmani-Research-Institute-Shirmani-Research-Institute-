# Shirmani Supreme Human-Presentation System — Implementation Roadmap
**Date:** 2026-10-14  
**Product:** SRI-PRES-001 / Heart-View Character Studio  
**State:** Implementation plan; not a claim that live voice/avatar/lip-sync is active.

## Character contract
- Identity line: **Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh**
- Preserve the original authorised portrait unchanged except proportional scaling and neutral layout/cropping. Do not synthesize a replacement face and call it the original.
- Use the user's authorised voice recording only when the actual file and permission are available.
- Speak simply first; add examples and technical depth on request. Respect different people and communities without flattery, pressure, or claims of superiority over them.
- Distinguish **INDEPENDENTLY VERIFIED**, **SOURCE-BASED**, **PHILOSOPHICAL / PERSONAL PERSPECTIVE**, and **INSUFFICIENT EVIDENCE**. For insufficient evidence say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

## Measurable pipeline
1. **Voice input:** microphone permission, speech-to-text, language detection, transcript preview and correction.
2. **Context and response:** intent, user goal, conversational context, plain-language answer, optional specialist explanation.
3. **Evidence gate:** sources attached to factual claims; philosophy attributed to the stated perspective; uncertainty visible.
4. **Authorised voice output:** provider integration behind a server-side key; consent/asset check; no key in browser code.
5. **Photo/avatar:** exact source portrait, no identity-altering edits; approved context-specific background and lighting.
6. **Lip-sync:** generated only from an authorised source and an actual provider job; record job ID, output URL, duration, and review status.
7. **Live presentation:** only activate after end-to-end tests; label prerecorded or synthetic presentation clearly where appropriate.
8. **Audit/improvement:** store minimal, consented test inputs, timing, defect, reviewer result, and fix reference. Do not retain sensitive conversations by default.

## Four staged versions
- **V1 — Character Brief & Rehearsal:** existing browser-local tool; manual scripts and checklist.
- **V2 — Evidence-aware Presenter:** response drafting, source ledger, captions and export; provider integrations remain optional.
- **V3 — Authorised Voice + Avatar:** STT/TTS and avatar/lip-sync using configured providers, consented assets and server-side credentials.
- **V4 — Live Studio:** moderated live Q&A, stream output, telemetry, rollback and operator controls.

Each version is a distinct scope. Do not advertise V3/V4 as available until actual provider integration, legal/consent checks, and end-to-end demonstration pass.

## NVIDIA integration lane
Evaluate NVIDIA tools by task and current account access, not by branding:
- **Riva** for speech recognition/synthesis where deployment, language and hardware requirements fit.
- **NeMo** for model development/evaluation and guardrail experiments.
- **NVIDIA NIM** for supported inference microservices where compatible endpoints and credentials are available.
- **Maxine** for supported audio/video enhancement where licensing and deployment requirements fit.
No NVIDIA account, GPU, API key, model endpoint or successful integration is assumed by this document. Keep credentials server-side; test latency, Hindi/English quality, privacy, cost, fallback and accessibility before selection.

## Product release contract
Every public product must expose a real working example, product-specific passport, actual demo video or the explicit state **STORYBOARD — NOT RECORDED**, actual screenshot or **ILLUSTRATIVE MOCK-UP**, usage guide, price/quote basis, limits, QC status, and enquiry path. A QR is valid only after its destination is deployed and tested on mobile.

## Immediate execution order
1. Merge and run the layered security workflow; configure branch protection and secret scanning in GitHub settings.
2. Inventory the existing public tools and separate working browser-local prototypes from live provider integrations.
3. Improve SRI-PRES-001 with a sample question, evidence labels and an end-to-end manual rehearsal.
4. Connect one provider at a time using documented APIs and consented assets; record actual output artefacts.
5. Produce one real MP4 demo and one actual screenshot for the first product; do not substitute a storyboard/mock-up.
6. Publish only tested features to the showroom and start a measured writing/research enquiry funnel.

## Release metrics
- Working use cases with reproducible example.
- Real MP4 demos / published products.
- Actual screenshots / published products.
- Products with tested QR, guide, passport, price basis and enquiry path.
- Critical security findings open.
- Provider end-to-end tests passed.
- Qualified prospects, human-confirmed outreach, replies, quotes and paid orders—each counted only with evidence.
