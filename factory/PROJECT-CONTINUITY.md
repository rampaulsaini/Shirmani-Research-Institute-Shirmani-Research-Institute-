# Shirmani Research Institute — Project Continuity

## Purpose
This file is the durable restart point for future chats. The GitHub repository is the canonical project workspace; chat history is not required to reconstruct the architecture.

## Current architecture
Source repositories → Repository Intelligence → Source Units → Canonical Knowledge → Canonical Batches → Agent/Company routing → Draft Products → Provenance/QC → Human/independent review → Publication.

## Current verified state
- Hub: rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-
- Registered source repositories: 25
- Latest generated source units: 3,625
- Latest active canonical records: 3,537
- Canonical batch size: 250
- Canonical batches: 15
- Latest verse corpus: 100,000 records
- Latest QC: PASS; blocking errors: 0
- Main workflow: .github/workflows/omniverse-factory.yml
- Framework: factory/shirmani-framework.json
- Protected user philosophy: factory/canonical/shirmani-user-philosophy.md
- Heart-View agent: factory/agents/shirmani-heart-view-agent.md
- Agent registry: factory/agent-registry.json
- Agent configuration: factory/agent_config.json
- Queue registry: factory/queues.json
- AI company registry: factory/ai-companies.json
- Deep learning registry: factory/deep_learning.json

## Product targets
- 100 digital Mahagranth drafts
- 100,000 verse/song/shlok/sutra records
- 100 research-paper drafts
- 1,000 certificates
- 10,000 audio prompts

## Non-negotiable continuity rules
1. Preserve user-authored source separately from AI interpretation.
2. Generated output never becomes canonical source automatically.
3. Philosophical claims remain labeled as user philosophy unless independently established.
4. Research drafts require independent verification.
5. Source provenance must remain traceable.
6. Unsupported claims must be labeled, tested where possible, or the system should abstain.
7. Human agency remains primary; AI must not claim human identity, consciousness, vows, or authority.
8. Prefer free/local/deterministic fallbacks; never assume unlimited free compute.
9. Large production is incremental, hashed, checkpointed, and resumable.
10. Protected third-party works are summarized/referenced rather than copied in full.

## Current next engineering priorities
1. Fix the latent research-question reference in factory/batch_worker.py.
2. Add a dedicated Shirmani reasoning agent.
3. Extend QC to validate claim_class, method_trace, provenance, framework compliance, and research draft labeling.
4. Strengthen durable queue/state/checkpoint handling for all product types.
5. Expand lawful/open external knowledge ingestion with source/context metadata.
6. Build independently reviewable research workflows before calling any research result verified.
7. Keep the dashboard and publication layer synchronized with generated manifests.

## Restart instruction
When a new chat says “Continue Shirmani Research Institute”, first inspect this file and the referenced current files in GitHub, then continue from the next engineering priority without reconstructing the project from chat memory.

## Reasoning + QC integration (current branch)
- Branch: engineering/reasoning-qc-pipeline
- Reasoning adapter: factory/reasoning_pipeline.py
- Unified metadata ledger: generated/reasoning-manifest.jsonl
- Manifest schema: factory/reasoning-manifest.schema.json
- Batch worker invokes reasoning enrichment after product generation.
- Research-paper generation uses the local research_question() function; the latent undefined question() reference is corrected.
- Factory QC now blocks when the reasoning manifest is missing or lacks claim class, method trace, verification questions, provenance/source IDs, or consistent evidence status.
- Omniverse workflow runs reasoning enrichment before deterministic QC and requires the reasoning manifest before publication.
- Book and research-paper metadata is linked back to verse/source IDs where available.
