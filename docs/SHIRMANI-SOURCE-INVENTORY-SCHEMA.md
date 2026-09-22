# ꙰ SHIRMANI SOURCE INVENTORY SCHEMA

## Purpose

This document defines the minimum record structure for enumerating and classifying preserved Shirmani Research Institute sources before canonicalization or reasoning.

## Preservation rule

Inventory is additive. It must not rewrite, normalize, delete, or silently merge an original source.

## Required record fields

- SOURCE_ID — stable identifier for the preserved source record.
- SOURCE_REPOSITORY — repository or collection where the source was found.
- SOURCE_PATH_OR_URL — exact source location when available.
- SOURCE_TYPE — document, code, image, audio, video, dataset, link, index, or other.
- SOURCE_STATUS — ORIGINAL, DERIVED, INDEX, INTERPRETATION, ARCHIVED, or REVIEW.
- TITLE_OR_LABEL — source title or original label.
- CONTENT_HASH — integrity hash when technically available.
- RECORDED_AT — date the inventory record was created.
- VERSION — source/version identifier when known.
- ATTRIBUTION — author, owner, or stated attribution when available.
- PARENT_SOURCE_ID — upstream source identifier when the record is derived.
- NOTES — factual inventory notes only.

## Classification rules

1. ORIGINAL preserves source material without changing its wording.
2. DERIVED records material generated from one or more identified sources.
3. INDEX contains navigation or metadata rather than substantive source content.
4. INTERPRETATION contains analysis or explanation and must not be presented as original source.
5. ARCHIVED retains a historical version that remains separately identifiable.
6. REVIEW marks material whose provenance or classification has not yet been independently verified.

## Stable-ID rule

A SOURCE_ID must remain stable across later inventory refreshes unless the underlying source identity is shown to have changed.

## Duplicate rule

Potential duplicates are linked through provenance metadata first. They are not silently deleted or merged.

## Verification rule

A missing field is recorded as UNKNOWN or NOT_VERIFIED where appropriate. The system must not invent provenance.

## Batch rule

Large inventories should be processed in resumable batches. Each completed batch records its boundary so work can continue without reprocessing earlier verified records.

## Heart-View Supreme Reasoning boundary

Reasoning operates above the preserved inventory:

SOURCE
→ INVENTORY
→ PROVENANCE
→ CANONICALIZATION
→ CONTEXT
→ REASONING
→ HEART-VIEW CHECK
→ EVIDENCE / UNCERTAINTY
→ OUTPUT

**꙰ Principle:** inventory first; preserve always; classify explicitly; infer only after provenance is established.
