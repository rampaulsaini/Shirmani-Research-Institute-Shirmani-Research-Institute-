# SHIRMANI SUPREME — Live Readiness Implementation Plan (V1)

**Status:** implementation plan / acceptance contract. Not a claim that HeyGen, voice cloning, lip-sync, or live streaming is connected.

## Purpose

Build a character experience that is simple, calm, respectful, transparent, context-aware, and evidence-first. “Supreme” is measured through observable quality, not superlative claims.

## Character behavior contract

1. Listen to the actual request; restate it briefly when that reduces ambiguity.
2. Match the user's language and level of familiarity. Explain in plain language first, then add examples, reasoning, and specialist detail as useful.
3. Separate **VERIFIED**, **SOURCE-BASED**, **PHILOSOPHICAL / PERSONAL PERSPECTIVE**, and **INSUFFICIENT EVIDENCE**.
4. When evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” Do not fabricate sources, scientific results, equations, sales, income, or provider status.
5. Respect every person's dignity regardless of wealth, caste, religion, community, institution, or disagreement. Challenge claims rather than demean people.
6. Be warm without flattery, manipulation, false certainty, or encouraging emotional dependency. Invite independent judgement.
7. Correct errors openly; ask one focused question if a missing detail prevents a safe or accurate result.
8. For high-impact, ambiguous, or public-facing outputs, provide a human-review / stop path.

## End-to-end architecture

`Input voice/text → speech recognition (if voice) → language/context understanding → response planning → evidence gate → answer/script → authorized voice output → authorized portrait/avatar render → lip-sync/timing QA → live delivery → audit and feedback`

Each stage exposes a state: `NOT_CONFIGURED`, `READY_FOR_TEST`, `PASS`, `FAIL`, or `BLOCKED`. A stage may be marked `PASS` only when a timestamped reproducible test artifact exists. UI presence or a workflow run is not evidence of functional integration.

## Four staged versions

- **V1 — Character & evidence:** working accessible showroom, multilingual answer rubric, evidence labels, test fixtures, privacy notice, and local demo clearly labeled as a prototype.
- **V2 — Authorized voice:** confirm ownership/consent, verify exact original audio hash, integrate provider via server-side secrets, run Hindi/English speech and Q&A tests, record provider response IDs without exposing credentials.
- **V3 — Face & lip-sync:** verify the exact original portrait hash; permit proportional layout scaling only for the displayed original; generate a provider sample; review identity consistency, gaze, facial motion, pronunciation, and lip-sync against the audio.
- **V4 — Live & audited:** controlled live test, measured latency and audio/video offset, monitoring, failure fallback, human stop control, retention limits, and explicit public-release review.

## Acceptance test matrix

Store one result per case with: test ID, language, input, expected behavior, actual output, evidence state, pass/fail, timestamp, reviewer, and artifact link.

| ID | Test | Pass condition |
|---|---|---|
| CHAR-01 | Simple Hindi explanation | Clear answer in everyday Hindi; no unsupported claims |
| CHAR-02 | English explanation | Meaning preserved; readable, respectful English |
| CHAR-03 | Complex topic | Plain-language summary first; assumptions and limits are stated |
| EVID-01 | Source-backed factual question | Source is linked and claim matches source |
| EVID-02 | Missing evidence | Explicitly says “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” |
| EVID-03 | Personal philosophy | Clearly labelled as a perspective, not scientific proof |
| FAIR-01 | Disagreement / identity-sensitive context | Respectful, no stereotyping or personal attack |
| VOICE-01 | Authorized voice | Consent record, exact asset hash, provider test artifact available |
| FACE-01 | Original portrait | Exact hash match; no retouching or face alteration |
| SYNC-01 | Lip-sync | Human-reviewed sample plus measured audio/video offset |
| LIVE-01 | End-to-end live | Actual session artifact, latency measurements, stop/fallback tested |
| SEC-01 | Secret handling | No API keys or provider identifiers exposed in client code/public logs |
| PRIV-01 | Data minimization | Explicit notice, minimal logs, documented retention/deletion path |

## Release gates

- **Gate A — Assets:** original portrait and authorized voice files actually available; compute SHA-256 from the exact files; compare against expected hashes. A hash written in documentation is not a match.
- **Gate B — Provider:** actual HeyGen project/account integration test and output captured. Provider IDs alone do not prove success. Keep credentials server-side.
- **Gate C — Q&A:** run at least 20 Hindi/English prompts including ambiguity, source quality, unsupported premise, disagreement, and insufficient evidence. Preserve outputs.
- **Gate D — Presentation:** inspect real generated media for portrait integrity, gaze, facial movement, pronunciation, lip-sync and timing. Record measurements; do not invent thresholds after observing results.
- **Gate E — Live & security:** run a controlled session, test stop/fallback, check logs/secrets, and document reviewer sign-off.
- **Release decision:** any missing critical gate means `BLOCKED / NOT VERIFIED`; do not describe the character as live or production-ready.

## Media handling

The supplied `Video.Guru_20261013-080950532.mp4` is a 35.983-second, 888×1920 H.264/AAC reference recording. Reported SHA-256: `a9f7872659ff6f7ceded7624b0f41c04163a395ae1dfb96fd03c209f32566f99`. It is a reference screen recording, not proof of a generated avatar or a verified provider integration. Do not claim the binary is hosted in the repository unless the exact public asset URL is confirmed. Do not publish private provider identifiers or secrets.

## Immediate next actions

1. Locate the exact original portrait and separate authorized voice file in approved storage; do not ask for the existing MP4 again.
2. Hash the actual files locally and compare with repository manifests.
3. Run existing repository tests and inspect the results, including the product-media integrity gate.
4. Complete a real HeyGen test using authorized assets and save provider output plus review notes.
5. Run the Q&A matrix and presentation timing checks.
6. Update the release scorecard only with reproducible evidence.

## Honest current boundary

The showroom currently contains a browser-local response-outline demo. It does not itself call an AI model, connect HeyGen, send email, clone a voice, create an avatar, or stream live. This document defines what must be implemented and proven next; it does not mark any of those capabilities as complete.
