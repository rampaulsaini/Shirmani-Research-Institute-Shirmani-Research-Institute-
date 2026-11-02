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
  decision TEXT NOT NULL CHECK (decision IN ('ACCEPT','REJECT')),
  conflict_checked BOOLEAN NOT NULL DEFAULT FALSE,
  conflict_declared BOOLEAN NOT NULL DEFAULT FALSE,
  evidence_digest TEXT NOT NULL CHECK (evidence_digest ~ '^[a-f0-9]{64}$'),
  signature_ref TEXT NOT NULL,
  reviewed_at TIMESTAMPTZ,
  UNIQUE(case_id, reviewer_id),
  CHECK (conflict_checked)
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

-- A certificate cannot be inserted unless all issuance gates are satisfied.
-- Conflict declarations remain recordable, but a conflicted reviewer cannot approve.
CREATE OR REPLACE FUNCTION yatharth_mudra_validate_certificate()
RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE
  v_case yatharth_mudra_cases%ROWTYPE;
  v_level_count INTEGER;
  v_review_count INTEGER;
  v_accept_count INTEGER;
  v_conflict_count INTEGER;
  v_digest_count INTEGER;
BEGIN
  SELECT * INTO v_case
  FROM yatharth_mudra_cases
  WHERE id = NEW.case_id
  FOR UPDATE;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'Yatharth Mudra case does not exist';
  END IF;
  IF NOT v_case.consent_recorded THEN
    RAISE EXCEPTION 'Recorded subject consent is required';
  END IF;
  IF v_case.continuity_days <> 365 THEN
    RAISE EXCEPTION '365 days of voluntary continuity evidence are required by policy';
  END IF;
  IF v_case.status IN ('REJECTED','REVOKED','APPROVED_HONOUR_ONLY') THEN
    RAISE EXCEPTION 'Case status does not permit certificate issuance';
  END IF;

  SELECT COUNT(DISTINCT level) INTO v_level_count
  FROM yatharth_mudra_evidence
  WHERE case_id = NEW.case_id AND level BETWEEN 1 AND 7;
  IF v_level_count <> 7 THEN
    RAISE EXCEPTION 'Evidence for all seven levels is required';
  END IF;

  SELECT COUNT(*),
         COUNT(*) FILTER (WHERE decision = 'ACCEPT'),
         COUNT(*) FILTER (WHERE conflict_declared),
         COUNT(DISTINCT evidence_digest)
    INTO v_review_count, v_accept_count, v_conflict_count, v_digest_count
  FROM yatharth_mudra_reviews
  WHERE case_id = NEW.case_id
    AND conflict_checked
    AND reviewed_at IS NOT NULL
    AND length(trim(signature_ref)) > 0;

  IF v_review_count <> 3 OR v_accept_count <> 3 THEN
    RAISE EXCEPTION 'Exactly three authenticated, independent ACCEPT reviews are required';
  END IF;
  IF v_conflict_count <> 0 THEN
    RAISE EXCEPTION 'A reviewer with a declared conflict cannot approve';
  END IF;
  IF v_digest_count <> 1 THEN
    RAISE EXCEPTION 'All reviewers must review the same evidence digest';
  END IF;

  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS yatharth_certificate_issue_gate ON yatharth_mudra_certificates;
CREATE TRIGGER yatharth_certificate_issue_gate
BEFORE INSERT ON yatharth_mudra_certificates
FOR EACH ROW EXECUTE FUNCTION yatharth_mudra_validate_certificate();

CREATE OR REPLACE FUNCTION yatharth_mudra_mark_case_approved()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  UPDATE yatharth_mudra_cases
     SET status = 'APPROVED_HONOUR_ONLY', updated_at = now()
   WHERE id = NEW.case_id;
  RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS yatharth_certificate_mark_case ON yatharth_mudra_certificates;
CREATE TRIGGER yatharth_certificate_mark_case
AFTER INSERT ON yatharth_mudra_certificates
FOR EACH ROW EXECUTE FUNCTION yatharth_mudra_mark_case_approved();
