# SRI-HV-001 — Heart-View Human Presentation Production Contract

**Version:** 1.0.0  
**Status:** Production specification; provider-backed live avatar is not yet connected.  
**Purpose:** Turn the author's stated communication values into a testable, respectful presentation product without claiming that subjective or philosophical statements are independently established scientific facts.

## 1. Character profile

The presentation should consistently aim to be simple, calm, clear, natural and transparent; respectful across income, profession, nationality, caste, religion, organisation and worldview; direct without humiliation, coercion, exaggerated promises or pressure tactics; warm and attentive; and explicit about uncertainty and source quality.

The user's identity statement and philosophical framework may be presented as the author's self-description. The system must not convert them into universal scientific claims without suitable independent evidence.

## 2. Required chain

`Voice input → Speech recognition → Intent/context → Response draft → Evidence gate → Authorized voice output → Approved photo/avatar → Expression/gaze → Lip-sync → Live presentation → Audit and improvement`

Each component has an independent readiness field. A planning screen or browser animation is not evidence that a hosted model, voice provider, face animation service, live stream or payment system is connected.

## 3. Four presentation versions

| Version | Use | Required behavior |
|---|---|---|
| V1 — Clear | Text/script and static presentation | Plain language, audience and purpose fields, exportable script |
| V2 — Voice | Speech input/output | Explicit voice authorization, transcript review, compatibility notice |
| V3 — Avatar | Approved photo/avatar and expression | Consent/authorization record, asset rights, face/voice matching checks |
| V4 — Live | Interactive Q&A/live presentation | End-to-end latency, moderation, evidence state, failure fallback and session audit |

Versions describe capability tiers, not a claim that external services have been integrated.

## 4. Evidence gate

- **VERIFIED:** sufficient independent evidence and a documented check support the specific claim.
- **SOURCE-BASED:** source links exist, but independent verification is incomplete.
- **PHILOSOPHICAL / IDENTITY:** author-declared belief, personal account, value or self-description.
- **INSUFFICIENT EVIDENCE:** no adequate support is available; say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

Keep source facts, inference, interpretation, confidence and unresolved uncertainty separate.

## 5. Acceptance tests

A release candidate must record pass/fail for:
1. Hindi and English script clarity.
2. Correct capture of user intent and context.
3. Evidence-state selection, including insufficient-evidence cases.
4. Respectful language; no demographic stereotyping or demeaning comparison.
5. Explicit authorization before using a real person's voice, face or likeness.
6. Transcript review and correction before publication.
7. Voice-to-face timing and lip-sync on actual supported test media.
8. End-to-end latency and interruption/fallback behavior.
9. Mobile layout, keyboard access, captions/transcript and readable contrast.
10. Privacy, data retention, deletion and incident handling.
11. Exported audit record with product version, test date, test result and known limitations.
12. No release marked LIVE or READY when a critical integration or test is missing.

## 6. Release record

For every version, record product ID/version and build commit; connected components and provider/configuration version; test inputs, expected/observed outputs and pass/fail; authorization state (never store sensitive proof in public logs); media references and usage rights; QC code, reviewer and release decision; public demo URL, actual recorded demo-video URL (if produced), screenshot and usage guide; price, included usage, support/refund terms and checkout state.

Never substitute a storyboard, demo script, mock avatar or generated preview for a real recorded MP4.

## 7. Commercial boundary

The browser prototype can be offered as a planning/demo tool only until provider-backed features pass tests. Do not promise a finished avatar, one-hour delivery, always-on operation, natural lip-sync, global scale or guaranteed emotional effect unless each promise has a measurable, tested service level.

Before a paid project begins, agree in writing on scope, deliverables, source assets, voice/likeness rights, timeline, revisions, price and payment terms. No sales, contact, payment or revenue is claimed by this contract.

## 8. Continuous improvement loop

`Customer feedback → classify issue → prioritize by impact → create change → run regression tests → review evidence → publish version notes → update demo and guide`

Public feedback creates a reviewed work item; it does not automatically change production code. Changes ship only after regression and release checks.
