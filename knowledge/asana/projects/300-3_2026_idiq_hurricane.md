# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift + $16,000 Delivery Order for 2 ground stations (approved 5/12/26) = **$499,000 total**
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - Background: SBIR Phase I (2018, #1305M218CNRMW0059) and Phase II (2019–2020, #1305M219CNRMW0030) collaboration; ongoing partnership since 2018
- **Timeline:** 
  - Project Start/Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
  - **Critical hardware ship date:** May 27, 2026
  - **Final delivery deadline:** June 30, 2026
- **Status:** **ACTIVE — BUT DATA INCONSISTENCY DETECTED.** Previous knowledge indicated 2 critical tasks due 5/22/26 in OPEN state with imminent May 27 ship deadline. New raw data shows 4 completely different OPEN tasks (all unassigned, no due dates) related to broader S0 production (20 units for 2026, 4 for Sasquatch, 1 for 2025 needs, 1 refurb from testing). **This suggests either:** (a) Asana project structure changed; (b) previous critical May 2026 tasks were completed/closed and new production phase tasks added; or (c) data sources are misaligned. **Action needed: Clarify current project state with Meredith O'hara Needham — are May 2026 critical shipments complete?**
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction, power switch builds)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement)
- **Risk Signals:** 
  - ⚠️ **DATA INCONSISTENCY:** Previous knowledge documented critical May 22, 2026 tasks (2 SHOW s0 builds with 2025 parts, shipment to NOAA) in OPEN state. New data shows no tasks with May 2026 due dates; instead 4 unassigned production tasks with no due dates.
  - ⚠️ **All 4 open tasks are UNASSIGNED.** This is unusual and requires clarification — are these placeholder/parent tasks, or is ownership genuinely unclear?
  - ⚠️ **No due dates on new open tasks.** This breaks tracking against the 7/31/26 project end date and invoice milestones.

## Key Deliverables & Milestones

**Primary Deliverable:** 20 UAS units for NOAA + 2 ground stations ($16k)

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

**Hardware Development Milestones (from previous knowledge):**

| Task | Owner | Due Date | Status | Notes |
|------|-------|----------|--------|-------|
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ COMPLETED 2026-05-08 | Firmware fix completed; downstream work unblocked. |
| **Rebuild BST s0 (platform rebuild)** | Nate Straus | 2026-05-15 | ✅ COMPLETED 2026-05-14 | Critical progress on schedule. |
| **Build 2 SHOW s0's using 2026 parts** | Nate Straus | 2026-07-17 | ✅ **COMPLETED 2026-05-19** | Shipped ahead of May 27 deadline. |
| **Build 2 SHOW tripods** | Nate Straus | 2026-05-22 | ✅ **COMPLETED 2026-05-19** | Shipped with s0 units ahead of schedule. |

## Task Summary

**Current Asana Status: 4 open tasks (all unassigned, no due dates)**

**Open Tasks (New Data):**
1. **Build 20x S0 for 2026** | Unassigned | No due date | Status: OPEN
2. **Build 4x S0 for sasquatch** | Unassigned | No due date | Status: OPEN
3. **Build 1x S0 to satisfy 2025 delivery needs** | Unassigned | No due date | Status: OPEN
4. **Refurbish 1x S0 from clear air testing** | Unassigned | No due date | Status: OPEN

**Notable Patterns:**
- **All tasks unassigned:** Requires clarification whether these are parent/summary tasks or genuinely unowned work items.
- **No due dates:** Breaks tracking against project milestones and invoice schedule. Should be assigned and dated.
- **Production totals:** 20 (2026) + 4 (Sasquatch) + 1 (2025 needs) + 1 (refurb) = 26 units total in backlog — exceeds 20-unit NOAA contract by 6 units (likely related projects or internal builds).

## Recent Activity

**Data Conflict Detected:**
- Previous knowledge file referenced May 2026 as critical phase with 2 high-priority tasks due 5/22 (Nate Straus s0 builds and Meredith O'hara Needham shipment).
- New raw data shows no May 2026 tasks; instead shows 4 unassigned, undated production tasks with broader scope (2026 batch, Sasquatch, 2025 backlog, refurbishment).
- **Possible interpretation:** Critical May 2026 milestones (2 SHOW s0's with 2025 parts, shipment to NOAA) were completed or closed out and are no longer appearing in open task list. Current Asana reflects next production phase (20-unit 2026 build, other platform work).

**Recommendation:** Contact Meredith O'hara Needham to confirm:
1. Status of May 27, 2026 shipment to NOAA (UASD Lakeland + UxSOC Silver Spring).
2. Whether previous critical