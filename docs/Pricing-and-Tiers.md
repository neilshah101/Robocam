# Pricing and Tiers

Status: LOCKED (v1.0)

This document is the single source of truth for Robocam's product vision, feature set, pricing model,
Tier design, industry logic, and enterprise split.

## 1. Core Product Philosophy
Robocam is not a CCTV system. Robocam is an AI Vision Intelligence Platform that:
- Sees people, vehicles, and behavior.
- Organizes video by who and what, not files.
- Applies industry-specific intelligence automatically.
- Scales from a $5 camera to city-wide deployments.

Key design principles:
- Simple outside, powerful inside.
- Few choices, deep intelligence.
- Per-camera pricing (no confusion).
- Industry presets, not industry plans.
- Privacy-first by default.

## 2. Customer Segmentation (Locked)

| Segment | Camera Count | Motion | Description |
| --- | --- | --- | --- |
| Segment A | 1-32 cameras | Self-serve | Homes, SMBs, hotels, gas stations, small offices |
| Segment B | 33+ cameras | Sales-assisted | Industrial, hospitals, schools, government, smart cities |

This split is non-negotiable.

## 3. Pricing Model (Segment A - Self Serve)
Pricing is per camera per month. No camera caps (up to 32). Linear scaling. Same pricing for all
industries.

| Tier | Price | Meaning |
| --- | --- | --- |
| AI Watch | $4.99 | AI watches and alerts |
| AI Watch Plus | $7.99 | AI understands situations |
| AI Understand | $12.99 | AI understands routines |
| AI Operate | $24.99 | AI operates and investigates |

## 4. Industry Presets (Applies to All Tiers)
At signup, users select what kind of place they have. This applies preset rules, dashboards, and alerts.
Industry is configuration, not pricing.

Supported industries (Segment A):
- Home / Residential
- Small Business
- Hotel / Hospitality
- Gas Station
- Retail
- Warehouse / Light Industrial
- Clinic / Small School

## 5. Hero Feature - Facial Detection and Face Timeline (Core)
Included in all tiers.

What it does:
- Detects every face seen by a camera.
- Creates anonymous temporary face IDs.
- Builds a Face Timeline, sortable by camera and time.
- Clicking a face shows all video clips where that face appeared with timeline playback.

What it does not do by default:
- No naming
- No identity matching
- No cross-site identity

This keeps the system privacy-safe, easy to sell, and globally compliant.

## 6. Face Capabilities by Tier

| Capability | Watch | Watch Plus | Understand | Operate |
| --- | --- | --- | --- | --- |
| Face detection | Included | Included | Included | Included |
| Face timeline (per camera) | Included | Included | Included | Included |
| Click face to view all clips | Included | Included | Included | Included |
| Temporary face IDs | Included | Included | Included | Included |
| Face labeling (VIP, staff, etc.) | Not included | Not included | Included | Included |
| Alerts on flagged faces | Not included | Not included | Included | Included |
| Cross-camera face grouping | Not included | Limited | Included | Included |
| Facial recognition | Add-on | Add-on | Add-on | Add-on |

## 7. Core Feature Matrix (All Features)

| Feature | Watch | Watch Plus | Understand | Operate |
| --- | --- | --- | --- | --- |
| Person detection | Included | Included | Included | Included |
| Vehicle detection | Included | Included | Included | Included |
| Intrusion alerts | Included | Included | Included | Included |
| Loitering detection | Not included | Included | Included | Included |
| Zone duration rules | Not included | Included | Included | Included |
| Industry routines | Not included | Not included | Included | Included |
| Behavior and anomaly AI | Not included | Not included | Included | Included |
| Event-based video search | Not included | Not included | Included | Included |
| Cross-camera intelligence | Not included | Not included | Not included | Included |
| Path reconstruction | Not included | Not included | Not included | Included |
| Audit logs | Not included | Not included | Included | Included |
| Multi-site dashboard | Not included | Not included | Included | Included |

## 8. In-App Feature Toggles (Locked Design)
Users can toggle features on or off within their tier limits.
- Toggles control rules, not models.
- No cost gaming.
- No compute abuse.

Examples:
- Enable or disable staff routine monitoring.
- Enable or disable loitering alerts.
- Enable or disable face alerts (if available).

## 9. Add-ons (Optional, All Tiers)

| Add-on | Price | Notes |
| --- | --- | --- |
| License Plate Recognition | +$5 / camera | Vehicle OCR and watchlists |
| Facial Recognition | +$4 / camera | Consent-based only |
| Extended retention (+30d) | +$5 / camera | Applies to all footage |
| WhatsApp or SMS alerts | +$3 / location | Not per camera |

## 10. Enterprise Model (Segment B - 33+ Cameras)
Industries:
- Industrial and factories
- Hospitals and healthcare
- Schools and universities
- Large offices and campuses
- Government
- Smart cities

Features:
- Deep SOP mapping
- Multi-location intelligence
- Compliance workflows
- Advanced audits
- SLA and dedicated support

Pricing:
- Custom (still per camera)
- Annual contracts

## 11. One-Line Buying Logic (Final)
Choose your industry, choose how smart the AI should be, add cameras, toggle features.

## 12. Final Status
Product model locked. Pricing model locked. Feature set locked. Scales from $5 to enterprise.
Matches founder's original vision.

This document is the foundation for: website, sales, development, and investor decks.
