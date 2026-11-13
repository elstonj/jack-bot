_Asana snapshot as of 2026-11-13: 54 open tasks, 16 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Project Owner:** Dan Prendergast
- **Status:** Active — Heavy development phase with 54 open tasks and 16 completed. Multiple prototype builds and flight tests underway across 6 CLINs.
- **Timeline:** 
  - Early phase (camera/hardware selection): Nov 2026
  - PCLT test launch: Nov 13, 2026
  - Component integration & prototyping: Dec 2026 – Feb 2027
  - Operational flight evaluations: Mar–Apr 2027
  - Final closeouts: May 31, 2027
- **Team Members:** Dan Prendergast (owner, lead systems), Josh Fromm (mechanical design), Jack Elston (electrical/comms), Ethan Domagala (prototyping/build), Ben Busby (software), Maciej Stachura (sensors/software), Alex Lomis (testing), others

## Key Deliverables & Milestones

| Deliverable | Due Date | Notes |
|---|---|---|
| **GFI: Answers re PCLT** | 2026-11-20 | Safe separation (16lb?), mount angle, aircraft skin gap |
| **PCLT Test Launch at SOCOM Facility** | 2026-11-13 | Flight test of instrumented prototype |
| **CLIN 1 Closeout** (METAR variant) | 2027-03-12 | Design, build, test, operational flight eval |
| **CLIN 2 Closeout** (EO/IR R&R variant) | 2027-03-12 | Design, build, test, operational flight eval |
| **CLIN 4 Closeout** | 2027-03-12 | System-level requirements and integration |
| **CLIN 3 Closeout** (Auto-METAR variant) | 2027-05-31 | Sensor integration, automation, flight eval |
| **CLIN 5 Closeout** (EO/IR ATR variant) | 2027-05-31 | ATR model integration, real-time processing |
| **CLIN 6 Closeout** (EO/IR FMV variant) | 2027-05-31 | Gimballed camera, datalink, video UI, flight eval |
| **GFI: Customer begins airworthiness process** | 2027-01-25 | Regulatory milestone |

## Task Summary

- **Total:** 54 open, 16 completed (23.0% completion rate)
- **Assignee Distribution & Completion Rates:**
  - **Dan Prendergast:** 13 open tasks (owner/lead; multiple design reviews, requirements, closeouts)
  - **Ethan Domagala:** 9 open tasks (prototyping, build, bench/flight testing across all variants)
  - **Josh Fromm:** 4 open tasks (mechanical design updates, PCLT design changes)
  - **Jack Elston:** 4 open tasks (radio selection, comm protocol for multiple CLINs)
  - **Ben Busby:** 3 open tasks (payload software for METAR, ATR, FMV variants)
  - **Maciej Stachura:** 3 open tasks (sensor trade studies, auto-METAR software)
  - **Unassigned:** 18 open tasks (critical path: GFI milestones, CLIN closeouts, comm protocol)

- **Notable Patterns:**
  - Parallel workstreams across 6 CLINs (METAR, EO/IR R&R, Auto-METAR, ATR, FMV, plus PCLT test & CLIN 4 integration)
  - Heavy use of role-based hour estimates (Mechanical Engineer, Test Engineer, Electrical/Firmware, Software Engineer, Systems Engineer, Technician)
  - Significant unassigned work on critical path items (GFI responses, CLIN closeouts, comm protocols)
  - Many tasks cluster around mid-January 2027 (system-level requirements, comms, software) and late Feb–early Mar 2027 (prototype builds, flight tests)

## Recent Activity

**Recently Completed (Nov 2026):**
- Camera testing phase complete: nighttime STARVIS/Sony IMX585 sensor & lens filter assessments (Nov 11)
- Daytime FoV/resolution assessments (Nov 6)
- Hadron camera ordered and received (Nov 10–11)
- SOCOM site visit & instrumented S0 PCLT launch (Oct 30)
- PCLT prototype with accelerometer built (Oct 30)

**Approaching/Overdue Deadlines (next 30 days):**
- **Nov 13, 2026:** PCLT test launch + draft test results report (Dan Prendergast)
- **Nov 11, 2026:** Camera selection and trade study documentation (Dan Prendergast, unassigned)
- **Nov 18, 2026:** Common processing hardware selection (Jack Elston)
- **Nov 20, 2026:** GFI response on PCLT separation, mount angle, aircraft skin gap (Unassigned — **CRITICAL, AT RISK**)

## Notes & Context

- **PCLT (Parafoil Controlled Load Tube) Flight Test:** Early validation prototype with accelerometer launched. GFI (Government Furnished Information) responses due Nov 20 on safe separation margin (16lb threshold?), PCLT tube mount angle in aircraft, and gap between aircraft skin and tube rim. Answers critical for design changes and SOCOM facility coordination.

- **Multi-variant Strategy:** Project splits into parallel CLINs:
  - **CLIN 1 & 2:** METAR (weather reporting) and EO/IR R&R (reconnaissance/recovery) — closeout Mar 12
  - **CLIN 3:** Auto-METAR — closeout May 31
  - **CLIN 4:** System integration and common components
  - **CLIN 5 & 6:** EO/IR with ATR (Automatic Target Recognition) and FMV (Full Motion Video) with gimbal — closeout May 31

- **Hardware/Comms Selection Critical Path (Nov–Dec 2026):**
  - Camera selection due Nov 11 (Dan Prendergast, unassigned)
  - Processing hardware due Nov 18 (Jack Elston, $30k Electrical/Firmware)
  - Radio selection due Dec 11 (Jack Elston, $25k)
  - Carrier board design & fab due Dec 14 (Sam Hild, $40k)
  - PCLT design changes due Dec 11 (Josh Fromm, $70k mechanical)

- **Prototype Build & Flight Test Timeline (Feb–Apr 2027):**
  - S0 METAR prototype build due Feb 1 (Ethan Domagala, $65k)
  - S0 EO/IR R&R prototype build due Feb 1 (Ethan Domagala, $55k)
  - S0 Auto-METAR prototype build due Feb 24 (Ethan Domagala)
  - S0 EO/IR ATR variant due Apr 2 (Ethan Domagala)
  - S0 EO/IR FMV variant due Feb 24 (Ethan Domagala)
  - Operational flight evaluations span Mar–Apr with heavy Test Engineer and Systems Engineer hours (52h + 31h for OFE1)

- **Software/Autonomy Scope:**
  - Ben Busby (payload integration automation) due Jan 22 for METAR ($60k software), Feb 1 for EO/IR R&R ($40k), Apr 1 for ATR ($TBD)
  - Maciej Stachura (sensor integration, autonomous collection patterns) for Auto-METAR (due Mar 5, $TBD)
  - Notes indicate autonomous data collection patterns: "fly in circle and take data/image at each cardinal heading," back-end functions for image triggers, compression, calibration

- **Risk Signals:**
  - **Unassigned critical work:** GFI PCLT answers (Nov 20), three CLIN closeouts (3/12 and 5/31), comm protocol task (no due date)
  - **Compressed timeline:** Nov 13 PCLT test results expected just 2 days after launch; design changes due only 4 weeks later
  - **Parallel workload:** Ethan Domagala has 9 open build/test tasks across 5+ variants; potential bottleneck
  - **Hardware selection compressed:** All major component selections (camera, radio, processing, carrier board) due within 3-week window (Nov 11–Dec 14)

- **Airworthiness Process Kickoff:** Jan 25, 2027 milestone for customer to begin airworthiness review; implies design must stabilize by early Jan