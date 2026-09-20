# Agent Orchestration

The factory is source-first.

The long-term protection charter is documented in `factory/HUMAN-CIVILIZATION-SANJEEVANI.md` and applies to the knowledge, AI, research and publication pipeline.

Repository content is collected and normalized into a canonical knowledge layer. Agents consume canonical source units and produce candidate artifacts. Generated artifacts never become canonical sources automatically.

## Pipeline

Repository Intelligence
→ Canonical Knowledge
→ Agent Selection
→ Draft Generation
→ Provenance/QC
→ Human or independent review
→ Publication

## Agent boundaries

Research, Mahagranth, Verse, Paper, Certificate, Audio and Translation agents are separate logical workers. The Quality agent runs across their outputs.

No generated research artifact is considered scientifically validated merely because it was produced automatically.

## Scaling

Large targets must be generated incrementally with manifests, hashes, checkpoints and resumable batches. A single GitHub Actions job should not be assumed to have unlimited free compute or storage.
