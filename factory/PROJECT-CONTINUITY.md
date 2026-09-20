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

## Latest completed engineering work
- Removed the latent research-question dependency from factory/batch_worker.py.
- Fixed the research-paper worker to call research_question(base["text"]) rather than a nonexistent question helper.
- Added and registered the deterministic Shirmani reasoning agent at factory/agents/shirmani_reasoning_agent.py.
- Added factory/reasoning_pipeline.py for reasoning/provenance records without converting philosophy into scientific fact.
- Extended deterministic QC to validate claim class, method trace, evidence status, provenance and human-review requirements.
- Integrated reasoning/provenance before QC in .github/workflows/omniverse-factory.yml.
- Isolated CI Python-source validation from vendored/template material under factory/_sources.
- Added Python-cache exclusions to .gitignore.
- Strengthened factory/queue_worker.py with atomic JSONL persistence, idempotent enqueue, retry scheduling, lease expiry recovery, dead-letter handling, and single-writer locking where fcntl is available.
- Added factory/tests/test_queue_worker.py covering idempotency, lease assignment, lease-token protection, retry/dead-letter lifecycle, and expired-lease recovery.
- PR #5 was intentionally closed unmerged after generated/cache files contaminated its branch; no contaminated PR content was merged into main.

## Current engineering state
The clean durable-queue implementation is prepared on branch feat/durable-queue-checkpoints-clean. It is not yet merged into main. CI/status must be verified before merge.

The existing factory/state.py remains the next integration point. It currently provides atomic state save/load and completed-item markers, but does not yet provide a complete v2 checkpoint model for in-flight jobs, retry/lease state, per-kind counters, artifact manifests, and recovery metadata.

## Current next engineering priorities
1. Verify the clean queue implementation and tests in CI.
2. Merge only the clean queue changes after verification.
3. Introduce a versioned state/checkpoint schema that records per-kind target/completed/running/retrying/failed counts, checkpoint cursor, artifact hashes/manifests, queue references, and recovery metadata.
4. Integrate queue claims, lease tokens, completion, and state checkpoints into the actual batch worker for every product type.
5. Expand lawful/open external knowledge ingestion with source/context metadata.
6. Build independently reviewable research workflows before calling any research result verified.
7. Keep the dashboard and publication layer synchronized with generated manifests.
8. Continue incremental expansion toward the defined product targets.

## Restart instruction
When a new chat says “Continue Shirmani Research Institute”, first inspect this file and the referenced current files in GitHub, then continue from the next engineering priority without reconstructing the project from chat memory.
