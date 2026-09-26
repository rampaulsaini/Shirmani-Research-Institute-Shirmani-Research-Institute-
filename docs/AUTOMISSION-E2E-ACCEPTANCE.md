# Automission End-to-End Acceptance

This document records the acceptance contract for the cross-repository automission path.

## Source

- Repository: `rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-`
- Workflow: `SHIRMANI Inter-Repository Automission Orchestrator`
- Event: `yatharth_studio_request`

## Receiver

- Repository: `rampaulsaini/yatharth-music-ai`
- Receiver workflow: `Receive Yatharth Studio Automission Request`
- Receipt path: `automation/inbox/yatharth-studio-request-<source_run_id>.json`

## Acceptance sequence

1. Source workflow validates the federation credential.
2. Source workflow dispatches the receiver event.
3. Receiver validates the source repository, source run ID, and format.
4. Receiver persists a source-run-keyed `RECEIVED` receipt.
5. Source workflow reads the receipt from the receiver's `main` branch.
6. Source validates status, source run ID, and `independent_verification_claim=false`.

## Boundary

A `RECEIVED` receipt is delivery acknowledgement only. It is not:
- scientific verification,
- human verification,
- creative completion,
- employment or payment completion,
- publication approval.

Generated artifacts remain derivatives until independently reviewed under the repository verification policy.
