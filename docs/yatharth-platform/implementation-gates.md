# Yatharth Platform — Implementation Gates

Gate 0 — Source: preserve requirement, user story or author source.
Gate 1 — Specification: define inputs, outputs, permissions, dependencies and failure modes.
Gate 2 — Implementation: code, data contracts, interfaces and workflows exist.
Gate 3 — Automated Test: unit, integration, contract, smoke and regression checks as applicable.
Gate 4 — Security & Privacy: authentication, authorization, minimization, secrets and abuse controls reviewed.
Gate 5 — Production Readiness: deployment, monitoring, rollback, incidents and support exist.
Gate 6 — Public Availability: capability is actually reachable through the public interface.
Gate 7 — Independent Review: required qualified independent review is obtained.
Gate 8 — Continuous Audit: behavior is monitored and improvements feed back into the lifecycle.

Fail closed: never label an unimplemented capability as live; never label author testimony as independent verification; never treat CI success as proof of a substantive claim; never allow an agent beyond its authorization scope; never expose secrets or sensitive data in logs; never make irreversible high-impact decisions solely from an unreviewed model output; preserve appeal and correction paths.

Dashboard stages: PLANNED → SPECIFIED → IMPLEMENTED → TESTED → SECURITY_REVIEWED → PRODUCTION_READY → LIVE → INDEPENDENTLY_REVIEWED → VERIFIED.
