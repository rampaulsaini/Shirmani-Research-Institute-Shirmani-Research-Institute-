# Autonomous Service Matrix

## Objective

Turn the public platform into an AI-native operating system while keeping high-impact decisions bounded, auditable and appealable.

| Service | AI/ML/NLP role | Automission role | Human gate |
|---|---|---|---|
| Content intake | classify, extract, translate | route | escalation |
| Search | semantic retrieval | index/update | abuse escalation |
| Recommendations | personalization | refresh | policy/audit |
| Creator publishing | metadata, quality checks | publish pipeline | restricted-content escalation |
| Marketplace | matching, ranking, fraud signals | fulfilment routing | disputes |
| Freelancing | skill/job matching | workflow orchestration | contract disputes |
| Education | tutoring, translation, learning paths | course pipeline | safeguarding |
| Music/media | generation assistance, tagging | production pipeline | rights/safety escalation |
| Customer support | triage and response | ticket routing | unresolved/high-impact cases |
| Verification | evidence extraction and consistency checks | packet generation | independent human review |
| Justice | intake, evidence organization, case routing | workflow tracking | authorized human decision-maker |
| Economy/payments | anomaly detection and reconciliation | bounded transaction workflows | regulated/financial exceptions |
| Nature | data aggregation and monitoring | alerts and reporting | domain review |
| Security | anomaly detection | incident response | critical incidents |
| Platform health | telemetry and diagnosis | recovery workflows | production escalation |

## Bounded autonomy

Automission may execute only actions explicitly permitted by a capability contract.

Every task should have:

- task ID;
- actor/service identity;
- input provenance;
- policy checks;
- allowed transition;
- output;
- audit event;
- rollback/compensation path;
- escalation path.

## Fail-closed rules

The system must stop or escalate when:

- identity or authorization is uncertain;
- evidence is insufficient for a verification claim;
- a financial action exceeds its approved boundary;
- a legal/justice decision requires authorized human judgment;
- safety policy is ambiguous;
- an external integration is unavailable;
- data integrity checks fail.

## Continuous improvement

Use production telemetry, user feedback, support outcomes, failed runs and independent audits to improve agents. Learning must not silently rewrite canonical source records or verified evidence.
