_Asana snapshot as of 2026-10-30: 4 open tasks, 8 completed (last 90 days)._

# [001-22] Fleet Maintenance

## Overview
- **Owner:** Dan Prendergast
- **Purpose:** Track required maintenance actions across BST aircraft fleet
- **Fleet Aircraft:** E20006, E20009, E20014, S10022, S10005, S20009, S20004, S30001 (plus operational aircraft S10021, S10019, FW0001, and ERAU E2)
- **Status:** Active — ongoing maintenance operations
- **Team Members:** Spencer Hoehl, Jack Elston, Josh Fromm, Ethan (and others)
- **View Format:** List view organized by tail number

## Key Metrics
- **Open Tasks:** 4
- **Completed Tasks:** 8
- **Recent Completion Rate:** High (8 recent completions across maintenance types)

## Open Maintenance Tasks

| Aircraft | Task | Assignee | Issue | Aircraft Status | QC Required | Due Date |
|----------|------|----------|-------|-----------------|-------------|----------|
| S10020 | Repairing S1-VTOL | Spencer Hoehl | Repair S1-VTOL 2040 with new AP and PSNS; replace MHP | Down (Grounded) | Yes | None |
| S10022 | S1-22 Door hinge | Spencer Hoehl | Fix side door hinge latch | Up (Operational) | No | None |
| S10005 | S1-5 Pitot tube loose tip | Spencer Hoehl | Glue down pitot tube tip | Up (Operational) | No | None |
| S10019 | Trims | Unassigned (Ethan) | Reset trim surfaces for current center points in manual | Up (Operational) | No | None |

**Risk Signals:**
- **No due dates set** — open tasks lack deadline visibility
- **One grounded aircraft (S10020)** requiring QC — S1-VTOL repair is a high-priority blocker
- **Unassigned task (Trims)** — S10019 trim work needs formal assignment despite Ethan noted in custom field

## Recently Completed Maintenance (October 2026)

| Aircraft | Task | Assignee | Completed | Issue |
|----------|------|----------|-----------|-------|
| S10021 | Update cruise speed to 16 m/s | Unassigned | 2026-10-27 | Configuration update |
| S10021 | Recalibrate mags | Unassigned | 2026-10-27 | Calibration maintenance |
| S10021 | Fix AP on S10021 | Jack Elston | 2026-10-23 | Autopilot boot failure after swap (overdue from 2026-05-18) |
| FW0001 | Low RSSI issue | Spencer Hoehl | 2026-10-16 | Cabling inspection |
| S10021 | Pitot tube not holding Airspeed | Spencer Hoehl | 2026-10-13 | AOG (Aircraft on Ground) priority — resolved |
| ByLight Mustang | Mechanical Trim resetting | Unassigned (Ethan) | 2026-10-08 | Manual trim pitch control |
| ERAU E2 | Locking collar fix | Josh Fromm | 2026-10-06 | Arm mechanism loose collar (was grounded) |
| ERAU E2 | Prop replacement | Spencer Hoehl | 2026-10-05 | Hardware replacement |

## Task Summary by Assignee

| Assignee | Open | Completed | Notes |
|----------|------|-----------|-------|
| Spencer Hoehl | 3 | 4 | Primary maintenance technician; most active |
| Jack Elston | 0 | 1 | Autopilot specialist; one task (overdue completion) |
| Josh Fromm | 0 | 1 | Structural/mechanism repairs |
| Ethan | 0 | 2 | Trim and configuration work |
| Unassigned | 1 | 1 | Trims task needs formal assignment |

## Custom Fields in Use

- **Work Type:** Fix / New Feature
- **Aircraft Status:** Up (Operational) / Down (Grounded)
- **QC Required:** Yes / No
- **Maintenance Type:** Unscheduled Repair, Modification
- **Priority:** Medium, AOG (Aircraft on Ground)
- **Hardware or Software:** Hardware / Software
- **Parts Status:** Available
- **Affected Aircraft:** Tail number tracking

## Notes & Context

1. **No due dates on open tasks** — The project tracks maintenance but lacks deadline discipline. Consider setting target completion dates for prioritization, especially the grounded S10020.

2. **S10021 activity pattern** — Heavy recent activity on S10021 (4 tasks in October), suggesting either recent inspection/turnaround or recurring issues (AP swap, pitot tube, magneto recalibration). Monitor for systemic problems.

3. **Spencer Hoehl workload** — Carries 3 of 4 open tasks plus 4 recent completions. Capacity risk if new maintenance demands arise.

4. **Grounded aircraft (S10020)** — S1-VTOL repair requiring QC is the highest operational priority blocking that tail number.

5. **External aircraft tracking** — Project includes non-standard fleet aircraft (ERAU E2, FW0001, ByLight Mustang) beyond the declared 8-aircraft fleet, suggesting dynamic maintenance scope or partnerships.