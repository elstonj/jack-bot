# Flight Checklists

## Overview
- **Owner:** Ethan Domagala
- **Project Lead:** Daniel Prendergast
- **Client/Customer:** External flight operations (EMASS controller supplier, By-Lite fuse hardware vendor, CU IRISS training partner, 53rd Weather Squadron/SOCOM); **ISARRA Flight Week campaign (S0 VTOL units)**
- **Dollar Value:** Invoice 1667 — **$21,181.81 (ISARRA S0 VTOL units)** paid 2026-05-21
- **Timeline:** 
  - ISARRA delivery target: **August/September 2026**
  - NOAA ocean array test flight (By-Lite): **late July or early August 2026** (exact date TBD)
  - Asana milestone dates (2026-05-20 to 2026-05-29) are **stale and do not reflect actual flight schedule**
- **Status:** **BLOCKED & STALE** — All 12 Asana tasks remain unassigned. Real work is **external-dependency-driven**:
  - **EMASS controller binary (indefinitely delayed)** — customer blocker as of 2026-05-14 per Daniel Prendergast
  - **By-Lite fuse hardware (indefinitely delayed)** — no test flights until arrival per Jack & Maciej (2026-04-30); **2 flight opportunities still owed**
  - **CU IRISS training (✓ COMPLETED)** per Daniel Prendergast (2026-05-13/14)
  - **ISARRA Flight Week campaign** — **2 S0 VTOL units + ground station/tablet; build in QC (2026-07-03); flight-testing ongoing to resolve tracking bug per Beck; August delivery confirmed per Jack Elston & Kevin Adkins**
  - **Post-flight workflow improvement (IN PROGRESS)** — Daniel working to automate Maintenance Action Form linkage in log parse (2026-07-13/14)
- **Team Members:** Ethan Domagala (owner), Daniel Prendergast (project lead/SOCOM priority/post-flight workflow), Jack Elston (ISARRA logistics), Maciej (By-Lite flights/NOAA coordination), Kevin Adkins (approvals), Beck (flight-testing/demo calendar), Josh, Alex
- **Risk Signals (CRITICAL):**
  - **All 12 tasks unassigned** — execution blocker
  - **Planning Task 1 due 2026-05-20** — marked "Not started," likely overdue
  - **Execution Tasks 1 & 2 due 2026-05-26** — Task 2 in progress but unassigned; status unknown
  - **One task has no title/description** — data quality issue
  - **Planning Task 3 marked "Completed" but remains open** — status inconsistency
  - **Milestone 1 due 2026-05-21, marked in progress but unassigned** — status unclear
  - **Asana project structure obsolete** — real priorities driven by external dependencies and team Slack coordination, not Asana pipeline

## Key Deliverables & Milestones

| Deliverable | Target Date | **Real Status (Team Feedback — Authoritative)** | Value |
|---|---|---|---|
| **ISARRA Flight Week Campaign (2 S0 VTOL units + ground station/tablet)** | **August/September 2026** | **IN BUILD QC** — flight-testing ongoing to resolve tracking bug per Beck (2026-03-17); August delivery target confirmed per Jack Elston & Kevin Adkins (2026-05-21); build QC commenced 2026-07-03 | $21,181.81 |
| **NOAA Ocean Array Test Flight (By-Lite)** | **Late July or early August 2026** | **SCHEDULED (DATE TBD)** — Maciej coordinating with NOAA; requires Jack, Josh, Alex, or Maciej per Maciej (2026-07-10/13) | N/A |
| **By-Lite Fuse Hardware Test Flights** | Pending hardware arrival | **BLOCKED INDEFINITELY** — 2 flight opportunities still owed to By-Lite per Jack & Maciej (2026-04-30) | N/A |
| **CU IRISS Training** | N/A | **✓ COMPLETED** per Daniel Prendergast (2026-05-13/14) | N/A |
| **EMASS Validation Flight #2** | ~2026-05-26 | **POSTPONED INDEFINITELY** — awaiting customer controller binary per Daniel Prendergast (2026-05-14) | N/A |
| **EMASS Validation Flight #3** | ~2026-05-27 | **DELAYED TO ≥2026-05-08 Monday** per Daniel Prendergast (2026-05-04) | N/A |
| **Post-Flight Workflow (Maintenance Action Form automation)** | N/A | **IN PROGRESS** — Daniel working to embed form link in log parse end-of-upload flow (2026-07-13/14); goal: automatic checklist discipline | N/A |
| **Demo/Flight Calendar (through September)** | N/A | **UPDATED** — Beck maintaining shared calendar through September (2026-07-10/13) | N/A |

## Task Summary
- **Total:** 12 open, 0 completed
- **All 12 tasks unassigned** — critical blocker; no work allocation despite active flight operations
- **Status inconsistencies:**
  - Planning Task 3 marked "Completed" but remains open
  - Execution Task 2 & Milestone 1 marked "In progress" but unassigned with no updates
  - One task has empty title/description field
  - Launch Tasks 1 & 2 have no due dates
  - Execution plan approval task has no due date
- **Planning estimates:** Planning Task 1 (30m), Planning Task 2 (45m), Planning Task 3 (20m); execution/launch tasks have no estimates
- **Completion rate:** 0% (12 open, 0 closed; inconsistency in Planning Task 3 status)
- **By stage:** All 12 tasks in "Planning" stage despite active flight operations underway
- **By priority:** 4 High, 2 Medium, 2 Low, 4 unspecified
- **By assignee:** Unassigned (12/12)

## Recent Activity

### Team Feedback (Overrides Asana Dates — Authoritative)

**2026-07-14** — Daniel Prendergast: **Post-flight workflow automation in progress.** Seeking to embed Maintenance Action Form link in log parse at end of log upload process to drive automatic checklist discipline and task creation (hardware issues, software bugs).

**2026-07-13** — Daniel Prendergast: Repeating request to automate Maintenance Action Form linkage in log parse workflow for post-flight discipline.

**2026-07-13** — Maciej: **NOAA ocean array test flight (By-Lite).** NOAA requesting one additional clear air test flight over ocean array outside North Carolina in late July or early August; exact date TBD. Will require Jack, Josh, Alex, or Maciej.

**2026-07-13** — Beck: Updated demo/flight calendar through September (shared sheet accessible).

**2026-07-10** — Beck: Updated demo/flight calendar through September.

**2026-07-10** — Maciej: NOAA test flight coordination — one additional clear air test flight required late July or early August; date pending.

**2026-07-06** — Jack Bot (Slack #commercial-sales): **ISARRA Flight Week campaign** in build QC. 2 S0 VTOL units + ground station/tablet; invoice 1667 ($21,181.81) paid 2026-05-21. Flight-testing ongoing to resolve tracking bug per Beck (2026-03-17). August delivery target aligns with ISARRA planning & transport logistics per Jack Elston & Kevin Adkins (2026-05-21).

**2026-05-14** — Daniel Prendergast: CU IRISS training **complete**.