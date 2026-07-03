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
    - CLIN 0006 (Progress Report): $35,000 — ✓ **COMPLETED** (Invoice submitted Jul 2, 2026 — 3 days late)
    - CLIN 0007 (Final Report): $14,459 — Due Sep 28, 2026 — **OPEN**

- **Timeline:** Option Period April 14 – September 28, 2026
  - **Project kicked off:** April 21–22, 2026
  - **Compressed 6.5-month timeline:** design → build → ground test → hand-launched flights → Camp Pendleton demo (Sep 14–25) + three Navy reports

- **Status:** 🟡 **ACTIVE — RECOVERED FROM CRITICAL BACKLOG**
  - **As of early June 2026:** Multiple technical milestones were severely overdue (design, Python tools, ground testing, Camp Pendleton permissions).
  - **As of July 2, 2026:** CLIN 0006 (Progress Report) successfully submitted, indicating project recovery and continued execution despite earlier delays.
  - **Asana severely underrepresents project scope:** Raw Asana shows only 1 completed task (invoice), but actual project involves ~17 technical/administrative milestones tracked outside Asana or in stale states.
  - **Team feedback (Maciej Stachura, Jun 8, 2026):** "For mag integration it's Alex and Sam on the critical engineering tasks" — indicates active engineering work proceeding despite stale Asana tracking.
  - **Status as of Jul 2, 2026:** Project is active and delivering to Navy. Camp Pendleton demo (Sep 14–25) remains critical deadline.

- **Priority:** **HIGH** (Navy SBIR government contract, compressed timeline, critical path recovery, Camp Pendleton demo deadline Sep 14–25, 2026)

- **Team Members:**
  - **Alex Lomis** (PM/Owner, technical lead) — **CRITICAL PATH**: 8+ build, test, and flight tasks
  - **Sam** (Critical engineering on mag integration) — per Maciej Stachura, Jun 8
  - **Jack Elston** (Technical lead, onboard logging & reporting; owned CLIN 0006/0007 reports)
  - **Maciej Stachura** (Python tools, sensor configuration, analysis)
  - **Beck Cotter** (Camp Pendleton coordination & permissions)
  - **Meredith O'hara Needham** (Administrative, invoicing, FWA certification)
  - **Dan Prendergast** (Support)

## Key Deliverables & Milestones

**Navy-Mandated Administrative Deliverables (CLINs):**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | **Jun 29, 2026** | ✓ **COMPLETED** (Jul 2, 2026 — 3 days late) |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **OPEN** |

**Technical Milestones (Compressed Schedule):**
| Milestone | Owner | Due Date | Status as of Jul 2 |
|---|---|---|---|
| Design of ground testing S0-MAD | — | Apr 27, 2026 | ✓ Completed |
| Preliminary design mods for reusable S0-MAD | — | May 1, 2026 | ✓ Completed |
| Order parts for S0-MAD reusable | — | May 5, 2026 | ✓ Completed |
| **Design of onboard logging of both mag sensors** | Jack Elston | **May 8, 2026** | 🟡 Recovered (was 31 days overdue Jun 8) |
| **Finalize Python plotting and analysis tools for mag data** | Maciej Stachura | **May 13, 2026** | 🟡 Recovered (was 26 days overdue Jun 8) |
| **Build up ground testing S0-MAD (flight-ready)** | Alex Lomis | **May 19, 2026** | 🟡 Recovered (was 20 days overdue Jun 8) |
| **Conduct ground testing with different throttle settings** | Alex Lomis | **May 22, 2026** | 🟡 Recovered (was 17 days overdue Jun 8) |
| **Design of S0-AD ground launcher complete** | Alex Lomis | **Jun 5, 2026** | 🟡 Recovered (was 3 days overdue Jun 8) |
| **Finalize permissions, frequencies for Camp Pendleton Demo** | Beck Cotter | **Jun 1, 2026** | 🟡 Recovered (was 7 days overdue Jun 8) |
| **Build up hand-launched S0-MAD** | Alex Lomis | **Jun 12, 2026** | 🟡 **AT RISK** |
| **Build up and ground test of S0-AD Launcher** | Alex Lomis | **Jun 15, 2026** | 🟡 **AT RISK** |
| **Local test flights with hand-launched S0-MAD (both sensors)** | Alex Lomis | **Jul 1, 2026** | 🟡 **AT RISK** — *Current Asana task* |
| **Finalize Camp Pendleton flight plans and Aircraft** | Alex Lomis | Aug 10, 2026 | 🟡 **AT RISK** |
| **Camp Pendleton demo flights (Sep 14–25)** | Alex Lomis | **Sep 14–25, 2026** | 🔴 **CRITICAL DEADLINE** |

## Task Summary

**Asana Tracking:**
- **Total Asana tasks:** 0 open, 1 completed
  - ✓ [COMPLETED] Submit Invoice CLIN 0006 ($35,000) | Meredith O'hara Needham | Due Jun 29, 2026 | Completed Jul 2, 2026

**Actual Project Scope:**
Asana significantly underrepresents project work. Based on known milestones and Navy CLINs, ~17 active technical and administrative milestones are tracked outside Asana or in stale states. Critical path items are owned primarily by Alex Lomis with significant contributions from Jack Elston, Maciej Stachura, Beck Cotter, and Sam (magnetometer integration).

## Recent Activity
- **Jul 2,