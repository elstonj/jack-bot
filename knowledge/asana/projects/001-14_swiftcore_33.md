# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: Active development (yellow status as of Nov 28, 2023, with overdue milestones and 78 open tasks)
- **Team members**: Jack Elston (owner), Maciej Stachura, Ben Busby, whole BST team
- **Risk signals**: Multiple overdue milestones and tasks as of Nov 28, 2023; 78 open tasks indicate substantial ongoing work; significant concentration of flight-critical bugs (joystick control, landing detection, flight termination) suggest safety/stability concerns requiring resolution before release

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
- **Total tasks**: 78 open, 375 completed (83% completion rate)
- **Tasks by assignee**:
  - Jack Elston: ~40 open tasks (majority workload; focus on surface control, payload systems, calibration, joystick mode, power management, sensors, logging)
  - Maciej Stachura: ~30 open tasks (VTOL/control systems focus; transition control, landing, wind alignment, navigation, motor control)
  - Ben Busby: ~8 open tasks (tablet/UI focus; scripting, landing plan sync, XML configuration, log parsing)
- **Notable patterns**: 
  - Heavy focus on VTOL systems (transitions, landing, motor control, climbout)
  - Flight-critical issues concentrated in joystick mode, landing detection, and flight termination
  - Multi-aircraft hardware support (S0, S1, S2, commercial variants, 2030/2040/2050/3000)
  - Low priority custom field designation despite active development and safety-critical open items

## Recent Activity
Recent completions (Feb 2026 dates likely represent data timestamps) show intensive VTOL and control system development:
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
- **Joystick Mode**: Takeover failures, abort problems, activation in prohibited modes (climbout), lost comms behavior
- **Landing**: Detection failures, wind alignment, spiral vs vertical switching, orbit removal, timing
- **Flight Termination**: Bug on S10011 (2024-03-08), fault tree analysis needed, wind alignment, lost comms behavior
- **Control Systems**: Pitch/roll command limits, trim functionality for VTOL, manual takeover bugs (S2), turn rate computation
- **Actuators**: Surfaces not moving despite ACK, calibration mode limits, initial XML deflections, PWM channel configuration
- **Sensors**: BAD_IAS flag missing for VTOL, pressure sensor backup alerts, battery detection failures, sensor initialization timing

**Scripting & Payload Systems:**
- Scripting non-functional for most VTOL commands and fixed-wing climb/descent
- Landing plan switching not updating execution
- Payload door premature opening, position hold issues
- System-wide feature for adding system time to all packets needed

**Data Quality & Configuration:**
- Duplicate XML entries for safe height
- Rate limiter removal needed (legacy code)
- Nav overlap issues causing suboptimal paths
- Log parsing timing issues with waypoint values

**System Integration:**
- MHP integration into CAN bus pending
- Dual pitot setup integration needed
- USB bootloader flag update for 2050 hardware
- Constant controller rate verification for quad platforms

The 375 completed tasks versus 78 open indicates significant progress on feature development, but the nature and concentration of open issues (particularly around flight-critical systems like landing, termination, and joystick control) suggest the codebase requires stability hardening and safety validation before production releases.