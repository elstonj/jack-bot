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
    - CLIN 0006 (Progress Report): $35,000 — Due Jun 29, 2026
    - CLIN 0007 (Final Report): $14,459 — Due Sep 28, 2026
- **Timeline:** Option Period April 14 – September 28, 2026
  - **Project kicked off:** April 21–22, 2026
  - **Compressed 6.5-month timeline** for design → build → ground test → hand-launched flights → Camp Pendleton demo + three Navy reports
- **Status:** **Active – Option Period in execution, mostly on schedule** (per Maciej Stachura, May 6 & Jack Elston, May 8–11, 2026)
  - **PRIORITY ALERT:** Navy STTR has priority over this SBIR as of May 2026 (Jack Elston, May 8 & 11). S3 IRAD, S0-VTOL, EMASS closure, and By-Lite Mustang also higher priority (Maciej Stachura, Apr 30). **Team bandwidth constrained.**
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights)
  - Jack Elston (technical lead, onboard logging & final reporting)
  - Maciej Stachura (Python tools, sensor configuration)
  - Beck Cotter (Camp Pendleton coordination)
  - Meredith O'hara Needham (administrative, invoicing, FWA certification)
  - Dan Prendergast (support)
- **Risk Signals:**
  - **Navy STTR now higher priority** (Jack Elston, May 11): Team bandwidth constrained; SBIR may slip if STTR escalates.
  - **Several near-term milestones now approaching or at their due dates** (May 8, 13, 18, 19, 22): Verify actual completion status given team's shifting priorities and Maciej's statement "mostly caught up" (May 6).
  - **Critical external dependency:** Camp Pendleton permissions & frequencies (Beck Cotter, due Jun 1) must be secured before Aug 10 logistics finalization.
  - **New launcher development (S0-AD):** Ground launcher design and build/test on critical path (Jun 5, Jun 15) — adds scope beyond original magnetometer integration.

## Key Deliverables & Milestones

**Administrative Deliverables (Navy-Required):**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** (submitted Apr 14) |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | **Jun 29, 2026** | **IN PROGRESS** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | **Sep 28, 2026** | **PENDING** |

**Technical Milestones (Critical Path):**
| Milestone | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | ✓ **COMPLETED** |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | ✓ **COMPLETED** |
| Order parts for S0-MAD reusable | Alex Lomis | May 5, 2026 | ✓ **COMPLETED** |
| Design onboard logging (both mag sensors) | Jack Elston | **May 8, 2026** | **OPEN** (due date passed; mark as overdue or verify completion) |
| Finalize Python plotting/analysis tools | Maciej Stachura | **May 13, 2026** | **OPEN** (due date passed; likely completed per May 6 feedback) |
| Settings for both Mag Sensors | Maciej Stachura | **May 18, 2026** | **OPEN** |
| **Build up ground testing S0-MAD** | **Alex Lomis** | **May 19, 2026** | **OPEN** | Critical path; due before May 22 ground testing execution |
| **Conduct ground testing with different throttle settings** | **Alex Lomis** | **May 22, 2026** | **OPEN** | Active execution; 1 open task in Asana |
| S0-AD launcher design | Alex Lomis | Jun 5, 2026 | **OPEN** | Critical path; new launcher development adds scope |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **OPEN** |
| S0-AD launcher build & test | Alex Lomis | Jun 15, 2026 | **OPEN** |
| **Finalize Camp Pendleton permissions & frequencies** | **Beck Cotter** | **Jun 1, 2026** | **OPEN** | **Blocker for Aug 10 logistics finalization** |
| Local test flights (hand-launched) | Alex Lomis | Jul 1, 2026 | **OPEN** |
| Finalize Camp Pendleton flight plans and Aircraft | Alex Lomis | Aug 10, 2026 | **OPEN** |
| **Camp Pendleton demo flights (Sep 14–25)** | **Alex Lomis** | **Aug 14, 2026** | **OPEN** | Major deliverable; actual demo dates Sep 14–25 |

## Task Summary
- **Total Tasks:** 18 open, 0 completed
- **Tasks by Assignee:**
  - Alex Lomis: 8 open tasks (technical lead for builds & flights; critical path items)
  - Jack Elston: 2 open tasks (reporting deliverables & onboard logging)
  - Meredith O'hara Needham: 2 open tasks (invoicing & administrative)
  - Maciej Stachura: 2 open tasks (Python tools & sensor configuration)
  - Beck Cotter: 1 open task (Camp Pendleton coordination — blocker)
  - Unassigned: 3 open tasks (Navy contacts: Angel Ruiz-Reyes, Anthony Brescia; project notes)
- **Completion Rate:** 0% (all tasks in Asana remain open)
- **Notable Patterns:**
  - Heavy technical workload concentrated on Alex Lomis (builds, testing, flights) — bandwidth risk given team prioritization shift.
  - Reporting deliverables depend on completion of technical work (Jack Elston producing progress & final reports based on testing results).
  - Five tasks with due dates in May 2026 (8, 13, 18,