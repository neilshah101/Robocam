# Release Plan

This plan converts the locked product model into a solo-founder, Codex-assisted execution path.
Timeline is 6 months across three independently launchable milestones.

## Overall Strategy
Build depth gradually, not breadth all at once:
- Milestone 1: It works
- Milestone 2: It feels intelligent
- Milestone 3: It feels magical and scalable

Assumptions:
- Solo founder
- Heavy Codex and AI assistance
- Early users and feedback over perfection

## Milestone 1 (Month 1-2) - Foundation and Early MVP
Goal: "AI Watch is live and usable." Launch a working product that accepts cameras, detects people and
faces, sends alerts, and supports basic onboarding.

Features to build (only these):
- Camera ingestion (RTSP / IP camera)
- Person detection
- Facial detection (anonymous)
- Motion and intrusion detection
- Per-camera processing pipeline
- User authentication
- Camera CRUD
- Event storage
- Clip storage (short clips only)
- Basic UI: login/signup, add camera, live view, events list
- Face timeline v1 (per camera, temporary IDs, click face to view clips)

Do not build yet:
- Industry presets
- Feature toggles
- Video search
- Advanced alerts
- Multi-camera logic

Milestone 1 outcome:
"For $5 per camera, you can see every face your camera has seen."

## Milestone 2 (Month 3-4) - Intelligence and Differentiation
Goal: "Now it feels like Robocam." Introduce tiers, industry logic, and control while keeping UX simple.

Features to add:
- Tier system (Watch, Watch Plus, Understand, Operate)
- Feature gating by tier (backend flags)
- Industry presets v1 (Home, Small Business, Hotel, Gas Station)
- Feature toggles that control rules, not models
- Face labeling (VIP, staff, watchlist)
- Alerts on flagged faces (same camera)
- UI improvements: tier badges, industry badges, toggle switches, better timelines

Do not build yet:
- Cross-camera tracking
- Video search
- Enterprise features
- Heavy analytics

Milestone 2 outcome:
"Robocam understands routines and alerts you when something is off."

## Milestone 3 (Month 5-6) - Power and Scale Readiness
Goal: "This is not a toy anymore." Support up to 32 cameras, advanced investigation, and enterprise prep.

Features to add:
- Video search by face, event type, time range
- Cross-camera intelligence (limited window) for Operate tier
- Path reconstruction and incident replay
- Tier-based retention enforcement and retention add-on
- Stripe integration for per-camera billing and add-ons
- Camera count detection (>32) and contact sales flow
- Basic org and location grouping

Do not build yet:
- Smart city scale
- Deep compliance automation
- Custom ML training

Milestone 3 outcome:
A real SaaS with paying customers, clear enterprise upsell, and alignment to the locked model.

## Timeline Snapshot

| Month | Focus |
| --- | --- |
| 1 | Camera ingest and face detection |
| 2 | Face timeline and MVP launch |
| 3 | Tiers and industry presets |
| 4 | Feature toggles and labeling |
| 5 | Video search and cross-camera |
| 6 | Billing and scale readiness |
