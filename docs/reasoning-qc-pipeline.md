# Reasoning + Provenance + Verification QC

The factory now treats reasoning metadata as a first-class production artifact.

## Flow

Canonical source → product generation → reasoning layer → provenance ledger →
verification metadata → deterministic QC → human/independent review → publication.

The reasoning layer does not turn a source trace into proof. It records:
- claim class
- framework ID
- source IDs
- method trace
- verification questions
- evidence status
- human-review requirement
- content hash and creation timestamp

## Product coverage

The same contract is attached to:
- verse/song/shlok/sutra records
- digital book drafts
- research-paper drafts

Generated text remains non-canonical. Research remains a draft until independent verification.

## Publication gate

QC must block publication when reasoning metadata is missing, malformed, disconnected
from the artifact hash, or inconsistent with the artifact status. A verified label
requires evidence metadata; generation alone cannot produce that status.

## Reproducibility

Artifact identity is content-addressed. A changed artifact produces a changed content
hash, so stale reasoning metadata cannot silently remain attached to new text.
reasoning-manifest.jsonl is regenerated from the current generated artifacts.