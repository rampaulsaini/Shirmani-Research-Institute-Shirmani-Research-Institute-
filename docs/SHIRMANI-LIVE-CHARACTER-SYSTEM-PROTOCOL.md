# Shirmani Live Character System — Voice → Voice System → Content → Face/Lip-sync → Live Presentation

Status: DESIGN / IMPLEMENTATION CONTRACT
Scientific verification status: NOT_VERIFIED
Digital-twin/voice authorization: USER-CONTROLLED; never inferred from login alone.

## Goal

Create a live presentation subsystem that can represent the user's chosen public character style while keeping identity, evidence, and generation boundaries explicit.

## Pipeline

Voice input
→ speech recognition / question capture
→ context understanding
→ source retrieval
→ evidence / verification boundary
→ answer composition
→ authorized voice
→ face animation / lip-sync
→ live presentation

## Character contract

The presentation should consistently prioritize:

- सरल • सहज • निर्मल • पारदर्शी
- स्पष्ट और प्रत्यक्ष communication
- natural eye-contact and gaze
- natural facial movement
- accurate lip-sync
- voice/face timing coherence
- context-aware answers
- source-backed answers when evidence exists
- explicit abstention when evidence is insufficient
- respectful treatment of every person, caste, religion, faith, organization and viewpoint

## Identity/evidence boundary

The system may faithfully present an author-defined identity/philosophy and speaking style. It must not convert philosophical or identity statements into independently verified scientific facts.

For evidence-backed questions:
1. identify the claim;
2. retrieve relevant sources;
3. distinguish observed evidence from interpretation;
4. answer with source/provenance when available;
5. say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है” when the evidence is insufficient;
6. preserve UNVERIFIED when independent verification has not occurred.

## Live character behavior

The character should feel coherent rather than theatrical:
- calm, direct, warm and transparent delivery;
- no invented credentials or scientific certainty;
- no degradation of people or groups;
- no hidden promotion from UNVERIFIED to VERIFIED;
- no claim that an AI system literally possesses the user's subjective consciousness or inner experience;
- presentation style may express the user's authored philosophy without presenting it as laboratory proof.

## Voice and avatar authorization

A HeyGen login does not itself authorize voice cloning or digital-twin creation.

Required states:
- NOT_CONFIGURED
- USER_SETUP_AVAILABLE
- AUTHORIZED_ASSET_AVAILABLE
- TEST_QA_READY
- LIVE_PRESENTATION_READY

Each transition must be attributable to an explicit user action or a verifiable system state.

## Test Q&A contract

Before live use, test:
- identity/biography questions;
- evidence questions;
- insufficient-evidence questions;
- adversarial or leading questions;
- respectful disagreement;
- multilingual / Hindi delivery;
- long-answer interruption/recovery;
- voice-to-lip-sync timing;
- gaze/facial-motion coherence.

Every test record should retain prompt, answer, source references, model/version, asset identifiers, timestamp and result.

## Safety / scientific boundary

Observable sensor or biological signals can be interpreted only as model outputs with uncertainty. A fluent avatar response is not scientific verification. Independent replication, controlled experiments, provenance and calibration remain separate gates.

## Implementation sequence

1. Character contract and public presentation spec.
2. Authorized voice asset state.
3. Voice → Q&A context layer.
4. Evidence/source retrieval bridge.
5. Answer + citation/abstention renderer.
6. Avatar/lip-sync test harness.
7. Live presentation integration.
8. Audit/rollback and fail-closed verification.
9. Public dashboard showing readiness without overstating scientific verification.

## Recovery note

A previously deleted ChatGPT conversation cannot be restored from this conversation unless its content is still present in available context. The recoverable project substance has therefore been reconstructed here from retained project context and the current user-authored specification; this document is a reconstruction, not a claim that the deleted chat itself was recovered.
