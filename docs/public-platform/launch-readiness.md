# Launch Readiness Contract

A module may be called production only when its implementation and operational evidence satisfy the relevant gates.

## Minimum gates

- Functional API/UI path exists.
- Authentication and authorization are enforced.
- Input validation and error handling exist.
- Tests cover normal and failure paths.
- Audit events exist for consequential changes.
- Privacy and data-retention behavior is documented.
- Abuse/moderation controls exist where user-generated content is involved.
- Payment/security controls exist where money is involved.
- Accessibility and mobile behavior are checked.
- Monitoring and rollback procedures exist.
- Human escalation exists for high-impact decisions.
- Public status is truthful: no “live” or “verified” label without evidence.

## Readiness labels

architecture — contract/design exists.

in_build — implementation is actively being added.

testing — implementation exists and automated checks are running.

beta — controlled real-user testing with explicit limitations.

production — operational requirements and release evidence have been satisfied.

verified_research — a research claim has passed its independent verification contract; this is not a software release label.

## Dashboard rule

Show separate metrics for:
- code/feature completion
- automated test health
- operational readiness
- research verification

Never combine them into one percentage.
