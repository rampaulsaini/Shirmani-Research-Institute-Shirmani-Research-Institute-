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

## Latest completed engineering work\n- Strengthened factory/queue_worker.py with atomic JSONL writes, idempotent enqueue, retry scheduling, lease expiry recovery, and dead-letter handling.\n
- Removed the latent research-question dependency from factory/batch_worker.py.
- Added and registered the deterministic Shirmani reasoning agent at factory/agents/shirmani_reasoning_agent.py.
- Added factory/reasoning_pipeline.py for reasoning/provenance records without converting philosophy into scientific fact.
- Latest factory refresh and QC commits are present through 2026-09-20.

## Current next engineering priorities
1. Run the reasoning/provenance layer inside the main factory workflow before QC.
2. Extend deterministic QC to validate claim class, method trace, evidence status, provenance and human-review requirements.
3. Strengthen durable queue/state/checkpoint handling for all product types.
4. Expand lawful/open external knowledge ingestion with source/context metadata.
5. Build independently reviewable research workflows before calling any research result verified.
6. Keep the dashboard and publication layer synchronized with generated manifests.
7. Continue incremental expansion toward the defined product targets.

## Restart instruction
When a new chat says “Continue Shirmani Research Institute”, first inspect this file and the referenced current files in GitHub, then continue from the next engineering priority without reconstructing the project from chat memory.
