# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; orders due Jun 22–23, 2026
- **Status:** **ACTIVE — CRITICAL RECOVERY.** Task count rebounded from 1 to **5 open tasks**. ⚠️ **Previous critical failures (form-based auto-closure, auto-deletion, task disappearance) appear to have been resolved or reversed.** However, **all 5 new tasks are assigned to Meredith O'hara Needham exclusively** (100% concentration) — a dramatic shift from prior single-point-of-failure pattern under Nate Straus. All orders are imminent (due Jun 22–23, 2026). **Prior task "sendcutsend #SC51C906" has been removed from the system** — status unclear (legitimate closure vs. auto-deletion).
- **Team members involved:**
  - **Meredith O'hara Needham** (5/5 assigned; 100% of open workload; project owner)
  - **Requesters:** Alex (3 tasks), Nate (1 task), Ethan (1 task)

- **Risk signals:**
  - 🔴 **NEW SINGLE-POINT-OF-FAILURE RISK: MEREDITH 100% OF OPEN TASKS** — All 5 orders now assigned exclusively to Meredith (project owner). No distribution to team. If Meredith is unavailable Jun 22–23, all orders will stall.
  - 🟡 **IMMINENT DEADLINES (JUN 22–23, 2026)** — 5 orders due within 1–2 days. No buffer for delays or approvals.
  - 🟡 **PRIOR TASK VANISHED** — sendcutsend #SC51C906 (which was "Order Received" and 18+ days stale) no longer appears in task list. Unknown if legitimately closed, auto-deleted, or removed manually.
  - 🟡 **FORM-BASED AUTO-CLOSURE STILL UNCLEAR** — No evidence that prior form mechanism failures have been fixed; new tasks may be vulnerable to same closure/deletion issues.

## Key Deliverables & Milestones

### **DUE JUN 22–23, 2026 — 5 Tasks**

| Task | Due | Vendor | Assigned | Project | Requester | Approval Required? | Tax Exempt? |
|------|-----|--------|----------|---------|-----------|-------------------|------------|
| McMaster | Jun 22, 2026 | McMaster | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | No | No |
| GetFPV | Jun 22, 2026 | GetFPV | Meredith O'hara Needham | Shop Supplies | Alex | No | No |
| Digikey (GCS wifi) | Jun 23, 2026 | Digikey | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | No | No |
| Jawstec | Jun 23, 2026 | Jawstec | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | No | No |
| JawsTec - ByLight Gimbal | Jun 23, 2026 | JawsTec | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | No | No |

## Task Summary

- **Total tasks:** 5 open, 0 completed (rebounded from 1 open task in prior cycle; **+400% increase**)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 5/5 (100%) — all five orders
- **Requester distribution:**
  - **Alex:** 3/5 (McMaster, GetFPV, Jawstec)
  - **Nate:** 1/5 (Digikey GCS wifi)
  - **Ethan:** 1/5 (JawsTec ByLight Gimbal)
- **Projects covered:**
  - [550-1] Navy SBIR: Magnetometer (2 tasks)
  - [300-3] 2026 IDIQ (Hurricane) (1 task)
  - [043-3] Mustang Pt. 2 (1 task)
  - Shop Supplies (1 task)

## Recent Activity

- **Dramatic task rebound:** 5 new open tasks added (up from 1). All are assigned to Meredith O'hara Needham (project owner).
- **Prior task removed:** sendcutsend #SC51C906 (status: "Order Received", due Jun 21, 18+ days stale) is no longer visible in Asana task list. Unknown whether legitimately closed, auto-deleted by form policy, or manually removed. **Requires clarification.**
- **All orders imminent:** Due dates clustered at Jun 22–23, 2026 (within 1–2 days of current observation). No buffer for delays or approval cycles.
- **No approvals required:** All 5 orders marked "Requires Approval?: No" — suggests pre-approval or expedited purchasing.
- **Tax exempt status:** None of the 5 orders marked as tax-exempt (unlike prior sendcutsend task which was tax-exempt).

## Notes & Context

- **URGENT ACTIONS:**
  1. **Distribute purchasing workload from Meredith immediately.** All 5 orders are due Jun 22–23; Meredith alone cannot execute in time. Assign tasks to Nate Straus and/or other team members based on vendor/project affinity.
  2. **Clarify fate of sendcutsend #SC51C906.** Determine if task was:
     - Legitimately closed and removed (expected behavior), OR
     - Auto-deleted by form policy (indicating prior warnings about auto-deletion were accurate), OR
     - Manually removed.
     This is critical for understanding whether form-based auto-closure/auto-deletion mechanism is still active and dangerous.
  3. **Verify form-based auto-closure mechanism status.** New tasks do not show any "Order Placed" or "Order Received" status flags yet. Confirm whether:
     - Form mechanism is now functional (e.g., will auto-close tasks when orders are placed), OR
     - Mechanism is still broken (requiring manual closure), OR
     - Has been disabled pending redesign.
  4. **Monitor for project field truncation.** Prior tasks showed truncated project names (e.g., "Genera", "[300-3] 2026 IDIQ ("). Verify new tasks display full project names correctly in billing system.

- **Workload concentration risk:** Meredith O'hara Needham (project owner) is now holding 100% of open purchasing tasks. This is unsustainable and represents a single point of failure. Recommend:
  - Immediate delegation of 2–3 tasks to Nate Straus (who previously handled purchasing orders).
  - Clear escalation plan if Meredith is unavailable Jun 22–23.

- **Form policy reminder:** Project notes state "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE" with link to Asana form. All 5 current tasks appear to have been created via form (they have structured notes with vendor, requester, project, and due date fields). Monitor whether form mechanism properly auto-closes tasks upon order placement, or whether manual closure will again be required.