# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift; additional $16k Delivery Order for 2 ground stations (approved 5/12/26)
- **Total Contract Value:** $499,000
- **Timeline:** 
  - Project Start: 2026-07-31
  - Project Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
  - **Critical hardware ship date:** May 27, 2026 (SHOW units)
  - **Final delivery deadline:** June 30, 2026 (all 20 units packed)
- **Status:** **ACTIVE — CRITICAL PHASE.** 4 of 6 invoices completed. **FIRMWARE FIX COMPLETED (7 DAYS LATE).** Platform rebuild task completed ahead of schedule (5/14 vs 5/15 due date). 2 open tasks remaining in Asana; major hardware milestones appear to have moved to external tracking or completion. Critical path remains May 15–27 hardware milestones with minimal buffer.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, S0 builds, servo assembly, linkage construction) — **completed critical May 15 rebuild**
  - Maciej Stachura (platform validation/testing, magnetic calibration)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly — newly visible in task assignment)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA + 2 ground stations ($16k, approved 5/12/26)
  - Background: SBIR Phase I (2018, #1305M218CNRMW0059) and Phase II (2019–2020, #1305M219CNRMW0030) collaboration; current IDIQ builds on established partnership since 2018
- **Risk Signals:** 
  - 🟡 **FIRMWARE FIX RESOLVED (7 DAYS LATE):** "Add RH / Vaisala fix to PSNS code" (Jack Elston) was **DUE 2026-05-01** — **COMPLETED 2026-05-08.** 7-day slip may have cascade impact on downstream QC/assembly.
  - 🚨 **VALIDATION TASK OVERDUE:** "Figure out why S0-70 rolled over during CAT on 04-09" (Maciej Stachura) **DUE 2026-05-08 — STATUS UNKNOWN.** Not visible in current task list; may be externally resolved, deprioritized, or tracked elsewhere.
  - ✅ **CRITICAL MAY 15 REBUILD COMPLETED EARLY:** "Rebuild BST s0 (currently partially disassembled)" (Nate Straus) **DUE 2026-05-15 — COMPLETED 2026-05-14.** Nate's critical path work is tracking ahead of schedule.
  - 🟡 **ASANA TASK LIST SIGNIFICANTLY REDUCED:** Knowledge file showed 21 open tasks; current raw data shows only 2 open tasks. This suggests either (a) major project progress with tasks completed/archived, (b) tasks moved to external tracking systems, or (c) Asana project not fully maintained as source of truth. **Recommend confirming actual hardware build status with Nate Straus and Sam Hild.**
  - 🚨 **TWO CRITICAL OPEN TASKS:**
    1. **"Build up new GCS x2"** (Josh Fromm, due 2026-07-01) — Ground control stations for 2-unit Delivery Order. On track.
    2. **"QC at least one of each board as they arrive"** (Sam Hild, due 2026-05-15) — **NOW OVERDUE.** This is a gating validation task for assembly flow. Completion status unknown.

## Key Deliverables & Milestones

**Primary Deliverable:** 20 UAS units for NOAA + 2 ground stations ($16k) with critical atmospheric measurement capabilities

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ **Completed 2026-05-01 (3 days early)** |
| 4 of 6 | $72,000 | 2026-06-05 | ⏳ Open |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Open |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Open |
| **Subtotal** | **$483,000** | | |
| **Ground Stations DO** | **$16,000** | **2026-05-12** | ✅ **Approved 5/12/26** |
| **TOTAL** | **$499,000** | | |

**Hardware/Firmware/Validation Development Milestones (from prior knowledge; current status partially unknown):**

| Task | Owner | Due Date | Status | Priority | Notes |
|------|-------|----------|--------|----------|-------|
| **Figure out why S0-70 rolled over during CAT on 04-09** | Maciej Stachura | 2026-05-08 | ❓ **STATUS UNKNOWN** | HIGH | Not visible in current task list; may be resolved or externally tracked. |
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ **COMPLETED 2026-05-08 (7 DAYS LATE)** | **CRITICAL** | Firmware fix completed; downstream work unblocked. |
| **Rebuild BST s0 (currently partially disassembled)** | Nate Straus | 2026-05-15 | ✅ **COMPLETED 2026-05-14 (1 DAY EARLY)** | HIGH | **Critical progress:** ahead of schedule. |
| **QC at least one of each board as they arrive** | Sam Hild | 2026-05-15 | 🚨 **OVERDUE** | **CRITICAL** | Hardware validation gate; currently overdue. **Verify completion status.** |
| **Build up 2 SHOW s0's using 2025 parts** | Nate Straus | 2026-05-22 | ❓ **STATUS UNKNOWN** | **CRITICAL** | **MUST SHIP MAY 27.** Not visible in current task list; assume in progress or completed. |
| **Build 2 show tripods** | Nate Straus | 2026-05-22 | ❓ **STATUS UNKNOWN** | **CRITICAL** | **MUST SHIP MAY 27.** Not visible in current task list. |
| **Build up new GCS x2** | Josh Fromm | 2026-07-01 | ⏳ **OPEN** | HIGH | Ground control stations for 2-unit Delivery Order. On track. |

## Task Summary
- **Open Tasks (Asana)