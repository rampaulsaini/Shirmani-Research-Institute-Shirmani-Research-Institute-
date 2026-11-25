-- Guest service-order lifecycle for consented public enquiries.
-- Apply after schema.sql and migrations 003/004. Does not create synthetic customer accounts.
create table if not exists guest_service_orders (
  id uuid primary key default gen_random_uuid(),
  enquiry_id uuid not null unique references client_enquiries(id) on delete restrict,
  scope text not null check (length(trim(scope)) between 1 and 5000),
  amount_minor bigint not null check (amount_minor > 0),
  currency char(3) not null default 'INR' check (currency = 'INR'),
  deadline text not null check (length(trim(deadline)) between 1 and 160),
  revision_limit integer not null check (revision_limit between 0 and 10),
  written_acceptance_reference text not null
    check (written_acceptance_reference ~ '^private://[A-Za-z0-9/_-]{1,960}$'),
  accepted_at timestamptz not null default now(),
  status text not null default 'awaiting_payment'
    check (status in ('awaiting_payment','paid','delivered','completed','cancelled')),
  delivery_reference text,
  delivered_at timestamptz,
  customer_acceptance_reference text,
  customer_accepted_at timestamptz,
  created_by uuid not null references accounts(id) on delete restrict,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  check ((delivery_reference is null and delivered_at is null) or (delivery_reference is not null and delivered_at is not null)),
  check ((customer_acceptance_reference is null and customer_accepted_at is null) or (customer_acceptance_reference is not null and customer_accepted_at is not null)),
  check (delivery_reference is null or delivery_reference ~ '^private://[A-Za-z0-9/_-]{1,960}$'),
  check (customer_acceptance_reference is null or customer_acceptance_reference ~ '^private://[A-Za-z0-9/_-]{1,960}$')
);
create index if not exists guest_service_orders_status_idx
  on guest_service_orders(status, created_at desc);

create table if not exists guest_service_payment_proofs (
  id uuid primary key default gen_random_uuid(),
  service_order_id uuid not null references guest_service_orders(id) on delete restrict,
  amount_minor bigint not null check (amount_minor > 0),
  currency char(3) not null check (currency = 'INR'),
  payment_reference text not null unique check (length(trim(payment_reference)) between 1 and 200),
  evidence_reference text not null
    check (evidence_reference ~ '^private://[A-Za-z0-9/_-]{1,960}$'),
  customer_consent boolean not null check (customer_consent = true),
  verification_status text not null default 'pending'
    check (verification_status in ('pending','verified','rejected')),
  verification_method text check (verification_method in ('owner_bank_statement')),
  verified_by uuid references accounts(id) on delete set null,
  verified_at timestamptz,
  created_at timestamptz not null default now(),
  check (
    (verification_status = 'verified' and verification_method = 'owner_bank_statement' and verified_by is not null and verified_at is not null)
    or verification_status <> 'verified'
  )
);
create unique index if not exists guest_service_one_open_proof_per_order
  on guest_service_payment_proofs(service_order_id)
  where verification_status in ('pending','verified');
create index if not exists guest_service_verified_income_idx
  on guest_service_payment_proofs(verified_at desc)
  where verification_status='verified';

comment on table guest_service_orders is
'Guest customer orders linked to consented enquiries; no synthetic account or marketplace listing is created.';
comment on table guest_service_payment_proofs is
'Private guest-service payment evidence. Verified means owner-attested recipient bank-credit match, not independent audit.';
