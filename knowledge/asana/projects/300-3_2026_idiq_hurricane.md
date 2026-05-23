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
  - **Critical hardware ship date:** May 27, 2026 (SHOW s0 units using 2025 parts)
  - **Final delivery deadline:** June 30, 2026 (all 20 units packed)
- **Status:** **ACTIVE — CRITICAL PHASE IN PROGRESS.** ⚠️ **2 OPEN CRITICAL TASKS** (per current Asana data) — hardware builds in final stages. Both tasks due 5/22/26 (s0 units and shipment to NOAA). Note: Previous knowledge file listed 4 open tasks; current Asana shows 2 open. Power switches task and parameter validation may have been completed or closed.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction, power switch builds) — **carrying critical open hardware task**
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement)
- **Risk Signals:** 
  - ⚠️ **2 critical tasks due 5/22/26, both in OPEN state:**
    - "Build up 2 SHOW s0's using 2025 parts - MUST SHIP MAY 27th" (Nate Straus, due 5/22)
    - "Ship S0s Models to NOAA (2 locations)" (Meredith O'hara Needham, due 5/22)
  - ⚠️ **May 27 ship date is imminent and on critical path.** Tasks due 5/22 have 5-day buffer before shipment deadline.
  - ⚠️ **Previous knowledge documented 2026-parts s0 build completed 5/19; current task is for 2025-parts build**, suggesting either distinct unit batches or rework cycle. Confirm Nate Straus' actual workload.

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

**Hardware Development Milestones:**

| Task | Owner | Due Date | Status | Notes |
|------|-------|----------|--------|-------|
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ COMPLETED 2026-05-08 (7 days late) | Firmware fix completed; downstream work unblocked. |
| **Rebuild BST s0 (platform rebuild)** | Nate Straus | 2026-05-15 | ✅ COMPLETED 2026-05-14 (1 day early) | Critical progress on schedule. |
| **Build 2 SHOW s0's using 2026 parts** | Nate Straus | 2026-07-17 | ✅ **COMPLETED 2026-05-19 (59 days early)** | Previous knowledge: shipped ahead of critical May 27 deadline. |
| **Build 2 SHOW tripods** | Nate Straus | 2026-05-22 | ✅ **COMPLETED 2026-05-19 (3 days early)** | Previous knowledge: shipped with s0 units ahead of schedule. |
| **Build 5 power switches with short pcb** | Nate Straus | 2026-05-21 | ✅ COMPLETED or CLOSED | Status unclear in current data; no longer listed as open task. |
| **Build up 2 SHOW s0's using 2025 parts - MUST SHIP MAY 27th** | Nate Straus | 2026-05-22 | ⏳ OPEN | **CRITICAL TASK.** Distinct from 2026-parts build completed 5/19. May indicate secondary unit production or rework. |
| **Ship S0s Models to NOAA (2 locations)** | Meredith O'hara Needham | 2026-05-22 | ⏳ OPEN | **CRITICAL SHIPMENT TASK.** Addresses 2 NOAA locations: **NOAA UASD (LCDR Nick Pawlenko, Flight Operations Office, 3450 Flightline Drive, Lakeland, FL 33811-2836)** and **NOAA UxSOC (LCDR Nick Pawlenko, 1315 East-West Highway, Silver Spring, MD area)**. |
| **Get 2025 and 2026 params files validated and in folder** | Maciej Stachura | 2026-06-30 | ✅ COMPLETED or CLOSED | Status unclear in current data; no longer listed as open task. |

## Task Summary

**Current Asana Status: 2 open tasks, 0 completed** (note: Asana project completion counter may not reflect overall project task completion; refer to detailed milestone table above for full picture)

**Open Tasks:**
1. **Build up 2 SHOW s0's using 2025 parts - MUST SHIP MAY 27th** | Nate Straus | Due 2026-05-22 | Status: OPEN
2. **Ship S0s Models to NOAA (2 locations)** | Meredith O'hara Needham | Due 2026-05-22 | Status: OPEN

**Task Distribution & Completion:**
-