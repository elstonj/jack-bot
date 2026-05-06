# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift
- **Timeline:** 
  - Project Start: 2026-07-31
  - Project Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
- **Status:** **ACTIVE — CRITICAL PHASE.** 4 of 6 invoices completed (Invoice 3 submitted 2026-05-01, 3 days early). **22 open tasks** across platform builds, firmware, QC, and kit assembly. Multiple **OVERDUE and APPROACHING OVERDUE** items with critical path impact to May 22–27 hardware ship dates.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, S0 builds, servo assembly)
  - Maciej Stachura (platform validation/testing, magnetic calibration)
  - Alex Lomis (strategic partnerships, NASA opportunities)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA
  - Background: SBIR Phase I (2018) and Phase II (2019–2020) collaboration; current IDIQ builds on prior partnership
- **Risk Signals:** 
  - 🚨 **CRITICAL OVERDUE:** "Add RH / Vaisala fix to PSNS code" (Jack Elston) **DUE 2026-05-01 — NOW PAST DUE.** No task closure visible.
  - 🚨 **APPROACHING OVERDUE (5 days):** "Figure out why S0-70 rolled over during CAT on 04-09" (Maciej Stachura) **DUE 2026-05-08.** 
  - 🚨 **CRITICAL MAY 22 DEADLINES (MUST SHIP MAY 27):**
    - "Build up 2 SHOW s0's using 2025 parts" (Nate Straus) — DUE 2026-05-22
    - "Build 2 show tripods" (Nate Straus) — DUE 2026-05-22
    - "QC at least one of each board" (Sam Hild) — DUE 2026-05-15
  - 🚨 **NATE STRAUS WORKLOAD BOTTLENECK:** 7 active tasks with critical path impact; 4 with firm deadlines (May 15–22). Risk of hardware delivery delay.
  - 🚨 **JACK ELSTON FIRMWARE DEPENDENCY:** Overdue RH/Vaisala fix blocks downstream QC/assembly work. Two firmware tasks (AP/PSNS finalization and deployment tube) due June 26 and May 29.
  - **Final system delivery deadline 2026-06-30:** ~4 weeks to pack full systems for NOAA after SHOW ship date.

## Key Deliverables & Milestones

**Deliverable:** 20 UAS units for NOAA with critical atmospheric measurement capabilities

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
| **Total** | **$483,000** | | |

**Hardware/Firmware/Validation Development Milestones:**
| Task | Owner | Due Date | Status | Priority | Notes |
|------|-------|----------|--------|----------|-------|
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | 🚨 **OVERDUE** | **CRITICAL** | Firmware fix blocking downstream QC/assembly. |
| **Figure out why S0-70 rolled over during CAT on 04-09** | Maciej Stachura | 2026-05-08 | ⏳ **APPROACHING OVERDUE** | HIGH | Validation milestone; 5 days past due. |
| **QC at least one of each board** | Sam Hild | 2026-05-15 | ⏳ Open | **CRITICAL** | Hardware validation gate; enables assembly flow. |
| **Rebuild BST s0 (currently partially disassembled)** | Nate Straus | 2026-05-15 | ⏳ Open | HIGH | Platform availability for testing. |
| **Build up 2 SHOW s0's using 2025 parts** | Nate Straus | 2026-05-22 | ⏳ Open | **CRITICAL** | **MUST SHIP MAY 27.** Controls primary delivery milestone. |
| **Build 2 show tripods** | Nate Straus | 2026-05-22 | ⏳ Open | **CRITICAL** | **MUST SHIP MAY 27 with S0's.** |
| **Finalize deployment tube firmware** | Jack Elston | 2026-05-29 | ⏳ Open | HIGH | Firmware finalization for deployment systems. |
| **Finish deployment tube board QCs** | Sam Hild | 2026-06-05 | ⏳ Open | HIGH | Hardware validation; enables kit assembly. |
| **Submit Invoice 4 of 6** | Meredith O'hara Needham | 2026-06-05 | ⏳ Open | HIGH | On track with prior schedule. |
| **Rebuild old BST s0 (2024 version)** | Nate Straus | 2026-06-19 | ⏳ Open | MEDIUM | Secondary platform rebuild for field operations. |
| **Begin kit assembly** | Sam Hild | 2026-06-19 | ⏳ Open | HIGH | Full system assembly phase; gated by board QCs. |
| **Finalize AP & PSNS firmware** | Jack Elston | 2026-06-26 | ⏳ Open | HIGH | Final firmware release for production units. |
| **Finish 2025 S0's (full system packed)** | Nate Straus | 2026-06-30 | ⏳ Open | **CRITICAL** | **FINAL DELIVERY GATE.** All 20 units must be packed and ready. |
| **Build up 2 SHOW s0's using 2026 parts** | Nate Straus | 2026-07-17 | ⏳ Open | HIGH | Secondary unit build; buffer capacity. |
| **Participate in magnetic calibration** | Maciej Stachura | 2026-07-01 | ⏳ Open | MEDIUM | Sensor calibration; late-stage activity. |
| **Submit Invoice 5 of 6** |