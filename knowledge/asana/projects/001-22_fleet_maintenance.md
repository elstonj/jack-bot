_Asana snapshot as of 2026-11-14: 4 open tasks, 9 completed (last 90 days)._

# [001-22] Fleet Maintenance

## Overview
- **Owner:** Dan Prendergast
- **Purpose:** Track required maintenance actions across BST's aircraft fleet
- **Fleet aircraft:** E20006, E20009, E20014, S10022, S10005, S20009, S20004, S30001 (plus additional aircraft appearing in tasks: S10021, S10019, FW0001, ByLight Mustang, ERAU E2)
- **Status:** Active — ongoing unscheduled repairs and maintenance across the fleet
- **Team members:** Spencer Hoehl (primary maintenance), Jack Elston, Josh Fromm, Ethan
- **Risk signals:** 
  - 4 open maintenance items with no due dates assigned
  - 1 aircraft currently grounded (S10021) with repair in progress
  - Multiple high-priority items affecting operational aircraft

## Task Summary
- **Total tasks:** 13 (4 open, 9 completed)
- **Completion rate:** 69% (9 of 13 completed)

### By Assignee
- **Spencer Hoehl:** 3 open tasks; 5 completed — primary maintenance technician
- **Unassigned:** 2 open tasks (Trims for S10019, trim/mag calibration completed on S10021)
- **Jack Elston:** 1 completed (AP repair on S10021)
- **Josh Fromm:** 1 completed (E2 locking collar fix)
- **Ethan:** 1 completed (mechanical trim resetting)

### Custom Fields in Use
- **Work Type:** Fix (all tasks)
- **Aircraft Status:** Up (Operational) vs. Down (Grounded)
- **QC Required:** Yes/No
- **Maintenance Type:** Unscheduled Repair, Modification
- **Hardware or Software:** Hardware (majority), Software
- **Priority:** High, Medium, Low, AOG (Aircraft on Ground)

## Open Maintenance Items

| Aircraft | Task | Assignee | Status | Priority | QC Required |
|----------|------|----------|--------|----------|-------------|
| S10022 | Loose GPS connection | Spencer Hoehl | Up (Operational) | High | No |
| S10021 | Repairing S1-VTOL 2040 (new AP, PSNS, replace MHP) | Spencer Hoehl | Down (Grounded) | Low | **Yes** |
| S10005 | Pitot tube loose tip | Spencer Hoehl | Up (Operational) | — | No |
| S10019 | Trims reset | Unassigned | Up (Operational) | — | No |

## Recent Activity

**Completed (October 2026):**
- Oct 30: S10022 door hinge repair (Spencer Hoehl)
- Oct 27: S10021 cruise speed update & mag recalibration (automation/unassigned)
- Oct 23: S10021 autopilot repair completed after 5+ month delay (Jack Elston, originally due May 18)
- Oct 16: FW0001 RSSI cabling check (Spencer Hoehl)
- Oct 13: S10021 pitot tube airspeed hold issue (Spencer Hoehl) — AOG priority
- Oct 8: Mechanical trim resetting (Ethan)
- Oct 6: ERAU E2 locking collar fix (Josh Fromm)
- Oct 5: ERAU E2 prop replacement (Spencer Hoehl)

**Current blockers:**
- S10021 remains grounded pending completion of AP/PSNS/MHP repair with QC sign-off
- S10022 GPS issue (high priority) and S10005 pitot tube work unscheduled
- S10019 trim work unassigned

## Notes & Context

- **No dollar values** recorded in custom fields for this project
- **No due dates** set on open tasks — maintenance is reactive/unscheduled rather than scheduled preventive
- **Aircraft nomenclature mismatch:** Project notes specify 8 tail numbers (E/S series), but tasks reference variants (S10019, S10020, S10021 not in project header; FW0001; ERAU E2; ByLight Mustang also appear)
- **Custom field usage is heavy and consistent** — Work Type, Aircraft Status, QC Required, Hardware/Software, Priority, and Maintenance Type enable tracking across repair categories
- **Spencer Hoehl is the primary technician** — 8 of 13 total tasks assigned to him (3 open, 5 completed)
- **QC flag:** Only the S10021 major repair (AP swap + modifications) requires QC; other fixes are field-level maintenance
- **Completion velocity:** 9 completed tasks with no defined due dates suggests work is logged after completion rather than scheduled in advance