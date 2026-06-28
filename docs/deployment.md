# Deployment Guide

This project can be deployed as a Render Web Service.

## Render settings

Build Command:

    pip install -r requirements.txt

Start Command:

    alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT

## Environment variables

For the current SQLite demo version:

    DATABASE_URL=sqlite:///./applications.db

## Important note about SQLite on hosted platforms

SQLite is fine for a demo, but local file storage may not persist across redeploys unless the platform provides persistent storage.

For a more production-ready version, switch to PostgreSQL.

## Demo URLs after deployment

Replace YOUR_RENDER_URL with the deployed Render URL.

Web UI:

    https://YOUR_RENDER_URL/ui

API docs:

    https://YOUR_RENDER_URL/docs

Health check:

    https://YOUR_RENDER_URL/health
