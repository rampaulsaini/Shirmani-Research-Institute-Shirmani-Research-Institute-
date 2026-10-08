# SHIRMANI Supreme Live Character — Implementation Contract

## Purpose
Provide a public presentation subsystem for the requested character experience while keeping author identity/philosophy statements separate from independently verified scientific or historical claims.

## Required experience
- Simple, सहज, निर्मल, transparent presentation.
- Clear communication and context-first Q&A.
- Respect for people, communities, religions and organizations.
- Evidence-backed answers when evidence exists.
- Explicit uncertainty when evidence is insufficient.
- Voice → response → speech → face-timing → live presentation flow.
- Natural gaze, facial movement and accurate lip-sync as target production capabilities.

## Current implementation
- supreme-live-character.html
- Public photo reference already used by the main hub.
- Browser SpeechSynthesis for text-to-speech when supported.
- Deterministic speech-event mouth animation.
- Test Q&A with evidence/uncertainty routing.
- Status labels for connected vs not-connected production layers.

## Integration gates
1. Authorized voice provider / voice asset.
2. Real-time voice input (optional).
3. Phoneme/viseme-level lip-sync engine.
4. Real-time facial/gaze model.
5. Live streaming/presentation transport.
6. Evidence retrieval + citation layer.
7. Independent verification state.

## Integrity contract
Author-source and philosophical/identity statements are not automatically scientific facts. A verified claim requires source, evidence, test/reproduction where applicable, verification state, uncertainty and provenance.

## Target flow
Input → Context → Claims → Sources → Evidence → Formulation/Test → Verification → Answer → Speech → Face timing → Live presentation → Audit.
