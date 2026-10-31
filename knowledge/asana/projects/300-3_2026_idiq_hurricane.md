_Asana snapshot as of 2026-10-31: 10 open tasks, 12 completed (last 90 days)._

# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration)
- **Dollar Value:** $483,000 (BST allocation from $1,111,000 total IDIQ)
- **Invoice Delivery Order:** 1305M226F0084 (IDIQ # 1305M226D0012)
- **Timeline:** 
  - Original 20 S0s: due August 2026
  - 13 S0s: due October 2026
  - 21 S0s: due November 2026 (option exercised 8/5/26)
  - Additional 30 S0s: due June 2027
  - Project end date: June 1, 2027
- **Status:** Active — hardware deliveries progressing; significant manufacturing work ongoing (PSNS fixes, QC); multiple milestones open without due dates
- **Team Members:** Jack Elston (lead), Josh Fromm, Ben Busby, Sam Hild, Ali Sulehria, Meredith O'hara Needham (owner/invoicing), Maciej Stachura
- **Risk Signals:** 
  - Five critical tasks (PSNS v1.5 fixes, QC, board replacement, kit completion, 13-aircraft delivery) have **no due dates** despite November delivery window approaching
  - Unassigned 21-platform delivery task due 11/30/26
  - Invoice 3 of 3 ($117,000) due 10/5/26 with no clear completion dependencies listed

## Key Deliverables & Milestones
| Milestone | Due Date | Status | Notes |
|-----------|----------|--------|-------|
| Deliver 20 original S0s for NOAA UAS | August 2026 | **COMPLETED** | Delivered 7/31/26; 2 ground stations also delivered 7/12/26 |
| Deliver 13 S0s (Option 1) | October 2026 | **OPEN** | Milestone assigned to Josh Fromm; closeout is delivery to customer |
| Deliver 21 S0s (Option 2) | November 30, 2026 | **OPEN** | Option exercised 8/5/26; unassigned |
| Web Controller Complete for NOAA | TBD (open) | **OPEN** | Assigned Ben Busby; closeout is BST sim testing with no errors |
| Conduct NOAA Sim Training | TBD (open) | **OPEN** | Assigned Jack Elston; closeout is NOAA payment |
| Develop Plan for 2027 Delivery | TBD (open) | **OPEN** | Assigned Jack Elston; closeout is planning document |
| Deliver 30 S0s (Option 3) | June 1, 2027 | Planned | Not yet broken into tasks |

## Task Summary
- **Total Tasks:** 22 (10 open, 12 completed)
- **Completion Rate:** 55% overall

### By Assignee (Open Tasks)
| Assignee | Open Tasks | Type |
|----------|-----------|------|
| Sam Hild | 3 | Manufacturing/QC (PSNS fixes, board replacement, kit completion) |
| Jack Elston | 2 | Strategic (sim training, 2027 planning) |
| Ben Busby | 1 | Web Controller development |
| Josh Fromm | 1 | Delivery milestone (13 S0s) |
| Ali Sulehria | 1 | QC (v1.5 PSNS re-check) |
| Meredith O'hara Needham | 1 | Invoicing (Invoice 3 of 3, $117k) |
| Unassigned | 1 | Delivery (21 S0s) |

### Notable Patterns
- **Manufacturing bottleneck:** Sam Hild owns most open hardware tasks; v1.5 PSNS board issues require fixes, full QC re-certification, and retrofit on already-built aircraft — critical path unclear
- **Invoicing discipline:** Three invoices tracked ($58.5k, $58.5k, $117k); Invoice 2 submitted 9/28, Invoice 3 due 10/5/26
- **Milestone ambiguity:** Four major milestones (web controller, training, 2027 plan, 13-aircraft delivery) have no due dates despite <8 weeks to November delivery

## Recent Activity
- **September 28, 2026:** Invoices 2 and 6 submitted (total $130.5k)
- **October 2, 2026:** Mag calibration process completed (Maciej Stachura)
- **October 30, 2026:** Large batch of historical tasks marked complete—accelerated closeout of 2025 inventory, power switches, and ground station work
- **August 5, 2026:** Customer exercised option for additional 21 platforms (now due November)
- **May 29, 2026:** Communication protocol updated due to Nick Pawlenko transition to UxSOC headquarters; Meredith O'hara Needham now primary contact point

## Notes & Context
- **PSNS v1.5 Crisis:** A critical defect in the v1.5 Power and Sensor Node System (PSNS) requires:
  1. Design fix (Sam Hild assigned)
  2. Re-QC on fixed boards (Ali Sulehria assigned)
  3. Physical replacement of all PSNS boards on already-built S0s plus re-QC (Sam Hild assigned)
  - **No due date specified** — this is a blocking issue for the 13-aircraft October delivery and likely the 21-aircraft November delivery
- **Kit Completion:** Sam Hild also owns "Finish kits needed for new S0s to be built to finish out the 13 aircraft order" — no due date
- **Invoicing:** Track Invoice 3 ($117k) submission by 10/5/26 against invoice template (linked in task notes)
- **2027 Planning:** 30 additional S0s due June 2027 have not yet been decomposed into tasks; requires planning document and task writeout from Jack Elston
- **Government customer:** NOAA is high-priority; payment milestones tied to delivery and sim training completion
- **Project Notes Discrepancy:** Original project notes reference "20 for NOAA UAS (due Aug 2026)" and separate S0 delivery windows; all original 20 delivered on time; current focus is on Options 1 and 2 (13 + 21 platforms)