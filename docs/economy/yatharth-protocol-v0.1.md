# Yatharth Mudra Protocol v0.1 — Private Testnet Only

**Status:** DESIGN / TESTNET SPECIFICATION — NOT DEPLOYED  
**Ticker:** YTH (proposed)  
**Maximum lifetime issuance:** 100,000 YTH  
**Initial supply:** 0 YTH  
**Decimals:** 8  
**Governance:** 3-of-5 independent multisig, with a timelocked mint executor  
**Distribution basis:** verified, consent-based contributions; AI may assist but never approve or mint.

> This specification supersedes the earlier 1,000,000,000 placeholder shown in the legacy `yatharth-mudra.html` surface. The selected maximum is 100,000 YTH. It is a technical supply cap, not a valuation, promise, investment, legal tender, redemption right, or guarantee of ₹100 crore per unit.

## 1. Decisions locked for v0.1

| Decision | v0.1 rule |
|---|---|
| Maximum supply | 100,000 whole YTH (10^13 base units at 8 decimals) |
| Initial supply | 0 |
| Minting | Explicit verified-allocation mint only |
| Distribution | Verified contribution with consent and appeal |
| Governance | 3 approvals from 5 independent signers |
| Mint executor | Timelock controlled by the 3-of-5 governance Safe |
| Network | Isolated private testnet; chain ID and validators configured only for test |
| DEX | Not included in v0.1; no swap, pool, sale or fiat rails |
| Public launch | Prohibited by this specification |
| AI authority | Advisory only; no signing keys, reviewer role, or mint permission |

The allocation buckets below are ceilings, not guaranteed entitlements or an instruction to mint the entire cap:

| Bucket | Share | Maximum bucket |
|---|---:|---:|
| Verified public-interest contribution grants | 40% | 40,000 YTH |
| Validator/security rewards | 25% | 25,000 YTH |
| Research, education and nature projects | 20% | 20,000 YTH |
| Emergency network reserve | 15% | 15,000 YTH |
| **Total** | **100%** | **100,000 YTH** |

Unallocated units remain unminted. No bucket can exceed its ceiling. A bucket change requires a public governance proposal, a delay, 3-of-5 approval and an audit entry.

## 2. Architecture

1. **Identity registry:** existing platform account IDs remain identifiers only. A registry ID is not a wallet, token balance or proof of funds.
2. **Self-custody wallet:** user controls private keys; the platform must never collect seed phrases or private keys.
3. **Contribution service:** records consent, contribution category, evidence digest and private evidence reference.
4. **Review service:** three distinct, conflict-checked human reviewers independently review the same evidence digest.
5. **Allocation service:** creates a mint intent only after the review threshold and policy checks pass.
6. **Governance:** 3-of-5 multisig approves policy and authorizes the timelocked mint executor.
7. **Token contract:** enforces the lifetime cap, one-time allocation IDs, evidence digests and role restrictions.
8. **Audit stream:** append-only events correlate database decisions with testnet transaction hashes.

AI/ML/NLP may classify submissions, flag duplicates, translate text and identify anomalies. AI output is never proof of a person's inner state, never the sole basis for rejection, and never a signature or authorization. Reviewers must be able to inspect evidence, declare conflicts, explain decisions and process appeals.

## 3. Verified contribution policy

Eligible evidence categories for the test are research, education, open knowledge, creative work, verified service, accessibility, public-interest work and environmental stewardship. The applicant must consent. Evidence must be relevant, minimally collected and stored privately.

A contribution becomes `VERIFIED` only when:
- consent is recorded;
- evidence digest is fixed for the review;
- three distinct authenticated human reviewers approve the same digest;
- each reviewer declares no conflict of interest;
- the contribution passes duplicate/fraud checks;
- any appeal window and policy-specific safeguards are satisfied.

No fasting, deprivation, isolation, self-harm, health disclosure, religious test, political test or private spiritual declaration is required. A person's dignity, food, shelter, healthcare or access to help must never depend on token eligibility. An AI score cannot measure enlightenment, consciousness or total satisfaction.

## 4. Mint authorization lifecycle

`SUBMITTED → UNDER_REVIEW → VERIFIED → ALLOCATION_PROPOSED → GOVERNANCE_QUEUED → GOVERNANCE_APPROVED → TIMELOCKED → MINTED`

Alternative terminal states: `REJECTED`, `WITHDRAWN`, `APPEALED`, `CANCELLED`.

A mint intent includes:
- unique allocation ID;
- recipient wallet address;
- amount in base units;
- contribution ID;
- SHA-256 evidence digest;
- bucket;
- policy version;
- three reviewer decisions;
- governance proposal and execution references.

The contract accepts only a mint call from the MINTER role, which must be held by a timelock executor controlled by the 3-of-5 Safe. The contract independently checks the lifetime cap and rejects reused allocation IDs. No AI agent, API key, database administrator or single reviewer receives a mint role.

## 5. Governance and validator controls

- Five independent governance signers; threshold 3-of-5.
- Signers use hardware-backed keys and documented recovery/rotation procedures.
- Timelock delay: at least 48 hours for mint-policy, role, cap or treasury changes.
- Emergency pause: 2-of-5 signers may pause transfers/minting; unpause requires 3-of-5.
- Role changes, contract upgrades (if ever introduced), bucket changes and mint intents are public testnet governance events.
- No proxy/upgrade mechanism in v0.1. A new audited contract version requires a new governance decision.
- Test validators must be operated by at least 4 separately administered nodes for fault testing; this is a private test network, not a claim of decentralization or production resilience.

## 6. Database boundary

Use the isolated schema in `testnet/sql/001_yatharth_testnet.sql` only on a disposable private-testnet database. It does not alter production account registry migrations 004/005. Do not run it against the live income database or production Neon branch.

Store only hashes and encrypted object references in ordinary database rows. Never store private keys, seed phrases, identity documents or raw sensitive evidence in public Git. Database state is not the source of token balances; the testnet contract is authoritative for testnet token balances.

## 7. Contract boundary

`testnet/contracts/YatharthToken.sol` is a testnet-only reference contract:
- fixed lifetime cap of 100,000 YTH at 8 decimals;
- initial supply zero;
- mint function requires MINTER_ROLE;
- each allocation ID can be used once;
- evidence digest must be nonzero;
- lifetime minted counter does not decrease when tokens are burned;
- pause blocks transfers, minting and burns;
- governance Safe administers roles; timelock executor holds MINTER_ROLE.

The contract does not implement a DEX, fiat conversion, redemption, custody, price oracle, public sale or automatic contribution scoring.

## 8. Testnet acceptance gates

Do not proceed to any public or production deployment unless all gates pass:
1. reproducible local-chain deployment from a pinned toolchain;
2. unit tests for cap, role access, duplicate allocation, pause, decimals and lifetime issuance;
3. integration tests for 3-of-5 approval and timelock delay;
4. database migration and rollback tested on disposable database;
5. privacy, threat-model and key-recovery review;
6. independent smart-contract audit with no unresolved critical/high findings;
7. jurisdiction-specific legal review before any exchange, custody, transfer or public economic activity;
8. explicit new written authorization for any deployment beyond the private testnet.

## 9. Evidence labels

- `DESIGNED`: specification exists.
- `IMPLEMENTED`: source code and tests exist.
- `LOCAL_TESTED`: tests pass on a local chain.
- `PRIVATE_TESTNET_DEPLOYED`: contract deployed to isolated test network.
- `INDEPENDENTLY_AUDITED`: third-party audit report exists.
- `PUBLIC_LAUNCH_AUTHORIZED`: separate approval and legal gates passed.

These states must never be conflated. v0.1 starts at `DESIGNED`; no token has been minted or deployed by this document.
