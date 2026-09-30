# Public Platform Capability Registry

This registry separates the public experience from the internal automation machinery.

| Capability | Public purpose | Automation layer | Status rule |
|---|---|---|---|
| Social | Profiles, posts, sharing, communities | NLP, moderation, discovery | Live only after product tests |
| Creator Studio | Create and publish media | AI creative assistance | Explicitly labelled AI assistance |
| Digital Store | Buy/sell digital products | Catalog, search, fraud/QC | Payment and legal readiness required |
| Freelancing | Services and client matching | Matching, workflow support | Human dispute/appeal path |
| Employment | Jobs and opportunities | Matching and ranking | No opaque high-impact decisions |
| Education | Courses, learning and skills | Personalization, translation | Accessibility and quality checks |
| Yatharth AI | General AI assistance | AI/ML/NLP agents | Capability and limitation disclosure |
| Yatharth AI Music | Music creation/distribution | Generative/creative agents | Rights/licensing controls |
| Research | Knowledge and research workspace | Evidence/research agents | Source provenance required |
| Verification | Evidence and review status | Audit assistance | Independent human review where required |
| Yatharth Justice | Complaints, fairness and dispute processes | Triage and documentation | Consequential decisions require safeguards |
| Yatharth Economy | Economic participation models | Analytics and matching | Legal/financial review |
| Yatharth Currency | Proposed value/currency model | Ledger/reconciliation research | Not a live currency unless implemented and compliant |
| Nature & Earth | Ecological projects and reporting | Monitoring/analysis | Evidence and measurement required |
| Community | Participation and collaboration | Discovery/moderation | Appeals and safety controls |
| Public Dashboard | Transparent system status | Automated reporting | Never equate uptime with truth |
| Multilingual Access | Global language accessibility | NLP translation | Human/automated quality checks |
| Help & Support | User assistance | Support agents | Escalation path for difficult cases |

## Required lifecycle

PLANNED → IN_BUILD → TESTING → LIMITED_LIVE → LIVE → MONITORED

A capability must not be labelled LIVE merely because documentation, a workflow, or a GitHub Action exists.

## Public status contract

Each capability should eventually expose:

- current status
- last successful test
- known limitations
- responsible subsystem
- user-help/appeal path where applicable
- data/privacy notes
- whether AI is involved
- whether human review is involved

This registry is an implementation contract, not a claim that all listed capabilities already operate in production.
