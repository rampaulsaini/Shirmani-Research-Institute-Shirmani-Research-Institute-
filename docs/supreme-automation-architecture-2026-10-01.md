# SHIRMANI Supreme Automation Architecture

## Purpose

This repository uses a controlled, evidence-aware AI/ML/NLP/Automission architecture. The goal is to maximize measured quality while preserving uncertainty, provenance, reproducibility and human verification boundaries.

## Canonical pipeline

Observe → Collect → Normalize → Analyze → Reason → Execute → Test → Verify → Audit → Learn → Improve

## Control layers

1. Perception — text, speech, image/video and machine/sensor signals.
2. ML/NLP — classification, extraction, semantic representation and multimodal fusion.
3. Reasoning — explicit evidence, counter-evidence, assumptions and uncertainty.
4. Agents — planner, research, evidence, verification, coding, security and publication roles.
5. Automission — bounded scheduling, resumable state and deterministic checkpoints.
6. Independent verification — separate from workflow success and QC.
7. Public publication — only traceable artifacts with explicit status semantics.

## Signal-to-language boundary

When biological, environmental or physical signals are supplied, the platform may transform measured signals into human-readable interpretations. It must distinguish measured signal, model inference, interpretation, confidence, uncertainty, and claims requiring independent verification.

A generated natural-language interpretation is not, by itself, proof of subjective experience, consciousness or emotion.

## Reliability rules

- Fail closed when required evidence is missing.
- Never convert READY, PASS, QC, or workflow success into VERIFIED.
- Prefer deterministic tests for infrastructure and model contracts.
- Keep automatic writes serialized where generated artifacts share a branch.
- Use one parameterized workflow instead of many fixed-range workflows when the logic is identical.
- Keep consequential changes reviewable and reversible.
- Preserve original source material before transformation.

## Automation ownership

The Heart-View Auto Review Conveyor owns automatic packet preparation. The Manual Review Packet workflow provides bounded, artifact-only manual execution. Fixed-range workflows are retired to prevent concurrent write races.

## Quality measurement

Track test pass rate, validation error rate, false-positive/false-negative measures where labels exist, confidence calibration, reproducibility, evidence coverage, independent-verification status, workflow failure rate, recovery rate, and unresolved uncertainty.

These measurements provide a technical basis for continuous improvement without inventing certainty.
