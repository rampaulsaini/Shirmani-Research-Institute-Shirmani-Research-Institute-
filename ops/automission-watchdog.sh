#!/usr/bin/env bash
set -euo pipefail

: "${PROJECT_DIR:=/opt/shirmani/Shirmani-Research-Institute-Shirmani-Research-Institute-}"
: "${COMPOSE_FILE:=${PROJECT_DIR}/automission-runtime/docker-compose.yml}"
SERVICE="automission"

cd "$PROJECT_DIR"
compose=(docker compose --project-directory "$PROJECT_DIR" -f "$COMPOSE_FILE")

container_id="$("${compose[@]}" ps -q "$SERVICE" 2>/dev/null || true)"
if [[ -z "$container_id" ]]; then
  echo "Automission container missing; starting service"
  "${compose[@]}" up -d "$SERVICE"
  exit 0
fi

state="$(docker inspect --format '{{.State.Status}}' "$container_id")"
health="$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$container_id")"

if [[ "$state" != "running" ]]; then
  echo "Automission container state=$state; starting service"
  "${compose[@]}" up -d "$SERVICE"
elif [[ "$health" == "unhealthy" ]]; then
  echo "Automission heartbeat unhealthy; restarting service"
  "${compose[@]}" restart "$SERVICE"
elif [[ "$health" == "none" ]]; then
  echo "Automission healthcheck missing; refusing to report healthy"
  exit 1
else
  echo "Automission container state=$state health=$health"
fi
