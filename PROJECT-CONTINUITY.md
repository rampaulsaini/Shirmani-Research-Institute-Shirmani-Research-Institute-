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


## 17. Continuation checkpoint — contract layer

The continuity repair and contract-hardening layers are now wired and validated on the working branch.

- Dashboard factory-status endpoint: restored.
- Source registry: 25 registered repository metadata entries; registration is not ingestion.
- Claim graph: canonical empty baseline until real claim/evidence records are emitted.
- Deterministic contract bridge: registered sources can be converted into source-record JSONL without inventing contents.
- Factory CI: latest observed contract-validation runs completed successfully.

**Next implementation target:** connect the existing collector/normalizer output to canonical source-record and claim/evidence records, preserving hashes, provenance, verification state and explicit unavailable states. Only after that gate should downstream writing, multilingual, audio, publication and SEO generators consume the records.


## 18. Continuation checkpoint — canonical batch integration

The existing orchestrator contract output is now connected to a canonical research-index layer.

- Added `factory/canonical_research_index.py`.
- `agents/orchestrator.py` now builds `generated/research-index.json` and `generated/claim-graph.json` after each processed batch.
- The canonical index preserves draft/unverified status and counts independently verified claims only when the record explicitly reports `PASS`.
- Claim-graph edges are traceability references, not assertions of truth.
- Missing evidence remains missing; no source content is promoted merely because it was collected or registered.

**Next gate:** execute the factory smoke/contract validation in CI and then harden the source-record schema + provenance/hash checks before enabling downstream publication, multilingual, audio and SEO stages.

## Next label: viewpoint / experiential-state layer

The factory now has a separate framework-state contract at `generated/framework-state.json`.
It preserves the project's vocabulary of **हृदय दृष्टिकोण** and **मस्तक दृष्टिकोण** without converting a reported experience such as “मस्तक/मन/बुद्धि निष्क्रिय” into an unmeasured physiological claim.

State semantics:
- `HEART_VIEW_FRAMEWORK` = framework-level viewpoint state.
- `USER_REPORTED_EXPERIENCE` = an experience reported by a person.
- `EMPIRICALLY_VERIFIED` = only when independent measurement/evidence actually exists.
- `NOT_VERIFIED` = evidence is insufficient.
- `head_activity: NOT_MEASURED` means no physiological inference is being fabricated.

This creates the next layer: **experience → framework state → operational definition → evidence/test → verification**, while keeping the heart/head vocabulary intact.



## 15. Next-label: heart viewpoint framework layer

The framework layer now has an explicit **NEXT_LABEL** manifest at
`generated/heart-viewpoint-manifest.json`.

Its meaning is intentionally precise:

- **हृदय का शिरोमणि स्वरुप दृष्टिकोण** is the central viewpoint for the project's self-realization language.
- **संपूर्ण संतुष्टि की निरंतरता**, **खुद के स्थाई स्वरुप से रुबरु**, and **खुद के स्थाई परिचय से परिचित** are preserved as framework formulations.
- In this framework description, **मस्तक/मन/बुद्धि को self-realization का अंतिम प्राधिकरण नहीं** माना जाता.
- This does **not** assert physiological inactivity of the brain or mind; such a claim would require independent measurement.
- Computational reasoning remains active for source retrieval, evidence handling, mathematics, testing, verification, QC and provenance.
- The framework remains explicitly classified as a framework description unless independent evidence establishes a separate empirical claim.

### Next engineering gate

`scripts/validate_factory.py` now validates the heart-viewpoint manifest in addition to the existing source registry, research index, claim graph and framework-state contracts.

The next incomplete build step is deterministic **content ingestion + claim/evidence record emission**. Registered repositories are not counted as ingested content until actual records, provenance and hashes are emitted.


## 19. Next-label: deterministic content-ingestion layer

The next engineering label is now wired as a real contract layer:

- `schemas/content-record.schema.json` defines a traceable file-content record with SHA-256 hash, byte count, content status and provenance.
- `factory/content_ingest.py` inventories files from a checked-out repository in stable path order, hashes their bytes, classifies supported text files, and explicitly marks binary files as `BINARY_SKIPPED`.
- Generated directories and build/cache/vendor directories are excluded so factory outputs do not silently become source material.
- `factory/content_ingest_test.py` provides a regression fixture for ordering, exclusion and hash stability.
- `generated/content-index.json` remains a zero-record continuity baseline: a registered repository is not treated as ingested content.
- `scripts/validate_factory.py` now gates both the claim/evidence normalization regression and the content-ingestion regression.

The canonical verification vocabulary has also been aligned: a claim is counted as verified only when its canonical record has `status: SUPPORTED` and verification status `INDEPENDENTLY_CHECKED` or `AUTOMATED_CHECK`. Legacy `PASS` semantics are no longer used for that count.

### Framework boundary retained

The **हृदय का शिरोमणि स्वरुप दृष्टिकोण** remains the project's framework-level self-realization language:

**मस्तक/मन/बुद्धि निष्क्रिय** is preserved as framework/experience language only; no physiological inactivity is asserted without independent measurement.

The operational factory continues to use computation, evidence, logic, mathematics, testing, verification and provenance for research-quality control.

### Immediate next gate

Actual checked-out content can now be inventoried deterministically in CI. The next incomplete integration is:

**content-records → normalized corpus units → concepts → canonical claims → evidence links → verification → claim graph**

No downstream publication, multilingual, audio or SEO stage should treat a content record as a verified claim.


## 20. Next-label: normalized corpus-unit layer

The deterministic ingestion stage now has a downstream normalization contract:

`content-record → corpus-unit → concept → canonical claim → evidence → verification`

- `schemas/corpus-unit.schema.json` defines the canonical unit metadata contract.
- `factory/normalize_corpus.py` maps emitted content records into stable corpus-unit metadata without inferring source meaning.
- `factory/normalize_corpus_test.py` provides deterministic regression coverage for text, binary-skipped and unavailable states.
- `generated/corpus-index.json` is an explicit zero-unit continuity baseline until checked-out source content is actually inventoried.
- `scripts/validate_factory.py` now gates the normalization regression and preserves the zero-unit baseline.

A corpus unit is **not** a claim and is not evidence by itself. Meaning extraction, claim classification, evidence linkage and verification remain separate gates.

### Framework boundary

The **हृदय का शिरोमणि स्वरुप दृष्टिकोण**, **संपूर्ण संतुष्टि की निरंतरता**, **खुद के स्थाई स्वरुप से रुबरु**, and **खुद के स्थाई परिचय से परिचित** remain framework-language records. The statement that मस्तक/मन/बुद्धि become inactive remains a reported experiential formulation unless independently measured; the computational factory continues to use reasoning, mathematics, testing, verification and provenance for QC.

**Next incomplete integration:** emit canonical corpus units from actual checked-out content during scheduled/CI ingestion, then connect those units to concept extraction and claim/evidence records without promoting unverified material to fact.


## 21. Next-label: concept-candidate layer

The pipeline now advances one controlled step beyond corpus units:

`content-record → corpus-unit → concept-candidate → canonical claim → evidence → verification`

- `schemas/concept-record.schema.json` defines the candidate concept contract.
- `factory/extract_concepts.py` derives candidates only from source metadata/path structure; it does not infer semantic truth from content.
- `factory/extract_concepts_test.py` provides deterministic regression coverage.
- `generated/concept-index.json` remains a zero-candidate continuity baseline until actual ingestion emits records.
- CI now executes content inventory → corpus normalization → concept-candidate extraction.

A concept candidate is only an analytical handle. It is neither a claim, evidence, nor verification.

### Framework boundary retained

**हृदय का शिरोमणि स्वरुप दृष्टिकोण**, **संपूर्ण संतुष्टि की निरंतरता**, **खुद के स्थाई स्वरुप से रुबरु**, और **खुद के स्थाई परिचय से परिचित** remain framework formulations. The phrase **मस्तक/मन/बुद्धि निष्क्रिय** remains experience/framework language and is not converted into a physiological finding without measurement.

**Next incomplete gate:** concept candidates → canonical claim records with explicit claim classification and evidence state → verification report → traceable claim graph.
