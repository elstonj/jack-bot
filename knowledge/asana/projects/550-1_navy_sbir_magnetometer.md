# [550-1] NAVY SBIR: Magnetometer

## Overview
- **Client/Customer:** Department of the Navy (NAVAIR, NAWCAD)
  - TPOC: Angel Ruiz-Reyes, Physicist, Advanced Technology Development Department
  - Email: angel.r.ruiz-reyes.civ@us.navy.mil
  - Phone: (240) 587-9542
  - Address: NAWCAD, 22347 Cedar Point Road, Bldg. 2185, Patuxent River, MD 20670
  - Secondary Contact: Anthony Brescia, Avionics Engineering S&T Domain Lead
  - Email: anthony.d.brescia.civ@us.navy.mil
  - Phone: (240) 538-5265
- **Dollar Value:** $242,540 total budget
  - Phase I: Completed (January 2026)
  - **Option Period (Apr 14 – Sep 28, 2026): $99,459**
    - CLIN 0005 (Kick-Off & FWA Certification): $50,000 ✓ **COMPLETED** (submitted Apr 14, 2026)
    - CLIN 0006 (Progress Report): $35,000 — Due Jun 29, 2026
    - CLIN 0007 (Final Report): $14,459 — Due Sep 28, 2026
- **Timeline:**
  - Phase I completed: January 2026
  - **Option Period active:** April 14, 2026 – September 28, 2026
  - **Project kicked off:** April 21, 2026 (per Maciej Stachura, Apr 21)
  - **Key Technical Dates:**
    - Design phase: Apr 27 – May 5
    - Build & ground testing: May 19 – May 29
    - Hand-launched flights: Jul 1
    - Camp Pendleton demo: Aug 17
    - CLIN 0006 (Progress Report): Jun 29, 2026
    - CLIN 0007 (Final Report): Sep 28, 2026
- **Status:** **Active – Option Period underway.** Per Maciej Stachura (Apr 24, Apr 30): Navy SBIR Magnetometer is **priority #5** on current workload: "(1) S3 IRAD, (2) S0-VTOL, (3) Closing out EMASS, (4) By-Lite Mustang, and (5) **Initial tasks on the SBIR Magnetometer project.**" Project kicked off Apr 21, 2026. Asana task list shows only 1 open task (parts order due May 5), which aligns with **early-stage execution** (design phase compression). See Notes section for task tracking clarification.
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights) — primary execution lead
  - Jack Elston (technical lead, onboard logging & final reporting)
  - Maciej Stachura (Python tools, sensor configuration) — completed assigned tasks as of Apr 20
  - Beck Cotter (Camp Pendleton coordination)
  - Meredith O'hara Needham (administrative, invoicing, FWA certification) — CLIN 0005 delivered Apr 14
  - Dan Prendergast (support)
- **Risk Signals:**
  - **Priority #5 status with compressed timeline:** Option period runs Apr 14 – Sep 28 (6.5 months) to complete design → build → ground test → hand-launched flights → Camp Pendleton demo + three Navy reports. Team bandwidth is constrained by higher priorities (S3 IRAD, S0-VTOL, EMASS closure).
  - **Critical external dependency:** Camp Pendleton permissions & frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized (Aug 10). Monitor June checkpoint.
  - **Design freeze compression:** Only 9 days to finalize design (Apr 27–May 5) before parts order. Single visible Asana task is parts procurement at May 5 deadline.

## Key Deliverables & Milestones

**Option Period Administrative Deliverables:**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** (submitted Apr 14) |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | Jun 29, 2026 | **In Progress** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **Pending** |

**Technical Milestones (Option Period):**
| Milestone | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Complete design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | **Open** | Critical path start |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | **Open** | Follows design phase |
| **Order parts for S0-MAD reusable** | **Alex Lomis** | **May 5, 2026** | **OPEN in Asana** | **Design freeze point; only task visible in current export** |
| Design onboard logging (both mag sensors) | Jack Elston | May 8, 2026 | **Open** | Parallel to design phase |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | ✓ **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Configure settings for both mag sensors | Maciej Stachura | May 18, 2026 | ✓ **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Build ground testing S0-MAD (flight-like) | Alex Lomis | May 19, 2026 | **Open** | Parts arrival dependent |
| Ground testing with throttle settings | Alex Lomis | May 29, 2026 | **Open** | Build completion dependent |
| Finalize Camp Pendleton permissions & frequencies | Beck Cotter | Jun 1, 2026 | **Open** | External coordination; critical path |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **Open** | Ground testing results dependent |
| Local test flights (hand-launched with both sensors) | Alex Lomis | Jul 1, 2026 | **Open** | Hand-launched build dependent |
| Finalize Camp Pendleton flight plans & aircraft | Alex Lomis | Aug 10, 2026 | **Open** | Permissions confirmed dependent |
| Camp Pendleton demo flights | Alex Lomis | Aug 17, 2026 | **Open** | Flight plans finalized dependent |

**Phase I (Completed January 2026):**
- Magnetometer Design, Analysis, and Testing ✓
- Acoustic Sensor Design, Analysis, and Testing ✓
- S0 platform modification and CAD delivery ✓
- Motor interference characterization and shielding analysis ✓
- DD882 interim patent form filed (Jan 28, 2026) ✓
- All Phase I reports and invoices submitted and paid (Feb 9–11, 2026) ✓

## Task Summary
- **Asana tasks (current export):** 1 open, 0 completed
  - **Open:** Order parts for S0-MAD Re-usable (Alex Lomis, due May 5, 2026)
  
- **Task status clarification (from team feedback):**
  - Per Maciej (Apr 20): Python tools and sensor configuration tasks "done" (Finalize plotting/analysis + Configure settings both marked complete in knowledge file)
  