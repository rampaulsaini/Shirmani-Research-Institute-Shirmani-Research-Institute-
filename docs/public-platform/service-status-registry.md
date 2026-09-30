# Public Platform Service Status Registry

This registry prevents the public interface from presenting architecture as a live service.

## Status vocabulary

- PLANNED — documented objective; implementation not established.
- IN_DEVELOPMENT — implementation work exists but is not production-ready.
- TESTED — automated tests pass for the defined scope.
- LIMITED_PREVIEW — available only to a controlled audience or environment.
- LIVE — deployed, reachable, monitored, and documented for public use.
- AUTOMATED — bounded automation is operating; this is not itself a production-status claim.
- HUMAN_REVIEWED — a qualifying human review has occurred for the specific artifact/action.
- INDEPENDENTLY_VERIFIED — only when the defined independent verification contract is satisfied.

## Required service record

Every public capability should expose:

1. service_id
2. owner/system boundary
3. user-facing description
4. current status
5. deployment location
6. last tested timestamp
7. automation scope
8. human-review requirements
9. privacy/data category
10. safety/risk class
11. complaint and appeal path
12. evidence/provenance links
13. rollback/recovery path

## Initial service families

| Service family | Intended capability | Default status |
|---|---|---|
| Accounts & profiles | registration, profile, privacy and preferences | IN_DEVELOPMENT |
| Social | posts, comments, communities, messaging | IN_DEVELOPMENT |
| Creator publishing | articles, audio, video, music and research | IN_DEVELOPMENT |
| Digital Store | digital products, licensing and subscriptions | IN_DEVELOPMENT |
| Freelancing & Jobs | service listings, matching and work tracking | IN_DEVELOPMENT |
| Education | courses, learning paths and certificates | IN_DEVELOPMENT |
| Research | source, claim, evidence and comparison layers | IN_DEVELOPMENT |
| AI/ML/NLP | bounded agent assistance and semantic services | IN_DEVELOPMENT |
| Yatharth AI Music | creation, publishing and licensing | IN_DEVELOPMENT |
| Yatharth Justice | complaints, evidence, appeals and human review | PLANNED |
| Yatharth Currency | research/concept layer subject to legal review | PLANNED |
| Nature/Earth | conservation information and impact reporting | PLANNED |
| Public Dashboard | service and verification transparency | IN_DEVELOPMENT |

No row may be changed to LIVE merely because a GitHub workflow succeeds.
