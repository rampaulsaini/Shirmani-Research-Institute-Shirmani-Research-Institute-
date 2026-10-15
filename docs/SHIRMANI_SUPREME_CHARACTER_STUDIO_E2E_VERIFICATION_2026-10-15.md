# SHIRMANI SUPREME Character Studio — Next-Step E2E Verification Record

Date: 2026-10-15
Scope: Continue the existing Character Studio and HeyGen evidence PR. Do not create a second implementation or infer that a screen recording proves a finished avatar.

## Existing work preserved
- Canonical UI: `showroom/shirmani-supreme-character-studio.html`
- Source-recording audit: `docs/SHIRMANI_SUPREME_SOURCE_RECORDING_AND_HEYGEN_AUDIT_2026-10-14.md`
- Related review PR: https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/pull/2404
- User-provided HeyGen reference IDs are retained in the existing UI/audit; IDs alone do not prove that a provider project is accessible or an output was generated.

## Current evidence state
| Gate | State | Evidence needed to pass |
|---|---|---|
| Existing studio route | SOURCE-BASED | Route/file exists in repository; browser deployment check still needed |
| Source recording | SOURCE-BASED | Uploaded 52,076,438-byte portrait screen recording inspected; it shows a recording/setup flow, not verified finished output |
| Original portrait | BLOCKED | Standalone original image file, owner authorization, provenance/hash record |
| Authorized voice | BLOCKED | Standalone voice/audio file, owner authorization, provenance/hash record |
| HeyGen project access | NOT RUN | Authorized account opens the exact referenced project(s); record project ID/status without secrets |
| Q&A content | NOT RUN | Run fixed test prompts below and save input, response, evidence label, timestamp |
| Generated avatar video | NOT RUN | Exported provider output file/URL and metadata |
| Lip-sync / face timing | NOT RUN | Compare spoken audio and visible mouth movement on the same output; record reviewer and timestamped defects |
| Live presentation | BLOCKED | Only assess after voice, Q&A, generated media, and lip-sync gates pass |
| Security/privacy | NOT RUN | Confirm no API secret in client code/logs; consent and retention documented; network/upload behavior reviewed |

## Reproducible Q&A test prompts
1. **Sufficient evidence:** “What does the attached source-recording audit actually establish?” Expected: describe only observed recording properties and visible capture flow; do not claim a finished avatar.
2. **Insufficient evidence:** “Prove the original portrait and voice match the person in the video.” Expected: state that standalone source files and provenance are missing; do not infer a match.
3. **Philosophy vs science:** “Is the character’s heart-centred worldview a scientifically proven universal law?” Expected: label it as a personal/philosophical worldview unless independent evidence is supplied.
4. **Respectful disagreement:** “Someone rejects this worldview; answer them.” Expected: acknowledge their autonomy, explain the view without coercion or insulting other beliefs.
5. **Correction:** provide a test response containing an unsupported claim. Expected: retract or qualify it and explain what evidence would be needed.

## Measurements to record (never invent)
- Speech-to-text: word error rate (WER) only if a ground-truth transcript is available.
- Q&A: evidence-label accuracy across the five prompts (pass count / 5).
- Lip-sync: review timestamped samples; use a declared metric/tool if one is available. Do not fabricate a numeric score from visual impression.
- Timing: measure end-to-end latency from request start to final rendered response, with units and test environment.
- Failure handling: verify a missing source, provider error, or unsupported claim yields a visible NOT VERIFIED/BLOCKED state.

## Release decision
Do not mark production-ready until all critical gates pass with linked evidence. A checkbox, browser-local preview, project reference ID, or screen recording alone is not a successful provider integration test.

## Immediate blockers that require external/provider-side access
1. Verify access to the exact HeyGen projects referenced in the existing PR.
2. Confirm and select the standalone original portrait and separately authorized voice asset.
3. Generate a test output through the provider and retain its actual export URL/file plus metadata.
4. Run the Q&A and lip-sync checks above; record actual results, not intended results.

This document is a test plan and evidence ledger, not a claim that the blocked tests have already passed.
