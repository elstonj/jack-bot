# [001-04] S0 VTOL IRAD

## Overview
- **Owner:** Alex Lomis
- **Team:** BST (Whole Team)
- **Timeline:** Active; milestones span through June 2026
  - Visual Observation Bench Test: Due 2026-04-30
  - Instrumented Bench Test: Due 2026-05-15
  - Instrumented Flight Test: Due 2026-06-05
- **Status:** Active — high-priority IRAD; ready to move to hover testing phase (as of Feb 21, 2024)
- **Priority:** High

## Key Deliverables & Milestones

1. **Visual Observation Bench Test** (Due 2026-04-30)
   - Sinusoidal command test with visual observation
   - Crashed flight replay with visual observation
   - Lead: Alex Lomis

2. **Determine Components of Interest and Logging Tools** (Due 2026-04-30)
   - Motor RPM instrumentation (ESC telemetry, eRPM sensors, optical tachometer)
   - 9-Channel PWM logging (L Ail, L Piv, L Mot, L RV, R Ail, R Piv, R Mot, R RV, T Mot)
   - Servo True Position (6 servos with rotary encoders)
   - ESC Power Data (current, voltage from telemetry)
   - Lead: Alex Lomis

3. **Instrumented Bench Test** (Due 2026-05-15)
   - Select and validate eRPM sensors and logging device
   - Develop firmware (Teensy) for PWM/eRPM logging to SD card
   - Install and validate on bench S0 VTOL
   - Complete long sinusoidal test (1hr+)
   - Log analysis and discrepancy checking
   - Lead: Alex Lomis

4. **Instrumented Flight Test** (Due 2026-06-05)
   - Integrate instrumentation into flight-capable S0
   - Bench testing with flight platform
   - Parachute system design and integration (recovery handset)
   - Repeated hover testing with instrumented system
   - Full flight test with instrumentation and parachute
   - Lead: Alex Lomis

## Task Summary
- **Total tasks:** 4 open, 0 completed (as of latest data)
- **Task breakdown:**
  - Visual Observation Bench Test: 2 subtasks (unassigned)
  - Components of Interest & Logging Tools: 4 subtasks (unassigned)
  - Instrumented Bench Test: 6 subtasks (unassigned)
  - Instrumented Flight Test: 8 subtasks (unassigned)
- **All 4 milestones assigned to Alex Lomis; all subtasks unassigned**

## Recent Activity
- **Feb 21, 2024:** Status update — two tasks completed (bench test sessions); **ready to begin hover testing next week**
- All milestone due dates are 2026; current phase is transitioning from visual observation to instrumented testing

## Notes & Context
- **Detailed component research included:** Motor RPM sensors (Hobbywing, optical tachometer), servo shaft adapters/couplers, PWM-to-UART logging
- **9-channel instrumentation scope:** Motors, ailerons, pivoters, rudder vanes, tail motor
- **Recovery system planned:** Parachute with standalone handset trigger for safe S0 VTOL recovery
- **Testing progression:** Visual → Instrumented bench → Instrumented flight (progressive validation of control and telemetry systems)
- **No budget or dollar value** specified in task data