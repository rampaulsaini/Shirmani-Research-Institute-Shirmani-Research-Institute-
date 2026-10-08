# Voice → Voice System → Content → Photo/Lip-sync → Live Presentation Subsystem v1

## Purpose

This subsystem defines a production-safe path from a voice input/output signal to a publishable live presentation:

Voice → Voice System → Content → Photo/Lip-sync → Live Presentation

It is a routing and evidence contract, not a claim that a third-party voice, avatar, lip-sync or live-stream provider is already connected.

## Pipeline

1. Voice
   - input: microphone/uploaded audio or an approved voice source
   - output: normalized audio asset + duration + codec metadata
   - required provenance: source reference, consent/authorization state, timestamp

2. Voice System
   - speech-to-text (optional)
   - text-to-speech (optional)
   - voice transformation/cleanup (optional)
   - output: transcript and/or synthesized speech
   - quality gates: intelligibility, clipping, duration, language/locale, authorization

3. Content
   - source material is converted into a presentation script
   - factual claims can retain source/provenance references
   - generated copy is explicitly marked generated
   - output: versioned script + content manifest

4. Photo / Lip-sync
   - approved photo or avatar reference
   - lip-sync/animation is an optional presentation transform
   - identity substitution is disabled by default
   - output: rendered presentation asset with renderer/model/provider metadata

5. Live Presentation
   - preview → QC → human approval → publish/live
   - live state is distinct from generated/rendered state
   - a successful workflow run never by itself means that a presentation is truthful, independently verified, or safe for public release

## State model

REGISTERED → PREPARED → RENDERED → QC_PASS → HUMAN_APPROVED → LIVE

Fail-closed states:

- ABSTAINED
- QC_FAIL
- UNAUTHORIZED
- PROVENANCE_MISSING
- IDENTITY_REVIEW_REQUIRED
- LIVE_UNAVAILABLE

No state transition may convert UNVERIFIED into VERIFIED merely because media generation, lip-sync, or live publication succeeded.

## Minimum artifact contract

Each presentation packet should carry:

- packet_id
- voice_asset_id
- content_asset_id
- visual_asset_id
- renderer
- renderer_version
- language
- consent_status
- provenance
- qc
- verification_state
- publication_state
- created_at

## Identity and safety boundary

A photo/avatar may be used only when the project has an explicit authorization/consent record appropriate to that use. The subsystem must not silently replace a real person's identity with an AI-generated identity, nor imply that lip-sync accuracy proves identity authenticity.

## Live release gates

Before LIVE, the packet must satisfy:

- required assets exist and are addressable
- provenance is present
- authorization/consent is present where applicable
- content QC passes
- audio/video synchronization checks pass
- no unresolved critical safety flag exists
- human approval is recorded for public presentation
- rollback/unpublish route is known

## Evidence boundary

This subsystem can prove that a media pipeline executed and that specified QC checks passed. It cannot, by itself, prove the truth of the spoken content, the identity of a person, or independent scientific verification of any claim.

## Initial implementation strategy

Start with deterministic manifests and adapters:

voice asset → transcript/script → visual reference → render job → QC record → approval record → live route

Provider-specific integrations should be isolated behind adapters so that the public contract remains stable.

## Next engineering targets

- schema validation tests
- deterministic packet IDs
- media metadata/provenance records
- adapter interface for STT/TTS and lip-sync providers
- synchronization QC
- human approval/rollback records
- public live-status dashboard
