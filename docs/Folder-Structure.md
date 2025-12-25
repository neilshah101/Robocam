# Folder Structure (Milestone 1)

This structure is optimized for a solo-founder build with a clear separation between UI, API, and
video/AI services.

```
apps/
  api/                FastAPI backend
  web/                Next.js frontend
  worker/             Background jobs (Celery/RQ)
services/
  ingest/             FFmpeg RTSP ingest and clip pipeline
  inference/          AI inference service (people/face detection)
  streaming/          HLS packaging and playback helpers
packages/
  db/                 DB models, migrations, and queries
  shared/             Shared types and utilities
infra/
  docker/             Docker compose and container definitions
```
