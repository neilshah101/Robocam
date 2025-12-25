from __future__ import annotations

import os
import uuid
from datetime import datetime

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Camera, User


def get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL is not set")
    return url


def main() -> None:
    engine = create_engine(get_database_url())

    with Session(engine) as session:
        def get_or_create_user(email: str, password_hash: str) -> User:
            existing_user = session.scalar(select(User).where(User.email == email))
            if existing_user:
                return existing_user
            new_user = User(
                id=uuid.uuid4(),
                email=email,
                hashed_password=password_hash,
                created_at=datetime.utcnow(),
            )
            session.add(new_user)
            return new_user

        admin_user = get_or_create_user("admin@robocam.local", "admin_password_hash")
        demo_user = get_or_create_user("demo@robocam.local", "demo_password_hash")

        existing_camera = session.scalar(
            select(Camera).where(Camera.user_id == demo_user.id, Camera.name == "Demo Camera")
        )
        if not existing_camera:
            camera = Camera(
                id=uuid.uuid4(),
                user_id=demo_user.id,
                name="Demo Camera",
                rtsp_url="rtsp://example.local/stream",
                status="offline",
                created_at=datetime.utcnow(),
            )
            session.add(camera)

        session.commit()


if __name__ == "__main__":
    main()
