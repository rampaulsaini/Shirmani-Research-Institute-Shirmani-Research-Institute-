# Income Opportunity Research

## Current state

The research layer is deliberately **source-gated**. It does not fabricate opportunities and it does not treat estimates as income.

### Flow

SOURCE → INTAKE → STRUCTURAL QC → UNVERIFIED QUEUE → HUMAN/SOURCE VERIFICATION → APPROVAL → EXECUTION → EVIDENCE → ACTUAL INCOME

### Rules

1. Every opportunity must retain a source URL and discovery timestamp.
2. Intake may normalize records but may not upgrade verification or approval.
3. New records enter as `UNVERIFIED` and `PENDING`.
4. Estimated value is not actual income.
5. Financial transactions, external-account actions, publication, contracts, and commitments remain human-approved actions.
6. Invalid source records are rejected and retained for audit.
7. Placeholder records are scaffolding only and must be replaced with real sources before execution.

### Life-support priority

Research should be ordered around the existing Income Command Center priorities:

1. Employment & Work
2. Freelancing
3. AI Marketing
4. Digital Store
5. Yatharth AI Music
6. Economic Vision

No opportunity is executable merely because it appears in the queue.
