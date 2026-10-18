# Voice-to-Live: measurable acceptance and release plan

**Project:** Shirmani Research Institute  
**Workflow:** Voice → Voice System → Content/Dialogue → Authorized Portrait/Avatar → Rendered Video → Lip-sync/Audio QC → Live Q&A → Release Review  
**Status at creation:** Design/acceptance specification; provider-side end-to-end verification is not established by this document.

## Existing user-provided reference — do not request it again

- HeyGen reference already supplied by the user: https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7
- Keep this reference attached to the project and link it from the relevant console.
- Do not ask the user to re-send the same photo or video. A URL is a reference, not proof that the provider job, original portrait file, voice authorization, generated output, lip-sync, or live session has passed.
- Do not claim to possess a separate original portrait/audio file unless it is actually accessible in the repository or connected provider.

## Acceptance gates

| ID | Gate | Minimum evidence to mark VERIFIED | Failure / fallback |
|---|---|---|---|
| VTL-01 | Source voice & authorization | Accessible source asset or provider asset ID; permission/source note; reviewer | BLOCKED if the asset or authorization cannot be inspected |
| VTL-02 | Voice system output | Actual generated audio; job/run ID; transcript; pronunciation and voice-match review | Keep output quarantined; correct settings and rerun |
| VTL-03 | Content/dialogue | Prompt, response, language, source references and uncertainty labels; scripted test cases | Reject unsupported factual claims; revise and rerun |
| VTL-04 | Portrait/avatar fidelity | Provider asset/job ID and rendered sample reviewed against the authorized reference | Do not publish altered or mismatched identity output |
| VTL-05 | Rendered video | Playable final video/audio; provider job ID; duration/resolution; playback result | Retry provider job; preserve error and run ID |
| VTL-06 | Lip-sync/audio QC | Timestamped sample review; synchronization defects; clipping/noise/pronunciation notes; reviewer | Mark FAILED or BLOCKED; never infer lip-sync from a still image |
| VTL-07 | Live Q&A | Real session record, test questions, response transcript, latency, errors and fallback behavior | Keep live capability marked NOT TESTED until a real session is reviewed |
| VTL-08 | Release review | All required gates reviewed; privacy/consent check; named reviewer; release decision and timestamp | No public production claim until the release reviewer signs off |

Every gate must retain: `status`, `test_cycle_id`, `evidence_reference`, `reviewer`, `tested_at`, `result`, `limitations`, and `next_action`. Use the statuses `NOT TESTED`, `IN PROGRESS`, `BLOCKED`, `FAILED`, and `VERIFIED`. A stage counts as verified only if status is VERIFIED and evidence reference, cycle ID, and reviewer are non-empty. An entered URL alone is not verification.

## Honest counters

- **Verified-gate coverage** = number of VERIFIED gates with complete evidence ÷ 8 × 100.
- **Test cycles** = distinct non-empty test-cycle IDs recorded; this is not a count of automated runs unless a runner actually executed them.
- **Pass rate** = passed test cases ÷ all completed test cases × 100; show “N/A” when no tests have completed.
- **Evidence completeness** = records with all required fields ÷ all gate records × 100.
- **Production uptime** requires timestamped server/provider health checks over a stated window. A browser-local counter cannot prove 24/7 uptime.
- Never use arbitrary “quality”, “truth”, IQ, heart-view, or scientific-certainty percentages. Subjective ratings must be labelled as reviewer ratings with a defined rubric.

## Minimum end-to-end test set

1. **Voice source:** verify the source and permission without exposing private assets publicly.
2. **Voice output:** generate a short approved test phrase; save output reference and transcript; review pronunciation and audio quality.
3. **Dialogue:** run at least one simple factual question, one ambiguous question, and one question whose answer is unknown; confirm uncertainty is stated rather than invented.
4. **Portrait/render:** generate a short sample with the authorized portrait/avatar and inspect the actual rendered file.
5. **Lip-sync:** inspect several timestamps across the clip, including pauses and plosive sounds; record defects and reviewer.
6. **Live Q&A:** conduct a real session with at least three prepared questions; capture transcript, latency, failure/fallback and session reference.
7. **Release:** a reviewer other than the test operator checks the evidence and records PASS, FAIL, or BLOCKED.

These are acceptance targets, not claims that any provider tests have already run.

## Automation and security boundaries

- The browser-local evidence console is a manual register unless a verified backend/provider integration is implemented. Do not label localStorage records as cloud-synced, live telemetry, or 24/7 monitoring.
- Keep API keys and provider credentials server-side in managed secrets. Never commit secrets to this repository or expose them in browser JavaScript.
- Use least-privilege credentials, consent/authorization checks, rate limits, audit logs, retention controls, and a human release gate.
- Retry only transient failures with bounded exponential backoff; record each attempt and stop repeated failing cycles rather than looping indefinitely.
- Do not delete filters, failed runs, or inconvenient evidence to improve counters. Preserve status history and link the corrective run.
- Do not send outreach or claim a sale, revenue, integration, or production readiness unless the action/result is actually evidenced.

## Next implementation sequence

1. Keep the existing console and supplied HeyGen reference as the single operator path.
2. Add the eighth release-review gate and validate all counters with empty, partial, failed, and complete test fixtures.
3. Connect provider jobs only after credentials and API capabilities are verified; store secrets server-side.
4. Add durable server-side audit storage and role-based access before multi-device/team use.
5. Run the test set above, record evidence, and only then publish provider integration status.

## Definition of done

The feature is done when an operator can follow one linked path from source authorization through a real rendered video and real live Q&A, record evidence at each gate, export an audit report, and see truthful coverage/pass/failure counters. Until those conditions are met, the UI must show the unverified stages as NOT TESTED, IN PROGRESS, or BLOCKED—not as completed.
