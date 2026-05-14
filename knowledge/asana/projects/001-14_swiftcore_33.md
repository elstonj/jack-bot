# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: Active development (yellow status as of Nov 28, 2023, with overdue milestones and 78 open tasks). No recent team corrections indicate delays or status changes beyond Asana data.
- **Team members**: Jack Elston (owner), Maciej Stachura, Ben Busby, whole BST team
- **Risk signals**: 78 open tasks with no due dates assigned; multiple flight-critical bugs in joystick control, landing detection, flight termination, and surface actuation; significant concentration of safety/stability concerns requiring resolution before production release

## Key Deliverables & Milestones
**Open Milestones (no due dates assigned):**
- Final release supporting 2030, 2040 and likely 2050 and 3000 hardware
- Final release supporting commercial S1
- Adds initial tailsitter support
- Official scripting release (including payload control)
- Control through the payload serial interface
- Adds app support (payload, flight parameters, scripting)

**Completed Milestones:**
- Adds initial VTOL support (completed 2026-02-03)
- Unified Estimator (completed 2026-02-03)

## Task Summary
- **Total tasks**: 78 open, 375 completed (83% completion rate overall)
- **Tasks by assignee**:
  - Jack Elston: ~40 open tasks (majority workload; focus on surface control, payload systems, calibration, joystick mode, power management, sensors, logging, actuators)
  - Maciej Stachura: ~30 open tasks (VTOL/control systems focus; transition control, landing, wind alignment, navigation, motor control, estimator, fault analysis)
  - Ben Busby: ~8 open tasks (tablet/UI focus; scripting, landing plan sync, XML configuration, log parsing, communications packets)
- **Notable patterns**: 
  - Heavy focus on VTOL systems (transitions, landing, motor control, climbout, wind alignment)
  - Flight-critical issues concentrated in joystick mode, landing detection, flight termination, and surface actuation
  - Multi-aircraft hardware support (S0, S1, S2, commercial variants, 2030/2040/2050/3000)
  - No due dates assigned to any open tasks—priority sequencing relies on task naming and notes
  - Custom field priority designation: Low (despite flight-critical open items)

## Recent Activity
Latest team feedback (May 2026) from Daniel Prendergast relates to fleet maintenance process integration (post-flight issue capture form), not SwiftCore 3.3 development status. No corrections override Asana task list data.

Recent task completion activity (Feb 2026 timestamps) shows intensive VTOL and control system development:
- Landing system refinements (laser-based flare, altitude management, orbit sizing)
- Motor and transition control improvements (rotation smoothing, pitch command tuning, motor bump fixes)
- Wind estimation with real-time MHP integration
- Climbout automation (timeout handling, time generation from height)
- Joystick control improvements and abort functionality
- Controller tuning across multiple aircraft models (S0, S1-22, S10020)
- Parameter management and initialization fixes
- RTK, GNSS, and sensor startup improvements

## Notes & Context

**Core Development Focus:**
- **VTOL Integration**: Major effort on VTOL aircraft support with multi-phase transitions, landing systems, wind alignment, and motor feedback during critical phases
- **Hardware Expansion**: Supporting legacy (S0, S1, S2) and next-gen hardware (2030, 2040, 2050, 3000) plus commercial variants
- **Advanced Capabilities**: Scripting engine, payload control via serial interface, dual pitot systems, real-time wind estimation, tablet app integration
- **Multi-Mode Operations**: Fixed-wing, multirotor, tailsitter support with mode switching and abort logic

**Flight-Critical Open Issues Requiring Priority Resolution:**
- **Joystick Mode**: Takeover failures (S2 on 05-30-24, FW0002 on 2024-03-08), abort problems, activation in prohibited modes (climbout), lost comms behavior, handset control validation
- **Landing**: Detection failures (S10011 on 2024-01-19), wind alignment (vertical vs spiral switching, landing direction maintenance), spiral vs vertical switching, orbit removal, timing, multirotor GPS/pressure loss fallback
- **Flight Termination**: Bug on S10011 (2024-03-08), fault tree analysis needed for policy on joystick allowance (GPS loss consideration), wind alignment, lost comms behavior, open-loop control for GPS/pressure loss
- **Surface Actuation & Control**: Surfaces not moving despite ACK, calibration mode limits preventing full range, initial XML deflections on load, PWM channel configuration (S00001), kill switch non-functionality, roll/pitch command limits, trim functionality for VTOL, manual takeover bugs (S2)
- **Sensors & Power**: BAD_IAS flag missing for VTOL, pressure sensor backup alerts, battery detection failures (ERROR_NO_BATTERY on E2), sensor initialization timing validation, dual pitot setup integration pending
- **Navigation & Path Planning**: Dubins path recomputation on turnrate-to-waypoint transitions, nav overlap issues causing suboptimal paths, non-fly-through waypoints too close generating bad paths, glide path angle optimization needed (S0-VTOL)

**Scripting & Payload Systems:**
- Scripting non-functional for most VTOL commands and fixed-wing climb/descent
- Landing plan switching not updating execution (ACK timing issue identified)
- Payload door premature opening (during pre-flight mapping setup), position hold issues in calibrate mode
- Deployment tube should not send turn-off if flap never closed
- Payload should not turn off on lost comms unless in flying mode
- System-wide feature for adding system time to all packets needed

**Data Quality & Configuration:**
- Duplicate XML entries for safe height
- Rate limiter code removal needed (legacy FilterParameters_t fields: roll_cmd_rate, pitch_cmd_rate, ias_cmd_rate, vx_dot_cmd_rate)
- Nav overlap issues causing suboptimal paths
- Log parsing timing issues with waypoint values (3rd S2-9 flight on 11/06)
- Trigger packet logging gaps
- Rolling command logging excessive (should log only on change)
- Scale factor addition to comm packets under investigation

**System Integration:**
- MHP integration into CAN bus pending
- Dual pitot setup integration with drained version pending
- USB bootloader flag update for 2050 hardware
- Constant controller rate verification for quad platforms (controller → AP → actuator board)
- ECAMS tree implementation verification needed
- Sensor startup timing and value validation before use/logging

**TECS & Control System Issues:**
- gamma_c uses small angle assumptions while gamma_a does not (inconsistency)
- TECSalt_Land possibly unused (candidate for deletion)
- Flight timer appears to be engine-not-too-low timer (may conflict with VTOL modes)
- Pitch/roll command limits need validation
- Front motors throttle up after landed mode on S1-22 ground tests

The 375 completed tasks versus 78 open indicates significant progress on feature development, but the nature and concentration of open issues (particularly around flight-critical systems like landing, termination, joystick control, and surface actuation) combined with complete absence of due dates suggests the codebase requires prioritized stability hardening, safety validation, and systematic testing before production releases. The low priority custom field designation appears inconsistent with the severity of open flight-critical items.