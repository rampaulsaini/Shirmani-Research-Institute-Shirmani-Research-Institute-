# SRI-WEB-001 — Local Business Website Builder

- **Purpose:** let a small-business owner create a responsive one-page website draft from their own business details.
- **Audience:** local shops, tutors, independent service providers, craftspeople and small organisations.
- **User workflow:** enter brand name, tagline, description, services, service area, phone and optional WhatsApp number → inspect local preview → download standalone HTML or copy its source.
- **Output:** a single responsive HTML file with business information and an optional WhatsApp enquiry link.
- **Runtime:** browser-local; no account, backend, database, analytics, remote form submission, payment gateway or hosting integration.
- **Data handling:** form values remain in the current browser page; the generated file is downloaded locally. No server upload is performed.
- **Commercial delivery:** may be offered as a website-draft/customisation service. Hosting, domain, production QA, content fact-checking, accessibility review and client-specific revisions must be separately scoped and tested.
- **Release gate:** test generated output on mobile and desktop; verify escaped user text, valid WhatsApp link, responsive layout, working download, and customer-approved content before paid delivery.
- **Truth boundary:** builder completion is not a published customer website, a received enquiry, a sale, a payment or delivery confirmation.
- **Version:** 1.0 prototype.
