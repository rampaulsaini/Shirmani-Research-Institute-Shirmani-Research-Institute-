# Universal Synchronization, NLP and Scientific Visualization Architecture

**Status:** proposal / documentation only. This document does not claim that the integrations below are deployed, connected, real-time, or independently validated.

## Purpose

Create one understandable interface across the Shirmani Research Institute's digital catalogue, websites, web apps, products, tools, research sources and (where scientifically appropriate) educational models of matter and life.

The design principle is **one shared language and evidence model, not one undifferentiated database or one giant executable**. Each connected system keeps its own source of truth. The Institute coordinates records through documented adapters and versioned events.

## Repositories and their appropriate roles

| Repository | Observed contents | Recommended role | Boundary |
|---|---|---|---|
| [Koyab Founding Declaration](https://github.com/rampaulsaini/Koyab-Founding-Declaration-Omniversal-Manifesto) | Declaration of balance, humanity/nature, neutral understanding, compassion and peace; MIT license reported by GitHub | Human-readable principles and product/service governance policy | Principles guide decisions; they are not scientific evidence or executable authorization |
| [kit-app-template](https://github.com/rampaulsaini/kit-app-template) | Fork of NVIDIA Omniverse Kit App Template; Python/C++, OpenUSD, GPU-oriented 3D app templates and a receipt-only federation intake workflow | Optional specialist workspace for 3D education, visualization and simulation prototypes | Keep it isolated as an optional renderer/simulation service. Check the current NVIDIA and component terms before use, redistribution, hosting or commercial delivery |
| [C-Labs](https://github.com/rampaulsaini/C-Labs) | Fork of Hantz509/C-Labs; current `main.cpp` is a small C++ character-run counting exercise; no repository license was reported | Isolated algorithm learning and benchmark sandbox only | Do not treat it as an NLP engine. Do not copy, modify, or redistribute upstream code until permission/license is confirmed |
| [Shirmani Research Institute](https://github.com/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-) | Public catalogue/showroom, browser-local production tools, evidence-aware discovery page | Main public interface, product catalogue and orchestration layer | Browser-local prototypes remain distinct from server-backed, live integrations |

## Shared record contract

Every adapter should translate source data into a common, versioned envelope. Suggested fields:

- `schema_version`: contract version
- `record_id`: stable Institute identifier
- `source_id` and `source_record_id`: original system and record identity
- `record_type`: website, webapp, product, tool, API, research, scientific_concept, dataset, media, or service
- `title`, `summary`, `language`, `tags`
- `source_url`, `license`, `rights_checked_at`
- `source_updated_at`, `observed_at`, `synced_at`
- `content_hash` and `source_version`
- `verification_status`: unverified, reviewed, verified, rejected, or stale
- `evidence_refs`: references to supporting material and test results
- `consent_scope` and `access_class` where personal or restricted data is involved

A repeated identical observation must not erase a valid review. A material change to source content, rights, or provenance must mark the record stale/unverified and request re-review. Preserve an append-only change history.

## Synchronization mechanism

1. **Discover:** use official APIs, feeds, repository metadata or explicitly supplied files. No arbitrary URL crawling or access-control bypass.
2. **Normalize:** validate and map source fields into the shared contract.
3. **Identify:** deduplicate by source identity and stable content hash.
4. **Queue:** record an event with source version and checkpoint; make retries idempotent.
5. **Apply:** update only the relevant record, retaining provenance and previous versions.
6. **Verify:** distinguish source availability, automated checks, human review and independent scientific verification.
7. **Present:** show the user the current state, last sync time, source link, limitations and next action.
8. **Recover:** bounded retries, rate-limit handling, dead-letter/error status and a visible manual retry path.

Synchronization is eventual and bounded by provider rate limits, quotas, queues and service availability. Do not promise universal, instantaneous or atomic synchronization.

## NLP interaction in सरल, सहज, निर्मल, पारदर्शी भाषा

Use a layered language pipeline:

1. Receive Hindi, English or another supported language.
2. Detect language and preserve the original user text.
3. Normalize spelling and phrasing without changing intent.
4. Extract entities, objects, quantities, dates, relationships and requested action.
5. Classify intent: explain, discover, compare, verify, create, synchronize or purchase.
6. Retrieve only authorized sources and attach provenance.
7. Check freshness, conflicts, confidence and evidence state.
8. Explain in plain language: **क्या मिला → किस स्रोत से → कितना जाँचा गया → क्या अभी बाकी है**.
9. For external changes, ask for approval where required; never infer consent for payment, publication, messaging, deletion or irreversible operations.
10. Record the action result and show failures honestly.

Suggested user-facing status words: **उपलब्ध**, **जाँच बाकी**, **जाँचा गया**, **स्रोत बदला**, **समन्वय जारी**, **विफल**, **अनुमति चाहिए**.

## Scientific and living-world models

Keep different scientific domains distinct while allowing them to share the presentation contract:

- **Particle/atomic model:** proton, neutron and electron counts, charge, mass number, units, source and model assumptions.
- **Molecular model:** atoms, bonds, geometry and chemistry-specific evidence.
- **Microbiology model:** organism/taxon, cell structure, environment, observation method, date and scientific source.
- **Digital systems model:** websites, applications, APIs, products, services and their dependencies.

A 3D scene may visualize these models; it does not itself prove a scientific claim. Label educational illustrations, simulated outputs, measured observations and independently validated results separately. Never imply that software synchronization physically controls particles, electrons, organisms or nature.

## Delivery sequence

### Phase 1 — shared contract and public explanation
Document the record schema, evidence states, Hindi status vocabulary and source/rights boundaries in the main Institute repository.

### Phase 2 — safe digital-source adapters
Connect one source at a time through official APIs. Start with the GitHub discovery work in the separate FreeLLMAPI repository; add other providers only after their official API, authorization, quota and terms are checked.

### Phase 3 — NLP layer
Build a small, testable intent/normalization/explanation service. Keep model-provider credentials server-side; never expose API keys in browser code or public records.

### Phase 4 — optional Omniverse visualization
Prototype one clearly labelled educational scene only after the required SDK, hardware/cloud cost, runtime and license checks. Keep the 3D renderer optional so the public catalogue remains lightweight.

### Phase 5 — customer value and income evidence
Expose useful product demonstrations, enquiry, consent-based proposal, verified payment and delivery records. A catalogue entry, generated report, successful CI run or simulation is not a sale or payment.

## Acceptance gates

- Contract schema has automated validation and migration tests.
- Adapters have pagination, rate-limit, timeout, retry and deduplication tests.
- Changed source content invalidates stale verification.
- No secret, personal data or untrusted instruction is executed from an ingested record.
- Hindi explanations identify source, freshness, uncertainty and evidence status.
- Scientific views label simulation versus measurement.
- No integration is called live until the deployed endpoint and public user journey are smoke-tested.
- Commercial reuse is blocked until all applicable repository, SDK, model and data licenses are checked.

## Current status

This is an architecture proposal only. No code from the three repositories has been merged into the Institute, no Omniverse runtime has been deployed, and no universal real-time synchronization or NLP service is claimed.
