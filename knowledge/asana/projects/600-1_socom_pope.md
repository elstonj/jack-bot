_Asana snapshot as of 2026-11-10: 57 open tasks, 12 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Customer:** SOCOM (US Special Operations Command)
- **Priority:** High
- **Timeline:** Active project spanning November 2026 – May 2027
  - Near-term milestones: Camera selection & PCLT testing (Nov 2026)
  - Major closeouts: CLIN 1–6 (Mar–May 2027)
- **Status:** Active development. Currently in camera evaluation and prototype build phase
- **Team:** Dan Prendergast (lead/owner), Alex Lomis, Josh Fromm, Jack Elston, Sam Hild, Ben Busby, Ethan Domagala, Maciej Stachura
- **Risk signals:**
  - 57 open vs 12 completed tasks (low completion rate to date)
  - Multiple near-term deadlines in Nov 2026 (camera selection, PCLT test launch) with active work ongoing
  - Several unassigned critical tasks (FCL/DD254 sponsorship, camera trade study doc, CLIN 2 & 6 closeouts)

## Key Deliverables & Milestones

| Milestone | Due Date | Status | Lead |
|-----------|----------|--------|------|
| PCLT Test Launch (SOCOM facility) | 2026-11-13 | Open | Dan Prendergast |
| Camera & hardware selection (common variants) | 2026-11-11 | Open | Dan Prendergast / Jack Elston / Sam Hild |
| **CLIN 1 Closeout** | 2027-03-12 | Open | Dan Prendergast |
| **CLIN 2 Closeout** (METAR prototype) | 2027-03-12 | Open | Unassigned |
| **CLIN 3 Closeout** (Auto-METAR prototype) | 2027-05-31 | Open | Unassigned |
| **CLIN 4 Closeout** (EO/IR R&R prototype) | 2027-03-12 | Open | Dan Prendergast |
| **CLIN 5 Closeout** (EO/IR ATR prototype) | 2027-05-31 | Open | Dan Prendergast |
| **CLIN 6 Closeout** (FMV variant) | 2027-05-31 | Open | Unassigned |
| PCLT Flight Test | 2027-03-05 | Open | Dan Prendergast |
| Operational Flight Evaluations (CLINs 1, 2, 4) | 2027-03-05 | Open | Unassigned / Dan Prendergast |

**No dollar amounts found in task data.**

## Task Summary

- **Total tasks:** 57 open, 12 completed (17% completion rate)
- **Tasks by assignee (open only):**
  - Dan Prendergast: 13 tasks (owner/lead, heavily involved in PCLT, design decisions, requirements, closeouts)
  - Ethan Domagala: 8 tasks (prototyping & testing across multiple CLINs)
  - Josh Fromm: 4 tasks (mechanical/electrical design updates)
  - Jack Elston: 3 tasks (hardware selection & comm protocol)
  - Alex Lomis: 3 tasks (camera testing, comm protocol for CLINs)
  - Ben Busby: 3 tasks (software payload integration)
  - Maciej Stachura: 3 tasks (sensor trade studies, Auto-METAR software)
  - Sam Hild: 1 task (carrier board design)
  - Unassigned: 6 tasks (FCL/DD254 sponsorship, camera trade study doc, CLIN 2 & 3 & 6 closeouts, operational flight eval)

- **Notable patterns:**
  - Multi-variant structure: PCLT (test platform), METAR, Auto-METAR, EO/IR R&R, EO/IR ATR, FMV — each with parallel design → prototype → test → closeout tracks
  - Heavy prototyping workload on Ethan Domagala (bench, ground, local flight testing across 6 variants)
  - Camera/sensor selection happening now (Nov 2026); all downstream component & comm protocol work keyed to those decisions
  - Several tasks duplicated across CLINs with same due date (e.g., "Comm Protocol Design & Implementation" assigned to different people for different CLINs)

## Recent Activity

**Completed (last ~2 weeks, inferred from dates):**
- Camera test plans & daytime camera testing completed (Alex Lomis, ~Nov 6)
- L3 Harris image intensifier meeting held (Dan Prendergast, Nov 9)
- CoVar SOW & requirements drafted (Dan Prendergast, Nov 9)
- SOCOM site visit & PCLT S0 instrumented launch executed (Josh Fromm, Oct 30)
- PCLT prototype built & end cap designed (Ethan Domagala & Josh Fromm, Oct 15–30)

**Imminent (next 2–3 weeks):**
- Nighttime camera tests with STARVIS sensor & lens filter assessments (Alex Lomis, due Nov 10)
- Order 2× Hadron cameras (Dan Prendergast, due Nov 10)
- Document camera trade study & select cameras for common variants (Dan Prendergast / Unassigned, due Nov 11)
- Software post-processing of video for assessments (Dan Prendergast, due Nov 9)
- Draft PCLT test launch results report (Dan Prendergast, due Nov 13)
- **PCLT Test Launch at SOCOM facility** (Dan Prendergast, due Nov 13) — major gate event

## Notes & Context

1. **PCLT (Prototype Concept Launch Test)** is the near-term proof-of-concept that will inform the six parallel CLIN variants (METAR, Auto-METAR, EO/IR R&R, EO/IR ATR, FMV). Successful launch and results are critical path.

2. **Camera selection is a key blocker:** Multiple tasks depend on deciding between STARVIS/Sony IMX585 sensors and lens configurations. Night and day test results (due ~Nov 10) will feed this decision.

3. **Sponsorship unknown:** Task "Ask Jags for FCL/DD254 sponsorship" is unassigned with no due date — unclear if this is pending or already resolved externally.

4. **Auto-METAR (CLIN 3) payload notes suggest autonomous flight patterns** (e.g., circular orbits, cardinal headings for data collection) and back-end functions (triggers, compression, calibration) still being designed.

5. **ATR (Automatic Target Recognition) work (CLIN 5)** has model questions on training data, validation, and classification status — all noted as open-source, unclassified, which may affect integration scope.

6. **Six CLIN variants create scheduling complexity:** Parallel hardware/comm/software tracks, but most depend on PCLT results and common platform decisions (camera, processing hardware, radio) to move forward.

7. **Completion bottleneck:** 12 completed tasks vs 57 open suggests project is in heavy execution phase but not yet closing out work. Most tasks have future due dates (Nov 2026 – May 2027).