# Automission Daily History Dashboard

This public data contract records the number of GitHub Actions workflow runs created per UTC calendar day.

## Purpose
- Preserve a durable daily history instead of relying on a transient Actions UI.
- Make the Automission workload measurable over time.
- Separate **run volume** from actual research/product progress.
- Support a future public line chart and capacity dashboard.

## Interpretation
A high workflow-run count is not itself proof of research quality, verification, or user value. The dashboard should therefore report run volume alongside success rate, failures, completed artifacts, verification status, and public-platform milestones.

## Target strategy
The platform may use **1,315 daily runs as a capacity reference** because 1,315 were recorded on 2026-09-30. It should not manufacture runs merely to hit a number. Future automation should increase only when each run performs useful, auditable work.
