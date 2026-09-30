# API Module Plan

The existing API foundation should grow by bounded modules rather than one monolithic endpoint.

| Module | Core resources | Primary lifecycle |
|---|---|---|
| Identity | users, profiles, sessions | create → authenticate → recover → delete/export |
| Social | posts, comments, reactions, follows | draft → publish → moderate → archive |
| Media | media assets, audio, video, live sessions | upload → process → publish → remove |
| Commerce | listings, carts, orders, entitlements | list → order → fulfil → refund/support |
| Work | services, jobs, proposals, contracts, milestones | discover → propose → execute → review |
| Education | courses, lessons, enrolments, assessments | publish → enrol → learn → assess |
| Research | sources, claims, evidence, reviews | ingest → normalize → map → review |
| Trust | reports, cases, appeals, audit events | report → triage → decide → appeal |
| AI | tasks, agents, policies, model runs | enqueue → execute → validate → audit |
| Economy | value records, payouts, currency research records | define → test → govern |
| Community | groups, memberships, events | create → join → participate |
| Nature | projects, knowledge, impact records | propose → participate → report |
| Admin | capability registry, feature flags, incidents | observe → govern → recover |

All modules should expose stable IDs, timestamps, actor identity, status, provenance and audit references where applicable.
