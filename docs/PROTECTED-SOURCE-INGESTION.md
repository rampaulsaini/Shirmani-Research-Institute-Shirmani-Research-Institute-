# Protected User Source Ingestion

This layer separates exact user-authored source material from every derivative artifact.

A historical user statement may only be marked preserved after the exact source text is actually available, captured verbatim, hashed, and linked to provenance.

## Record contract

`source_id → exact_text → language → captured_at → content_hash → provenance → derivative_links`

The SHA-256 hash is computed over the exact UTF-8 text. No normalization, translation, correction, summarization, or whitespace folding is performed before hashing.

## Status rules

- `CAPTURED`: exact source text has been ingested.
- `HASHED`: exact text has a deterministic content hash.
- `VERIFIED`: provenance and hash have passed validation.
- `MISSING_SOURCE`: a reference exists but the actual source text is unavailable.

Missing historical material must remain missing; it must never be reconstructed from memory or inferred from a derivative.

## Derivatives

Translations, summaries, interpretations, code, research formulations, and publications are downstream records. They reference protected `source_id` values and never replace the original.

## Current state

The repository now contains the preservation architecture and schema contracts. This document does not claim that every historical word from prior conversations has already been imported. Actual historical source material must be supplied through a traceable source before it can be marked preserved.
