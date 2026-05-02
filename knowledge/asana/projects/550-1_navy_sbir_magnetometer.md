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
- **Status:** **Active – Option Period underway (kicked off Apr 21, 2026).** Per Maciej Stachura (Apr 24): Navy SBIR Magnetometer is **priority #5** on current workload, behind S3 IRAD, S0-VTOL, EMASS closeout, and By-Lite Mustang.
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights)
  - Jack Elston (technical lead, onboard logging & final reporting)
  - Maciej Stachura (Python tools, sensor configuration)
  - Beck Cotter (Camp Pendleton coordination)
  - Meredith O'hara Needham (administrative, invoicing, FWA certification)
  - Dan Prendergast (support)
- **Risk Signals:**
  - **Heavy task load concentration on Alex Lomis:** 8 open technical tasks spanning design, procurement, build, and flight testing through Aug 17 demo. Critical path work concentrated on single PM.
  - **Compressed technical timeline:** Design (Apr 27–May 5) → build (May 19) → ground testing (May 29) → hand-launched flights (Jul 1) → Camp Pendleton demo (Aug 17), all before final report (Sep 28).
  - **Critical path dependencies:** Ground testing depends on completed design & parts ordering; hand-launched flights depend on build completion; Camp Pendleton demo depends on finalized flight plans.
  - **External dependency:** Camp Pendleton permissions/frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized.
  - **Asana/task tracking lag:** Raw data shows only 1 open task in Asana vs. 13 technical + 4 administrative tasks tracked in project knowledge file. Tasks appear tracked externally or in bulk-closed status without visibility updates. Recommend synchronization check before next priority review.
  - **Priority #5 status:** Resource constraints may limit team availability during peak execution phases (May–Aug).

## Key Deliverables & Milestones

**Option Period Administrative Deliverables:**
| CLIN | Deliverable | Owner | Amount | Due Date | Status |
|------|---|---|---|---|---|
| 0005 | Kick-Off & FWA Certification Report + Invoice | Meredith O'hara Needham | $50,000 | Apr 14, 2026 | ✓ **COMPLETED** (submitted Apr 14) |
| 0006 | Progress Report + Invoice | Jack Elston / Meredith O'hara Needham | $35,000 | Jun 29, 2026 | **In Progress** |
| 0007 | Final Report + Invoice | Jack Elston / Meredith O'hara Needham | $14,459 | Sep 28, 2026 | **Pending** |

**Technical Milestones (Option Period):**
| Milestone | Owner | Due Date | Status | Dependency |
|---|---|---|---|---|
| Complete design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | **OPEN** | Critical path start |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | **OPEN** | Follows design phase |
| Order parts for S0-MAD reusable | Alex Lomis | May 5, 2026 | **OPEN** | Design freeze |
| Design onboard logging (both mag sensors) | Jack Elston | May 8, 2026 | **OPEN** | Parallel to design phase |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | **OPEN** | Data processing prep |
| Configure settings for both mag sensors | Maciej Stachura | May 18, 2026 | **OPEN** | Pre-build |
| Build ground testing S0-MAD (flight-like) | Alex Lomis | May 19, 2026 | **OPEN** | Parts arrived |
| Ground testing with throttle settings | Alex Lomis | May 29, 2026 | **OPEN** | Build complete |
| Finalize Camp Pendleton permissions & frequencies | Beck Cotter | Jun 1, 2026 | **OPEN** | External coordination |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **OPEN** | Ground testing results |
| Local test flights (hand-launched with both sensors) | Alex Lomis | Jul 1, 2026 | **OPEN** | Hand-launched build |
| Finalize Camp Pendleton flight plans & aircraft | Alex Lomis | Aug 10, 2026 | **OPEN** | Permissions confirmed |
| Camp Pendleton demo flights | Alex Lomis | Aug 17, 2026 | **OPEN** | Flight plans finalized |

**Phase I (Completed January 2026):**
- Magnetometer Design, Analysis, and Testing ✓
- Acoustic Sensor Design, Analysis, and Testing ✓
- S0 platform modification and CAD delivery ✓
- Motor interference characterization and shielding analysis ✓
- DD882 interim patent form filed (Jan 28, 2026) ✓
- All Phase I reports and invoices submitted and paid (Feb 9–11, 2026) ✓

## Task Summary
- **Asana tasks (raw data):** 1 open, 0 completed
  - Single visible task: Preliminary Design Mods for re-usable S0-MAD (Alex Lomis, due May 1, 2026)
  - **Discrepancy Note:** Prior knowledge file tracked 13 technical + 4 administrative + 2 contact tasks. Raw Asana export shows only 1 task. Tasks appear to be tracked in project management system outside Asana or in bulk-closed status. Recommend task list reconciliation.
- **Tasks by assignee (from knowledge file):**
  - Alex Lomis: 8 open technical tasks (design, procurement, build, flight testing)