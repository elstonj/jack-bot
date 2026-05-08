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
  - **Project kicked off:** April 21, 2026
  - **Key Technical Dates (early phase completed):**
    - Design phase: Apr 27 – May 5 ✓ **COMPLETED** (May 6)
    - Parts order: May 5 ✓ **COMPLETED** (May 6)
    - Ground testing: May 22, 2026
    - S0-AD launcher design: Jun 5, 2026
    - S0-AD launcher build & test: Jun 15, 2026
    - UK Navy EOI submission: May 19, 2026
    - Camp Pendleton demo: Aug 17, 2026 (pending)
    - CLIN 0006 (Progress Report): Jun 29, 2026
    - CLIN 0007 (Final Report): Sep 28, 2026
- **Status:** **Active – Option Period in execution.** Design phase completed early (May 6); parts ordered. Current work focuses on ground testing, launcher design/build, and UK Navy EOI. One open task: Jack Elston's onboard logging design (due May 8 — **approaching deadline**).
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights) — primary execution lead
  - Jack Elston (technical lead, onboard logging & final reporting) — **1 active task**
  - Maciej Stachura (Python tools, sensor configuration) — completed assigned tasks as of Apr 20
  - Beck Cotter (Camp Pendleton coordination, UK Navy EOI)
  - Meredith O'hara Needham (administrative, invoicing, FWA certification)
  - Dan Prendergast (support)
- **Risk Signals:**
  - **APPROACHING DEADLINE:** Jack Elston's "Design of onboard logging of both mag sensors" due May 8 — status in Asana shows **open** (may be in progress or stalled).
  - **Priority #5 with compressed timeline:** Option period runs Apr 14 – Sep 28 (6.5 months) to complete design → build → ground test → hand-launched flights → Camp Pendleton demo + three Navy reports. Team bandwidth is constrained by higher priorities (S3 IRAD, S0-VTOL, EMASS closure).
  - **Critical external dependency:** Camp Pendleton permissions & frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized (Aug 10).
  - **New launcher development:** S0-AD ground launcher is on critical path (design due Jun 5, build/test due Jun 15) — adds complexity beyond original magnetometer integration scope.

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
| Complete design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | ✓ **COMPLETED** (May 6) | Design phase completed early |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | ✓ **COMPLETED** (May 6) | Design phase completed early |
| **Order parts for S0-MAD reusable** | **Alex Lomis** | **May 5, 2026** | **✓ COMPLETED (May 6)** | **Parts procurement complete** |
| **Design onboard logging (both mag sensors)** | **Jack Elston** | **May 8, 2026** | **🔴 OPEN – APPROACHING DEADLINE** | **In progress or at risk** |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | ✓ **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Configure settings for both mag sensors | Maciej Stachura | May 18, 2026 | ✓ **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| **Conduct ground testing with different throttle settings** | **Alex Lomis** | **May 22, 2026** | **OPEN** | Critical next phase |
| **Design of S0-AD ground launcher complete** | **Alex Lomis** | **Jun 5, 2026** | **OPEN** | New launcher development |
| **Build up and ground test of S0-AD Launcher** | **Alex Lomis** | **Jun 15, 2026** | **OPEN** | Launcher build phase |
| Finalize Camp Pendleton permissions & frequencies | Beck Cotter | Jun 1, 2026 | **Open** | External coordination; critical path |
| **Submit UK Navy EOI** | **Beck Cotter** | **May 19, 2026** | **OPEN** | Expression of Interest submission |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **Open** | Ground testing results dependent |
| Local test flights (hand-launched with both sensors) | Alex Lomis | Jul 1, 2026 | **Open** | Hand-launched build dependent |
| Finalize Camp Pendleton flight plans & aircraft | Alex Lomis | Aug 10, 2026 | **Open** | Permissions confirmed dependent |
| Camp Pendleton demo flights | Alex Lomis | Aug 17, 2026 | **Open** | Flight plans finalized dependent |

**Phase I (Completed January 2026):**
- Magnetometer Design, Analysis, and Testing ✓
- Acoustic Sensor Design, Analysis, and Testing ✓
- S0 platform modification and CAD delivery ✓
- Motor interference characterization and shielding analysis ✓
- DD882 interim patent form filed (Jan 28