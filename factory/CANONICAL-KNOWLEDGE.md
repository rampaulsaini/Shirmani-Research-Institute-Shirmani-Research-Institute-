# Canonical Knowledge Layer

The factory maintains an incremental canonical knowledge layer at `generated/canonical-knowledge.jsonl`.

## Rules
- Records are derived only from collected repository source units.
- Each record has a stable ID based on repository, branch, path, and source hash.
- Records that disappear from a later snapshot are retained as `active: false`.
- `first_seen_at` and `last_seen_at` make change history traceable.
- Generated books, verses, papers, certificates, and future audio outputs are not source material.
- Research outputs remain drafts until independently reviewed and verified.

The layer is designed for resumable downstream agents: agents consume active canonical records without rebuilding identity from scratch on every run.
