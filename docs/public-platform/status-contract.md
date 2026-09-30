# Public Capability Status Contract

## States
- PLANNED — documented target; no implementation claim.
- ARCHITECTURE — interfaces/data model/workflow defined.
- MVP — runnable prototype or limited implementation exists.
- TESTED — automated or manual tests cover the stated scope.
- DEPLOYMENT_GATED — implementation exists but production dependencies are not connected.
- LIVE — an actual public production service is deployed and operational for the stated scope.
- AUTOMATED — routine operations are automated with monitoring, rollback and human escalation.
- INDEPENDENTLY_VERIFIED — a claim or result has passed its defined independent evidence/review contract.

## Required evidence for LIVE
1. reachable production HTTPS endpoint;
2. production data store and backups;
3. authentication/recovery;
4. privacy, deletion and export controls;
5. moderation and abuse handling;
6. monitoring and incident response;
7. security controls;
8. documented owner/operator and rollback path;
9. tests covering production-critical flows.

## Required evidence for AUTONOMOUS
Automated operation additionally requires explicit automation scope, safety constraints, retry/failure handling, audit logs, alerting, rollback, human escalation, and periodic review.

## Required evidence for INDEPENDENTLY_VERIFIED
Verification requires a stable claim/result identifier, operational definition, relevant independent sources or reproducible tests, counter-evidence handling, and qualified independent human review where required.

## Non-equivalence
CI success != production availability.
API success != user adoption.
Workflow completion != truth verification.
Author testimony != independent verification.
Conceptual currency design != legal/operational currency.
Architecture != deployed product.
