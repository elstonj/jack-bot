# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** $483,000 total IDIQ funding + $16,000 Delivery Order for 2 ground stations = **$499,000 total**
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084
  - Ongoing partnership since 2018 (SBIR Phase I 2018, Phase II 2019–2020)
- **Timeline:** 
  - Final delivery deadline: **2026-07-31**
  - Invoice schedule: March 2026 – July 2026
  - Critical hardware ship date: **May 19, 2026** (✅ completed early; 2 SHOW s0's and tripods shipped)
- **Status:** **🔴 ACTIVE — CRITICAL URGENCY. MULTIPLE BLOCKING ISSUES OVERDUE/DUE IMMEDIATELY (as of 6/5/26).** Hardware milestones delivered early. Field season imminent.
  - **BLOCKING ISSUES (6/4–6/5/26):**
    1. **Firmware finalization (Jack Elston) — OVERDUE as of 6/4/26** — deployment tube firmware **past due (due 6/4/26)**; AP & PSNS firmware due 6/26/26. Gating Invoice 4 ($72k, due 6/5/26) and hardware release.
    2. **QC board validation (Sam Hild) — DUE 6/5/26 (TODAY)** — deployment tube board QC critical path for hardware release. Finish deployment tube board QCs due 6/5/26; begin kit assembly due 6/19/26.
    3. **Gateworks boards sourcing (Josh Fromm) — UNRESOLVED & URGENT** — Josh requested status confirmation **5/28/26 & 5/29/26** (per team feedback). **No documented response from Meredith or procurement.** Status UNKNOWN. Blocks GCS assembly (2 units due 7/1/26; additional units for 25-UAS production due 7/31/26).
    4. **Communication continuity — INCOMPLETE** — Nick Pawlenko transitioned to UxSOC HQ effective **5/29/26**. Project note from 5/29/26 indicates backup contact protocol was being drafted but **transmission was truncated mid-sentence.** BST has **NOT YET received complete backup contacts from NOAA/UASD** for scheduling, foreign nationals clearances, flight planning, and maintenance.
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - **Jack Elston** (firmware/software) — **CRITICAL PATH: deployment tube firmware OVERDUE (6/4/26); AP & PSNS firmware due 6/26/26**
  - **Sam Hild** (QC, hardware validation, kit assembly) — **CRITICAL PATH: deployment tube QC due 6/5/26 (TODAY); kit assembly due 6/19/26**
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction, power switches)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation, failure analysis)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - **Josh Fromm** (GCS assembly, long-lead parts, Gateworks board sourcing) — **URGENT: requested board status 5/28–5/29/26 (per team feedback); awaiting response; GCS build due 7/1/26**
  - Ben Busby (web-based controller development) — due 7/31/26
  - Nick Pawlenko (UxSOC liaison — **transitioned 5/29/26; reduced availability; backup protocol PENDING**)

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasquatch + 1 leftover from 2025 + 1 refurb from clear air testing) + 2 rack-mount ground stations ($16k DO)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| **4 of 6** | **$72,000** | **2026-06-05** | 🔴 **DUE TODAY — BLOCKED on firmware (overdue) & QC (due today) completion** |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Upcoming |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Final |

**Key Firmware & Hardware Milestones:**
| Task | Owner | Due Date | Status |
|------|-------|----------|--------|
| Deployment tube firmware | Jack Elston | 2026-06-04 | 🔴 **OVERDUE** |
| Deployment tube board QC (finish) | Sam Hild | 2026-06-05 | 🔴 **DUE TODAY** |
| AP & PSNS firmware | Jack Elston | 2026-06-26 | ⏳ Upcoming (21 days) |
| Begin kit assembly | Sam Hild | 2026-06-19 | ⏳ Upcoming (14 days) |
| Build 2x rack-mount GCS | Josh Fromm | 2026-07-01 | ⏳ Upcoming (26 days); **Gateworks board sourcing UNRESOLVED** |
| Rebuild old BST s0 (2024) | Nate Straus | 2026-06-19 | ⏳ Upcoming (14 days) |
| Finish 2025 S0's | Nate Straus | 2026-06-30 | ⏳ Upcoming (25 days) |
| Operator training | Unassigned | 2026-07-31 | ⏳ Upcoming (57 days); unassigned |
| Web-based controller | Ben Busby | 2026-07-31 | ⏳ Upcoming (57 days); no visible progress |

## Task Summary

**Overall:** 31 open tasks, 0 completed (100% open rate — project is early-stage execution phase)

**Tasks by Assignee:**
- **Jack Elston:** 3 tasks (deployment tube firmware *OVERDUE*, AP & PSNS firmware due 6/26, S0 acc scaling unscheduled) — **CRITICAL PATH**
- **Sam Hild:** 3 tasks (QC board validation due 6/4 *OVERDUE*, finish QC due 6/5 *TODAY*, begin kit assembly due 6/19) — **CRITICAL PATH**
- **Nate Straus:** 8 tasks (rebuild old s0 due 6/19, finish 2025 S0's due 6/30, power switches *OVERDUE 5/21*, linkages/servos/latch tray assembly unscheduled)
- **Maciej Stachura:** 4 tasks (mag cal due 7/1, S0-70 rollover investigation *OVERDUE 5/8*, cruise speed due 6/30, params files due 6/30)