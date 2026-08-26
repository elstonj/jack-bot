# BST White Paper — RFI Drone CLT

## Document Metadata
- **Type:** White Paper (response to RFI)
- **Client/Agency:** HQ USSOCOM (United States Special Operations Command), SOF AT&L (Special Operations Forces Air, Land & Theater), PEO-Fixed Wing
- **Program/Solicitation:** RFI — Drone CLT (Notice ID H9240826RFIDRONECLT)
- **Date:** August 2026
- **BST Products/Systems Referenced:** S0 (backpackable & air-deployed), S0-VTOL, S2/SuperSwift, S3, E2, SwiftCore Flight Management System, SwiftCore Safe Sandbox
- **Key Personnel:** Dr. Jack Elston (Founder & CEO)

---

## Executive Summary

Black Swift Technologies proposes to deliver a Group 1/2 unmanned aircraft system (UAS) employable from the Common Launch Tube (CLT) on SOF fixed-wing hosts (e.g., AC-130J Ghostrider). BST's S0 platform is already fielded operationally with NOAA/USAF, has demonstrated extreme-environment survivability (240 mph Guinness-verified wind record inside Hurricane Milton, October 2024), and holds a proven track record across 19 operational deployments in 2024 alone. BST is actively engineering CLT integration through a Navy SBIR effort and direct USSOCOM engagement, with a fielded S0 variant and passive elastic launch rail purpose-built to reproduce ~10 g tube-deployment shock profiles. The company's proprietary SwiftCore autopilot exposes an open machine-to-machine (M2M) API designed to integrate with government-owned collaborative autonomy services (FANTOM Core) and Battle Management Systems (BMS).

---

## Technical Approach

**Core Strategy:**
BST proposes to adapt its fielded S0 platform for CLT employment rather than developing a clean-sheet vehicle. The approach leverages existing airframe and avionics maturity (TRL 8–9) while spiraling CLT-specific elements (canister interface, effector packaging, launch qualification) to TRL 6+.

**Key Technical Elements:**

1. **Airframe & Form Factor**
   - Stowed S0 with folded wings/tail fits within 5.9-inch diameter × 42-inch length CLT envelope
   - Vehicle weight well under the ≤55 lb not-to-exceed (NTE) limit, providing growth margin for warhead/payload
   - Extreme-environment hardening proven through repeated Category 4/5 hurricane deployments

2. **Launch Survivability & Qualification**
   - BST has designed and built a reusable, ground-launched S0 variant paired with a passive elastic launch rail (Navy SBIR N6833525C0492)
   - Elastic rail tuned to reproduce ~10 g tube-deployment shock profile without active systems or complex tuning
   - Constructed primarily from off-the-shelf extrusion for field assembly and travel
   - Reusable test article enables repeated, rapid iteration on launch-shock tolerance
   - Qualification path: elastic-rail g-replication → captive-carry integration → live SOF-platform release

3. **Flight Control & Autonomy: SwiftCore FMS**
   - Two-tier modular architecture:
     - **Flight-Critical Safety Tier:** STM32/FreeRTOS (handles flight-safety-critical functions)
     - **Mission-Autonomy Tier:** Linux SBC (higher-level autonomy, tasking, collaborative operations)
   - **SwiftCore Safe Sandbox:** Runtime-assured autonomy partition isolating mission-autonomy code from flight-safety functions, enabling government autonomy services to command vehicle without touching safety-critical code
   - **M2M API:** Documented machine-to-machine interface designed to accept command-and-control from government-owned FANTOM Core and Battle Management Systems
   - MOSA/WOSA-aligned modular interfaces with versioned hardware/firmware baselines and interface control documents (ICDs)

4. **Host Integration**
   - Air-deployment pedigree: S0 currently air-deployed from NOAA/USAF WP-3D "Hurricane Hunter" at mission airspeeds (120–300 KTAS)
   - In development: freefall-chute deployment package for C-130-class hosts
   - Release windows: 120–300 KTAS airspeed, 5,000 ft AGL to 35,000 ft MSL altitude
   - Transition-to-flight validated under extreme dynamic pressure and turbulence conditions

5. **Navigation in Contested Environments**
   - GPS-denied navigation ("DS-GPS") developed under NOAA SBIR Phase II
   - Resilient positioning, navigation & timing (PNT) baseline for contested/denied-access operations
   - Anti-jam datalink and encrypted C2 architecture supported by SwiftCore

6. **Mission Endurance & Performance**
   - Range to loiter: ≥75 nautical miles (within fixed-wing S0 energy budget)
   - Loiter time: ≥40 minutes at 500–3,000 ft AGL
   - Cruise/loiter speed: 50–100 knots; dash capability 100+ knots
   - Payload bay: modular design flown with multiple sensor packages (EO/IR, meteorological, magnetic-anomaly detection)

7. **Environmental Qualification**
   - Operating temperature: −40 °F to 135 °F (cold-weather hardening active; S2/S3 heritage from Alaska/Greenland operations)
   - Vibration/shock: MIL-STD-810H Category 8 environment; 2-ft drop qualification planned
   - Extreme dynamic pressure: Proven by 240 mph wind survival in Category 5 hurricanes

**Design & Process Rigor:**
- Lightweight but disciplined systems-engineering process with traceable requirements (objective/threshold workbook bidirectionally linked to stakeholder needs)
- Multidisciplinary peer review before each build spiral
- Vertically integrated airframe/avionics/software design cycle (internal ownership of all critical components reduces vendor lead-time risk)
- Bench → captive-carry → flight test progression with high sortie rate
- Configuration management via versioned hardware/firmware and documented ICDs per interface

---

## Products & Capabilities Described

### **S0 (Backpackable & Air-Deployed UAS)**

**What it is:**
- Group 1/2 unmanned aircraft system designed for rapid deployment and extreme-environment operation
- Currently fielded with NOAA/USAF Hurricane Hunters and multiple U.S. military agencies (Navy, USSOCOM, Air Force)
- Air-deployable from fast-moving fixed-wing hosts; can be hand-launched

**Extreme-Environment Pedigree:**
- **Guinness World Record:** Highest wind speed recorded by uncrewed aircraft — 240 mph, measured inside Hurricane Milton, October 2024 (NCAR verified)
- **Operational Deployments:** 19 S0 aircraft deployed in 2024 hurricane season; multiple Category 4/5 hurricane penetrations
- **Survivability:** Independently documented resilience to extreme dynamic pressure, turbulence, and precipitation

**Proposed CLT Employment:**
- Stowed configuration fits 5.9-in × 42-in envelope
- Weight well under 55 lb NTE, leaving growth margin for warhead/payload
- Air-deployment from SOF hosts at 120–300 KTAS airspeeds
- Autonomous transition to controlled flight post-release
- Endurance supports ≥75 NM range-to-loiter and ≥40 min loiter at 500–3,000 ft AGL

**Payload Flexibility:**
- Modular payload bay flown with:
  - EO/IR sensors (passive, low-RF signature)
  - Meteorological instruments (NOAA heritage)
  - Magnetic-anomaly detection (MAD) (Navy program heritage)
  - ATR (Automatic Target Recognition) integration with government-furnished equipment (GFE) or partner sourcing

**Current Manufacturing Status:**
- Production-representative hardware built and tested
- Established build procedures and acceptance tests
- Low-rate production capability demonstrated (19 aircraft in single season)
- TRL 8–9 for airframe and avionics

---

### **S0-VTOL**

**What it is:**
- Vertical-takeoff-and-landing variant of the S0 platform (referenced in platform lineup but not detailed in this white paper)

---

### **S2 / SuperSwift**

**What it is:**
- Larger Group 1/2 fixed-wing UAS in BST's product line
- Cold-weather heritage from Alaska/Greenland operations (referenced for temperature-hardening experience)
- EAR classification: ECCN 9A012

---

### **S3**

**What it is:**
- Extended-range or higher-endurance variant in BST's product line
- Cold-weather heritage; EAR self-classified as EAR99
- Referenced for environmental-hardening experience

---

### **SwiftCore Flight Management System (FMS)**

**What it is:**
- Proprietary, modular, open-architecture autopilot designed and built in-house by BST
- Three generations of complete avionics systems developed by BST

**Architecture & Integration:**
- **Two-tier design:**
  - Flight-critical safety tier (STM32/FreeRTOS kernel)
  - Mission-autonomy tier (Linux single-board computer)
- **SwiftCore Safe Sandbox:** Runtime-assured autonomy partition isolating mission code from safety-critical functions per MOSA/WOSA intent
- **M2M API:** Machine-to-machine interface exposing command-and-control to external services (FANTOM Core, BMS)
- **Modular interfaces:** Documented ICDs aligned to modular open-systems approaches

**Proposed C2 Integration (CLT RFI):**
- SwiftCore M2M API as primary integration point for government-owned FANTOM Core collaborative autonomy
- BMS (Battle Management System) integration via documented M2M message set
- Support for encrypted C2 and anti-jam datalinks
- Intra-platform communications (with host aircraft and collaborating effectors) via M2M interface

**Development Heritage:**
- Advanced through NASA and DAF (Department of Air Force) efforts focused on secure, adaptive, and runtime-assured autonomy
- Designed to accept third-party or government autonomy services without requiring changes to safety-critical code

---

### **SwiftCore Safe Sandbox**

**What it is:**
- Runtime-assured autonomy partition within SwiftCore architecture
- Isolates mission-autonomy functions from flight-safety-critical functions

**Proposed Use in CLT Context:**
- Enables government autonomy services (e.g., FANTOM Core) to command vehicle behavior without access to safety-critical flight-control code
- Foundation for secure, adaptive collaborative autonomy in contested environments

---

## Use Cases & Applications

### **Primary RFI Use Case: SOF Rapid-Employment Platform**
- **Mission Profile:** Air-deployed from SOF fixed-wing hosts (AC-130J Ghostrider or similar CLT-equipped platform)
- **Release Scenario:** Release from 120–300 KTAS, 5,000 ft AGL to 35,000 ft MSL
- **Operational Sequence:** Release → autonomous transition to controlled flight → transit ≥75 NM → loiter ≥40 min at 500–3,000 ft AGL with passive EO/IR or ATR payload
- **C2 Environment:** Contested or non-contested; M2M integration with FANTOM Core and BMS
- **Payload:** Passive low-RF seeker preferred; payload-flexible design supports government-furnished effector elements

### **Fielded Heritage Use Cases (Demonstrating Platform Maturity)**

**Hurricane Sampling & Meteorological Research (NOAA/USAF WP-3D)**
- Air-deployment from fast-moving fixed-wing host (WP-3D "Hurricane Hunter")
- Operation in extreme wind (240 mph Category 5 conditions proven)
- Meteorological and environmental sensor payloads
- 19 operational deployments in 2024 hurricane season
- Direct evidence of extreme-environment survivability and operational reliability

**Navy Programs**
- Magnetic-anomaly detection (MAD) payload integration
- Launch-survivability engineering under Navy SBIR (N6833525C0492)
- Reusable ground-launched variant with elastic launch rail for shock qualification
- Demonstrates BST's