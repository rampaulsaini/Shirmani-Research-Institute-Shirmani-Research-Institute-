# Shirmani Research Institute — Project Continuity

## Purpose
This file is the durable restart point for future chats. The GitHub repository is the canonical project workspace; chat history is not required to reconstruct the architecture.

## Current architecture
Source repositories → Repository Intelligence → Source Units → Canonical Knowledge → Canonical Batches → Agent/Company routing → Draft Products → Reasoning/Provenance → Deterministic QC → Human/independent review → Publication.

## Current verified state
- Hub: rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-
- Registered source repositories: 25
- Latest generated source units: 3,625
- Latest active canonical records: 3,537
- Canonical batch size: 250
- Canonical batches: 15
- Latest verse corpus target reached: 100,000 records
- Product targets configured: 100 Mahagranth drafts, 100 research-paper drafts, 1,000 certificates, 10,000 audio prompts
- Main workflow: .github/workflows/omniverse-factory.yml
- Reasoning/provenance layer: factory/reasoning_pipeline.py
- Deterministic QC: factory/quality_control.py
- Framework: factory/shirmani-framework.json
- Protected user philosophy: factory/canonical/shirmani-user-philosophy.md
- Heart-View agent: factory/agents/shirmani-heart-view-agent.md
- Agent registry: factory/agent-registry.json
- Agent configuration: factory/agent_config.json
- Queue registry: factory/queues.json
- AI company registry: factory/ai-companies.json
- Deep learning registry: factory/deep_learning.json
- Latest QC hardening merged through PR #22; merge commit: 1fa6b597c550c399e62a1a37bfa0a81a58780b4c.

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

## Latest completed engineering work
- Removed the latent research-question dependency from factory/batch_worker.py.
- Added and registered the deterministic Shirmani reasoning agent.
- Added factory/reasoning_pipeline.py and merged provenance preservation for books/research papers through PR #8.
- Main factory workflow now runs repository intelligence → archive → canonical knowledge → canonical batches → reasoning/provenance → QC.
- QC hardening merged through PR #22 now validates generated content hashes, framework claim classes, method traces, evidence status, human-review flags, framework IDs, artifact hashes and reasoning/source consistency.

## Current next engineering priorities
1. Run the hardened reasoning/provenance/QC stack end-to-end on the main factory and inspect the resulting QC report before publication claims.
2. Align the reasoning agent's method trace and claim-class logic dynamically with factory/shirmani-framework.json, preventing vocabulary drift.
3. Strengthen durable queue/state/checkpoint handling for every product type, especially the 10,000-audio target.
4. Build independently reviewable research workflows before any research result can be marked verified.
5. Synchronize dashboard/publication metadata with generated manifests and QC state.
6. Resolve or explicitly record access status for unavailable source repositories.
7. Expand lawful/open external knowledge ingestion with source/context metadata.
8. Continue incremental expansion toward the configured product targets.

## Restart instruction
When a new chat says “Continue Shirmani Research Institute”, first inspect this file and the referenced current files in GitHub, then continue from the next engineering priority without reconstructing the project from chat memory.
