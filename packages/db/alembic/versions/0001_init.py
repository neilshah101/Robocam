"""init

Revision ID: 0001_init
Revises:
Create Date: 2025-12-25 04:30:00.000000
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "cameras",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("rtsp_url", sa.Text(), nullable=False),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("last_seen_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    op.create_index("ix_cameras_user_id", "cameras", ["user_id"], unique=False)

    op.create_table(
        "events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("camera_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("event_type", sa.String(length=100), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("occurred_at", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["camera_id"], ["cameras.id"]),
    )
    op.create_index("ix_events_camera_id", "events", ["camera_id"], unique=False)
    op.create_index("ix_events_event_type", "events", ["event_type"], unique=False)

    op.create_table(
        "face_detections",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("camera_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("face_track_id", sa.String(length=200), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("bounding_box", postgresql.JSONB(), nullable=False),
        sa.Column("occurred_at", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["camera_id"], ["cameras.id"]),
    )
    op.create_index("ix_face_detections_camera_id", "face_detections", ["camera_id"], unique=False)
    op.create_index("ix_face_detections_face_track_id", "face_detections", ["face_track_id"], unique=False)

    op.create_table(
        "clips",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("camera_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("event_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("storage_key", sa.Text(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["camera_id"], ["cameras.id"]),
        sa.ForeignKeyConstraint(["event_id"], ["events.id"]),
    )
    op.create_index("ix_clips_camera_id", "clips", ["camera_id"], unique=False)
    op.create_index("ix_clips_event_id", "clips", ["event_id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_clips_event_id", table_name="clips")
    op.drop_index("ix_clips_camera_id", table_name="clips")
    op.drop_table("clips")

    op.drop_index("ix_face_detections_face_track_id", table_name="face_detections")
    op.drop_index("ix_face_detections_camera_id", table_name="face_detections")
    op.drop_table("face_detections")

    op.drop_index("ix_events_event_type", table_name="events")
    op.drop_index("ix_events_camera_id", table_name="events")
    op.drop_table("events")

    op.drop_index("ix_cameras_user_id", table_name="cameras")
    op.drop_table("cameras")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
