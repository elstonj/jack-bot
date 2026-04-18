# #emass-bst

## Overview
This channel serves as the primary collaboration hub between Black Swift Technologies (BST) and eMASS AI for integrating the ECSDoT hardware (an energy management system) onto the E2 aircraft platform. The channel covers software development, hardware integration, testing, and model training activities.

**Key Participants:**
- Nikhila (eMASS AI) - Primary developer, leading chip integration and AI model implementation
- Jack Elston (BST) - Autopilot/simulation expertise, hardware integration guidance, protocol specification
- Dan Prendergast (BST) - Flight test coordination, E2 aircraft management, hardware setup lead
- Moe/Prof. Moe (eMASS AI) - AI model training and optimization
- Maciej (BST) - Vehicle parameters and specifications
- Sergio Ruocco (eMASS AI) - Autoboot firmware expert, SDK bring-up and troubleshooting

**Activity Level:** Highly active collaboration spanning February-April 2026. Initial setup in early February ramped to intensive HWIL and model training in March-April. Most recent activity (Apr 17, 2026) focused on bench test debugging. Daily communication during critical phases.

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

**Safety Limits Enforcement (Apr 15, 2026)**
- Jack Elston determined that safety limits should remain as-is for flight testing (same as E2 specifications)
- Decided against changing autopilot limits in simulation; instead eMASS to retrain AI model for stricter adherence to limits
- Rationale: Simulation validation should reflect actual flight envelope constraints

---

## Projects & Initiatives

### ECSDoT Integration onto E2 Aircraft
**Status:** Final flight test preparation with active bench test debugging (as of Apr 17, 2026)

**Scope:** Integrating eMASS AI's ECSDoT energy management chip onto BST's E2 multirotor UAS for final flight testing.

**Components:**
- UART communication interface (/dev/ttyUSB0) between autopilot and ECSDoT chip
- Telemetry reception → AI inference → PWM actuator output pipeline
- Integration with SwiftPilot autopilot (pro_core_swil_MULTIROTOR)
- Payload protocol implementation over port 55551 with GCS control via port 55555

**Recent Progress (Apr 8-17, 2026):**
- **Hardware Bring-up (Apr 8-14):**
  - Resolved JTAG/UART dual connection issues on Eval Board (FTDI Dual RS232-HS)
  - Fixed Linux user permissions issue (dialout group requirement) blocking serial device access
  - Successfully compiled and ran HelloWorld on Eval Board via Docker SDK
  - Transitioned to Pico 2 autoboot procedure with firmware flashing
  
- **Payload Protocol Implementation (Apr 14-16):**
  - Identified and corrected payload connection state cycling issue
  - Root cause: Incorrect packet sequence understanding; AI chip was sending `PAYLOAD_CTRL_READY` too quickly after `SYSTEM_INITIALIZE`
  - Fixed by implementing proper packet sequence per Jack Elston's protocol specification:
    1. Continuous heartbeats (0.2s interval) from payload
    2. Wait for `SYSTEM_INITIALIZE` request from autopilot
    3. Respond with initialization packets
    4. Wait for `READY` command from tablet (not from chip)
    5. Chip can request `ACTIVE` control only after `READY` received
    6. Send actuator packets only after autopilot confirms running state
  - Resolved heartbeat timeout issue (reduced from higher interval to 0.2s per Jack's guidance)
  - Fixed UART receive buffer blocking issue that prevented heartbeats during `PAYLOAD_WAITING` state (Apr 3:13 AM)

- **AI Model Performance Issues (Apr 14-16):**
  - Model inference producing 4% rate of actuator values that exceed autopilot safety limits (80 violations per 2000 inferences)
  - SHUTDOWN events occurring when AI output exceeds vrate limit (e.g., vrate = 3.01 when max is 3.0)
  - After SHUTDOWN, tablet must resend `READY` command to reconnect
  - Initiated model retraining for stricter adherence to safety constraints

- **Bench Test Debugging (Apr 17):**
  - Nikhila investigating potential race condition causing bench-test program to hang
  - Indicates possible connectivity or state machine logic issue unrelated to simple connectivity failures
  - Debugging underway; resolution expected same day

**Binaries Available (as of Apr 17, 2026):**
1. **Bench Test Binary** - 40 second test with 20s @ 1300µs, 20s @ 1400µs PWM output (under debugging)
2. **HWIL Gazebo Sim-Only** - AI model trained on sim-only data
3. **HWIL Real Flight Data** - AI model trained with actual E2 flight data
4. **Droneapp-20260402_2007** - Flight test binary with integrated AI model (latest as of Apr 17)
5. **Test Binary** - Generic testing application

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
- Apr 6-7: Delivered bench test code and executable binaries
- Apr 8: Assisted with Docker image access troubleshooting (token/permission verification)
- Apr 8-9: Provided detailed hardware wiring and connection guidance
- Apr 10: Delivered SWIL app with AI model
- Apr 11-12: Delivered HWIL Gazebo sim-only binary with compilation instructions
- Apr 14-15: Fixed heartbeat protocol issues (0.2s interval); implemented proper payload state machine
- Apr 15: Identified and corrected packet sequence misunderstanding in payload protocol
- Apr 15: Delivered updated gazebo sim-only and actual flight binaries with corrected protocol
- Apr 15: Initiated Google Meet with Prof. Moe and Dan to discuss model training improvements
- Apr 16-17: Delivered three updated binaries (bench test, HW