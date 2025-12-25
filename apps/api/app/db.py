from __future__ import annotations

import sys
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .config import DATABASE_URL

REPO_ROOT = Path(__file__).resolve().parents[3]
DB_PACKAGE = REPO_ROOT / "packages" / "db"
if str(DB_PACKAGE) not in sys.path:
    sys.path.insert(0, str(DB_PACKAGE))

from models import Base  # noqa: E402

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
