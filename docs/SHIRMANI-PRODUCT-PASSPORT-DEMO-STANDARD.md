# SHIRMANI Product Passport, QR, Screenshot and Demo Standard
Version: 1.0
Status: Implementation specification; no product is considered complete until its evidence is attached.

## Required product identity
Every product must have:
- Unique product name, stable product ID, version, owner/maintainer, and status.
- A short plain-language description on its showroom image.
- A product-specific QR code that resolves to that product's own passport page.
- A high-quality product-specific screenshot; do not use a generic image as proof of a working product.
- A product-specific demo video (MP4 where supported) showing the actual workflow and output.
- A usage guide with prerequisites, steps, expected output, limitations, and support route.
- A changelog and test evidence.

## Showroom visual layout
1. Place the owner's supplied original photograph as the identity logo, preserving the image unchanged except proportional size adjustment.
2. Beneath the photo, show this identity line exactly:
   "Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh"
3. Place the product-specific QR at the upper-right with adequate contrast and quiet zone.
4. Show the product name, version, and short description on the visual.
5. Use a consistent, accessible layout and best-fit scaling without stretching the photograph.
6. Do not publish an identity photo or voice asset that is not actually available and authorized.

## Passport page fields
- Product ID and name
- Version and release date
- Purpose and intended users
- What it does / does not do
- Requirements and setup
- Step-by-step usage guide
- Demo video URL and screenshot
- Test cases, expected results, actual results, and evidence links
- Known limitations and security/privacy notes
- Pricing, offer terms, refund/support terms (only when approved)
- Feedback/review route and version history

## Demo video acceptance criteria
- Demonstrates the real product, not a concept animation.
- Shows input, action, output, and at least one normal-use scenario.
- Includes a failure/limitation case when relevant.
- Uses captions or a readable transcript.
- Does not expose credentials, personal data, private customer content, or secrets.
- Records product version and demo date.
- A placeholder or unrecorded video must be marked NOT AVAILABLE, never PASS.

## QR acceptance criteria
- QR target is unique to the product passport and uses a stable URL.
- Scan test succeeds on a phone and desktop destination loads.
- Destination is public or has the intended access permissions.
- Broken, duplicate, generic, or untested QR codes fail the release gate.

## Product release gate
A product may be labelled VERIFIED only when its actual functionality has been tested and evidence is recorded for screenshot, demo, usage guide, QR resolution, and core test cases. Otherwise use one of: SPECIFICATION, PROTOTYPE, IN TEST, BLOCKED, or INSUFFICIENT EVIDENCE.

## Customer feedback loop
Collect user feedback with consent; categorize defects and feature requests; reproduce issues; prioritize by impact; make a versioned change; rerun regression tests; publish the result and changelog. Do not fabricate reviews, ratings, customers, sales, or performance numbers.

## Current project status
This document defines the acceptance standard. It does not itself prove that any product, QR, screenshot, video, payment flow, or integration is implemented or tested.
