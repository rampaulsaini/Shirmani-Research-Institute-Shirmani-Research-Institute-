# SHIRMANI Automission Continuity and Safe-Cleanup Guardrails

**Status:** Proposed operational standard; not a claim that all controls are implemented.
**Scope:** GitHub Actions automation, production persistence, security gates, deployment, media integrity, and research/product production.
**Safety rule:** protect useful work first. No workflow, file, artifact, or branch is deleted solely because its name looks redundant, it has a low run count, or another workflow is green.

## Evidence observed during the 2026-10-17 repository review

The workflow search surfaced these distinct scheduled automation files:

| Workflow file | Observed trigger/concurrency detail | Review disposition |
|---|---|---|
| `.github/workflows/shirmani-product-first-automission.yml` | `*/5 * * * *`, manual dispatch, a dedicated concurrency group | Audit side effects, overlap, runtime, and outputs before changing cadence |
| `.github/workflows/shirmani-production-multi-layer-automission.yml` | `*/5 * * * *`, manual dispatch | Compare responsibilities and write targets with product-first workflow |
| `.github/workflows/unique-tool-automission.yml` | `*/5 * * * *`, manual dispatch, dedicated concurrency group | Compare generated outputs and branch/PR behavior |
| `.github/workflows/shirmani-production-first-operations.yml` | `*/10 * * * *`, manual dispatch, concurrency | Verify whether it duplicates checks or owns unique recovery operations |
| `.github/workflows/shirmani-inter-repository-automission.yml` | concurrency group includes `github.ref` | Check whether separate refs can concurrently mutate shared downstream resources |
| `.github/workflows/supreme-nlp-automission-health.yml` | `cancel-in-progress: true` | Verify that cancellation cannot interrupt a required write, publish, or recovery transaction |
| `.github/workflows/shirmani-supreme-multilayer-production.yml` | manual fallback; file comment says canonical production is handled by `public-production-automission.yml` | Candidate for de-duplication review, not deletion; validate dispatch consumers, permissions, and fallback purpose |

This is a **partial search-based inventory**, not a complete repository listing. The search result alone does not establish that any workflow is safe to remove.

## Required multi-layer execution model

1. **Discover:** enumerate workflow files, triggers, permissions, concurrency groups, path filters, dependencies, artifacts, branch/PR writes, schedules, and recent run outcomes.
2. **Classify:** label each workflow essential, unique support, duplicate candidate, obsolete candidate, blocked, or unknown. Record the evidence and owner for every classification.
3. **Validate before mutation:** compare actual commands, outputs, write destinations, downstream consumers, and required status checks. Names and descriptions are not enough.
4. **Serialize shared writes:** workflows that mutate the same branch, generated state, release, deployment, or persistence record must share an appropriate lock/concurrency strategy. Do not cancel an in-progress write unless it is safe and idempotent.
5. **Bound execution:** set appropriate job timeouts; use finite retries only for transient failures; add backoff; avoid retry storms and overlapping schedules.
6. **Least privilege:** grant only required token permissions. Read-only verification stages should remain read-only.
7. **Layer gates independently:** source/format checks → unit/regression tests → security/dependency checks → build/package → artifact integrity → deployment → production smoke test → persistence/truth gate → rollback readiness. Skip downstream publication when a required upstream gate fails.
8. **Truthful status:** every stage reports PASS, FAIL, BLOCKED, or NOT VERIFIED with commit SHA, run URL, timestamp, relevant logs/artifacts, and reproducible steps. Pending/cancelled is not PASS.
9. **Safe cleanup:** first open a small PR with an inventory, dependency analysis, and proposed removals. Preserve a recoverable copy or reversible git change. Delete only after confirming no required trigger, consumer, check, recovery path, or production output depends on it.
10. **Continuous review:** compare schedule overlap, queue time, run duration, cancellation frequency, duplicate artifacts, repeated PRs, failure rate, and production regressions. Optimize for useful validated product output, not workflow count.

## Stop conditions

Stop publication and report a clear blocker if any of these occurs:
- required security or regression check fails;
- a generated artifact has no stable identity or expected integrity evidence;
- concurrent runs may overwrite shared state;
- deployment smoke checks disagree with repository/build state;
- rollback path or last-known-good artifact is unavailable;
- a workflow is cancelled during a non-idempotent mutation;
- provider-backed features are claimed without a successful end-to-end test.

## Removal acceptance checklist

Before disabling/deleting a candidate, attach evidence for all:
- [ ] Complete workflow file and recent run history inspected.
- [ ] Triggers, branch protections, required checks, reusable-workflow callers, and dispatch callers checked.
- [ ] Outputs and downstream consumers identified.
- [ ] Overlapping responsibilities demonstrated by command/output equivalence, not names.
- [ ] Unique recovery/security/deployment behavior preserved elsewhere.
- [ ] A reversible PR and rollback instructions prepared.
- [ ] Tests show the remaining canonical workflow still produces the required output.
- [ ] Production owner approves after the evidence is reviewed.

## Immediate review queue

1. Investigate the reported cancelled `SHIRMANI Read-Only Security Baseline #922` and distinguish concurrency cancellation from a substantive failure.
2. Inspect pending serialized production runs before dispatching new runs.
3. Compare the two five-minute production/product-first workflows and `unique-tool-automission.yml` for overlapping writes and outputs.
4. Inspect `cancel-in-progress: true` in the Supreme NLP health workflow; keep it only if cancellation is safe for every interrupted step.
5. Verify the canonical public production workflow and the manual fallback before proposing any removal.
6. Verify the public Heart-View page and HeyGen media separately; a merged HTML preview is not proof of live avatar, voice, lip-sync, or provider API integration.

## Report format

| Check | Status | Evidence | Risk/blocker | Next action |
|---|---|---|---|---|
| Source and regression tests | NOT VERIFIED until run evidence attached | Commit + run URL | Unknown | Execute/check existing tests |
| Security baseline | NOT VERIFIED until latest result inspected | Run URL + logs | Cancellation reason unknown | Inspect run/job details |
| Artifact integrity | NOT VERIFIED until expected hash is sourced and compared | Approved original + computed hash | Original/hash may be missing | Obtain trusted source asset |
| Deployment smoke test | NOT VERIFIED until public endpoint is tested | URL + response/test log | Deployment may lag source | Verify deployed page |
| Provider-backed avatar/Q&A | NOT VERIFIED until end-to-end evidence exists | Provider run/output + test record | Prototype may be mistaken for integration | Run controlled acceptance tests |

**Do not mark a check PASS from this document alone.** This file establishes guardrails and a review queue; it does not execute workflows, inspect every dependency, or certify production health.
