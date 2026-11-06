# Yatharth Protocol v0.1 — Private Testnet Build Plan

**No live deployment, no real-value token, no public sale, no DEX, no fiat rails.**

## Repository contents

- `contracts/YatharthToken.sol` — capped ERC-20 test contract; mint permission is restricted to a timelock executor.
- `sql/001_yatharth_testnet.sql` — isolated contribution/review/allocation/governance schema.
- `../docs/economy/yatharth-protocol-v0.1.md` — protocol rules and acceptance gates.

## Local prerequisites

Use a pinned Foundry release, Solidity 0.8.24 compiler, and OpenZeppelin Contracts 5.x. Commit the exact dependency version and lockfile before running CI. Do not use production credentials or production database URLs.

## Build sequence

1. Create a disposable local Postgres database and apply only `sql/001_yatharth_testnet.sql`.
2. Start a local EVM development chain with a fresh chain ID and test-only keys.
3. Deploy a 3-of-5 Safe and a TimelockController in the local environment. Use five distinct test signer keys; do not reuse personal or production keys.
4. Deploy `YatharthToken` with the Safe as admin/pauser and the TimelockController as the sole minter.
5. Confirm initial supply is zero, lifetime cap is 100,000 YTH, decimals are 8, and no public sale/DEX contract exists.
6. Run unit and integration tests for authorization, cap, allocation replay, evidence digest, pause and timelock.
7. Run a complete simulated contribution: consent → evidence digest → three independent reviewer approvals → allocation proposal → 3-of-5 Safe approval → timelock delay → mint to a test wallet.
8. Verify database audit events against emitted contract events and transaction receipts.
9. Destroy the local chain and disposable database after evidence export.

## Required contract tests

- constructor rejects zero governance/minter addresses;
- only MINTER_ROLE can mint;
- mint amount cannot be zero;
- allocation ID cannot be zero or reused;
- evidence digest cannot be zero;
- total lifetime issuance cannot exceed 100,000 YTH;
- burning does not restore lifetime issuance capacity;
- pause blocks transfers, mint and burn;
- unpause is restricted to governance admin;
- no owner-only or public mint function exists.

## CI requirements before private testnet

- Solidity compile and unit tests;
- SQL migration apply/re-apply test on disposable Postgres;
- static analysis (Slither) and dependency audit;
- secret scanning and no production environment variables;
- deterministic build metadata and deployment manifest;
- reviewer and signer separation tests.

## Deployment restrictions

Do not deploy to a public chain or connect to a public exchange. Do not configure a public RPC, bridge, liquidity pool, price oracle, token sale or payment provider. A private testnet may still be reachable by its operators; protect RPC endpoints and test keys.

Any move beyond local/private testing requires a new explicit user decision, independent security audit, legal review for the relevant jurisdiction, and documented operational approvals. This README is a plan, not evidence that any step has run.
