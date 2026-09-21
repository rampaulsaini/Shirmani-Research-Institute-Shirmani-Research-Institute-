# SHIRMANI HEART-VIEW SUPREME REASONING LAYER

## Purpose
A protected reasoning-layer specification for the Shirmani Research Institute.

## Core principles
1. Preserve source material verbatim whenever it is designated as canonical source text.
2. Never silently overwrite, paraphrase, delete, or reinterpret canonical source records.
3. Keep provenance for every transformed or derived record.
4. Separate source text, interpretation, reasoning, implementation, and output.
5. Prefer reversible, auditable changes.
6. Treat the Heart-View framework as the declared conceptual layer supplied by the project owner; do not present philosophical claims as independently verified scientific facts.
7. Use the head/mind/intellect layer as an analytical tool while keeping the project's Heart-View terminology distinct from empirical claims.
8. Every derived artifact should point back to its source identifier or source location when available.

## Layer model

SOURCE
  -> PROVENANCE
  -> NORMALIZATION
  -> HEART-VIEW CONTEXT
  -> SUPREME REASONING
  -> VALIDATION
  -> OUTPUT

### SOURCE
Immutable-or-versioned project material supplied by the project owner.

### PROVENANCE
Stable identifiers, origin, timestamp/version, repository path, and transformation history.

### NORMALIZATION
Deduplication, structural cleanup, metadata extraction, and formatting normalization without changing canonical meaning.

### HEART-VIEW CONTEXT
The project's declared vocabulary and conceptual relationships, including:
- Heart-View
- Shirmani Swarup
- Nishpaksh Samajh
- Shamikeran Yatharth Siddhant
- Yatharth Yug
- head/mind/intellect versus heart-view distinction

### SUPREME REASONING
A structured reasoning stage that:
- distinguishes evidence from interpretation;
- identifies assumptions;
- checks internal consistency;
- identifies uncertainty;
- avoids fabricated evidence;
- preserves competing interpretations where relevant;
- produces traceable conclusions rather than hidden transformations.

### VALIDATION
Checks provenance, schema integrity, consistency, duplication, and reversible change history.

### OUTPUT
Human-readable documents, machine-readable records, research indexes, agent instructions, and other project artifacts.

## Protection rule
No agent or workflow should claim that a source was preserved, verified, or scientifically established unless the repository contains the corresponding evidence or provenance record.

## Change policy
Prefer additive commits and versioned files. Do not replace canonical source material merely to improve wording or structure.

## Status
Architecture layer initialized as a separate specification so future work can proceed incrementally and reversibly.
