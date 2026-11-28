import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { once } from "node:events";
import net from "node:net";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
import pg from "pg";
import jwt from "jsonwebtoken";

const { Pool } = pg;
const databaseUrl = process.env.DATABASE_URL;

test("guest service order completes the owner-only HTTP lifecycle against PostgreSQL", {
  skip: !databaseUrl ? "DATABASE_URL is required for the disposable PostgreSQL integration test" : false,
  timeout: 45_000
}, async () => {
  const pool = new Pool({ connectionString: databaseUrl, max: 2 });
  const suffix = `${Date.now()}-${Math.random().toString(16).slice(2)}`;
  const ownerEmail = `sri-http-owner-${suffix}@example.invalid`;
  const customerEmail = `sri-http-customer-${suffix}@example.invalid`;
  const ordinaryEmail = `sri-http-user-${suffix}@example.invalid`;
  const jwtSecret = `integration-only-${suffix}-secret`;
  let ownerId;
  let ordinaryId;
  let enquiryId;
  let orderId;
  let proofId;
  let child;
  let baseUrl;

  const jsonRequest = async (path, { method = "GET", token, body } = {}) => {
    const response = await fetch(`${baseUrl}${path}`, {
      method,
      headers: {
        ...(token ? { authorization: `Bearer ${token}` } : {}),
        ...(body ? { "content-type": "application/json" } : {})
      },
      ...(body ? { body: JSON.stringify(body) } : {})
    });
    const data = await response.json();
    return { status: response.status, data };
  };

  let portServer;
  try {
    const owner = await pool.query(
      "insert into accounts(email,password_hash) values($1,$2) returning id",
      [ownerEmail, "integration-test-only-not-a-password"]
    );
    ownerId = owner.rows[0].id;
    const ordinary = await pool.query(
      "insert into accounts(email,password_hash) values($1,$2) returning id",
      [ordinaryEmail, "integration-test-only-not-a-password"]
    );
    ordinaryId = ordinary.rows[0].id;

    portServer = net.createServer();
    portServer.listen(0, "127.0.0.1");
    await once(portServer, "listening");
    const address = portServer.address();
    const port = address.port;
    await new Promise(resolve => portServer.close(resolve));
    portServer = null;
    baseUrl = `http://127.0.0.1:${port}`;

    const entrypoint = fileURLToPath(new URL("../src/index.js", import.meta.url));
    child = spawn(process.execPath, [entrypoint], {
      cwd: fileURLToPath(new URL("..", import.meta.url)),
      env: {
        ...process.env,
        NODE_ENV: "test",
        PORT: String(port),
        DATABASE_URL: databaseUrl,
        JWT_SECRET: jwtSecret,
        OWNER_ACCOUNT_ID: ownerId,
        OWNER_EMAIL: ownerEmail
      },
      stdio: "ignore"
    });

    const ownerToken = jwt.sign({ sub: ownerId }, jwtSecret, {
      expiresIn: "5m",
      issuer: "shirmani-social-api"
    });
    const ordinaryToken = jwt.sign({ sub: ordinaryId }, jwtSecret, {
      expiresIn: "5m",
      issuer: "shirmani-social-api"
    });

    let ready = false;
    for (let attempt = 0; attempt < 60; attempt += 1) {
      if (child.exitCode !== null) throw new Error(`API process exited before readiness: ${child.exitCode}`);
      try {
        const response = await fetch(`${baseUrl}/health`);
        if (response.ok) { ready = true; break; }
      } catch {}
      await new Promise(resolve => setTimeout(resolve, 250));
    }
    assert.equal(ready, true, "API server should become healthy");

    const before = await jsonRequest("/api/status");
    assert.equal(before.status, 200);
    const beforeIncome = BigInt(before.data.counters.income_inr_minor || "0");
    const beforeOwnerAttested = BigInt(before.data.income_assurance.owner_attested_bank_match_inr_minor || "0");
    const beforeProviderVerified = BigInt(before.data.income_assurance.provider_verified_payment_inr_minor || "0");
    const beforeOrders = Number(before.data.counters.guest_service_orders || 0);

    assert.equal((await jsonRequest("/api/owner/service-orders")).status, 401,
      "owner inbox must reject requests without authentication");
    assert.equal((await jsonRequest("/api/owner/service-orders", { token: ordinaryToken })).status, 403,
      "owner inbox must reject authenticated non-owners");

    const enquiry = await jsonRequest("/v1/enquiries", {
      method: "POST",
      body: {
        name: "Integration Customer",
        email: customerEmail,
        service: "SRI-SVC-001",
        language: "English",
        topic: "HTTP lifecycle integration",
        goal: "Exercise the guest order flow",
        consent: true
      }
    });
    assert.equal(enquiry.status, 201, JSON.stringify(enquiry.data));
    enquiryId = enquiry.data.id;

    const orderPayload = {
      scope: "Hindi-English writing, up to 500 words",
      amount_minor: 99900,
      currency: "INR",
      deadline: "2 working days",
      revision_limit: 1,
      written_acceptance_reference: `private://integration/acceptance-${suffix}`
    };
    const created = await jsonRequest(`/api/owner/enquiries/${enquiryId}/convert-to-service-order`, {
      method: "POST", token: ownerToken, body: orderPayload
    });
    assert.equal(created.status, 201, JSON.stringify(created.data));
    assert.equal(created.data.payment_status, "NOT_PAID");
    orderId = created.data.id;

    const duplicateOrder = await jsonRequest(`/api/owner/enquiries/${enquiryId}/convert-to-service-order`, {
      method: "POST", token: ownerToken, body: orderPayload
    });
    assert.equal(duplicateOrder.status, 200);
    assert.equal(duplicateOrder.data.duplicate, true);
    assert.equal(duplicateOrder.data.id, orderId);

    const missingConsent = await jsonRequest(`/api/owner/service-orders/${orderId}/payment-proof`, {
      method: "POST", token: ownerToken,
      body: {
        payment_reference: `payment-no-consent-${suffix}`,
        evidence_reference: `private://integration/payment-${suffix}`,
        customer_consent_reference: `private://integration/consent-${suffix}`,
        customer_consent: false
      }
    });
    assert.equal(missingConsent.status, 400);

    const proof = await jsonRequest(`/api/owner/service-orders/${orderId}/payment-proof`, {
      method: "POST", token: ownerToken,
      body: {
        payment_reference: `payment-${suffix}`,
        evidence_reference: `private://integration/payment-${suffix}`,
        customer_consent_reference: `private://integration/consent-${suffix}`,
        customer_consent: true
      }
    });
    assert.equal(proof.status, 201, JSON.stringify(proof.data));
    assert.equal(proof.data.income, "PENDING_UNVERIFIED");
    proofId = proof.data.id;

    const prematureDelivery = await jsonRequest(`/api/owner/service-orders/${orderId}/deliver`, {
      method: "POST", token: ownerToken,
      body: { delivery_reference: `private://integration/delivery-${suffix}` }
    });
    assert.equal(prematureDelivery.status, 409);

    const unconfirmedPayment = await jsonRequest(`/api/owner/service-payment-proofs/${proofId}/verify`, {
      method: "POST", token: ownerToken, body: { confirm_bank_match: false }
    });
    assert.equal(unconfirmedPayment.status, 400);

    const verified = await jsonRequest(`/api/owner/service-payment-proofs/${proofId}/verify`, {
      method: "POST", token: ownerToken, body: { confirm_bank_match: true }
    });
    assert.equal(verified.status, 200, JSON.stringify(verified.data));
    assert.equal(verified.data.status, "paid");
    assert.equal(verified.data.verification_scope, "owner_attested_bank_match_not_independent_audit");

    const prematureAcceptance = await jsonRequest(`/api/owner/service-orders/${orderId}/customer-acceptance`, {
      method: "POST", token: ownerToken,
      body: {
        customer_confirmed: true,
        acceptance_reference: `private://integration/customer-acceptance-${suffix}`
      }
    });
    assert.equal(prematureAcceptance.status, 410,
      "owner-recorded customer acceptance must be disabled");

    assert.equal((await jsonRequest(`/api/owner/service-orders/${orderId}/acceptance-invitations`, { method: "POST", body: {} })).status, 401,
      "acceptance invitation issuance must require authentication");
    assert.equal((await jsonRequest(`/api/owner/service-orders/${orderId}/acceptance-invitations`, {
      token: ordinaryToken, method: "POST", body: {}
    })).status, 403, "acceptance invitation issuance must be owner-only");

    const prematureInvitation = await jsonRequest(`/api/owner/service-orders/${orderId}/acceptance-invitations`, {
      method: "POST", token: ownerToken, body: {}
    });
    assert.equal(prematureInvitation.status, 409,
      "acceptance invitations cannot be issued before delivery");

    const delivered = await jsonRequest(`/api/owner/service-orders/${orderId}/deliver`, {
      method: "POST", token: ownerToken,
      body: { delivery_reference: `private://integration/delivery-${suffix}` }
    });
    assert.equal(delivered.status, 200, JSON.stringify(delivered.data));
    assert.equal(delivered.data.status, "delivered");

    const issued = await jsonRequest(`/api/owner/service-orders/${orderId}/acceptance-invitations`, {
      method: "POST", token: ownerToken, body: {}
    });
    assert.equal(issued.status, 201, JSON.stringify(issued.data));
    assert.equal(issued.data.delivery_channel, "MANUAL_OUT_OF_BAND_REQUIRED");
    assert.match(issued.data.token, /^[A-Za-z0-9_-]{40,60}$/);
    assert.equal(JSON.stringify(issued.data).includes(createHash("sha256").update(issued.data.token).digest("hex")), false,
      "API response must not expose the stored token hash");

    const invalidToken = await jsonRequest("/api/service-order-acceptance", {
      method: "POST", body: { token: "not-a-real-token", accepted: true }
    });
    assert.equal(invalidToken.status, 400);

    const missingCustomerConfirmation = await jsonRequest("/api/service-order-acceptance", {
      method: "POST", body: { token: issued.data.token, accepted: false }
    });
    assert.equal(missingCustomerConfirmation.status, 400);

    const tokenHash = createHash("sha256").update(issued.data.token).digest("hex");
    await pool.query(
      "update guest_service_acceptance_tokens set expires_at=now()-interval '1 minute' where token_hash=$1",
      [tokenHash]
    );
    const expired = await jsonRequest("/api/service-order-acceptance", {
      method: "POST", body: { token: issued.data.token, accepted: true }
    });
    assert.equal(expired.status, 410, "expired tokens must not complete an order");

    const renewed = await jsonRequest(`/api/owner/service-orders/${orderId}/acceptance-invitations`, {
      method: "POST", token: ownerToken, body: {}
    });
    assert.equal(renewed.status, 201);
    const revokedOldToken = await jsonRequest("/api/service-order-acceptance", {
      method: "POST", body: { token: issued.data.token, accepted: true }
    });
    assert.equal(revokedOldToken.status, 404, "reissuing must revoke the previous token");

    const concurrentAcceptances = await Promise.all([
      jsonRequest("/api/service-order-acceptance", {
        method: "POST", body: { token: renewed.data.token, accepted: true }
      }),
      jsonRequest("/api/service-order-acceptance", {
        method: "POST", body: { token: renewed.data.token, accepted: true }
      })
    ]);
    const accepted = concurrentAcceptances.find(result => result.status === 200);
    const replayed = concurrentAcceptances.find(result => result.status === 409);
    assert.ok(accepted, JSON.stringify(concurrentAcceptances));
    assert.ok(replayed, "a concurrent replay must be rejected: " + JSON.stringify(concurrentAcceptances));
    assert.equal(accepted.data.status, "completed");
    assert.equal(accepted.data.customer_acceptance_method, "single_use_token");
    assert.equal(accepted.data.acceptance_scope, "single_use_bearer_token_possession_not_identity_verified");
    assert.equal(concurrentAcceptances.filter(result => result.status === 200).length, 1,
      "exactly one concurrent customer acceptance may succeed");

    const inbox = await jsonRequest("/api/owner/service-orders", { token: ownerToken });
    assert.equal(inbox.status, 200);
    assert.ok(inbox.data.items.some(item => item.id === orderId && item.email === customerEmail));

    const after = await jsonRequest("/api/status");
    assert.equal(after.status, 200);
    assert.equal(Number(after.data.counters.guest_service_orders), beforeOrders + 1);
    assert.equal(BigInt(after.data.counters.income_inr_minor) - beforeIncome, 99900n);
    assert.equal(BigInt(after.data.income_assurance.owner_attested_bank_match_inr_minor) - beforeOwnerAttested, 99900n);
    assert.equal(after.data.income_assurance.provider_verified_payment_inr_minor, null,
      "provider-verified totals remain unavailable until signed server-side verification exists");
    assert.match(after.data.income_assurance.meaning, /not independently audited/);

    assert.equal((await jsonRequest("/api/export-income")).status, 401,
      "income export must reject unauthenticated requests");
    assert.equal((await jsonRequest("/api/export-income", { token: ordinaryToken })).status, 403,
      "income export must remain owner-only");
    const incomeExport = await jsonRequest("/api/export-income", { token: ownerToken });
    assert.equal(incomeExport.status, 200, JSON.stringify(incomeExport.data));
    assert.equal(BigInt(incomeExport.data.owner_attested_total_minor_units),
      BigInt(after.data.counters.income_inr_minor),
      "owner export total must reconcile with the public aggregate");
    assert.equal(Number(incomeExport.data.owner_attested_payment_records),
      Number(after.data.counters.paid_orders || 0) + Number(after.data.counters.guest_paid_orders || 0),
      "owner export must include both legacy and guest-service proof counts");
    assert.ok(incomeExport.data.records.some(row =>
      row.source === "guest_service_payment_proofs" && row.service_order_id === orderId &&
      BigInt(row.amount_minor) === 99900n
    ), "owner export must include the verified guest-service payment with its source");
    assert.match(incomeExport.data.verification_basis, /not_independently_audited/);

    const csvExport = await fetch(`${baseUrl}/api/export-income?format=csv`, {
      headers: { authorization: `Bearer ${ownerToken}` }
    });
    assert.equal(csvExport.status, 200);
    const csvText = await csvExport.text();
    assert.match(csvText.split(/\r?\n/)[0], /source/);
    assert.match(csvText, /guest_service_payment_proofs/);
    assert.equal(csvText.includes(customerEmail), false,
      "income export must not include customer contact details");
    assert.equal(JSON.stringify(after.data).includes(customerEmail), false,
      "public aggregate status must not expose customer contact data");
    assert.equal(JSON.stringify(after.data).includes("Integration Customer"), false,
      "public aggregate status must not expose customer names");
  } finally {
    if (child && child.exitCode === null) {
      child.kill("SIGTERM");
      await Promise.race([once(child, "exit"), new Promise(resolve => setTimeout(resolve, 3000))]);
      if (child.exitCode === null) child.kill("SIGKILL");
    }
    if (portServer) await new Promise(resolve => portServer.close(resolve));
    if (proofId) await pool.query("delete from guest_service_payment_proofs where id=$1", [proofId]);
    if (orderId) await pool.query("delete from guest_service_orders where id=$1", [orderId]);
    if (enquiryId) await pool.query("delete from client_enquiries where id=$1", [enquiryId]);
    if (ownerId) await pool.query("delete from accounts where id=$1", [ownerId]);
    if (ordinaryId) await pool.query("delete from accounts where id=$1", [ordinaryId]);
    await pool.end();
  }
});
