_Asana snapshot as of 2026-11-18: 63 open tasks, 17 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Project Owner:** Dan Prendergast
- **Status:** Active – multi-phase development project with 6 CLINs (Contract Line Items) spanning through May 2027
- **Team Members:** Dan Prendergast (lead), Jack Elston, Sam Hild, Josh Fromm, Ben Busby, Ethan Domagala, Maciej Stachura, Alex Lomis
- **Dollar Value:** Not stated in custom fields; hours tracked by role (Mechanical Engineer, Electrical/Firmware, Software Engineer, Test Engineer, Systems Engineer, Technician)
- **Timeline:** 
  - Started: ~October 2026 (early prototyping)
  - Current phase: Component selection & PCLT testing (November 2026)
  - Final deliverable: May 2027 (CLIN 6 closeout)

## Key Deliverables & Milestones

| Milestone | Due Date | CLIN | Notes |
|-----------|----------|------|-------|
| PCLT Test Launch at SOCOM Facility | 2026-11-13 | Pre-CLIN | 50 Mech Eng hrs, 12 Sys Eng hrs; test report due 2026-11-13 |
| GFI: Answers re PCLT | 2026-11-20 | Pre-CLIN | Critical questions on 16lb separation, mount angle, skin gap |
| All-variants Common Camera Selection | 2026-11-11 | 1,2,4 | 70 total hours (10 Mech, 60 Test) |
| All-variants Common Processing Hardware Selection | 2026-11-18 | 1,2,4 | 30 Electrical/Firmware hrs |
| All-variants Common Radio Selection | 2026-12-11 | 1,2,4 | 25 Electrical/Firmware hrs |
| All-variants Carrier Board Design & Fab | 2026-12-14 | 1,2,4 | 40 Electrical/Firmware hrs (Sam Hild) |
| CLIN 1 Closeout (METAR variant) | 2027-03-12 | 1 | Includes sensor selection, component build, bench/ground/flight testing |
| CLIN 2 Closeout (EO/IR R&R variant) | 2027-03-12 | 2 | Sensor trade studies, prototype build, flight eval by 2027-03-05 |
| CLIN 3 Closeout (Auto-METAR variant) | 2027-05-31 | 3 | Precipitation, cloud layer, visibility sensor trades by 2027-01-29 |
| CLIN 4 Closeout (EO/IR ATR variant) | 2027-03-12 | 4 | ATR model selection, flight eval by 2027-04-24 |
| CLIN 5 Closeout (EO/IR FMV variant) | 2027-05-31 | 5 | Gimballed camera, gimbal control UI, flight eval by 2027-03-22 |
| CLIN 6 Closeout | 2027-05-31 | 6 | Closeout slides/report due 2027-03-26 |
| GFI: Customer begins airworthiness process | 2027-01-25 | — | Regulatory milestone |

## Task Summary

**Total Tasks:** 80 (63 open, 17 completed)

**Completion Rate:** 21% (17/80)

**Tasks by Assignee (open tasks):**
- **Dan Prendergast:** 10 open (project lead; camera selection, PCLT test, requirements, flight evals, closeout reports)
- **Jack Elston:** 4 open (processing hardware, radio selection, comm protocols)
- **Josh Fromm:** 3 open (PCLT design changes, mechanical/electrical updates)
- **Ethan Domagala:** 8 open (prototype builds & testing across all variants)
- **Ben Busby:** 3 open (software for payload integration)
- **Maciej Stachura:** 3 open (sensor trade studies, software/collection patterns)
- **Sam Hild:** 1 open (carrier board design)
- **Unassigned:** 31 open tasks (critical gaps in component studies, interface specs, hardware selection work, and prototype builds)

**Key Patterns:**
- **Heavy unassigned work:** 49% of open tasks have no assignee; includes critical path items (camera trade study, VOXL2 lead times, RB5 SOM comparison, autopilot-SBC interface spec, EMI testing)
- **Multiple parallel variants:** Project manages 6 distinct payload variants (METAR, EO/IR R&R, Auto-METAR, ATR, FMV, plus common platform work)
- **Hour tracking:** Extensive use of custom fields to track effort by role; major effort concentration in Mechanical Engineer hours (60–70 per task) and Test Engineer hours (40–60 per task)
- **Near-term pressure:** 11 tasks due by 2026-11-20; several marked as milestones with SOCOM questions pending

## Recent Activity

**Completed (November 2026):**
- Camera selection finalized (2026-11-13)
- Night/day camera testing completed (2026-11-06, 2026-11-11)
- Hardware ordered (Hadron cameras 2026-11-11)
- Site visit & instrumented S0 PCLT launch completed (2026-10-30)
- PCLT prototype with accelerometer built (2026-10-30)

**Imminent (November 2026):**
- PCLT test launch and report due 2026-11-13 (Dan Prendergast) — appears on track
- Multiple component selection/trade studies due 2026-11-18 to 2026-11-20 (mostly unassigned)
- Critical SOCOM feedback required by 2026-11-20 (PCLT safe separation, mount angle, skin gap)

**Upcoming (December 2026 – January 2027):**
- Carrier board design & fab (due 2026-12-14)
- Design changes for PCLT flight test (due 2026-12-11, Josh Fromm)
- Mechanical/electrical component integration updates (due 2026-12-21)
- Comm protocol design & implementation (due 2027-01-01)
- System-level requirements (due 2027-01-04)
- Sensor trade studies for CLIN 3 (due 2027-01-29)
- ATR selection & integration (due 2027-01-19)

## Notes & Context

**Critical Issues:**
1. **Unassigned critical path work:** 31 unassigned open tasks include foundational hardware decisions (VOXL2, RB5 SOM, radio, interface specs) needed to unblock downstream design. Recommend immediate assignment.
2. **PCLT feedback loop:** SOCOM's answers to 16lb separation, mount angle, and skin gap are due 2026-11-20 and will drive design changes (task due 2026-12-11). This is on the critical path.
3. **Hardware selection convergence:** Camera, processing, radio, and carrier board selections cluster around 2026-11-11 to 2026-12-14. Delays here will propagate to all 6 variants.

**Project Structure:**
- **CLIN 1 (METAR):** Weather sensor suite for autonomous collection (precipitation, cloud, visibility sensors)
- **CLIN 2 (EO/IR R&R):** Electro-optical/infrared with rapid-response capability
- **CLIN 3 (Auto-METAR):** Automated METAR variant (note: some tasks reference both METAR and Auto-METAR; may overlap or iteration)
- **CLIN 4 (ATR):** Real-time Automatic Target Recognition variant (open-source, unclassified models per task notes)
- **CLIN 5 (FMV):** Full-Motion Video with gimballed camera and datalink
- **CLIN 6:** Final integration and closeout

**Technical Context (from task notes):**
- **Computing platform:** VOXL2 + Hadron stack + RB5-class SOM; CoVar vision processing; custom autopilot-SBC interface
- **Testing:** Bench, ground, and local flight testing for each variant before operational flight evaluation with SOCOM
- **Airworthiness:** Customer to begin airworthiness process by 2027-01-25; suggests regulatory/safety-critical nature

**Next Steps:**
- Assign 31 unassigned tasks immediately, prioritizing component selection and interface spec work (due 2026-11-20)
- Confirm SOCOM PCLT feedback and design change timeline with Dan Prendergast
- Monitor carrier board design and comm protocol convergence (critical path for all variants)