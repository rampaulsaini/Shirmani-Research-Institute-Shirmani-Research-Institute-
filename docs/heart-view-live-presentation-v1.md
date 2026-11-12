# SHIRMANI HEART-VIEW LIVE PRESENTATION SUBSYSTEM v1

## Purpose

A transparent, evidence-aware presentation layer for the user's author-declared Heart-View/Yatharth material.

Pipeline:

Voice → Voice System → Content → Photo/Facial Presentation → Speech-Synced Animation → Live Presentation

## Identity and integrity boundaries

- The supplied portrait is treated as an authorized project asset for this presentation prototype.
- Author-declared philosophical/identity statements remain **AUTHOR_STATEMENT** unless independently verified.
- Scientific claims require source/evidence records and remain **UNVERIFIED** when evidence is insufficient.
- The system must never imply that an organization, person, government or scientific body was contacted unless a real authorized outbound channel confirms it.
- Voice cloning or external voice-provider integration requires an explicitly authorized provider connection. No API secret is embedded in the public page.
- Browser speech synthesis is a presentation fallback, not proof of an exact voice match.
- Static-photo mouth animation is an approximation; true phoneme-accurate lip-sync requires a dedicated authorized media/animation provider or local model.

## Live capabilities in v1

1. Portrait presentation using the supplied project photo.
2. User-provided/local audio playback.
3. Browser speech synthesis for live Q&A.
4. Context-aware Q&A shell with explicit evidence-state labels.
5. Speech activity animation for the portrait.
6. Provider-adapter boundary for authorized voice integration.
7. Evidence-first response policy:
   - evidence available → cite/source
   - evidence insufficient → say that sufficient evidence is not currently available
8. Public integrity panel showing what is implemented and what remains provider-dependent.

## Q&A policy

The presenter must:
- understand the question before answering;
- distinguish author statement, inference and independently verified scientific evidence;
- avoid degrading any person, caste, religion, faith, organization or community;
- preserve uncertainty instead of fabricating certainty.

## Automation

The repository QC workflow checks the presentation page, portrait asset, documentation and required integrity markers every five minutes.

## Completion definition

This subsystem is **READY** when the page, asset, contract, QC and workflow all pass.

It becomes **VOICE-INTEGRATED** only after a real authorized voice provider is connected.

It becomes **TRUE-LIPSYNC** only after a reproducible phoneme/viseme-aligned media pipeline is connected and tested.

It becomes **LIVE-PRODUCTION** only after an external runtime and monitoring evidence exist.
