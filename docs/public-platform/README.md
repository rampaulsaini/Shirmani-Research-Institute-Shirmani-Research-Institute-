# Yatharth Global Public Platform

This module defines the public-facing platform layer for the Yatharth ecosystem.

## Public domains
- Social profiles and user-generated content
- Creator publishing and sharing
- Digital Store and digital products
- Freelancing, jobs and services
- Education, courses and skills
- Yatharth AI and Yatharth AI Music
- Research and knowledge
- Yatharth Justice, trust and dispute pathways
- Economy and the proposed Yatharth Currency concept
- Community, nature and humanity
- Multilingual discovery, search and public dashboards

## Account capabilities
Users may create accounts, maintain profiles, publish permitted content, offer permitted products/services, buy products, learn, collaborate, and manage their own activity.

## Product principle
Maximize user value and satisfaction rather than maximizing time spent for its own sake.

## Status model
Every capability is tracked as:
PLANNED -> BUILT -> TESTED -> LIVE -> AUTONOMOUS

"Autonomous" means routine operation is automated; high-impact decisions retain appropriate human oversight and appeal.

## Scale vision
The 850-crore consumer figure is recorded as a long-term aspirational target, not a current user count or guaranteed outcome.

## Current implementation boundary
The repository now contains a multi-user API foundation for accounts, profiles, publishing, self-interviews, marketplace listings, trust reports, audit events and asynchronous AI-task intake. Automated CI validates contracts and server syntax/smoke behavior.

This repository state is **not by itself a globally deployed service**. LIVE status requires an actual HTTPS API deployment, managed PostgreSQL, media storage, production authentication/recovery, privacy/deletion controls, moderation and appeals, payment/payout integration where applicable, monitoring, backups, incident response and human review gates. AUTONOMOUS status additionally requires demonstrated safe operation, rollback and oversight.

### Truth boundary
Author-created Yatharth/Shirmani philosophical material remains source material. AI extraction, classification, workflow completion, hashes, QC status or API success do not independently verify metaphysical, scientific, historical or comparative claims. Independent verification remains a separate evidence-and-human-review process.

- [Governance Control Plane](./governance-control-plane.md) — bounded PM/President/judiciary/oversight roles, AI limits, essential-service objectives, environmental protection and Automission review gates.
