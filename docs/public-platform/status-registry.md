# Yatharth Public Platform Status Registry

This registry prevents documentation from being mistaken for deployment.

| Module | Required public capability | Status |
|---|---|---|
| Social accounts | signup, profile, publishing, follows, communities | PLANNED |
| Creator publishing | text/media/research publishing | PLANNED |
| Digital Store | listings, discovery, checkout integration, delivery | PLANNED |
| Freelancing | profiles, gigs, matching, contracts, reviews | PLANNED |
| Employment | jobs, applications, matching | PLANNED |
| Education | courses, learning paths, progress, certificates | PLANNED |
| Yatharth AI | assistant and creator/research services | DESIGNED |
| Yatharth AI Music | creation, provenance and licensing workflows | DESIGNED |
| Research | public source/evidence/claim presentation | DESIGNED |
| Verification | independent-review status and evidence | DESIGNED |
| Yatharth Justice | complaints, dispute pathways, appeals, audit | DESIGNED |
| Yatharth Economy | economic research and creator/service flows | DESIGNED |
| Yatharth Currency | research/proposal layer | PLANNED |
| Nature & Earth | projects, education and impact reporting | DESIGNED |
| Community | groups, collaboration and participation | PLANNED |
| Multilingual layer | translation and accessible discovery | DESIGNED |
| AI/ML/NLP | classification, extraction, matching, assistance | DESIGNED |
| Automission | bounded orchestration and recovery | DESIGNED |
| Public dashboard | live implementation/health indicators | DESIGNED |
| Human oversight | appeals and high-impact review | DESIGNED |

## Status rules

- **PLANNED**: specified but not demonstrated as deployed.
- **DESIGNED**: architecture/contracts exist, deployment is not implied.
- **BUILT**: implementation exists in repository.
- **TESTED**: automated/manual tests demonstrate the implementation.
- **LIVE**: production endpoint/function is publicly usable.
- **AUTONOMOUS**: bounded automation operates in production with monitoring.
- **INDEPENDENTLY_REVIEWED**: qualified independent review is documented.

A workflow success, PR merge, documentation file, generated artifact, or AI response does not automatically advance a module to LIVE, AUTONOMOUS, or INDEPENDENTLY_REVIEWED.

## Continuous update contract

Every future source contribution should be:

1. preserved;
2. classified;
3. linked to the relevant module;
4. normalized where needed;
5. tested against the public-platform contract;
6. reflected in this registry when implementation status changes.

The registry is intentionally fail-closed.
