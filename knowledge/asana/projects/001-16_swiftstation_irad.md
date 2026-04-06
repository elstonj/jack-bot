# [001-16] SwiftStation IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Internal Research and Development)
- **Dollar value**: Not specified
- **Timeline**: Long-term project with tasks spanning 2024-2026; wiring phase in progress (Feb 14, 2025)
- **Status**: Active (yellow status) — bench test setup in progress, targeting completion by end of week
- **Team members involved**: Sam Hild (project owner, primary developer), Jack Elston, Alex Lomis, Ethan Domagala, Nate Straus
- **Priority**: Low
- **Risk signals**: 
  - Multiple critical tasks assigned to Sam Hild due May-October 2026 (concentration risk)
  - RF interference issues flagged as critical blocker for RTK module
  - Hot-plug device assignment due March 27, 2026 approaching
  - Starlink compatibility unassigned and unfunded

## Key Deliverables & Milestones
- **Field Test** (completed 2024-08-07) — GNSS and radio validation complete
- **Bench Top Test** (completed 2024-05-23) — Hardware validation milestone
- **Bench Test Phase 2** (in progress, due end of week Feb 21) — Verify wiring, power, and logic level requirements
- **New GCS Housing** (in progress, Ethan Domagala, no due date) — Critical for RF interference mitigation
- **Fix Hot-plug device Assignment** (due 2026-03-27, Sam Hild)
- **Add RTK/Power Board Communications to gcsDaemon** (due 2026-05-31, Sam Hild)
- **Fix RF Interference Issues** (due 2026-05-31, Sam Hild) — Priority order: P900 > WiFi > Cell Module > Switching Circuitry
- **Cell Module Driver** (due 2026-10-30, Sam Hild)
- **Battery Integration Code Review** (due 2026-04-24, Jack Elston)

## Task Summary
- **Total tasks**: 32 (8 open, 24 completed) — 75% completion rate
- **Tasks by assignee**:
  - **Sam Hild**: 6 open tasks (hot-plug assignment, RTK features, power board comms, RF interference fix, cell module driver) + majority of completed work — primary development bottleneck
  - **Jack Elston**: 1 open task (battery integration code review)
  - **Ethan Domagala**: 1 open task (New GCS Housing, no due date set)
  - **Unassigned**: 1 open task (Starlink compatibility)
- **Notable patterns**: Sam Hild carries disproportionate load; hardware/software integration focus with heavy emphasis on RF issues and daemon control logic; Alex Lomis completed most CAD and hardware setup work; strong collaboration between firmware and hardware teams

## Recent Activity
- **Current focus** (Feb 14 status): Wiring work in progress; bench test setup targeting end of week with verification of wiring, power, and logic level requirements
- **Recently completed** (Dec 2025-Feb 2025):
  - GNSS boards procurement (Dec 2025)
  - Modular GCS housing for interference testing (Sep 2025)
  - Moving base RTK functionality (May 2025)
  - GCS firmware GPS issue fix (Mar 2025)
  - Antenna repair (Feb 2025)
- **Approaching deadlines**: Hot-plug device assignment (March 27, 2026); RTK/Power features and RF fixes (May 31, 2026)

## Notes & Context
- **RF Interference Critical Priority Chain** (mitigation for new GCS housing layout):
  1. P900 (highest)
  2. WiFi
  3. Cell Module
  4. Switching Circuitry
- **Project scope**: Ground control station (GCS) with RTK GPS, cellular connectivity, 900MHz P900 radio, weather station integration, power management, and potential Starlink compatibility
- **Architecture**: gcsDaemon controls RTK features and power board communications; modular housing approach for RF testing
- **Completed infrastructure**: Power board hardware/software (v1.2), battery management, moving base RTK, wiring schematics, cellular plan setup
- **Team dependency**: Sam Hild handles majority of firmware/driver development and integration work; needs support or delegation to reduce 2026 bottleneck
- **Next immediate task**: Bench test completion verification by ~Feb 21, 2025