_Asana snapshot as of 2026-11-02: 10 open tasks, 15 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer:** Internal BST flight testing operations; includes work for ByLight (Mustang) and NASA (S2 platform)
- **Dollar value:** Not specified in task data
- **Timeline:** Ongoing; most recent activity Oct 14–16, 2026
- **Status:** Active — 10 open tasks, 15 recently completed; no stale due dates blocking progress
- **Team members involved:** Spencer Hoehl (primary test pilot), Alex Lomis, Ethan Domagala, Maciej Stachura
- **Risk signals:** No overdue tasks; however, team feedback (Daniel Prendergast, Oct 15–16) indicates ongoing friction — quote: *"Mine's correct. Stop hazing me, Mr. Flight Director."* Context unclear but suggests interpersonal tension that may affect workflow.

## Key Deliverables & Milestones
No formal milestones with dollar amounts or fixed end dates. Work is organized by aircraft platform and firmware release cycles:

- **Release Candidate Testing (multiple platforms):** S20003, E20006, S10021, S10022, FW0001, FW0005, S10011, FW0002 — all open, no due dates, marked "Ready for Flight Testing"
- **ERAU E2 Instability Investigation** — ongoing, no due date; investigation as of 9/29 found issue could not be reproduced with/without wind sensor mast
- **Swiftab App Release Candidate** — open, uploaded, awaiting testing
- **Recent completions:** S10022 VTOL flights (Oct 14), S10021 VTOL QC (Oct 14), Soil Moisture E2 (Oct 5), NASA S2 QC (Sep 21, passed), ByLight Mustang (Sep 22, completed on time)

## Task Summary
- **Total:** 10 open, 15 completed
- **Primary assignee:** Spencer Hoehl carries ~90% of both open and completed workload
- **Secondary contributors:** Alex Lomis (2 tasks), Ethan Domagala (1 task, ByLight), Maciej Stachura (1 task, autopilot)
- **Completion rate:** 60% overall (15/25); suggests steady throughput with large backlog of RC testing queued
- **Status field usage:** "Ready for Flight Testing" is predominant on open tasks; completed tasks show mixed statuses ("More Info Requested," "Passed," "Maintenance Required")

## Recent Activity
- **Oct 14:** Spencer completed two VTOL firmware QC flights (S10022, S10021), both marked "More Info Requested" — suggests results may need review
- **Oct 9:** S1 fixed wing and FlameWheel QC flights completed
- **Oct 5:** Soil Moisture E2 sensor testing flight completed
- **Oct 1:** General firmware QC flight (S1/FW) and S0 VTOL work completed (S0 was overdue by ~1 month from Aug 28 target but no escalation noted)
- **Sep 21–22:** NASA S2 QC passed; ByLight Mustang completed (was due Sep 18, delivered Sep 22)
- **Aug–Sep:** Heavy QC and maintenance cycle on multiple platforms (S10019, S10020, Flamewheel, S1 Fixed Wing)

## Notes & Context
- **No due dates:** Almost all open tasks lack due dates, suggesting Spencer manages a rolling test queue rather than time-boxed milestones
- **Firmware/RC pattern:** Many open tasks are release candidate testing for same platform (S10021, S10022, etc.) — likely parallel validation for different radio or motor configurations
- **Incomplete notes:** Several task notes are truncated in source data (e.g., S0 VTOL, S10019 Autopilot), indicating ongoing investigation work
- **QC field:** "QC Required" flag is sparse but used inconsistently; not a strong control mechanism
- **Team friction:** Daniel Prendergast's feedback (Oct 15–16) suggests conflict with Flight Director role; unclear if this affects task assignment or priority, but worth monitoring
- **External customers:** ByLight and NASA work completed on or near schedule; internal BST test cycles have no formal deadlines

---

**Note:** This project operates as a continuous flight test pipeline with no formal release gates or dollar budgets visible in task data. Spencer Hoehl is a potential bottleneck for scheduling and execution.