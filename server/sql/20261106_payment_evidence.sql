-- Additive payment-evidence ledger. Apply after server/sql/schema.sql.
-- Never store public screenshot URLs; screenshot_storage_key must point to private object storage.
create table if not exists payment_evidence (
  id uuid primary key default gen_random_uuid(),
  order_id uuid not null references orders(id) on delete restrict,
  payment_id text,
  upi_ref text,
  screenshot_storage_key text,
  customer_consent_at timestamptz not null,
  amount_minor bigint not null check (amount_minor > 0),
  currency char(3) not null,
  verification_status text not null default 'pending'
    check (verification_status in ('pending','verified','rejected')),
  verification_source text,
  verified_by text,
  verified_at timestamptz,
  created_at timestamptz not null default now(),
  check (payment_id is not null or upi_ref is not null or screenshot_storage_key is not null),
  check (
    verification_status <> 'verified'
    or (verified_at is not null and verified_by is not null
        and verification_source is not null
        and (payment_id is not null or upi_ref is not null))
  )
);
create unique index if not exists payment_evidence_one_record_per_order
  on payment_evidence(order_id);
create index if not exists payment_evidence_order_idx
  on payment_evidence(order_id, created_at desc);
create index if not exists payment_evidence_verified_idx
  on payment_evidence(verified_at desc)
  where verification_status = 'verified';
create unique index if not exists payment_evidence_payment_id_unique
  on payment_evidence(payment_id) where payment_id is not null;
create unique index if not exists payment_evidence_upi_ref_unique
  on payment_evidence(upi_ref) where upi_ref is not null;
