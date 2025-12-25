# System Architecture

This document describes the high-level system architecture. It defines the major components and their
responsibilities, without prescribing implementation details.

## Goals
- Support per-camera processing and pricing.
- Enable privacy-first defaults with optional consent-based features.
- Provide event-driven indexing and investigation.
- Scale from single-camera to multi-site deployments.

## Core Components

### Camera Ingestion
- Accepts RTSP / IP camera streams.
- Manages camera connectivity, health, and stream lifecycle.

### Stream Processing Pipeline
- Per-camera video pipeline for detection and tracking.
- Produces structured detections for people, vehicles, faces, and events.

### AI Services
- Object detection and tracking
- Vehicle classification and tracking
- Face detection and optional recognition (opt-in)
- Behavior and anomaly intelligence
- Cross-camera re-identification (site-limited)

### Event Engine
- Converts detections into structured events with timestamps and confidence.
- Applies rule logic for intrusion, loitering, and zone duration.

### Media Storage
- Stores short clips linked to events.
- Maintains retention by tier and add-on policies.

### Metadata Index
- Indexes events by object type, time, camera, and attributes.
- Enables visual search and timeline reconstruction.

### Alerting Service
- Sends notifications when confidence thresholds and rules are met.
- Channels: email, WhatsApp, in-app.

### Application Layer
- User authentication and account management.
- Camera CRUD and configuration.
- Tier and add-on assignment per camera.
- Industry presets and feature toggles.

### Billing and Entitlements
- Per-camera billing and add-on billing.
- Enforces tier limits and feature access.

## Data Flow Overview
1. Camera stream ingested and processed by per-camera pipeline.
2. AI services generate detections and tracking IDs.
3. Event engine normalizes detections into event records.
4. Clips and metadata are stored and indexed.
5. UI and APIs query timelines, search, and alerts.

## Non-Goals
- Model training, deployment details, or hardware selection.
- Jurisdiction-specific compliance workflows.
