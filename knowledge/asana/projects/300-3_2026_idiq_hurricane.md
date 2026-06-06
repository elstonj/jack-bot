# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total IDIQ funding + $16,000 Delivery Order for 2 ground stations (approved 5/12/26) = **$499,000 total**
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - Background: SBIR Phase I (2018) and Phase II (2019–2020) collaboration; ongoing partnership since 2018
- **Timeline:** 
  - Project Start/Due: 2026-07-31 (final delivery deadline)
  - Invoice schedule: March 2026 – July 2026
  - Critical hardware ship date: May 27, 2026 (passed; hardware shipped early 5/19/26)
- **Status:** **ACTIVE — IN EXECUTION, CRITICAL URGENCY.** Hardware milestones delivered early (2 SHOW s0's and tripods shipped 5/19/26, ahead of 5/27 deadline). **🔴 TWO BLOCKING ISSUES DUE TOMORROW (6/5/26):**
  1. **Firmware finalization (Jack Elston) — overdue as of 6/4/26** — status unknown; gating Invoice 4 ($72k)
  2. **QC board validation completion (Sam Hild) — due 6/5/26** — critical path for hardware release
  3. **Communication continuity risk (5/29/26):** Nick Pawlenko transitioning to UxSOC HQ; reduced availability during field season. NOAA/UASD guidance (5/29/26) states BST must include alternative contacts for scheduling, foreign nationals, flight planning, and UAS/HX operations. **ACTION REQUIRED: Obtain complete list of backup NOAA contacts from Meredith O'hara Needham.** (Project note was truncated; full contact list not yet received.)
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software development) — **CRITICAL PATH, OVERDUE**
  - Sam Hild (QC, hardware validation, kit assembly) — **CRITICAL PATH, DUE TOMORROW**
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement, Gateworks board sourcing) — completed long-lead parts 6/1/26
  - Ben Busby (web-based controller development)
  - Nick Pawlenko (UxSOC liaison — **transitioning 5/29/26; reduced availability expected**)
- **Risk Signals:** 
  - 🔴 **CRITICAL/OVERDUE:** Firmware finalization (Jack Elston) due 2026-06-04 — **NOW OVERDUE; STATUS UNKNOWN.** Gating Invoice 4 ($72k, due 6/5/26) and all downstream hardware delivery and 25-unit production schedule.
  - 🔴 **CRITICAL/DUE TOMORROW (6/5/26):** Deployment tube board QC completion (Sam Hild) — gating Invoice 4 submission and hardware release to field.
  - 🔴 **CRITICAL/DUE TOMORROW (6/5/26):** Invoice 4 ($72k) submission due — blocked on firmware and QC completion.
  - ⚠️ **UNRESOLVED SOURCING:** Gateworks boards for 2 S0 ground stations (DO, $16k) — Josh Fromm asking on 5/28–5/29 whether BST has obtained boards yet. **NO OWNER or DUE DATE assigned to GCS build.** Field season imminent.
  - ⚠️ **UNASSIGNED/HIGH RISK:** 25 additional S0 units due 7/31/26 (24 for season + 4 for sasqwatch + 1 2025 carryover) — no build schedule documented; firmware and QC dependencies not yet cleared.
  - ⚠️ **Web-based controller (Ben Busby) due 7/31/26** — no progress visible; potential blocker for operator training.
  - ⚠️ **Operator Training due 7/31/26** — unassigned; depends on firmware, web controller, and hardware delivery.
  - ⚠️ **Communication continuity:** Nick Pawlenko's transition effective 5/29/26 may disrupt scheduling, foreign national clearances, flight planning. **Backup contact protocol not yet defined.**

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasqwatch + 1 leftover from 2025) + 2 rack-mount ground stations ($16k)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| **4 of 6** | **$72,000** | **2026-06-05** | 🔴 **CRITICAL — DUE TOMORROW; blocked on overdue firmware & QC** |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Upcoming |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Final |
| **Subtotal** | **$483,000** | | |
| **Ground Stations DO** | **$16,000** | **2026-05-12** | ⚠️ **Approved 5/12/26; sourcing/build status unclear** |
| **TOTAL** | **$499,000** | | |

**Hardware Development Milestones:**

| Task | Owner | Due Date | Status | Notes |
|------|-------|----------|--------|-------|
| Add RH / Vaisala fix to PSNS code | Jack Elston | 2026-05-01 | ✅ Completed 5/8/26 | Firmware fix complete; downstream work unblocked. |
| Rebuild BST s0 (platform rebuild) | Nate Straus | 2026-05-15 | ✅ Completed 5/14/26 | On schedule. |
| Ship 2 SHOW s0's + tripods | Meredith O'hara Needham / Nate Straus | 2026-05-22 | ✅ Completed 5/19/26 | Shipped ahead of 5/27 deadline. |
| Order long-lead parts (20+) | Josh Fromm | No due date | ✅ Completed 6/1/26 | Parts secured. |
| **Finalize deployment tube firmware** | **Jack Elston** | **2026-06-04** | 🔴 **OVERDUE — STATUS UNKNOWN** | **URGENT: Confirm completion immediately. Gating Invoice 4 ($72k, due 6/5/26), QC sign-off, and 25-unit production.** |
| **QC board validation / Finish deployment tube board QCs**