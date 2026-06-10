# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders spanning June 9–August 8, 2026
- **Status:** **ACTIVE — CRITICAL DATA INCONSISTENCY DETECTED.** Current dataset shows **15 open tasks** (up from 1 in prior update). This represents a **1500% increase in single update cycle**. **URGENT VERIFICATION REQUIRED:** Prior update reported 4 jawstec tasks "removed from Asana" with status "Order Received" due June 7. Current update shows these same 4 jawstec tasks are now **back in Asana with status changed to "Order Placed in Inventory" and due dates extended to August 8, 2026.** Additionally, 7 new/recovered tasks have appeared (DataPro, Mouser items, SendCutSend, Amazon/Hurricane). **CRITICAL:** Determine whether (1) form auto-deletion system reversed course and restored tasks; (2) data sync error occurred; (3) tasks were externally managed and re-imported; (4) prior cycle report was incorrect about "removal."

- **Team members involved:**
  - **Meredith O'hara Needham** (4/15 assigned tasks; order placement role; project owner)
  - **Nate Straus** (0/15 assigned; but appears as requester on 4 tasks)
  - **Joshua Fromm** (5/15 tasks as requester; dominant requester, recovered from prior cycle absence)
  - **Dan Prendergast** (1/15 as requester)
  - **Alex** (3/15 as requester; NEW to current cycle)
  - **Ethan** (1/15 as requester; NEW to current cycle)
  - **Unassigned:** 11/15 tasks (73% of backlog unassigned; critical operational gap)

- **Risk signals:**
  - 🔴 **CRITICAL DATA INTEGRITY ISSUE:** Prior update reported 4 jawstec tasks "removed from Asana." Current update shows all 4 jawstec tasks present with **materially changed metadata** (status changed from "Order Received" → "Order Placed in Inventory"; due dates extended from June 7 → August 8). **IMMEDIATE ACTION:** (1) Verify whether orders were actually received/placed by June 7 as prior cycle indicated; (2) confirm status change rationale (order delay? tracking system change?); (3) audit form auto-deletion system behavior; (4) determine if prior cycle report was based on stale snapshot or data loss event.
  - 🔴 **CRITICAL UNRESOLVED TASK:** jawstec for multiple projects (#68821) — **now showing 49+ days overdue** (ordered May 20; currently due August 8 in Asana but order date was May 20). Status: "Order Placed in Inventory." Project field: still incomplete ("M" — "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN"). **MUST RESOLVE:** Obtain actual receipt date, verify order was fulfilled, provide project allocation breakdown, and properly close/document.
  - 🔴 **MASSIVE BACKLOG CREATED IN SINGLE CYCLE:** 15 open tasks created/recovered between prior and current updates. **11/15 unassigned (73%).** Meredith is single point of failure (4/15 assigned; all others unassigned). Suggests either: (1) major purchasing push with incomplete assignment; (2) system backlog surfaced after form/auto-deletion fixes; (3) historical orders recovered and re-queued.
  - 🔴 **CRITICAL UNRESOLVED MULTI-PROJECT ALLOCATION:** jawstec #68821 (May 20 order, status "Order Placed in Inventory," tax-exempt, Joshua Fromm requester) still has incomplete project field ("M"). **ACTION REQUIRED:** Contact Joshua Fromm to provide project breakdown for audit/billing purposes before order can be reconciled.
  - ⚠️ **Extended due dates suggest delivery delays or inventory hold:** 7 tasks (DataPro, Mouser ×2, PCBWay, Amazon/Hurricane, ARK Electronics, SendCutSend) all have **August 8, 2026 due dates** despite being placed/ordered in May–June. Suggests either: (1) long lead-time items (expected behavior); (2) on-hand inventory hold pending project allocation; (3) orders not yet shipped. **Recommend:** Verify actual ship/delivery dates with vendors.
  - ⚠️ **Requester concentration partially recovered but unstable:** Joshua Fromm (5/15 = 33% of requests; returned from prior cycle absence). Nate (4/15 requests). New requesters Alex (3) and Ethan (1) have appeared. **Improved diversification vs. prior single-requester cycles, but Joshua still dominates.**
  - ⚠️ **Assignment concentration at risk:** Meredith O'hara Needham (4/15 assigned = 27%). **11/15 tasks unassigned.** If Meredith is order-placement role and backlog continues to grow, assignment bottleneck likely.

## Key Deliverables & Milestones

### **Immediate Cycle (June 9–11, 2026) — 4 Tasks Due**

1. **Amazon Shop supplies** | Due June 9, 2026 | Assigned: Meredith O'hara Needham | Project: [001-1] IRAD General | Requires Approval: NO | Tax Exempt: NO | Requester: Nate | Vendor: Amazon Shop supplies

2. **jawstec for s3 parts - SALES** | Due June 9, 2026 | Assigned: Meredith O'hara Needham | Project: General Sales (No Specific Project) | Requires Approval: NO | Tax Exempt: YES | Requester: Joshua Fromm | Vendor: jawstec

3. **18650batterystore for s3 sales (#549011)** | Due June 11, 2026 | Assigned: Meredith O'hara Needham | Project: General Sales (No Specific Project) | Status: Order Placed | Requires Approval: NO | Tax Exempt: YES | Requester: Joshua Fromm | Vendor: 18650batterystore

4. **uni USB C to Ethernet Adapter** | Due June 11, 2026 | Assigned: Meredith O'hara Needham | Project: [001-7] IRAD S3 | Status: Order Placed | Requires Approval: NO | Tax Exempt: NO | Requester: Dan Prendergast | Vendor: uni USB C to Ethernet Adapter

### **Extended Cycle (August 8, 2026 — 11 Tasks) — Inventory Hold or Long Lead-Time**

All 11 tasks below have **due date August 8, 2026** and **status "Order Placed in Inventory."** Actual order placement dates span **May 11–June 4, 2026**. **These appear to be backlogged inventory or delayed shipments.**

| Task | Project | Requester | Order Placed | Tax Exempt | Notes |
|------|---------|-----------|--------------|-----------|-------|
| DataPro / Hurricane GCS (#605111011462) | [300-3] 2026 IDIQ (Hurricane) | Nate | May 11, 2026 | NO | **UNASSIGNED** |
| Mouser / Hurricane GCS (#39155920) | [300-3] 2026 IDIQ (Hurricane) | Nate | May 11, 2026 | NO | **UNASSIGNED** |
| Mouser (#39225140) | General Sales | Alex | May 18, 2026 | NO | **UNASSIGNED** |
| PCBWay (#YE1730257) | [001-7] IRAD S3 | Alex | May 12, 2026 | NO | **UNASSIGNED** |
| Amazon / Hurricane GCS | [300-3] 2026 IDIQ (Hurricane) | Nate | May 11, 2026 | NO | **UNASSIGNED** |
|