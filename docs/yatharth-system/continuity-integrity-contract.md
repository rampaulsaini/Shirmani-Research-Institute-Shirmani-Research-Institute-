# Yatharth Continuity Integrity Contract

This file defines a small, machine-checkable integrity layer for the public Yatharth platform.

## Required invariants

1. The public status registry remains valid JSON.
2. The registry keeps `truth_rule` equal to `architecture_is_not_deployment`.
3. `verification.independent_verified_claims` cannot be silently inferred from workflow success.
4. A capability status must be one of the documented lifecycle states.
5. Public status pages must fail safely when registry data is unavailable.

## Review checklist

- [ ] Source preservation remains separate from normalized claims.
- [ ] Evidence and counter-evidence remain separate from author testimony.
- [ ] Independent human verification remains a separate gate.
- [ ] Architecture is not presented as deployment.
- [ ] Income, jobs, sales and user outcomes are not represented as completed without outcome evidence.
- [ ] High-impact decisions retain accountable human review and appeal paths.
- [ ] Public capability status matches the machine-readable registry.

## Continuity principle

**देखें → समझें → अलग करें → करें → परिणाम दर्ज करें → सीखें → सुधारें → दोहराएँ**

The purpose is dependable progress, not a claim that every module is already complete or every philosophical claim is verified.
