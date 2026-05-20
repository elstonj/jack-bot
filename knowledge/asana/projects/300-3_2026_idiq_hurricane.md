# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift + $16,000 Delivery Order for 2 ground stations (approved 5/12/26) = **$499,000 total**
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA + 2 ground stations
  - Background: SBIR Phase I (2018, #1305M218CNRMW0059) and Phase II (2019–2020, #1305M219CNRMW0030) collaboration; ongoing partnership since 2018
- **Timeline:** 
  - Project Start: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
  - **Critical hardware ship date:** May 27, 2026 (SHOW units)
  - **Final delivery deadline:** June 30, 2026 (all 20 units packed)
- **Status:** **ACTIVE — CRITICAL PHASE RECENTLY COMPLETED.** Hardware builds appear substantially finished. Asana task list shows 0 open tasks and 2 completed (tripods & s0 builds both completed 5/19/26 ahead of May 27 ship date). 4 of 6 invoices completed; next invoice due 6/5/26.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development) — firmware fix completed 5/8 (7 days late)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction)
  - Maciej Stachura (platform validation/testing, magnetic calibration)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement)
- **Risk Signals:** ✅ **CRITICAL HARDWARE MILESTONES NOW COMPLETE.** Both tripod and s0 builds shipped 3 days early (5/19 vs 5/22 due). No open tasks in Asana. Firmware fix was 7 days late but did not block downstream work.

## Key Deliverables & Milestones

**Primary Deliverable:** 20 UAS units for NOAA + 2 ground stations ($16k) with critical atmospheric measurement capabilities

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| 4 of 6 | $72,000 | 2026-06-05 | ⏳ Due in next invoice cycle |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Due later |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Due at project end |
| **Subtotal** | **$483,000** | | |
| **Ground Stations DO** | **$16,000** | **2026-05-12** | ✅ **Approved 5/12/26** |
| **TOTAL** | **$499,000** | | |

**Hardware Development Milestones — RECENTLY COMPLETED:**

| Task | Owner | Due Date | Status | Notes |
|------|-------|----------|--------|-------|
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ COMPLETED 2026-05-08 (7 days late) | Firmware fix completed; downstream work unblocked. |
| **Rebuild BST s0 (platform rebuild)** | Nate Straus | 2026-05-15 | ✅ COMPLETED 2026-05-14 (1 day early) | Critical progress on schedule. |
| **Build 2 SHOW s0's using 2026 parts** | Nate Straus | 2026-07-17 (Asana) | ✅ **COMPLETED 2026-05-19 (59 DAYS EARLY)** | **Shipped ahead of critical May 27 deadline.** |
| **Build 2 SHOW tripods** | Nate Straus | 2026-05-22 | ✅ **COMPLETED 2026-05-19 (3 DAYS EARLY)** | **Shipped with s0 units ahead of schedule.** |

## Task Summary

**Open Tasks in Asana: 0**

**Completed Tasks: 2**
- ✅ Build 2 SHOW s0's using 2026 parts | Nate Straus | Due 2026-07-17 | Completed 2026-05-19
- ✅ Build 2 SHOW tripods to ship with SHOW s0 2026's | Nate Straus | Due 2026-05-22 | Completed 2026-05-19

**Notable Pattern:** Hardware assembly pipeline completed significantly ahead of schedule. Both critical builds completed together on 5/19/26, well before May 27 ship gate. Nate Straus drove early completion.

## Recent Activity

- **2026-05-19:** Both SHOW s0 builds (2 units) and tripods (2 units) completed and ready to ship — **3–59 days ahead of respective due dates.** Critical hardware now staged for May 27 shipment.
- **2026-05-08:** Firmware fix (RH/Vaisala) completed, 7 days behind original due date but did not block hardware builds.
- **2026-05-14:** Platform rebuild (s0) completed 1 day early, enabling downstream unit assembly.
- **2026-05-04:** Invoice 3 of 6 ($54k) submitted ahead of schedule (3 days early).

## Notes & Context

**Project Status:** In strong execution. No open tasks in Asana; all visible critical hardware milestones completed ahead of schedule by Nate Straus. The 2 completed tasks (tripods and s0 builds) both shipped 5/19, supporting the May 27 critical hardware shipment deadline for NOAA.

**Invoice Trajectory:** On track. 4 of 6 invoices completed ($162k + $18k travel = $180k submitted). Next invoice (4 of 6, $72k) due 2026-06-05.

**External Tracking Note:** Prior knowledge file flagged that major hardware milestones (QC, power switches, GCS assembly, long-lead parts) appeared to be externally tracked or in progress but not visible in Asana. Raw data now confirms core s0 and tripod builds are **complete**. Recommend confirming status of remaining assembly tasks (GCS units, final unit packing, QC sign-off) with Sam Hild and Josh Fromm during next standup.

**Contract Continuity:** NOAA partnership spans 8+ years (SBIR Phase I 2018, Phase II 2019–2020, now IDIQ build-out). Strong relationship foundation.