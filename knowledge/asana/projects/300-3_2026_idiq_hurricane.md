# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total funding to Black Swift + $16,000 Delivery Order for 2 ground stations (approved 5/12/26) = **$499,000 total**
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (invoice against this number)
  - Background: SBIR Phase I (2018) and Phase II (2019–2020) collaboration; ongoing partnership since 2018
- **Timeline:** 
  - Project Start/Due: 2026-07-31 (final delivery deadline)
  - Invoice schedule: March 2026 – July 2026
  - Critical hardware ship date: May 27, 2026 (passed; hardware shipped early 5/19/26)
- **Status:** **ACTIVE — IN EXECUTION, HIGH URGENCY.** Hardware milestones delivered early (2 SHOW s0's and tripods shipped 5/19/26, ahead of 5/27 deadline). ⚠️ **CRITICAL BLOCKING ISSUES — OVERDUE:**
  - Firmware finalization (Jack Elston) due 6/4/26 — **NOW OVERDUE** — gating Invoice 4 ($72k, due 6/5/26)
  - QC validation (Sam Hild) due 6/4/26 — **NOW OVERDUE** — must complete immediately
  - Board QC follow-up (Sam Hild) due 6/5/26 — approaching deadline
  - **COMMUNICATION CONTINUITY RISK (5/29/26):** Nick Pawlenko (UxSOC liaison) transitioning to UxSOC headquarters role; may have limited availability during field season. NOAA/UASD guidance (5/29/26) states BST must include alternative contacts for scheduling, foreign nationals, flight planning, and UAS/HX operations. **ACTION REQUIRED: Obtain complete list of backup NOAA contacts from Meredith O'hara Needham.** (Project note was truncated mid-sentence in source data; full contact list not yet received.)
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software development) — **CRITICAL PATH, OVERDUE**
  - Sam Hild (QC, hardware validation, kit assembly) — **CRITICAL PATH, OVERDUE**
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement) — completed long-lead parts 6/1/26
  - Ben Busby (web-based controller development)
  - Nick Pawlenko (UxSOC liaison — **transitioning; reduced availability expected**)
- **Risk Signals:** 
  - 🔴 **CRITICAL/OVERDUE:** Firmware finalization (Jack Elston) due 2026-06-04 — **STATUS UNKNOWN; CONFIRM IMMEDIATELY.** Gating Invoice 4 ($72k, due 6/5/26) and all downstream hardware delivery.
  - 🔴 **CRITICAL/OVERDUE:** QC board validation (Sam Hild) due 2026-06-04 — **STATUS UNKNOWN; CONFIRM IMMEDIATELY.** Gating Invoice 4 and hardware validation gates.
  - ⚠️ **APPROACHING:** Board QC completion (Sam Hild) due 2026-06-05 (same day as Invoice 4 deadline).
  - ⚠️ **UNASSIGNED/HIGH RISK:** Build 2 x rack-mount GCS (ground stations DO, $16k approved 5/12/26) — no owner, no due date set. Field season imminent.
  - ⚠️ **UNASSIGNED/HIGH RISK:** 25 additional S0 units due 7/31/26 (24 for season + 4 for sasqwatch + 1 2025 carryover) — no build schedule documented; firmware and QC dependencies not yet cleared.
  - ⚠️ **Web-based controller (Ben Busby) due 7/31/26** — no progress visible; potential blocker for operator training.
  - ⚠️ **Operator Training due 7/31/26** — unassigned; depends on firmware, web controller, and hardware delivery.
  - ⚠️ **Communication continuity:** Nick Pawlenko's transition may disrupt scheduling, foreign national clearances, flight planning coordination. Backup contact protocol needed immediately.

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasqwatch + 1 leftover from 2025) + 2 rack-mount ground stations ($16k)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| 4 of 6 | $72,000 | 2026-06-05 | 🔴 **CRITICAL — Due tomorrow; gated on overdue firmware & QC tasks** |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Due later |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Due at project end |
| **Subtotal** | **$483,000** | | |
| **Ground Stations DO** | **$16,000** | **2026-05-12** | ✅ **Approved 5/12/26** |
| **TOTAL** | **$499,000** | | |

**Hardware Development Milestones:**

| Task | Owner | Due Date | Status | Notes |
|------|-------|----------|--------|-------|
| **Add RH / Vaisala fix to PSNS code** | Jack Elston | 2026-05-01 | ✅ COMPLETED 2026-05-08 | Firmware fix completed; downstream work unblocked. |
| **Rebuild BST s0 (platform rebuild)** | Nate Straus | 2026-05-15 | ✅ COMPLETED 2026-05-14 | Critical progress on schedule. |
| **Ship 2 SHOW s0's + tripods** | Meredith O'hara Needham / Nate Straus | 2026-05-22 | ✅ **COMPLETED 2026-06-01** | Shipped ahead of 5/27 deadline. |
| **Order long-lead parts (20+)** | Josh Fromm | No due date | ✅ **COMPLETED 2026-06-01** | Parts procurement secured. |
| **Finalize deployment tube firmware** | Jack Elston | 2026-06-04 | 🔴 **OVERDUE — STATUS UNKNOWN** | **URGENT: Confirm completion status immediately. Gating Invoice 4 ($72k, due 6/5/26) and all downstream hardware builds.** |
| **QC board validation** | Sam Hild | 2026-06-04 |