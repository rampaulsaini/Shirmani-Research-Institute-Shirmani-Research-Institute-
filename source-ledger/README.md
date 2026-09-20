# ꙰ Protected Source Ledger

This directory is the canonical boundary for exact user-source records.

## Rules

- A source record contains the exact captured text, not an AI rewrite.
- Each record receives a stable `source_id` and SHA-256 content hash.
- Provenance identifies where and when the source was captured.
- Derivatives point back to source records; source records never point to derivatives as their authority.
- Historical material that has not been captured from its actual source remains `PENDING_CAPTURE` or `UNAVAILABLE`.
- Do not claim that the entire historical conversation corpus is preserved until records exist for that corpus.

## Record flow

`exact user words → source record → canonical unit → claim/concept → evidence → verification → derivative`

The repository's existing evidence-first contract in `PROJECT-CONTINUITY.md` remains in force.
