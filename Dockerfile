# --- web: React + TypeScript front end, built to static files ---
FROM node:24-alpine AS web
WORKDIR /web
COPY web/package.json web/package-lock.json ./
RUN npm ci --no-audit --no-fund
COPY web ./
RUN npm run build -- --outDir /web/dist

# --- app: FastAPI back end that also serves the built front end ---
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /srv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY presets ./presets
COPY --from=web /web/dist ./app/static
ENV DATA_DIR=/data PYTHONUNBUFFERED=1
RUN useradd -u 1000 -m scout && mkdir -p /data && chown scout /data
USER scout
WORKDIR /srv/app
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8000/healthz')"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
