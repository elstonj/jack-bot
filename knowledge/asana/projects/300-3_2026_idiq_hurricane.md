# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift
- **Timeline:** 
  - Project Start: 2026-07-31
  - Project Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
- **Status:** Active — invoicing on schedule (3 of 6 invoices completed); hardware development and validation tasks in critical phase. **SHOW s0 demonstration units (2025 parts) must ship by May 27, 2026 — imminent deadline (~5 weeks away as of mid-April 2026).**
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, kit assembly, hardware validation)
  - Maciej Stachura (magnetometer calibration, platform validation/testing)
  - Nate Straus (platform rebuild/validation, SHOW demonstration unit builds)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - BST (whole team)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA
  - Background: SBIR Phase I (2018) and Phase II (2019–2020) collaboration; current IDIQ builds on prior partnership
- **Risk Signals:** 
  - **IMMEDIATE CRITICAL DEADLINE:** Nate Straus must ship 2 SHOW s0 units (2025 parts) + 2 tripods by **May 27, 2026** — only ~5 weeks away
  - **Platform stability issue under investigation:** Maciej Stachura investigating S0-70 rollover during CAT (Contained Altitude Test) on 2026-04-09; follow-up task due 2026-05-08 (before May 27 shipping deadline)
  - **Hardware/validation tasks now critical path:** 8+ open firmware, QC, assembly, and validation tasks with May–July deadlines
  - **Compressed timeline:** Project start and due date both listed as 2026-07-31 (final delivery/completion required by end of July)
  - **Magnetometer calibration in final month:** Maciej Stachura's mag cal task due 2026-07-01 (tight window before final delivery)
  - **Parallel build tracks:** Nate managing both 2025-parts SHOW build (May 27 deadline) and 2026-parts SHOW build (July 17 deadline) simultaneously with other firmware/QC work

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
| **Investigate S0-70 rollover during CAT** | Maciej Stachura | 2026-05-08 | ⏳ Open — **BLOCKING** |
| **Build 2 SHOW s0's using 2025 parts + ship** | Nate Straus | 2026-05-27 | ⏳ Open — **IMMINENT** |
| **Build 2 SHOW tripods** | Nate Straus | 2026-05-27 | ⏳ Open — **IMMINENT** |
| Finalize deployment tube firmware | Jack Elston | 2026-05-29 | ⏳ Open |
| Finish deployment tube board QCs | Sam Hild | 2026-06-05 | ⏳ Open |
| Begin kit assembly | Sam Hild | 2026-06-19 | ⏳ Open |
| Finalize AP & PSNS firmware | Jack Elston | 2026-06-26 | ⏳ Open |
| **Build 2 SHOW s0's using 2026 parts** | Nate Straus | 2026-07-17 | ⏳ Open |
| Participate in mag cal process | Maciej Stachura | 2026-07-01 | ⏳ Open |

## Task Summary
- **Total Tasks:** 12 (11 development/validation + 1 new investigation task)
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
  - **Maciej Stachura (Calibration/Validation):** 2 tasks — 0% completion
    - **Investigate S0-70 rollover during CAT** (due 2026-05-08) — **NEWLY CRITICAL**
    - Participate in mag cal process (due 2026-07-01)
- **Notable Patterns:**
  - **Nate Straus is primary bottleneck:** Manages 3 hardware build tasks spanning May–July; first two (SHOW 2025) must ship by May 27 with only ~5 weeks to build and test
  - **Platform stability issue now in critical path:** S0-70 rollover during testing suggests potential design or balance problem that must be resolved before May 27 shipping deadline
  - SHOW units are demonstration/validation platforms (