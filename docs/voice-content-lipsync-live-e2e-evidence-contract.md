# SHIRMANI Voice → Content → Lip-sync → Live: End-to-End Evidence Contract

**Status:** specification proposed; production execution is not implied.  
**Owner:** Shirmani Research Institute  
**Reference presentation supplied by the owner:** https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7

## Purpose

Provide one traceable path from the approved voice and presentation assets to a user-visible live response. Do not repeatedly request assets already supplied by the owner. First inspect repository records and the supplied reference URL; if the actual source file or provider permission cannot be accessed from the connected environment, record that specific limitation without claiming the asset is absent everywhere.

This contract deliberately separates a working local prototype from a real external-provider integration.

## The measurable chain

| Stage | Input | Required output/evidence | Pass condition |
|---|---|---|---|
| 1. Asset provenance | Owner-supplied photo, voice, and reference video | Asset ID, source/location, SHA-256 when bytes are accessible, consent/usage record | Source and permitted use are traceable; never substitute a generated face for an identity-locked original |
| 2. Voice system | Approved voice asset or authorized voice-provider voice ID | Provider, model/voice ID, request ID, audio artifact, duration, language, timestamp | A real audio artifact is retrieved and played; browser speech synthesis is labelled synthetic and is not a voice-clone pass |
| 3. Content | User prompt, language, context, factual sources | Prompt/input record, response text, citations/evidence labels, output hash | Response is saved and linked to its input; unsupported factual claims remain unverified |
| 4. Photo/avatar and lip-sync | Approved portrait/avatar plus generated audio and script | Provider job ID, rendered video, media metadata, audio/video duration, frame/sample review | Rendered output exists and is inspectable; timing is measured from the actual output, not inferred from a UI toggle |
| 5. Live presentation | Rendered or provider-streamed presentation | Session ID, connection events, start/end times, error log, recording or auditable event trace | A real session starts and delivers the expected media to a test client |
| 6. Dialogue / Q&A | Test questions in Hindi and English | Question/answer pair, response latency, source/evidence state, error/fallback | Questions receive context-relevant responses; unsafe, unsupported, and provider-failure cases fall back safely |
| 7. Independent verification | Evidence bundle from stages 1–6 | Reviewer, test version, result, counter-evidence, timestamp | A reviewer can reproduce the result; workflow success alone never means independently verified |

## Evidence states

Use only these values for each stage:

- `NOT_STARTED` — no run has been recorded.
- `BLOCKED` — a named prerequisite is missing or inaccessible.
- `RUNNING` — a real execution has begun and has not finished.
- `FAILED` — a test ran and did not meet its acceptance condition.
- `PASSED` — the stage's concrete acceptance test passed with attached evidence.
- `INDEPENDENTLY_VERIFIED` — a separate reviewer reproduced the result and reviewed counter-evidence.

A URL, screenshot, mock screen, code presence, checkbox, provider dashboard label, or successful workflow run is not by itself proof of generated audio, finished video, lip-sync quality, live dialogue, or independent verification.

## Required counters

Counters must be calculated from recorded evidence, never typed as aspirational values.

- **Cycle count** = number of distinct cycle IDs with a persisted start record.
- **Completed cycles** = cycle IDs with a persisted terminal result.
- **Stage pass rate** = passed eligible stage-runs / all completed eligible stage-runs × 100.
- **End-to-end pass rate** = end-to-end runs passing every mandatory stage / completed end-to-end runs × 100.
- **Independent verification rate** = independently verified runs / completed end-to-end runs × 100.
- **Provider success rate** = successful provider requests / all provider requests with terminal outcomes × 100.
- **Median / p95 latency** = statistics over measured request-to-response durations; disclose sample size and time window.
- **Asset integrity rate** = assets with a matched source record and reproducible hash / assets requiring integrity checks × 100.
- **Sales, customers, income, and dispatch** remain separate counters and are zero until transaction evidence exists.

When the denominator is zero, display **N/A — no measured runs**, not 0%, 100%, or a fabricated precision such as 99.9999%. Every displayed percentage must include its numerator, denominator, time window, and source artifact.

## Minimum reproducible test suite

1. Hindi normal prompt → content → authorized voice → rendered presentation → audible output.
2. English normal prompt → content → authorized voice → rendered presentation → audible output.
3. Short and long utterances; measure audio/video duration and visible mouth-motion alignment on sampled frames.
4. Question requiring evidence → answer includes sources or explicitly says evidence is insufficient.
5. Respectful disagreement → response addresses the claim, not the person's worth.
6. Provider timeout/rate limit → bounded retry, visible failure state, no false success.
7. Missing or invalid asset → fail closed; do not silently substitute another face or voice.
8. Live Q&A disconnect → safe fallback and recorded reconnect/error result.
9. Repeat the same test with a new run ID; preserve earlier evidence rather than overwriting it.
10. Independent reviewer follows the evidence bundle from input to output and records any disagreement.

For each test, persist: `run_id`, UTC timestamp, build/commit SHA, environment, test case ID, input hash, output artifact references, provider request IDs, measured latency, stage states, errors, reviewer, and evidence hashes. Never put API keys, tokens, private contact data, or raw secrets in logs or public artifacts.

## Security and operational guardrails

- Provider credentials stay in server-side secrets; never embed them in public HTML or repository files.
- Restrict upload and provider actions to authorized users; validate file type and size, rate-limit requests, and avoid logging raw personal media.
- Keep a deletion/retention policy for media and derived artifacts.
- Use only authorized portrait and voice assets and provider features; do not bypass provider safeguards.
- Scheduled automission may prepare reports and run bounded checks, but must not automatically publish a claim as verified or silently alter protected production code.
- A failure in one subsystem must not erase existing work or evidence from another subsystem.

## Public dashboard requirements

The public interface should show a simple ordered progress rail:

**Voice asset → Voice system → Content → Photo/avatar + lip-sync → Live presentation → Q&A → Independent verification**

Each card shows: current evidence state, latest real run time, measured pass rate (or N/A), run count, one-line blocker, and a link to its evidence record. Put technical details behind “View evidence” so the main public page stays readable. Do not show an unmeasured 24/7/365 uptime claim; report observed uptime only when monitoring data exists.

## Release gate

The chain is **not production-ready** until a complete Hindi and English run passes, a provider-backed video/audio artifact is inspectable, lip-sync and latency are measured, live Q&A is tested, failure cases pass, and an independent reviewer signs the evidence bundle. Keep each unpassed stage visibly blocked while allowing unrelated production work to continue.

## Current recorded state at specification time

- Owner-provided HeyGen reference URL: recorded above.
- Provider-backed audio generation: **NOT VERIFIED by this specification**.
- Finished avatar render and lip-sync: **NOT VERIFIED by this specification**.
- Live presentation and dialogue: **NOT VERIFIED by this specification**.
- Independent end-to-end test: **NOT VERIFIED by this specification**.

This is an implementation contract and reviewable next step, not a claim that external provider execution occurred in this commit.
