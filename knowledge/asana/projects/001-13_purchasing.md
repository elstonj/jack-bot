# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; orders due Jun 25–28, 2026
- **Status:** **ACTIVE — CRITICAL WORKLOAD CONCENTRATION PERSISTS; TASK COUNT COLLAPSED 50%.** ⚠️ **KEY CHANGES FROM PRIOR CYCLE:**
  - **DRAMATIC TASK REDUCTION:** Open tasks fell from 6 to **3 (50% decrease)** in current cycle. **Prior near-duplicates and JawsTec gimbal task have disappeared from task list — no documentation of resolution, merge, or archival.** Suggests either external closure or silent task deletion without audit trail.
  - **WORKLOAD REBALANCING PARTIALLY SUSTAINED:** Sendcutsend remains assigned to **Nate Straus** (due Jun 28, status "Order Received") — first delegation still in effect.
  - **SINGLE-POINT-OF-FAILURE RE-CONCENTRATED:** **2 of 3 tasks (67%) assigned to Meredith O'hara Needham.** Combined with 50% task reduction, suggests possible external handling or project slowdown, not healthy workload distribution.
  - **NEAR-DUPLICATE AMAZON TASKS DISAPPEARED:** "amazon for shop supplies" (Joshua Fromm) and prior "digikey for idiq" tasks no longer in list — **unconfirmed whether resolved, merged, or archived.**
  - **IMMINENT DEADLINES:** All 3 remaining tasks due Jun 27–28 (within 1–3 days). Compressed timeline persists.

- **Team members involved:**
  - **Meredith O'hara Needham** (2/3 assigned; 67% of open workload; project owner)
  - **Nate Straus** (1/3 assigned; 33% of open workload)
  - **Requesters:** Nate (2 tasks), Alex (1 task)

- **Risk signals:**
  - 🔴 **TASK DISAPPEARANCE WITHOUT DOCUMENTATION:** 3 of 6 prior tasks now absent from task list (50% reduction). Prior cycle flagged "amazon for shop supplies" (Joshua Fromm, due Jun 26) and "digikey for idiq" (due Jun 26) as active. **Current data shows only 3 tasks; no closure notes, completion records, or archival explanation.** Possible causes:
    - External order placement (form-based system may bypass Asana task lifecycle)
    - Silent task deletion (form auto-delete referenced in project notes)
    - Manual cleanup without audit trail
    - **ACTION REQUIRED:** Confirm whether orders were placed externally and tasks auto-deleted per form rules, or if data integrity issue exists.
  - 🟠 **SINGLE-POINT-OF-FAILURE RE-CONCENTRATED:** 2 of 3 tasks (67%) assigned to Meredith. Prior cycle showed delegation progress; current reduction suggests either project slowdown or external handling without task updates.
  - 🟡 **IMMINENT DEADLINES:** All 3 tasks due Jun 27–28; minimal execution buffer.
  - 🟡 **FORM SUBMISSION AUTO-DELETE MECHANISM ACTIVE:** Project notes state "YOUR TASK WILL AUTO DELETE" if form not used. This explains task disappearance but creates audit trail risk — no historical record of order placement, requester, or project billing.

## Key Deliverables & Milestones

### **DUE JUN 27–28, 2026 — 3 Tasks**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Notes |
|------|-----|--------|----------|---------|-----------|--------|-------|
| Amazon weights | Jun 27, 2026 | Amazon | Meredith O'hara Needham | [001-1] IRAD General | Nate | Order Placed | Requested for Jun 26 placement |
| Amazon Shop supplies | Jun 27, 2026 | Amazon | Meredith O'hara Needham | Shop Supplies (form says [001-1] IRAD General) | Nate | Order Placed | Requested for Jun 25 placement; billing project discrepancy noted |
| Sendcutsend (#S1841769) | Jun 28, 2026 | Sendcutsend | Nate Straus | [550-1] Navy SBIR: Magnetometer | Alex | Order Received | Originally requested Jun 17 |

## Task Summary

- **Total tasks:** 3 open, 0 completed
  - **2 assigned to Meredith O'hara Needham** (67%)
  - **1 assigned to Nate Straus** (33%)

- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 2/3 (67%)
  - **Nate Straus:** 1/3 (33%)

- **Requester distribution:**
  - **Nate:** 2/3 (Amazon weights, Amazon Shop supplies)
  - **Alex:** 1/3 (Sendcutsend)

- **Status breakdown:**
  - **Order Placed:** 2 (Amazon weights, Amazon Shop supplies)
  - **Order Received:** 1 (Sendcutsend)

- **Notable patterns:**
  - Amazon vendor concentration: 2/3 tasks (67%)
  - **Significant task reduction (6 → 3, 50% decrease)** — prior near-duplicate and multi-project tasks now absent
  - **Workload rebalancing partially sustained:** Nate retains Sendcutsend delegation; however, concentration to Meredith on remaining 2 tasks suggests externally-placed orders or form auto-deletion without task closure documentation

## Recent Activity

- **Task list collapsed 50%** from prior cycle (6 → 3 open tasks). No closure notes or completion records for disappeared tasks. **Likely explanation:** Form-based auto-delete mechanism (`"YOUR TASK WILL AUTO DELETE"` per project notes) triggered when orders placed via form, removing Asana task without audit trail. **This creates compliance/audit risk if order records need historical retrieval.**
- **Nate Straus delegation sustained:** Sendcutsend (Order Received, due Jun 28) remains assigned to Nate, confirming prior cycle's workload rebalancing attempt.
- **All remaining tasks imminent:** Due Jun 27–28; execution phase active.
- **Billing project discrepancy:** "Amazon Shop supplies" form shows project as both "Shop Supplies" (task title) and "[001-1] IRAD General" (form field) — requires reconciliation.

## Notes & Context

- **Form submission mechanism with auto-delete creates audit trail gap:** Project notes state form link and threat of auto-deletion. This explains task disappearance but means **no historical record of orders placed via form.** Recommend:
  - Confirm whether external order management system (e.g., vendor portal, procurement tool) is handling placed orders while Asana tasks are auto-deleted
  - If using form auto-delete, establish complementary order log or archive to preserve audit trail
  - Update project documentation to clarify task lifecycle (form submission → order placement → task auto-delete vs. manual closure)

- **Billing project tagging inconsistencies:** "Amazon Shop supplies" (Nate's request) shows conflicting project assignments in task title vs. form field. Verify whether Shop Supplies is a valid billing project or if all orders should bill to [001-1] IRAD General.

- **Requesters vs. assignees:** All 3 current tasks requested by Nate (2) or Alex (1), but only Sendcutsend assigned to requesting-adjacent team member (Nate). Amazon tasks remain with Meredith despite coming from Nate. Suggests Meredith is purchase order handler independent of requester.

- **Prior cycle unresolved items now absent:**
  - "digikey for idiq" (Joshua Fromm, due Jun 26, "Order Shipped") — not in current data
  - "amazon for shop supplies" (Joshua Fromm, due Jun 26, "Order Placed") — not in current data
  - "Amazon Lava Lamp bulb" (Et