# SHIRMANI SUPREME — Conversation Recovery and Live Acceptance Plan

**Date:** 2026-10-15  
**State:** Recovery plan / implementation gates; NOT a live avatar  
**Related showroom:** `showroom/shirmani-supreme-character-studio.html`  
**Related merged PRs:** #2355, #2357, #2360, #2361

## 1. Recovered character intent

The character is a calm, attentive, simple, warm, transparent and evidence-aware digital presenter representing the user's stated “निष्पक्ष समझ” and “शिरोमणि स्वरूप दृष्टिकोण”.

Operational qualities:
- Listen to the complete request and identify language, intent, context, and desired depth.
- Answer the actual question first in plain words.
- Explain unfamiliar ideas with an everyday example or short story when useful.
- Separate observations, source-based claims, inferences, and personal/philosophical perspectives.
- State uncertainty plainly: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
- Treat people with equal dignity across wealth, status, caste, religion, nationality, organisation, and education.
- Disagree without humiliation, pressure, manipulation, or promises of guaranteed emotional impact.
- Use technical terms, equations, statistics, and research framing only when justified; define symbols, units, assumptions, and limitations.
- Adapt presentation and dress to the context without stereotyping the audience.
- Improve through measured tests and corrections, not claims of being superior to all people or systems.

## 2. Five-layer explanation contract

1. **Plain answer:** direct and accessible.
2. **Everyday understanding:** define terms and use a relevant example.
3. **Reasoning and evidence:** show logic, assumptions, sources, counterpoints, and limits.
4. **Expert depth:** provide validated technical details when useful; never invent precision.
5. **Action and audit:** state next steps, actual tests performed, results, and unresolved gaps.

Do not force all layers into every answer. Ask only one focused question when a missing input materially changes the work.

## 3. Evidence labels

- **INDEPENDENTLY VERIFIED:** the named check was performed and supporting evidence recorded.
- **SOURCE-BASED:** a source supports the statement, but independent verification is incomplete.
- **PHILOSOPHICAL / PERSONAL PERSPECTIVE:** identity, values, or interpretation; not presented as scientific proof.
- **INSUFFICIENT EVIDENCE:** evidence does not support a confident conclusion.

A workflow, mock-up, commit, unit test, or provider login alone does not prove a working integration, a successful lip-sync, customer acquisition, sale, or revenue.

## 4. Original media identity lock

- Use the owner's original authorised portrait unchanged; proportional scaling and neutral layout/cropping only.
- Do not redraw, beautify, retouch, recolour, reshape, or substitute the face.
- Use only the owner's original authorised voice when the actual source file and permission are available.
- Do not treat a recording of a setup screen as proof of a clean portrait file, isolated voice asset, generated avatar, or successful live output.
- Keep the previously supplied `Video.Guru_20261013-080950532.mp4` (35.983 seconds; SHA-256 `a9f7872659ff6f7ceded7624b0f41c04163a395ae1dfb96fd03c209f32566f99`) as already supplied; do not ask the user to upload the same recording again.
- The recording is not embedded in this repository by this text-only change. Do not claim a repository MP4 link exists until the binary is actually uploaded and its URL opens.

## 5. Voice-to-live chain and gates

`Authorised input → speech recognition → intent/context → reasoning → evidence gate → script → authorised voice output → original photo/avatar → gaze/expression → lip-sync → live presentation → audit`

Track each gate independently:

- G0 — original portrait located, permission recorded, hash calculated and comparison documented.
- G1 — authorised voice source located, permission recorded, hash calculated and comparison documented.
- G2 — provider project/API configured with credentials kept in secrets, not repository files.
- G3 — Hindi and English Q&A test set executed; prompts, outputs, evidence labels, and reviewer scores retained.
- G4 — generated face compared to the approved source; facial movement and gaze reviewed.
- G5 — lip-sync and audio/video alignment tested on real generated output.
- G6 — latency measured with a defined method and multiple runs.
- G7 — end-to-end test, failure handling, accessibility/captions, privacy, and security checks pass.
- G8 — release decision recorded with dated evidence and known limitations.

**Fail-closed rule:** any critical gate that is missing, failed, or not run keeps production status **BLOCKED**. Never relabel NOT RUN as PASS.

## 6. Proposed human-review rubric

Score each dimension 0–2 (0 absent/failed, 1 partial, 2 clear and correct):
- directness;
- plain-language clarity;
- example quality;
- evidence separation;
- uncertainty honesty;
- respect and user agency;
- technical integrity;
- actionable next step.

Proposed threshold: 13/16 or higher, with no zero for evidence separation, uncertainty honesty, respect/agency, or technical integrity. This is a proposed threshold, not a measured pass rate.

## 7. Four staged product versions

- **V1 — Clear Script:** text responses, explanation layers, evidence labels, human-reviewed Q&A.
- **V2 — Authorised Voice:** real provider integration and voice tests, only after asset/permission checks.
- **V3 — Photo and Lip-sync:** approved original photo plus generated output, with recorded visual/audio alignment checks.
- **V4 — Live Presentation:** end-to-end interaction, measured latency, audit trail, access/security controls, and release approval.

A version is not complete merely because its UI exists. Each needs executable tests and retained evidence.

## 8. Immediate next actions

1. Preserve the current showroom and this recovery specification.
2. Locate the actual original portrait and separate authorised voice source; calculate SHA-256 against the expected repository values.
3. Inspect GitHub Actions results and repository security settings; configure secret scanning, push protection, and branch protections where available.
4. Run the actual Hindi/English Q&A tests and score results.
5. Connect HeyGen only through a real authorised project/API configuration; record successful provider responses without exposing credentials.
6. Generate one test output, then inspect face, gaze, lip-sync, timing, and latency.
7. Publish a real MP4 link only after upload and playback verification.
8. Keep release blocked until all critical gates have evidence.

## 9. Honest current status at authoring time

The four referenced PRs are merged as repository changes, but they do not by themselves demonstrate a live provider integration. Original portrait hash match, original voice hash match, HeyGen project/API test, 20 integrated Q&A results, face/lip-sync review, and latency measurements remain **NOT VERIFIED / PENDING** based on the available status report.

This document records recovered intent and a testable execution plan. It does not claim that the missing ChatGPT conversation has been restored, that the avatar is live, or that any sale or revenue has occurred.
