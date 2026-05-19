# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift; additional $16k Delivery Order for 2 ground stations (approved 5/12/26)
- **Total Contract Value:** $499,000
- **Timeline:** 
  - Project Start/Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
  - **Critical hardware ship date:** May 27, 2026 (SHOW units)
  - **Final delivery deadline:** June 30, 2026 (all 20 units packed)
- **Status:** **ACTIVE — CRITICAL PHASE.** 4 of 6 invoices completed. Firmware fix completed 7 days late (5/8 vs 5/1 due). Platform rebuild completed ahead of schedule (5/14 vs 5/15). **Major risk: QC task overdue (due 5/15); only 1 open task visible in current Asana (order long-lead parts), but critical hardware builds (2 SHOW s0s, tripods, power switches, GCS units) appear to be in progress or externally tracked.** Critical path: May 15–27 with minimal buffer.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development) — firmware fix completed 5/8
  - Sam Hild (QC, hardware validation, kit assembly) — **overdue QC task**
  - Nate Straus (platform rebuild/validation, S0 builds, servo assembly, linkage construction) — completed May 15 rebuild 1 day early; 1 open power switch task due 5/21
  - Maciej Stachura (platform validation/testing, magnetic calibration)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA + 2 ground stations ($16k, approved 5/12/26)
  - Background: SBIR Phase I (2018, #1305M218CNRMW0059) and Phase II (2019–2020, #1305M219CNRMW0030) collaboration; current IDIQ builds on established partnership since 2018
- **Risk Signals:** 
  - 🚨 **CRITICAL QC TASK OVERDUE:** "QC at least one of each board as they arrive" (Sam Hild) **DUE 2026-05-15 — STATUS UNKNOWN.** This is a gating validation task for assembly flow. **Verify completion immediately.**
  - 🟡 **FIRMWARE FIX 7 DAYS LATE:** "Add RH / Vaisala fix to PSNS code" (Jack Elston) **DUE 2026-05-01 — COMPLETED 2026-05-08.** Potential cascade impact on downstream validation.
  - 🟡 **ASANA TASK LIST SIGNIFICANTLY REDUCED:** Prior knowledge file tracked 21+ active tasks; current raw data shows only 1 open task. Major hardware milestones (SHOW s0 builds, tripods, board QC, power switches, GCS assembly) appear completed, archived, or moved to external tracking. **Recommend verbal confirmation with Nate Straus and Sam Hild on hardware build status.**
  - 🟡 **LONG-LEAD PARTS PROCUREMENT — NO DUE DATE:** "order +20 more long lead time parts" (Josh Fromm) currently unscheduled in Asana. Given May 27 critical ship date, this task needs immediate prioritization and deadline assignment.

## Key Deliverables & Milestones

**Primary Deliverable:** 20 UAS units for NOAA + 2 ground stations ($16k) with critical atmospheric measurement capabilities

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| 4 of 6 | $72,000 | 2026-06-05 | ⏳ Open |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Open |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Open |
| **Subtotal** | **$483,000** | | |
| **Ground Stations DO** | **$16,000** | **2026-05-12** | ✅ **Approved 5/12/26** |
| **TOTAL** | **$499,000** | | |

**Hardware/Firmware/Validation Development Milestones:**

| Task | Owner | Due Date | Status | Priority | Notes |
|------|-------|----------|--------|----------|-------|
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ **COMPLETED 2026-05-08 (7 DAYS LATE)** | **CRITICAL** | Firmware fix completed; downstream work unblocked. |
| **Rebuild BST s0 (platform rebuild)** | Nate Straus | 2026-05-15 | ✅ **COMPLETED 2026-05-14 (1 DAY EARLY)** | HIGH | Critical progress: ahead of schedule. |
| **QC at least one of each board as they arrive** | Sam Hild | 2026-05-15 | 🚨 **OVERDUE** | **CRITICAL** | Hardware validation gate; currently overdue. **Verify completion status immediately.** |
| **Build 5 power switches with short pcb** | Nate Straus | 2026-05-21 | ⏳ **OPEN (Asana)** | **CRITICAL** | Component assembly; tight window before May 27 hardware ship. |
| **Build up 2 SHOW s0's using 2025 parts** | Nate Straus | 2026-05-22 | ❓ **NOT VISIBLE IN ASANA** | **CRITICAL** | **MUST SHIP MAY 27.** Likely in progress; confirm status. |
| **Build 2 show tripods** | Nate Straus | 2026-05-22 | ❓ **NOT VISIBLE IN ASANA** | **CRITICAL** | **MUST SHIP MAY 27.** Likely in progress; confirm status. |
| **Order +20 more long lead time parts** | Josh Fromm | **NO DUE DATE** | ⏳ **OPEN (Asana)** | **HIGH** | Procurement task missing deadline; needs immediate assignment. |
| **Build up new GCS x2** | Josh Fromm | 2026-07-01 | ❓ **NOT VISIBLE IN ASANA** | HIGH | Ground control stations for 2-unit Delivery Order. Assume in progress. |

## Task Summary

**Open Tasks in Asana: 1**
- Order +20 more long lead time parts | Josh Fromm | **NO DUE DATE ASSIGNED** ⚠️

**Completed Tasks in Asana: 0 (tracked in prior knowledge file)**
- Add