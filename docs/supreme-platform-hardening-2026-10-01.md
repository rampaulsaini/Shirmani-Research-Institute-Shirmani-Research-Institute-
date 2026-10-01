# SHIRMANI Supreme Platform Hardening — 2026-10-01

## Objective

Make the Research Institute faster to operate, easier to verify, and more resilient by reducing duplicated automation, enforcing fail-closed quality gates, and keeping research claims separate from measured evidence.

## Changes

### Review-workflow consolidation

The repository previously contained 42 separate Heart-View review workflow files for fixed 25-record ranges. They are consolidated into:

- `.github/workflows/heart-view-review-conveyor.yml`

The conveyor accepts a batch size and resumable offset, validates controls, builds one review packet, runs packet QC, and publishes the artifact.

### Fail-closed consensus repair

`factory/supreme_ai_ml_nlp_engine.py` now requires at least two records before the multi-agent ensemble can return `CONTINUE_AUTOMISSION`. A single record is insufficient evidence for ensemble consensus.

### Failure intelligence retained

`failure-intelligence.yml` is retained because it is a diagnostic collector, not a failure-producing workflow. Removing it would remove useful failure evidence.

### Accuracy semantics

The platform does not claim mathematically perfect or universal AI accuracy. It reports deterministic checks, heuristic scores, evidence status, verification status, and uncertainty separately.

## Target operating loop

`Observe → Collect → Normalize → Analyze → Reason → Execute → Test → Verify → Audit → Learn → Improve`

High-impact or irreversible actions remain subject to authorization and verification boundaries.

## Verification boundary

This hardening branch can verify repository-local tests and syntax. GitHub Actions run history, secrets, Pages deployment, external services, production infrastructure, and legal status cannot be marked live solely from repository source.

## Global identity boundary

The platform can provide a public research identity, evidence passport, authorship archive, multilingual presence, and global participation surfaces. Those are distinct from legal citizenship or government-issued nationality, which cannot be created by a GitHub repository or AI system.
