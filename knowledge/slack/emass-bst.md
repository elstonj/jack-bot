# #emass-bst

## Overview
This channel serves as the primary collaboration hub between Black Swift Technologies (BST) and eMASS AI for integrating the ECSDoT hardware (an energy management system) onto the E2 aircraft platform. The channel covers software development, hardware integration, testing, and model training activities.

**Key Participants:**
- Nikhila (eMASS AI) - Primary developer, leading chip integration and AI model implementation
- Jack Elston (BST) - Autopilot/simulation expertise, hardware integration guidance
- Dan Prendergast (BST) - Flight test coordination, E2 aircraft management
- Moe (eMASS AI) - AI model training and optimization
- Maciej (BST) - Vehicle parameters and specifications

**Activity Level:** Highly active collaboration spanning February-April 2026, with daily communication during critical integration phases. Initial setup discussions in early February ramping to intensive HWIL (Hardware-In-The-Loop) and model training work in March-April. Recent activity shows transition toward flight test finalization (early April 2026).

---

## Key Decisions

**C++ Firmware Capability (Feb 11, 2026)**
- Dan Prendergast requested clarification on whether C++ could be used in eMASS firmware, with Jack Elston offering to review initial code implementation.

**Energy Savings Methodology (Mar 16-17, 2026)**
- Decided to measure energy savings through flight time comparison rather than real-time calculation
- Jack Elston raised concerns about accuracy, suggesting integration of instantaneous current per flight phase may be more reliable
- Agreed to use BST flight logs to validate approach

**Payload Architecture (Mar 26, 2026)**
- Established that only one payload can connect at a time on port 55551
- ECSDoT chip designated as the primary payload; EMASS application would not connect as payload
- Test program via GCS port 55555 would be used for takeoff/landing

**Waypoint Strategy (Mar 24-25, 2026)**
- Expanded waypoint collection from limited sample to 16 waypoints with varying altitudes
- Decision made to generate sim-only training data first, then validate with real flight data in HWIL

**Hardware Addition (Apr 1, 2026)**
- Determined that a Raspberry Pi Pico 2 with headers is required for autoboot functionality

**Flight Test Priority Over Research (Apr 6, 2026)**
- Jack Elston confirmed that current Statement of Work (SOW) takes priority over eMASS internal research needs
- Decision to defer building safety-guard-free autopilot variant until after flight test completion
- Rationale: Removing limit checks is time-consuming; completing flight test is the immediate priority

---

## Projects & Initiatives

### ECSDoT Integration onto E2 Aircraft
**Status:** Final flight test preparation phase (as of Apr 6, 2026)

**Scope:** Integrating eMASS AI's ECSDoT energy management chip onto BST's E2 multirotor UAS for final flight testing.

**Components:**
- UART communication interface (/dev/ttyUSB0) between autopilot and ECSDoT chip
- Telemetry reception → AI inference → PWM actuator output pipeline
- Integration with SwiftPilot autopilot (pro_core_swil_MULTIROTOR)

**Recent Progress:**
- AI pipeline fully operational as of Mar 20, 2026
- ECSDoT chip successfully connects to autopilot and receives PAYLOAD_CTRL_ACTIVE commands
- PPO (Proximal Policy Optimization) inference running at 70 Hz
- Model validation in SWIL (Software-In-The-Loop) environment completed
- Real flight data model training completed; HWIL testing underway as of Apr 1
- Model performing with minimal errors in HWIL validation

**Current Work:**
- Final HWIL validation tests with Pico 2 autoboot support in progress
- Preparing for flight test execution with current safety-constrained autopilot
- eMASS planning internal research study in simulation (safety-guard-free variant) as post-flight-test activity

---

## Action Items & Commitments

### From Nikhila (eMASS AI)

**Completed:**
- Feb 13: Requested GitHub usernames to share ECSDoT SDK
- Feb 22: Provided Docker image with sample code and build instructions
- Mar 20: Completed AI pipeline integration; delivered binary app and source code via docker pull
- Mar 24: Provided sim-only flight data (CSV file) to Prof. Moe for model training
- Mar 25: Committed to HWIL validation with sim-only model by end of day
- Mar 27: Committed to validate AI model with minimal errors over weekend
- Apr 5: Requested access to safety-guard-free autopilot variant for internal research study in simulation

**Pending:**
- Complete internal AI model study in simulation (post-flight-test, per Apr 6 decision)

### From Jack Elston (BST)

**Completed:**
- Feb 9: Clarified that gcsDaemon sensor errors in simulation are expected/benign
- Mar 11: Provided candidate interface running in Gazebo sim with README instructions
- Mar 24: Provided minor fix to third test case
- Mar 26: Delivered detailed UART connection instructions for ECSDoT-SwiftPilot integration
- Mar 30: Clarified that cruise speed is safety parameter, not physical limit
- Mar 31: Confirmed no existing wind/disturbance models available in Gazebo
- Apr 6: Confirmed prioritization of flight test completion over research needs; committed to building safety-guard-free autopilot variant after SOW completion

**Pending:**
- None explicitly stated in immediate term

### From Dan Prendergast (BST)

**Completed:**
- Feb 3: Added E2 flight data logs (E20006, E20009) to shared drive; recommended using E20009 logs for final test training
- Feb 11: Requested code review and assistance documentation
- Feb 27: Provided 6 minutes of E2 flight data with benign and dynamic flight sections, ECS-DoT hardware mounted as per final configuration
- Mar 20: Requested GitHub access via email dtprendergast@live.com
- Mar 24: Provided 16-waypoint flight plan code with varying altitudes to replace test case

**Pending:**
- None explicitly stated

### From Maciej (BST)

**Completed:**
- Mar 31: Provided updated battery capacity specification: 907.2 Wh (converted from Ah, recently switched units)

---

## Client & External References

### Internal Collaboration
- **Prof. Moe** (eMASS AI) - AI model training and optimization; initiating internal research study on AI model behavior in simulation (Apr 5)

### External Hardware/Software
- **Gazebo Simulation** - SwiftPilot SWIL simulation environment
- **GitHub Repository:** `https://github.com/emassAI/ecsdot-baremetal-sdk-blackswift`
- **Docker Images:**
  - `ghcr.io/emassai/ecsdot-baremetal-sdk-blackswift/ecsdot-baremetal-sdk-blackswift_amd64:release-refactor-81b5d22b` (Feb 22)
  - `ghcr.io/emassai/ecsdot-baremetal-sdk-blackswift/ecsdot-baremetal-sdk-blackswift_amd64:release-refactor-13270a8a` (Apr 1 - with real flight data model)
- **Vehicle Platform:** E2 multirotor UAS (two aircraft: E20006, E20009)
- **Autopilot:** SwiftPilot (pro_core_swil_MULTIROTOR)
- **Hardware:** Raspberry Pi Pico 2

---

## Recurring Topics & Themes

### 1. **Integration & Communication Protocol**
- Continuous troubleshooting of UART communication and payload handshake procedures
- Payload detection, telemetry reception, and control authority arbitration
- GCS daemon errors and debug procedures (Feb 8-9)

### 2. **Model Training & Data Collection**
- Iterative cycles of data collection → model training → validation
- Requests for additional varied data to improve model accuracy
- Shift from sim-only to real flight data training (Mar