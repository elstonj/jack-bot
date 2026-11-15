_Asana snapshot as of 2026-11-15: 53 open tasks, 17 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Project Owner:** Dan Prendergast
- **Status:** Active — undergoing Asana restructuring (as of 2026-10-27, per Maciej); team managing execution via physical Kanban board while Asana tracks milestones and weekly tasks
- **Team Members:** Dan Prendergast (lead), Jack Elston, Sam Hild, Josh Fromm, Ben Busby, Ethan Domagala, Maciej Stachura, Alex Lomis
- **Risk Signals:** 
  - Maciej flagged (2026-11-05, 2026-11-04) that many SOCOM tasks remain on Kanban board; unclear if they should move to next week or need additional resources
  - Daniel Prendergast refactoring Asana project structure (in progress as of 2026-11-02, promised completion "Monday morning")

## Key Deliverables & Milestones
All CLIN closeouts are firm milestones:

| Milestone | Due Date | Notes |
|-----------|----------|-------|
| GFI: Answers re PCLT | 2026-11-20 | Customer questions on separation safety, mount angle, aircraft skin gap |
| PCLT Test Launch (Dan Prendergast) | 2026-11-13 | 50 ME hrs, 12 SE hrs |
| GFI: Customer begins airworthiness process | 2027-01-25 | |
| CLIN 1 Closeout | 2027-03-12 | METAR variant |
| CLIN 2 Closeout | 2027-03-12 | EO/IR R&R variant |
| CLIN 3 Closeout | 2027-05-31 | Auto-METAR variant |
| CLIN 4 Closeout | 2027-03-12 | EO/IR Real-time ATR variant |
| CLIN 5 Closeout | 2027-05-31 | EO/IR FMV variant |
| CLIN 6 Closeout | 2027-05-31 | Gimballed camera/datalink variant |

## Task Summary
- **Total:** 53 open, 17 completed (24% completion)
- **By Assignee (open tasks):**
  - Dan Prendergast: 11 tasks (camera trade study, PCLT test, design changes, requirements, ATR selection, FMV variant eval, gimballed camera trade study, various closeouts)
  - Ethan Domagala: 8 tasks (prototyping & testing across all variants: METAR, EO/IR, ATR, FMV)
  - Josh Fromm: 4 tasks (mechanical/electrical design updates across variants)
  - Jack Elston: 4 tasks (radio selection, comm protocol design, datalink radio)
  - Ben Busby: 3 tasks (software for payload integration; gimbal UI development)
  - Maciej Stachura: 3 tasks (sensor trade studies, software for Auto-METAR)
  - Unassigned: 10 tasks (milestones, comm protocol, mechanical updates, camera documentation)
- **Custom Field Usage:** Heavy labor tracking — most tasks include Mechanical Engineer, Test Engineer, Software Engineer, Systems Engineer, and Technician hour allocations

## Recent Activity
**Recently Completed (as of ~2026-11-13):**
- Select cameras (2026-11-13) — Dan Prendergast
- Order Hadron cameras (2026-11-11)
- Nighttime camera tests (2026-11-11) — Alex Lomis
- Software post-processing of video (2026-11-11)
- Meet with L3 Harris about image intensifiers (2026-11-09)
- SOCOM site visit & instrumented S0 launch (2026-10-30) — Josh Fromm
- Build prototype PCLT S0 with accelerometer (2026-10-30) — Ethan Domagala

**Approaching Near-term:**
- **Due 2026-11-11:** Document camera trade study and selection (unassigned), All-variants Common Camera Selection (Dan Prendergast)
- **Due 2026-11-13:** Draft report for test PCLT launch results (Dan Prendergast)
- **Due 2026-11-20:** GFI answers re PCLT (unassigned) — customer milestone

## Notes & Context

### Asana Restructuring (Authoritative)
**[2026-10-27] Maciej:** Planning two-level approach:
- Asana tracks long-term milestones and upcoming weekly tasks
- Physical Kanban board manages weekly engineering execution
- 6-month rolling milestone plan in Asana
**[2026-11-02, 2026-11-04] Daniel Prendergast:** Still refactoring SOCOM Asana project; "Project and stickies will be ready by Monday morning" (promised 2026-11-04, likely completed by 2026-11-05).

### Resource Constraints
**[2026-11-05, 2026-11-04] Maciej:** Flagged concerns that SOCOM and S3 projects have many tasks still on Kanban board. Asked for prioritization and resource allocation assessment. Note: "I know we don't have many [resources] available but just curious if anything could help."

### Project Scope
Six distinct variants across contract line items (CLINs):
1. **METAR** — meteorological sensor payload
2. **EO/IR R&R** — electro-optical/infrared with resource recorder
3. **Auto-METAR** — autonomous meteorological collection
4. **EO/IR Real-time ATR** — ATR (automatic target recognition) real-time processing
5. **EO/IR FMV** — full-motion video with gimballed camera
6. **Gimballed FMV variant** — FMV with datalink and gimbal control (CLIN 6)

Each follows: design → prototype build → bench/ground/local flight test → operational flight evaluation.

### Key Technical Questions (from task notes)
- PCLT safe separation distance (16lb?), mount angle in aircraft, gap between aircraft skin and tube rim
- Camera selection finalized (Hadron); night/day FoV testing complete
- ATR model: unclassified, open-source datasets, validation results, label list
- METAR sensors: precipitation, cloud layer/ceiling, horizontal visibility (trade studies due 2027-01-29)
- Software: autonomous data collection patterns, image triggers/compression/calibration, gimbal UI, no-comm transit mode

### Integration Notes
- Comm protocol design appears in CLIN 1, 2, 3, 5; due dates vary (late 2026 to early 2027)
- Mechanical and electrical design updates scheduled across variants, with high labor allocation (54–70 ME hours per variant)
- Technician hours concentrated in prototype build and testing phases (30–40 hrs per task)