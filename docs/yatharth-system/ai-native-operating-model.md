# AI-Native Operating Model

## Agent layers
- Intake Agent: accepts and normalizes user/content events.
- NLP Agent: language detection, extraction, semantic indexing, translation.
- Safety Agent: spam, abuse, fraud and policy triage.
- Discovery Agent: search, recommendation, matching and personalization.
- Creator Agent: assists writing, audio, music, media and product preparation.
- Commerce Agent: catalog, order-state assistance, customer-support routing and anomaly detection.
- Education Agent: course discovery, learning-path assistance and tutoring support.
- Research Agent: claim extraction, evidence mapping and comparative research.
- Verification Gate: keeps author-source, evidence, independent review and verified status separate.
- Automission Supervisor: schedules, observes, retries, escalates and audits workflows.
- Federation Agent: coordinates approved work across repositories/services.
- Public Presentation Agent: publishes only contract-compliant public status and content.

## Machine-learning responsibilities
ML components may support ranking, classification, anomaly detection, semantic similarity, recommendation, fraud signals, demand forecasting, and quality prediction. Model outputs remain probabilistic and require monitoring for error, drift, bias, and unsafe behavior.

## NLP responsibilities
NLP must support multilingual ingestion, entity/concept extraction, claim segmentation, sentiment/context where appropriate, translation, semantic search, duplicate detection, contradiction candidates, and structured metadata generation.

## Fail-closed controls
No model output alone may:
- declare a contested author claim scientifically verified;
- determine criminal/civil guilt;
- make irreversible account sanctions without the defined review path;
- execute uncontrolled financial actions;
- expose private user information;
- bypass platform safety or applicable law.

## Human oversight
Human review remains available for high-impact moderation, disputes, appeals, legal/financial decisions, independent verification, and safety incidents. Automation should reduce routine workload rather than remove accountability.

## Operational telemetry
Every agent should emit traceable event IDs, model/version metadata where relevant, input/output classification, confidence where meaningful, decision source, retry state, and escalation state without leaking sensitive information.

## Success measures
Track availability, latency, task completion, false-positive/false-negative rates, user satisfaction, complaint resolution time, accessibility, safety incidents, evidence quality, verification progress, and cost per successful task.
