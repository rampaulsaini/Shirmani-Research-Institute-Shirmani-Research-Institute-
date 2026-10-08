# SHIRMANI Live Presentation System

## Purpose
Voice → authorized voice integration → test Q&A → photo/lip-sync → live presentation

## Non-negotiable state boundary
A configured workflow is not the same thing as a live service. The system may mark a stage READY, NOT_CONNECTED, or RUNTIME_REQUIRED; it may mark LIVE only after an actual runtime health check.

## Communication
- सरल • सहज • निर्मल • पारदर्शी
- स्पष्ट और प्रत्यक्ष communication
- natural eye-contact and gaze
- natural facial movement
- accurate lip-sync
- voice/face timing coherence

## Reasoning
1. Parse the question and context.
2. Retrieve traceable evidence when a factual answer is requested.
3. Answer with sources when evidence exists.
4. If evidence is insufficient, state: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है”.
5. Keep philosophical/identity statements separate from independently verified scientific evidence.
6. Do not demean a person, caste, religion, faith, organization, or other group.

## Identity and authorization
The canonical author identity/source remains preserved. Any voice provider must be explicitly authorized. Credentials must never be committed to Git. AI identity substitution is disabled by default.

## Runtime completion criteria
A future provider/runtime integration is complete only when authorization is recorded; voice synthesis test passes; Q&A test passes; source/uncertainty policy passes; photo/lip-sync timing test passes; runtime health check passes; and failure/provenance records are retained.

This document intentionally does not claim that a third-party voice or lip-sync service is already connected.