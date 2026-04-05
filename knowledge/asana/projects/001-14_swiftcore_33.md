# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: No specific start/end dates; active development branch
- **Status**: Active development (yellow status as of Nov 28, 2023, with overdue milestones)
- **Team members**: Jack Elston (owner), Maciej Stachura, Ben Busby, whole BST team
- **Risk signals**: Multiple overdue milestones and tasks as of Nov 28, 2023; 78 open tasks vs 375 completed suggests heavy ongoing development load

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
  - Jack Elston: ~40 open tasks (majority of workload)
  - Maciej Stachura: ~30 open tasks (VTOL/control systems focus)
  - Ben Busby: ~8 open tasks (tablet/UI focus)
- **Notable patterns**: Heavy focus on VTOL systems, scripting capabilities, and hardware support across multiple aircraft models (S0, S1, S2, etc.)

## Recent Activity
Recent completions show active VTOL development with tasks completed through February 2026 (likely data error - should be 2024):
- RSS421 sensor integration and nan handling
- Landing system improvements including laser-based flare for VTOL
- Parameter save/load functionality fixes
- VTOL transition and control refinements including motor rotation smoothing
- Wind estimation improvements with real-time MHP integration
- Climbout timing automation and timeout handling
- Joystick control improvements and abort functionality

## Notes & Context
This is the development branch for SwiftCore 3.3, focusing on:
- **VTOL Integration**: Major effort on VTOL aircraft support with transition control, landing systems, and flight modes
- **Hardware Support**: Expanding compatibility across aircraft models (S0, S1, S2, commercial variants, 2030/2040/2050/3000 hardware)
- **Advanced Features**: Scripting, payload control, dual pitot systems, wind estimation, joystick controls
- **Quality Issues**: Multiple flight-critical bugs being tracked including:
  - Joystick mode issues and takeover problems
  - Landing detection failures
  - Flight terminate problems
  - Manual takeover bugs on S2
  - Actuator communication issues
- **Custom Field Usage**: Priority marked as "Low" despite active development status

The project represents core autopilot software development with significant technical complexity around VTOL operations and multi-platform hardware support. The high volume of completed tasks (375) versus open tasks (78) indicates substantial progress, but the concentration of open issues around flight-critical systems suggests ongoing stability and safety concerns that need resolution before release.