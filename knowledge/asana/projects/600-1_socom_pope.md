_Asana snapshot as of 2026-11-02: 58 open tasks, 6 completed (last 90 days)._

# SOCOM Pope [600-1]

## Overview

- **Client/Customer:** SOCOM
- **Priority:** High
- **Status:** Active, in execution phase. Recent team feedback (2026-10-30) indicates ongoing Asana restructuring to improve visibility and alignment with Kanban board.
- **Team Lead:** Dan Prendergast
- **Key Team Members:** Josh Fromm, Alex Lomis, Ben Busby, Ethan Domagala, Maciej Stachura, Jack Elston
- **Risk Signals:** 
  - Asana project undergoing restructuring as of late October; interim task tracking may be incomplete or stale
  - Multiple milestones with November 2026 deadlines (camera testing, design reviews) in active phase
  - Long-tail deliverables extending through May 2027 across 6 CLINs

## Key Deliverables & Milestones

**Near-term (November 2026):**
- **All-variants Common Camera Selection** – Due 2026-11-06 (milestone); trade study doc due 2026-11-11
- **Camera Testing (Day/Night/FoV Assessment)** – Due 2026-11-03 to 2026-11-05 (Alex Lomis)
- **Design Changes for PCLT Flight Test** – Due 2026-11-03 (Josh Fromm)
- **PCLT Test Launch at SOCOM Facility** – Due 2026-11-13
- **Comm Protocol Design & Implementation (CLIN 1)** – Due 2026-11-24 (Jack Elston)
- **Mechanical & Electrical Design Updates (CLIN 1)** – Due 2026-11-25 (Josh Fromm)
- **Gimballed Camera Trade Study** – Due 2026-11-25

**Mid-term (December 2026 – March 2027):**
- **Software for Payload Integration & Automation (CLIN 1)** – Due 2026-12-03 (Ben Busby)
- **Build Prototype S0 METAR** – Due 2026-12-22 (Ethan Domagala)
- **System-level Requirements** – Due 2027-01-04
- **CLIN 1 Closeout** – Due 2027-03-12
- **PCLT Flight Test** – Due 2027-03-05
- **Build Prototype S0 Auto-METAR** – Due 2027-02-24 (Ethan Domagala)
- **Build Prototype S0 EO/IR R&R** – Due 2027-01-28 (Ethan Domagala)
- **Build Prototype S0 EO/IR Real-time ATR** – Due 2027-04-02 (Ethan Domagala)
- **Build Prototype S0 EO/IR FMV** – Due 2027-02-24 (Ethan Domagala)

**Later CLINs (through May 2027):**
- **CLIN 2, 4, 5, 6 Closeouts** – Between March and May 2027
- **Operational Flight Evaluations** across variants – Between January and April 2027

## Task Summary

- **Total Tasks:** 58 open, 6 completed
- **Task Completion Rate:** ~9% (6 of 64 total)
- **Tasks by Assignee (open only):**
  - Dan Prendergast: 15+ tasks (driver for reqs, SOW, reports, flight evals, closeouts)
  - Ethan Domagala: 9 tasks (builds and testing across 5 prototypes)
  - Josh Fromm: 5 tasks (mechanical/electrical design, PCLT design)
  - Alex Lomis: 5 tasks (camera testing, comm protocol, datalink)
  - Ben Busby: 4 tasks (software payloads, gimbal control)
  - Maciej Stachura: 4 tasks (sensor trade studies, software)
  - Jack Elston: 1 task (comm protocol CLIN 1)
  - Unassigned: 10+ tasks (milestones and critical path items)

- **Notable Patterns:**
  - Heavy structural use of milestone subtasks; many critical deliverables unassigned
  - Multiple parallel CLIN streams (METAR, Auto-METAR, EO/IR R&R, EO/IR ATR, EO/IR FMV, FMV Gimbal)
  - Significant dependency on Ethan Domagala for prototyping across all variants
  - Test-heavy execution model (bench, ground, flight evals for each variant)

## Recent Activity

**As of 2026-10-30:**
- Daniel Prendergast actively refactoring Asana project structure; redesigned project and stickies to be ready by Monday morning (2026-11-02 implied).
- Team transitioning to a two-level planning model: Asana tracks long-term milestones and weekly tasks; physical Kanban board manages weekly engineering execution.
- Site visit completed (2026-10-30) with instrumented S0 launch and accelerometer testing; end cap design and accelerometer ordered.
- Camera test plans drafting underway (due 2026-11-03); daytime and nighttime camera assessments imminent.
- Top-level requirements being derived from five CONOPS in ROMs; expected completion early November 2026.

**Upstream Status (from 2026-10-07/08 feedback):**
- End cap CAD completed by Josh; quote requested
- Accelerometer ordered for ejection force profile measurement
- Components expected late week of 2026-10-19 or week of 2026-10-26

## Notes & Context

- **Project Restructuring:** Per Maciej (2026-10-27), this project is undergoing significant Asana restructuring to simplify active R&D tracking and provide better visibility. Asana data as of this export may not reflect current execution state. The team is implementing a 6-month rolling milestone plan with weekly execution tracked on a physical Kanban board.
- **CLIN Structure:** Project is organized into six Contract Line Items with staggered timelines and prototype variants:
  - **CLIN 1 (PCLT):** Narrowest scope; test launch Nov 2026, flight test Mar 2027
  - **CLIN 2 (Auto-METAR):** Operational flight eval Mar 2027
  - **CLIN 4 (EO/IR ATR):** Real-time auto-target recognition; operational flight eval Apr 2027
  - **CLIN 5 (EO/IR FMV):** Full-motion video with gimbal; operational flight eval Mar 2027
  - **CLIN 6 (FMV Gimbal):** Gimballed camera variant; complete May 2027
  - Additional CLIN for sensor trade studies (Precipitation, Cloud, Visibility)
- **Critical Path Risks:**
  - Many unassigned milestones and subtasks; assignment ownership unclear
  - Ethan Domagala is single point of failure for five prototype builds spanning Dec 2026 – Apr 2027
  - Design changes and component arrival (late Oct/early Nov) feed into downstream milestones tightly; any slippage cascades
  - Software payload integration (Ben Busby, Maciej Stachura) starts mid-December with tight 4–6 week cycles to operational flight eval

- **Dollar Value:** Not visible in task names or custom fields; likely tracked in separate contract/finance system
- **Autonomy Questions:** Ben Busby's software integration tasks reference "Autonomous Data Collection Patterns" (fly in circle, capture at cardinal headings); indicates active design discussion for automated operational workflows