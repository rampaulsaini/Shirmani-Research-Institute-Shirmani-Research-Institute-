-- Yatharth Genesis Account Registry — migration 004.
-- Reserves a stable platform identity number only. This is NOT a bank account,
-- blockchain wallet, token balance, legal tender, deposit account, or payment rail.
-- Apply only after review: psql "$DATABASE_URL" -f server/sql/migrations/004_yatharth_genesis_account_registry.sql

BEGIN;

CREATE SEQUENCE IF NOT EXISTS yatharth_account_number_seq START WITH 2 INCREMENT BY 1;

CREATE TABLE IF NOT EXISTS yatharth_account_registry (
  account_number text PRIMARY KEY
    CHECK (account_number ~ '^YTH-[0-9]{10}$'),
  account_type text NOT NULL
    CHECK (account_type IN ('GENESIS','STANDARD')),
  owner_label text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  metadata jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE UNIQUE INDEX IF NOT EXISTS yatharth_one_genesis_account_idx
  ON yatharth_account_registry(account_type)
  WHERE account_type = 'GENESIS';

CREATE TABLE IF NOT EXISTS yatharth_account_events (
  event_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  account_number text NOT NULL
    REFERENCES yatharth_account_registry(account_number) ON DELETE RESTRICT,
  event_type text NOT NULL
    CHECK (event_type IN (
      'ACCOUNT_RESERVED',
      'ACCOUNT_ACTIVATED',
      'WALLET_BOUND',
      'ACCOUNT_SUSPENDED',
      'ACCOUNT_REVIEWED'
    )),
  event_data jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE OR REPLACE FUNCTION yatharth_reject_immutable_mutation()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
  RAISE EXCEPTION
    'Yatharth account identities and event history are append-only; record a new event instead';
END;
$$;

DROP TRIGGER IF EXISTS yatharth_registry_immutable ON yatharth_account_registry;
CREATE TRIGGER yatharth_registry_immutable
  BEFORE UPDATE OR DELETE ON yatharth_account_registry
  FOR EACH ROW EXECUTE FUNCTION yatharth_reject_immutable_mutation();

DROP TRIGGER IF EXISTS yatharth_events_immutable ON yatharth_account_events;
CREATE TRIGGER yatharth_events_immutable
  BEFORE UPDATE OR DELETE ON yatharth_account_events
  FOR EACH ROW EXECUTE FUNCTION yatharth_reject_immutable_mutation();

CREATE OR REPLACE FUNCTION next_yatharth_account_number()
RETURNS text
LANGUAGE sql
VOLATILE
AS $$
  SELECT 'YTH-' || lpad(nextval('yatharth_account_number_seq')::text, 10, '0');
$$;

CREATE OR REPLACE VIEW yatharth_account_current_state AS
SELECT
  r.account_number,
  r.account_type,
  r.owner_label,
  r.created_at,
  COALESCE(latest.event_type, 'ACCOUNT_RESERVED') AS latest_event,
  latest.event_data AS latest_event_data,
  latest.created_at AS latest_event_at
FROM yatharth_account_registry r
LEFT JOIN LATERAL (
  SELECT e.event_type, e.event_data, e.created_at
  FROM yatharth_account_events e
  WHERE e.account_number = r.account_number
  ORDER BY e.event_id DESC
  LIMIT 1
) latest ON true;

INSERT INTO yatharth_account_registry
  (account_number, account_type, owner_label, metadata)
VALUES
  (
    'YTH-0000000001',
    'GENESIS',
    'Shirmani Founder Account',
    '{"purpose":"Permanent platform identity reservation","not_a_wallet":true,"not_a_bank_account":true,"no_balance":true,"no_token_issued":true,"not_legal_tender":true}'::jsonb
  )
ON CONFLICT (account_number) DO NOTHING;

INSERT INTO yatharth_account_events (account_number, event_type, event_data)
SELECT
  'YTH-0000000001',
  'ACCOUNT_RESERVED',
  '{"state":"RESERVED","blockchain":"NOT_DEPLOYED","funds":"NONE"}'::jsonb
WHERE NOT EXISTS (
  SELECT 1
  FROM yatharth_account_events
  WHERE account_number = 'YTH-0000000001'
    AND event_type = 'ACCOUNT_RESERVED'
);

COMMENT ON TABLE yatharth_account_registry IS
  'Append-only Yatharth platform identity registry. Account numbers are identifiers, not bank accounts, wallets, tokens, balances, or proof of funds.';
COMMENT ON TABLE yatharth_account_events IS
  'Append-only lifecycle/audit events for Yatharth platform account identities. No financial settlement is performed here.';

COMMIT;
