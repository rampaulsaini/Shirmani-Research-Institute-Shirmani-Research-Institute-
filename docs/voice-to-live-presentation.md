# Voice → Voice System → Content → Photo/Lip-sync → Live Presentation

## Purpose

Define an auditable presentation pipeline for the public platform:

**Voice input → Voice System → Content → Photo/Lip-sync → Live Presentation**

The subsystem is an orchestration layer. It does not turn generated media into evidence, and it does not bypass the platform's independent-verification boundary.

## Pipeline

1. **Voice intake**
   - Capture an authorized voice request or live question.
   - Preserve request/session identifiers and language metadata.
   - Reject missing authorization or malformed media.

2. **Voice System**
   - Speech-to-text (when source is speech).
   - Language identification and normalization.
   - Intent/question extraction.
   - Optional response voice synthesis using an explicitly authorized voice profile.
   - Record voice provenance: source, authorization, model/runtime version, and timestamps.

3. **Content**
   - Retrieve relevant platform documents and sources.
   - Generate a bounded answer from the retrieved context.
   - Keep author statements, generated text, evidence, and verification state distinct.
   - If evidence is insufficient, produce an abstention/uncertainty state instead of inventing certainty.

4. **Photo / Lip-sync**
   - Select only an authorized presenter image/avatar.
   - Generate lip-sync timing from the approved response audio.
   - Preserve a media manifest linking presenter asset, audio asset, and generation runtime.
   - Never imply that a synthetic presenter is the original speaker unless that identity claim is separately established.

5. **Live presentation subsystem**
   - Stream or publish the assembled audio + presenter output.
   - Expose captions/transcript and source/evidence links where applicable.
   - Track runtime health, latency, dropped frames, and presentation state.
   - Fail closed to text/audio-only presentation when visual generation is unavailable or unsafe.

## State machine

`RECEIVED → TRANSCRIBED → CONTENT_READY → VOICE_READY → VISUAL_READY → LIVE`

Failure/uncertainty states:

- `REJECTED`
- `ABSTAINED`
- `UNVERIFIED`
- `DEGRADED`

A workflow success signal must not change `UNVERIFIED` to `VERIFIED`.

## Evidence and provenance contract

Every answer that presents research/evidence should carry:

- request/session ID
- content/answer ID
- source references
- evidence state
- verification state
- voice authorization reference
- presenter asset reference
- audio generation reference
- visual generation reference
- runtime/version metadata

The media layer is a delivery mechanism. It is not independent scientific verification.

## Safety and integrity gates

- **Voice authorization:** no unapproved voice cloning.
- **Presenter authorization:** no unapproved face/avatar use.
- **Content grounding:** source-backed answers where evidence is expected.
- **Abstention:** insufficient or conflicting evidence must remain explicit.
- **Independent verification:** only an independent review record can establish VERIFIED.
- **Human control:** high-impact or disputed outputs remain reviewable.
- **Degraded mode:** if lip-sync fails, continue with safe text/audio presentation where policy permits.

## Implementation status

| Layer | Status |
|---|---|
| Architecture contract | BUILT |
| Event/provenance schema | BUILT |
| Runtime STT/TTS integration | PLANNED |
| Source-grounded content adapter | PLANNED / integrates existing platform controls |
| Authorized photo/lip-sync runtime | PLANNED |
| Live streaming/presentation runtime | PLANNED |
| End-to-end integration tests | PLANNED |
| Production LIVE declaration | NOT ESTABLISHED |

This document deliberately distinguishes architecture from deployment and operational proof.
