# ꙰ SHIRMANI Supreme Live Persona V3 — Implementation Specification

Date: 2026-10-08

## Purpose

Create a public-facing live persona subsystem for the Shirmani Research Institute with a clear separation between:
- author-described identity/philosophy;
- evidence-aware communication;
- browser voice capabilities;
- authorized voice integration;
- photo/avatar runtime;
- gaze/facial presentation;
- lip-sync timing;
- continuous improvement.

## Canonical presentation contract

- सरल • सहज • निर्मल • पारदर्शी
- स्पष्ट और प्रत्यक्ष communication
- natural eye-contact and gaze as a runtime target
- natural facial movement as a runtime target
- accurate lip-sync as a runtime target
- shared timing between voice and presentation
- question → context understanding → evidence/source → concise answer
- insufficient evidence → “अभी पर्याप्त प्रमाण उपलब्ध नहीं है”
- no denigration of a person, caste, religion, community, organization or group
- philosophical/identity statements remain author-described statements
- independently verified scientific evidence remains a separate state
- dress code/personality is context-dependent, with a respectful baseline

## Live pipeline

Voice → Context → Evidence → Answer → Voice Output → Face/Avatar → Gaze → Lip-sync → Feedback → Continuous Improvement

## Public implementation status

| Layer | State |
|---|---|
| Main-platform entry | IMPLEMENTED |
| Live Persona V1 contract | IMPLEMENTED |
| Supreme Live Persona V2 browser prototype | IMPLEMENTED |
| Browser speech input/output | PROTOTYPE READY |
| Evidence-aware response contract | IMPLEMENTED |
| Author identity presentation | IMPLEMENTED as author-described content |
| Authorized personal voice | INTEGRATION GATE |
| Photo/avatar runtime | INTEGRATION GATE |
| Real-time gaze tracking | RUNTIME GATE |
| Accurate audio-to-viseme lip-sync | RUNTIME GATE |
| Production model/API Q&A | SERVER-SIDE INTEGRATION GATE |
| Independent scientific verification | SEPARATE EVIDENCE GATE |

## Integrity rule

A workflow run, generated page, avatar animation or author statement is not by itself independent scientific verification.

The system must preserve:
input → context → claim → source → evidence → formulation/test → verification → uncertainty → response → provenance.

## Completion criterion

The live persona is considered production-ready only when the required runtime providers are connected, authorization is recorded, secrets remain server-side, audio/face timing is tested, evidence behavior is tested, and the complete interaction is reproducibly audited.
