# Automission 24/7 Host Deployment

The worker is independent of ChatGPT. GitHub Actions validates code and contracts; it is not the persistent worker host. A continuously running VPS/server is required.

## Deploy

1. Provision an always-on Linux host with Docker Engine and the Docker Compose plugin.
2. Clone this repository to `/opt/shirmani/Shirmani-Research-Institute-Shirmani-Research-Institute-`.
3. Review `automission-runtime/.env.example`; create a protected `.env` file on the host. Keep provider credentials out of Git and restrict file permissions (for example, `chmod 600 .env`).
4. Configure only real, authorized adapters and source feeds. Empty adapter variables mean those channels are not connected; the worker must not be described as executing those external services.
5. Start the worker from the repository root: `docker compose -f automission-runtime/docker-compose.yml up -d --build`.
6. Install the host watchdog:
   - Copy `ops/automission-watchdog.sh` to `/usr/local/bin/shirmani-automission-watchdog` and make it executable.
   - Copy both files in `ops/systemd/` to `/etc/systemd/system/`.
   - If the repository path differs, update `PROJECT_DIR` and `COMPOSE_FILE` in the service unit.
   - Run `systemctl daemon-reload`, `systemctl enable --now shirmani-automission-watchdog.timer`.
7. Verify with `docker compose -f automission-runtime/docker-compose.yml ps`, `docker compose -f automission-runtime/docker-compose.yml logs --tail=100 automission`, and `systemctl list-timers shirmani-automission-watchdog.timer`.

## Recovery and safety

- The container uses a persistent named volume for SQLite state and Docker's `restart: unless-stopped` policy.
- The container healthcheck now checks the age of the last successful worker heartbeat, not merely whether an old heartbeat row exists.
- The host-level systemd timer checks container health every two minutes and starts/restarts a missing, stopped, or unhealthy service.
- Queue retries, idempotency, stale-work recovery, and fail-closed authorization remain application-level controls.
- Payment, contracts, paid campaigns, external publication, withdrawals, and verified-income claims remain gated by explicit authorization and evidence.
- A single VPS is not high availability. For stronger resilience, use a second host, tested backups, remote monitoring from outside the host, and documented recovery drills.
- No software can guarantee zero downtime or zero-microsecond interruption. Confirm actual uptime from host monitoring after deployment.

## Deployment status

Adding these files to Git does not provision a server or activate the worker. Report the runtime as DEPLOYED only after the host is provisioned, the container is running, fresh heartbeats are observed, adapters are individually authorized, and an external monitor confirms availability.
