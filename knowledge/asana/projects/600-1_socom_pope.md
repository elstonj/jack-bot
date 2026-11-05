_Asana snapshot as of 2026-11-05: 58 open tasks, 6 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Status:** Active — in early testing and design phase; multiple CLINs (Contract Line Items) spanning through May 2027
- **Timeline:** 
  - Current activity: Camera selection & testing (Nov 2026)
  - PCLT test launch: Nov 2026
  - PCLT flight test: Mar 2027
  - Full project completion (CLIN 6): May 2027
- **Team Members:** Dan Prendergast (lead/owner), Alex Lomis, Josh Fromm, Ethan Domagala, Ben Busby, Jack Elston, Maciej Stachura
- **Risk Signals:** 
  - 58 open tasks vs 6 completed (very early stage)
  - Multiple unassigned milestones (camera/radio/processing hardware selection, CLIN 2 closeout)
  - Several subtasks under "Design Changes for PCLT Flight Test" are unassigned with no due dates

## Key Deliverables & Milestones

**Near-term (Nov 2026):**
- Camera selection & testing (Nov 3–5): Day/night FoV and STARVIS sensor assessments (Alex Lomis)
- Design Changes for PCLT Flight Test (Nov 3, Josh Fromm)
- PCLT Test Launch at SOCOM Facility (Nov 13, Dan Prendergast)
- Comm Protocol Design & Implementation variant 1 (Nov 24, Jack Elston)

**CLIN 1 (through Mar 2027):**
- All-variants Common Camera, Radio, and Processing Hardware Selection (dates TBD, unassigned)
- Mechanical/Electrical Design Updates (Nov 25, Josh Fromm)
- Software for Payload Integration (Dec 3, Ben Busby)
- Prototype S0 METAR build & testing (Dec 22–Jan 9, Ethan Domagala)
- CLIN 1 Closeout (Mar 12)

**CLIN 2–6 (through May 2027):**
- Multiple sensor trade studies (Precipitation, Cloud/Ceiling, Visibility — Jan 29, Maciej Stachura)
- Prototype builds for Auto-METAR, EO/IR R&R, EO/IR Real-time ATR, EO/IR FMV variants
- Operational flight evaluations (multiple dates Jan–Apr 2027)
- Individual CLIN closeouts staggered through May 28

## Task Summary

**Completion Status:**
- 58 open, 6 completed (~9% completion rate)
- Project is in early execution; most design and build work ahead

**Tasks by Assignee:**

| Assignee | Open Tasks | Key Responsibilities |
|----------|-----------|----------------------|
| Dan Prendergast | 14 | Project lead; camera selection, SOW drafting, test launches, CLIN closeouts, operational evaluations |
| Ethan Domagala | 8 | Prototype builds (METAR, Auto-METAR, EO/IR variants); bench & flight testing |
| Josh Fromm | 7 | Design changes, mechanical/electrical updates for multiple CLINs |
| Ben Busby | 4 | Software for payload integration (CLIN 1, EO/IR R&R, Real-time ATR) |
| Alex Lomis | 5 | Camera testing (day/night), comm protocol, datalink radio selection |
| Maciej Stachura | 3 | Sensor trade studies (3 types), software/automation updates |
| Jack Elston | 1 | Comm Protocol Design & Implementation (CLIN 1, Nov 24) |
| Unassigned | 11 | Common hardware selections (camera, radio, processing), subtasks under design changes, CLIN 2 closeout |

**Notable Patterns:**
- Heavy reliance on Dan Prendergast for leadership/closeout tasks
- Ethan Domagala owns all prototype builds across multiple CLINs
- Multiple duplicate/parallel milestones (e.g., "Comm Protocol Design & Implementation" appears 4 times under different CLINs with different assignees and dates)
- 11 critical tasks unassigned, including common component selections that may block downstream work

## Recent Activity

**Completed (past few weeks):**
- SOCOM site visit and instrumented S0 launch (Oct 30, Josh Fromm) — answered aircraft integration questions
- Prototype PCLT S0 with accelerometer (Oct 30, Ethan Domagala)
- PCLT end cap design and order (Oct 15, Josh Fromm)
- Requirements & top-level design docs completed (late Oct, Dan Prendergast)

**Imminent (Next 2 weeks):**
- Write requirements and hold review (due Nov 2, Dan Prendergast)
- Camera start/stop and test plan write-ups (due Nov 3, Alex Lomis)
- Daytime camera tests with various FoV/resolution (due Nov 4, Alex Lomis)
- Nighttime camera tests with STARVIS sensor (due Nov 5, Alex Lomis)
- Software post-processing, camera selection, monthly customer meeting, SOW drafting (all due Nov 6, Dan Prendergast)

## Notes & Context

- **Project Structure:** This is a contract with 6 CLINs (Contract Line Items), each representing a different payload variant or capability for the PCLT (Payload Container Launch Tube) system:
  - CLIN 1: METAR variant (standard meteorological)
  - CLIN 2: Auto-METAR variant
  - CLIN 4: EO/IR Real-time ATR (Automatic Target Recognition)
  - CLIN 5: EO/IR Real-time ATR (appears to overlap or extend CLIN 4)
  - CLIN 6: EO/IR FMV (Full-Motion Video)
  
  (Note: CLIN 3 and CLIN 5 designations unclear from task list; may reflect contract structure not fully represented in subtasks.)

- **Camera Testing:** Alex Lomis is running a critical evaluation of day/night camera performance at 400' AGL with various field-of-view lenses in early November. This feeds into the "All-variants Common Camera Selection" milestone, which is unassigned and has no due date despite being listed first in the critical path.

- **Design Questions:** Notes under PCLT Flight Test design changes indicate open questions about aircraft integration (safe separation for payload, mounting angle, gap clearance) that may impact Nov 3 milestone.

- **ATR Variant Notes:** Dan Prendergast has flagged model questions (training datasets, validation, classification level) for the real-time ATR variant — all indicating open-source, unclassified models are being used.

- **Software Complexity:** Multiple milestones for "Software for Payload Integration and Automation" with different assignees and dates suggest a complex, phased software rollout. Notes reference autonomous data collection patterns, image capture triggers, compression, calibration, and UI updates.

- **Risk:** 11 unassigned tasks and lack of due dates on key hardware selections (camera, radio, processing hardware) could delay downstream variants if not assigned and scheduled soon. Dan Prendergast has heavy load through project closeout.