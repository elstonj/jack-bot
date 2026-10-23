_Asana snapshot as of 2026-10-23: 37 open tasks, 2 completed (last 365 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Client/Customer:** Internal R&D (IRAD — Independent Research and Development)
- **Team Lead:** Alex Lomis (primary owner); Jack Elston (secondary)
- **Timeline:** 
  - Project status update as of Feb 21, 2024: "Should be able to begin hover testing next week"
  - Key milestone dates range from Apr 2025 – Jun 2026
  - **Note:** Asana data appears dated (Feb 2024 status update) but milestone due dates extend to 2026; exact current status unclear from task list alone
- **Status:** [YELLOW] Active development with testing phases planned; however, 37 open tasks and 2 completed suggests early/mid-stage execution
- **Priority:** High (custom field)
- **Risk Signal:** Most tasks unassigned; many lack due dates; "Identify motor imbalance bug" was due 2026-02-20 (now overdue)

## Key Deliverables & Milestones

| Milestone | Lead | Due Date | Status | Notes |
|-----------|------|----------|--------|-------|
| **Visual Observation Bench Test** | Alex Lomis | 2026-04-30 | Open (2 subtasks) | Sinusoidal command & crash replay testing |
| **Instrumented Bench Test** | Alex Lomis | 2026-05-15 | Open (6 subtasks) | eRPM sensors, Teensy firmware, long-duration logging |
| **Instrumented Flight Test** | Alex Lomis | 2026-06-05 | Open (8 subtasks) | Flight integration, parachute system, repeated hover/flight tests |
| **Autopilot-Based Bench Test Rig** | Alex Lomis | No due date | Open (2 subtasks) | Automation for endurance testing; sensor investigation |
| **ERAU S0 Delivery** | Unassigned | 2025-04-30 | Open | Customer delivery |
| **Barbados S0 Delivery (1)** | Unassigned | 2025-06-13 | Open | Customer delivery |
| **NOAA (2)** | Alex Lomis | No due date | Open | Customer delivery; scope undefined |
| **Janet (1)** | Alex Lomis | No due date | **COMPLETED** (2026-07-24) | Archived milestone |

## Task Summary

- **Total Tasks:** 39 (37 open, 2 completed)
- **Assignees:**
  - **Alex Lomis:** 19 tasks assigned (mostly open, hardware/design/testing work)
  - **Jack Elston:** 2 tasks assigned (design updates, Remote ID)
  - **Unassigned:** 18 tasks (including both customer deliveries, ISR Payload, and several critical bench tests)
- **Completion Rate:** ~5% (2/39 completed)
- **Notable Pattern:** Heavy concentration of hardware design, integration, and testing tasks on Alex Lomis; critical testing phases (Visual Observation, Instrumented Bench/Flight) lack assigned owners despite being on critical path

## Recent Activity

- **Last Status Update:** Feb 21, 2024 — "Should be able to begin hover testing next week"
- **Completed:** 
  - Janet (1) delivery — completed 2026-07-24
  - "Determine Components of Interest and Logging Tools" milestone — completed 2026-05-04 (with open subtasks for Motor RPM, PWM, Servo Position, ESC Power Data)
- **Approaching/Overdue:**
  - "Identify motor imbalance bug" — **due 2026-02-20 (overdue)**
  - "Build up another S0-VTOL" — due 2026-03-04
  - Visual Observation Bench Test — due 2026-04-30
  - ERAU S0 Delivery — due 2025-04-30 (may be overdue; status unclear)

## Notes & Context

### Process Gap Identified (Team Feedback)
**[2026-10-19–20] From Daniel Prendergast:**  
"Currently we don't have a well-defined process for transitioning proposed system builds/deliveries into the production pipeline."  
Example: LMUK project requires 2× S0-AD with Magnetometer, 2× S0-AD with Camera, 2× S0-AD variants — but no clear pipeline for moving from proposal to production.

**Related:** [2026-10-20] Production tracking gap noted — no holistic spreadsheet for planned production exists. The **S0 Production QC Website** (built by Jack) is the closest resource, currently tracking S0-AD orders only with an "Orders" tab dashboard and add-new-order functionality. Potential to extend this site for broader production visibility.

### Technical Work Streams
1. **Testing & Instrumentation** (Critical Path for next ~12 months)
   - Visual observation bench → instrumented bench → instrumented flight → repeated validation
   - Requires eRPM sensors, Teensy logging firmware, parachute integration
   
2. **Hardware Design & Manufacturing Issues**
   - Motor imbalance; motor boom drilling; aileron control horn mount
   - Battery packaging (4s2p consolidation vs. 2×2 design)
   - Non-yellowing nose compound; autopilot/sensor mounting
   - Wiring complexity (ESC telemetry, AP power, dual GPS consideration)
   
3. **Customer Deliveries**
   - ERAU (due 2025-04-30) — status unclear
   - Barbados (1 unit, due 2025-06-13)
   - NOAA (2 units) — no due date set; scope not defined in Asana

### Gaps & Risks
- **Unassigned critical tasks:** Both customer deliveries unassigned; Visual Observation and Instrumented Flight tests lack assigned owners despite being on critical path
- **No due dates:** 16 open tasks have no due date, including ISR Payload, autopilot mounting standardization, assembly guides, and Remote ID solutions
- **Motor imbalance bug:** Overdue by 8 months; unclear if resolved externally or blocked
- **Data staleness:** Last status update from Feb 2024; milestone dates 2025–2026 suggest Asana may not reflect current execution state

---

**Recommendation for AI Assistant:** Treat this project as mid-stage R&D with documented process gaps around production transition and no single source of truth for current status. Prioritize clarification of ERAU/Barbados delivery status and assignment of unowned critical-path tasks before forecasting delivery dates.