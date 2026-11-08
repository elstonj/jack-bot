_Asana snapshot as of 2026-11-08: 58 open tasks, 10 completed (last 90 days)._

# SOCOM Pope

## Overview

- **Client/Customer:** SOCOM
- **Project Lead:** Dan Prendergast
- **Priority:** High
- **Status:** **Active — undergoing Asana restructuring.** Per Daniel Prendergast (2026-11-02), the SOCOM Asana project is being refactored; "Project and stickies will be ready by Monday morning." Per Maciej (2026-11-04 & 2026-11-05), SOCOM has significant task volume on the Kanban board and resource constraints; tasks may need to shift to following week or require additional resource allocation.
- **Timeline:** 
  - Near-term milestones: Nov 6–13, 2026 (camera selection, PCLT test launch prep)
  - PCLT Flight Test: March 5, 2027
  - Final CLIN closeouts: May 28–31, 2027
- **Team Members:** Dan Prendergast (owner), Josh Fromm, Ethan Domagala, Alex Lomis, Ben Busby, Jack Elston, Maciej Stachura

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| All-variants Common Camera Selection | Dan Prendergast | 2026-11-13 | Open (camera tests & selection in progress) |
| PCLT Test Launch at SOCOM Facility | Dan Prendergast | 2026-11-13 | Open (prep work in flight) |
| Design Changes for PCLT Flight Test | Josh Fromm | 2026-12-11 | Open (awaiting site visit answers) |
| PCLT Flight Test | Dan Prendergast | 2027-03-05 | Open |
| CLIN 1 Closeout | Dan Prendergast | 2027-03-12 | Open |
| Comm Protocol Design & Implementation (CLIN 3) | Jack Elston | 2026-11-24 | Open |
| Mechanical and Electrical Design Updates (CLIN 3) | Josh Fromm | 2026-11-25 | Open |
| Software for Payload Integration and Automation (CLIN 3) | Ben Busby | 2026-12-03 | Open |
| Build Prototype S0 METAR | Ethan Domagala | 2026-12-22 | Open |
| Precipitation/Cloud/Visibility Sensor Trade Studies (CLIN 2) | Maciej Stachura | 2027-01-29 | Open (3 parallel studies) |
| ATR Selection and Integration (CLIN 5) | Dan Prendergast | 2027-01-19 | Open (awaiting model details from customer) |
| CLIN 6 Complete | Unassigned | 2027-05-31 | Open |

## Task Summary

- **Total Tasks:** 58 open, 10 completed (14.6% completion rate)
- **Tasks by Assignee:**
  - Dan Prendergast: 13 open (milestone owner for multiple CLINs; heavy lifting on requirements, reviews, and closeouts)
  - Ethan Domagala: 8 open (all prototype build and flight test phases)
  - Josh Fromm: 5 open (mechanical/electrical design across multiple CLINs)
  - Alex Lomis: 3 open (camera tests, datalink selection, comm protocol)
  - Ben Busby: 3 open (software integration across multiple CLINs)
  - Maciej Stachura: 3 open (sensor trade studies, software automation)
  - Jack Elston: 1 open (CLIN 3 comm protocol)
  - Unassigned: 19 open (risk — multiple milestones and blocking tasks lack owners)

- **Notable Patterns:**
  - **Six CLINs tracked in parallel** (PCLT, METAR, Auto-METAR, EO/IR R&R, EO/IR Real-time ATR, EO/IR FMV). Each CLIN follows similar phases: design → prototype build → testing → closeout.
  - **Heavy reliance on Dan Prendergast** for milestone closeouts and customer coordination.
  - **Unassigned blocking tasks:** Site visit follow-ups (gap measurements, separation verification) and hardware selections (radio, processing) lack owners.
  - **Custom field usage:** Organization/Customer and Priority tracked; dollar amounts not visible in task list.

## Recent Activity

- **Completed (Nov 2–6):**
  - Daytime camera tests (Alex Lomis) — Nov 6
  - Camera test plan write-ups (Alex Lomis) — Nov 6
  - Bench camera start/stop testing (Alex Lomis) — Nov 6
  - Requirements review held (Dan Prendergast) — Nov 2
  - Monthly customer PM meeting setup (Dan Prendergast) — Nov 5
  - Site visit & instrumented S0 launch (Josh Fromm) — Oct 30

- **Approaching Deadlines (Next 2 weeks):**
  - **Software post-processing of video** (Dan Prendergast) — Nov 6 (likely due today or overdue)
  - **Draft SOW and Requirements for CoVar** (Dan Prendergast) — Nov 6 (likely due today or overdue)
  - **Select cameras** (Dan Prendergast) — Nov 6 (likely due today or overdue)
  - **Nighttime camera tests** (Alex Lomis) — Nov 10
  - **Document camera trade study** (Unassigned) — Nov 11
  - **Draft report for test PCLT launch results** (Dan Prendergast) — Nov 13
  - **All-variants Common Camera Selection** [MILESTONE] (Dan Prendergast) — Nov 13

- **Resource Constraint Signal:** Per Maciej (Nov 4–5), SOCOM tasks remain on Kanban board; team is evaluating whether to defer tasks or secure additional resources. This aligns with Daniel's note that Asana refactoring is underway to improve visibility and capacity planning.

## Notes & Context

1. **Asana Restructuring in Progress:** Per Daniel Prendergast (Nov 2) and Maciej (Oct 27), the SOCOM project Asana structure is being refactored to implement a two-level planning model: Asana tracks long-term milestones and weekly tasks; the physical Kanban board manages weekly execution. This may explain why some Asana tasks lack assignment or due dates — the project is mid-transition.

2. **Site Visit Outcomes:** Oct 30 site visit (Josh Fromm + team) at SOCOM facility generated critical design questions:
   - Can PCLT tube be loaded inflight, or only on ground?
   - Is S0 power switch accessible when inside tube?
   - Safe separation requirements for 16 lb S0
   - PCLT installation angle in host aircraft
   - Gap between aircraft skin and PCLT tube exit rim
   - Payload methods to sense clear of tube
   
   These answers drive "Design Changes for PCLT Flight Test" (Josh Fromm, due Dec 11). Several site visit follow-up tasks are **Unassigned**.

3. **Blockers & Dependencies:**
   - **Camera selection** (Nov 13) depends on nighttime STARVIS sensor tests (Alex, due Nov 10) — tight timeline.
   - **CLIN 3 design work** (Nov 24–Dec 3) depends on camera & hardware selections being finalized.
   - **ATR variant (CLIN 5)** awaits customer clarification on model datasets, validation, and classification status (noted in task).
   - **CoVar requirements** (Dan, due Nov 6) is external scope — unclear if it blocks PCLT work.

4. **Team Capacity Concerns:** Maciej's Nov 4–5 Kanban check-in signals resource pressure on SOCOM and S3 projects. SOCOM has "lots of tasks still on the board"; team exploring whether to defer or add resources.

5. **No Dollar Value Visible:** Contract value, CLINs budget, or milestone payments are not exposed in task custom fields (only Organization and Priority are shown). This should be tracked for financial forecasting.

6. **10 Completed Tasks:** All recent completions are camera tests and requirements (Sept–Nov). No prototype or design closures yet — project is in early phase.