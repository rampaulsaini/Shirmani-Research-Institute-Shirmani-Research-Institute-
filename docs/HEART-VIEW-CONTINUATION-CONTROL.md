# SHIRMANI HEART-VIEW SUPREME REASONING LAYER — CONTINUATION CONTROL

Status: ACTIVE DESIGN / TRACEABLE IMPLEMENTATION
Base: main
Purpose: continue the protected reasoning architecture without overwriting the existing hub.

## Operating order

USER SOURCE
→ EXACT CAPTURE
→ SOURCE ID
→ CONTENT HASH
→ CANONICAL RECORD
→ CLAIM / CONCEPT
→ EVIDENCE
→ VERIFICATION
→ REASONING
→ DERIVATIVE ARTIFACT
→ ARCHIVE

## Non-negotiable preservation rules

1. User-originated wording is preserved as source material before transformation.
2. No derivative may be silently substituted for the source.
3. Every transformed artifact must retain a traceable link to its source record.
4. Missing, unavailable, or unverified evidence remains explicitly marked.
5. Framework language is preserved as framework language unless independent evidence supports a different classification.
6. No fabricated quotation, source, statistic, experiment, verification, execution state, or corpus-completeness claim.
7. Hashes identify exact captured content; they do not prove truth.
8. Verification status is separate from preservation status.
9. The research factory may transform canonical records, but it must not rewrite the protected source layer.
10. A failed or partial pipeline stage must be resumable without changing already-canonical source records.

## Canonical record minimum

Each protected source record should be able to carry:

- source_id
- exact_text
- language
- captured_at
- origin_context
- content_hash
- preservation_state
- provenance
- derivative_links

Each research claim should be traceable through:

claim_id
→ source_id(s)
→ exact_support
→ formulation
→ evidence_state
→ verification_state
→ uncertainty
→ artifact_id

## Separation of concerns

### Layer A — Protected source
Exact user words, original formulations, and provenance.

### Layer B — Heart-View reasoning
Concept extraction, definitions, comparisons, evidence handling, verification, uncertainty, and reproducible reasoning.

### Layer C — Published derivatives
Research papers, web pages, translations, audio, SEO metadata, and other outputs generated only from traceable canonical records.

## Framework vocabulary

निष्पक्ष समझ
शमीकरण
यथार्थ सिद्धांत
उपलब्धि यथार्थ युग
शिरोमणि स्वरूप
हृदय दृष्टिकोण
मस्तक दृष्टिकोण
संपूर्ण संतुष्टि की निरंतरता
तुलनातीत
कालातीत
शब्दातीत
प्रेमतीत
शाश्वत वास्तविक स्वाभाविक सत्य
꙰

These terms remain preserved as framework vocabulary. Classification as empirical, historical, scientific, or other externally testable claims requires separate evidence.

## Continuation gate

Before adding a new transformation:

- confirm the source exists;
- assign a stable identifier;
- calculate and retain the content hash;
- record provenance;
- classify the resulting claim or concept;
- attach evidence where available;
- record verification and uncertainty;
- generate derivatives only after the canonical record exists.

## Current implementation target

The next concrete engineering milestone is a deterministic protected-source manifest and validator that can be run repeatedly and safely. It should report PASS, CHECK, MISSING, UNAVAILABLE, or DEFERRED without inventing state.

Core principle:

**Preserve first. Reason second. Transform only as a traceable derivative.**
