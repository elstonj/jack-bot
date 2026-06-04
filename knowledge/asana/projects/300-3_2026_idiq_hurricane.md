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
- **Status:** **ACTIVE — IN EXECUTION.** Hardware milestones delivered early (2 SHOW s0's and tripods shipped 5/19/26, ahead of 5/27 deadline). ⚠️ **CRITICAL COMMUNICATION CONTINUITY ISSUE (5/29/26):** Nick Pawlenko (UxSOC liaison) transitioning to UxSOC headquarters role; may have limited availability. NOAA/UASD guidance issued: **BST must include alternative contacts for scheduling, foreign nationals, flight planning, and UAS/HX operations** to prevent communication gaps during field season. **ACTION REQUIRED: Obtain complete list of backup NOAA contacts from Meredith O'hara Needham.** Project notes indicate guidance text was cut off mid-sentence in raw data; complete contact list missing.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software development)
  - Sam Hild (QC, hardware validation, kit assembly)
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts procurement) — completed long-lead parts 6/1/26
  - Ben Busby (web-based controller development)
  - Nick Pawlenko (UxSOC liaison — **transitioning; reduced availability expected**)
- **Risk Signals:** 
  - ⚠️ **OVERDUE/CRITICAL PATH:** Firmware task (Jack Elston) due 2026-06-04 — **must complete immediately** to unblock Invoice 4 ($72k, due 6/5/26) and downstream hardware delivery.
  - ⚠️ **OVERDUE/CRITICAL PATH:** QC board validation (Sam Hild) due 2026-06-04 — **must complete immediately** to support Invoice 4 submission and hardware validation gates.
  - ⚠️ **Build 2 x rack-mount GCS: UNASSIGNED with no due date.** High risk given that 2 ground stations ($16k DO) were approved 5/12/26 and field season is imminent.
  - ⚠️ **25 additional S0 units due 7/31/26** — includes 24 for 2026 season + 4 for sasqwatch + 1 leftover from 2025. **Owner(s) unclear in current task list; no build schedule documented.** High risk given compressed timeline and firmware dependencies.
  - ⚠️ **Web-based controller due 7/31/26** (Ben Busby) — no progress visible in current task list; potential blocker for operator training.
  - ⚠️ **Operator Training due 7/31/26** — unassigned; depends on firmware, web controller, and hardware delivery.
  - ⚠️ **Communication continuity:** Nick Pawlenko's transition to UxSOC HQ may disrupt scheduling, foreign national clearances, flight planning, and UAS operations coordination. **ACTION REQUIRED: Establish backup contact protocol with NOAA team immediately per 5/29/26 guidance.**

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasqwatch + 1 leftover from 2025) + 2 rack-mount ground stations ($16k)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| 4 of 6 | $72,000 | 2026-06-05 | ⏳ **Approaching** — gated on firmware & QC |
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
| **Finalize deployment tube firmware** | Jack Elston | 2026-06-04 | ⚠️ **OPEN — CRITICAL PATH** | **Gating Invoice 4 ($72k, due 6/5/26) and all downstream hardware builds. Status requires immediate verification.** |
| **QC board validation** | Sam Hild | 2026-06-04 | ⚠️ **OPEN — CRITICAL PATH** | **Validate assembly as boards arrive. Critical for Invoice 4 and hardware validation gates. Status requires immediate verification.** |
| **Build 2 x rack-mount GCS** | **UNASSIGNED** | No due date | ⏳ OPEN | **High risk — no owner assigned. Ground stations DO ($16k) approved 5/12/26; field season imminent. Assign immediately and set due date.** |
| **Deliver 24 S0 for 2026 season (incl. 4 sasqwatch)** | **UNASSIGNED** | 2026-07-31 | 