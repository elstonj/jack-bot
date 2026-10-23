_Asana snapshot as of 2026-10-23: 10 open tasks, 24 completed (last 365 days)._

# Flight Testing

## Overview

- **Client/Customer:** Internal BST flight operations (multiple aircraft platforms: S-series, E-series, Flamewheel, ByLight Mustang)
- **Dollar value:** Not specified in task data
- **Timeline:** Ongoing; most recent activity October 2026
- **Status:** Active, operationally running. Per Daniel Prendergast (2026-10-02): "You guys shouldn't be flying next season anyway. New flight ops folks should get that qual for next season" — indicates current flight testing cycle is winding down before handoff to new flight ops team.
- **Team members involved:** Spencer Hoehl (primary test pilot, 30+ tasks), Daniel Prendergast (validation flights), Ethan Domagala (ByLight Mustang, form/checklist setup), Alex Lomis (S0 VTOL, S10020 testing), Maciej Stachura (autopilot testing)

## Key Deliverables & Milestones

| Milestone | Status | Notes |
|-----------|--------|-------|
| Release Candidate Testing (S10011, FW0002, S20003, E20006, S10005, FW0001, S10022, S10021) | Open, no due dates | 8 aircraft awaiting release candidate firmware validation; Params must be downloaded before firmware upload |
| ERAU E2 Instability Investigation | Open, ready for flight testing | Investigating aircraft instability over "next couple weeks"; issue could not be reproduced as of 9/29 |
| Swiftab App Release Candidate | Open | Version uploaded; testing status pending |
| Validation Flight Series (#1–3) | Completed 2026-04-25, 2026-07-13 | Led by Dan Prendergast |
| ByLight Mustang Flight Test | Completed 2026-09-22 | Characterized stability and max range; due date was 2026-09-18 (4 days overdue) |

## Task Summary

- **Total tasks:** 34 (10 open, 24 completed)
- **Completion rate:** 71%
- **Tasks by assignee:**
  - **Spencer Hoehl:** ~30 tasks (mostly completed QC flights, currently assigned all 10 open release candidate tests and ERAU investigation)
  - **Daniel Prendergast:** 3 validation flights (all completed)
  - **Ethan Domagala:** 4 tasks (ByLight Mustang, form/checklist creation)
  - **Alex Lomis:** 2 tasks (S0 VTOL hover/transition, S10020 ESC testing)
  - **Maciej Stachura:** 1 task (S10019 autopilot test)

- **Notable patterns:**
  - Spencer Hoehl is the bottleneck: nearly all active testing and all open release candidate tests assigned to him
  - **No due dates on open tasks** — risk of unclear priorities and deadlines
  - Heavy focus on firmware QC validation cycles (major code updates rolled out mid-August, with subsequent QC flights throughout August–September)
  - Aircraft-specific maintenance issues documented (mag signal drops, ESC power loss, autopilot altitude loss, motor spin-up issues)

## Recent Activity

- **2026-10-14:** S10022 Test Flights and S10021 VTOL QC flights completed (firmware validation)
- **2026-10-09:** S1 fixed wing and FlameWheel QC completed
- **2026-10-05:** Soil Moisture E2 flight testing completed
- **2026-10-01:** QC Flight for new firmware completed; S0 VTOL testing completed (was overdue since 2026-08-28)
- **2026-09-22:** ByLight Mustang Flight Test completed (4 days past 2026-09-18 due date)
- **2026-09-21:** NASA S2 QC flight passed (customer readiness confirmed)
- **Late August–early September:** Major firmware QC cycle completed across S1, Flamewheel, S0-MAD, S10019, S10020 platforms

## Notes & Context

- **Team transition planned:** Per Daniel Prendergast (2026-10-02 & 10-01), current flight ops team will not fly next season; new flight ops personnel should obtain qualifications before then. This signals the project is in a structured wind-down phase.

- **No externally driven timelines:** Despite Asana task deadlines spanning April–September 2026, the lack of due dates on current open tasks and the team's feedback suggests internal prioritization is driving the schedule, not external customer commitments (except NASA S2, which has passed QC).

- **Release candidate bottleneck:** 8 aircraft systems awaiting release candidate testing, all assigned to Spencer Hoehl with no due dates. This is the active work stream.

- **Known aircraft issues (partially resolved):**
  - S10019: Autopilot altitude loss during hand-launch (maintenance required; QC'd 2026-08-04)
  - S10020: Mag signal drop and ESC power loss during VTOL transition (QC'd 2026-08-21 & 2026-08-25)
  - S0 VTOL: MAG signal not sending; params not saving (completed 2026-10-01 despite 2026-08-28 due date)
  - S30001: Rear motor spin-up issue in auto mode (completed 2026-07-21)
  - ERAU E2: Instability unresolved as of 2026-09-29; ready for further investigation

- **Custom field usage:** Tasks consistently tagged with flight status ("Ready for Flight Testing", "More Info Requested", "Passed", "Maintenance Required", "In Design") and QC requirements, enabling workflow tracking.