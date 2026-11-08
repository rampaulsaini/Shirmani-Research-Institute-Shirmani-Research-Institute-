// Parse the configured CORS origins once and share the canonical allowlist.
// Empty entries and wildcard entries are never treated as trusted origins.
export function parseAllowedOrigins(value) {
  return new Set((value || "").split(",").map(origin => origin.trim()).filter(origin => origin && origin !== "*"));
}
