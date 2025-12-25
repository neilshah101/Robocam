# Milestone 1 Tasks

This document breaks Milestone 1 into modules and tasks. Each task is intended to be small, testable,
and shippable.

## 1) Repo and Dev Environment
- Initialize service skeletons for API, web, worker, ingest, inference, and streaming.
- Add Docker Compose for API, Postgres, Redis, MinIO, and worker.
- Add basic environment config files (.env.example).

## 2) Database and Models
- Define core tables: users, cameras, events, face_detections, clips.
- Add migration tooling and first migration.
- Add minimal seed data for local testing.

## 3) API - Auth and Users
- Create auth endpoints (signup/login) with JWT.
- Add password hashing and validation.
- Add current-user endpoint.

## 4) API - Camera CRUD
- Create camera create/list/update/delete endpoints.
- Validate RTSP URL format and camera health fields.
- Store camera status and last-seen timestamps.

## 5) Ingest Service
- Build RTSP ingest worker using FFmpeg.
- Generate HLS segments and snapshots per camera.
- Emit ingest health events to API/DB.

## 6) Inference Service
- Load people and face detection models.
- Process frames from ingest pipeline.
- Emit detections to API/DB.

## 7) Event Engine (MVP Rules)
- Convert detections into structured events.
- Implement intrusion and motion events only.
- Store event confidence and camera references.

## 8) Clip Storage
- Store short clips linked to events.
- Enforce basic retention window for MVP.

## 9) Web App - Core UI
- Auth screens (login/signup).
- Add camera flow (form + list).
- Camera live view (HLS player).
- Events list with basic filters.

## 10) Face Timeline (Hero Feature v1)
- Store face detections and temporary face IDs.
- Create face timeline API endpoints.
- Build face timeline UI (per camera, time-ordered).
- Click face to view linked clips.

## 11) Alerts (MVP)
- Send email alerts for intrusion or motion events.
- Add alert settings per camera (on/off only).

## 12) Observability and Ops
- Add structured logging for API and services.
- Add basic health checks for API and workers.
- Add error tracking placeholder (Sentry config stub).

## 13) QA and Verification
- Add curl-first API examples for auth and camera CRUD.
- Add smoke test checklist for ingest, detection, events, UI.
- Validate end-to-end: camera -> detection -> event -> clip -> UI.
