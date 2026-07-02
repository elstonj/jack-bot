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
    - CLIN 0006 (Progress Report): $35,000 — Due **Jun 29, 2026** — **OPEN** 
    - CLIN 0007 (Final Report): $14,459 — Due Sep 28, 2026 — **OPEN**

- **Timeline:** Option Period April 14 – September 28, 2026
  - **Project kicked off:** April 21–22, 2026
  - **Compressed 6.5-month timeline:** design → build → ground test → hand-launched flights → Camp Pendleton demo (Sep 14–25) + three Navy reports

- **Status:** 🔴 **CRITICAL — SIGNIFICANT OVERDUE BACKLOG**
  - **Multiple technical milestones OVERDUE as of Jun 8, 2026:**
    - Design of onboard logging (Jack Elston) — **31 days overdue** (due May 8)
    - Python plotting/analysis tools (Maciej Stachura) — **26 days overdue** (due May 13)
    - Build up ground testing S0-MAD (Alex Lomis) — **20 days overdue** (due May 19)
    - Ground testing with throttle variations (Alex Lomis) — **17 days overdue** (due May 22)
    - S0-AD launcher design (Alex Lomis) — **3 days overdue** (due Jun 5)
    - Camp Pendleton permissions/frequencies (Beck Cotter) — **7 days overdue** (due Jun 1)
  - **Asana currently shows 1 open task:** Local test flights with hand-launched S0-MAD (due Jul 1, 2026)
  - **Team feedback (Maciej Stachura, Jun 8, 2026):** "For mag integration it's Alex and Sam on the critical engineering tasks" — indicates active work underway despite stale Asana tracking. Note: Asana appears to significantly underrepresent actual project scope and real-time status.

- **Priority:** **HIGH** (Navy SBIR government contract, compressed timeline, critical path delays, Camp Pendleton demo deadline Sep 14–25, 2026)

- **Team Members:**
  - **Alex Lomis** (PM/Owner, technical lead) — **CRITICAL PATH**: 8+ build, test, and flight tasks
  - **Sam** (Critical engineering on mag integration) — per Maciej Stachura, Jun 8
  - **Jack Elston** (Technical lead, onboard logging & reporting; owns CLIN 0006/0007 reports) — Overdue design deliverable
  - **Maciej Stachura** (Python tools, sensor configuration, analysis) — Overdue analysis tools
  - **Beck Cotter** (Camp Pendleton coordination & permissions) — Overdue permissions task
  - **Meredith O'hara Needham** (Administrative, invoicing, FWA certification)
  - **Dan Prendergast** (Support)

## Key Deliverables & Milestones

**Navy-Mandated Administrative Deliverables (CLINs):**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | **Jun 29, 2026** | **OPEN — DUE IN 21 DAYS** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **OPEN** |

**Technical Milestones (Compressed Schedule):**
| Milestone | Owner | Due Date | Status as of Jun 8 |
|---|---|---|---|
| Design of ground testing S0-MAD | — | Apr 27, 2026 | ✓ Completed |
| Preliminary design mods for reusable S0-MAD | — | May 1, 2026 | ✓ Completed |
| Order parts for S0-MAD reusable | — | May 5, 2026 | ✓ Completed |
| **Design of onboard logging of both mag sensors** | Jack Elston | **May 8, 2026** | 🔴 **OVERDUE (31 days)** |
| **Finalize Python plotting and analysis tools for mag data** | Maciej Stachura | **May 13, 2026** | 🔴 **OVERDUE (26 days)** |
| **Build up ground testing S0-MAD (flight-ready)** | Alex Lomis | **May 19, 2026** | 🔴 **OVERDUE (20 days)** |
| **Conduct ground testing with different throttle settings** | Alex Lomis | **May 22, 2026** | 🔴 **OVERDUE (17 days)** |
| **Design of S0-AD ground launcher complete** | Alex Lomis | **Jun 5, 2026** | 🔴 **OVERDUE (3 days)** |
| **Finalize permissions, frequencies for Camp Pendleton Demo** | Beck Cotter | **Jun 1, 2026** | 🔴 **OVERDUE (7 days)** |
| **Build up hand-launched S0-MAD** | Alex Lomis | **Jun 12, 2026** | 🟡 **AT RISK** |
| **Build up and ground test of S0-AD Launcher** | Alex Lomis | **Jun 15, 2026** | 🟡 **AT RISK** |
| **Local test flights with hand-launched S0-MAD (both sensors)** | Alex Lomis | **Jul 1, 2026** | 🟡 **AT RISK** — *Current Asana task* |
| **Finalize Camp Pendleton flight plans and Aircraft** | Alex Lomis | Aug 10, 2026 | 🟡 **AT RISK** |
| **Camp Pendleton demo flights (Sep 14–25)** | Alex Lomis | **Sep 14–25, 2026** | 🔴 **CRITICAL DEADLINE** |

## Task Summary

**Asana Tracking:**
- **Total Asana tasks:** 1 open, 0 completed
  - [OPEN] Local test flights with hand-launched S0-MAD with both sensors | Alex Lomis | Due Jul 1, 2026

**Technical Work Status:**
Asana task count significantly underrepresents project scope. Based on known milestones, ~17 active technical/administrative milestones are tracked outside Asana or in stale states. Critical path items owned by Alex Lomis (