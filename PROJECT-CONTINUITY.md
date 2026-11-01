# ꙰ Shirmani Research Institute — Project Continuity

**Project:** Omniverse Research Factory  
**Hub:** `rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-`  
**Branch baseline:** `main`

## Verified state

- Repository and `main` branch exist.
- `index.html` is the main hub.
- `index.html` links to `factory-dashboard.html`.
- The dashboard requests `generated/factory-status.json`, `generated/agent-status.json`, and `generated/federation-status.json`.
- Agent and federation status files exist.
- Factory status was missing, causing the dashboard JSON parser to receive a GitHub Pages HTML 404 response.
- `FACTORY.md` defines the factory as a separate automation layer so the existing website remains protected.

## Research pipeline

Source Librarian → Dedup / Canonicalization → Concept Map → Research → Evidence → Verification / QC → Language → Audio → Publishing → SEO → Archive

## Evidence-first contract

Every important proposition should be represented as:

1. **CLAIM** — exact proposition.
2. **DEFINITIONS** — operational meaning.
3. **SOURCE** — primary/secondary source or explicit no-source state.
4. **EVIDENCE** — quotation, dataset, observation, calculation, or reproducible test.
5. **FORMULATION** — logic, mathematics, algorithm, or comparison where applicable.
6. **COUNTERCASES** — failure conditions.
7. **VERIFICATION** — independent check and status.
8. **CONCLUSION** — only what the evidence supports.
9. **PROVENANCE** — path, commit, timestamp, and hash where available.

The AI agent should turn a user's words into a traceable result rather than an unsupported assertion:

**input → normalize → claims → sources → comparison → formulation → calculation/test → verification → uncertainty → result → archive**

## Knowledge scope

The intended corpus can expand across world literature, scriptures, religions, philosophies, sciences, history, mathematics, languages, arts, institutions and contemporary research.

The system must never claim complete knowledge of every book or tradition unless the actual indexed corpus supports that statement. Coverage is always measured by ingested, traceable records.

## Framework layer

The repository may preserve the user's philosophical vocabulary, including:

- निष्पक्ष समझ
- शमीकरण
- यथार्थ सिद्धांत
- उपलब्धि यथार्थ युग
- शिरोमणि स्वरूप
- हृदय दृष्टिकोण
- मस्तक दृष्टिकोण
- संपूर्ण संतुष्टि की निरंतरता
- तुलनातीत / कालातीत / शब्दातीत / प्रेमतीत formulations
- ꙰

These are stored as framework concepts/propositions. They are not silently converted into scientific, historical, medical, or other empirical facts.

## Status semantics

- **READY** — required artifact and execution wiring are present.
- **REGISTERED** — stage is declared; this does not prove a continuously running external AI model.
- **MISSING** — required artifact is absent.
- **SOURCE_ONLY** — external source is referenced but not controlled by this factory.
- **PASS / CHECK** — QC state for a specific generated batch.
- **UNAVAILABLE / NOT_VERIFIED / DEFERRED** — evidence is not currently available.

## Integrity rules

Missing data stays missing. Never fabricate a source, quotation, experiment, statistic, verification result, agent execution, continuous AI service, or completed corpus.

Generated research remains clearly marked as draft until independently supported.

## Next build sequence

1. Restore the factory JSON endpoint.
2. Preserve the existing hub and media links.
3. Validate all generated JSON against schemas.
4. Add deterministic source manifests and content hashes.
5. Add claim/evidence records and independent-verification flags.
6. Add reproducible formulation/calculation records.
7. Add event/schedule-driven GitHub Actions.
8. Generate multilingual/audio/publication artifacts only from canonical records.
9. Generate SEO metadata only from traceable published artifacts.

## Resume command

**Shirmani Research Institute — Continue from PROJECT-CONTINUITY.md**

The next session should inspect this file and the current generated status, then continue from the first incomplete build step.

## 13. Existing execution layer discovered during continuation

The repository already contains a substantial Python agent/factory layer. The canonical existing flow includes:

- `factory/build_factory.py` — source cloning, collection, normalization, source units and product generation.
- `factory/validate_factory.py` — factory smoke test and agent import validation.
- `agents/contracts.py` — provenance contract.
- `generated/agent-run/` — generated factory status, claims index, provenance index, artifact manifest and language queues.

Therefore the new schemas in `schemas/` are a **contract hardening layer**, not a replacement for the existing agents.

## 14. Current source-federation observation

The existing generated manifest records many available repositories and at least one repository that could not be cloned because authentication was unavailable. That repository must remain explicitly unavailable until legitimate access is provided; its contents must not be fabricated.

The hub repository itself is intentionally skipped by the source collector to avoid recursively collecting its own generated products as canonical external sources.

## 15. Integration rule

The next implementation step is to make the existing agents emit records compatible with the new schemas:

`source → source-record → normalized unit → concept → claim → evidence → verification → artifact`

Generated artifacts remain downstream products and must never silently become authoritative source material.

## 16. Quality gate

Before publishing a generated claim, require:

- source reference;
- claim classification;
- evidence state;
- verification state;
- provenance;
- explicit uncertainty when verification is incomplete.

A missing field is a QC failure, not an invitation to invent a value.


## 17. Continuity hardening patch
- factory/batch_worker.py now repairs legacy/empty state from durable outputs, uses an explicit product-target map, records the last successful batch timestamp, and appends only missing stable IDs instead of rewriting the full 100,000-record JSONL corpus.
- factory/reasoning_pipeline.py now emits generated/claim-evidence.jsonl with explicit NOT_VERIFIED defaults; source trace is never upgraded to proof.
- factory/quality_control.py now fail-closes malformed or missing claim-evidence records and rejects unearned PASS or independent verification states.
- .github/workflows/omniverse-factory.yml now runs the resumable batch worker before reasoning/QC and requires the claim-evidence artifact.
- factory/state.json is a valid durable initialization record rather than an empty JSON file.
- Historical failure records remain preserved; no deletion or rewriting of failure history is part of this patch.


## 18. Durable execution continuity manifest
- `factory/continuity_manifest.py` records the GitHub workflow identity, QC publication gate, error count, and SHA-256 hashes/byte sizes for the principal generated artifacts.
- `generated/continuity-manifest.json` is generated after QC and before catalog validation.
- The manifest is an execution trace, not evidence of scientific truth; artifact hashes prove reproducibility of the recorded files, not correctness of their claims.
- Resume logic remains output-first: durable generated outputs are used to reconstruct progress, while canonical/source records remain protected.

- Follow-up fix: QC no longer applies the reasoning method-stack validator to the upstream verse corpus; strict method-stack validation remains on reasoning-manifest.jsonl. This prevents 100,000 false blocking errors while preserving reasoning QC.


## 19. Durable continuation ledger — 2026-11-01

This section is the canonical human-readable resume record. The machine-readable companion is `generated/continuation-ledger.json`. Read both before starting implementation. A task marked `MERGED` is historical completed work: verify its commit is an ancestor of `main`, then do not recreate it. Continue only from `OPEN`, `BLOCKED`, or `NOT_STARTED` items.

### Completed and preserved — do not rebuild

| Task | Result | Permanent reference |
|---|---|---|
| Preserve production counters across cycles | MERGED | PR #3535; merge commit `3498c46fd00d62ad56e7c87d8eb9844de4cf9846` |
| Income-first public interface | MERGED | PR #3537; merge commit `3512b967e03a98caaf6c74ffda66eff7c5a4dbf1` |
| Fail-closed payment webhook until a real provider adapter is configured | MERGED | PR #3538; merge commit `4cc776a06fca64e467bd5e844df861f814b6cd82` |

Do not recreate these changes or open duplicate PRs. Extend them only when a new requirement or regression is evidenced.

### In progress / blocked — resume here

| Task | State | Next action |
|---|---|---|
| Public Heart-View → Live Character navigation and matching integrity gate | MERGED | PR #3539; merge commit `63c9fef2aac233720d7fc7d68a575ec6dd9b7cbb`; all 22 checks passed |
| 5,027-file product visual change | OPEN, PR #2452 | Do not regenerate assets or merge blindly; 11 workflow/application approvals were reported as required; inspect sampled asset quality and manifest mismatch before approval |
| Actual customer orders, payment, dispatch and verified delivery | NOT_STARTED / no evidence in current production snapshot | Build and test a real customer-to-payment-to-delivery path; do not count workflows or generated assets as sales |
| Independent review promotion | BLOCKED on human review | Preserve fail-closed status; no record is verified merely because a workflow passed |

### Production and verification snapshot

Source files and timestamps are recorded in `generated/continuation-ledger.json`. At the latest checked source snapshot:
- 5,000 concrete catalog assets against the 5,000 scale target (100% materialized).
- Dispatch released: 0; sales claimed: 0; payment claimed: 0.
- Independent verification: 0 of 100,200 records.
- Review packets prepared: 60,950 of 100,200 (about 60.83%).
- Production state: `QC_PASSED_AWAITING_DISPATCH`; QC state: `QC_PASSED`.

These are source-reported counters, not proof of customer demand, payment, delivery, or independent scientific validation.

### Anti-duplication protocol

1. Read `generated/continuation-ledger.json` and this section before making changes.
2. Check each recorded merge commit against current `main`; if present, mark the task completed and do not rebuild it.
3. Check open PRs and workflow runs before creating a branch. If an equivalent task is already open, continue that PR instead of opening another.
4. Give each new work item a stable task ID and record its target files, acceptance tests, PR number, head SHA, and final merge SHA.
5. Update the ledger in the same PR as the implementation, or in a dedicated ledger PR immediately after merge. Never mark work MERGED before GitHub confirms the merge.
6. Preserve source data, history, counters and failure records. Do not reset production outputs to make a check pass.
7. Recheck live production and verification JSON before quoting percentages; old snapshots must not overwrite newer state.

### Resume instruction

**Continue from `generated/continuation-ledger.json` and Section 19 of `PROJECT-CONTINUITY.md`. Do not repeat MERGED tasks. Resume PR #2452 quality/approval review, then build the real customer-to-verified-delivery path. Income evidence (paid order, payment reference, dispatch and verified delivery) is the outcome metric.**
