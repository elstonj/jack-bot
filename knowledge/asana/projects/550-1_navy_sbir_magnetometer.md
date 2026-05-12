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
  - **Key Upcoming Dates:**
    - Ground testing: May 22, 2026
    - S0-AD launcher design: Jun 5, 2026
    - S0-AD launcher build & test: Jun 15, 2026
    - Camp Pendleton demo: Aug 17, 2026 (flights scheduled Sep 14–25, 2026)
    - CLIN 0006 (Progress Report): Jun 29, 2026
    - CLIN 0007 (Final Report): Sep 28, 2026
- **Status:** **Active – Option Period in execution.** Early design & procurement phases completed (May 6). UK Navy EOI submitted early (May 11, 2026). Ground testing and launcher development underway. Camp Pendleton demo flights scheduled Sep 14–25, 2026 (field work tracking in Asana as due Aug 14 for planning/logistics).
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights) — primary execution lead
  - Jack Elston (technical lead, onboard logging & final reporting)
  - Maciej Stachura (Python tools, sensor configuration) — tasks completed
  - Beck Cotter (Camp Pendleton coordination, UK Navy EOI) — EOI submitted early
  - Meredith O'hara Needham (administrative, invoicing, FWA certification)
  - Dan Prendergast (support)
- **Risk Signals:**
  - **Compressed timeline:** Option period runs Apr 14 – Sep 28 (6.5 months) to complete design → build → ground test → hand-launched flights → Camp Pendleton demo + three Navy reports. Team bandwidth constrained by higher priorities (S3 IRAD, S0-VTOL, EMASS closure).
  - **Critical external dependency:** Camp Pendleton permissions & frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized (Aug 10).
  - **New launcher development:** S0-AD ground launcher is on critical path (design due Jun 5, build/test due Jun 15) — adds scope beyond original magnetometer integration.

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
| Order parts for S0-MAD reusable | Alex Lomis | May 5, 2026 | ✓ **COMPLETED** (May 6) | Parts procurement complete |
| Design onboard logging (both mag sensors) | Jack Elston | May 8, 2026 | **OPEN** | Blocks ground testing |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | ✓ **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Configure settings for both mag sensors | Maciej Stachura | May 18, 2026 | ✓ **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Conduct ground testing with different throttle settings | Alex Lomis | May 22, 2026 | **OPEN** | Dependent on onboard logging design |
| Submit UK Navy EOI | Beck Cotter | May 19, 2026 | ✓ **COMPLETED** (May 11, 2026) | **Submitted early** |
| Design of S0-AD ground launcher complete | Alex Lomis | Jun 5, 2026 | **OPEN** | New launcher development |
| Finalize Camp Pendleton permissions & frequencies | Beck Cotter | Jun 1, 2026 | **OPEN** | External coordination; critical path |
| Build up and ground test of S0-AD Launcher | Alex Lomis | Jun 15, 2026 | **OPEN** | Launcher build phase |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **OPEN** | Ground testing results dependent |
| Local test flights (hand-launched with both sensors) | Alex Lomis | Jul 1, 2026 | **OPEN** | Hand-launched build dependent |
| Finalize Camp Pendleton flight plans & aircraft | Alex Lomis | Aug 10, 2026 | **OPEN** | Permissions confirmed dependent |
| Camp Pendleton demo flights | Alex Lomis | Aug 17, 2026 → **Sep 14–25, 2026** | **IN PLANNING** | Actual flight window: Sep 14–25, 2026; planning/logistics due Aug 14 |

**Phase I (Completed January 2026):**
- Magnetometer Design, Analysis, and Testing ✓
- Acoustic Sensor Design, Analysis, and Testing ✓
- S0 platform modification and CAD delivery ✓

## Task Summary
- **Total Tasks in Asana:** 2 (1 open, 1 completed)
  - **OPEN:** Camp Pendleton demo flights (Alex Lomis, due Aug 14, 2026) — logistics/planning for Sep 14–25 field work
  - **COMPLETED:** Submit UK Navy EOI (Beck Cotter, completed May 11, 2026 — 8 days early)

**Note:** Asana tracking is minimal. Most execution work is tracked outside Asana or in other