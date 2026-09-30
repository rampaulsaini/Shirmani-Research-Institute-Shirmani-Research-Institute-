# AI / ML / NLP / Automission Agent Contracts

## Agent families

### A. User and content
- Account Agent
- Content Intake Agent
- NLP Understanding Agent
- Translation Agent
- Semantic Index Agent
- Safety / Abuse Detection Agent

### B. Discovery and marketplace
- Search Agent
- Recommendation Agent
- Creator–Audience Matching Agent
- Freelancer–Client Matching Agent
- Product Discovery Agent
- Customer Support Agent

### C. Research and education
- Claim Extraction Agent
- Evidence Discovery Agent
- Counter-Evidence Agent
- Comparative Research Agent
- Research Packet Agent
- Education Tutor Agent
- Learning Path Agent

### D. Creator and commerce
- Creator Studio Agent
- Music Workflow Agent
- Store Listing Agent
- Order/Delivery Agent
- Seller Support Agent

### E. Trust and operations
- Provenance Agent
- Audit Agent
- Fraud/Anomaly Agent
- Automission Supervisor
- Federation Agent
- Recovery Agent
- Public Status Agent

## Agent contract

Every production agent must declare:

- input schema
- output schema
- allowed tools/actions
- data classification
- confidence/uncertainty
- provenance
- escalation condition
- retry policy
- audit event
- human-review requirement
- failure-safe state

No agent may silently convert uncertainty into certainty.

## ML/NLP boundary

ML and NLP components may rank, classify, extract, cluster, translate or recommend. They must not be treated as independent scientific verification merely because a model produces a high-confidence output.
