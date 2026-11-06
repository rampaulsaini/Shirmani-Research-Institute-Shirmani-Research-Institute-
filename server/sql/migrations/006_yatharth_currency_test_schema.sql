-- Yatharth Currency Protocol v0.1 — OFF-CHAIN TEST SCHEMA ONLY.
-- Proposed migration. Do NOT apply to production/main database in this phase.
-- No tokens are minted and no financial transaction is executed by this schema.

BEGIN;

CREATE TABLE IF NOT EXISTS yatharth_currency_config (
  config_id smallint PRIMARY KEY DEFAULT 1 CHECK (config_id = 1),
  protocol_version text NOT NULL DEFAULT '0.1',
  token_symbol text NOT NULL DEFAULT 'YTH' CHECK (token_symbol = 'YTH'),
  max_supply_base_units numeric(78,0) NOT NULL
    DEFAULT 100000000000000000000000
    CHECK (max_supply_base_units = 100000000000000000000000),
  decimals smallint NOT NULL DEFAULT 18 CHECK (decimals = 18),
  minting_enabled boolean NOT NULL DEFAULT false CHECK (minting_enabled = false),
  public_launch_enabled boolean NOT NULL DEFAULT false CHECK (public_launch_enabled = false),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

INSERT INTO yatharth_currency_config (config_id)
VALUES (1)
ON CONFLICT (config_id) DO NOTHING;

CREATE TABLE IF NOT EXISTS yatharth_contributions (
  contribution_id text PRIMARY KEY,
  account_number text REFERENCES yatharth_account_registry(account_number) ON DELETE RESTRICT,
  category text NOT NULL CHECK (category IN
    ('WORK','SERVICE','RESEARCH','EDUCATION','CREATIVE','PRODUCT','SOCIAL_UTILITY','ENVIRONMENT')),
  summary text NOT NULL CHECK (length(summary) BETWEEN 10 AND 2000),
  evidence_bundle_hash text NOT NULL CHECK (evidence_bundle_hash ~ '^[a-fA-F0-9]{64}$'),
  evidence_reference text NOT NULL,
  policy_version text NOT NULL DEFAULT '0.1',
  status text NOT NULL DEFAULT 'SUBMITTED' CHECK (status IN
    ('SUBMITTED','EVIDENCE_PENDING','UNDER_REVIEW','VERIFIED','REJECTED','DISPUTED','APPEALED','CLOSED')),
  submitted_at timestamptz NOT NULL DEFAULT now(),
  reviewed_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_contribution_reviews (
  review_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  contribution_id text NOT NULL REFERENCES yatharth_contributions(contribution_id) ON DELETE RESTRICT,
  reviewer_ref text NOT NULL,
  decision text NOT NULL CHECK (decision IN ('APPROVE','REJECT','REQUEST_CHANGES','CONFLICT')),
  rationale text NOT NULL CHECK (length(rationale) BETWEEN 10 AND 4000),
  conflict_declared boolean NOT NULL DEFAULT false,
  panel_round smallint NOT NULL DEFAULT 1 CHECK (panel_round > 0),
  reviewed_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (contribution_id, reviewer_ref, panel_round)
);

CREATE TABLE IF NOT EXISTS yatharth_mint_authorizations (
  authorization_id text PRIMARY KEY,
  contribution_id text NOT NULL UNIQUE REFERENCES yatharth_contributions(contribution_id) ON DELETE RESTRICT,
  recipient_wallet text NOT NULL CHECK (recipient_wallet ~ '^0x[a-fA-F0-9]{40}$'),
  amount_base_units numeric(78,0) NOT NULL CHECK (amount_base_units > 0),
  evidence_bundle_hash text NOT NULL CHECK (evidence_bundle_hash ~ '^[a-fA-F0-9]{64}$'),
  policy_version text NOT NULL,
  reviewer_approval_count smallint NOT NULL CHECK (reviewer_approval_count >= 3),
  governance_reference text NOT NULL,
  status text NOT NULL DEFAULT 'PROPOSED' CHECK (status IN
    ('PROPOSED','GOVERNANCE_APPROVED','REVOKED','EXECUTED','EXPIRED')),
  expires_at timestamptz NOT NULL,
  tx_hash text UNIQUE CHECK (tx_hash IS NULL OR tx_hash ~ '^0x[a-fA-F0-9]{64}$'),
  created_at timestamptz NOT NULL DEFAULT now(),
  approved_at timestamptz,
  executed_at timestamptz
);

CREATE TABLE IF NOT EXISTS yatharth_governance_proposals (
  proposal_id text PRIMARY KEY,
  proposal_type text NOT NULL CHECK (proposal_type IN
    ('POLICY_CHANGE','ROLE_CHANGE','MINT_ENABLEMENT','TREASURY_ACTION','PAUSE','UNPAUSE','DEPLOYMENT')),
  description text NOT NULL CHECK (length(description) BETWEEN 10 AND 5000),
  payload_hash text NOT NULL CHECK (payload_hash ~ '^[a-fA-F0-9]{64}$'),
  status text NOT NULL DEFAULT 'DRAFT' CHECK (status IN
    ('DRAFT','OPEN','APPROVED','REJECTED','EXECUTED','CANCELLED','EXPIRED')),
  proposer_ref text NOT NULL,
  threshold_required smallint NOT NULL DEFAULT 3 CHECK (threshold_required >= 3),
  created_at timestamptz NOT NULL DEFAULT now(),
  expires_at timestamptz NOT NULL
);

CREATE TABLE IF NOT EXISTS yatharth_governance_votes (
  vote_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  proposal_id text NOT NULL REFERENCES yatharth_governance_proposals(proposal_id) ON DELETE RESTRICT,
  signer_ref text NOT NULL,
  decision text NOT NULL CHECK (decision IN ('APPROVE','REJECT')),
  signature_hash text NOT NULL CHECK (signature_hash ~ '^[a-fA-F0-9]{64}$'),
  voted_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (proposal_id, signer_ref)
);

CREATE TABLE IF NOT EXISTS yatharth_chain_events (
  event_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  network_label text NOT NULL CHECK (network_label IN ('LOCAL_DEV','PRIVATE_TESTNET')),
  chain_id numeric(78,0) NOT NULL,
  tx_hash text NOT NULL CHECK (tx_hash ~ '^0x[a-fA-F0-9]{64}$'),
  event_name text NOT NULL,
  evidence_id_hash text,
  block_number numeric(78,0) NOT NULL,
  observed_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (network_label, chain_id, tx_hash, event_name)
);

CREATE INDEX IF NOT EXISTS yatharth_contributions_status_idx
  ON yatharth_contributions(status, submitted_at);
CREATE INDEX IF NOT EXISTS yatharth_reviews_contribution_idx
  ON yatharth_contribution_reviews(contribution_id, panel_round);
CREATE INDEX IF NOT EXISTS yatharth_mint_authorizations_status_idx
  ON yatharth_mint_authorizations(status, expires_at);
CREATE INDEX IF NOT EXISTS yatharth_chain_events_block_idx
  ON yatharth_chain_events(network_label, chain_id, block_number);

COMMENT ON TABLE yatharth_currency_config IS
  'Design configuration only. Minting and public launch remain disabled in v0.1.';
COMMENT ON TABLE yatharth_contributions IS
  'Off-chain contribution references and hashes; do not store sensitive source documents or private keys here.';
COMMENT ON TABLE yatharth_mint_authorizations IS
  'Proposed allocation instructions; a row is not a mint, token balance, payment or income.';
COMMENT ON TABLE yatharth_chain_events IS
  'Observed local/private test chain events only; not proof of public network deployment.';

COMMIT;
