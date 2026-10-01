# Supreme AI / ML / NLP / Automission Precision Architecture

## Target
Build a fast, evidence-first conveyor that maximizes measurable correctness rather than making an unverifiable claim of perfect accuracy.

## Layered execution
1. Intake — stable task ID.
2. Canonicalization — normalize text, entities, units, dates and schemas.
3. Retrieval — primary evidence first; hybrid lexical/semantic retrieval where available.
4. Reasoning — candidate answer with explicit assumptions.
5. Countercheck — independent contradiction and missing-case search.
6. Evidence — provenance attached to externally verifiable claims.
7. Verification — insufficient evidence remains UNVERIFIED.
8. Quality gate — schema, provenance, duplication, consistency and replay checks.
9. Publication — only gated outputs become publishable.

## Accuracy engineering
Track groundedness, accuracy, consistency, coverage, latency and failure rate independently. No single model confidence score is proof.

## ML/NLP integration contract
Adapters may include embedding/retrieval, reranking, claim/entity extraction, contradiction/NLI, classifier/evaluator and generation. Each adapter should expose:
input_hash -> model_id -> model_version -> parameters -> output_hash -> evaluation_metrics

External calls need timeout, retry, rate-limit and cost controls. A failed model call must not silently become successful verification.

## Automission control loop
observe -> validate -> select -> execute -> measure -> checkpoint

The five-minute workflow is deliberately lightweight. Concurrency cancellation prevents stale-run buildup. Irreversible actions remain outside unattended execution unless explicitly authorized.

## Failure handling
Classify failures as SCHEMA_FAILURE, RETRIEVAL_FAILURE, EVIDENCE_GAP, CONTRADICTION, MODEL_TIMEOUT, RATE_LIMIT, QUALITY_GATE_FAILURE or UNVERIFIED. Retry transient failures; do not endlessly retry semantic contradictions.

## Next implementation layer
Add an idempotent queue processor for the existing 100,200-item review state, with stable item hashes, small batches, durable checkpoints and per-item verification status. Reuse the existing governance instead of creating a second truth system.
