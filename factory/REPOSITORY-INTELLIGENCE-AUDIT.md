# Repository Intelligence Audit — Phase 1

Generated: 2026-09-20

## Scope
The federation manifest currently contains **25 repositories**. Repository metadata checks confirmed that all 25 names resolve through the connected GitHub account.

## Confirmed integration observations

| Area | Finding | Action |
|---|---|---|
| Hub | The Research Institute repository is the central web/archive hub | Keep as orchestration layer |
| Branches | Most repositories use `main`; `rampaulsaini/omniverse--ai-scripts-` uses `base-branch-main` | Source collector must detect the remote default branch rather than assume `main` |
| Workflows | Multiple repositories already contain GitHub Actions automation | Do not duplicate existing automation blindly; inventory before federation |
| Content | Several repositories are primarily HTML/Markdown/static-site material | Treat as knowledge/content sources |
| AI/automation | `Omniverse-AI`, the Research Institute and other repos contain workflow/automation artifacts | Separate source material from executable automation |
| NVIDIA template | `NVIDIA-Omniverse/kit-app-template` resolves and is included in the federation | Treat as external reference/template source, not user-owned content |
| Research safeguards | Existing factory code labels generated papers as drafts | Preserve this boundary; generated text is not scientific validation |

## Important architecture correction

The federation should use **repository metadata + detected default branch + source classification** rather than assuming every repository has the same branch or project structure.

The next production layers are:

1. **Repository Intelligence Layer** — metadata, default branch, language/file inventory, workflow inventory, source classification.
2. **Canonical Knowledge Layer** — normalized source units with stable hashes and repository/path provenance.
3. **Agent Layer** — research, महाग्रंथ, गीत/श्लोक, paper, certificate, audio and translation agents.
4. **Quality Layer** — duplicate detection, source traceability, claim/status labels, schema validation and regression tests.
5. **Publication Layer** — controlled generation into the hub and GitHub Pages.

## Current risk

The existing generator is a useful prototype, but it should not yet be treated as a production 100,000-item publishing engine. Large output generation should be staged and resumable, and generated outputs must remain isolated from source inputs.

## Free-first constraint

The architecture can remain free-first with GitHub/GitHub Actions/open-source tooling, but GitHub-hosted compute and Pages have usage/resource limits. The system should therefore use incremental builds, caching, manifests and resumable batches rather than assuming unlimited free compute.

## Phase-1 status

- Repository resolution: complete for the current manifest.
- Default-branch discovery: started; one non-main branch already confirmed.
- Workflow/content inventory: started on representative high-priority repositories.
- Full file-level audit of all repositories: pending.
- Production agent layer: pending.
