# [550-1] NAVY SBIR: Magnetometer

## Overview
- **Client/Customer:** Department of the Navy (NAVAIR, NAWCAD)
  - **TPOC:** Angel Ruiz-Reyes, Physicist, Advanced Technology Development Department
    - Email: angel.r.ruiz-reyes.civ@us.navy.mil
    - Phone: (240) 587-9542
    - Address: NAWCAD, 22347 Cedar Point Road, Bldg. 2185, Patuxent River, MD 20670
  - **Secondary Contact:** Anthony Brescia, Avionics Engineering S&T Domain Lead
    - Email: anthony.d.brescia.civ@us.navy.mil
    - Phone: (240) 538-5265

- **Dollar Value:** $242,540 total budget
  - Phase I: Completed (January 2026)
  - **Option Period (Apr 14 – Sep 28, 2026): $99,459**
    - CLIN 0005 (Kick-Off & FWA Certification): $50,000 ✓ **COMPLETED** (submitted Apr 14, 2026)
    - CLIN 0006 (Progress Report): $35,000 — Due Jun 29, 2026 — **OPEN**
    - CLIN 0007 (Final Report): $14,459 — Due Sep 28, 2026 — **OPEN**

- **Timeline:** Option Period April 14 – September 28, 2026
  - **Project kicked off:** April 21–22, 2026
  - **Compressed 6.5-month timeline:** design → build → ground test → hand-launched flights → Camp Pendleton demo (Sep 14–25) + three Navy reports

- **Status:** ⚠️ **CRITICAL—DATA MISMATCH & REVIEW REQUIRED**
  - **Asana shows:** 1 open task ("Build up hand-launched S0-MAD", Alex Lomis, due Jun 12, 2026); last status update Mar 16, 2026 (green).
  - **Knowledge file documents:** 16 additional technical and administrative tasks with due dates May–August 2026, many now significantly overdue.
  - **⚠️ IMMEDIATE ACTION REQUIRED:** Contact Alex Lomis and Jack Elston to clarify:
    - Have the 16 overdue/in-progress technical and administrative tasks been completed but not closed in Asana?
    - Is the project actually on schedule for the Sep 28, 2026 final report deadline and Camp Pendleton demo (Sep 14–25)?
    - What is the current status of Camp Pendleton demo preparation?
  - **Priority:** **HIGH** (Navy government contract, compressed timeline, critical path on single assignee)

- **Team Members:**
  - **Alex Lomis** (PM/Owner, technical lead for builds & flights) — **⚠️ CRITICAL PATH; only assignee on open task**
  - **Jack Elston** (technical lead, onboard logging & reporting)
  - **Maciej Stachura** (Python tools, sensor configuration)
  - **Beck Cotter** (Camp Pendleton coordination & permissions)
  - **Meredith O'hara Needham** (administrative, invoicing, FWA certification)
  - **Dan Prendergast** (support)

## Key Deliverables & Milestones

**Administrative Deliverables (Navy-Required):**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | Jun 29, 2026 | **OPEN** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **OPEN** |

**Technical Milestones (from Knowledge File):**
| Milestone | Owner | Due Date | Status |
|---|---|---|---|
| Design of ground testing S0-MAD | — | Apr 27, 2026 | ✓ Completed |
| Preliminary design mods for reusable S0-MAD | — | May 1, 2026 | ✓ Completed |
| Order parts for S0-MAD reusable | — | May 5, 2026 | ✓ Completed |
| Design of onboard logging of both mag sensors | Jack Elston | May 8, 2026 | **⚠️ OVERDUE** (per knowledge file) |
| Finalize Python plotting and analysis tools for mag data | Maciej Stachura | May 13, 2026 | **⚠️ OVERDUE** (per knowledge file) |
| Build up ground testing S0-MAD (flight-ready) | Alex Lomis | May 19, 2026 | **⚠️ OVERDUE** (per knowledge file) |
| Conduct ground testing with different throttle settings | Alex Lomis | May 22, 2026 | **⚠️ OVERDUE** (per knowledge file) |
| Design of S0-AD ground launcher complete | Alex Lomis | Jun 5, 2026 | **⚠️ OVERDUE** (per knowledge file) |
| Finalize permissions, frequencies for Camp Pendleton Demo | Beck Cotter | Jun 1, 2026 | **⚠️ OVERDUE** (per knowledge file) |
| **Build up hand-launched S0-MAD** | Alex Lomis | Jun 12, 2026 | **OPEN** (only task in current Asana) |
| Build up and ground test of S0-AD Launcher | Alex Lomis | Jun 15, 2026 | — |
| Local test flights with hand-launched S0-MAD (both sensors) | Alex Lomis | Jul 1, 2026 | — |
| Finalize Camp Pendleton flight plans and Aircraft | Alex Lomis | Aug 10, 2026 | — |
| **Camp Pendleton demo flights** | Alex Lomis | Sep 14–25, 2026 | — |

## Task Summary
- **Asana Data (Current Raw Import):** 
  - 1 open task, 0 completed
  - **Build up hand-launched S0-MAD** (Alex Lomis, due Jun 12, 2026)

- **Knowledge File Data (Historical):** 
  - 17 open/in-progress tasks documented with due dates spanning May–September 2026
  - Multiple deliverables now overdue by months (May 8–Jun 5 due dates)

- **Data Quality Issue:** Significant mismatch between Asana and knowledge file.
  - Asana last updated: Mar 16, 2026 (before project kick-off on Apr 21–22)
  - No task closures or updates logged despite 4+ months of documented technical work
  - **Hypothesis:** Tasks completed and closed offline, or Asana project not actively maintained with closures
  - **⚠️ This is the PRIMARY REASON for immediate escalation to Alex Lomis and Jack Elston**

- **Critical Path Analysis:**
  - **Alex Lomis:** 8 tasks (design, builds, ground testing, hand-launched flights, Camp Pendleton demo execution, flight planning) — **Single point of failure on compressed timeline**
  - **Jack Elston:** 3 tasks (logging design, two Navy reports due Jun 29 & Sep 28)
  - **Maciej Stachura:** 1 task (Python tools, due May 13 — now overdue per knowledge file)
  - **Beck Cotter:** 1 task (Camp Pendleton permissions, due Jun 1 — now overdue per knowledge file)

## Recent Activity
- **Last Asana Status Update:** Mar 16, 