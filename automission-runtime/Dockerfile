FROM python:3.12-slim
WORKDIR /app
COPY automission-runtime/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY income /app/income
COPY automission-runtime /app/automission-runtime
ENV PYTHONUNBUFFERED=1
ENV AUTOMISSION_HEARTBEAT_SECONDS=300
ENV AUTOMISSION_STATE_DIR=/app/automission-runtime/state
CMD ["python","/app/automission-runtime/worker.py"]
