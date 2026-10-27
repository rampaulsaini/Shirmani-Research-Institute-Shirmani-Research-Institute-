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


## 19. Verified continuation checkpoint — 2026-09-21

This checkpoint was verified against the current GitHub repository state before continuation.

### Repository integrity
- Repository: `rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-`
- Visibility: public.
- Default branch: `main`.
- Repository is not archived.
- The connected owner context has admin/maintain/push permissions.
- Protected source records remain separate from generated derivatives.

### Heart-View preservation
- `SHIRMANI-HEART-VIEW-SUPREME-REASONING-LAYER.md` exists as the protected preservation policy.
- `source/user-directives/2026-09-20-shirmani-heart-view-request.md` exists as an exact user-source provenance record.
- The exact-source record has a SHA-256 content hash and is explicitly marked derivative-free.
- Latest preservation commit: `089177e4aac1256ece6809923c1c67e682c9a015`.

### Factory state
- `generated/factory-status.json` is present and records successful QC for the recorded 1,000-record product batch.
- The recorded target is 100,000 records, with 1,000 processed in that recorded batch.
- The dashboard-facing factory-status artifact is therefore no longer missing at this checkpoint.
- `generated/agent-status.json` and `generated/federation-status.json` are also present.
- Federation status records 23 managed agents: 21 READY and 2 MISSING, plus 1 external SOURCE_ONLY repository.

### Existing reasoning architecture
The repository already contains connected stages:
`repository intelligence → source collection → canonical knowledge → resumable batches → provenance/integrity → reasoning → claim/evidence → QC → formulation/test → independent verification queue → verification registry/promotion → evidence graph → publication gate → continuity manifest → publication PR`.

### Next incomplete work
1. Reconcile dashboard/generated status timestamps with the latest workflow outputs.
2. Validate the complete generated artifact chain from canonical records through publication gate.
3. Resolve the two federation entries marked MISSING, only where legitimate source access exists.
4. Continue independent-verification review packets without promoting unverified claims.
5. Keep every user-source record immutable; all improvements remain traceable derivatives.

### Percentage rule
No overall completion percentage is asserted here because the repository has multiple independent workstreams and no single authoritative denominator. Progress should be reported by concrete gates, counts, and verified artifacts rather than invented precision.

**Continuation principle: preserve exact source → verify pipeline state → complete the next failing/incomplete gate → commit traceable derivative only.**
