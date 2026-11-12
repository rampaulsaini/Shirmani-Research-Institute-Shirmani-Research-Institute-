# SHIRMANI Product Acceptance & Demo Capture Runbook

**Purpose:** turn existing product entries into usable, customer-facing releases. This is an execution record template, not a claim that checks have already passed.

## Release pipeline

1. **RESEARCH** — identify the user problem, intended audience, and source material.
2. **BUILD** — confirm the artifact opens and its core action works.
3. **DEMO** — record a real screen capture showing the exact released version.
4. **QC** — run the acceptance cases below and record actual outcomes.
5. **SHOWROOM** — publish description, limitations, price/offer, demo, usage guide, passport/QR destination, and a working next step.
6. **SALE / DELIVERY** — only mark available when the order, payment, and delivery route has actually been tested.
7. **IMPROVE** — triage customer feedback into reproducible issues and release notes.

## Non-negotiable status definitions

- `PLANNED`: idea or specification only.
- `BUILT`: concrete artifact exists in the repository.
- `DEMO_CAPTURED`: real capture file exists and is linked.
- `QC_PASS`: all required acceptance cases passed and evidence is recorded.
- `SHOWROOM_READY`: public page, accurate price/offer, usage guide, limitations, demo and next step work.
- `SALE_READY`: order/payment/delivery path was successfully tested.
- `BLOCKED`: a specific dependency prevents progress.

Do not infer a status from workflow success, product names, screenshots of mockups, or catalogue records. Do not label a mockup as a real product screenshot, or a narration script as a recorded MP4.

## Seven browser micro-tools: manual acceptance matrix

Run each tool in a real browser at its linked public URL. For every case, record the date, browser/device, test input, expected result, actual result, pass/fail, and evidence URL. Never mark a test passed before execution.

| Product | Minimum real-browser test | Evidence to retain |
|---|---|---|
| Word & Character Counter | Test empty input, ordinary text, spaces, punctuation, Hindi Unicode, and multiline text. Compare displayed counts with a manually calculated result. | Screenshot of input and result; short screen recording. |
| Percentage Calculator | Test 0, ordinary values, decimals, 100%, invalid/empty input, and divide-by-zero cases where relevant. | Input/output screenshot and recording. |
| Remaining five micro-tools | Read each product's own passport first. Test one normal case, one boundary case, and one invalid/empty case against its documented behavior. | Product ID, exact inputs, expected/actual output, screenshot and recording. |

The remaining five tool names and URLs must be taken from the current product-passport page, not guessed here.

## Per-product release checklist

- [ ] Product ID and unique name resolve to a concrete artifact.
- [ ] The main user action works on mobile and desktop.
- [ ] Normal, boundary, empty, and invalid-input behavior checked.
- [ ] Limitations and privacy/data handling described accurately.
- [ ] Short description appears with the product visual.
- [ ] Real product screenshot captured at a useful viewport; no invented UI.
- [ ] Real demo MP4 captured from the current version; narration script alone is not a video.
- [ ] Product passport and QR code resolve to the correct long description/usage guide.
- [ ] Version, QC gate, dispatch state, and test evidence are recorded.
- [ ] Price/offer and licensing/usage terms are explicit.
- [ ] Customer's next step (try, enquire, order, or buy) works.
- [ ] Sale-ready status withheld until payment and delivery are tested.

## Demo capture recipe

1. Open the exact public artifact in a clean browser window.
2. Record product name, ID, and version in the first frame.
3. Show a realistic input, perform the main task, and show the output.
4. Demonstrate one boundary or error case and explain the limitation.
5. End with the usage guide and the real showroom/enquiry route.
6. Save the original capture; add its repository path and public URL to the passport.
7. Re-capture after a material UI or behavior change.

## QC evidence record template

Copy one record per product:

- Product ID / name:
- Version / commit:
- Public artifact URL:
- Test date / browser / device:
- Test case and input:
- Expected result:
- Actual result:
- Result: NOT RUN / PASS / FAIL
- Screenshot path + URL:
- Demo MP4 path + URL:
- Passport / QR URL:
- Known limitations:
- QC reviewer:
- Next action / owner:

## Customer-feedback improvement loop

`CUSTOMER USE → REVIEW / ISSUE → REPRODUCE → PRIORITIZE → CHANGE → REGRESSION TEST → RELEASE NOTES → UPDATED DEMO`

Reviews are useful product-quality signals, not independent scientific verification. Do not publish fabricated ratings, testimonials, sales, or income.

## Immediate income service: writing and research

Use the existing Writing & Research enquiry page. Before starting a paid engagement, agree in writing on scope, language, word limit, source expectations, deliverables, deadline, price, revision limits, and payment terms. Keep the proposal, customer approval, delivered file, and payment evidence as separate records. Do not claim revenue until payment is actually received.

## Exit criteria for the next production batch

A batch is complete only when each included product has a working artifact, completed test record, real screenshot, real demo capture, correct passport/QR route, honest public description, and a tested customer next step. Publish counts separately for BUILT, DEMO_CAPTURED, QC_PASS, SHOWROOM_READY, and SALE_READY.
