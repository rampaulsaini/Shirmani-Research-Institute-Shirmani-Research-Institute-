# Result-First Verification Architecture

## Purpose

The platform should verify the **result of a completed operation**, not manufacture a verification decision by looking only at a workflow, a queue entry, or a direct verification flag.

The intended multi-layer path is:

**AI/ML/NLP/Automission inputs → processing → concrete result artifact → integrity/QC → independent review → reviewer decision → promotion/publication**

This preserves a strict boundary:

- workflow success = activity evidence
- generated packet = preparation evidence
- result artifact = an observable output to review
- result integrity = evidence that the output was not silently changed
- independent review = separate human/qualified review decision
- VERIFIED = a downstream decision, never an upstream shortcut

## Result-first gate

The `scripts/result_first_review_gate.py` tool checks that a concrete result artifact:

1. has a stable result ID and task ID;
2. declares an allowed result state;
3. contains a result object;
4. contains provenance;
5. has an intact fingerprint;
6. explicitly remains `UNVERIFIED`;
7. does not carry a direct verification shortcut.

A passing gate returns `READY_FOR_INDEPENDENT_REVIEW`, **not VERIFIED**.

## Multi-layer operating model

The system can run many bounded layers concurrently:

| Layer | Primary responsibility | Cannot claim |
|---|---|---|
| AI/ML/NLP | interpretation and prediction | scientific truth |
| Automission | orchestration and recovery | independent verification |
| QC | schema/integrity/quality checks | truth of a claim |
| Result-first gate | validate concrete outputs | VERIFIED status |
| Independent review | review result + evidence + counter-evidence | more than the review protocol supports |
| Promotion gate | enforce required decision/provenance fields | invent a reviewer decision |
| Publication/archive | preserve approved records | upgrade evidence |

The layers may operate in parallel, but promotion remains fail-closed.

## Operating principle

**एक काम पूरा होने पर उसका concrete result बने → result की integrity/QC हो → फिर वही result independent review में जाए।**

This allows continuous multi-task progress without confusing automation volume with verification progress.
