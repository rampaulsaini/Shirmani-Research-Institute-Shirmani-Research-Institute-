-- Yatharth Protocol v0.1 — PRIVATE TESTNET ONLY.
-- Apply only to a disposable, isolated testnet database.
-- NEVER run against the production income database or production Neon branch.
-- This schema records test decisions; it does not mint tokens or control contract balances.

BEGIN;

CREATE SCHEMA IF NOT EXISTS yatharth_testnet;

CREATE TABLE IF NOT EXISTS yatharth_testnet.testnet_accounts (
  account_id text PRIMARY KEY,
  wallet_address text NOT NULL,
  chain_id bigint NOT NULL,
  network_label text NOT NULL DEFAULT 'PRIVATE_TESTNET',
  status text NOT NULL DEFAULT 'ACTIVE'
    CHECK (status IN ('ACTIVE','SUSPENDED','CLOSED')),
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (chain_id, wallet_address)
);

CREATE TABLE IF NOT EXISTS yatharth_testnet.contributions (
  contribution_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  account_id text NOT NULL REFERENCES yatharth_testnet.testnet_accounts(account_id) ON DELETE RESTRICT,
  category text NOT NULL CHECK (category IN (
    'RESEARCH','EDUCATION','OPEN_KNOWLEDGE','CREATIVE_WORK',
    'VERIFIED_SERVICE','ACCESSIBILITY','PUBLIC_INTEREST','ENVIRONMENT'
  )),
  description text NOT NULL CHECK (length(description) BETWEEN 10 AND 2000),
  consent_recorded boolean NOT NULL DEFAULT false CHECK (consent_recorded),
  evidence_sha256 bytea NOT NULL CHECK (octet_length(evidence_sha256) = 32),
  private_evidence_ref text NOT NULL,
  policy_version text NOT NULL DEFAULT '0.1',
  status text NOT NULL DEFAULT 'SUBMITTED'
    CHECK (status IN ('SUBMITTED','UNDER_REVIEW','VERIFIED','REJECTED','WITHDRAWN','APPEALED')),
  submitted_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_testnet.review_decisions (
  contribution_id bigint NOT NULL REFERENCES yatharth_testnet.contributions(contribution_id) ON DELETE RESTRICT,
  reviewer_id text NOT NULL,
  evidence_sha256 bytea NOT NULL CHECK (octet_length(evidence_sha256) = 32),
  decision text NOT NULL CHECK (decision IN ('APPROVE','REJECT','REQUEST_INFO')),
  conflict_declared boolean NOT NULL CHECK (conflict_declared = false),
  rationale text NOT NULL CHECK (length(rationale) BETWEEN 10 AND 2000),
  decided_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (contribution_id, reviewer_id)
);

CREATE TABLE IF NOT EXISTS yatharth_testnet.allocations (
  allocation_id text PRIMARY KEY,
  contribution_id bigint NOT NULL UNIQUE REFERENCES yatharth_testnet.contributions(contribution_id) ON DELETE RESTRICT,
  recipient_wallet text NOT NULL,
  bucket text NOT NULL CHECK (bucket IN ('PUBLIC_INTEREST','VALIDATOR','RESEARCH_NATURE','RESERVE')),
  amount_base_units numeric(78,0) NOT NULL CHECK (amount_base_units > 0),
  evidence_sha256 bytea NOT NULL CHECK (octet_length(evidence_sha256) = 32),
  status text NOT NULL DEFAULT 'PROPOSED'
    CHECK (status IN ('PROPOSED','GOVERNANCE_QUEUED','APPROVED','TIMELOCKED','MINTED','CANCELLED')),
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_testnet.governance_approvals (
  proposal_id text NOT NULL,
  signer_id text NOT NULL,
  decision text NOT NULL CHECK (decision IN ('APPROVE','REJECT')),
  payload_sha256 bytea NOT NULL CHECK (octet_length(payload_sha256) = 32),
  signature_ref text NOT NULL,
  signed_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (proposal_id, signer_id)
);

CREATE TABLE IF NOT EXISTS yatharth_testnet.mint_receipts (
  allocation_id text PRIMARY KEY REFERENCES yatharth_testnet.allocations(allocation_id) ON DELETE RESTRICT,
  chain_id bigint NOT NULL,
  contract_address text NOT NULL,
  transaction_hash text NOT NULL UNIQUE,
  amount_base_units numeric(78,0) NOT NULL CHECK (amount_base_units > 0),
  minted_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_testnet.audit_events (
  event_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  event_type text NOT NULL,
  entity_type text NOT NULL,
  entity_id text NOT NULL,
  actor_id text NOT NULL,
  payload jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS contributions_status_idx
  ON yatharth_testnet.contributions(status, submitted_at);
CREATE INDEX IF NOT EXISTS review_decisions_contribution_idx
  ON yatharth_testnet.review_decisions(contribution_id, decided_at);
CREATE INDEX IF NOT EXISTS audit_events_entity_idx
  ON yatharth_testnet.audit_events(entity_type, entity_id, event_id);

-- Enforce that reviewer decisions refer to the exact submitted evidence digest.
CREATE OR REPLACE FUNCTION yatharth_testnet.check_review_digest()
RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE expected_digest bytea;
BEGIN
  SELECT evidence_sha256 INTO expected_digest
  FROM yatharth_testnet.contributions
  WHERE contribution_id = NEW.contribution_id;
  IF expected_digest IS NULL OR expected_digest <> NEW.evidence_sha256 THEN
    RAISE EXCEPTION 'review evidence digest does not match contribution';
  END IF;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS review_digest_guard ON yatharth_testnet.review_decisions;
CREATE TRIGGER review_digest_guard
  BEFORE INSERT OR UPDATE ON yatharth_testnet.review_decisions
  FOR EACH ROW EXECUTE FUNCTION yatharth_testnet.check_review_digest();

-- Require three distinct, conflict-free human approvals before VERIFIED status.
CREATE OR REPLACE FUNCTION yatharth_testnet.require_three_approvals()
RETURNS trigger LANGUAGE plpgsql AS $
DECLARE approvals integer;
BEGIN
  IF NEW.status = 'VERIFIED' AND OLD.status IS DISTINCT FROM NEW.status THEN
    SELECT count(*) INTO approvals
    FROM yatharth_testnet.review_decisions
    WHERE contribution_id = NEW.contribution_id
      AND decision = 'APPROVE'
      AND evidence_sha256 = NEW.evidence_sha256
      AND conflict_declared = false;
    IF approvals < 3 THEN
      RAISE EXCEPTION 'three distinct human approvals are required before VERIFIED';
    END IF;
  END IF;
  RETURN NEW;
END;
$;

DROP TRIGGER IF EXISTS contribution_three_approvals_guard ON yatharth_testnet.contributions;
CREATE TRIGGER contribution_three_approvals_guard
  BEFORE UPDATE OF status ON yatharth_testnet.contributions
  FOR EACH ROW EXECUTE FUNCTION yatharth_testnet.require_three_approvals();

-- Review decisions, governance signatures, mint receipts and audit events are append-only.
CREATE OR REPLACE FUNCTION yatharth_testnet.reject_immutable_mutation()
RETURNS trigger LANGUAGE plpgsql AS $
BEGIN
  RAISE EXCEPTION 'Yatharth testnet evidence is append-only; add a correction event instead';
END;
$;

DROP TRIGGER IF EXISTS review_decisions_immutable ON yatharth_testnet.review_decisions;
CREATE TRIGGER review_decisions_immutable
  BEFORE UPDATE OR DELETE ON yatharth_testnet.review_decisions
  FOR EACH ROW EXECUTE FUNCTION yatharth_testnet.reject_immutable_mutation();

DROP TRIGGER IF EXISTS governance_approvals_immutable ON yatharth_testnet.governance_approvals;
CREATE TRIGGER governance_approvals_immutable
  BEFORE UPDATE OR DELETE ON yatharth_testnet.governance_approvals
  FOR EACH ROW EXECUTE FUNCTION yatharth_testnet.reject_immutable_mutation();

DROP TRIGGER IF EXISTS mint_receipts_immutable ON yatharth_testnet.mint_receipts;
CREATE TRIGGER mint_receipts_immutable
  BEFORE UPDATE OR DELETE ON yatharth_testnet.mint_receipts
  FOR EACH ROW EXECUTE FUNCTION yatharth_testnet.reject_immutable_mutation();

DROP TRIGGER IF EXISTS audit_events_immutable ON yatharth_testnet.audit_events;
CREATE TRIGGER audit_events_immutable
  BEFORE UPDATE OR DELETE ON yatharth_testnet.audit_events
  FOR EACH ROW EXECUTE FUNCTION yatharth_testnet.reject_immutable_mutation();

-- The schema deliberately does not grant application permissions. Configure
-- least-privilege roles and row-level access only after a separate security review.
COMMENT ON SCHEMA yatharth_testnet IS
  'Disposable private-testnet data only; not production money, wallet custody, or token balances.';

COMMIT;
