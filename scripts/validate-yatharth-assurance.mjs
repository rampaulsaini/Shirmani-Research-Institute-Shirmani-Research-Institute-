import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const registryPath = path.join(root, "docs/public-platform/public-capability-registry.json");
const apiPath = path.join(root, "server/src/index.js");
const checks = [];

const fail = (message) => checks.push({ id: "check-" + (checks.length + 1), status: "FAIL", message });
const pass = (message) => checks.push({ id: "check-" + (checks.length + 1), status: "PASS", message });
const warn = (message) => checks.push({ id: "check-" + (checks.length + 1), status: "WARN", message });

if (!fs.existsSync(registryPath)) {
  console.error("ASSURANCE_FAIL: capability registry is missing");
  process.exit(1);
}
if (!fs.existsSync(apiPath)) {
  console.error("ASSURANCE_FAIL: API source is missing");
  process.exit(1);
}

const registry = JSON.parse(fs.readFileSync(registryPath, "utf8"));
const api = fs.readFileSync(apiPath, "utf8");
const states = Array.isArray(registry.status_model) ? registry.status_model : [];
const capabilities = registry.capability_states && typeof registry.capability_states === "object"
  ? registry.capability_states
  : {};

if (!states.length) fail("Registry status_model is empty.");
else pass("Registry exposes " + states.length + " capability states.");

const stateSet = new Set(states);
const domainNames = Array.isArray(registry.domains) ? registry.domains : Object.keys(capabilities);
const duplicateDomains = domainNames.filter((d, i) => domainNames.indexOf(d) !== i);

if (!domainNames.length) fail("Registry contains no domains.");
if (duplicateDomains.length) fail("Duplicate domain declarations: " + [...new Set(duplicateDomains)].join(", "));
if (Object.keys(capabilities).length !== domainNames.length) {
  fail("Domain inventory and capability_states inventory have different sizes.");
} else {
  pass("Domain inventory and capability_states inventory have matching cardinality.");
}

for (const domain of domainNames) {
  const state = capabilities[domain];
  if (!state) fail("Missing capability state for domain: " + domain);
  else if (!stateSet.has(state)) fail("Unknown state " + state + " for domain: " + domain);
}

const modelMatch = api.match(/status_model:\s*\[([^\]]+)\]/);
if (!modelMatch) {
  fail("API /v1/capabilities/status does not expose a machine-readable status_model.");
} else {
  const apiStates = [...modelMatch[1].matchAll(/"([^"]+)"/g)].map((m) => m[1]);
  if (JSON.stringify(apiStates) !== JSON.stringify(states)) {
    fail("API status_model differs from registry: API=" + JSON.stringify(apiStates) + " registry=" + JSON.stringify(states));
  } else {
    pass("API status_model exactly matches registry status_model.");
  }
}

const apiCapabilityMatches = [...api.matchAll(/\{ id: "([^"]+)", status: "([^"]+)" \}/g)];
const apiCapabilities = new Map(apiCapabilityMatches.map((m) => [m[1], m[2]]));
const operationalThreshold = new Set(["MVP", "TESTED", "DEPLOYMENT_GATED", "LIVE", "AUTOMATED", "INDEPENDENTLY_VERIFIED"]);

for (const [domain, state] of Object.entries(capabilities)) {
  if (operationalThreshold.has(state) && !apiCapabilities.has(domain)) {
    fail("Operational capability " + domain + " is " + state + " but absent from /v1/capabilities/status.");
  }
}

const registryOperational = Object.values(capabilities).filter((s) => operationalThreshold.has(s)).length;
if (registryOperational) pass(registryOperational + " capability declarations are at or above MVP and were checked for API parity.");
else warn("No capability is currently declared at or above MVP.");

const live = Object.entries(capabilities).filter(([, s]) => s === "LIVE");
const verified = Object.entries(capabilities).filter(([, s]) => s === "INDEPENDENTLY_VERIFIED");
const automated = Object.entries(capabilities).filter(([, s]) => s === "AUTOMATED");

const deploymentEvidence = path.join(root, "docs/public-platform/deployment-evidence.json");
if (live.length && !fs.existsSync(deploymentEvidence)) {
  fail("LIVE capability declarations exist (" + live.map(([d]) => d).join(", ") + ") but deployment-evidence.json is absent.");
} else if (live.length) {
  pass("LIVE declarations have a deployment evidence record.");
} else {
  pass("No capability is declared LIVE.");
}

const verificationDir = path.join(root, "evidence/independent-verification");
if (verified.length && !fs.existsSync(verificationDir)) {
  fail("INDEPENDENTLY_VERIFIED is declared but the independent-verification evidence directory is absent.");
} else if (verified.length) {
  pass("Independent-verification evidence directory exists for verified declarations.");
} else {
  pass("No capability is declared INDEPENDENTLY_VERIFIED.");
}

if (automated.length) pass("AUTOMATED declarations are present and remain explicit in the public registry.");
else pass("No capability is declared AUTOMATED in the public registry.");

const failures = checks.filter((c) => c.status === "FAIL").length;
const report = {
  version: "1.0",
  generated_at: new Date().toISOString(),
  source_registry: "docs/public-platform/public-capability-registry.json",
  summary: {
    domains: domainNames.length,
    operational: registryOperational,
    architecture_only: Object.values(capabilities).filter((s) => s === "ARCHITECTURE" || s === "PLANNED").length,
    failures
  },
  checks
};

console.log(JSON.stringify(report, null, 2));
if (failures) process.exit(1);
