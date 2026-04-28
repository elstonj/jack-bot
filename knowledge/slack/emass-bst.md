# #emass-bst

## Overview
This channel serves as the primary collaboration hub between Black Swift Technologies (BST) and eMASS AI for integrating the ECSDoT hardware (an energy management system) onto the E2 aircraft platform. The channel covers software development, hardware integration, testing, and model training activities.

**Key Participants:**
- Nikhila (eMASS AI) - Primary developer, leading chip integration and AI model implementation
- Jack Elston (BST) - Autopilot/simulation expertise, hardware integration guidance, protocol specification, flight testing, data analysis
- Dan Prendergast (BST) - Flight test coordination, E2 aircraft management, hardware setup lead, simulator testing
- Mohamed M. Sabry (eMASS AI) - AI model training and constraint optimization
- Moe/Prof. Moe (eMASS AI) - AI model training and optimization
- Maciej (BST) - Vehicle parameters and specifications
- Sergio Ruocco (eMASS AI) - Autoboot firmware expert, SDK bring-up and troubleshooting
- Shantanu (eMASS AI) - Hardware verification and validation

**Activity Level:** Highly active collaboration spanning February-April 2026. Intensive HWIL and model training in March-April. Most recent activity (Apr 27-28, 2026) focused on post-first-flight debugging, PWM value discrepancies, AI model refinement, and preparation for next flight test. Critical first-flight test completed on Apr 24, 2026.

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

**Baud Rate Increase (Apr 20-21, 2026)**
- eMASS team (Nikhila, Prof. Moe, Shantanu) proposed increasing baud rate from default to address packet rate and connectivity issues
- Jack Elston approved all three options: 230400, 460800, or 921600 baud
- Nikhila tested and confirmed 460800 works with both chip and autopilot
- **Decision: Set baud rate to 460800** for improved packet transmission reliability

**Event System Refactoring (Apr 20, 2026)**
- Nikhila refactored eMASS event system to use different API functions, resolving reconnection looping issues
- Root cause was bench test code using different function calls than gazebo_hwil and droneapp
- Fix applied across all three application binaries (bench test, droneapp, gazebo-hwil)

**External Control Mode Implementation (Apr 23, 2026)**
- Jack Elston identified critical missing control mode configuration: ECSDoT chip must request and operate in "external" control modes
- **Decision: Implement dual control mode commands:**
  - Request external control: Set `CMD_ALT_MODE` and `CMD_LAT_MODE` to `ALT_MODE_EXTERNAL` and `LAT_MODE_EXTERNAL` respectively
  - Only send actuator packets after autopilot confirms mode change to external
  - Relinquish control on shutdown: Set modes back to `ALT_MODE_RATE` and `LAT_MODE_AUTO`
- Rationale: Autopilot "steps aside" only when explicitly told to operate in external mode; prevents conflicting control signals
- Status: Verified working in pre-flight testing - "if I send those commands, I'm seeing your hardware take over control" (Jack Elston, Apr 23 12:41)

**Waypoint Modification for Part 107 Compliance (Apr 25, 2026)**
- Jack Elston identified that original waypoints violated the 120m ceiling requirement for Part 107 operations
- **Decision: Modified waypoints to ensure compliance** while maintaining test objectives
- Updated waypoint list provided to eMASS team for AI model training and next test flight

**Dual AI Model Variants for Constraint Testing (Apr 25, 2026)**
- Mohamed M. Sabry proposed generating two updated AI models with different constraint levels for next flight
- **Decision: Two models to be provided:**
  - Model 1: Maximum 4% change constraint
  - Model 2: Maximum 10% change constraint
- Rationale: Will enable testing of AI accuracy improvements using flight data from compliant waypoint path (same path used for Gazebo training)
- Status: Models to be sent to BST before next test flight

**AI Model Control Behavior Specification (Apr 25-26, 2026)**
- Jack Elston requested clarification on AI model behavior once activated in flight: "will it hold a point or try to fly somewhere?"
- Mohamed M. Sabry confirmed: AI model primarily follows the planned path/waypoints and will hover if waypoints imply a hover command
- Rationale: Model trained to track waypoint-based flight plans, not maintain fixed positions

**Waypoint Loading & Active Plan Verification (Apr 26, 2026)**
- Jack Elston inquired whether eMASS is actively checking which waypoints are loaded and which flight plan is active
- Status: Clarification pending from eMASS team regarding active monitoring of loaded waypoints and plan status in flight

**PWM Value Range Correction (Apr 27, 2026)**
- Nikhila identified discrepancy in PWM actuator value conversion in emass_handler.cpp
- Current code assumes range: -100→1000µs, 0→1500µs, +100→2000µs (formula: 1500 + actuators[i] * 5)
- Flight Log User Guide references different range: 1150µs (0%) to 1900µs (100%)
- **Decision: Pending clarification from Jack Elston on correct PWM value ranges**
- Impact: Simple loopback test sending incoming PWM values back caused autopilot shutdown, indicating conversion error
- Status: Awaiting corrected range specification before next test

**AI Model PWM Output Rate Adjustment (Apr 27, 2026)**
- eMASS team (Nikhila, Prof. Moe) reduced PWM actuator output rate from 75Hz to 25Hz
- Rationale: Concern that 75Hz was too fast for stable control
- **Decision: Test new 4% constraint model at 25Hz