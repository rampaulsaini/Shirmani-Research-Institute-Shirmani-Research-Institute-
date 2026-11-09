FROM python:3.12-slim
WORKDIR /app
COPY lead_agent.py /app/lead_agent.py
COPY tests /app/tests
RUN useradd --create-home --uid 10001 app && mkdir -p /data && chown -R app:app /data /app
USER app
ENV LEAD_DB_PATH=/data/leads.sqlite3
CMD ["python","lead_agent.py","init"]
