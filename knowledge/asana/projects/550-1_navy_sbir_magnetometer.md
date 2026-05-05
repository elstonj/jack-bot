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
- **Status:** **Active – Option Period underway.** Per Maciej Stachura (Apr 24, Apr 30): Navy SBIR Magnetometer is **priority #5** on current workload. However, **Asana data shows significant compression:** only 1 open task remains ("Order parts for S0-MAD Re-usable," due May 5, 2026), vs. 19 open tasks documented in previous knowledge file. This suggests either: (a) tasks have been aggressively closed/archived since last update, or (b) Asana task list is stale. **See Risk Signals below.**
- **Team Members:**
  - Alex Lomis (PM/Owner, technical lead for builds & flights) — 1 open task visible in current data
  - Jack Elston (technical lead, onboard logging & final reporting) — no open tasks visible
  - Maciej Stachura (Python tools, sensor configuration) — no open tasks visible
  - Beck Cotter (Camp Pendleton coordination) — no open tasks visible
  - Meredith O'hara Needham (administrative, invoicing, FWA certification) — no open tasks visible
  - Dan Prendergast (support)
- **Risk Signals:**
  - **CRITICAL: Task list compression mismatch.** Previous knowledge file documented 19 open technical tasks spanning design, procurement, build, and flight testing through Aug 17. Current Asana export shows only 1 open task. This is a **red flag for task tracking currency.** Either tasks have been bulk-closed without status update, or the Asana export is incomplete/filtered. **Recommend immediate audit with team to confirm actual project status vs. Asana visibility.**
  - **Compressed technical timeline remains:** Design (Apr 27–May 5) → build (May 19) → ground testing (May 29) → hand-launched flights (Jul 1) → Camp Pendleton demo (Aug 17), all before final report (Sep 28). Single remaining visible task (parts order, due May 5) is at design freeze point.
  - **Priority #5 status:** Resource constraints may limit team availability during peak execution phases (May–Aug).
  - **External dependency:** Camp Pendleton permissions/frequencies (Beck Cotter, due Jun 1) must be secured before demo logistics finalized (Aug 10). No open task visible for this critical path item.

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
| Complete design of ground testing S0-MAD (both mags) | Alex Lomis | Apr 27, 2026 | **OPEN** | Critical path start |
| Preliminary design mods for reusable S0-MAD | Alex Lomis | May 1, 2026 | **OPEN** | Follows design phase |
| **Order parts for S0-MAD reusable** | **Alex Lomis** | **May 5, 2026** | **OPEN** | **Only task visible in current Asana data; Design freeze point** |
| Design onboard logging (both mag sensors) | Jack Elston | May 8, 2026 | **OPEN** | Parallel to design phase |
| Finalize Python plotting/analysis tools | Maciej Stachura | May 13, 2026 | **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Configure settings for both mag sensors | Maciej Stachura | May 18, 2026 | **COMPLETE** | Per Maciej (Apr 20): "Tasks for the Navy project is done" |
| Build ground testing S0-MAD (flight-like) | Alex Lomis | May 19, 2026 | **OPEN** | Parts arrival dependent |
| Ground testing with throttle settings | Alex Lomis | May 29, 2026 | **OPEN** | Build completion dependent |
| Finalize Camp Pendleton permissions & frequencies | Beck Cotter | Jun 1, 2026 | **OPEN** | External coordination critical |
| Build hand-launched S0-MAD | Alex Lomis | Jun 12, 2026 | **OPEN** | Ground testing results dependent |
| Local test flights (hand-launched with both sensors) | Alex Lomis | Jul 1, 2026 | **OPEN** | Hand-launched build dependent |
| Finalize Camp Pendleton flight plans & aircraft | Alex Lomis | Aug 10, 2026 | **OPEN** | Permissions confirmed dependent |
| Camp Pendleton demo flights | Alex Lomis | Aug 17, 2026 | **OPEN** | Flight plans finalized dependent |

**Phase I (Completed January 2026):**
- Magnetometer Design, Analysis, and Testing ✓
- Acoustic Sensor Design, Analysis, and Testing ✓
- S0 platform modification and CAD delivery ✓
- Motor interference characterization and shielding analysis ✓
- DD882 interim patent form filed (Jan 28, 2026) ✓
- All Phase I reports and invoices submitted and paid (Feb 9–11, 2026) ✓

## Task Summary
- **Asana tasks (current):** 1 open, 0 completed
  - **Discrepancy alert:** Previous knowledge file documented 