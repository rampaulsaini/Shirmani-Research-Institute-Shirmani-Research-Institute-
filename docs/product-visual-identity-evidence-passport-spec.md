# Product Visual Identity & Evidence Passport
**Project:** Shirmani Research Institute  
**Status:** Specification drafted; visual assets and live integrations remain unverified  
**Date:** 2026-10-11

## Purpose
Give every real tool or product a distinct, understandable public identity. Every card must explain the use in plain language and let a visitor inspect a demo, a detailed passport, and evidence before purchase. Do not describe planned features as already working.

## Product-card visual standard
- Responsive 16:9 or 4:3 preview image, high-contrast text, readable at mobile width.
- Product's finalized display name and one-line plain-language benefit.
- Short description on the image; keep it brief enough to read without zooming.
- Owner-provided “impartial understanding” portrait as a small, consistent logo, once the exact original image file is supplied and approved. Never synthesize or substitute the portrait.
- QR code at the upper-right linking to that product's stable public passport URL. Generate QR from the actual URL; never use a decorative/fake QR.
- Clear state: **Demo available**, **Prototype**, **Planned**, or **Verified**. Use “Verified” only after the stated tests pass.
- Alt text, accessible contrast, image dimensions and source/licence recorded.

## Required product passport
Each product record should contain:
1. Stable product ID and version.
2. Finalized name, category, status, owner and last-updated date.
3. What it does / does not do, intended users and prerequisites.
4. Step-by-step usage guide in simple Hindi and English.
5. Working demo video URL, or explicit “Demo not yet available”.
6. VIP screenshot / product preview URL, or explicit “Screenshot pending”.
7. Test plan, dated test results, evidence links, limitations and known issues.
8. Price and scope only when actually approved; no invented pricing, testimonials, sales, or income.
9. Support/contact route, privacy notes, accessibility notes and changelog.
10. Customer feedback fields and a documented review → triage → fix → retest loop.

## Demo and release gate
A product is publishable as a sale-ready item only when its card, passport, real QR, usage guide, demo (or an explicitly labelled demo-pending prototype), and test status agree. The production-ready gate requires:
- [ ] The public URL resolves on mobile and desktop.
- [ ] QR scans to the exact passport URL.
- [ ] Preview accurately represents the current product.
- [ ] Demo shows a real workflow and labels mock data.
- [ ] All claims are linked to evidence or marked as goals.
- [ ] Accessibility and basic security checks pass.
- [ ] Price, deliverables, refund/support terms are visible before checkout.
- [ ] No user photo, voice, face, or likeness is used without the user's explicit asset authorization.

## Character and communication policy
The presentation persona should communicate in a simple, respectful, transparent way; adapt vocabulary to the audience without stereotyping. Separate personal/philosophical statements from independently verified scientific claims. Cite reliable sources for factual claims and say **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है”** when evidence is insufficient. Never demean a person or community to claim superiority.

## Catalog scaling
Use a structured manifest (JSON/YAML or database) as the single source of truth for cards and passports. For a 150,000-item catalogue, use paginated/sharded indexes, stable IDs, search filters, image/CDN variants, lazy loading, and automated link/QR validation. Do not manually duplicate the same metadata in each page.

## First income-oriented release
Start with the already stated services: Hindi/English writing, research summaries, and website/blog content. The enquiry form must gather topic, audience, language, word range, deadline, source links, and budget. Confirm scope, price, deliverables, timeline, and payment terms in writing before work starts. Track enquiries, qualified leads, quotes sent, accepted jobs, completed deliveries, and actual payments separately. A visit, email draft, workflow run, or quote is not a sale or income.

## Asset and implementation blockers
- Exact owner-approved portrait/logo image is required to render the requested face faithfully.
- Each product needs a real stable passport URL before its QR can be generated.
- Each demo video and VIP screenshot must be supplied or captured from a functioning product; do not fabricate proof.
- Email, messaging, payment, social-media and voice-provider integrations require authorized accounts, credentials, consent, and end-to-end tests. Do not claim that outreach or live voice/lip-sync works before a successful test.

## Acceptance metrics
Report measured counts only:
- products with unique IDs / total products;
- cards with portrait logo / total published cards;
- valid QR links / QR links checked;
- passports complete / published products;
- working demos / products requiring demos;
- mobile/desktop checks passed;
- enquiries received, quotes accepted, jobs delivered, payments actually received.
