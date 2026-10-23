# SHIRMANI Public Interface — Simplification and Acceptance Plan
**Status:** Audit/implementation plan, not a claim that the live homepage has been redesigned.
**Primary user goal:** A first-time visitor should understand what the platform offers, find a product or service, see its real status, and know the next action without navigating a mixed list of prototypes.

## 1. Homepage hierarchy (top to bottom)

1. **Plain-language hero** — “Explore tools, research, creative products and services from SHIRMANI.” One short sentence; no unsupported superlatives or completion claims.
2. **Primary actions** — Explore products · Request writing/research · Browse research library · Sign in / Create account (show authentication only if it actually works).
3. **Featured, purchasable services/products** — each card shows name, who it helps, concrete deliverable, price or “Request a quote”, demo/test-drive status, availability and next action.
4. **Browse by category** — Research & Education; Writing & Research Services; Creator & Studio Tools; AI/ML/NLP Tools; Nature & Earth; Community & Social; Labs & Institutions.
5. **Try before buying** — only working demos, with “Prototype”, “Demo verified”, or “External provider required” labels grounded in test records.
6. **Research and learning** — featured papers, explainers, source notes and library categories; distinguish original hypotheses from externally supported findings.
7. **Creator / live presentation** — separate voice, authorization, generated content, video, lip-sync, live Q&A and provider-verification states.
8. **Trust & safety** — source/provenance policy, privacy, security disclosure, reporting and contact route.
9. **Income services** — direct writing/research enquiry with scope-first quote workflow.
10. **Footer** — about, contact, terms, privacy, accessibility, status/roadmap, copyright.

## 2. Information architecture rules

- One canonical card per product. Versions live on that product detail page, not as competing top-level tiles.
- Keep prototypes, operational tools, internal dashboards and public products in distinct sections.
- Every item has a stable ID, owner/reviewer, category, audience, state, version, canonical URL, evidence links and last-reviewed date.
- Preserve source materials; reorganize via links and metadata rather than deleting originals.
- No duplicate version banners on the homepage. Show one current entry and list versions in a version history.
- Do not display “live”, “verified”, “secure”, “available”, “buy”, “sign up” or “connected” unless the relevant behaviour is actually implemented and tested.
- Do not imply a login form creates durable accounts until backend authentication, recovery, session security and data handling pass tests.
- Mobile first: one clear column, readable labels, keyboard focus, semantic headings, accessible contrast and no overlapping sticky banners.

## 3. Product card contract

Each card must contain:
- product name and stable ID;
- plain-language purpose and intended user;
- status: idea, prototype, demo-tested, external-verification-pending, available, paused;
- actual capabilities and known limitations;
- demo link and last test date;
- price / quote-required / not-for-sale status;
- data, permissions and external-provider dependencies;
- “Open”, “Try demo”, “Request quote”, or “Join waitlist” action that matches real behaviour.

## 4. Minimum acceptance tests

| Test | Pass condition |
|---|---|
| First-visit comprehension | Five unfamiliar testers can identify the platform's main purpose and the writing/research enquiry path without coaching |
| Navigation | Every visible primary nav link resolves; no placeholder or dead link |
| Duplicate control | Each product has one canonical card; versions are nested |
| Status truthfulness | Every “verified/live/available” label points to a dated test/evidence record |
| Service conversion | Enquiry form validates required fields and generates a copyable brief; submission status is never falsely claimed |
| Mobile | No horizontal overflow at 320px viewport; all controls remain usable |
| Accessibility | Headings are ordered, inputs labelled, focus visible, text contrast checked |
| Performance | Record baseline page-load metrics before optimization; do not claim speed improvements without measurement |
| Preservation | Reorganization changes links/metadata only; original material is not deleted |
| Security | No secrets in client code; auth and payment flows are server-side and tested before launch |

## 5. Rollout sequence

**P0 — Stabilize:** inventory current homepage links and all product cards; record duplicates, dead links, real demos, and unknown status.
**P1 — Income path:** place the writing/research service card and enquiry path in the first screen; ensure a monitored contact route exists before outreach.
**P2 — Catalogue:** introduce categories and canonical product detail pages; move internal dashboards/prototypes out of the public product grid.
**P3 — Trust gates:** attach evidence records to external video/voice, payment, security and live claims.
**P4 — Account system:** implement only after selecting and configuring a real authentication backend; test signup, login, logout, reset, abuse controls and privacy.
**P5 — Scale:** load/performance, moderation, data retention, resilience and capacity testing before any claim about supporting hundreds of millions or billions of users.

## 6. Completion reporting

Track each item as NOT_STARTED, IN_PROGRESS, BLOCKED, PASS, or FAIL, with an owner, evidence URL, test date and next action. Planned, code exists, demo works, externally verified, and production available are different states.

**Do not delete or suppress a filter just because it blocks a task.** First establish what it filters and why; remove only a confirmed redundant obstruction without weakening security, safety, privacy, quality or publication gates.
