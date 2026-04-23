# #emass

## Overview
Channel for coordination of the EMASS (machine learning AI chip) integration project with Black Swift Technologies. The project involves integrating EMASS's custom AI hardware and ML-based flight controller onto the E2 aerial platform to evaluate potential improvements in flight efficiency and endurance.

**Key Participants:**
- Dan Prendergast (project lead, primary point of contact)
- Jack Elston (software/firmware engineer)
- Ethan Domagala (hardware integration)
- Maciej (controls/simulation)
- Beck Cotter (proposals/planning)
- Scott and Mark (CEO) from EMASS (external partner)
- Nikhila (external, ML model training and bench-test app development)
- Moe (EMASS contact)
- Alex Lomis (flight operations/coordination)

**Activity Level:** Ongoing active project spanning November 2025 - April 2026, with critical intensity. Hardware-in-the-Loop (HWIL) and bench testing actively underway; real flight testing imminent (targeting early May). EMASS planning media release for their chip first week of May, creating deadline pressure.

## Key Decisions

**November 2025:**
- Beck Cotter created initial kickoff presentation based on proposal
- Clarified task division: EMASS would run simulators and AI training; BST would provide aerodynamic models and E2 parameters
- Dan Prendergast noted in proposal that any BST simulations would be low-res, for safety only, not proof of EMASS chip efficacy

**January 2026:**
- Project completion date pushed to March 11, 2026
- Jack Elston identified interface freeze as critical milestone to prevent firmware/AI scope creep
- Agreed to emphasize need for stable interfaces early, demo-focused success criteria, and fast turnaround on decisions
- Performance expectations reset: EMASS initially claimed 40-85% improvement (deemed "delusional"), Scott later agreed to target 30%, BST set realistic expectation of 10-15%

**February 2026:**
- Ethan Domagala completed mount and interface cable; identified voltage mismatch (3.3V UART input vs 5V output) requiring level translator
- Jack Elston provided level shifter solution
- Created external EMASS-BST Slack channel for coordination

**March 2026:**
- Decided on full control handoff model: EMASS controller operates at 75Hz with full actuator authority or BST autopilot operates at 250Hz; no mixed control
- Pitch/roll/yaw angle commands chosen as safe outer control loop (not rates) for EMASS to command
- Jack Elston completed major sim architecture rework with headless testing mode and dual socket architecture (payload port 55551, GCS port 55555)

**April 2026:**
- Ordered Pico 2 with headers for new hardware requirement from EMASS
- **April 13-15:** Multiple firmware updates and GCS fixes deployed by Jack Elston to resolve communication issues; HWIL testing actively underway
- **April 16:** Weather assessment indicates Monday/Tuesday (April 21-22) suitable for E2 flight testing with EMASS payload
- **April 20-22:** GitLab project created (`blackswifttechnologies/emass-test`) for managing test software and binaries instead of passing zip files
- **April 22:** Committed to real-time debugging meeting with Nikhila and Moe (EMASS team) morning of April 23 (9-10am or flexible time) to troubleshoot command transmission issues; EMASS team willing to work flexible hours due to timezone/deadline pressure

## Projects & Initiatives

### EMASS Integration (Primary)
**Status:** Critical debugging phase; bench testing on E2 underway; real flight testing scheduled for late April/early May, with EMASS media release planned for first week of May creating hard deadline

**Scope:**
- Integrate EMASS's ECS-DoT evaluation board (AI chip with ML controller) onto E2 platform
- Develop interface between EMASS hardware and E2 autopilot
- Create simulation environment (Gazebo-based SWIL) for validation
- Conduct flight testing with comparative analysis (controller on/off)
- Timeline: Originally January-March 2026, pushed to March 11, 2026; further delays occurred due to EMASS team responsiveness and BST resource conflicts; HWIL testing active as of mid-April; bench testing on E2 platform started April 21-22; real flights targeting late April/early May 2026

**Technical Components:**

1. **Hardware Integration:**
   - Custom mount for AI board on E2
   - UART interface with level translation (3.3V to 5V)
   - Power delivery through 5V barrel connector
   - Magnetometer calibration adjustments after battery relocation
   - ECS-DoT eval board communication via two devices (UART and JTAG connections)
   - Serial connection options: DB9 connector or jumpers + USB microUSB (preferred per Jack Elston as of April 22)
   - Baud rate: 460800 bps (verified working April 22)

2. **Firmware/Software (As of April 22):**
   - Autopilot modifications to accept EMASS actuator commands at 75Hz via UART
   - Two-mode operation: EMASS control or BST autopilot control (no blending)
   - EXTERNAL mode in autopilot for payload authority handoff
   - Protections to automatically revert to BST control on failure/timeout
   - Headless testing framework with pass/fail criteria
   - Serial baud rate adjustable through tablet interface (baud rate changes must be made via tablet, not command line)
   - Parameter synchronization via `param_mr_0x41000002.bst` file (safety limits enforced, model tuning allowed)
   - Recent updates (April 20-22):
     - Jack Elston added logging to capture state machine transitions and rates
     - Telemetry adjustments to ensure timing requirements met
     - New autopilot binary pushed April 22 with improved connection debugging
     - Binary version: 0x358094b (per Maciej April 21)
     - Fixes to bench-test and full-flight app connection issues
   - **Critical Issues Identified (April 22):**
     - **Command transmission not confirmed:** High confidence that EMASS actuator commands are not actually being transmitted to E2 autopilot despite successful connection establishment
     - Bench-test app connects and runs but produces no effect on SimE2 (rotors stay at ~68%, no controller response)
     - Full-flight app connection/handshake successful in simulation but behavioral validation needed
     - Gazebo HWIL app successfully commanding motors (8-point flight plan executed cleanly; EMASS controller staying within safety limits on latest retraining)
     - Discrepancy: gazebo-hwil-flight app works end-to-end; bench-test and live-flight apps do not command effectively
   - Rate timing issues observed in earlier testing now attributed to connection/telemetry synchronization fixes

3. **Simulation:**
   - Gazebo SWIL with realistic E2 dynamics
   - Current model implementation (with power consumption calculations)
   - Support for headless automated testing
   - Trajectory replay capability
   - Socket-based test framework (preferred over test app for HWIL)
   - Gazebo HWIL flight app confirmed working: EMASS controller flew complete 8-point flight plan with no disconnects or safety limit violations (April 22)
   - Issue: bench-test app behaves differently in simulation (connects, takes off, starts controller, controller has no effect for 40 seconds, then times out)

4. **Flight Testing:**
   - Scheduled for late April/early May 2026 (weather dependent; April 21-22 initial target)
   - Alex Lomis coordinating flight operations
   - Payload activation via Payload tab on tablet (SDK tab preferred interface)
   - Speed limit monitoring (4.0 m/s threshold triggering shutdowns when exceeded)
   - Latest EMASS controller retraining successfully stays within safety limits (no limit violation disconnects observed in recent testing)

**GitLab Repository:**
- Created: `https://gitlab.com/blackswifttechnologies/emass-test`
- Purpose: Centralized management of test software, binaries, and documentation (replacing ad-hoc zip file sharing)
- Contents (as of April 22): Autopilot binaries, README with timing requirements and debugging