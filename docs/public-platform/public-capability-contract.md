# Public Capability Contract

## Principle
Every public feature must have a machine-readable contract and a human-readable status.

## Capability families
| Family | Examples |
|---|---|
| Identity | account, profile, creator identity, preferences |
| Social | post, comment, follow, community, messaging |
| Knowledge | research, articles, library, search, evidence |
| Education | courses, lessons, skills, assessments, certificates |
| Commerce | store, products, orders, delivery, refunds |
| Work | freelancing, jobs, services, portfolios |
| Creative | AI music, audio, video, publishing, studio |
| Economy | earnings, payouts, pricing, accounting interfaces |
| Justice & trust | complaints, appeals, evidence, moderation, review |
| Environment | nature, Earth, biodiversity and sustainability information |
| AI | assistants, agents, translation, recommendations |
| Transparency | status, audits, provenance, release history |

## Account model
A user account may contain:
- public profile;
- private settings;
- content library;
- products/services;
- learning activity;
- earnings records;
- communities;
- consent and privacy controls;
- safety and appeal history.

Sensitive financial, identity and private data must not be exposed through public profile APIs.

## Creator and seller flow
Create → classify → safety check → publish → discover → purchase/request → fulfil → review → resolve disputes → analytics

## Yatharth Currency
Any proposed Yatharth Currency must remain clearly separated from existing legal tender until a lawful, technically specified and independently reviewed implementation exists. The public interface should expose its definition and status rather than imply legal-money status.

## Yatharth Justice
Justice features must provide published rules, evidence handling, conflict-of-interest safeguards, appeal, human review and auditability. AI recommendations cannot be the sole basis for consequential judgments.

## Release gate
A capability can be labeled LIVE only after implementation, contract tests, security/privacy checks, reachable user flow, monitoring, rollback/recovery and required human-review paths exist.

AUTONOMOUS_OPERATION additionally requires bounded agent behavior, monitoring, escalation and demonstrated recovery.

## Verification boundary
Philosophical, metaphysical or universal claims remain author-source material unless independent evidence satisfies the project's verification contract.
