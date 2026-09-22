# SHIRMANI HEART-VIEW SUPREME REASONING LAYER

## Continuous execution architecture

This repository is the central orchestration point for the Shirmani Research Institute federation.

### What is now real

- A repository federation manifest is stored in `automation/repository-manifest.json`.
- An idempotent task queue specification is stored in `automation/queue/tasks.json`.
- A GitHub Actions audit worker is installed at `.github/workflows/shirmani-continuous-audit.yml`.
- The worker runs on push/manual dispatch and on a 5-minute schedule.
- The worker audits every currently discovered owned repository in parallel.
- The first layer is deliberately read-only: it inventories commits, branches, workflow presence, repository visibility, and basic source statistics.
- Every audit produces a timestamped JSON result as a workflow artifact.

## What is deliberately NOT automatic yet

The system does not automatically modify or delete files in the federation. Cross-repository writes require explicit GitHub authentication with permissions covering those repositories.

The GitHub Actions `GITHUB_TOKEN` is scoped to the repository that owns the workflow; it is not a universal credential for changing other repositories. A GitHub App or appropriately scoped token is required for cross-repository writes.

AI-model execution is also kept behind a separate credential boundary. No API key is embedded in source code.

## Continuous execution model

1. Scheduler starts the audit worker.
2. Matrix workers inspect repositories concurrently.
3. Each worker emits an immutable audit result.
4. Queue tasks remain idempotent and can be retried.
5. Later layers can consume these results for reasoning, classification, indexing, and controlled change proposals.
6. Any write layer should use branch + validation + pull-request gates before merging.

## Safety invariant

**Preserve source -> observe -> index -> reason -> propose -> validate -> approve -> apply.**

No layer should silently replace the source corpus.

## Current federation discovery

The authenticated GitHub listing currently exposes 24 repositories owned by `rampaulsaini`. The previously stated federation size is 25, so one target repository remains to be identified before claiming full 25-repository coverage.

## AI / Supreme Reasoning Layer

The architecture reserves a model-agent layer for source classification, canonicalization proposals, provenance linking, duplicate detection, contradiction detection, task decomposition, queue prioritization, and validation reports.

Those capabilities become genuinely autonomous only after a model provider and credentials are deliberately configured. The system will not invent or assume credentials.
