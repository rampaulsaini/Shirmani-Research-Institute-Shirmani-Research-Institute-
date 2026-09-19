# Factory Job Queue

The queue makes large production resumable and idempotent. Each product has a stable job ID, product kind, sequence number, topic and status.

## Lifecycle
pending → running → done / failed

The queue is designed for GitHub Actions and free deterministic processing. A batch can be resumed without requiring one workflow run to generate every product.

## Truth and provenance
Queue state controls production only. It does not turn user-authored philosophy into independently verified fact. Research claims still require independent evidence and review.
