# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders spanning June 5–12, 2026
- **Status:** **ACTIVE — CRITICAL DATA CORRECTION FROM PRIOR CYCLE.** New dataset shows **6 open tasks** (down from 15 reported in prior update). **MAJOR DISCREPANCY RESOLVED:** Prior cycle reported 15 tasks including recovered jawstec/DataPro/Mouser/SendCutSend items with August 8 due dates. **Current dataset shows those extended-date tasks have been removed from Asana.** Only **6 near-term tasks remain** (all due June 7–12, 2026). **INTERPRETATION:** Prior cycle's "data integrity issue" appears to have self-corrected—extended-inventory tasks were likely removed by form auto-deletion system or manual cleanup. **HOWEVER:** Two jawstec tasks (#69219, #69119) and one 18650batterystore task (#549011) remain open with June due dates and "Order Shipped" status, indicating orders are in transit but still marked incomplete in Asana. **ACTION:** Verify receipt and close these shipped orders.

- **Team members involved:**
  - **Meredith O'hara Needham** (6/6 assigned tasks; order placement role; project owner)
  - **Joshua Fromm** (3/6 as requester; S3 sales and parts focus)
  - **Nate Straus** (1/6 as requester)
  - **Alex** (1/6 as requester)
  - **Dan Prendergast** (1/6 as requester)

- **Risk signals:**
  - 🔴 **CRITICAL:** Two tasks marked "Order Shipped" but still open in Asana: **jawstec for s3 parts (#69119, due June 7)** and **18650batterystore (#549011, due June 11)**. These orders are in transit but task completion has not been tracked. **ACTION REQUIRED:** Confirm receipt dates and close tasks immediately upon delivery.
  - 🟡 **IMMINENT DEADLINE PRESSURE:** Four tasks due within 48 hours of current snapshot (June 10–12 "When should this order be placed?" dates, actual due dates June 7–12). All assigned to Meredith O'hara Needham. **Recommend:** Verify all four are placed and track receipt proactively.
  - 🟡 **Single-point-of-failure assignment:** Meredith O'hara Needham holds 6/6 assigned tasks (100%). If Meredith is unavailable, all purchasing workflow halts. **Recommend:** Cross-train or establish backup assignment protocol.
  - 🟡 **Project billing gaps:** Two tasks lack specific project allocation: **jawstec for s3 parts - SALES (#69219)** and **18650batterystore (#549011)** both show "General Sales (No Specific Project)." Tax-exempt purchases require accurate project billing for audit/cost allocation. **ACTION:** Contact Joshua Fromm to confirm whether these sales are for [001-7] IRAD S3 or external sales channel.

## Key Deliverables & Milestones

### **IMMINENT (June 7–12, 2026) — 6 Tasks**

| Task | Due | Assigned | Project | Requester | Status | Tax Exempt | Notes |
|------|-----|----------|---------|-----------|--------|-----------|-------|
| jawstec for s3 parts (#69119) | Jun 7, 2026 | Meredith O'hara Needham | [001-7] IRAD S3 | Joshua Fromm | **Order Shipped** | YES | **OVERDUE** — in transit, needs receipt confirmation & closure |
| uni USB C to Ethernet Adapter | Jun 11, 2026 | Meredith O'hara Needham | [001-7] IRAD S3 | Dan Prendergast | Order Placed | NO | Order placed Jun 8 |
| 18650batterystore for s3 sales (#549011) | Jun 11, 2026 | Meredith O'hara Needham | General Sales | Joshua Fromm | **Order Shipped** | YES | **PROJECT UNSPECIFIED** — needs allocation; in transit |
| jawstec for s3 parts - SALES (#69219) | Jun 12, 2026 | Meredith O'hara Needham | General Sales | Joshua Fromm | Order Placed | YES | **PROJECT UNSPECIFIED** — needs allocation; placed Jun 9 |
| Amazon Shop supplies | Jun 12, 2026 | Meredith O'hara Needham | [001-1] IRAD General | Nate Straus | Order Placed | NO | Placed Jun 9 |
| Amazon | Jun 12, 2026 | Meredith O'hara Needham | [001-7] IRAD S3 | Alex | Order Placed | NO | Placed Jun 10 |

## Task Summary
- **Total tasks:** 6 open, 0 completed
- **Assignee breakdown:**
  - Meredith O'hara Needham: 6/6 (100%) — **single point of failure**
  - All requesters (Joshua Fromm, Nate, Alex, Dan Prendergast): appear only as requester field, not assignee
- **Status breakdown:**
  - Order Shipped: 2 tasks (33%) — require receipt confirmation
  - Order Placed: 4 tasks (67%) — in transit or awaiting confirmation
- **Project allocation:**
  - [001-7] IRAD S3: 3 tasks
  - [001-1] IRAD General: 1 task
  - General Sales (unspecified): 2 tasks ⚠️

## Recent Activity
- **Prior Cycle → Current Cycle Transition:** Prior update reported 15 open tasks with extended August 8 due dates (DataPro, Mouser ×2, PCBWay, Amazon/Hurricane, ARK Electronics, SendCutSend). **Current dataset shows only 6 tasks; all extended-date tasks removed.** Suggests prior cycle data included recovered/orphaned tasks that were subsequently cleaned up or auto-deleted by form system.
- **Status Updates:** Two jawstec/battery tasks now show "Order Shipped" (previously "Order Placed in Inventory" in prior cycle), indicating orders are in transit. However, tasks remain open—likely awaiting receipt confirmation.
- **Timeline Correction:** All current tasks have realistic near-term due dates (June 7–12, 2026) aligned with order-placement intent, suggesting form auto-deletion system has successfully removed stale/orphaned inventory-hold tasks from prior cycle.

## Notes & Context
- **Form-Based Task Management:** Project uses form submission for purchasing requests with auto-deletion feature. Prior cycle showed anomalous data (15 tasks with extended dates); current cycle shows cleaner state with only active near-term orders.
- **Tax-Exempt Tracking:** 4/6 tasks marked tax-exempt (jawstec ×2, 18650batterystore). Require accurate project allocation for compliance audit.
- **Joshua Fromm Requester Concentration:** 3/6 current tasks (50%) requested by Joshua Fromm (all S3 sales/parts related). Indicates S3 sales pipeline is primary purchasing driver in current cycle.
- **Missing Project Specifications:** Two sales-related tasks lack specific project allocation ("General Sales"). **ACTION:** Clarify whether these are [001-7] IRAD S3 sales or external customer sales; affects billing and cost allocation.
- **Shipped Orders Not Closed:** Two tasks marked "Order Shipped" remain open, indicating Asana workflow does not automatically close upon shipment confirmation. **Recommend:** Establish receiving/closure protocol to prevent stale open-task accumulation.