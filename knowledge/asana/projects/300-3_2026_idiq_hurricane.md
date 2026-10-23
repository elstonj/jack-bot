_Asana snapshot as of 2026-10-23: 24 open tasks, 24 completed (last 365 days)._

# 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration)
- **Dollar Value:** $483,000 (Total funding to Black Swift)
- **IDIQ Contract:** 1305M226D0012 | Delivery Order: 1305M226F0084
- **Timeline:** 
  - 20 original S0s due August 2026 ✓
  - 13 S0s due October 2026
  - 21 S0s (option exercised 8/5/26) due November 2026
  - 2 ground stations due 12 July 2026
  - Project completion: 1 June 2027
- **Status:** Active — High volume of ongoing manufacturing and delivery obligations
- **Team Members:** Meredith O'hara Needham (owner/invoicing), Sam Hild (QC/assembly), Ben Busby (web controller), Maciej Stachura (flight validation), Jack Elston (firmware), Josh Fromm (GCS builds), Spencer Hoehl (qualifications coordination)
- **Priority:** Low (custom field), but critical delivery deadlines

## Risk Signals
- **Many open tasks unassigned** — 17 of 24 open tasks have no assignee, despite near-term due dates
- **Key manufacturing tasks without owners:**
  - "Deliver 24 S0 for 2026 season" (due 31 July 2026) — unassigned
  - "Deliver 13 S0" (due 30 October 2026) — unassigned  
  - "Deliver 21 S0" (due 30 November 2026) — unassigned
  - "Finish 2025 S0's (full system packed)" (due 30 June 2026) — unassigned
- **Incomplete subassembly tasks with no due dates** — servo wiring, linkage construction, GCS builds, refurbishment tasks lack owners and deadlines
- **Invoice 3 of 3 ($117,000) approaching due date** (5 October 2026) — assigned to Meredith O'hara Needham
- **Leadership transition:** Note from 29 May 2026 indicates Nick Pawlenko transitioning to UxSOC headquarters role; communication handoff occurred

## Key Deliverables & Milestones

| Deliverable | Quantity | Due Date | Status |
|-------------|----------|----------|--------|
| Ground stations (rack-mount GCS) | 2 | 12 July 2026 | Open, unassigned |
| S0 units (original order for NOAA UAS) | 20 | Aug 2026 | Completed (invoiced) |
| S0 units (Season 1 batch) | 13 | 30 October 2026 | Open, unassigned |
| S0 units (Season 2 batch, option) | 21 | 30 November 2026 | Open, unassigned |
| S0 units from 2025 season | 1 | 31 July 2026 | Open, unassigned |
| Invoice 3 of 3 (CLIN 1001 POF0344) | — | 5 October 2026 | Open |
| Web-based controller | 1 | 31 July 2026 | Open, assigned to Ben Busby |
| Operator training | — | 31 July 2026 | Open, unassigned |

## Task Summary

**Total Tasks:** 48 (24 open, 24 completed)

**Completion Rate:** 50% (heavily skewed by invoicing & early-stage fabrication work; manufacturing pipeline not yet complete)

**Tasks by Assignee:**

| Assignee | Open | Completed | Notes |
|----------|------|-----------|-------|
| Unassigned | 17 | — | **Critical issue:** Most manufacturing deliverables lack owners |
| Meredith O'hara Needham | 1 | 9 | Invoicing pipeline (5 invoices submitted, 1 pending) |
| Sam Hild | 3 | — | QC & assembly lead (board validation, kit assembly start) |
| Ben Busby | 1 | — | Web-based controller development |
| Maciej Stachura | — | 3 | Flight dynamics validation (recently completed: mag cal, params, cruise speed) |
| Jack Elston | 1 | 2 | Firmware finalization (AP, PSNS, deployment tube) |
| Josh Fromm | — | 2 | GCS builds, parts ordering |

**Notable Patterns:**
- Heavy invoicing discipline — 9 invoices submitted on schedule, tracking against $483k budget
- Maciej Stachura's flight validation work recently completed (all tasks done as of 2 Oct 2026)
- Manufacturing pipeline tasks deeply fragmented — many subtasks (wiring servos, linkages, power switches) lack owners and deadlines
- Sam Hild carries QC bottleneck (multiple board/assembly QC tasks)

## Recent Activity

**Last 30 Days (as of 2 October 2026):**
- **2 Oct 2026:** Flight validation work completed — Maciej Stachura finished mag cal participation, parameter file validation, and cruise speed adjustment
- **28 Sept 2026:** Invoice 2 of 3 submitted ($58,500) and Invoice 6 of 6 submitted ($72,000)
- **Earlier (July-Sept):** Firmware finalized, GCS units built, show units shipped, original 20 S0s fabricated and shipped

**Upcoming Critical Dates:**
- **5 Oct 2026:** Invoice 3 of 3 ($117,000) due
- **30 Oct 2026:** First 13 S0 units due to NOAA
- **30 Nov 2026:** Second batch (21 S0 units) due to NOAA

## Notes & Context

### Qualification Request (Active)
**Spencer Hoehl issued qualification survey on 1–2 October 2026:** Team members should document and submit:
- FAA pilot qualifications (Part 107, 61, 141, etc.)
- Security clearances
- NOAA Hurricane training
- COA (Certificate of Waiver or Authorization) training and issuing authority
- Supporting documentation

This is ongoing and should be tracked separately as a compliance/HR function.

### Project Structure
- **CLIN 1001 (original):** 20 S0 units for NOAA UAS + support services → invoiced in 6 increments ($36k → $54k → $54k → $72k → $72k → $72k = $360k total)
- **CLIN 1001 POF0344 (option addition):** 13 S0 units (Oct) + 21 S0 units (Nov) + 2 ground stations → invoice in 3 increments ($58.5k → $58.5k → $117k = $234k, exceeds budgeted $483k by alignment with delivery order 1305M226F0084)

### Manufacturing Dependencies
- Original 20 S0s completed and shipped; invoicing pipeline on track
- 2025 S0 completion and 1 leftover delivery blocked by lack of assembly assignment
- Ground station builds (2x rack-mount GCS) unassigned despite mid-July deadline
- Subassembly tasks (linkages, servo wiring for wings/tails, power switches) fragmented — may represent bottleneck in scaling to 13 + 21 unit batches

### Leadership Context
Nick Pawlenko (LCDR, NOAA UASD) transitioned to NOAA UxSOC headquarters; communication protocol established to maintain continuity with NOAA Flight Operations and UxS Operations Center in Silver Spring, MD.

---

**Data extracted:** Asana project as of 2 October 2026 | **Owner:** Meredith O'hara Needham