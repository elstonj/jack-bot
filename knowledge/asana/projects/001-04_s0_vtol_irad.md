_Asana snapshot as of 2026-11-11: 42 open tasks, 3 completed (last 90 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Client/Customer:** Multiple (NOAA, ERAU, Barbados mentioned in delivery milestones); appears to be internal R&D platform with external customers
- **Dollar Value:** Not specified in custom fields
- **Timeline:** 
  - Current phase: Hover testing (ready to begin week of Feb 26, 2024)
  - Near-term: Avionics integration and testing (Dec 2026)
  - Customer deliveries: ERAU (Apr 2025), Barbados (Jun 2025)
  - Extended testing: Through Jun 2026
- **Status:** Active – low priority but progressing. Recent completions (avionics ordering, DFM checks, fit verification as of Nov 4, 2026). Status update dated Feb 21, 2024 indicates "should be able to begin hover testing next week."
- **Team Members:** Alex Lomis (owner/lead), Jack Elston, Sam Hild, Ali Sulehria, Spencer Hoehl, Ethan Domagala, Josh Waldman
- **Risk Signals:** 
  - One task ("Identify motor imbalance bug") was due Feb 20, 2026 and remains open
  - "Build up another S0-VTOL" due Mar 4, 2026 and open
  - Many unassigned tasks across bench/flight testing milestones with no due dates
  - Wide date scatter (some tasks due 2025, others 2027) suggests phased or contingent work

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Est. Hours | Status |
|-----------|-------|----------|-----------|--------|
| Build up new avionics/bench test | Jack Elston | Dec 4, 2026 | 40h | Open |
| Integrate new avionics into platform | Alex Lomis | Dec 11, 2026 | 32h | Open |
| 50 transition flights | Spencer Hoehl | Dec 18, 2026 | 40h | Open |
| Pack and Deliver | Ethan Domagala | Dec 21, 2026 | 8h | Open |
| Build guides/work instructions | Josh Waldman | Jan 1, 2027 | – | Open |
| Visual Observation Bench Test | Alex Lomis | Apr 30, 2026 | – | Open (unassigned subtasks) |
| Instrumented Bench Test | Alex Lomis | May 15, 2026 | – | Open (unassigned subtasks) |
| Instrumented Flight Test | Alex Lomis | Jun 5, 2026 | – | Open (unassigned subtasks) |
| ERAU S0 Delivery | – | Apr 30, 2025 | – | Open (unassigned) |
| Barbados S0 Delivery (1) | – | Jun 13, 2025 | – | Open (unassigned) |
| NOAA (2) | Alex Lomis | No due date | – | Open |

## Task Summary

- **Total:** 45 tasks (42 open, 3 completed)
- **Completion Rate:** 6.7% (very early stage)
- **By Assignee:**
  - **Alex Lomis:** 23 tasks (design decisions, integration, testing oversight) – highest volume
  - **Unassigned:** 12 tasks (primarily bench/flight testing subtasks)
  - **Jack Elston:** 3 tasks (avionics procurement, DFM, remote ID)
  - **Ali Sulehria:** 2 tasks (electronics & test bench work, final QC)
  - **Spencer Hoehl:** 1 task (transition flights)
  - **Ethan Domagala:** 1 task (pack & deliver)
  - **Josh Waldman:** 1 task (guides/work instructions)
  - **Sam Hild:** 1 task (electronics bench test)
- **Key Pattern:** Alex Lomis owns most design/engineering decisions; many test and integration tasks remain unassigned, suggesting contingent assignment after earlier milestones complete

## Recent Activity

**As of Feb 21, 2024:**
- Status update indicates readiness to begin hover testing the following week
- Recently completed (Nov 4, 2026):
  - Ordered S0-VTOL avionics stacks and electronics
  - Finished DFM (Design for Manufacturing) checks
  - Verified new avionics stack fits in OnShape design
- Next phase: Proceed to avionics bench testing (Sam Hild, Ali Sulehria) and integration (Alex Lomis)

## Notes & Context

- **Project Structure:** Highly iterative hardware development with multiple testing phases (bench → instrumented bench → instrumented flight → customer delivery)
- **Custom Field Priority:** Marked as "Low" – may indicate this is exploratory IRAD work rather than immediate revenue-critical
- **Assembly & Manufacturability Focus:** Significant effort on design refinements (motor wire color-coding, drill jigs, aileron mounts, battery design, wiring/harness standardization, autopilot mounting). Suggests S0 is moving from prototype to more producible design
- **Unassigned Test Work:** Large cluster of unassigned subtasks across Visual Observation, Instrumented Bench, and Instrumented Flight milestones (parachute recovery, sensor integration, firmware logging for Teensy). These will likely be assigned as earlier milestones complete
- **Customer Commitments:** ERAU and Barbados deliveries due 2025; NOAA units unscheduled (potentially unfunded or contingent)
- **Long Tail:** Many design exploration tasks with no due dates (radar vs. laser, IR surface temperature necessity, dual GPS accommodation, ESC telemetry reading method) indicate active iteration and feature evaluation