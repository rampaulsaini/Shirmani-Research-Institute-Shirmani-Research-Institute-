# Yatharth Currency Protocol v1
## Design specification — testnet-first, not an issuance authorization

**Status:** DRAFT / DESIGN ONLY  
**Ticker:** YTH (proposed)  
**Decimals:** 8 (proposed)  
**Maximum supply:** 1,000,000,000 base units (as currently stated on the Yatharth Mudra reference page; subject to explicit governance approval before implementation)  
**Initial supply:** 0  
**Genesis identity:** YTH-0000000001 (identity reservation only; not a wallet, token, balance, or proof of funds)

> This document is not a token launch, offer, investment promise, guarantee of value, or authorization to mint. No mainnet, public sale, custody, fiat on/off-ramp, or exchange execution is enabled by this specification.

## 1. Design goals

1. User-controlled accounts: users control wallet keys; the platform never asks for or stores seed phrases.
2. Verifiable issuance: every issuance event has a reason code, policy version, authorizing governance record, transaction ID, and public audit trail.
3. Bounded supply: no mint path may exceed the approved cap; the default mint authority is disabled.
4. Distributed operation: independent validators, public protocol rules, reproducible software, and published security assumptions.
5. Human rights and due process: AI supports review; it does not make unappealable decisions about a person's dignity, identity, inner experience, or access to essential services.
6. Evidence before claims: testnet, audits, deployment, liquidity, market price, and redemption are separate states and must never be conflated.

## 2. Proposed network architecture

- **Ledger:** a dedicated application-specific blockchain may be evaluated, but no chain framework is selected by this document.
- **Consensus:** evaluate a mature Proof-of-Stake Byzantine-fault-tolerant consensus implementation. Do not invent a new consensus algorithm for production.
- **Validators:** independent operators with published entry, exit, slashing, uptime, and conflict-of-interest rules. Testnet validators must be clearly labelled.
- **Execution:** audited deterministic state transitions / smart contracts. Contract upgrades require a timelock, public proposal, and independent review.
- **Wallets:** standard audited key-management libraries, hardware-wallet compatibility where feasible, clear recovery warnings, and no server-side custody by default.
- **Indexing/API:** read-only public endpoints for supply, transactions, validator state, and verification proofs. API responses must identify whether data is testnet or mainnet.

## 3. Supply and issuance

The reference design currently lists maximum supply 1,000,000,000, initial supply 0, and 8 decimals. These are design parameters, not deployed facts.

Before any minting, governance must approve and publish:
- the exact unit convention (whole YTH vs base units);
- allocation schedule and vesting;
- emission limits per epoch;
- treasury and grant controls;
- validator reward formula;
- burn policy, if any;
- pause/emergency process and the conditions for using it.

**Hard invariant:** total minted minus burned must never exceed the approved maximum supply. The contract must reject unauthorized mint calls and emit a machine-readable issuance event for every successful mint. No administrator key may silently change the cap.

### 3.1 Mining and validation

The initial design does not use energy-intensive Proof-of-Work mining. Under a Proof-of-Stake design, validators propose/attest blocks and receive protocol-defined rewards only after transparent participation checks. Staking rewards are not guaranteed income. Slashing must be narrowly defined, evidence-based, appealable where appropriate, and tested against false positives.

## 4. Contribution grants and eligibility

The phrase “self-realization and continuing satisfaction” may remain a philosophical purpose, but it is not objectively measurable by an AI system and must not be represented as scientifically verified.

A possible grant process may consider voluntary, evidence-backed contributions such as:
- open research and educational material;
- verified public-interest software or tools;
- environmental restoration and conservation;
- documented community service;
- useful creative or accessibility work.

Safeguards:
- participation is voluntary and privacy-minimizing;
- no biometric, mental-health, religious, or intimate-life inference;
- AI/ML/NLP may classify submissions, detect duplicate evidence, translate, and flag anomalies, but cannot autonomously issue currency;
- human reviewers use published criteria, disclose conflicts, provide reasons, and allow an appeal;
- no one is ranked as more or less human, worthy, enlightened, or deserving;
- grants are budget-capped, auditable, and subject to anti-fraud checks.

## 5. AI / ML / NLP automission boundary

Allowed support functions:
- duplicate-evidence detection and provenance checks;
- anomaly and Sybil-risk flags with human review;
- natural-language application assistance and translation;
- monitoring of validator uptime and protocol health;
- reconciliation of issuance events against the public ledger.

Prohibited autonomous actions:
- minting or transferring funds solely on an opaque model score;
- changing supply, consensus, contract permissions, or eligibility rules;
- confiscating balances or permanently banning users without due process;
- claiming that quantum computing, “infinity” processing, or an AI label creates monetary value or cryptographic security.

All model-assisted decisions must be logged with model/version, input provenance, confidence/limitations, reviewer action, and appeal outcome, while minimizing personal data.

## 6. Accounts and decentralised exchange

A wallet address is a cryptographic identifier, not a bank account and not proof of identity, balance, ownership of an external asset, or legal-tender status. Users retain control of their keys.

A future DEX may be considered only after:
- contract design and independent audit;
- tested price discovery and liquidity controls;
- MEV, oracle, manipulation, and loss-risk analysis;
- clear disclosures of slippage, fees, impermanent loss, and smart-contract risk;
- jurisdiction-specific legal and AML/CFT review.

A DEX does not make a project independent of the internet, validators, device infrastructure, law, or external assets. No claim of immunity from governments, banks, or legal obligations is permitted.

## 7. Price and redemption policy

The aspiration of ₹1,00,00,00,000 per YTH is a target statement only. It is not a peg, reserve, redemption promise, fair value, or market price. AI cannot manufacture demand or guarantee buyers.

Any future price statement must be labelled as one of:
- **target/aspiration** — not a market quote;
- **observed market price** — supported by verifiable trades and liquidity context;
- **redeemable value** — backed by enforceable redemption terms and sufficient disclosed assets.

Do not advertise a guaranteed ₹100-crore value. Do not imply that a displayed price means a holder can sell at that price.

## 8. Governance and key safety

- Separate roles for proposal, review, deployment, and emergency response.
- Multi-party authorization for any future mint authority or contract upgrade.
- Timelocked public governance changes and reproducible build artifacts.
- Published incident response, key rotation, backup, and recovery procedures.
- Emergency pause must be limited, logged, reviewable, and unable to create arbitrary balances.
- No single founder, AI agent, operator, or API credential may unilaterally mint unlimited supply.

## 9. Required release gates

1. Protocol and tokenomics review published.
2. Jurisdiction-specific legal review completed.
3. Threat model and independent smart-contract/security audit completed.
4. Testnet deployed with zero real monetary value.
5. Supply invariants, access controls, replay protection, wallet flows, and recovery tested.
6. Independent test results and known limitations published.
7. Mainnet and any exchange launch approved through separate explicit governance and compliance gates.

Until all gates are evidenced, the public status must remain **DESIGN / TESTNET-FIRST — NOT ISSUED**.

## 10. Evidence states

Use separate machine-readable states:
- `DESIGN_ONLY`
- `TESTNET_DEPLOYED`
- `TESTNET_VERIFIED`
- `AUDIT_COMPLETE`
- `LEGAL_REVIEW_COMPLETE`
- `MAINNET_DEPLOYED`
- `MINTING_ENABLED`
- `EXCHANGE_ENABLED`

A state may be marked complete only with a dated artifact, source commit, environment, verifier, and reproducible evidence. Do not infer deployment or verification from a merged PR.

## 11. Immediate implementation scope

The first engineering milestone is a non-monetary testnet prototype:
- local/testnet chain only;
- zero-value test tokens;
- no public sale, fiat, custody, or DEX;
- test issuance events and cap-enforcement tests;
- independent validator simulation;
- public read-only supply and transaction explorer;
- CI tests proving unauthorized mint attempts fail.

The Genesis identity reservation `YTH-0000000001` remains an identity-registry record only. Do not allocate `YTH-0000000002` as a currency wallet or create a QR payment page until a separately approved wallet protocol exists and the Genesis verification endpoint has been independently checked.

---
**Document classification:** proposal for review. Not legal, financial, investment, or security advice.
