-- One-time bearer-token customer acceptance for guest service orders.
-- Apply after 005_guest_service_order_lifecycle.sql.
-- Possession of the token is recorded; it does not verify the recipient's legal identity.

alter table guest_service_orders
  add column if not exists customer_acceptance_method text;

-- Preserve historical owner-recorded rows while allowing token acceptance without
-- pretending that a private evidence file was uploaded.
update guest_service_orders
set customer_acceptance_method = 'owner_recorded'
where customer_accepted_at is not null
  and customer_acceptance_method is null;

do $$
declare
  constraint_row record;
begin
  for constraint_row in
    select conname
    from pg_constraint
    where conrelid = 'guest_service_orders'::regclass
      and contype = 'c'
      and pg_get_constraintdef(oid) ilike '%customer_acceptance_reference%'
      and pg_get_constraintdef(oid) ilike '%customer_accepted_at%'
      and pg_get_constraintdef(oid) ilike '%IS NULL%'
  loop
    execute format('alter table guest_service_orders drop constraint %I', constraint_row.conname);
  end loop;
end $$;

alter table guest_service_orders
  drop constraint if exists guest_service_orders_customer_acceptance_method_check,
  add constraint guest_service_orders_customer_acceptance_method_check
    check (customer_acceptance_method is null or customer_acceptance_method in ('owner_recorded','single_use_token')),
  drop constraint if exists guest_service_orders_customer_acceptance_state_check,
  add constraint guest_service_orders_customer_acceptance_state_check
    check (
      (customer_accepted_at is null and customer_acceptance_method is null and customer_acceptance_reference is null)
      or
      (customer_accepted_at is not null and customer_acceptance_method is not null)
    );

create table if not exists guest_service_acceptance_tokens (
  id uuid primary key default gen_random_uuid(),
  service_order_id uuid not null references guest_service_orders(id) on delete cascade,
  token_hash char(64) not null unique check (token_hash ~ '^[a-f0-9]{64}$'),
  expires_at timestamptz not null,
  consumed_at timestamptz,
  revoked_at timestamptz,
  issued_by uuid not null references accounts(id) on delete restrict,
  created_at timestamptz not null default now()
);

create index if not exists guest_service_acceptance_tokens_order_idx
  on guest_service_acceptance_tokens(service_order_id, created_at desc);

create unique index if not exists guest_service_one_active_acceptance_token
  on guest_service_acceptance_tokens(service_order_id)
  where consumed_at is null and revoked_at is null;

comment on table guest_service_acceptance_tokens is
'Hashed one-time bearer tokens for guest service-order acceptance. Raw tokens are returned once to the owner for manual out-of-band delivery; possession does not independently verify identity.';
comment on column guest_service_orders.customer_acceptance_method is
'Acceptance source: owner_recorded (legacy) or single_use_token (bearer possession; not identity verification).';
