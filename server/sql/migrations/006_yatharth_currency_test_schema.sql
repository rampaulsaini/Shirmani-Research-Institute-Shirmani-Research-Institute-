-- Yatharth Currency Protocol v0.1 — OFF-CHAIN TEST SCHEMA ONLY.
-- Proposed migration. Do NOT apply to production/main database.
-- Requires migration 004_yatharth_genesis_account_registry.sql first.
-- No tokens are minted and no financial transaction is executed here.

BEGIN;

CREATE TABLE IF NOT EXISTS yatharth_currency_config (
  config_id smallint PRIMARY KEY DEFAULT 1 CHECK (config_id = 1),
  protocol_version text NOT NULL DEFAULT '0.1',
  token_symbol text NOT NULL DEFAULT 'YTH' CHECK (token_symbol = 'YTH'),
  max_supply_base_units numeric(78,0) NOT NULL DEFAULT 100000000000000000000000
    CHECK (max_supply_base_units = 100000000000000000000000),
  decimals smallint NOT NULL DEFAULT 18 CHECK (decimals = 18),
  minting_enabled boolean NOT NULL DEFAULT false CHECK (minting_enabled = false),
  public_launch_enabled boolean NOT NULL DEFAULT false CHECK (public_launch_enabled = false),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
INSERT INTO yatharth_currency_config (config_id) VALUES (1)
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
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (contribution_id, evidence_bundle_hash)
);

CREATE TABLE IF NOT EXISTS yatharth_reviewer_registry (
  reviewer_ref text PRIMARY KEY,
  reviewer_key_hash text NOT NULL UNIQUE CHECK (reviewer_key_hash ~ '^[a-fA-F0-9]{64}$'),
  status text NOT NULL DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE','INACTIVE')),
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_contribution_reviews (
  review_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  contribution_id text NOT NULL REFERENCES yatharth_contributions(contribution_id) ON DELETE RESTRICT,
  reviewer_ref text NOT NULL REFERENCES yatharth_reviewer_registry(reviewer_ref) ON DELETE RESTRICT,
  decision text NOT NULL CHECK (decision IN ('APPROVE','REJECT','REQUEST_CHANGES','CONFLICT')),
  rationale text NOT NULL CHECK (length(rationale) BETWEEN 10 AND 4000),
  conflict_declared boolean NOT NULL DEFAULT false,
  panel_round smallint NOT NULL DEFAULT 1 CHECK (panel_round > 0),
  reviewed_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (contribution_id, reviewer_ref, panel_round)
);

CREATE OR REPLACE VIEW yatharth_contribution_review_gate AS
SELECT r.contribution_id, r.panel_round,
  COUNT(DISTINCT r.reviewer_ref) FILTER
    (WHERE r.decision = 'APPROVE' AND NOT r.conflict_declared)::smallint AS independent_approval_count,
  COUNT(DISTINCT r.reviewer_ref) FILTER
    (WHERE r.decision = 'REJECT' AND NOT r.conflict_declared)::smallint AS independent_rejection_count
FROM yatharth_contribution_reviews r
JOIN yatharth_reviewer_registry rr
  ON rr.reviewer_ref = r.reviewer_ref AND rr.status = 'ACTIVE'
GROUP BY r.contribution_id, r.panel_round;

CREATE TABLE IF NOT EXISTS yatharth_mint_authorizations (
  authorization_id text PRIMARY KEY,
  contribution_id text NOT NULL UNIQUE,
  evidence_bundle_hash text NOT NULL,
  recipient_wallet text NOT NULL CHECK (recipient_wallet ~ '^0x[a-fA-F0-9]{40}$'),
  amount_base_units numeric(78,0) NOT NULL CHECK (amount_base_units > 0),
  policy_version text NOT NULL,
  governance_reference text NOT NULL,
  status text NOT NULL DEFAULT 'PROPOSED' CHECK (status IN
    ('PROPOSED','GOVERNANCE_APPROVED','REVOKED','EXECUTED','EXPIRED')),
  expires_at timestamptz NOT NULL,
  tx_hash text UNIQUE CHECK (tx_hash IS NULL OR tx_hash ~ '^0x[a-fA-F0-9]{64}$'),
  created_at timestamptz NOT NULL DEFAULT now(),
  approved_at timestamptz,
  executed_at timestamptz,
  FOREIGN KEY (contribution_id, evidence_bundle_hash)
    REFERENCES yatharth_contributions(contribution_id, evidence_bundle_hash) ON DELETE RESTRICT
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
  threshold_required smallint NOT NULL DEFAULT 3 CHECK (threshold_required BETWEEN 3 AND 5),
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
COMMENT ON TABLE yatharth_reviewer_registry IS
  'Pseudonymous reviewer registry; independent identity vetting remains an off-database control.';
COMMENT ON VIEW yatharth_contribution_review_gate IS
  'Computed active, non-conflicted reviewer counts; not a governance approval or mint command.';
COMMENT ON TABLE yatharth_mint_authorizations IS
  'Proposed allocation instructions only; not a mint, token balance, payment or income.';
COMMENT ON TABLE yatharth_chain_events IS
  'Observed local/private test chain events only; not proof of public network deployment.';


-- Enforce the review gate in the database, not only in an application query.
CREATE OR REPLACE FUNCTION yatharth_require_review_gate()
RETURNS trigger LANGUAGE plpgsql AS $body$
DECLARE approvals integer;
BEGIN
  IF NEW.status = 'VERIFIED'
     AND (TG_OP = 'INSERT' OR OLD.status IS DISTINCT FROM NEW.status) THEN
    SELECT COALESCE(g.independent_approval_count, 0)
      INTO approvals
  FROM yatharth_contribution_review_gate g
  WHERE g.contribution_id = NEW.contribution_id
    AND g.panel_round = (
      SELECT max(panel_round)
      FROM yatharth_contribution_review_gate
      WHERE contribution_id = NEW.contribution_id
        AND independent_approval_count >= 3
    );

    IF COALESCE(approvals, 0) < 3 THEN
      RAISE EXCEPTION 'Three active, distinct, non-conflicted reviewer approvals in one panel round are required';
    END IF;
  END IF;
  RETURN NEW;
END;
$body$;

DROP TRIGGER IF EXISTS yatharth_verified_review_gate ON yatharth_contributions;
CREATE TRIGGER yatharth_verified_review_gate
  BEFORE INSERT OR UPDATE OF status ON yatharth_contributions
  FOR EACH ROW EXECUTE FUNCTION yatharth_require_review_gate();

CREATE OR REPLACE FUNCTION yatharth_require_mint_authorization_gate()
RETURNS trigger LANGUAGE plpgsql AS $body$
DECLARE approvals integer;
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM yatharth_contributions c
    WHERE c.contribution_id = NEW.contribution_id
      AND c.evidence_bundle_hash = NEW.evidence_bundle_hash
      AND c.status = 'VERIFIED'
  ) THEN
    RAISE EXCEPTION 'Mint authorization requires a VERIFIED contribution and matching evidence hash';
  END IF;

  SELECT COALESCE(g.independent_approval_count, 0)
    INTO approvals
  FROM yatharth_contribution_review_gate g
  WHERE g.contribution_id = NEW.contribution_id
    AND g.panel_round = (
      SELECT max(panel_round)
      FROM yatharth_contribution_review_gate
      WHERE contribution_id = NEW.contribution_id
        AND independent_approval_count >= 3
    );

  IF COALESCE(approvals, 0) < 3 THEN
    RAISE EXCEPTION 'Mint authorization requires three active, distinct, non-conflicted approvals';
  END IF;
  RETURN NEW;
END;
$body$;

DROP TRIGGER IF EXISTS yatharth_mint_authorization_review_gate ON yatharth_mint_authorizations;
CREATE TRIGGER yatharth_mint_authorization_review_gate
  BEFORE INSERT OR UPDATE OF contribution_id, evidence_bundle_hash
  ON yatharth_mint_authorizations
  FOR EACH ROW EXECUTE FUNCTION yatharth_require_mint_authorization_gate();

-- Review decisions are immutable; corrections are recorded in a new panel round.
CREATE OR REPLACE FUNCTION yatharth_reject_review_mutation()
RETURNS trigger LANGUAGE plpgsql AS $body$
BEGIN
  RAISE EXCEPTION 'Review history is append-only; submit a new panel-round review';
END;
$body$;

DROP TRIGGER IF EXISTS yatharth_reviews_append_only ON yatharth_contribution_reviews;
CREATE TRIGGER yatharth_reviews_append_only
  BEFORE UPDATE OR DELETE ON yatharth_contribution_reviews
  FOR EACH ROW EXECUTE FUNCTION yatharth_reject_review_mutation();

COMMIT;
