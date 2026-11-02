-- Yatharth Mudra Honour Verification v1
-- PostgreSQL migration. Apply only after a database owner reviews access policies.
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS yatharth_mudra_cases (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  public_record_id TEXT NOT NULL UNIQUE,
  display_name TEXT NOT NULL CHECK (length(display_name) BETWEEN 1 AND 120),
  consent_recorded BOOLEAN NOT NULL DEFAULT FALSE CHECK (consent_recorded),
  framework_version TEXT NOT NULL DEFAULT '1.0.0',
  continuity_days INTEGER NOT NULL DEFAULT 0 CHECK (continuity_days BETWEEN 0 AND 365),
  status TEXT NOT NULL DEFAULT 'DRAFT' CHECK (status IN ('DRAFT','EVIDENCE_PENDING','INDEPENDENT_REVIEW_PENDING','APPROVED_HONOUR_ONLY','REJECTED','REVOKED')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_mudra_evidence (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id UUID NOT NULL REFERENCES yatharth_mudra_cases(id),
  level SMALLINT NOT NULL CHECK (level BETWEEN 1 AND 7),
  evidence_sha256 TEXT NOT NULL CHECK (evidence_sha256 ~ '^[a-f0-9]{64}$'),
  evidence_type TEXT NOT NULL,
  public_metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
  private_storage_ref TEXT,
  submitted_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(case_id, level, evidence_sha256)
);

CREATE TABLE IF NOT EXISTS yatharth_mudra_reviews (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id UUID NOT NULL REFERENCES yatharth_mudra_cases(id),
  reviewer_id TEXT NOT NULL,
  decision TEXT NOT NULL CHECK (decision IN ('PENDING','ACCEPT','REJECT')),
  conflict_checked BOOLEAN NOT NULL DEFAULT FALSE,
  conflict_declared BOOLEAN NOT NULL DEFAULT FALSE,
  evidence_digest TEXT NOT NULL CHECK (evidence_digest ~ '^[a-f0-9]{64}$'),
  signature_ref TEXT NOT NULL,
  reviewed_at TIMESTAMPTZ,
  UNIQUE(case_id, reviewer_id),
  CHECK (NOT conflict_declared)
);

CREATE TABLE IF NOT EXISTS yatharth_mudra_audit_events (
  id BIGSERIAL PRIMARY KEY,
  case_id UUID NOT NULL REFERENCES yatharth_mudra_cases(id),
  event_type TEXT NOT NULL,
  event_payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  previous_event_hash TEXT,
  event_hash TEXT NOT NULL CHECK (event_hash ~ '^[a-f0-9]{64}$'),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS yatharth_mudra_certificates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  case_id UUID NOT NULL UNIQUE REFERENCES yatharth_mudra_cases(id),
  certificate_hash TEXT NOT NULL UNIQUE CHECK (certificate_hash ~ '^[a-f0-9]{64}$'),
  canonicalization TEXT NOT NULL DEFAULT 'RFC8785-JCS',
  issued_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  status TEXT NOT NULL DEFAULT 'ISSUED' CHECK (status IN ('ISSUED','REVOKED')),
  legal_boundary TEXT NOT NULL DEFAULT 'HONOUR ONLY; NOT LEGAL TENDER; NOT REDEEMABLE; NO PAYMENT OBLIGATION'
);

-- Reviews, evidence and audit events are append-only. Corrections use new rows/events.
CREATE OR REPLACE FUNCTION yatharth_mudra_reject_mutation()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  RAISE EXCEPTION 'Yatharth Mudra evidence/review/audit records are append-only; add a correction event instead';
END;
$$;

DROP TRIGGER IF EXISTS yatharth_evidence_no_mutation ON yatharth_mudra_evidence;
CREATE TRIGGER yatharth_evidence_no_mutation BEFORE UPDATE OR DELETE ON yatharth_mudra_evidence
FOR EACH ROW EXECUTE FUNCTION yatharth_mudra_reject_mutation();
DROP TRIGGER IF EXISTS yatharth_reviews_no_mutation ON yatharth_mudra_reviews;
CREATE TRIGGER yatharth_reviews_no_mutation BEFORE UPDATE OR DELETE ON yatharth_mudra_reviews
FOR EACH ROW EXECUTE FUNCTION yatharth_mudra_reject_mutation();
DROP TRIGGER IF EXISTS yatharth_audit_no_mutation ON yatharth_mudra_audit_events;
CREATE TRIGGER yatharth_audit_no_mutation BEFORE UPDATE OR DELETE ON yatharth_mudra_audit_events
FOR EACH ROW EXECUTE FUNCTION yatharth_mudra_reject_mutation();

-- IMPORTANT: do not grant public INSERT/UPDATE on these tables.
-- Configure least-privilege server roles, reviewer authentication, RLS and
-- private evidence storage before connecting an application.
