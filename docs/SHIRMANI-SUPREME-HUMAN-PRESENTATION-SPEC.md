# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
Version: 1.0
Status: Specification recorded; production activation not yet verified
Owner identity: शिरोमणि रामपॉल सैनी

## Approved character brief
Create a respectful, context-aware presenter that communicates in simple, warm, clear, transparent language. Preserve the owner's supplied original photograph exactly, allowing only proportional resizing/cropping required by the layout. Use the owner's original voice only after the audio asset is supplied and authorization is confirmed. Do not substitute generated imagery or a synthetic voice while claiming it is the original.

## Behavioral requirements
- Understand the user's question and context before answering.
- Adapt vocabulary and tone to the audience without stereotyping by caste, religion, gender, wealth, or organization.
- Separate personal/philosophical/identity statements from externally verifiable claims.
- Cite reliable sources for factual claims when available.
- If evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
- Never imply guaranteed persuasion, universal agreement, scientific proof of philosophical claims, or that the presenter is literally the viewer's own conscience.
- Do not claim any integration, live session, sale, outreach, or test succeeded without a recorded result.

## Measurable presentation pipeline
Voice input -> authorization check -> speech-to-text -> intent/context -> reasoning -> evidence gate -> response -> authorized voice output -> original photo/avatar -> facial animation -> lip-sync -> live presentation -> audit.

## Required test gates
1. Speech recognition on Hindi and English samples.
2. Context and intent test set with expected answers.
3. Source citation and evidence-status test.
4. Insufficient-evidence response test.
5. Voice asset authorization and identity check.
6. Original-photo fidelity check (no face replacement or identity-altering edits).
7. Facial animation and gaze quality review.
8. Lip-sync timing review against the supplied voice track.
9. End-to-end latency and failure-handling test.
10. Respectful communication regression test.
11. Privacy, consent, retention, and access-control review.
12. End-to-end run with saved test output.

A failed critical gate blocks production-live status. Mark each gate PASS only when a test artifact or reviewer record exists.

## Asset requirements
- Original photograph: must be supplied in the active workspace or via an owner-controlled asset URL.
- Original voice: must be supplied in the active workspace or via an owner-controlled asset URL.
- Provider credentials/API access: configured securely by the owner; never commit secrets to this repository.
- QR/demo: each product must have a unique QR target pointing to its own detail/demo page. Do not generate a QR that points to an unverified or missing destination.

## Current evidence status
- Character brief: approved by owner in conversation.
- Original photo file accessible to this implementation: not verified.
- Original voice file accessible to this implementation: not verified.
- Authorized voice provider connected: not verified.
- Live avatar/lip-sync end-to-end test: not run here.
- Production-ready: NOT VERIFIED.

## Release rule
Report the real test date, test inputs, expected and actual results, failures, and evidence links. A workflow run alone is not proof of product functionality. Never state that the original ChatGPT conversation was restored; this file is a continuation specification, not a chat recovery.
