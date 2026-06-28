# Database Migrations

This project uses Alembic to track database schema changes.

## Why migrations matter

At the beginning of the project, the app can create tables automatically with SQLAlchemy.

For a more professional backend project, database schema changes should be tracked through migrations.

Migrations make it possible to:

- Recreate the database schema consistently
- Track database changes over time
- Upgrade production databases safely
- Review schema changes in Git commits

## Current migration

The first migration creates the `applications` table.

## Run migrations

    alembic upgrade head

## Check migration history

    alembic history

## Create a future migration

    alembic revision -m "describe schema change"

Then edit the generated migration file inside:

    alembic/versions/

## Notes

The current app still supports local development with SQLAlchemy table creation, but Alembic is now available for formal schema management.
