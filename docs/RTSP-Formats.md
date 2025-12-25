# RTSP URL Formats & Requirements — Top 50 IP Camera Vendors

## Purpose of This Document

This document is a developer-grade reference for RTSP stream ingestion across the top 50 major IP
camera vendors. It is designed to be used directly by Codex and backend automation for Robocam.

Goals:
- Standardize RTSP discovery logic
- Reduce vendor-specific guesswork
- Define fallback strategies when ONVIF fails
- Serve as a single source of truth for ingestion pipelines

This is not marketing documentation. It is an engineering contract.

---

## RTSP Fundamentals (Global Assumptions)

These assumptions apply unless explicitly overridden by a vendor or model.

- Protocol: RTSP (Real Time Streaming Protocol)
- Default Port: 554 (configurable on device)
- Authentication:
  - Most devices require username:password
  - Some reject credentials embedded in URL and expect client-level auth
- Transport: TCP preferred (UDP fallback optional)
- Codecs: H.264 / H.265 dominate
- Streams:
  - Main stream (high quality)
  - Sub stream (lower bitrate, analytics-friendly)

---

## Mandatory Discovery Order (Robocam Rule)

Codex must follow this exact order:

1. ONVIF Discovery (Primary)
   - GetCapabilities -> Media
   - GetProfiles
   - GetStreamUri (RTSP)
   - Persist resolved URI

2. Vendor Family Fallback (Secondary)
   - Dahua-family
   - Hikvision-family
   - Hanwha / Wisenet
   - Axis

3. Explicit Vendor Templates (Tertiary)
   - Use hardcoded templates listed below

4. Manual Entry (Last Resort)

No step may be skipped.

---

## Vendor Family Patterns (Critical for Automation)

### 1. Dahua Family (Dahua, Amcrest, Lorex, IMOU, many OEMs)

```
rtsp://USER:PASS@IP:PORT/cam/realmonitor?channel=1&subtype=0
```

- subtype=0 -> main stream
- subtype=1 -> sub stream

---

### 2. Hikvision Family (Hikvision, HiLook, ANNKE, Speco, many OEMs)

```
rtsp://USER:PASS@IP:PORT/Streaming/Channels/101
```

- 101 -> main stream
- 102 -> sub stream

---

### 3. Hanwha / Wisenet

```
rtsp://USER:PASS@IP:PORT/profile1/media.smp
```

- profile1 = main
- profile2 = sub

---

### 4. Axis

```
rtsp://USER:PASS@IP:PORT/axis-media/media.amp
```

- Parameters often appended: resolution, fps, codec

---

## Vendor-by-Vendor RTSP Reference (Top 50)

### 1. Hikvision

```
rtsp://USER:PASS@IP:PORT/Streaming/Channels/101
```

### 2. Dahua

```
rtsp://USER:PASS@IP:PORT/cam/realmonitor?channel=1&subtype=0
```

### 3. Axis

```
rtsp://USER:PASS@IP:PORT/axis-media/media.amp
```

### 4. Hanwha / Wisenet

```
rtsp://USER:PASS@IP:PORT/profile1/media.smp
```

### 5. Bosch

```
rtsp://USER:PASS@IP:PORT/video
```

### 6. Panasonic / i-PRO

```
rtsp://USER:PASS@IP:PORT/MediaInput/h264
```

### 7. Uniview (UNV)

```
rtsp://USER:PASS@IP:PORT/unicast/c1/s0/live
```

### 8. Avigilon

```
rtsp://USER:PASS@IP:PORT/defaultPrimary?streamType=u
```

### 9. Arecont Vision

```
rtsp://USER:PASS@IP:PORT/h264.sdp
```

### 10. Mobotix

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 11. ACTi

```
rtsp://USER:PASS@IP:PORT/track1
```

### 12. Amcrest

(Dahua family)

### 13. Foscam

```
rtsp://USER:PASS@IP:PORT/videoMain
```

### 14. Reolink

```
rtsp://USER:PASS@IP:PORT/h264Preview_01_main
```

### 15. VIVOTEK

```
rtsp://USER:PASS@IP:PORT/live.sdp
```

### 16. Sony

```
rtsp://USER:PASS@IP:PORT/media/video1
```

### 17. Pelco

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 18. Honeywell

(Hikvision or Dahua OEM)

### 19. GEOVISION

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 20. FLIR (Security)

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 21. Ubiquiti (UniFi Protect)

- RTSP often disabled by default
- Requires explicit enable/export

### 22. TP-Link

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 23. D-Link

```
rtsp://USER:PASS@IP:PORT/live1.sdp
```

### 24. Netgear

```
rtsp://USER:PASS@IP:PORT/live.sdp
```

### 25. Lorex

(Dahua family)

### 26. Swann

(OEM dependent)

### 27. ANNKE

(Hikvision family)

### 28. EZVIZ

```
rtsp://USER:PASS@IP:PORT/h264_stream
```

### 29. IMOU

(Dahua family)

### 30. HiLook

(Hikvision family)

### 31. Tiandy

```
rtsp://USER:PASS@IP:PORT/live/ch00_0
```

### 32. Milesight

```
rtsp://USER:PASS@IP:PORT/main
```

### 33. Grandstream

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 34. Cisco (legacy)

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 35. American Dynamics

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 36. ADT (OEM)

```
rtsp://USER:PASS@IP:PORT/img/media.sav
```

### 37. AirLive

```
rtsp://USER:PASS@IP:PORT/live
```

### 38. Apexis

```
rtsp://USER:PASS@IP:PORT/live
```

### 39. Brickcom

```
rtsp://USER:PASS@IP:PORT/live.sdp
```

### 40. IQinVision

```
rtsp://USER:PASS@IP:PORT/stream1
```

### 41. Infinova

```
rtsp://USER:PASS@IP:PORT/live.sdp
```

### 42. Intellinet

```
rtsp://USER:PASS@IP:PORT/video.mp4
```

### 43. Siemens (legacy)

```
rtsp://USER:PASS@IP:PORT/img/video.asf
```

### 44. Sanyo (legacy)

```
rtsp://USER:PASS@IP:PORT/live.sdp
```

### 45. Trendnet

```
rtsp://USER:PASS@IP:PORT/live.sdp
```

### 46. Zavio

```
rtsp://USER:PASS@IP:PORT/video.pro1
```

### 47. QNAP

(Client-side RTSP only; consumes camera RTSP)

### 48. Wbox

(OEM dependent)

### 49. Speco

(Hikvision family)

### 50. Other OEM / White-label

- Always attempt ONVIF first

---

## Persistence Rules (Robocam Requirement)

Once a valid RTSP URI is resolved:
- Store URI
- Store stream type (main/sub)
- Store codec, resolution, fps
- Never rediscover unless failure occurs

---

## Non-Negotiable Engineering Rules

- ONVIF is mandatory when available
- Never brute-force passwords
- Never assume RTSP path without fallback
- Vendor family detection must be explicit
- All failures must be logged with reason codes

---

## End of Document

This document is locked for implementation and may only be modified through versioned updates.
