_Asana snapshot as of 2026-10-27: 4 open tasks, 6 completed (last 90 days)._

# [001-22] Fleet Maintenance

## Overview
- **Owner:** Dan Prendergast
- **Purpose:** Track required maintenance actions across company aircraft fleet
- **Status:** Active
- **Team Members:** Spencer Hoehl, Jack Elston, Ethan, Josh Fromm (and others as needed)
- **Risk Signals:** 
  - 4 open tasks with no due dates assigned
  - Aircraft grounded (S10021, S10020) with pending repairs
  - QC required on at least one active repair (S10020)

## Fleet & Aircraft Sections
Project organized by tail numbers:
- E20006, E20009, E20014
- S10022, S10005, S20009, S20004, S30001
- Also tracking: S10021, S10020, S10019, FW0001, ByLight Mustang, ERAU E2

## Key Custom Fields
- **Work Type:** Fix / New Feature
- **Aircraft Status:** Up (Operational) / Down (Grounded)
- **QC Required:** Yes / No
- **Maintenance Type:** Modification / Unscheduled Repair
- **Priority:** Medium, AOG (Aircraft on Ground), etc.
- **Hardware or Software:** Hardware / Software

## Task Summary
- **Total:** 10 tasks (4 open, 6 completed)
- **By Assignee:**
  - Spencer Hoehl: 3 tasks (2 completed, 1 open) — 67% completion
  - Jack Elston: 1 completed
  - Josh Fromm: 1 completed
  - Ethan: 2 tasks (1 completed, 1 open) — 50% completion
  - Unassigned: 2 open tasks

## Open Tasks (Critical Items)
| Task | Aircraft | Assignee | Status | Notes |
|------|----------|----------|--------|-------|
| Repairing S1-VTOL 2040 | S10020/S10021 | Spencer Hoehl | Down (Grounded) | Replace AP and PSNS, Replace MHP. QC Required. |
| Trims | S10019 | Unassigned | Up (Operational) | Reset trim surfaces for current center points. |
| Recalibrate mags | S10021 | Unassigned | — | No due date |
| Update cruise speed to 16 m/s | S10021 | Unassigned | — | No due date |

## Recent Activity
**Completed (Oct 2026):**
- Oct 23: Fix AP on S10021 (Jack Elston) — resolved autopilot boot issue
- Oct 16: FW0001 Low RSSI issue (Spencer Hoehl) — cabling check
- Oct 13: S10021 Pitot tube airspeed issue (Spencer Hoehl) — AOG priority, resolved
- Oct 8: Mechanical Trim resetting on ByLight Mustang (Ethan)
- Oct 6: ERAU E2 locking collar fix (Josh Fromm)
- Oct 5: ERAU E2 Prop replacement (Spencer Hoehl)

## Notes & Context
- **No due dates:** Most open and many closed tasks lack due dates; rely on custom fields for priority and aircraft status tracking
- **S10021 history:** Multiple recent repairs (AP fix, pitot tube, mags calibration pending)
- **Grounded aircraft:** S10020 and S10021 currently down; repairs in progress
- **QC gate:** S10020 repair requires QC sign-off before return to service
- **View format:** Project configured as List view per owner specifications