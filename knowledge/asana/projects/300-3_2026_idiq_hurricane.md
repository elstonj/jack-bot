# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift
- **Timeline:** 
  - Project Start: 2026-07-31
  - Project Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
- **Status:** Active — invoicing on schedule (3 of 6 invoices completed); hardware development and validation tasks in progress. **Critical hardware build phase underway: Nate Straus now building demonstration units (SHOW s0's) with aggressive shipping deadline (May 27).**
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, kit assembly, hardware validation)
  - Maciej Stachura (magnetometer calibration)
  - Nate Straus (platform rebuild/validation, **now also building SHOW demonstration units**)
  - BST (whole team)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA
  - Background: SBIR Phase I (2018) and Phase II (2019–2020) collaboration; current IDIQ builds on prior partnership
- **Risk Signals:** 
  - **IMMEDIATE CRITICAL DEADLINE:** Nate Straus must ship 2 SHOW s0 units (2025 parts) + 2 tripods by **May 27, 2026** — only ~5 weeks away (assuming data date ~mid-May)
  - **Hardware/validation tasks now critical path:** 8+ open firmware, QC, assembly, and validation tasks with May–July deadlines
  - **Compressed timeline:** Project start and due date both listed as 2026-07-31 (final delivery/completion required by end of July)
  - **Platform rebuild date discrepancy:** Previous knowledge file noted conflicting Nate Straus rebuild date (2026-05-15 vs. 2026-05-29 in Asana). **New task data shows May 27 SHOW unit shipping deadline — appears prior rebuild task has been superseded by SHOW build tasks.**
  - **Magnetometer calibration in final month:** Maciej Stachura's mag cal task due 2026-07-01 (tight window before final delivery)
  - **Parallel build tracks:** Nate now managing both 2025-parts SHOW build (May 27 deadline) and 2026-parts SHOW build (July 17 deadline) simultaneously with other firmware/QC work

## Key Deliverables & Milestones
**Deliverable:** 20 UAS units for NOAA with critical atmospheric measurement capabilities

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed (2026-03-13) |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed (2026-04-15) |
| Travel ($18k) | $18,000 | 2026-04-15 | ✅ Completed (2026-04-15) |
| 3 of 6 | $54,000 | 2026-05-14 | ⏳ Open |
| 4 of 6 | $72,000 | 2026-06-15 | ⏳ Open |
| 5 of 6 | $72,000 | 2026-07-15 | ⏳ Open |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Open |
| **Total** | **$483,000** | | |

**Hardware/Firmware/Validation Development Milestones:**
| Task | Owner | Due Date | Status |
|------|-------|----------|--------|
| Add RH / Vaisala fix to PSNS code | Jack Elston | 2026-05-01 | ⏳ Open |
| QC at least one of each board as they arrive | Sam Hild | 2026-05-01 | ⏳ Open |
| **Build 2 SHOW s0's using 2025 parts + ship** | Nate Straus | 2026-05-27 | ⏳ Open — **IMMINENT** |
| **Build 2 SHOW tripods** | Nate Straus | 2026-05-27 | ⏳ Open — **IMMINENT** |
| Finalize deployment tube firmware | Jack Elston | 2026-05-29 | ⏳ Open |
| Finish deployment tube board QCs | Sam Hild | 2026-06-05 | ⏳ Open |
| Begin kit assembly | Sam Hild | 2026-06-19 | ⏳ Open |
| Finalize AP & PSNS firmware | Jack Elston | 2026-06-26 | ⏳ Open |
| **Build 2 SHOW s0's using 2026 parts** | Nate Straus | 2026-07-17 | ⏳ Open |
| Participate in mag cal process | Maciej Stachura | 2026-07-01 | ⏳ Open |

## Task Summary
- **Total Tasks:** 11 identified (3 newly visible SHOW build tasks + 8 from existing knowledge file)
- **Tasks by Assignee:**
  - **Nate Straus (Platform Build/Demonstration):** 3 tasks — 0% completion
    - **Build 2 SHOW s0's using 2025 parts** (due 2026-05-27) — **CRITICAL, IMMINENT**
    - **Build 2 SHOW tripods** (due 2026-05-27) — **CRITICAL, IMMINENT**
    - Build 2 SHOW s0's using 2026 parts (due 2026-07-17)
  - **Jack Elston (Firmware/Software):** 3 tasks — 0% completion
    - Add RH / Vaisala fix to PSNS code (due 2026-05-01)
    - Finalize deployment tube firmware (due 2026-05-29)
    - Finalize AP & PSNS firmware (due 2026-06-26)
  - **Sam Hild (QC/Assembly):** 3 tasks — 0% completion
    - QC at least one of each board as they arrive (due 2026-05-01)
    - Finish deployment tube board QCs (due 2026-06-05)
    - Begin kit assembly (due 2026-06-19)
  - **Maciej Stachura (Calibration):** 1 task — 0% completion
    - Participate in mag cal process (due 2026-07-01)
- **Notable Patterns:**
  - **Nate Straus is now primary bottleneck:** Manages 3 hardware build tasks spanning May–July; first two (SHOW 2025) must ship by May 27 with only ~5 weeks to build and test
  - SHOW units appear to be demonstration/validation platforms (separate from final 20-unit delivery)
  - Firmware finalization staggered May–June to support QC and assembly workflow
  - Magnetometer calibration is final validation gate before delivery
  - Sam Hild's QC/assembly tasks dependent on Jack Elston's firmware milestones

## Recent Activity
- **NEW (raw data):** Nate Straus assigned 3 hardware build tasks with aggressive May 27 shipping deadline for SHOW demonstration units — represents shift from prior "platform rebuild" framing