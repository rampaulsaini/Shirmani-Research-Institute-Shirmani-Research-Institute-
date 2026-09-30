import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const registryPath = path.join(root, "docs/public-platform/public-capability-registry.json");
const apiPath = path.join(root, "server/src/index.js");
const deploymentEvidencePath = path.join(root, "docs/public-platform/deployment-evidence.json");
const verificationDir = path.join(root, "evidence/independent-verification");
const automationDir = path.join(root, "evidence/automation");
const checks = [];

const fail = (message) => checks.push({ id: "check-" + (checks.length + 1), status: "FAIL", message });
const pass = (message) => checks.push({ id: "check-" + (checks.length + 1), status: "PASS", message });
const warn = (message) => checks.push({ id: "check-" + (checks.length + 1), status: "WARN", message });

const readJson = (filePath, label) => {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch (error) {
    fail(label + " is not valid JSON: " + error.message);
    return null;
  }
};

if (!fs.existsSync(registryPath)) {
  console.error("ASSURANCE_FAIL: capability registry is missing");
  process.exit(1);
}
if (!fs.existsSync(apiPath)) {
  console.error("ASSURANCE_FAIL: API source is missing");
  process.exit(1);
}

const registry = readJson(registryPath, "Capability registry");
const api = fs.readFileSync(apiPath, "utf8");
if (!registry) process.exit(1);

const states = Array.isArray(registry.status_model) ? registry.status_model : [];
const capabilities = registry.capability_states && typeof registry.capability_states === "object"
  ? registry.capability_states
  : {};

if (!states.length) fail("Registry status_model is empty.");
else if (new Set(states).size !== states.length) fail("Registry status_model contains duplicate states.");
else pass("Registry exposes " + states.length + " unique capability states.");

const stateSet = new Set(states);
const domainNames = Array.isArray(registry.domains) ? registry.domains : [];
const capabilityNames = Object.keys(capabilities);
const domainSet = new Set(domainNames);
const capabilitySet = new Set(capabilityNames);

if (!domainNames.length) fail("Registry contains no domains.");
if (domainSet.size !== domainNames.length) fail("Registry domains contains duplicate declarations.");

const missingCapabilityStates = domainNames.filter((domain) => !capabilitySet.has(domain));
const orphanCapabilityStates = capabilityNames.filter((domain) => !domainSet.has(domain));
if (missingCapabilityStates.length) fail("Domains missing capability state: " + missingCapabilityStates.join(", "));
if (orphanCapabilityStates.length) fail("Capability states without declared domains: " + orphanCapabilityStates.join(", "));
if (!missingCapabilityStates.length && !orphanCapabilityStates.length) {
  pass("Domain inventory and capability_states keys match exactly.");
}

for (const domain of domainNames) {
  const state = capabilities[domain];
  if (!state) continue;
  if (!stateSet.has(state)) fail("Unknown state " + state + " for domain: " + domain);
}

const routeStart = api.indexOf('app.get("/v1/capabilities/status"');
const routeEnd = routeStart >= 0 ? api.indexOf("\n});", routeStart) : -1;
const capabilitySurface = routeStart >= 0 && routeEnd >= 0 ? api.slice(routeStart, routeEnd + 4) : "";
if (!capabilitySurface) {
  fail("API /v1/capabilities/status route is missing or structurally unreadable.");
}

const modelMatch = capabilitySurface.match(/status_model:\s*\[([^\]]+)\]/);
if (!modelMatch) {
  fail("API capability route does not expose a machine-readable status_model.");
} else {
  const apiStates = [...modelMatch[1].matchAll(/"([^"]+)"/g)].map((m) => m[1]);
  if (JSON.stringify(apiStates) !== JSON.stringify(states)) {
    fail("API status_model differs from registry.");
  } else {
    pass("API status_model exactly matches registry status_model.");
  }
}

const apiCapabilities = new Map();
for (const [, id, status] of capabilitySurface.matchAll(/\{ id: "([^"]+)", status: "([^"]+)" \}/g)) {
  if (apiCapabilities.has(id)) fail("Duplicate API capability declaration: " + id);
  apiCapabilities.set(id, status);
}

const operationalThreshold = new Set(["MVP", "TESTED", "DEPLOYMENT_GATED", "LIVE", "AUTOMATED", "INDEPENDENTLY_VERIFIED"]);

for (const [domain, state] of Object.entries(capabilities)) {
  if (operationalThreshold.has(state) && !apiCapabilities.has(domain)) {
    fail("Operational capability " + domain + " is " + state + " but absent from /v1/capabilities/status.");
  }
  if (operationalThreshold.has(state) && apiCapabilities.get(domain) !== state) {
    fail("Operational capability " + domain + " state mismatch: registry=" + state + " API=" + apiCapabilities.get(domain));
  }
}

const operationalApiOnly = [...apiCapabilities.keys()].filter((domain) => !capabilitySet.has(domain));
if (operationalApiOnly.length) fail("API exposes capability IDs absent from registry: " + operationalApiOnly.join(", "));

const registryOperational = Object.values(capabilities).filter((s) => operationalThreshold.has(s)).length;
if (registryOperational) pass(registryOperational + " capability declarations are at or above MVP and were checked for API parity.");
else warn("No capability is currently declared at or above MVP.");

const live = Object.entries(capabilities).filter(([, s]) => s === "LIVE");
const verified = Object.entries(capabilities).filter(([, s]) => s === "INDEPENDENTLY_VERIFIED");
const automated = Object.entries(capabilities).filter(([, s]) => s === "AUTOMATED");

if (live.length) {
  if (!fs.existsSync(deploymentEvidencePath)) {
    fail("LIVE capability declarations exist but deployment-evidence.json is absent.");
  } else {
    const evidence = readJson(deploymentEvidencePath, "Deployment evidence");
    if (evidence) {
      const records = evidence.capabilities && typeof evidence.capabilities === "object" ? evidence.capabilities : {};
      for (const [domain] of live) {
        const record = records[domain];
        if (!record || typeof record !== "object" || !record.url || !record.checked_at || !record.environment) {
          fail("LIVE capability " + domain + " lacks a complete deployment evidence record (url, checked_at, environment).");
        }
      }
      pass("LIVE declarations have capability-specific deployment evidence.");
    }
  }
} else {
  pass("No capability is declared LIVE.");
}

if (verified.length) {
  if (!fs.existsSync(verificationDir) || !fs.statSync(verificationDir).isDirectory()) {
    fail("INDEPENDENTLY_VERIFIED is declared but the independent-verification evidence directory is absent.");
  } else {
    for (const [domain] of verified) {
      const evidenceFile = path.join(verificationDir, domain + ".json");
      if (!fs.existsSync(evidenceFile)) {
        fail("INDEPENDENTLY_VERIFIED capability " + domain + " lacks dedicated evidence: evidence/independent-verification/" + domain + ".json");
      } else {
        const evidence = readJson(evidenceFile, "Independent verification evidence for " + domain);
        if (evidence && (!evidence.reviewer || !evidence.reviewed_at || !evidence.method || !evidence.conclusion)) {
          fail("Independent verification evidence for " + domain + " must include reviewer, reviewed_at, method and conclusion.");
        }
      }
    }
    if (!checks.some((c) => c.status === "FAIL" && c.message.includes("INDEPENDENTLY_VERIFIED capability"))) {
      pass("Every independently verified capability has a dedicated evidence record.");
    }
  }
} else {
  pass("No capability is declared INDEPENDENTLY_VERIFIED.");
}

if (automated.length) {
  if (!fs.existsSync(automationDir) || !fs.statSync(automationDir).isDirectory()) {
    fail("AUTOMATED is declared but evidence/automation is absent.");
  } else {
    for (const [domain] of automated) {
      const evidenceFile = path.join(automationDir, domain + ".json");
      if (!fs.existsSync(evidenceFile)) fail("AUTOMATED capability " + domain + " lacks dedicated automation evidence.");
    }
  }
  if (!automated.some(([domain]) => !operationalThreshold.has(capabilities[domain]))) {
    pass("AUTOMATED declarations remain explicit and require dedicated automation evidence.");
  }
} else {
  pass("No capability is declared AUTOMATED in the public registry.");
}

const failures = checks.filter((c) => c.status === "FAIL").length;
const report = {
  version: "1.1",
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

const reportPath = process.env.ASSURANCE_REPORT_PATH || path.join(root, "assurance-report.json");
fs.writeFileSync(reportPath, JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify(report, null, 2));
if (failures) process.exit(1);
