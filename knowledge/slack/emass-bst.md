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
- Shantanu (eMASS AI) - Hardware verification and validation

**Activity Level:** Highly active collaboration spanning February-April 2026. Initial setup in early February ramped to intensive HWIL and model training in March-April. Most recent activity (Apr 20, 2026) focused on connection stability debugging and hardware verification. Daily communication during critical phases.

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

**3.3V Power Supply Confirmation (Apr 19, 2026)**
- Dan Prendergast requested confirmation that 3.3V can be sourced from J18 pin #1 for the 5-to-3.3V level shifter
- Nikhila confirmed with Shantanu that this configuration is acceptable and won't cause issues

---

## Projects & Initiatives

### ECSDoT Integration onto E2 Aircraft
**Status:** Connection stability issues identified and under investigation (as of Apr 20, 2026)

**Scope:** Integrating eMASS AI's ECSDoT energy management chip onto BST's E2 multirotor UAS for final flight testing.

**Components:**
- UART communication interface (/dev/ttyUSB0) between autopilot and ECSDoT chip
- Telemetry reception → AI inference → PWM actuator output pipeline
- Integration with SwiftPilot autopilot (pro_core_swil_MULTIROTOR)
- Payload protocol implementation over port 55551 with GCS control via port 55555
- 5-to-3.3V level shifter powered from J18 pin #1

**Recent Progress (Apr 8-20, 2026):**
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

- **Connection Stability Issues (Apr 19-20):**
  - **Problem Description:** Sporadic initial connections between autopilot and ECSDoT chip using gazebo-hwil-sim-only image
  - **Symptoms Observed (Dan Prendergast, Apr 19):**
    1. Inconsistent handshake behavior: Sometimes completes quickly through INIT → CONNECTING → CONNECTED → WAITING; other times gets stuck in CONNECTING state for several minutes; sometimes completes to WAITING but tablet still shows "Init" status
    2. Slow cycling pattern every couple of minutes: connection completes successfully (reaches WAITING state), then drops back to INIT and CONNECTING, stalls for minutes before reconnecting
    3. Cycle persists when picocom is NOT actively monitoring ttyUSB0
    4. Picocom interference confirmed: incomplete packets when picocom is running; connection state slower but more stable without picocom
    5. Faster initial connection when ECSDoT is connected AFTER autopilot startup, but slow cycling still occurs
  - **Status:** Nikhila investigating root cause; appears to be related to connection state machine logic or timeout handling rather than simple connectivity failure
  - **Next Steps:** Profile connection behavior to identify why cycles occur and tablet status doesn't sync with actual chip state

- **Hardware Verification (Apr 19):**
  - Confirmed J18 pin #1 providing 3.3V for level shifter supply
  - Shantanu (eMASS) verified this configuration is safe and won't cause issues

**Binaries Available (as of Apr 17, 2026):**
1. **Bench Test Binary** - 40 second test with 20s @ 1300µs, 20s @ 1400µs PWM output
2. **HWIL Gazebo Sim-Only** - AI model trained on sim-only data (currently under test with connection issues)
3. **HWIL Real Flight Data** - AI model trained with actual E2 flight