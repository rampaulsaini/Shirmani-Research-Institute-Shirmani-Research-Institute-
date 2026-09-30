import assert from "node:assert/strict";
import test from "node:test";

test("public platform API reports degraded when production dependencies are absent", async () => {
  const previous = {
    port: process.env.PORT,
    database: process.env.DATABASE_URL,
    jwt: process.env.JWT_SECRET,
    nodeEnv: process.env.NODE_ENV
  };
  process.env.PORT = "8799";
  delete process.env.DATABASE_URL;
  delete process.env.JWT_SECRET;
  delete process.env.NODE_ENV;
  await import("../src/index.js?test=" + Date.now());
  await new Promise(resolve => setTimeout(resolve, 150));
  const response = await fetch("http://127.0.0.1:8799/health");
  const body = await response.json();
  assert.equal(response.status, 503);
  assert.equal(body.status, "DEGRADED");
  assert.equal(body.database, "NOT_CONFIGURED");
  process.env.PORT = previous.port;
  if (previous.database === undefined) delete process.env.DATABASE_URL; else process.env.DATABASE_URL = previous.database;
  if (previous.jwt === undefined) delete process.env.JWT_SECRET; else process.env.JWT_SECRET = previous.jwt;
  if (previous.nodeEnv === undefined) delete process.env.NODE_ENV; else process.env.NODE_ENV = previous.nodeEnv;
});
