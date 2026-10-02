# [001-22] Fleet Maintenance

## Overview
- **Owner:** Dan Prendergast
- **Purpose:** Track required maintenance actions across company aircraft fleet
- **Aircraft in scope:** E20006, E20009, E20014, S10022, S10005, S20009, S20004, S30001, plus S10020 (VTOL) and S10021 (VTOL)
- **Status:** Active
- **Dollar value:** Not specified
- **Timeline:** No defined project timeline
- **Team members involved:** Dan Prendergast, Jack Elston, Spencer Hoehl, Maciej Stachura, Ethan Domagala, Nate Straus, Josh Fromm

## Key Deliverables & Milestones
None defined.

## Task Summary
- **Total tasks:** 4 open, 0 completed
- **Tasks by assignee:**
  - Spencer Hoehl: 3 open tasks
  - Josh Fromm: 1 open task
- **Open tasks:**
  1. **ERAU E2 locking collar fix** (Josh Fromm, no due date)
     - Work Type: Fix
     - Aircraft Status: Down (Grounded)
     - QC Required: No
     - Maintenance Type: Unscheduled Repair
     - Hardware or Software: Hardware
     - Description: E2 for ERAU is grounded due to the arm locking mechanism on right side having a loose collar

  2. **ERAU E2 Prop replacement** (Spencer Hoehl, no due date)
     - Work Type: Fix
     - Aircraft Status: Down (Grounded)
     - QC Required: No
     - Maintenance Type: Unscheduled Repair
     - Hardware or Software: Hardware

  3. **S10020 (VTOL) right wing motor pivot** (Spencer Hoehl, no due date)
     - Work Type: Fix
     - Aircraft Status: Up (Operational)
     - QC Required: Yes
     - Maintenance Type: Preventive Maintenance
     - Priority: Low
     - Hardware or Software: Hardware
     - VTOL Only: Yes
     - Description: Right wing motor pivot oscillates during manual and joystick hover. Possible wing stiffness issue or worn servo. Investigate before committing to repair.

  4. **Repairing S10021** (Spencer Hoehl, no due date)
     - Work Type: Fix
     - Aircraft Status: Down (Grounded)
     - QC Required: Yes
     - Maintenance Type: Modification
     - Priority: Medium
     - Hardware or Software: Hardware
     - Affected Aircraft: S10021 (VTOL)
     - Description: Repair S1-VTOL 2040 with new AP and PSNS. Replace MHP.

## Recent Activity
- **New grounded aircraft:** ERAU E2 now appears in workload with two tasks (locking collar fix and prop replacement) — both unscheduled repairs with grounded status
- **New VTOL task:** S10021 repair task added to backlog (Modification work, grounded, QC required)
- **Active investigation:** S10020 preventive maintenance investigation remains low priority but operational

## Notes & Context
- Project structure uses aircraft tail numbers as section headers (List view)
- Custom fields in use: Work Type (Fix/New Feature), Aircraft Status (Up/Down), QC Required (Yes/No), Maintenance Type (Preventive Maintenance/Modification/Unscheduled Repair), Priority level, Hardware or Software designation, VTOL Only flag
- **Current grounded aircraft (3):**
  - ERAU E2: Right arm locking collar loose (2 tasks queued; Josh Fromm and Spencer Hoehl assigned)
  - S10021 (VTOL): Awaiting AP, PSNS, and MHP replacement (Spencer Hoehl assigned)
- **Operational aircraft with open maintenance:**
  - S10020 (VTOL): Low-priority investigation of right wing motor pivot oscillation; requires root cause analysis before repair decision
- **Staffing:** Spencer Hoehl carries 3 open tasks; Josh Fromm has 1 task
- **Critical gap:** No due dates set on any open tasks — recommend immediate scheduling with Dan Prendergast, especially for grounded E2 and S10021 aircraft
- No previously completed tasks visible in project