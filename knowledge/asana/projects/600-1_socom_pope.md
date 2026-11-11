_Asana snapshot as of 2026-11-11: 55 open tasks, 13 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Project Lead:** Dan Prendergast
- **Status:** Active — multi-CLIN development program in early phase (55 open tasks, 13 completed). Recent completions (camera tests, site visit, requirements) indicate project is progressing through initial prototype and evaluation stages.
- **Timeline:** 
  - Current phase: Nov 2026 – Dec 2026 (camera selection, PCLT testing, component orders)
  - Extended development: Jan – May 2027 (CLINs 1–6 closeouts through March–May)
  - Final milestone: CLIN 6 complete by 2027-05-31
- **Team Members:** Dan Prendergast (PM/lead), Josh Fromm, Alex Lomis, Jack Elston, Sam Hild, Ben Busby, Ethan Domagala, Maciej Stachura
- **Risk Signals:** 
  - Multiple tasks due Nov 2026 (11–13) approaching imminently; camera selection and PCLT test launch are critical path
  - PCLT Test Launch (2026-11-13) has high labor allocation (50 ME + 12 SE hours)
  - Unassigned tasks on critical milestones (CLIN 2, CLIN 3, CLIN 6 closeouts; Operational Flight Eval)

## Key Deliverables & Milestones

| Milestone | Due Date | Status | Labor (hours) | Notes |
|-----------|----------|--------|---------------|-------|
| **PCLT Test Launch at SOCOM Facility** | 2026-11-13 | Open | ME: 50, SE: 12 | Critical near-term; draft report due same day |
| **Camera & Hardware Selection** | 2026-11-11 | Open | ME: 10, TE: 60 | Select cameras, order Hadron units, document trade study |
| **CLIN 1 Closeout** | 2027-03-12 | Open | — | Operational Flight Eval + closeout |
| **CLIN 2 Closeout** | 2027-03-12 | Open | — | METAR variant build, test, eval |
| **CLIN 3 Closeout** | 2027-05-31 | Open | — | Auto-METAR variant (sensor trades, integration, build, test) |
| **CLIN 4 Closeout** | 2027-03-12 | Open | — | EO/IR Real-time ATR variant (50 ME + 40 TE for build/test) |
| **CLIN 5 Closeout** | 2027-05-31 | Open | — | EO/IR FMV variant (gimbal, datalink, video UI) |
| **CLIN 6 Closeout** | 2027-05-31 | Open | — | Slides/report due 2027-03-26 |

## Task Summary

**Totals:** 55 open, 13 completed (19% completion rate)

**By Assignee (Open Tasks):**
- **Dan Prendergast:** 13 tasks (camera selection, PCLT launch, design reviews, ATR selection, requirements, closeout reports)
- **Ethan Domagala:** 9 tasks (prototype builds, component orders, bench/flight testing for all variants)
- **Josh Fromm:** 4 tasks (mechanical/electrical design updates, PCLT design changes)
- **Alex Lomis:** 4 tasks (nighttime camera tests, comm protocol, datalink radio)
- **Ben Busby:** 3 tasks (software for payload integration across variants)
- **Jack Elston:** 3 tasks (processing hardware, radio, comm protocol selections)
- **Maciej Stachura:** 3 tasks (sensor trade studies, software for Auto-METAR)
- **Unassigned:** 6 tasks (document camera trade study, Operational Flight Eval [2 instances], CLIN 2/3/6 closeout, Comm Protocol on one variant)

**Patterns:**
- Heavy concentration on Ethan (prototyping/builds) and Dan (leadership/reviews)
- Multiple duplicate/variant tasks reflect parallel development tracks (METAR, Auto-METAR, ATR, FMV variants)
- Labor tracked by role (Mechanical Engineer, Test Engineer, Electrical/Firmware, Software, Technician, Systems Engineer)
- Significant labor load: common selections (ME: 10–25h, TE: 60h, EE/FW: 15–30h), then variant-specific builds/testing (ME: 40–54h, TE: 40h per variant)

## Recent Activity

**Recently Completed (past ~2 weeks):**
- Camera testing completed (day and night assessment, plan write-up) — Alex Lomis
- SOCOM site visit and instrumented S0 launch — Josh Fromm (2026-10-30)
- Build prototype PCLT S0 with accelerometer — Ethan Domagala (2026-10-30)
- Requirements reviews completed — Dan Prendergast
- Monthly update meeting with customer PM established — Dan Prendergast
- Meetings held: L3 Harris (image intensifiers), CoVar SOW/requirements

**Imminent Deadlines (Next 2–3 Weeks):**
- **2026-11-09:** Software post-processing for video assessments (Dan), Meet with L3 Harris (completed)
- **2026-11-10:** Order Hadron cameras (Dan), Nighttime camera tests (Alex)
- **2026-11-11:** Camera selection (Dan), Document camera trade study (Unassigned), Common Camera Selection review
- **2026-11-13:** PCLT Test Launch at SOCOM (Dan + team), Draft report for test results
- **2026-11-18:** All-variants Common Processing Hardware Selection (Jack)
- **2026-11-25:** Gimballed camera trade study (Dan)
- **2026-11-30:** Write requirements and hold review (Dan)

## Notes & Context

**Project Structure:**
- Multi-variant development: five distinct CLINs (1–6 represent different payload configurations: METAR, Auto-METAR, EO/IR ATR, EO/IR FMV, and a final evaluation/closeout phase)
- Common foundational work (camera, hardware, radio, carrier board) feeds all variants
- Prototype-driven: S0 builds precede evaluation flights for each variant

**Key Technical Threads:**
1. **Camera/Optics:** STARVIS sensor (Sony IMX585) with narrow-band IR filter testing; FoV and lens trade studies for day/night operation; gimballed variant TBD
2. **Communications:** Protocol design, datalink radio selection, no-comm transit mode fallback
3. **Payload Processing:** Autonomous data collection patterns (circular flight, cardinal headings), image compression, trigger logic
4. **Sensors (CLIN 3):** Precipitation, cloud layer/ceiling, horizontal visibility trade studies (Maciej leading)
5. **AI/ATR (CLIN 4):** Unclassified models trained on open-source datasets; real-time inference on embedded hardware
6. **Video/Streaming (CLIN 5):** Full-motion video downlink with gimbal control and UI

**Custom Field Usage:**
- Labor tracked by discipline (Mechanical Engineer, Test Engineer, Electrical/Firmware, Software Engineer, Technician, Systems Engineer)
- Total budgeted hours are substantial (e.g., 50 ME + 12 SE for PCLT launch alone; 60 TE for camera selection)

**Compliance/Security:**
- FCL/DD254 sponsorship pursued (completed 2026-11-10)
- Unclassified models and datasets confirmed for ATR work

**Potential Gaps/Concerns:**
- Six unassigned tasks on critical paths (trade studies, operational flight evals, closeout slides)
- Comm Protocol Design duplicated across variants (3 instances, with different assignees/dates) — may indicate unclear ownership or variant-specific implementations
- No clear rollup/integration testing phase between individual variant builds and final operational evaluation