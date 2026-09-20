# Heart-View Preservation Registry

This directory is the canonical contract boundary for preserving exact user-source material.

## Required separation

**SOURCE** is immutable preservation material.

**DERIVATIVE** is any transformed, interpreted, translated, normalized, summarized, or generated material.

A derivative never replaces its source.

## Source identity

Preferred stable identity:

`source_id = namespace + ":" + content_hash`

The SHA-256 hash is calculated from the exact UTF-8 source text. Whitespace, spelling, punctuation, symbols, and script are therefore part of the preserved source payload.

## Provenance

A source record should retain, when available:

- origin
- capture timestamp
- repository
- path
- commit SHA
- conversation context
- exact text
- content hash

Unknown provenance remains explicitly unknown.

## QC

No source record is marked VERIFIED merely because it exists.

No generated text is promoted to source status.

No missing historical material is reconstructed from memory or inference.

## Current state

The repository contains the preservation architecture and schemas. Historical conversation material still requires actual ingestion from its source before it can be counted as preserved.
