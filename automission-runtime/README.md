# Standalone Automission Runtime

This runtime is designed to operate independently of ChatGPT. ChatGPT is not a runtime dependency.

## Operating model

A persistent host/container runs the worker continuously. The worker loads the income control-plane contracts, emits heartbeats, discovers configured sources, normalizes/deduplicates opportunities, verifies evidence, routes permitted work, captures learning features, and exposes a provider-agnostic connector boundary.

## Connector model

Each income channel can use a configured Python adapter implementing health(), discover(), prepare(item), and execute(item). Configure only authorized providers. Credentials belong in environment variables or a secret manager, never in Git.

## Deployment

Use Docker Compose on an always-on VPS/server. GitHub Actions is CI/health validation, not the sole 24/7 runtime. The container restarts unless stopped and has a watchdog healthcheck.

The worker does not fabricate opportunities, claim unverified revenue, or perform irreversible actions without authorization.
