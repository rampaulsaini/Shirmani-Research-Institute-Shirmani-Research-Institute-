-- Yatharth public Genesis account verification registry.
-- This records a platform reservation only; it is not a wallet, deposit, token or legal tender.
BEGIN;
CREATE TABLE IF NOT EXISTS yatharth_accounts (
  account_id TEXT PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  status TEXT,
  proof_hash TEXT
);
INSERT INTO yatharth_accounts (account_id, status, proof_hash)
VALUES ('YTH-0000000001', 'RESERVED_PERMANENT', 'GENESIS-2026-11-06-001')
ON CONFLICT (account_id) DO NOTHING;
COMMIT;
