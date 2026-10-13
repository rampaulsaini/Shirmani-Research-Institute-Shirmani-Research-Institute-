# ꙰ SHIRMANI SUPREME Human-Presentation System

**Status:** Specification / implementation contract. This document does not by itself prove that live voice, avatar, lip-sync, or provider integrations are deployed.

## Approved identity and presentation contract

- Preserve the supplied original portrait unchanged; allow only proportional resizing/cropping needed for layout. Do not synthesize a replacement face.
- Use the supplied voice recording only with the owner's authorization and through a provider integration that passes an explicit test. Do not describe the voice integration as active until verified.
- Present the identity phrase and philosophy as the owner's self-description and worldview, not as independently established scientific facts.
- Aim for simple, calm, respectful, context-aware communication. Do not claim that every audience will respond identically or that any system can guarantee a permanent emotional effect.
- Respect people equally regardless of wealth, status, caste, religion, community, or organization.

## Measurable pipeline

`VOICE INPUT → AUTHORIZATION → STT → CONTEXT / INTENT → SOURCE CHECK → REASONING → RESPONSE → TTS → PORTRAIT / AVATAR → LIP-SYNC → PRESENTATION → AUDIT`

Each stage must emit a timestamped status, version, and failure reason. Never mark the whole chain verified just because a workflow started or completed.

## Evidence labels

- **VERIFIED** — the stated claim passed a documented check with an inspectable result.
- **SOURCE-BASED** — supported by a named source, but not independently reproduced by this system.
- **PHILOSOPHICAL / IDENTITY** — personal philosophy, self-description, or interpretation.
- **INSUFFICIENT EVIDENCE** — use the exact response: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

Scientific, commercial, security, and performance claims require appropriate evidence. Philosophical statements must not be silently re-labelled as scientific findings.

## Required acceptance gates

| Gate | Passing evidence |
|---|---|
| Portrait integrity | Input/output comparison confirms original facial content was not altered beyond approved crop/scale |
| Voice authorization | Provider, consent/authorization status, configured voice ID, and test result are recorded; secrets are not logged |
| Speech recognition | Test set with reference transcripts and measured word/error rate |
| Context and Q&A | Versioned test cases with expected answer criteria and recorded outcomes |
| Source/evidence gate | Source URL or evidence record for factual claims; insufficient-evidence test passes |
| Voice output | Authorized voice produces a test clip and playback is reviewed |
| Face / gaze / expression | Actual rendered output reviewed against a documented checklist |
| Lip-sync | Audio/video sample evaluated; measured offset is recorded against a defined tolerance |
| End-to-end latency | Repeated runs report median and p95 latency |
| Safety and respect | Regression cases cover respectful language, uncertainty, privacy, and non-discrimination |
| Auditability | Run ID links input reference, model/provider versions, evidence status, output, metrics, and failures |

A critical gate failure blocks a **VERIFIED / production-ready** label. Record partial readiness honestly.

## Implementation boundaries

1. Store API keys and provider credentials only in GitHub Actions secrets or an appropriate secret manager. Never commit keys, access tokens, voice IDs that are private, or personal recordings into public source control.
2. The uploaded portrait and MP3 must be deliberately placed in an access-controlled asset location before the website references them. This specification does not upload those local files.
3. A provider such as HeyGen must be integrated through its supported API or approved workflow. A login session or pasted identifier alone is not proof of API access, authorization, or successful generation.
4. Generated MP4 links must point to an actual committed or hosted video asset and be checked for reachability. Never fabricate a video URL or label a placeholder as a real video.
5. Public demos should show the actual capability, limitations, version, last test result, and a clear way to report a defect.

## Production record template

- Run ID:
- Commit / version:
- Provider and model versions:
- Portrait asset reference:
- Authorized voice reference (no secret values):
- Test Q&A set:
- Evidence state:
- Lip-sync offset:
- Median / p95 latency:
- Passed / failed gates:
- Logs / demo URL:
- Reviewer and timestamp:

## Next implementation sequence

1. Inspect the existing character-profile PR and avoid duplicating its work.
2. Connect the authorized provider using repository secrets.
3. Add reproducible Q&A, evidence, portrait-integrity, and lip-sync tests.
4. Generate one short real demo, inspect it, and publish its verified URL.
5. Expose the feature on the public showroom only after required gates pass.

**Truth gate:** “workflow completed” is not equivalent to “feature verified.” No sales, revenue, security, scale, or live-operation claim is valid without its own evidence.
