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

- **Status:** ⚠️ **CRITICAL—SIGNIFICANT OVERDUE TECHNICAL WORK**
  - **Current Asana:** 17 open tasks, 0 completed
  - **Major concern:** Multiple technical milestones now severely overdue (May 8–Jun 5 due dates; current date approximately Jun 8, 2026 per team feedback)
  - **Team feedback (Jun 8, 2026):** Maciej Stachura notes "mag integration it's Alex and Sam on the critical engineering tasks" — indicates **Sam is a critical team member not yet documented in Asana**
  - **Immediate risks:**
    - Camp Pendleton demo (Sep 14–25) depends on completion of overdue build, test, and design milestones
    - Alex Lomis is single point of failure (8 tasks on critical path)
    - CLIN 0006 Progress Report due Jun 29 requires status on overdue technical work
    - Unknown identity/role of "Sam" in critical path

- **Priority:** **HIGH** (Navy government contract, compressed timeline, critical path tasks overdue by 1+ months)

- **Team Members:**
  - **Alex Lomis** (PM/Owner, technical lead for builds & flights) — **⚠️ CRITICAL PATH; 8 technical tasks, many overdue**
  - **Sam** (Critical engineering on mag integration) — **ROLE/CONTACT INFO NEEDED**
  - **Jack Elston** (Technical lead, onboard logging & reporting)
  - **Maciej Stachura** (Python tools, sensor configuration)
  - **Beck Cotter** (Camp Pendleton coordination & permissions)
  - **Meredith O'hara Needham** (Administrative, invoicing, FWA certification)
  - **Dan Prendergast** (Support, not assigned to open tasks)

## Key Deliverables & Milestones

**Administrative Deliverables (Navy-Required):**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | **Jun 29, 2026** | **OPEN — 21 days to deadline** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **OPEN** |

**Technical Milestones (Critical Path — Many Overdue):**
| Milestone | Owner | Due Date | Status |
|---|---|---|---|
| Design of ground testing S0-MAD | — | Apr 27, 2026 | ✓ Completed |
| Preliminary design mods for reusable S0-MAD | — | May 1, 2026 | ✓ Completed |
| Order parts for S0-MAD reusable | — | May 5, 2026 | ✓ Completed |
| **Design of onboard logging of both mag sensors** | Jack Elston | **May 8, 2026** | **🔴 OVERDUE (31 days)** |
| **Finalize Python plotting and analysis tools for mag data** | Maciej Stachura | **May 13, 2026** | **🔴 OVERDUE (26 days)** |
| **Build up ground testing S0-MAD (flight-ready)** | Alex Lomis | **May 19, 2026** | **🔴 OVERDUE (20 days)** |
| **Conduct ground testing with different throttle settings** | Alex Lomis | **May 22, 2026** | **🔴 OVERDUE (17 days)** |
| **Design of S0-AD ground launcher complete** | Alex Lomis | **Jun 5, 2026** | **🔴 OVERDUE (3 days)** |
| **Finalize permissions, frequencies for Camp Pendleton Demo** | Beck Cotter | **Jun 1, 2026** | **🔴 OVERDUE (7 days)** |
| **Build up hand-launched S0-MAD** | Alex Lomis | **Jun 12, 2026** | **🟡 AT RISK (4 days)** |
| Build up and ground test of S0-AD Launcher | Alex Lomis | Jun 15, 2026 | At Risk |
| Local test flights with hand-launched S0-MAD (both sensors) | Alex Lomis | Jul 1, 2026 | At Risk |
| Finalize Camp Pendleton flight plans and Aircraft | Alex Lomis | Aug 10, 2026 | At Risk |
| **Camp Pendleton demo flights** | Alex Lomis | **Sep 14–25, 2026** | **🔴 CRITICAL DEADLINE** |

## Task Summary
- **Total Tasks:** 17 open, 0 completed
- **Tasks by Assignee & Overdue Status:**
  - **Alex Lomis:** 8 tasks (May 19, May 22, Jun 5, Jun 12, Jun 15, Jul 1, Aug 10, Sep 14) — **All depend on completing overdue May/early Jun milestones**
  - **Jack Elston:** 3 tasks (May 8 logging design 🔴 OVERDUE, Jun 29 Progress Report, Sep 28 Final Report)
  - **Maciej Stachura:** 1 task (May 13 Python tools 🔴 OVERDUE)
  - **Beck Cotter:** 1 task (Jun 1 Camp Pendleton permissions 🔴 OVERDUE)
  - **Meredith O'hara Needham:** 2 tasks (Jun 29 Invoice, Sep 28 Invoice)
  - **Unassigned:** 2 contact info tasks (Angel Ruiz-Reyes, Anthony Brescia)

- **Critical Pattern:** Alex Lomis carries 8 of 15 technical tasks on a compressed timeline with multiple sequential dependencies. Overdue early milestones (May 8–Jun 5) are now cascading; downstream tasks