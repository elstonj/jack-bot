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
- **Status:** **🔴 CRITICAL URGENCY — ACTIVE BLOCKING ISSUES (as of late June 2026).** Hardware milestones delivered early; field season imminent. Three blocking issues remain unresolved:
  1. **Deployment tube firmware (Jack Elston) — OVERDUE since 6/4/26 — BLOCKS Invoice 4 ($72k) & hardware release**
  2. **QC board completion (Sam Hild) — OVERDUE since 6/5/26 — BLOCKS Invoice 4 & downstream assembly**
  3. **Gateworks board sourcing status (Josh Fromm) — UNRESOLVED (queried 5/28–5/29/26, no documented response) — THREATENS GCS build due 7/1/26**
- **Team Members:** 
  - Meredith O'hara Needham (project owner, shipments, invoice submissions)
  - **Jack Elston** (firmware/software) — **CRITICAL PATH: deployment tube firmware OVERDUE; AP & PSNS firmware due 6/26/26**
  - **Sam Hild** (QC, hardware validation, kit assembly) — **CRITICAL PATH: deployment tube board QC overdue; kit assembly target 6/19**
  - Nate Straus (platform rebuild/validation, s0 builds, servo assembly, linkage construction, power switches)
  - Maciej Stachura (platform validation/testing, magnetic calibration, parameter file validation, failure analysis)
  - Alex Lomis (strategic partnerships, NASA opportunities)
  - **Josh Fromm** (GCS assembly, long-lead parts, Gateworks board sourcing) — **⚠️ CRITICAL: Gateworks board status UNKNOWN; queried 5/28–5/29/26 with no documented response; GCS build due 7/1/26**
  - Ben Busby (web-based controller development) — due 7/31/26
  - **Nick Pawlenko** (UxSOC liaison) — **transitioned to UxSOC HQ effective 5/29/26; reduced availability — broader UASD team now included for scheduling, personnel, flight planning, maintenance**

## Key Deliverables & Milestones

**Primary Deliverable:** 25 UAS units for NOAA (24 for 2026 season + 4 for sasquatch + 1 leftover from 2025 + 1 refurb from clear air testing) + 2 rack-mount ground stations ($16k DO)

**Invoice Schedule (CLIN 1001):**
| Invoice | Amount | Due Date | Status |
|---------|--------|----------|--------|
| 1 of 6 | $36,000 | 2026-03-13 | ✅ Completed |
| 2 of 6 | $54,000 | 2026-04-14 | ✅ Completed |
| Travel | $18,000 | 2026-04-15 | ✅ Completed |
| 3 of 6 | $54,000 | 2026-05-04 | ✅ Completed (5/1 — 3 days early) |
| **4 of 6** | **$72,000** | **2026-06-05** | 🔴 **OVERDUE — BLOCKED on firmware (overdue) & QC (overdue) completion** |
| 5 of 6 | $72,000 | 2026-07-02 | ⏳ Upcoming |
| 6 of 6 | $72,000 | 2026-07-31 | ⏳ Final |

**Key Firmware & Hardware Milestones:**
| Task | Owner | Due Date | Status |
|------|-------|----------|--------|
| Deployment tube firmware | Jack Elston | 2026-06-04 | 🔴 **OVERDUE** |
| QC at least one of each board as they arrive | Sam Hild | 2026-06-04 | 🔴 **OVERDUE** |
| Finish deployment tube board QCs | Sam Hild | 2026-06-05 | 🔴 **OVERDUE** |
| **Finalize AP & PSNS firmware** | **Jack Elston** | **2026-06-26** | **⏳ OPEN (Asana)** |
| **Rebuild old BST s0 (2024)** | **Nate Straus** | **2026-06-19** | **⏳ OPEN** |
| **Begin kit assembly** | **Sam Hild** | **2026-06-19** | **⏳ OPEN** |
| **Assembly latch carrier trays** | **Nate Straus** | — | ✅ **Completed 2026-06-23** |
| Build 2x rack-mount GCS | Josh Fromm | 2026-07-01 | ⏳ Upcoming; **⚠️ Gateworks board sourcing status unknown** |
| Finish 2025 S0's | Nate Straus | 2026-06-30 | ⏳ Upcoming |
| Participate in mag cal process | Maciej Stachura | 2026-07-01 | ⏳ Upcoming |
| Increase cruise speed back to 2024 value | Maciej Stachura | 2026-06-30 | ⏳ Upcoming |
| Get 2025/2026 params files validated | Maciej Stachura | 2026-06-30 | ⏳ Upcoming |
| Operator training | Unassigned | 2026-07-31 | ⏳ Upcoming; unassigned |
| Web-based controller | Ben Busby | 2026-07-31 | ⏳ Upcoming; no visible progress |

## Task Summary

**Asana Status:** 1 open task, 0 completed (in final execution phase)

**Open Task:**
- **Finalize AP & PSNS firmware** (Jack Elston) — Due 2026-06-26

**Recent Completions:**
- ✅ **Assembly latch carrier trays** (Nate Straus) — completed 2026-06-23

**Critical Path Bottlenecks:**
  - **Jack Elston:** 
    - Deployment tube firmware OVERDUE since 6/4/26 — blocks Invoice 4 ($72k) and hardware release
    - AP & PSNS firmware due 6/26/26 (approaching; likely to impact downstream validation)
  - **Sam Hild:** Deployment tube board QC OVERDUE since 6/5/26 — blocks Invoice 4 and kit assembly start (target 6/19)
  - **Josh Fromm:** Gateworks board sourcing status unresolved; no documented response to queries on 5/28–5/29/26 — threatens GCS build due 7/1/26

## Recent Activity

- **June 23, 2026:** Assembly latch carrier trays completed (Nate Straus)
- **May 29, 2026:** Nick Pawlenko trans