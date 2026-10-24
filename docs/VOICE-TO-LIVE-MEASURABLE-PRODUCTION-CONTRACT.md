# Voice-to-Live: measurable production contract

**Status:** specification / implementation contract. This document is not evidence that a provider integration, media render, live session, sale, or 24/7 monitor is already working.

**Existing operator surface:** [Voice-to-Live Evidence Console](../showroom/voice-to-live-evidence-console.html)  
**Existing Heart-View path:** [Heart-View Preview](../heart-view-preview.html)  
**Existing owner-provided HeyGen reference:** https://app.heygen.com/videos/avatar-v-video-5d938b91bb6841e9a9ddd93948c781b7

## 1. Required end-to-end chain

Voice source + authorization → voice-system job → approved script/content → authorized portrait/avatar → rendered audio/video → lip-sync and media QC → real dialogue/live Q&A → independent release review → public release.

Every transition must have a durable run ID and evidence record. A navigation link, configuration value, queued job, provider URL, generated template, or successful workflow execution is not proof that the user-visible output passed.

## 2. Stage state machine

Allowed statuses:

- `NOT_TESTED`: no run evidence has been evaluated.
- `QUEUED`: a job was accepted for execution; no output claim.
- `RUNNING`: a job is actively executing.
- `PASS`: output exists and the stage's acceptance checks passed.
- `FAIL`: a check ran and failed; retain failure reason.
- `BLOCKED`: a required credential, permission, asset, dependency, or human decision is missing.
- `WAIVED`: a named reviewer accepted a documented limitation for a bounded release; never count this as PASS.

Only PASS counts as a passed stage. Do not automatically promote QUEUED or RUNNING to PASS. Re-run after any material change to voice, script, portrait, provider, or render settings.

## 3. Minimum run record

Each stage event must capture:

| Field | Requirement |
|---|---|
| `run_id` | Stable UUID for one end-to-end attempt |
| `stage_id` | One of the eight stages listed below |
| `attempt` | Positive integer, incremented on retry |
| `status` | One allowed state above |
| `started_at`, `finished_at` | UTC timestamps; null only while not finished |
| `input_fingerprint` | Hash or stable version ID for the exact input; never expose secret values |
| `output_ref` | Artifact/provider job reference; avoid public links to private media |
| `checks` | Named checks, result, measured value, threshold and version |
| `reviewer` | Human reviewer or named automated check identity |
| `evidence_ref` | Durable log/artifact reference and access policy |
| `error_code`, `error_summary` | Required for FAIL/BLOCKED; redact tokens and personal data |
| `provider`, `provider_job_id` | Required when an external provider was used |
| `release_decision` | HOLD / APPROVED / REJECTED with reviewer and timestamp |

Do not put API keys, session cookies, voice biometrics, private customer data, or unredacted credentials in telemetry.

## 4. Eight stages and their pass conditions

1. **Voice source & authorization** — exact source asset is identified; rights/consent is recorded; the asset is accessible to the authorized workflow.
2. **Voice system** — actual output audio is available; job reference and settings are captured; listener checks for intelligibility, pronunciation, clipping and authorization pass.
3. **Content/dialogue** — exact script and version are recorded; language, factual claims and source notes are reviewed; unsafe or unsupported claims are handled.
4. **Portrait/avatar** — the authorized image/avatar asset and version are identified; identity/consent and asset-integrity checks pass.
5. **Rendered video** — actual media artifact exists and can be decoded and played fully; duration, resolution, audio presence and job reference are recorded.
6. **Lip-sync/audio QC** — synchronized audio/video is reviewed using a documented sampling method and threshold; pronunciation, clipping, silent frames and visual glitches are checked.
7. **Live Q&A / end-to-end** — a real session is executed against a versioned test set; response correctness, latency, failure handling, captions and fallback are recorded. A rehearsal page does not count.
8. **Independent release review** — reviewer checks all prior evidence, privacy/accessibility, open failures, rollback and user-facing disclosure; release decision is explicit.

Thresholds must be defined and versioned by the product owner before a run. Never invent a passing threshold after observing a result.

## 5. Counters: numerator, denominator and meaning

Publish counters with their source window and last-updated time. Show `N/A` when the denominator is zero; never display a fabricated 100%.

- **Stage pass rate** = PASS stage checks / all evaluated stage checks × 100.
- **Evidence coverage** = required evidence fields populated and validated / required evidence fields × 100.
- **End-to-end pass rate** = end-to-end runs that passed every required gate / completed end-to-end runs × 100.
- **First-pass yield** = runs passing all required gates on attempt 1 / runs with a completed first attempt × 100.
- **Failure rate** = completed failed runs / all completed runs × 100.
- **Availability** = minutes the monitored service passes its defined synthetic check / eligible monitored minutes × 100. Only report after an actual monitor is deployed.
- **Median / p95 latency** = measured end-to-end request duration from timestamped runs; publish sample count and period.
- **Production cycles** = unique run IDs actually started; retries are attempts, not new distinct cycles.
- **Generated artifacts** = distinct artifact IDs with storage references; templates are not unique verified products.
- **QC-passed artifacts** = artifacts that passed the named, versioned QC policy.
- **Published artifacts** = artifacts actually reachable at the intended public destination and passing smoke test.
- **Enquiries / paid orders / sales** = separate counters. Count an enquiry only from a real received record; a paid order only with payment evidence; revenue only from confirmed transactions net of refunds when known.

Do not combine unlike counters into a single “quality percentage”. A model/voice match score, if used, must name its method, sample size, limitations and reviewer; it is not a universal measure of a person's heart, character, consciousness or truth.

## 6. Automation and 24/7 operation

Automation must run only after the relevant runner, credentials, provider permissions, secret storage, monitoring destination and cost limits are configured. The implementation should:

1. Run on demand first; then add a bounded schedule only after a successful, reviewed end-to-end test.
2. Use a single-flight/concurrency lock so overlapping cycles cannot duplicate jobs or publish conflicting state.
3. Use idempotency keys and bounded retries with exponential backoff; never retry permanent auth/permission failures repeatedly.
4. Keep a durable append-only run ledger and artifact references. Browser `localStorage` is a prototype, not a shared 24/7 backend.
5. Keep secrets in GitHub Actions secrets or an approved secret manager; use least-privilege permissions.
6. Open a pull request for repository-generated changes where branch protection requires PR-only updates; never bypass protection or push directly to protected `main`.
7. Separate operational logs from user-facing counters and from independent release evidence.
8. Alert on stale heartbeat, repeated failure, provider quota, unusual spend and missing artifacts; include a runbook and manual stop switch.
9. Perform a post-release public URL smoke test and retain the exact commit, artifact, run and test references.
10. Provide a human-reviewed rollback path; a failed or uncertain stage holds the release.

A scheduled workflow being enabled is not proof of 24/7 service availability. Availability can be claimed only from deployed monitoring data over a stated time window.

## 7. Security and privacy gates

- Verify rights and consent for any voice, face, portrait or avatar asset before processing.
- Restrict private source media and test recordings; keep public demo assets separate from private originals.
- Redact secrets from logs and errors; validate provider webhooks and avoid trusting client-submitted status.
- Validate artifact MIME type, size, duration and file signature before processing.
- Apply rate limits, spend ceilings, access controls, audit logs and retention/deletion rules.
- Keep user-visible claims proportional to evidence; never claim a live integration, verified voice match, successful lip-sync, sale or scientific proof solely from code/configuration.

## 8. Release checklist

- [ ] The exact eight stages are represented in the run ledger.
- [ ] A single run ID joins inputs, provider jobs, media artifacts, QC and release review.
- [ ] Each stage has explicit, versioned pass conditions.
- [ ] A real end-to-end run has been completed twice, including one failure/fallback test.
- [ ] Evidence references are durable and access-controlled.
- [ ] Counters reconcile with raw run records and show sample counts/time window.
- [ ] External-provider behavior has been verified from actual outputs, not just a saved URL.
- [ ] Public-page smoke test and rollback test are recorded.
- [ ] Any unresolved item remains BLOCKED / NOT_TESTED and is disclosed.

## 9. Current honest baseline

The existing HTML Evidence Console is a browser-local manual register. It can help an operator record evidence and export an audit, but it does not itself connect to HeyGen, generate audio/video, provide real-time telemetry, synchronize across devices, create customer accounts, collect payment, or guarantee continuous operation. These are separate implementation and verification tasks. Keep the stages unverified until actual run artifacts are inspected.

## 10. Next implementation sequence

1. Preserve the existing operator console and current HeyGen reference; do not request the same assets again.
2. Add a server-side run ledger/API and authenticated reviewer workflow.
3. Add one provider adapter with secrets stored server-side and a sandbox/test mode.
4. Capture actual audio/video outputs and run reproducible QC.
5. Add live Q&A test harness and failure/fallback tests.
6. Wire counters to the durable ledger, not to manually typed totals.
7. Add bounded scheduled runs, monitoring and alerts only after steps 2–6 pass.
8. Gate publication on the independent release review.

This sequence deliberately prioritizes measurable proof and a small working vertical slice over claims that the entire platform is already complete.
