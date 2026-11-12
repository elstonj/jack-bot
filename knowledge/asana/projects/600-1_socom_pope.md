_Asana snapshot as of 2026-11-12: 54 open tasks, 16 completed (last 90 days)._

# SOCOM Pope [600-1]

## Overview
- **Client:** SOCOM
- **Priority:** High
- **Owner:** Dan Prendergast
- **Status:** Active — Heavy development phase. Team is refactoring Asana project structure (per Daniel Prendergast, 2026-11-02); Kanban board managing weekly execution while Asana tracks milestones.
- **Team Members:** Dan Prendergast, Jack Elston, Sam Hild, Josh Fromm, Ben Busby, Ethan Domagala, Alex Lomis, Maciej Stachura
- **Risk Signals:** 
  - **SOCOM tasks backing up on Kanban board** (Maciej, 2026-11-04/05) — inquiring if work should shift to following week or if additional resources needed
  - Multiple immediate deadlines (camera selection, PCLT test report, GFI milestones) in next 2 weeks
  - Several tasks lack assignees (GFI milestone, CLIN 2/3 closeouts)

## Key Deliverables & Milestones

| Milestone | Due Date | Status | Notes |
|-----------|----------|--------|-------|
| **GFI: Answers re PCLT** | 2026-11-20 | Open | Critical gate: separation distance, mount angle, skin gap |
| **PCLT Test Launch at SOCOM Facility** | 2026-11-13 | Open | Dan assigned; test report due 2026-11-13 |
| **GFI: Customer begins airworthiness process** | 2027-01-25 | Open | Major milestone |
| **CLIN 1 Closeout** | 2027-03-12 | Open | Dan owns closeout |
| **CLIN 2 Closeout** | 2027-03-12 | Open | Unassigned |
| **CLIN 3 Closeout** | 2027-05-31 | Open | Unassigned |
| **CLIN 4 Closeout** | 2027-03-12 | Open | Dan owns closeout |
| **CLIN 5 Closeout** | 2027-05-31 | Open | Dan owns closeout |
| **CLIN 6 Complete** | 2027-05-31 | Open | Slides/report due 2027-03-26 |

## Task Summary

**Total Tasks:** 54 open, 16 completed (23% completion rate)

**Tasks by Assignee (Open Only):**
- **Dan Prendergast:** 14 tasks (camera selection, PCLT launch, design reviews, closeouts, ATR integration, FMV variant eval)
- **Ethan Domagala:** 8 tasks (prototype builds S0 METAR, EO/IR R&R, Auto-METAR; testing across variants)
- **Josh Fromm:** 4 tasks (design changes, mechanical integration updates)
- **Ben Busby:** 4 tasks (software for payload integration across variants)
- **Jack Elston:** 3 tasks (processing hardware, radio selection, comm protocol)
- **Alex Lomis:** 3 tasks (comm protocol design, datalink radio selection)
- **Maciej Stachura:** 3 tasks (sensor trade studies, software for Auto-METAR)
- **Sam Hild:** 1 task (carrier board design & fab)
- **Unassigned:** 14 tasks (including critical milestones)

**Work Allocation Patterns:**
- Heavy custom field usage tracking engineering hours by role (Mechanical Engineer, Test Engineer, Electrical/Firmware, Software Engineer, Systems Engineer, Technician)
- Largest hour blocks: Mechanical Engineer (design, fabrication), Test Engineer (evaluations), Software Engineer (payload integration)
- Ethan Domagala bottleneck: owns all prototype builds and ground testing across 6 variants

## Recent Activity

**Completed (Last ~2 weeks):**
- Camera testing complete: daytime FoV/resolution tests (2026-11-06), nighttime STARVIS assessments (2026-11-11)
- Hadron cameras ordered (2026-11-11)
- SOCOM site visit with instrumented S0 launch completed (2026-10-30)
- Requirements and design reviews completed across multiple CLINs (2026-11-02, 2026-10-30)

**Approaching Deadlines (Next 2 Weeks):**
- **2026-11-11:** Camera selection and trade study documentation (Dan Prendergast)
- **2026-11-13:** PCLT test launch + draft report (Dan Prendergast)
- **2026-11-18:** Processing hardware selection (Jack Elston)
- **2026-11-20:** GFI answers submission (critical gate)

**Asana Restructuring in Progress:**
Per Daniel Prendergast (2026-11-02 and 2026-10-30), "Project and stickies will be ready by Monday morning." Two-level planning model being implemented: Asana = long-term milestones + upcoming weekly tasks; physical Kanban = weekly engineering execution. 6-month rolling milestone plan in development.

## Notes & Context

- **Project Structure:** 6 CLINs (Contract Line Items) representing product variants:
  1. METAR (meteorological) 
  2. EO/IR R&R (electro-optical/infrared, reconnaissance/relay)
  3. Auto-METAR (autonomous meteorological)
  4. EO/IR Real-time ATR (automated target recognition)
  5. EO/IR FMV (full-motion video with gimballed camera)
  6. FMV variant (additional variant with video UI)

- **Technical Threads:** All variants depend on common component selections (camera, processing hardware, radio, comm protocol) happening *now* (due dates 2026-11-11 to 2026-12-11). Delays here cascade.

- **Resource Constraints:** Maciej flagged limited availability (2026-11-05) but asked if any SOCOM or S3 tasks could benefit from extra resources. No response captured.

- **Unassigned Critical Work:** 14 open tasks lack owners, including 3 CLIN closeout milestones. Recommend immediate assignment.

- **Testing Bottleneck:** Ethan Domagala assigned to prototype build + ground testing for all major variants through Q1 2027. Consider identifying backup for build/test tasks or staging prototype work.