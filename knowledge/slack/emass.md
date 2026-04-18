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
- Nikhila (external, ML model training)
- Moe (EMASS contact, made autopilot request)
- Alex Lomis (flight operations/coordination)

**Activity Level:** Ongoing active project spanning November 2025 - April 2026, with increasing intensity. Hardware integration and HWIL (Hardware-in-the-Loop) testing actively underway; critical debugging phase as of April 17, 2026.

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

## Projects & Initiatives

### EMASS Integration (Primary)
**Status:** Hardware-in-the-Loop (HWIL) testing phase; critical debugging phase as of April 17, 2026; real flight testing scheduled for week of April 21, 2026

**Scope:**
- Integrate EMASS's ECS-DoT evaluation board (AI chip with ML controller) onto E2 platform
- Develop interface between EMASS hardware and E2 autopilot
- Create simulation environment (Gazebo-based SWIL) for validation
- Conduct flight testing with comparative analysis (controller on/off)
- Timeline: Originally January-March 2026, pushed to March 11, 2026; further delays occurred due to EMASS team responsiveness and BST resource conflicts; HWIL testing active as of mid-April; facing critical debugging issues as of April 17

**Technical Components:**

1. **Hardware Integration:**
   - Custom mount for AI board on E2
   - UART interface with level translation (3.3V to 5V)
   - Power delivery through 5V barrel connector (found USB A to micro cable insufficient; missing jumper wires between eval board and Pico board, being completed April 9)
   - Magnetometer calibration adjustments after battery relocation
   - ECS-DoT eval board communication via two devices (UART and JTAG connections identified)

2. **Firmware/Software (As of April 17):**
   - Autopilot modifications to accept EMASS actuator commands at 75Hz via UART
   - Two-mode operation: EMASS control or BST autopilot control (no blending)
   - EXTERNAL mode in autopilot for payload authority handoff
   - Protections to automatically revert to BST control on failure/timeout
   - Headless testing framework with pass/fail criteria
   - Serial baud rate adjustable through tablet interface
   - Parameter synchronization via `param_mr_0x41000002.bst` file (safety limits enforced, model tuning allowed)
   - **Recent fixes (April 13-15):**
     - GCS error message fixes
     - Edge case handling
     - Firmware build: 1057c5a5
     - Malformed packet detection and baud rate optimization
     - Serial link stability improvements
   - **Issues identified (April 17):**
     - Nikhila's `bench_test app` fails to connect in simulator environment; issue attributed to missing state machine fixes in `gazebo_hwil_flight_app` that were made in other application code (April 17, Dan Prendergast)
     - Connection state fallback issue: system incorrectly transitions to "fallback to connecting" state rather than "connected" state after shutdown and error conditions (April 17, Jack Elston identified root cause)
     - Recovery via `sys init` command expected to work but not being exercised
     - Critical regression: Initial connection establishment now failing after recent firmware push (April 17, evening); Jack Elston reports no changes made to connection logic, only shutdown/error state handling

3. **Simulation:**
   - Gazebo SWIL with realistic E2 dynamics
   - Current model implementation (with power consumption calculations)
   - Support for headless automated testing
   - Trajectory replay capability
   - Socket-based test framework (preferred over test app for HWIL)
   - Known issue: `gazebo_hwil_flight_app` missing state machine fixes present in other codebases (April 17)

4. **Flight Testing:**
   - Weather-dependent: Monday/Tuesday (April 21-22) identified as favorable conditions
   - Alex Lomis coordinating flight operations
   - Payload activation via Payload tab on tablet (SDK tab preferred interface)
   - Speed limit monitoring (4.0 m/s threshold triggering shutdowns when exceeded)

**Known Challenges:**
- EMASS team organization/responsiveness (especially Nikhila for ML model retraining and application state machine consistency)
- Schedule conflicts with other BST projects (ADONIS, USGS, hurricane, S3)
- Integrator wind-up issues in simulator
- Plugin loading issues in simulation environment
- Voltage interface compatibility between hardware (resolved with level shifters)
- Scope creep pressure (Moe/EMASS requesting autopilot without limits; request not escalated to Scott/Mark; rejected by Dan/Jack)
- **Critical (April 17):** Connection state machine bugs and potential regression in initial connection logic affecting HWIL testing
- Serial packet dropping at standard baud rates (partially resolved with baud rate increase)
- Payload speed limit violations during testing (model needs tuning to comply with 4.0 m/s safety limit)
- Financial/budgetary considerations emerging (April 6, 2026)
- HWIL setup complexity (three simultaneous processes: autopilot + UART flag, gcsDaemon, Gazebo)
- Code consistency issues across applications within same project (state machine fixes not propagated)

## Action Items & Commitments

**Outstanding (as of April 17, 2026):**
- Jack Elston: **URGENT** - Debug and resolve initial connection establishment failure introduced in latest firmware push (April 17, evening); clarify what changed vs. stated commit scope
- Jack Elston: Investigate reconnection after shutdown/error condition and validate `sys init` recovery mechanism (April 17)
- Nikhila (EMASS): Ensure `bench_test app` includes all necessary