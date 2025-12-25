from __future__ import annotations

import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PACKAGE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if DB_PACKAGE_DIR not in sys.path:
    sys.path.insert(0, DB_PACKAGE_DIR)

from models import Base

config = context.config
fileConfig(config.config_file_name)


def load_env_file(path: str) -> None:
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key and key not in os.environ:
                os.environ[key] = value


def get_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        repo_root = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", ".."))
        load_env_file(os.path.join(repo_root, ".env"))
        url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return url


config.set_main_option("sqlalchemy.url", get_url())


def run_migrations_offline() -> None:
    context.configure(
        url=get_url(),
        target_metadata=Base.metadata,
        literal_binds=True,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
