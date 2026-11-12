# Automation Consolidation — 2026-10-01

The legacy push-triggered Heart-View review jobs were removed from the cleanup branch.

## Root cause addressed
Recent failed runs passed packet generation and QC, then failed while pushing generated commits to `main`. Multiple legacy jobs targeted the same branch, producing non-fast-forward races.

## Canonical path
The `shirmani-heart-view-auto-review-conveyor.yml` remains the canonical preparation pipeline. It:
- restores the exact committed queue and registry;
- prepares one deterministic review packet at a time;
- runs fail-closed QC;
- publishes through an isolated automation branch and pull request;
- keeps human verification distinct from automated preparation.

## Quality boundary
The platform reports deterministic checks and bounded heuristics. It does not claim mathematically perfect accuracy. Evidence, provenance, uncertainty and independent verification remain explicit.

## Operational loop
Observe → Validate → Prepare → QC → Isolated publication → PR checks → Merge → Continue.
