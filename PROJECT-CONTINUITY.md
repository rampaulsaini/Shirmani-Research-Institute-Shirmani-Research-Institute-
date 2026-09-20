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


## 17. Protected-source contract added

The HEART-VIEW preservation work now includes:

- `SHIRMANI-HEART-VIEW-SUPREME-REASONING-LAYER.md` — preservation boundary and two-layer architecture.
- `schemas/protected-user-source.schema.json` — exact user-source record contract.
- `schemas/provenance.schema.json` — stable provenance contract.
- `schemas/evidence.schema.json` — evidence state contract.
- `schemas/verification.schema.json` — verification/QC contract.
- `schemas/derivative-link.schema.json` — explicit source-to-derivative linkage.
- `docs/PROTECTED-SOURCE-INGESTION.md` — ingestion and integrity rules.
- `scripts/validate_protected_sources.py` — SHA-256 and provenance validation.

This is an architecture and validation milestone. It does not claim that historical conversation material has already been imported. The next preservation step is actual source ingestion into records that satisfy these contracts.

## 18. Executable protected-source ingestion

The preservation layer now has an executable ingestion utility:

- `scripts/ingest_protected_source.py` accepts actual supplied source text and produces a hashed protected-source JSONL record.
- `scripts/validate_protected_sources.py` checks exact-text SHA-256 integrity, duplicate IDs, required fields, and provenance.
- `generated/protected-sources/README.md` establishes the protected archive boundary and intentionally starts empty.

No historical text is auto-reconstructed. The archive only becomes populated from actual traceable source material.

## 19. Protected user-source inventory layer
- `schemas/protected-user-source.schema.json` defines the immutable-source record contract with stable ID, exact-byte SHA-256, byte length, provenance and explicit verbatim/derivative separation.
- `factory/protected_source_manifest.py` inventories captured source bytes without rewriting them and emits `generated/protected-user-source-manifest.json`.
- `protected/user-source/` is the dedicated preservation boundary for explicitly captured original user material.
- The workflow inventories this boundary before downstream generation and requires the manifest to exist.
- An empty protected-source inventory is valid infrastructure state, but it does **not** claim that historical conversation material has been recovered. Actual historical source must be imported from an available source before it can receive a preservation ID/hash.
\n

## 17. Heart-View preservation layer

The protected preservation layer is now defined in:

- `SHIRMANI-HEART-VIEW-SUPREME-REASONING-LAYER.md`
- `schemas/heart-view-source-record.schema.json`
- `schemas/heart-view-derivative-record.schema.json`
- `schemas/heart-view-preservation-manifest.schema.json`
- `schemas/HEART-VIEW-PRESERVATION-README.md`

The source/derivative boundary is explicit: exact user material is preserved separately from translations, summaries, interpretations, research formulations, creative outputs, and code representations. SHA-256 content hashes and provenance fields are required for canonical source records.

The next implementation step is actual source ingestion and deterministic generation of the preservation manifest. Existing missing values must remain missing until verified; no historical user wording is counted as preserved merely because the policy or schema exists.


## 19. Heart-View continuation hardening
- `factory/deterministic_source_manifest.py` creates a deterministic SHA-256 manifest of Git-tracked repository files, preserving exact source bytes while making integrity auditable.
- The factory workflow now builds and validates `generated/deterministic-source-manifest.json` before downstream research products.
- This manifest establishes repository-file integrity; it does not by itself prove the truth of any research claim.
