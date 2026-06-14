# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total IDIQ funding + $16,000 Delivery Order for 2 ground stations (approved 5/12/26) = **$499,000 total**
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084
  - Background: SBIR Phase I (2018) and Phase II (2019–2020) collaboration; ongoing partnership since 2018
- **Timeline:** 
  - Project Start/Due: 2026-07-31 (final delivery deadline)
  - Invoice schedule: March 2026 – July 2026
  - Critical hardware ship date: May 27, 2026 (passed; hardware shipped early 5/19/26)
- **Status:** **🔴 ACTIVE — CRITICAL URGENCY, MULTIPLE BLOCKING ISSUES OVERDUE/DUE IMMEDIATELY (as of 6/5/26).** Hardware milestones delivered early (2 SHOW s0's and tripods shipped 5/19/26). Field season imminent.
  - **BLOCKING ISSUES (6/4–6/5/26):**
    1. **Firmware finalization (Jack Elston) — OVERDUE as of 6/4/26** — deployment tube firmware due 6/4/26 (now past due); AP & PSNS firmware due 6/26/26. Gating Invoice 4 ($72k, due 6/5/26) and hardware release.
    2. **QC board validation (Sam Hild) — DUE 6/5/26** — deployment tube board QC critical path for hardware release. Begin kit assembly due 6/19/26.
    3. **Gateworks boards sourcing (Josh Fromm) — UNRESOLVED** — Josh requested confirmation 5/28 & 5/29/26. **No documented response from Meredith or procurement.** Status UNKNOWN. Blocks GCS assembly (due 7/1/26).
    4. **Communication continuity:** Nick Pawlenko transitioned to UxSOC HQ effective 5/29/26. **NOAA backup contact protocol INCOMPLETE** — project note from 5/29/26 indicates full contact list was being drafted but transmission was truncated mid-sentence. BST has **NOT YET received complete backup contacts from NOAA/UASD.**
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software) — **CRITICAL PATH, DEPLOYMENT TUBE FIRMWARE OVERDUE (6/4/26); AP & PSNS DUE 6/26/26**
  - Sam Hild (QC, hardware validation, kit assembly) — **CRITICAL PATH, DEPLOYMENT TUBE QC DUE 6/5/26; KIT ASSEMBLY DUE 6/19/26**
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction, power switches)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation, failure analysis)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts, Gateworks board sourcing) — **URGENT: requested board status 5/28–5/29/26; no documented response; GCS build due 7/1/26**
  - Ben Busby (web-based controller development) — due 7/31/26
  - Nick Pawlenko (UxSOC liaison — **transitioned 5/29/26; reduced availability; backup protocol PENDING**)
- **Risk Signals:** 
  - 🔴 **CRITICAL/OVERDUE:** Deployment tube firmware (Jack Elston) due 6/4/26 — **NOW OVERDUE; STATUS UNKNOWN.** Blocks Invoice 4 ($72k), hardware release, and production schedule. AP & PSNS firmware due 6/26/26.
  - 🔴 **CRITICAL/DUE 6/5/26:** Deployment tube board QC (Sam Hild) — blocks Invoice 4 submission and hardware release.
  - 🔴 **CRITICAL/DUE 6/5/26:** Invoice 4 ($72k) — blocked on firmware and QC completion. **Meredith cannot submit without passing these gates.**
  - 🔴 **UNRESOLVED/URGENT:** Gateworks boards for 2 S0 ground stations ($16k DO) — Josh Fromm requested confirmation **5/28 & 5/29/26. NO DOCUMENTED RESPONSE.** GCS build due 7/1/26 (26 days away); field season imminent. **Meredith or procurement must confirm order status immediately.**
  - ⚠️ **PRODUCTION SCHEDULE UNDEFINED:** 25 additional S0 units (24 season + 4 sasqwatch + 1 2025 carryover + 1 refurb) due 7/31/26 — most tasks unassigned; no build schedule documented; firmware and QC dependencies not cleared. Kit assembly (Sam Hild) due 6/19/26 is first production gate.
  - ⚠️ **Overdue task:** S0-70 rollover investigation (Maciej Stachura) due 5/8/26 — **now overdue.** May indicate airframe/sensor scaling issues affecting fleet. Related: "S0 acc scaling is 8m/s/s" task (Jack Elston) unscheduled — may be root cause or follow-up.
  - ⚠️ **Web-based controller (Ben Busby) due 7/31/26** — no visible progress; delivery date critical for operator training.
  - ⚠️ **Operator Training due 7/31/26** — unassigned; depends on firmware, web controller, and hardware validation.
  - ⚠️ **Communication risk:** Nick's 5/29/26 transition may disrupt scheduling, foreign national clearances, flight planning. **Backup contact protocol from NOAA/UASD NOT YET RECEIVED** — note was truncated mid-sentence; BST must request completion immediately.
  - ⚠️ **Power switches overdue:** "Build 5 power switches with short pcb" (Nate Straus) due 5/21/26 — now overdue; dependency unclear but may block kit assembly.

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasqwatch + 1 leftover from 2025 + 1 refurb from clear air testing) + 2 rack-mount ground stations ($16k DO)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| **4 of 6** | **$72,000** | **2026-06-05** | 🔴 **CRITICAL — DUE TODAY/OVERDUE; blocked on overdue firmware & QC** |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Upcoming |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Final |
| **