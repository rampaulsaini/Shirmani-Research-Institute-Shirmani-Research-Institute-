# Omniverse Research Factory — Unified Architecture

## Roles

- **Shirmani Research Institute** — public research/archive website and factory control-center presentation.
- **Omniverse-Platform** — central automation/orchestration layer.
- **Federated repositories** — specialized research, publishing, store, marketplace and AI projects.

## Execution flow

Research or customer input → queue/intake → deterministic agent routing → specialist factory → QC gate → review when required → delivery/publishing → audit/provenance.

## Current automation layers

The central platform contains:
- queue orchestration
- freelance service factory
- ecommerce preparation factory
- specialist agent router
- deterministic QC gate
- delivery bundling
- continuous GitHub Actions workflow
- automation health/smoke tests

## Public-status rule

The Research Institute dashboard may display generated status artifacts from the federation. It must not invent live counters or imply that a registered agent is a continuously running external AI service.

## Safety and integration rule

External marketplaces, payment providers and other services are enabled only through permitted official APIs/OAuth/webhooks or approved integrations. Secrets stay in repository/environment secret storage. Refunds, disputes, regulated work and irreversible financial actions remain approval-gated.

## Free-first principle

The default architecture uses GitHub, GitHub Actions, Python and deterministic/local components. External paid services are optional and must not be represented as free unless their current terms actually support that use.
