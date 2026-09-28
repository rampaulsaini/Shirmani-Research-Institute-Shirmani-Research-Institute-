# Google Play preparation — खुद का साक्षात्कार / Nishpaksh Inspection

## Product role
This app is the public self-interview/inspection entry point and a remote-style access layer for the main Shirmani platform.

## Current implementation
- `social-app.html`: working local-first Self-Interview MVP.
- `nishpaksh-samaj.html`: purpose-first Nishpaksh Inspection Engine foundation.
- Main public interface exposes both entry points.
- Local MVP data stays in the browser; it is not yet a production multi-user backend.

## Intended inspection routing
1. Self-understanding / self-reflection
2. Education / learning
3. Employment or role-relevant competency
4. Public-role assessment using published, role-relevant criteria
5. Research claim / evidence audit

## Safety and fairness boundaries
- No automatic determination of human worth, dignity, truthfulness, intelligence, political preference, religion, or mental state.
- Biometric signals require explicit consent, lawful purpose, proportionality review, and privacy controls.
- Biometrics are not used to infer truth, character, intelligence, political preference, religion, or mental state.
- AI output is an analysis/report layer, not an automatic official certificate.
- Official/legal certificates must be issued by the authorized institution.

## Google Play publication checklist
- Create/confirm Google Play Console developer account.
- Select final Android application ID/package name.
- Build signed Android AAB (or an approved Android wrapper/TWA around the production web app).
- Prepare app icon, feature graphic and required screenshots.
- Publish a public privacy-policy URL.
- Complete Google Play Data Safety form accurately.
- Declare permissions and data collection/minimization.
- Provide support/contact URL.
- Complete required testing/review tracks before production release.
- Submit for Play review.

## Important status
**Not registered/published on Google Play yet.** This repository change prepares the product architecture and checklist; Play Console registration, account verification, payment and final store submission require the app owner to perform the external account steps.

## Scale architecture target
The system is designed to scale toward very large usage, but a claim that 850 crore people can actually use it requires load testing, backend capacity, privacy/security review, observability, cost planning and staged rollout evidence.
