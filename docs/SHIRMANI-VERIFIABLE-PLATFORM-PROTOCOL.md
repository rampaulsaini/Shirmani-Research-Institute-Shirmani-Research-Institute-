# Shirmani Verifiable Platform Protocol

## Status
**DESIGN ONLY — no blockchain deployment is authorized by this document.**

Build a verifiable platform protocol first; blockchain is an optional settlement and anchoring layer, not the source of truth by itself.

## Architecture
- **IDENTITY:** human/project/repository identities and authorization
- **PROVENANCE:** content/source/claim/evidence lineage
- **VERIFICATION:** independent review, replication, QC and promotion gates
- **ASSET:** digital rights, credentials, attestations and optional NFTs
- **GOVERNANCE:** roles, permissions, proposals, dispute and recovery rules
- **SETTLEMENT:** bounded economic accounting and, only after legal/security gates, token settlement
- **ARCHIVE:** hashes, manifests, snapshots and recovery records

## Yatharth Mudra (YTH)
YTH is a proposed economic/utility layer inside the broader protocol, not the protocol itself. Current status remains DESIGN_TESTNET_FIRST: no minting, deployment, public sale, or monetary price.

## NFT boundary
NFTs may represent unique digital certificates or assets. ERC-721 is appropriate for unique items; ERC-1155 supports mixed fungible/non-fungible token classes. These token standards define token interfaces; they do not by themselves establish legal ownership, scientific truth, authorship, or evidence validity.

## Security gates
- fail-closed promotion
- multi-party authorization for privileged actions
- hardware-backed/offline key protection where appropriate
- contract pause and recovery controls
- independent smart-contract audit before deployment
- reproducible builds and signed releases
- rate limits and replay/idempotency protection
- separate treasury, deployment and governance keys
- formal verification of critical invariants where feasible
- continuous monitoring and incident-response runbooks

## Evidence boundary
No token, NFT, blockchain transaction, workflow PASS, or platform record is itself proof of a scientific or universal claim.

## Roadmap
1. SPECIFICATION
2. LOCAL_DETERMINISTIC_TESTS
3. THREAT_MODEL
4. TESTNET
5. INDEPENDENT_SECURITY_AUDIT
6. INDEPENDENT_PROTOCOL_REVIEW
7. CONTROLLED_PILOT
8. LEGAL_COMPLIANCE_REVIEW
9. MAINNET_DECISION
