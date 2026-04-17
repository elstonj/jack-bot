# By Light Professional IT Services / Black Swift Technologies — Navy Medium Range Tactical UAS Proposal

## Document Metadata
- **Type:** Proposal (Technical Response to RFI)
- **Client/Agency:** U.S. Navy / NAVAIR PMA-263 (Navy & Marine Corps Small Tactical UAS Program Office), Patuxent River, MD
- **Program/Solicitation:** NOTICE ID 243-26-024; Medium Range Tactical (MRT) Unmanned Aircraft System (UAS)
- **Date:** April 13, 2026
- **BST Products/Systems Referenced:** Black Swift S3 UAS, SwiftCore Flight Management System, SwiftPilot (autopilot), SwiftStation, SwiftTab
- **Key Personnel:** Justin Baltz (By Light, Sales Engineer); Karleigh M. Hall, Kristen W. Ferro (Navy POCs)
- **Prime Contractor:** By Light Professional IT Services LLC (CAGE 3G4R0, UEI NKKQE6FG4C28)
- **Teaming Partner:** Black Swift Technologies LLC (CAGE 6PGF9, UEI C2J3K9NRE3L3; small business)

---

## Executive Summary

By Light and Black Swift Technologies propose the **Black Swift S3 UAS**—an advanced Vertical Takeoff and Landing (VTOL) platform designed for challenging government missions in tough environments. The S3 delivers high payload capacity, high-altitude and turbulent weather capability, and fully autonomous operations. The team combines By Light's complex program delivery expertise with BST's industry-leading UAS development capabilities, offering flexible teaming arrangements depending on competition type (large business prime for Full & Open; small business prime for set-asides).

---

## Technical Approach

### System Architecture & Philosophy
- **VTOL Fixed-Wing Hybrid:** Electric propulsion with 3 motors (2 pivoting, 1 fixed vertical) enabling vertical takeoff/landing with transition to fixed-wing cruise flight
- **Flight Management:** SwiftCore Flight Management System (proprietary, fully integrated, in-house design)
- **Autonomy-First Design:** Capable of full-mission autonomous execution from takeoff to landing; operator-in-the-loop control with real-time waypoint adjustment
- **Modular Payload Integration:** Swappable nose cone with standardized DB9 serial-UART interface; tool-free, glove-friendly payload swap (~1 minute)

### Key Design Features
- **Electric Propulsion:** 1080 Wh battery capacity, 6 kW max momentary output
- **Operator-Focused Maintenance:** Modular, tool-free component replacement (propellers, motors, pylons, wings, tail surfaces, batteries, nose cone)
- **Navigation Fusion:** Loosely coupled GNSS-INS architecture using UBlox ZED F9P dual GPS, MPU 6050 MEMs IMU, MS5611 barometric altimeter, RM3100 magnetometer; operates in GNSS-degraded mode with intelligent fallback
- **Control Philosophy:** Waypoint-based mission planning; operator can adjust waypoints in real-time or create entirely new plans during flight
- **Lost-Link Contingency:** Autonomous execution of pre-programmed contingency (e.g., return-to-home, land-in-place); user-configurable
- **Data Management:** Onboard MicroSD recording (50 Hz) on AV; GCS internal memory (128 GB); optional Iridium SATCOM for beyond-line-of-sight operations

---

## Products & Capabilities Described

### Black Swift S3 UAS

**What It Is:**
- Electrically powered VTOL fixed-wing UAS designed for tactical ISR and specialized payload delivery
- Fully integrated proprietary flight control and management suite

**Physical Specifications:**
- **Air Vehicle MGTOW (baseline EO/IR payload):** 33.5 lbs.
- **MGTOW (maximum payload):** 36.5 lbs.
- **Airframe Weight (no batteries):** 21.6 lbs.
- **Assembled Dimensions:** 162" × 88" × 18"
- **Packed System Weight:** ~85 lbs. (Case 1 with AV), ~75 lbs. (Case 2 with nose cone, batteries, datalink, tablet, accessories)
- **Total System Weight (fully fielded):** Includes 2× flight batteries (8.9 lbs. each), command datalink w/antennas (3.3 lbs.), control tablet (1.1 lbs.), cables, charger, peripheral gear (3.5 lbs.), carrying cases (60 lbs.)

**Launch & Recovery:**
- Hand-launch or autonomous VTOL takeoff (button-initiated; VTOL and transition autonomous once launched)
- Autonomous vertical landing (operator presses "Go to Landing"; AV executes approach, transition, and landing autonomously)
- Operator-supervised manual recovery supported
- Rapid mission turnaround: <10 minutes between sorties
- Operating clearance: ~35 ft. diameter recommended
- Cannot land on moving vehicles or ships (yet); suitable for ground platforms, amphibious environments, expeditionary bases with power/datalink

**Propulsion & Power:**
- **Type:** Electric; 3 motors (2 pivoting for VTOL, 1 fixed vertical)
- **Thrust:** 6 kW max momentary output
- **Battery:** 1080 Wh capacity; hot-swap supported (60-second changeover)
- **Endurance (standard EO/IR configuration):** 100 minutes
- **Max Endurance (optimal profile):** 120 minutes
- **Power Management:** Fixed profile with manual shutdown of payload/accessories; configurable low-battery alerting; auto-return at 20% capacity
- **GCS Power:** Internal Li-Ion battery (5050 mAh, 8-hour life) or power cord

**Payload Capacity & Modularity:**
- **Maximum Payload Capacity:** 2.7 kg (5.95 lbs.)
- **Baseline Payload:** EO/IR sensor (~3 lbs.) assumed; no fixed baseline specified
- **Payload Envelope:** 1000 cu. in. (8" diameter × 20" length)
- **Modular Interface:** Swappable nose cone with power/data interface (DB9, Serial-UART) to SwiftCore FMS
- **Payload Swap Time:** ~1 minute; tool-free, glove-friendly
- **Historical Payloads Supported (11 available):** Atmospheric sensing, thermal/hyperspectral imaging, multispectral cameras, gas sensors, nephelometers, wildfire-monitoring payloads
- **Third-Party Integration:** Open communication protocol based on BST Software Development Kit (SDK); supports consuming AV data and sensor-based aircraft control

**Sensor Capabilities:**

*Baseline EO/IR Payload (Trillium HD25):*
- **Electro-Optical (EO):** Visible 1280 × 720 pixels; 12× zoom (3× optical + 4× digital, continuous)
- **Infrared (IR):** LWIR 640 × 512 pixels; 2× zoom (1× optical + 2× digital)
- **Gimbal:** 2-axis stabilization (Pan: 360° continuous; Tilt: -80° to 42°/46° depending on variant)
- **Stabilization:** Electronic onboard; scene/geo-tracking and auto-track capability
- **Day/Night Imaging:** Full-color EO daytime (1280 × 720, H.264 encoding, onboard compression, analog video option); LWIR primary for night/low-light with electronic image stabilization and fusion
- **Video:** Up to 1080p, H.264/H.265 encoding
- **Still Imagery:** Operator-initiated frame capture from live video stream
- **Geospatial Metadata:** Embedded metadata in standard formats

**Command, Control & Autonomy:**
- **Autonomy Modes:** 
  - Manual (optional)
  - Semi-autonomous (stable, controlled flight with high-rate control loops; can adjust waypoints or create new flight plans in real-time)
  - Fully autonomous (complete mission from takeoff to landing without ground station communication)
- **Emergency/Contingency Autonomy:** Intelligent autonomous response to degraded systems (e.g., lost comms link)
- **Operator-in-the-Loop:** Executes waypoint-based flight plan autonomously; operator can adjust waypoints or create new plans at any time
- **Man-in-the-Loop:** No targeting/weapons systems implemented
- **Control Handoff:** Supported between operators via sequential datalink transfer (must complete before lost-link timeout)
- **Mission Execution:** Waypoint-based flight plan segments for ingress/egress, data collection patterns, orbits; graphical scripting to combine segments for full-mission autonomous execution
- **In-Flight Re-Tasking:** Supported (new waypoint plans can be created/uploaded in flight)
- **Terrain Avoidance:** Mission planning tool on control tablet includes terrain model to ensure plans avoid obstacles; no real-time onboard terrain avoidance
- **Multi-AV Management:** Currently 1 AV per operator; no multi-AV control mode yet; no cross-vendor interoperability

**Navigation & Guidance:**
- **Primary Systems:** UBlox ZED F9P dual GPS (sub-1° heading capability), MPU 6050 MEMs IMU, MS5611 barometric altimeter (10 cm resolution), RM3100 magnetometer (2° heading accuracy)
- **Navigation Fusion:** Loosely coupled GNSS-INS; does not require GNSS for flight/control but uses it to improve position estimation
- **GNSS-Degraded Operation:** Warns user; operator may choose to return home/land, land immediately, or continue
- **GNSS-Denied Operation:** Aircraft lands at current location
- **Anti-Jamming/Spoofing:** UBlox jamming/spoofing detection provides input to avionics when detected
- **Redundancy:** IMU integration for short-term operations when GNSS unavailable
- **Accuracy (GNSS Available):** 10 cm (RTK assumed)
- **Accuracy (GNSS-Denied):** Can be integrated as needed

**Communications, Datalinks & Networking:**
- **Primary C2 Datalink:** 900 MHz SwiftCore command/telemetry protocol; 8 km LoS (30 km with optional long-range LoS antenna)
- **Video/Payload Downlink:** Not separately designed/integrated; current scientific payloads share command/telemetry datalink
- **Backup Datalink:** 2.4 GHz manual handset link (on-command switchover)
- **Datalink Architecture:** Point-to-point, line-of-sight (standard); optional Iridium SATCOM for beyond-line-of-sight (unlimited range)
- **Onboard Compute:** Provisions for third-party payload integration via open SDK-based message protocol

**Ground Control Station (GCS):**
- **Form Factor:** Map-based app on Android tablet
- **Dimensions:** 9" × 5" × 0.5"
- **Weight:** 1.1 lbs.
- **Display:** 8" PLS LCD, 1200 × 1920 resolution
- **Environmental Rating:** IP68 (fully sealed)
- **Power/Battery:** Internal Li-Ion 5050 mAh battery; 8-hour operational life
- **Capabilities:** Mission planning with terrain model, real-time waypoint adjustment, live video feed, telemetry monitoring, health/status logs

**Mission Data Handling:**
- **Full-Motion Video:** HD daylight (up to 1080p, H.264/H.265, onboard compression)
- **Still Imagery:** Operator-initiated frame capture from live stream
- **Geospatial Metadata:** Embedded in standard formats
- **Recording Locations:** AV onboard storage (16 GB MicroSD, 50 Hz); GCS internal memory (128 GB, 50 Hz); Datalink internal MicroSD (16 GB, 10 Hz)
- **Data Security:** Currently not encrypted at rest; logs in NetCDF format
- **Field Extraction:** Download via USB-C or Wi-Fi; <20 seconds
- **Video/Telemetry Recording:** TBD upon EO/IR sensor integration

**Performance Envelope (with baseline EO/IR