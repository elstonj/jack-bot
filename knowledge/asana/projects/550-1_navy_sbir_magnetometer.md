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
  - **Option Period:** April 14 – September 28, 2026
  - **Project kicked off:** April 21–22, 2026 (per Maciej)
  - **Key Upcoming Dates:**
    - Design onboard logging: May 8, 2026 (Jack Elston) — **OVERDUE** (current date ~May 11 per UK EOI completion)
    - Finalize Python tools: May 13, 2026 (Maciej Stachura)
    - Settings for both mag sensors: May 18, 2026 (Maciej Stachura)
    - **Build up ground testing S0-MAD: May 19, 2026** (Alex Lomis) — *CRITICAL, due before May 22 execution*
    - Ground testing execution: May 22, 2026
    - Finalize Camp Pendleton permissions & frequencies: Jun 1, 2026 (Beck Cotter)
    - **S0-AD launcher design: Jun 5, 2026** (Alex Lomis)
    - Build hand-launched S0-MAD: Jun 12, 2026 (Alex Lomis)
    - S0-AD launcher build & test: Jun 15, 2026 (Alex Lomis)
    - CLIN 0006 (Progress Report): Jun 29, 2026 (Jack Elston / Meredith O'hara Needham)
    - Local test flights (hand-launched): Jul 1, 2026 (Alex Lomis)
    - Finalize Camp Pendleton flight plans & aircraft: Aug 10, 2026 (Alex Lomis)
    - **Camp Pendleton demo flights: Sep 14–25, 2026** (Alex Lomis)
    - CLIN 0007 (Final Report): Sep 28, 2026 (Jack Elston / Meredith O'hara Needham)
- **Status:** **Active – Option Period in execution.** Project is "mostly on schedule" as of May 6, 2026 (per Maciej) and "mostly on schedule" as of May 8–11 (per Jack). **PRIORITY CONTEXT:** Navy STTR has priority over this SBIR as of May 2026 (per Jack, May 8 & 11). S3 IRAD, S0-VTOL, EMASS closure, and By-Lite Mustang also higher priority (per Maciej, Apr 24 & 30).
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights) — primary execution lead
  - Jack Elston (technical lead, onboard logging & final reporting)
  - Maciej Stachura (Python tools, sensor configuration)
  - Beck Cotter (Camp Pendleton coordination, UK Navy EOI)
  - Meredith O'hara Needham (administrative, invoicing, FWA certification)
  - Dan Prendergast (support)
- **Risk Signals:**
  - **OVERDUE TASK:** "Design onboard logging of both mag sensors" (Jack Elston, due May 8, 2026) — now overdue as of May 11 (UK EOI completion date). Blocks ground testing and CLIN 0006 progress report.
  - **CRITICAL:** "Build up ground testing S0-MAD" (Alex Lomis, due May 19, 2026) — still open in Asana; due before May 22 ground testing execution. Blocks critical path.
  - **Compressed timeline:** Option period (6.5 months) to complete design → build → ground test → hand-launched flights → Camp Pendleton demo + three Navy reports. Team bandwidth constrained by higher-priority projects (S3 IRAD end-of-May deadline, S0-VTOL, EMASS closure, Navy STTR).
  - **Critical external dependency:** Camp Pendleton permissions & frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized (Aug 10).
  - **New launcher development:** S0-AD ground launcher is on critical path (design due Jun 5, build/test due Jun 15) — adds scope beyond original magnetometer integration.
  - **Possible stale Asana records:** Per Maciej (May 6), Navy SBIR tasks "mostly caught up" and Asana was updated that day. "Finalize Python plotting and analysis tools" (Maciej, May 13) and "Settings for both Mag Sensors" (Maciej, May 18) likely near completion or already done; verify current status.

## Key Deliverables & Milestones

**Option Period Administrative Deliverables:**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** (submitted Apr 14, 2026) |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | Jun 29, 2026 | **IN PROGRESS** — Blocked by overdue onboard logging design task |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **PENDING** |

**Report Templates:** Available at https://navysbir.com/links_forms.htm

**Technical Milestones (Option Period):**
| Milestone | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Complete design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | ✓ **COMPLETED** | Per knowledge file (May 6) |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | ✓ **COMPLETED** | Per knowledge file (May 6) |
| Order parts for S0-MAD reusable | Alex Lomis | May 5, 2026 | ✓ **COMPLETED** | Per knowledge file (May 6) |
| **Design onboard logging (both mag sensors)** | **Jack Elston** | **May 8, 2026** | **🔴 OVERDUE** | **Asana shows open; blocks ground testing and CLIN 0006 progress report.** |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | ✓ **LIKELY COMPLETED** | Per Maciej (May