# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; critical deadline Jun 28, 2026
- **Status:** **🔴 CRITICAL COLLAPSE — ACTIVE BUT SEVERELY DEGRADED.** Task list has collapsed from 3 open tasks (prior cycle) to **1 open task (67% reduction in 1 cycle).** Two Amazon orders (due Jun 27–28) have disappeared from task list without documented closure, completion records, or archival. **Form-based auto-delete mechanism confirmed as active.** This creates severe audit trail and compliance risk.

- **Team members involved:**
  - **Meredith O'hara Needham** (project owner; 0/1 current open tasks assigned)
  - **Nate Straus** (1/1 current open tasks assigned; 100% of current workload)
  - **Requesters:** Alex (1 task)

- **Risk signals:**
  - 🔴 **CATASTROPHIC TASK LOSS:** Open tasks collapsed 67% in one cycle (3 → 1). Prior Amazon orders (due Jun 27–28, assigned to Meredith) now completely absent from task list. **No closure notes, completion records, or archival documentation.** 
  - 🔴 **AUDIT TRAIL DESTROYED BY DESIGN:** Project notes confirm form-based auto-delete: `"YOUR TASK WILL AUTO DELETE"` if orders placed via form. This means **no historical record of order placement, vendor receipt, requester, project billing, or cost.** Creates compliance/SOX/audit risk if order records required for financial reconciliation or project cost tracking.
  - 🔴 **UNKNOWN OPERATIONAL STATE:** Cannot determine whether missing Amazon orders were placed externally (form auto-deleted tasks), cancelled, merged, or lost due to system error. **Requires immediate reconciliation.**
  - 🟡 **IMMINENT DEADLINE:** Remaining task (Sendcutsend) due Jun 28, 2026.

## Key Deliverables & Milestones

### **DUE JUN 28, 2026 — 1 Task**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Notes |
|------|-----|--------|----------|---------|-----------|--------|-------|
| Sendcutsend (#S1841769) | Jun 28, 2026 | Sendcutsend | Nate Straus | [550-1] Navy SBIR: Magnetometer | Alex | Order Received | Originally requested Jun 17 |

## Task Summary

- **Total tasks:** 1 open, 0 completed
  - **1 assigned to Nate Straus** (100%)

- **Tasks by assignee:**
  - **Nate Straus:** 1/1 (100%)

- **Requester distribution:**
  - **Alex:** 1/1 (Sendcutsend)

- **Status breakdown:**
  - **Order Received:** 1 (Sendcutsend)

- **Notable patterns:**
  - **Extreme workload concentration:** 100% of open tasks assigned to Nate (vs. 67% to Meredith in prior cycle)
  - **Dramatic task list contraction:** 3 → 1 open tasks (67% reduction) in single cycle
  - **Project owner (Meredith) has zero current assignments** — suggests either external order handling or task auto-deletion without reassignment

## Recent Activity

- **🔴 TASK COLLAPSE:** Two Amazon orders (Amazon weights, Amazon Shop supplies—both due Jun 27–28, assigned to Meredith O'hara Needham per prior cycle) have vanished from current task list **without documented closure, completion, or archival.**
  - **Likely explanation:** Form-based auto-delete mechanism (`"YOUR TASK WILL AUTO DELETE"` per project notes) triggered when orders placed via form, silently removing Asana task from task list. **This destroys audit trail — no record of order placement, cost, requester, or project billing.**
  - **ALTERNATIVE EXPLANATIONS UNCONFIRMED:** Orders cancelled, externally placed, or system error.
- **Sendcutsend persists:** Single remaining task (Sendcutsend #S1841769, status "Order Received," due Jun 28) still assigned to Nate Straus. Confirms continued project activity but minimal workload visibility.
- **No recent completion activity documented** in available data; prior cycle's 6 tasks reduced to current 1 without closure notes.

## Notes & Context

- **FORM AUTO-DELETE CREATES COMPLIANCE/AUDIT RISK:** Project explicitly instructs users: `"USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE"` (from project notes). This design removes Asana task from system when order is submitted via form, **eliminating any historical record of:**
  - Order placement date and requester
  - Project billing allocation
  - Vendor and cost
  - Order confirmation or receipt
  
  **RECOMMENDATION:** Establish complementary order management system (e.g., procurement log, vendor portal audit, or Asana form response archive) to preserve financial and operational records independent of auto-deleted tasks.

- **OPERATIONAL VISIBILITY COLLAPSE:** With 1 of 3 prior tasks remaining visible, cannot assess:
  - Whether Amazon orders were successfully placed and received
  - Project billing (prior "Shop Supplies" task showed project field discrepancies)
  - Cost and vendor status
  - Cause of task disappearance (form submission vs. cancellation vs. external system)

- **PROJECT OWNER WORKLOAD MISMATCH:** Meredith O'hara Needham is project owner but has zero current open task assignments. Prior cycle showed 67% workload concentration (2/3 tasks). Suggests either:
  - Orders placed via form and auto-deleted, removing visible assignments
  - Workload shifted externally (vendor portal, procurement tool)
  - Project slowdown or hiatus

- **Single Point of Failure Persists:** 100% of current visible workload assigned to Nate Straus (vs. prior 33%). Extremely narrow operational window if Nate becomes unavailable.

- **IMMEDIATE ACTIONS REQUIRED:**
  1. **AUDIT AMAZON ORDERS:** Confirm status of prior Amazon weights and Shop supplies tasks due Jun 27–28. Check order confirmation emails, vendor accounts, and receipts to determine actual placement status.
  2. **RECONCILE FORM AUTO-DELETE:** Verify whether form submissions auto-deleted Amazon tasks or if disappearance due to other cause (cancellation, system error, manual archival).
  3. **ESTABLISH AUDIT TRAIL:** If form auto-delete is intentional design, implement complementary order log or Asana form response archive to preserve financial and operational records.
  4. **CLARIFY BILLING PROJECTS:** Resolve prior discrepancy between "Shop Supplies" task and "[001-1] IRAD General" project field.