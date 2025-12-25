# Tech Stack (Milestone 1)

This document captures the approved v1 stack for Robocam aligned to the locked product model and the
Milestone 1 scope.

## Camera Ingest and Clip Pipeline

- FFmpeg for RTSP ingest, segmenting, and snapshots.
- HLS for live view and short clip playback in v1.
- WebRTC planned for later milestones.

## AI Inference (People and Face Detection)

- Python 3.11/3.12
- PyTorch for development and model iteration
- ONNX Runtime for production inference (CPU/GPU)
- TensorRT later when GPU scale requires it

Face handling guidance:

- Start with face detection only (no recognition by default).
- Represent detections as face crops plus embeddings.
- Store embeddings only when tier or add-on requires it.

## Backend API

- FastAPI (Python)
- PostgreSQL for core data
- Redis for queues, caching, and rate limits
- Background jobs: Celery (or RQ if simpler)
- JWT authentication for v1

## Data Storage Model

- Postgres tables for cameras, events, face_detections, face_tracks, face_labels, toggles, tiers,
  industries.
- Object storage for video (MinIO in dev, S3 in production).

## Frontend

- Next.js (App Router)
- Tailwind CSS
- shadcn/ui components
- HLS.js for video playback

## Billing

- Stripe for per-camera subscriptions and add-ons.

## Deployment (MVP)

- Docker Compose
- Single server for API + worker + DB + Redis + MinIO
- Separate inference worker(s) as needed

## Observability

- Sentry for frontend and backend errors
- Structured JSON logs (Prometheus/Grafana later)

## Architectural Rule

Keep AI outputs separate from rules:

- AI outputs: person_detected, face_detected, track_id, timestamp, camera_id
- Rules decide: alerts, timelines, labels, industry behaviors, tier availability
