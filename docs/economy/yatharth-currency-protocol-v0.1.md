# Yatharth Currency Protocol v0.1

**Status:** DESIGN + PRIVATE TESTNET SPECIFICATION ONLY  
**Token symbol:** YTH (proposed)  
**Maximum supply:** 100,000 YTH (18 decimal places; 100,000 × 10^18 base units)  
**Distribution basis:** verified contribution only  
**Governance:** independent multi-validator / multisig governance  
**Minting enabled:** NO  
**Public sale / exchange / deposits / withdrawals:** NO  
**Mainnet deployment:** NOT AUTHORIZED

## 1. Decisions locked for v0.1

1. Hard maximum supply is 100,000 YTH. No inflation beyond this cap.
2. No allocation is earned merely by registration, identity, belief, self-description, or AI score.
3. A contribution must have reviewable evidence and pass the review policy below.
4. AI/ML/NLP may assist triage, translation, duplicate detection, fraud signals and accessibility. AI cannot be the sole verifier, rejecter, allocator or mint authority.
5. Personal, health, biometric, spiritual or other sensitive data must not be put on-chain. Store only minimum necessary evidence references and cryptographic hashes off-chain.
6. No minting, sale, swap, fiat rail, custody, lending, redemption or public launch is active in this release.

## 2. Supply and units

- ERC-20 style display precision: 18 decimals.
- Hard cap: `100000000000000000000000` base units.
- Genesis minted supply: **0 YTH**.
- Testnet token balances, if ever used in a later explicitly approved test, are valueless test assets and must be visibly labelled TEST ONLY.
- The cap is a technical ceiling, not a price, reserve, guarantee, claim on assets or promise of redemption.
- No ₹100-crore price is set or implied by this protocol.

## 3. Contribution verification and distribution

### Eligible evidence classes
- completed work or service with a verifiable deliverable;
- educational or research output with provenance;
- creative/product output with rights and authorship checks;
- social utility or environmental work with independently reviewable evidence.

No contribution category may require disclosure of a person's private spiritual experience, medical data, biometric data, political or religious identity, or other sensitive traits.

### Review workflow
`SUBMITTED → EVIDENCE_PENDING → UNDER_REVIEW → VERIFIED | REJECTED | DISPUTED`

- Each application receives a stable contribution ID.
- Evidence is stored outside the chain; the database stores a content hash, reference, type, reviewer notes and timestamps.
- Minimum 3 independent approvals from a 5-reviewer panel for an allocation recommendation.
- A reviewer cannot review their own contribution or a related-party submission.
- Reviewers disclose conflicts; conflicted reviewers are excluded.
- Applicants receive reasons and an appeal route.
- Appeals are reviewed by a different panel.
- A verified contribution is not automatically a token allocation.
- Allocation amounts come from a separately published, versioned schedule and require governance approval.
- No algorithmic score alone determines a person's worth or eligibility.

### Mint authorization
A verified contribution can create a **proposed** mint authorization only. The authorization must contain:
- contribution ID;
- recipient wallet address supplied and controlled by the recipient;
- amount in base units;
- evidence bundle hash;
- policy version;
- at least 3 independent reviewer approvals;
- approval timestamp and expiry;
- governance approval reference.

Execution remains disabled until a separate security, legal and governance release decision. The contract's `mintVerified` function is guarded by an explicit minting-disabled switch and a MINTER_ROLE controlled by the governance multisig. No server API may hold a unilateral mint key.

## 4. Governance and validators

- Governance authority must be a threshold multisig, not a single externally owned account.
- Initial testnet recommendation: 3-of-5 independent signers, with signers held by separate trusted operators.
- Separate operational roles: proposal submitter, reviewer, validator operator, security pause guardian and multisig signer.
- Parameter changes, role changes, mint enablement, treasury transfers and contract upgrades (if any) require published proposals and threshold approval.
- Emergency pause may stop token transfers; unpause requires governance approval.
- Validators must be independently operated. A validator list in the database is a registry, not proof of consensus decentralization.
- Testnet consensus choice is deliberately deferred until node software, validator operations, failure recovery, slashing and operating costs are tested. Do not describe a private dev chain as decentralized production.

## 5. Database model

Migration `server/sql/migrations/006_yatharth_currency_test_schema.sql` adds the off-chain evidence, reviewer registry, review-gate view, allocation, governance and chain-observation records. The allocation table ties its evidence hash to the originating contribution with a composite foreign key. It is a proposed migration and has **not** been applied.

Core tables:
- `yatharth_currency_config`: one versioned policy row; cap and launch/mint flags.
- `yatharth_contributions`: contribution application and evidence hash/reference.
- `yatharth_reviewer_registry`: pseudonymous reviewer references and uniqueness hashes; independent identity vetting remains an off-database control.
- `yatharth_contribution_reviews`: reviewer decisions and conflicts, constrained to registered reviewer references.
- `yatharth_contribution_review_gate`: computed active, non-conflicted approval/rejection counts derived from persisted review rows; caller-supplied approval counts are not accepted.
- `yatharth_mint_authorizations`: approved but not necessarily executed mint intents.
- `yatharth_governance_proposals` / `yatharth_governance_votes`: proposal lifecycle and voting evidence.
- `yatharth_chain_events`: observed testnet transaction/event references.

No seed phrase, private key, raw identity document, medical record or full sensitive evidence is stored in these tables.

## 6. Smart contract

`contracts/YatharthToken.sol` is a source-only test artifact using pinned OpenZeppelin Contracts v5 APIs. `contracts/package.json`, `contracts/hardhat.config.cjs` and `contracts/test/` provide a disposable local Hardhat compile/unit-test harness. The test governance executor is a permissive fixture only and MUST NEVER be deployed to a public or value-bearing network. The contract enforces:
- fixed 100,000 YTH cap;
- minting disabled by default;
- explicit governance action required to enable minting;
- mint role controlled by a deployed governance contract address (the code-presence check does not itself validate multisig threshold or signer independence);
- unique evidence ID per mint;
- pause control;
- no owner-only unlimited mint function.

The source is not compiled, audited, deployed or activated by this PR. A successful unit test is not a security audit.

## 7. Security and privacy controls

- Never request, collect or store wallet seed phrases or private keys.
- Recipient controls their own wallet.
- Use hardware-backed or reputable multisig signer custody for governance.
- Rate-limit contribution and review APIs; require authentication and audit logs.
- Encrypt sensitive off-chain evidence; use short retention periods and consent.
- Public chain data is permanent and linkable; do not put personal data on-chain.
- Independent smart-contract audit and threat model are mandatory before any real-value deployment.
- Maintain tested backups and recovery drills for the database and evidence store.
- AI outputs must be explainable, reviewable and appealable; retain model/version and decision provenance.

## 8. Private testnet implementation plan

### Phase A — documentation and static checks
- Review this specification and migration.
- Pin Solidity and OpenZeppelin versions.
- Run `cd contracts && npm install && npm run compile && npm test` locally against the disposable Hardhat chain (chain ID 31337); the GitHub Actions test workflow is included for CI once available from the base branch.
- Verify cap, default mint-off, unauthorized mint rejection, duplicate evidence rejection, pause behaviour and governance role checks.

### Phase B — isolated database branch
- Create an isolated Neon branch from the existing database.
- Apply migration 006 only to that isolated branch using a direct (non-pooled) connection.
- Verify constraints, append-only audit behaviour, reviewer uniqueness and threshold queries.
- Do not apply migration 006 to production/main database.

### Phase C — private chain
- Use a local Anvil/Hardhat development chain first; do not expose a public RPC.
- Deploy only to a disposable local chain with test-only governance keys.
- Keep minting disabled; use mocked test fixtures only.
- If a later test explicitly needs token balances, use a separate TEST token deployment with a conspicuous test name and no value.

### Phase D — review gates
- Independent contract review and security audit.
- Legal and accounting review for the intended jurisdictions and activities.
- Governance signer independence and recovery drill.
- User privacy and appeals review.
- Written approval required before any public network, real token, mint, exchange, payment or sale.

## 9. Release acceptance criteria

- Contract compiles with Solidity 0.8.24 and the pinned OpenZeppelin dependency.
- Local tests prove EOA governance rejection, default mint-off, unauthorized mint rejection, unique evidence enforcement, hard-cap enforcement, and pause/unpause controls.
- Supply cap cannot be exceeded.
- Initial total supply is zero.
- Minting is disabled at deployment.
- Minting cannot be enabled by one server, one AI agent or one reviewer.
- Every test mint (if separately authorized on a disposable chain) maps to one unique evidence hash and governance approval.
- At least three independent reviews are recorded for each proposed allocation.
- Conflicts and appeals are handled and logged.
- No personal sensitive data or keys are stored on-chain.
- Tests, audit, legal review and governance approval are published before any later launch decision.

## 10. Explicit non-claims

This protocol does not create legal tender, a bank account, a deposit, a guaranteed asset, a guaranteed exchange rate, a ₹100-crore market price, passive income, a claim against reserves, or immunity from law, regulators, banks, internet providers or counterparties. A decentralized wallet does not make a person or service outside applicable law.

**Current state remains: design only; no real YTH minted; no public launch; no DEX trading; no financial service enabled.**
