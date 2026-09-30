# Public Feature Status Contract

Every public feature has an explicit lifecycle:

PLANNED -> DESIGNED -> BUILT -> TESTED -> DEPLOYMENT_GATED -> LIVE -> MONITORED

## Required status fields
- feature_id
- public_name
- purpose
- owner/system
- implementation_state
- test_state
- deployment_state
- safety_state
- data_requirements
- human_review_requirement
- last_audit
- evidence_links

## Truth rule
Architecture, code, workflow success, generated content and AI confidence do not by themselves prove that a public service is LIVE or independently verified.

## User-facing states
Planned, In development, Testing, Available, Limited availability, Temporarily unavailable and Retired.

A feature must not be displayed as LIVE until its deployment gates are satisfied.
