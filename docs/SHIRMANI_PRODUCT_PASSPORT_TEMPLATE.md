# SHIRMANI SUPREME — Product Passport Template

> Status: TEMPLATE ONLY. Replace every bracketed field with verified product-specific information before publishing. A template is not proof that a product exists, works, or has been tested.

## 1. Product identity
- Product name: [approved unique name]
- Product ID: [stable unique ID]
- Version: [semver or dated version]
- Category: [category]
- Owner/team: [responsible person/team]
- Last updated (UTC): [timestamp]
- Release state: [DRAFT / IN DEVELOPMENT / TESTING / VERIFIED / BLOCKED / RETIRED]

## 2. What it does
- One-sentence purpose: [plain-language purpose]
- Short description for product image: [brief, factual copy]
- Intended users: [specific audience]
- Supported tasks: [list]
- Not designed for: [limits / excluded tasks]
- Requirements: [device, browser, account, data, permissions]
- Known limitations: [list; write “Not yet assessed” if unknown]

## 3. Demonstration and visual proof
- Actual product screenshot URL/path: [link]
- Screenshot captured from version: [version]
- Demo video URL/path: [link]
- Demo recording date: [date]
- Demo steps shown: [numbered steps]
- Expected result: [observable result]
- Actual result: [observed result]
- Test environment: [device/browser/OS/build]
- Evidence owner: [person/team]
- Do not use concept art or a mockup as if it were a real product screenshot or a working demo.

## 4. Quick-start usage guide
1. [Step one]
2. [Step two]
3. [Step three]
4. [How to verify the expected result]
5. [How to report a problem]

## 5. Quality and test record
| Test ID | Requirement | Test method | Expected result | Actual result | Status | Evidence link |
|---|---|---|---|---|---|---|
| T-001 | Main task works | [repeatable steps] | [expected] | [observed] | NOT RUN | [link] |
| T-002 | Invalid input handled safely | [repeatable steps] | [expected] | [observed] | NOT RUN | [link] |
| T-003 | Error/limit explained clearly | [repeatable steps] | [expected] | [observed] | NOT RUN | [link] |
| T-004 | Accessibility/usability basics | [repeatable steps] | [expected] | [observed] | NOT RUN | [link] |

Allowed test statuses: NOT RUN, PASS, FAIL, BLOCKED. A test is PASS only when its evidence is attached and reviewed.

## 6. QR code rules
- Canonical passport URL: [stable public HTTPS URL]
- QR image URL/path: [generated QR asset]
- QR destination tested on: [device/browser]
- Destination matched this product ID/version: [YES/NO, evidence link]
- Last QR verification date: [date]

QR acceptance gate:
- [ ] URL is public or has the intended access permissions.
- [ ] QR scans successfully on a phone.
- [ ] Destination loads without unexpected login or error.
- [ ] Destination identifies this exact product and version.
- [ ] No secrets, private customer data, or access tokens appear in the QR URL.

## 7. Price and offer (optional; never imply approval prematurely)
- Currency and base price: [amount / NOT SET]
- Offer price: [amount / NOT SET]
- Offer start/end dates: [dates / NOT SET]
- Included deliverables: [list]
- Exclusions and usage/licence terms: [terms]
- Approval status: [DRAFT / APPROVED]
- Do not publish a price or discount until terms and delivery obligations are reviewed.

## 8. Feedback and improvement loop
- Feedback form/contact: [link]
- Review/rating source: [link]
- Feedback period: [dates]
- Number of genuine responses: [count with evidence]
- Common issues: [summarized, privacy-safe]
- Change made: [version + change]
- Regression tests rerun: [test IDs + evidence]
- Do not invent testimonials, ratings, customer counts, or sales.

## 9. Release decision
- Required tests passed: [x/y]
- Critical failures open: [count]
- Security/privacy review: [status + evidence]
- Demo matches released build: [YES/NO + evidence]
- QR resolves to this passport: [YES/NO + evidence]
- Decision: [RELEASE / HOLD]
- Reviewer and date: [name/team + date]

## 10. Public status summary
- Built: [evidence-backed statement]
- Tested: [evidence-backed count]
- Verified: [evidence-backed count]
- Known issues: [list]
- Next measurable milestone: [one specific outcome and due date]

**Release rule:** Never mark a product VERIFIED or production-ready based only on a workflow starting, a file existing, a design mockup, or an untested demo.