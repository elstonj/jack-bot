# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift; additional $16k Delivery Order for 2 ground stations (approved 5/12/26)
- **Timeline:** 
  - Project Start: 2026-07-31
  - Project Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
  - **Critical hardware ship date:** May 27, 2026 (SHOW units)
  - **Final delivery deadline:** June 30, 2026 (all 20 units packed)
- **Status:** **ACTIVE — CRITICAL PHASE.** 4 of 6 invoices completed. **FIRMWARE FIX COMPLETED (7 DAYS LATE).** One validation task overdue. Critical path heavily dependent on May 15–27 hardware milestones with minimal buffer. 21 open tasks with significant work concentration on Nate Straus.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, S0 builds, servo assembly, linkage construction) — **CRITICAL BOTTLENECK**
  - Maciej Stachura (platform validation/testing, magnetic calibration)
  - Alex Lomis (strategic partnerships, NASA opportunities)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA + 2 ground stations ($16k, approved 5/12/26)
  - Background: SBIR Phase I (2018, #1305M218CNRMW0059) and Phase II (2019–2020, #1305M219CNRMW0030) collaboration; current IDIQ builds on established partnership since 2018
- **Risk Signals:** 
  - 🟡 **FIRMWARE FIX RESOLVED (7 DAYS LATE):** "Add RH / Vaisala fix to PSNS code" (Jack Elston) was **DUE 2026-05-01** — **COMPLETED 2026-05-08.** This was a critical blocker for downstream QC/assembly; 7-day slip may have cascade impact on May 15–22 milestone tasks.
  - 🚨 **VALIDATION TASK OVERDUE:** "Figure out why S0-70 rolled over during CAT on 04-09" (Maciej Stachura) **DUE 2026-05-08 — NOW OVERDUE.** Platform robustness validation.
  - 🚨 **CRITICAL MAY 22–27 BOTTLENECK:** Multiple hard-deadline platform builds and tripod assembly tasks ("Build up 2 SHOW s0's using 2025 parts," "Build 2 show tripods") **MUST SHIP MAY 27.** Firmware slip compressed timeline.
  - 🚨 **NATE STRAUS WORKLOAD BOTTLENECK:** 13 of 21 open tasks assigned to Nate Straus, including all critical-path May 15–June 30 hardware milestones (platform rebuilds, servo assembly, linkage construction, system packing). **Minimal contingency capacity if delays cascade.**
  - 🚨 **FINAL DELIVERY GATE (JUNE 30):** "Finish 2025 S0's (full system packed)" is final gating task for all 20 units. Dependent on multiple prior QC, firmware, and assembly milestones with tight sequencing.
  - **8 tasks with no due dates** assigned to Nate (servo wiring, linkage construction, tray assembly) — suggest unscheduled subtasks or flexible scheduling; may indicate scope creep or incomplete planning.

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

**Hardware/Firmware/Validation Development Milestones:**

| Task | Owner | Due Date | Status | Priority | Notes |
|------|-------|----------|--------|----------|-------|
| **Figure out why S0-70 rolled over during CAT on 04-09** | Maciej Stachura | 2026-05-08 | 🚨 **OVERDUE** | HIGH | Platform robustness validation; unblocks further testing. |
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ **COMPLETED 2026-05-08 (7 DAYS LATE)** | **CRITICAL** | Firmware fix was blocking downstream QC/assembly. Late completion cascaded to hardware milestones. |
| **Rebuild BST s0 (currently partially disassembled)** | Nate Straus | 2026-05-15 | ⏳ Open | HIGH | Platform availability for testing; unblocks assembly validation. |
| **QC at least one of each board as they arrive** | Sam Hild | 2026-05-15 | ⏳ Open | **CRITICAL** | Hardware validation gate; enables assembly flow. Dependent on firmware fix completion. |
| **Build up 2 SHOW s0's using 2025 parts** | Nate Straus | 2026-05-22 | ⏳ Open | **CRITICAL** | **MUST SHIP MAY 27.** Primary delivery milestone; controls secondary unit availability. |
| **Build 2 show tripods** | Nate Straus | 2026-05-22 | ⏳ Open | **CRITICAL** | **MUST SHIP MAY 27 with S0's.** Hardware completeness gate. |
| **Finalize deployment tube firmware** | Jack Elston | 2026-05-29 | ⏳ Open | HIGH | Firmware finalization for deployment systems. |
| **Finish deployment tube board QCs** | Sam Hild | 2026-06-05 | ⏳ Open | HIGH | Hardware validation; enables full kit assembly phase. |
| **Submit Invoice 4 of 6 ($72k)** | Meredith O'hara Needham | 2026-06-05 | ⏳ Open | HIGH | On schedule. |
| **Rebuild old BST s0 (2024 version)** | Nate Straus | 2026-06-19