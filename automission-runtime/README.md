# Standalone Automission Runtime

This runtime is designed to operate independently of ChatGPT. ChatGPT is not a runtime dependency.

## Operating model

A persistent host/container runs the worker continuously. The worker:
1. loads the income control-plane contracts;
2. emits heartbeats;
3. discovers only configured sources;
4. normalizes and deduplicates opportunities;
5. verifies evidence;
6. places permitted work into a durable queue;
7. records outcomes and verified revenue evidence;
8. retries recoverable failures and fails closed on unsafe states.

External credentials and platform APIs are injected through environment variables or a secret manager. No credentials are stored in the repository.

## Deployment

Use Docker Compose on a VPS/server or equivalent always-on host. GitHub Actions is used for CI/health checks, not as the sole 24/7 runtime.

The worker deliberately does not claim income or perform irreversible actions without the configured authorization boundary.
