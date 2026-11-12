# SHIRMANI Presentation System — Production Truth Gate

**Status date:** 2026-10-16  
**Scope:** HeyGen voice, avatar, lip-sync, and live-presentation acceptance  
**Status:** PARTIAL / NOT PRODUCTION-VERIFIED

## Evidence observed

- `voice-to-presentation-studio.html` describes itself as a browser demo and explicitly states hosted AI, authorized external voice, facial animation, real lip-sync, persistent storage, payments, and real-time streaming are not connected.
- The supplied avatar group ID `cc49ee728c9b4877b60a13365f4fffd5` returned `avatar_not_found` in the connected HeyGen workspace.
- The supplied video IDs `5d938b91bb6841e9a9ddd93948c781b7` and `ba0ae3fdeb7f40afae0a3a3760b2a3ad` returned `video_not_found` in the connected HeyGen workspace. This does not prove that the assets do not exist in another workspace; account/workspace access must be checked in HeyGen.
- The supplied URLs/IDs therefore do not currently prove an end-to-end production run.

## Measurable acceptance chain

| Gate | Test | Required pass evidence | Current status |
|---|---|---|---|
| G0 — Access | Confirm the correct HeyGen workspace and asset ownership | Provider lookup succeeds for the intended avatar/video | BLOCKED |
| G1 — Voice | Generate short Hindi and English samples using an authorized voice | Provider job ID, completed status, playable output, authorization/consent record | NOT VERIFIED |
| G2 — Q&A | Run 10 fixed Hindi/English questions | 10/10 inputs and outputs recorded; claims sourced or uncertainty stated | NOT VERIFIED |
| G3 — Face/avatar | Resolve the authorized avatar/look and generate a short test | Correct avatar/look ID and successful provider status | BLOCKED |
| G4 — Lip-sync | Render a 30–60 second sample against approved audio | Completed job, playable output, human review of timing/artifacts | NOT VERIFIED |
| G5 — Live presentation | Run a 5-minute session with at least 10 questions | Session log, latency, error rate, reconnect test, human stop control | NOT VERIFIED |
| G6 — Security/privacy | Check consent, secret handling, rate limits, logs, retention, access control | Automated checks plus documented manual review | NOT VERIFIED |
| G7 — Deployment | Verify deployed build and public route after publishing | Deployment URL, commit SHA, successful health check, smoke-test report | NOT VERIFIED |

## Release gate

Do not label this feature “production ready”, “live”, “verified”, or “end-to-end complete” until all required gates pass with reproducible evidence. A local browser speech demo is not proof of provider voice cloning, avatar animation, lip-sync, or live Q&A.

## Immediate next actions

1. Sign in to the intended HeyGen workspace and confirm the existing avatar and video assets are visible there.
2. Re-run provider lookups using IDs copied directly from that workspace; do not create duplicate avatars to work around a lookup failure.
3. Verify voice authorization/consent and use a short non-sensitive test script first.
4. Run each gate independently and save job IDs, statuses, output links, and reviewer pass/fail.
5. Verify the actual deployed URL and production JSON/status endpoint separately; a repository file or intended workflow is not evidence of deployment.
6. Keep unsupported claims and personal/philosophical viewpoints labeled appropriately; do not represent them as independently verified scientific claims without evidence.

## Test record template

- Run ID:
- Commit SHA:
- Deployment URL:
- HeyGen workspace confirmed by owner: YES / NO
- Avatar/look ID:
- Voice ID and authorization/consent evidence:
- Q&A cases passed / total:
- Lip-sync job ID and output:
- Live-session duration / questions / median and p95 latency:
- Security checks passed / total:
- Reviewer:
- Final status: PASS / FAIL / BLOCKED

No revenue, customer, deployment, or production success is claimed by this document.
