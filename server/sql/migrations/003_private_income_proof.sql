-- Private payment-proof ledger and evidence-gated income.
-- Apply after server/sql/schema.sql and migration 002.
-- screenshot_url must be a private object-storage locator, never a public share URL.
create table if not exists paid_orders (
  id uuid primary key default gen_random_uuid(),
  order_id uuid not null unique references orders(id) on delete restrict,
  amount_minor bigint not null check (amount_minor > 0),
  currency char(3) not null,
  payment_id text not null unique check (length(trim(payment_id)) between 1 and 200),
  upi_ref text not null unique check (length(trim(upi_ref)) between 1 and 200),
  screenshot_url text not null check (length(trim(screenshot_url)) between 1 and 1000),
  customer_consent boolean not null check (customer_consent = true),
  verification_status text not null default 'pending'
    check (verification_status in ('pending','verified','rejected')),
  verification_method text
    check (verification_method in ('owner_bank_statement','provider_verified')),
  verified_by uuid references accounts(id) on delete set null,
  verified_at timestamptz,
  created_at timestamptz not null default now(),
  check (
    (verification_status = 'verified' and verification_method is not null and verified_by is not null and verified_at is not null)
    or verification_status <> 'verified'
  )
);
create index if not exists paid_orders_verified_idx
  on paid_orders(verified_at desc) where verification_status='verified';
comment on table paid_orders is
'Private evidence ledger. Only consented records with a recorded verification method contribute to reported income; owner bank-statement checks are explicitly not independent audits.';
comment on column paid_orders.screenshot_url is
'Private object-storage key/locator only. Never store a public screenshot URL or commit evidence to Git.';
