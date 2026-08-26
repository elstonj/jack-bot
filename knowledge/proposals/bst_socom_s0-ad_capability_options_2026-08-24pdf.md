# S0-AD Capability Development Options for USSOCOM

## Document Metadata
- **Type:** Technical Brief and Rough Order of Magnitude (ROM) Summary
- **Client/Agency:** USSOCOM (U.S. Special Operations Command)
- **Program/Solicitation:** USSOCOM-BST Cooperative Research and Development Agreement (CRADA)
- **Date:** 18 August 2026
- **BST Products/Systems Referenced:** S0, S0-AD (air-deployed variant), SwiftCore Flight Management System, SwiftTab operator interface, SwiftStation ground radio and control unit, SwiftLink, Pneumatic Common Launch Tube (PCLT) modification
- **Key Personnel:** Jack Elston, Ph.D. (Founder & CEO, Black Swift Technologies); Daniel Prendergast (last editor); TSgt Evan Wolff (USSOCOM contact)

## Executive Summary
This document provides ROM cost and effort estimates for three capability development tracks for the S0-AD (S0 air-deployed) unmanned aircraft system under SOCOM's CRADA: (1) mechanical integration with the Pneumatic Common Launch Tube (PCLT), (2) objective-area weather reconnaissance in METAR-equivalent configurations, and (3) three distinct EO/IR solution approaches at different cost/capability/risk tradeoffs. The S0-AD is a 3 lb, tube-form-factor fixed-wing aircraft that has already demonstrated successful free-fall air deployment from 12,000 ft MSL with SOCOM operators, with full autonomous flight capability and long-range (400 km tested) low-bandwidth command-and-data link.

## Technical Approach

### Baseline S0-AD Platform
- **Form factor:** Tube-compatible fixed-wing aircraft, ~3 lb, air-deployed
- **Flight control:** SwiftCore Flight Management System (BST-designed autopilot stack) with autonomous operation from release through mission completion
- **Operator interface:** SwiftTab operator interface on rugged tablet; SwiftStation ground radio and control unit
- **Command & data link:** 430 MHz Microhard P400 narrowband (2 W), tested to 400 km range against host-aircraft auxiliary antenna; **critical constraint:** long-range, low-bandwidth limits imagery transmission rates
- **Launch variants:** Hand-launched and tube-launched variants share same avionics
- **Operational heritage:** NOAA Hurricane Hunter P-3 deployments; holds Guinness World Record for highest wind speed measured by uncrewed aircraft (240 mph, Hurricane Milton, October 2024)

### Spiral Development Approach
BST recommends independent, progressively useful spirals, each culminating in real flight demonstration rather than paper deliverables:
- **Spiral 1:** Mechanical launch integration (Option 1)
- **Spiral 2:** Objective-area weather reconnaissance (Options 2a, 2b)
- **Spiral 3:** EO/IR capability (Options 3a, 3b, 3c—alternatives, not sequential)

All spirals converge on one airframe, one autopilot, and one operator interface.

## Products & Capabilities Described

### S0-AD (Air-Deployed S0)
**What it is:** Tube-compatible (5.9 in diameter × 42 in length CLT envelope), free-fall air-deployed fixed-wing UAS, approximately 3 lb
- **Current baseline unit price:** ~$18,000 (small quantities); not currently reusable; typically sustains light, repairable damage on landing
- **Operational pedigree:** Hurricane Hunter missions; verified in extreme atmospheric environments (240 mph winds, Hurricane Milton)
- **Deployment demonstrated:** 17 August 2026 free-fall deployment from 12,000 ft MSL, executed by SOCOM operators after one day of training

### SwiftCore Flight Management System
- BST-developed autopilot stack
- Enables autonomous flight from release through mission completion
- Integrates with SwiftTab and SwiftStation for operator control

### SwiftTab & SwiftStation
- SwiftTab: Rugged tablet operator interface
- SwiftStation: Ground radio and control unit
- Follow-on work proposed: Tactical SwiftLink and SwiftTab (lightweight tactical control unit optimized for man-packed deployment)

### Option 1: Pneumatic CLT-Modified S0
**ROM Development Cost:** $64,435 | **Recurring Unit Price:** $19,000 | **Est. Labor:** 162 hrs

**What it is:** Mechanical design modification enabling S0 to load into and be pneumatically ejected from SOCOM's Pneumatic Common Launch Tube
- **Interface:** Mechanical only; no electrical or data connection to tube
- **Scope:** Design modification, test-article fabrication, ground ejection testing with dummy round, live flight test from tube
- **Assumptions:** 
  - S0 powered on and loaded either in host aircraft or before takeoff (no remote power-on capability developed)
  - Aircraft survives pneumatic ejection intact (structural hardening for ejection loads *not* included—**single largest technical risk**)

**Key Technical Requirement:** SOCOM must provide PCLT ejection profile (peak pressure, acceleration, pulse duration) and ideally one tube for ground testing in Boulder

**Recommended Follow-On (not priced):** Tube-resident readiness firmware—optimize power consumption for extended in-tube sitting, pre-load mission profiles to collapse preflight sequence from ~10 minutes to short readiness check

---

### Option 2a: METAR Core Capability
**ROM Development Cost:** $152,690 | **Recurring Unit Price:** $23,000 | **Est. Labor:** 474 hrs

**What it is:** Weather reconnaissance of routes and objective areas in hours before direct action, supporting go/no-go decisions for rotary-wing landing zones, fixed-wing expeditionary runways, and drop zones

**Operator modes:**
- Reconnaissance element within line-of-sight of objective, OR
- Operator standing off in host aircraft

**Delivered products:**
- Pressure, temperature, humidity, dew point from BST's calibrated PTH sonde
- Wind direction and speed from BST's multi-hole probe (same instrumentation as Hurricane Hunter missions)
- Day/night-capable still-imaging payload (operator-commanded)—sufficient for operator to determine:
  - Presence and type of precipitation
  - Gross obscuration along route and over objective
  - Cloud levels above safe minimum
- Vertical profiles of measured parameters through aircraft descent

---

### Option 2b: METAR Automated Sensing (Cloud Layer, Ceiling, Visibility Research)
**ROM Development Cost:** $174,961 | **Recurring Unit Price:** TBD | **Est. Labor:** 524 hrs

**What it is:** Bounded research, integration, and flight-validation to determine automated, numerically-generated METAR-equivalent observations from a 3 lb air-deployed aircraft

**Objective:** Measure precipitation type/intensity, lowest cloud layer and ceiling altitude, horizontal visibility with no human interpretation of imagery required

**Approach—Three parallel trade studies:**
1. **Precipitation:** Capacitive, resistive, and optical sensing approaches evaluated for precipitation type and numerical intensity/rate/droplet-size measurement
2. **Cloud layer & ceiling:** Upward-looking approaches including:
   - Cameras with computer vision retrievals
   - Single-point lidar
   - Longwave infrared radiometry
   - Goal: numerical lowest-layer and ceiling altitudes
3. **Horizontal visibility:** Forward-looking approaches including:
   - Single-point lidar
   - Longwave infrared radiometry

**Phase 2 (following trade studies):** Finalize design, integrate selected sensors, ensure SWaP and flight-performance compliance. Includes electrical, mechanical, and software modifications to SwiftCore and SwiftControl stacks for automated data processing. Results displayed as actionable METAR-equivalent values on SwiftLink interface.

**Culmination:** Flight-test demonstration and operational evaluation with SOCOM personnel

---

### Option 3a: EO/IR—Record and Recover
**ROM Development Cost:** $116,048 | **Recurring Unit Price:** $21,000 | **Est. Labor:** 334 hrs

**What it is:** Intelligence preparation of the battlefield in weeks/days/hours before operation

**Mission profile:**
- Fully autonomous route with programmed photogrammetric coverage
- Records EO and IR imagery onboard with no gaps along trajectory
- Egresses to recovery point
- Imagery downloaded after recovery, exploited by ATR tooling or human analysis
- Can execute with datalink fully suppressed (transmits only telemetry and payload status if permitted)

**Sensor specification:**
- EO: 12 MP
- IR: 640 × 512 threshold; 1280 × 1024 objective (uncooled longwave infrared—reflects realistic SWAP-constrained performance; cooled mid-wave inappropriate for consumable aircraft)

**Why BST recommends starting here if EO/IR is priority:**
- Lowest cost and lowest risk of three EO/IR options
- Requires no new radio
- Every component reused directly in Option 3b

---

### Option 3b: EO/IR—Real-Time ATR
**ROM Development Cost:** $221,262 | **Recurring Unit Price:** $29,000 | **Est. Labor:** 634 hrs

**What it is:** Human-monitored, machine-assisted ISR in hours before operation to confirm/refute prior intelligence, with ability to retask aircraft mid-mission on findings

**Operating concept:**
- Third-party automatic target recognition algorithm runs onboard
- Transmits compact target data packets and occasional low-resolution target chips (not video)
- Includes trade study between camera + separate single-board computer vs. camera with integrated AI processing
- Operator interface displays detected targets, metadata, and imagery

**Sensor specification:** Same as Option 3a (12 MP EO, 640×512 IR threshold)

**Transmission rate constraint:** No more frequently than every 60 seconds per identified target
- At 50 nm on narrowband link, faster transmission not achievable without substantially larger radio/antenna than airframe supports
- Target data packets remain at 5-second intervals

**Key note on imagery cadence:** Bandwidth-limited, not software-limited. Single 1280×720 image over 50 nm takes minutes, not seconds, to transmit.

**Recommendation:** BST integrates and flight-qualifies ATR; does not develop algorithm. Government-furnished or SOCOM-preferred ATR removes both license cost and integration uncertainty. Export classification of candidate ATR software and imaging payload to be confirmed during component selection.

---

### Option 3c: EO/IR—Full Motion Video ISR
**ROM Development Cost:** $219,597 | **Recurring Unit Price:** $38,000 | **Est. Labor:** 639 hrs

**What it is:** Persistent real-time observation for tasks requiring human-in-the-loop: maintaining target custody, observation for indirect and aviation fires

**Equipment:**
- Gimbaled EO/IR camera (NextVision DragonEye class)
- Manual slew, object tracking, geolocation stare modes
- Streams 1080p30 EO and 640×480 IR to operator
- No-comm transit mode to reach operator or objective area
- Broadband radio (Microhard pMDDL2280 pre-selected)

**Critical constraints:**
1. **Video range ≠ aircraft range:** Aircraft can transit 50 nm; full motion video requires broadband link and only available to operator within roughly 15 nm
2. **Economic reality:** Gimbal ~45% of recurring unit price on non-recoverable airframe. Expending $38,000 aircraft for video sortie materially different economic proposition than $21,000 basic configuration.

**Recommendation:** Pair FMV with airframe recoverability effort (Section 8) or recovery-oriented CONOPS so expensive payload not consumed on every sortie.

---

## Use Cases & Applications

### METAR Configuration Use Cases
- Advanced weather reconnaissance for direct action operations
- Pre-assault objective area observation
- Support for rotary-wing landing zone (LZ) go/no-go decisions
- Fixed-wing expeditionary runway assessment
- Drop zone (DZ) weather characterization in hours before operations
- Route weather observation
- Vertical atmospheric profiling through aircraft descent

### EO/IR Configuration Use Cases
**Record & Recover (3a):**
- Intelligence preparation of the battlefield (IPB)
- Photogrammetric coverage planning
- Pre-operation area assessment (weeks/days/hours before)

**Real-Time ATR (3b):**
- Mid-mission ISR with retasking capability
- Target confirmation/refutation against prior intelligence
- Automated target detection and reporting

**Full Motion Video (3c):**