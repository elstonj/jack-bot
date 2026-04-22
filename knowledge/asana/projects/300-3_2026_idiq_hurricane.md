# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift
- **Timeline:** 
  - Project Start: 2026-07-31
  - Project Due: 2026-07-31
  - Invoice schedule: March 2026 – July 2026
- **Status:** Active — invoicing on schedule (3 of 6 invoices completed); hardware development and validation tasks in progress
- **Team Members:** 
  - Meredith O'hara Needham (project owner, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, kit assembly, hardware validation)
  - Maciej Stachura (magnetometer calibration)
  - Nate Straus (platform rebuild/validation)
  - BST (whole team)
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - 20 UAS units for NOAA
- **Risk Signals:** 
  - **Hardware/validation tasks now critical path:** 8 open firmware, QC, assembly, and validation tasks with near-term deadlines (May–July 2026)
  - **Compressed timeline:** Project start and due date both listed as 2026-07-31 (constraint is final delivery/completion by end of July)
  - **Platform rebuild date discrepancy:** Asana shows task due 2026-05-29, but existing knowledge file lists 2026-05-15 as critical path date for Nate Straus BST s0 rebuild. **Verify actual deadline with Nate.**
  - **Magnetometer calibration in final month:** Maciej Stachura's mag cal task due 2026-07-01 (tight window before final delivery)

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
| Rebuild BST s0 (currently partially disassembled) | Nate Straus | 2026-05-15 (planned) / 2026-05-29 (Asana) | ⏳ Open — **DATE CONFLICT** |
| Finalize deployment tube firmware | Jack Elston | 2026-05-29 | ⏳ Open |
| Finish deployment tube board QCs | Sam Hild | 2026-06-05 | ⏳ Open |
| Begin kit assembly | Sam Hild | 2026-06-19 | ⏳ Open |
| Finalize AP & PSNS firmware | Jack Elston | 2026-06-26 | ⏳ Open |
| Participate in mag cal process | Maciej Stachura | 2026-07-01 | ⏳ Open |

## Task Summary
- **Total Tasks:** 1 open in current Asana view (other 7 tasks visible in previous data export but not in raw task list — possible sync lag or filtering)
- **Tasks by Assignee (from existing knowledge + current data):**
  - **Jack Elston (Firmware/Software):** 3 tasks — 0% completion
    - Add RH / Vaisala fix to PSNS code (due 2026-05-01)
    - Finalize deployment tube firmware (due 2026-05-29)
    - Finalize AP & PSNS firmware (due 2026-06-26)
  - **Sam Hild (QC/Assembly):** 3 tasks — 0% completion
    - QC at least one of each board as they arrive (due 2026-05-01)
    - Finish deployment tube board QCs (due 2026-06-05)
    - Begin kit assembly (due 2026-06-19)
  - **Nate Straus (Platform Build/Validation):** 1 task — 0% completion
    - **Rebuild old BST s0 (2024 version) to make fully functional again** (due 2026-05-29 per Asana; planned 2026-05-15 per existing knowledge)
  - **Maciej Stachura (Calibration):** 1 task — 0% completion
    - Participate in mag cal process (due 2026-07-01)
- **Notable Patterns:**
  - Only 1 task currently visible in raw Asana export; other 7 from knowledge file may be in a different project view or list
  - Firmware finalization staggered May–June to support QC and assembly workflow
  - Platform rebuild task (Nate Straus) sits between firmware start and QC completion — suggests BST s0 is test/validation platform for firmware validation
  - Magnetometer calibration is final validation gate before delivery (due 2026-07-01, just 30 days before project close)
  - Sam Hild's QC/assembly tasks dependent on Jack Elston's firmware milestones

## Recent Activity
- **2026-04-20:** Alex Lomis shared NASA RFI link on hurricane ET call — recommended by NASA team and Joe for potential follow-on opportunity: https://sam.gov/workspace/contract/opp/d7e641e7fc4d4dfbbd2f5cd62f17758f/view (business development signal; not part of current NOAA delivery)
- **2026-04-17:** Alex Lomis shared same NASA RFI link after hurricane engineering team call
- **2026-04-15:** Invoice 2 of 6 ($54,000) + Travel ($18k) submitted — completed on time
- **2026-03-13:** Invoice 1 of 6 ($36,000) submitted — completed on time
- **Upcoming Critical Deadlines (IMMINENT):**
  - **2026-05-01:** Jack Elston firmware fix + Sam Hild board QC (imminent — ~2 weeks from data date)
  - **2026-05-14:** Invoice 3 of 6 ($54,000) due
  - **2026-05-15/29:** Nate Straus BST s0 rebuild due (**CONFLICTING DATES — clarify with Nate**)
  - **2026-06-05–06-26:** QC completion and firmware finalization window
  - **2026-07-01:** Magnetometer calibration process (