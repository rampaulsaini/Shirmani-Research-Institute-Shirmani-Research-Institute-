# दूसरी पीढ़ी Intelligent Research Factory

`Source Repositories → Corpus → Topic Agent → AI Company Router → NVIDIA/Free Fallback → Verification → QC → Provenance → Translation → Publishing → Live Dashboard`

## Queues
- `language.hi` → Hindi agent
- `language.pa` → Punjabi agent
- `language.en` → English agent
- specialist queues are mapped through `factory/ai-companies.json`
- failed jobs move to retry states and then dead-letter state after 3 attempts

## Model routing
NVIDIA is optional. Without `NVIDIA_API_KEY`, the deterministic repository-local fallback is used. No unlimited-free-compute assumption is made.

## Truth and research policy
A source trace proves provenance, not independent truth. User-authored philosophy, hypotheses, generated text, and externally verified evidence remain distinct statuses. Research drafts require independent verification.

## Artifact identity
Every production artifact should have a stable artifact ID, SHA-256 hash, source IDs, generator, language, creation timestamp, and verification status.

## Quality gates
QC checks emptiness, schema validity, duplicate IDs/hashes, provenance presence, language metadata, and unresolved verification status before publication.
