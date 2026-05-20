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
    - **Sensor configuration: May 18, 2026** (Maciej Stachura)
    - **Build up ground testing S0-MAD: May 19, 2026** (Alex Lomis) — *CRITICAL, due before May 22 execution*
    - Ground testing execution: May 22, 2026
    - Finalize Camp Pendleton permissions & frequencies: Jun 1, 2026 (Beck Cotter)
    - S0-AD launcher design: Jun 5, 2026
    - S0-AD launcher build & test: Jun 15, 2026
    - CLIN 0006 (Progress Report): Jun 29, 2026
    - Camp Pendleton demo: Aug 17, 2026 (flights scheduled Sep 14–25, 2026)
    - CLIN 0007 (Final Report): Sep 28, 2026
- **Status:** **Active – Option Period in execution.** Project is "mostly on schedule" as of May 6, 2026. Ground testing and launcher development underway. **NOTE:** Navy STTR has priority over SBIR as of May 2026. Camp Pendleton demo flights scheduled Sep 14–25, 2026.
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights) — primary execution lead
  - Jack Elston (technical lead, onboard logging & final reporting)
  - Maciej Stachura (Python tools, sensor configuration)
  - Beck Cotter (Camp Pendleton coordination, UK Navy EOI)
  - Meredith O'hara Needham (administrative, invoicing, FWA certification)
  - Dan Prendergast (support)
- **Risk Signals:**
  - **CRITICAL:** "Build up ground testing S0-MAD" (Alex Lomis, due May 19, 2026) — **1 OPEN TASK** in Asana. Due before May 22 ground testing execution. Blocks critical path.
  - **Compressed timeline:** Option period (6.5 months) to complete design → build → ground test → hand-launched flights → Camp Pendleton demo + three Navy reports. Team bandwidth constrained by higher-priority projects (S3 IRAD, S0-VTOL, EMASS closure, Navy STTR).
  - **Critical external dependency:** Camp Pendleton permissions & frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized (Aug 10).
  - **New launcher development:** S0-AD ground launcher is on critical path (design due Jun 5, build/test due Jun 15) — adds scope beyond original magnetometer integration.
  - **Possible stale Asana records:** "Settings for both Mag Sensors" (Maciej, May 18) may be completed; Maciej reported Navy tasks "done" as of Apr 20 & May 6. Verify status.

## Key Deliverables & Milestones

**Option Period Administrative Deliverables:**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** (submitted Apr 14, per Meredith Apr 17) |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | Jun 29, 2026 | **In Progress** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **Pending** |

**Report Templates:** Available at https://navysbir.com/links_forms.htm

**Technical Milestones (Option Period):**
| Milestone | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Complete design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | ✓ **COMPLETED** (May 6) | Design phase completed early |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | ✓ **COMPLETED** (May 6) | Design phase completed early |
| Order parts for S0-MAD reusable | Alex Lomis | May 5, 2026 | ✓ **COMPLETED** (May 6) | Parts procurement complete |
| Design onboard logging (both mag sensors) | Jack Elston | May 8, 2026 | **OPEN** | Blocks ground testing |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | ✓ **COMPLETED** | Per Maciej (Apr 20 & May 6) |
| Configure settings for both mag sensors | Maciej Stachura | May 18, 2026 | **OPEN (Asana)** | *Likely stale; Maciej reported Navy tasks "done" as of Apr 20 & May 6—verify status* |
| **Build up ground testing S0-MAD** | **Alex Lomis** | **May 19, 2026** | **🔴 OPEN (CRITICAL)** | **Due before May 22 ground testing execution. Currently only open task in Asana.** |
| Conduct ground testing with different throttle settings | Alex Lomis | May 22, 2026 | **OPEN** | Dependent on S0-MAD build completion (May 19) and onboard logging design |
| Submit UK Navy EOI | Beck Cotter | May 19, 2026 | ✓ **COMPLETED** (May 11, 2026) | Submitted early |
| Design of S0-AD ground launcher complete | Alex Lomis | Jun 5, 2026 | **OPEN** | New launcher development |
| Finalize Camp Pendleton permissions & frequencies | Beck Cotter | Jun 1, 2026 | **OPEN** | External coordination; critical path |
| Build up and ground test of S0-AD Launcher | Alex Lomis | Jun 15, 2026 | **OPEN** | Launcher build phase |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **OPEN** | Ground testing results dependent |
| Local test flights (hand-launched with both