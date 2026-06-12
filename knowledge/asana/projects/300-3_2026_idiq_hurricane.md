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
    1. **Firmware finalization (Jack Elston) — OVERDUE as of 6/4/26** — gating Invoice 4 ($72k, due 6/5/26)
    2. **QC board validation (Sam Hild) — DUE 6/5/26** — critical path for hardware release
    3. **Gateworks boards sourcing (Josh Fromm) — UNRESOLVED** — Josh requesting confirmation (5/28, 5/29/26); **no response documented; status UNKNOWN**
    4. **Communication continuity:** Nick Pawlenko transitioned to UxSOC HQ effective 5/29/26. **NOAA backup contact protocol incomplete** — project note from 5/29/26 indicates full contact list was being drafted but transmission was truncated mid-sentence; BST has **NOT YET received complete backup contacts from NOAA/UASD**
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - Jack Elston (firmware/software) — **CRITICAL PATH, OVERDUE (6/4/26)**
  - Sam Hild (QC, hardware validation, kit assembly) — **CRITICAL PATH, DUE 6/5/26**
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction, power switches)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation, failure analysis)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - Josh Fromm (GCS assembly, long-lead parts, Gateworks board sourcing) — **URGENT: requesting board status 5/28–5/29/26; no confirmation received**
  - Ben Busby (web-based controller development)
  - Nick Pawlenko (UxSOC liaison — **transitioned 5/29/26; reduced availability; backup protocol pending**)
- **Risk Signals:** 
  - 🔴 **CRITICAL/OVERDUE:** Firmware (Jack Elston) due 6/4/26 — **NOW OVERDUE; STATUS UNKNOWN.** Blocks Invoice 4 ($72k), hardware release, and 25-unit production schedule.
  - 🔴 **CRITICAL/DUE 6/5/26:** Deployment tube board QC (Sam Hild) — blocks Invoice 4 submission and hardware release.
  - 🔴 **CRITICAL/DUE 6/5/26:** Invoice 4 ($72k) — blocked on firmware and QC completion.
  - 🔴 **UNRESOLVED/URGENT:** Gateworks boards for 2 S0 ground stations ($16k DO) — Josh Fromm requested confirmation 5/28 and 5/29/26. **NO DOCUMENTED RESPONSE.** GCS build due 7/1/26; field season imminent.
  - ⚠️ **UNASSIGNED:** 25 additional S0 units (24 season + 4 sasqwatch + 1 2025 carryover + 1 refurb) due 7/31/26 — no build schedule; firmware and QC dependencies not cleared.
  - ⚠️ **Web-based controller (Ben Busby) due 7/31/26** — no visible progress.
  - ⚠️ **Operator Training due 7/31/26** — unassigned; depends on firmware, web controller, hardware.
  - ⚠️ **Communication risk:** Nick's transition may disrupt scheduling, foreign national clearances, flight planning. **Backup contact protocol not yet received from NOAA/UASD** (5/29/26 note truncated).
  - ⚠️ **Failure investigation overdue:** S0-70 rollover during CAT (4/9/26) — due 5/8/26, **now overdue; status unknown.** May indicate airframe/sensor scaling issues affecting fleet.

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasqwatch + 1 leftover from 2025 + 1 refurb from clear air testing) + 2 rack-mount ground stations ($16k DO)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| **4 of 6** | **$72,000** | **2026-06-05** | 🔴 **CRITICAL — DUE TODAY; blocked on overdue firmware & QC** |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Upcoming |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Final |
| **Subtotal** | **$483,000** | | |
| **Ground Stations DO** | **$16,000** | **Approved 5/12/26** | ⚠️ **Sourcing/build status UNCLEAR — Gateworks boards unconfirmed as of 5/29/26** |
| **TOTAL** | **$499,000** | | |

**Hardware Development Milestones:**
- ✅ 2 SHOW s0 UAS units and tripods shipped: **5/19/26** (5 days early; deadline 5/27/26)
- 🔴 Firmware finalization (Jack Elston): **DUE 6/4/26 — OVERDUE**
- 🔴 Deployment tube board QC (Sam Hild): **DUE 6/5/26**
- ⏳ 2 S0 ground stations GCS assembly (Josh Fromm): **DUE 7/1/26** — Gateworks boards sourcing status UNKNOWN as of 5/29/26
- ⏳ 25 additional S0 units production: **DUE 7/31/26** — no build schedule documented
- ⏳ Web-based controller (Ben Busby): **DUE 7/31/26** — no visible progress
-