# Yatharth Genesis Account 001

- Permanent platform identity: `YTH-0000000001`
- Account label: Shirmani Founder Account
- Registry state: `RESERVED`
- Account type: `GENESIS`
- Symbol association: YTH (proposed Yatharth Mudra)
- Blockchain network: not selected
- Wallet address: not created
- Token issuance / balance: none
- Fiat deposits, withdrawals, custody, or exchange execution: not enabled

## Meaning

The account number is a stable identifier in the Yatharth platform registry. It is designed to remain the same if the owner later binds one or more self-custody wallet addresses or uses different supported networks.

It is **not** a bank account number, payment account, blockchain address, private key, token balance, legal-tender claim, or proof that funds exist. No private key or recovery phrase is generated or stored by this registry.

## Design boundaries

1. The identity row is append-only at the application/database-trigger level; later lifecycle changes are recorded as new events.
2. A database owner can still alter database objects or restore/replace the database. Stronger tamper evidence requires external backups and/or a public blockchain anchor.
3. Wallets must be created under the account holder's own control. The platform must never ask the holder to disclose a seed phrase or private key.
4. Multi-currency display can show supported asset/network metadata. It does not mean every fiat currency can be deposited, withdrawn, or converted without payment partners.
5. A non-custodial peer-to-peer crypto exchange can reduce custody by the platform; it cannot guarantee immunity from applicable laws, chain-level restrictions, internet providers, counterparties, or fiat payment rails.
6. No public sale, minting, deposits, withdrawals, exchange execution, or income is enabled by this identity reservation.

## India launch gate

Before operating an exchange, custody, transfer, or fiat/virtual-asset conversion service, obtain jurisdiction-specific legal advice and complete applicable registration, AML/CFT, KYC, reporting, tax, consumer-protection, and security requirements. The registry alone does not authorize financial activity.

## Evidence distinction

`ACCOUNT_RESERVED` means only that this platform identity has been recorded. It does not mean `WALLET_CREATED`, `TOKEN_ISSUED`, `FUNDS_RECEIVED`, `EXCHANGE_LIVE`, or `INCOME_EARNED`.
