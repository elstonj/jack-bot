_Asana snapshot as of 2026-11-20: 42 open tasks, 3 completed (last 90 days)._

# S0 VTOL IRAD

## Overview
- **Project Type**: Internal R&D (IRAD) — S0 VTOL development platform
- **Owner**: Alex Lomis
- **Team**: Whole BST team (electrical, firmware, mechanical, systems engineering, test)
- **Status**: Active — currently in avionics upgrade and testing phase
- **Priority**: Low (per custom field)
- **Key Context**: As of Feb 21, 2024, team was preparing to begin hover testing. Project appears to be in a phased rollout with multiple delivery milestones to customers (Barbados, ERAU, NOAA).

---

## Key Deliverables & Milestones

**Near-term (Q4 2026):**
- **Build up new avionics/bench test** | Due Dec 4, 2026 | 16h electrical + 24h test engineer hours
- **Integrate new avionics into platform** | Due Dec 11, 2026 | Includes fuse mod (Dec 8), power-up & function verification (Dec 9), final QC (Dec 11)
- **50 transition flights** | Due Dec 18, 2026 | 40h systems engineer
- **Pack and Deliver** | Due Dec 21, 2026 | 8h technician

**Medium-term (Q1 2027 & beyond):**
- **Build guides/work instructions** | Due Jan 1, 2027 | Assigned to Josh Waldman
- **Barbados S0 Delivery (1)** | Due Jun 13, 2025 ⚠️ *Note: This date is in the past relative to other tasks; likely stale or multi-unit program*
- **ERAU S0 Delivery** | Due Apr 30, 2025 ⚠️ *Past date*
- **NOAA (2)** | No due date | Assigned Alex Lomis

**Later-stage validation (Q2–Q3 2026):**
- **Visual Observation Bench Test** | Due Apr 30, 2026 | Sinusoidal and crashed-flight-replay tests (unassigned subtasks)
- **Instrumented Bench Test** | Due May 15, 2026 | eRPM sensor selection, Teensy logging firmware, 1hr+ sinusoidal test (unassigned subtasks)
- **Instrumented Flight Test** | Due Jun 5, 2026 | Parachute integration, hover & full flight testing with instrumentation (unassigned subtasks)
- **Autopilot-Based Bench Test Rig for Future Testing** | No due date | Long-term automation infrastructure

---

## Task Summary

**Overall**:
- **Total open tasks**: 42
- **Completed tasks**: 3 (as of Nov 4, 2026)
  - Order S0-VTOL avionics stacks (completed Nov 4)
  - Finish DFM checks (completed Nov 4)
  - Ensure new avionics stack physically fits (completed Nov 4)

**By assignee (open tasks)**:
- **Alex Lomis**: ~26 tasks (design reviews, component design, bench test milestones, autopilot/sonde mounting, wiring/assembly improvements, testing fixes)
- **Jack Elston**: 3 tasks (avionics bench test milestone, design updates, Remote ID solution)
- **Sam Hild**: 1 task (electronics engineer bench test, Dec 4)
- **Ali Sulehria**: 2 tasks (test engineer bench test, final QC)
- **Spencer Hoehl**: 1 task (50 transition flights, Dec 18)
- **Ethan Domagala**: 1 task (pack & deliver, Dec 21)
- **Josh Waldman**: 1 task (build guides, Jan 1, 2027)
- **Unassigned**: 7 tasks (ISR payload, visual observation subtasks, instrumented bench/flight subtasks, motor imbalance bug, another S0 build, Barbados & ERAU deliveries)

**Completion rate**: Very low (3/45 = ~7%). Most work is ahead-of-schedule or in design/planning phases.

---

## Recent Activity

**Completed (Nov 4, 2026)**:
- Avionics procurement finalized and design fit confirmed — clears path for bench test and integration work in December.

**In Flight (Approaching Dec 4–21)**:
- Avionics bench test tasks (electrical & test engineer focus) starting immediately.
- Integration subtasks (fuse mod, power-up, QC) cascading through mid-December.
- 50 transition flights task assigned to Spencer Hoehl due Dec 18.
- Delivery/packing task due Dec 21.

**Notable Gaps**:
- Multiple unassigned subtasks in later-stage testing (instrumented bench, instrumented flight, autopilot bench rig, Visual Observation).
- Two customer delivery milestones (Barbados, ERAU) have past due dates (Jun 2025, Apr 2025) — likely stale or external coordination needed.
- Several design tasks have no due dates and may be deprioritized (battery design, nose material, radar vs. laser, Remote ID, ESC telemetry, assembly improvements).

---

## Notes & Context

1. **Restructuring in progress**: Per Maciej's note (Oct 27, 2026), BST was planning to restructure Asana to separate long-term milestones from weekly execution tracked on a physical Kanban board. This project may benefit from that clarification.

2. **Design-heavy backlog**: Many open tasks are exploratory design work (motor imbalance debugging, component layout optimization, wire routing improvements, sensor trade-offs). These are not critical-path blockers but reflect engineering best practices for the platform.

3. **Customer delivery program**: This is not a one-off project. References to Barbados, ERAU, and NOAA suggest S0 VTOL is a multi-unit platform with ongoing customer integrations. Stale due dates on those deliveries warrant clarification.

4. **Testing strategy is multi-phase**: Visual → Instrumented Bench → Instrumented Flight, with parachute safety integration. This is methodical and appropriate for a flying platform.

5. **Low priority flag**: Despite having near-term December milestones, the project is flagged as "Low" priority. May reflect that it is IRAD (internal R&D) rather than a customer contract, or that the Dec work is on track and not a risk.

---

## Risk Signals

- ⚠️ **Unassigned critical subtasks**: Instrumented bench & flight test subtasks (due May–Jun 2026) are unassigned; assignment should happen soon to avoid schedule slip.
- ⚠️ **Past-due customer deliveries**: Barbados (Jun 2025) and ERAU (Apr 2025) delivery milestones are overdue relative to task list date. Clarify if these are completed, externally managed, or truly delayed.
- ⚠️ **Dec 2026 crunch**: Four milestones in 3 weeks (Dec 4, 11, 18, 21) with limited apparent parallelization; monitor for dependencies and resource conflicts.
- ✓ **Avionics procurement complete**: Recent completion of ordering and fit verification removes a major blocking dependency.