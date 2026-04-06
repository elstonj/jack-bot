# [001-02] E2 IRAD & Fleet Maintenance

## Overview
- **Client/customer:** Internal BST project (IRAD - Independent Research and Development)
- **Dollar value:** Not specified
- **Timeline:** Ongoing maintenance project, no defined end date
- **Status:** Active (low priority) — recent completions on 2025-01-13, but minimal forward momentum
- **Team members involved:** Nate Straus (owner/project lead), Jack Elston (primary technical assignee)
- **Risk signals:** 
  - 4 unassigned fleet maintenance tasks (E20006, E20009, E20013, E20014) with no owners
  - 0 due dates set across all open work — makes prioritization and accountability unclear
  - Low priority designation may indicate deprioritization relative to other BST work

## Key Deliverables & Milestones
- **Electronic integration guide** — dependent on completion of mechanical guide (Jack Elston)
- **Image preview / video downlink capability** — technical feature (Jack Elston)
- **Fan speed control via PSB implementation** — uses Delta FFB0412EN-00Y2E fan spec (Jack Elston)
- **Fleet maintenance:** Four E2 units requiring work (E20006, E20009, E20013, E20014) — currently unassigned

## Task Summary
- **Total tasks:** 7 open, 2 completed (22% overall completion)
- **Tasks by assignee:**
  - Jack Elston: 3 open tasks (100% of his assigned work still pending)
  - Nate Straus: 0 open, 2 completed (100% closure rate on his work)
  - Unassigned: 4 open tasks (fleet units E20006, E20009, E20013, E20014)
- **Notable patterns:** 
  - Clear split: Nate handles ad-hoc fixes (e.g., configuration corrections), Jack owns new feature development
  - Fleet maintenance tasks lack ownership — potential bottleneck
  - All work is open-ended (no due dates), suggesting informal scheduling

## Recent Activity
**2025-01-13** — Last activity (Nate Straus completions):
- Fixed configuration parameters for E20009 (unit was running backwards)
- Located antenna for E20009

No activity recorded since then.

## Notes & Context
- Project is tagged **Low Priority** within BST's portfolio — may explain lack of urgency and missing due dates
- **E20009 appears to be the recent focus** (2 fixes completed in one day), but now has an unassigned maintenance task
- Jack Elston's 3 open tasks are all technical/integration work, not hardware maintenance
- **Unassigned fleet tasks need owner assignment** to clarify accountability and unblock progress
- Delta fan specification included in fan speed control task (technical reference available)
- Mix of hardware maintenance (fleet units) and software/integration work (guides, downlink, PSB control)