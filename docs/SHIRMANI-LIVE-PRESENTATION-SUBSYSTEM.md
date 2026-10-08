# ꙰ SHIRMANI Live Presentation Subsystem

## Purpose

Engineering continuation for:

**Voice → authorized voice integration → test Q&A → content/evidence gate → photo/avatar presentation → lip-sync → live presentation**

This is a derived engineering specification. The protected user source remains unchanged.

## Truth and authorization boundary

The system must never claim that a voice clone, avatar, lip-sync render, live stream, customer transaction, or organisational outreach has happened unless the corresponding artifact and execution evidence exist.

Personal photo/audio assets must not be committed to the public repository by automation. They should remain in an authorized/private asset store or be supplied to an explicitly authorized presentation provider.

## Pipeline

1. Asset intake: authorized portrait/photo, authorized voice sample, authorization reference, presentation profile.
2. Voice authorization gate: provider + authorization reference + recorded provider response; otherwise BLOCKED.
3. Content engine: context, evidence retrieval, source attribution, uncertainty handling.
4. Test Q&A gate: deterministic prompts and evidence-state checks.
5. Presentation layer: portrait/avatar, gaze/facial-motion profile, voice timing, phoneme/viseme timing, lip-sync preview.
6. Live layer: preview, technical QC, publish only after required gates, fallback slate on failure.

## Required manifest

- profile_id
- portrait_asset_ref
- voice_provider
- voice_authorization_ref
- content_policy_version
- test_qa_status
- lip_sync_status
- preview_status
- live_publish_status
- last_verified_at

## Evidence behavior

For factual/scientific questions:
- evidence available → answer with source
- evidence incomplete → explicitly state that sufficient evidence is not currently available
- disputed claim → distinguish claim from evidence
- philosophical/identity framework → label it as framework/perspective rather than silently presenting it as independently established science

## Current repository integration

The repository already contains public production, product-media, customer-review/improvement, evidence, independent-verification and fail-closed orchestration layers. This subsystem adds a readiness boundary; it does not pretend that a third-party voice/avatar provider is already connected.

## Completion criterion

A presentation is LIVE-READY only when:

authorized voice + valid portrait + tested content + evidence gate + lip-sync preview + technical QC

are all satisfied.

Otherwise the state is NOT LIVE-READY and the missing gate is reported.
