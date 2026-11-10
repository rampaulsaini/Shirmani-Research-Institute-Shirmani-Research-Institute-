-- Separate delivery and customer-acceptance evidence from payment verification.
-- Apply after migration 003_private_income_proof.sql.
alter table orders
  add column if not exists delivery_reference text,
  add column if not exists delivered_at timestamptz,
  add column if not exists customer_acceptance_reference text,
  add column if not exists customer_accepted_at timestamptz;

alter table orders
  drop constraint if exists orders_delivery_reference_private_check,
  add constraint orders_delivery_reference_private_check
    check (delivery_reference is null or delivery_reference ~ '^private://[A-Za-z0-9/_-]{1,960}$'),
  drop constraint if exists orders_acceptance_reference_private_check,
  add constraint orders_acceptance_reference_private_check
    check (customer_acceptance_reference is null or customer_acceptance_reference ~ '^private://[A-Za-z0-9/_-]{1,960}$'),
  drop constraint if exists orders_delivery_timestamp_check,
  add constraint orders_delivery_timestamp_check
    check ((delivery_reference is null and delivered_at is null) or (delivery_reference is not null and delivered_at is not null)),
  drop constraint if exists orders_acceptance_timestamp_check,
  add constraint orders_acceptance_timestamp_check
    check ((customer_acceptance_reference is null and customer_accepted_at is null) or (customer_acceptance_reference is not null and customer_accepted_at is not null));

comment on column orders.delivery_reference is
'Private evidence locator for delivery. Never store public links or customer personal data.';
comment on column orders.customer_acceptance_reference is
'Private evidence locator for explicit customer acceptance; owner-recorded, not independent audit.';
