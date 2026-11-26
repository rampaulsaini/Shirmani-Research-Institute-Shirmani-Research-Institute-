\set ON_ERROR_STOP on
insert into accounts(email,password_hash)
values ('migration-test@example.invalid','not-a-real-password-hash');
insert into client_enquiries(service,language,topic,consent_at,email)
values ('SRI-SVC-001','English','Migration integration test',now(),'customer@example.invalid');
insert into guest_service_orders(
  enquiry_id,scope,amount_minor,currency,deadline,revision_limit,
  written_acceptance_reference,created_by
)
select e.id,'Test scope',99900,'INR','2 working days',1,
       'private://acceptance/test-1',a.id
from client_enquiries e cross join accounts a
where e.email='customer@example.invalid'
  and a.email='migration-test@example.invalid';
insert into guest_service_payment_proofs(
  service_order_id,amount_minor,currency,payment_reference,evidence_reference,
  customer_consent,customer_consent_reference
)
select id,99900,'INR','test-payment-reference-1',
       'private://evidence/test-1',true,'private://consent/test-1'
from guest_service_orders;
do $$
declare order_id uuid;
begin
  select id into order_id from guest_service_orders limit 1;
  begin
    insert into guest_service_payment_proofs(
      service_order_id,amount_minor,currency,payment_reference,evidence_reference,
      customer_consent,customer_consent_reference
    ) values (
      order_id,99900,'INR','test-payment-reference-invalid',
      'not-private-evidence',true,'private://consent/test-2'
    );
    raise exception 'Expected invalid evidence reference to be rejected';
  exception when check_violation then null;
  end;
end
$$;
do $$
declare order_id uuid;
begin
  select id into order_id from guest_service_orders limit 1;
  begin
    insert into guest_service_payment_proofs(
      service_order_id,amount_minor,currency,payment_reference,evidence_reference,
      customer_consent,customer_consent_reference
    ) values (
      order_id,99900,'INR','test-payment-reference-duplicate-open',
      'private://evidence/test-2',true,'private://consent/test-3'
    );
    raise exception 'Expected one-open-proof unique index to reject duplicate';
  exception when unique_violation then null;
  end;
end
$$;
select 'guest service-order migration integration: PASS' as result;
