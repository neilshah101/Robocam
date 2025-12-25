# Database Package

This package contains SQLAlchemy models, Alembic migrations, and a minimal seed script for local
setup.

## Layout
- models.py: SQLAlchemy models and metadata.
- alembic/: Migration environment and versions.
- seed.py: Minimal seed data for local testing.

## Usage (local)
- Set `DATABASE_URL` in `.env`.
- Run Alembic from this folder: `alembic upgrade head`.
- Seed: `python seed.py`.
