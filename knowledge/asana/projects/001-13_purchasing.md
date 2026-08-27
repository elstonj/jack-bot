# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across 10+ active projects
- **Timeline:** Ongoing operational project. **Critical compressed deadlines through Aug 27, 2026.** Current snapshot shows 7 open tasks; all due Aug 27–28.
- **Status:** 🟡 **SIGNIFICANT REDUCTION FROM CRISIS STATE.** Open task count has dropped from 45 to 7 (85% decrease). **This represents either:**
  - (a) **Successful batch closure** — Meredith and Nate completed 38 orders since last snapshot, OR
  - (b) **Data synchronization event** — prior snapshot captured orphaned/stale tasks that have now been cleaned up.
  - **VERIFY:** Confirm with Meredith/Nate whether this reflects real completion or system correction. If real completion, purchasing pipeline capacity has recovered significantly.
  - **Current state appears more manageable:** 7 tasks ÷ 2 staff = 3.5 tasks/person; assuming 30-min processing per task = ~1.75 hours work remaining. **However, all tasks are due in final 48 hours (Aug 27–28), suggesting end-of-sprint urgency rather than breathing room.**
- **Team members involved:**
  - **Meredith O'hara Needham** (5/7 = 71%) — still primary handler; managing final wave
  - **Nate Straus** (2/7 = 29%) — supporting with S3 sales orders
- **Requesters:** 
  - Joshua Fromm (3/7 = 43%) — S3 SALES orders dominate Nate's queue
  - Alex (2/7 = 29%) — GetFPV, 3dr
  - Ethan Domagala (1/7 = 14%) — McMaster Carr
  - Dan Prendergast (1/7 = 14%) — Dronetag Mini 4G
- **Risk signals:**
  - 🟡 **COMPRESSED FINAL DEADLINE:** All 7 remaining tasks due Aug 27–28. If any order placement, vendor confirmation, or invoice processing hits a snag in final 48 hours, potential for deadline miss or rushed QA bypass.
  - 🟡 **NATE'S S3 SALES BACKLOG (3 TASKS, ALL "ORDER RECEIVED"):**
    - jawstec for s3 SALES (#70664) — due Aug 28, "Order Received"
    - mks for s3 sales (#23022) — due Aug 28, "Order Received"
    - mks for s3 sales (#22962) — due Aug 28, "Order Received" (**placed Aug 6 — 21 days old**)
    - **These should have been closed immediately upon receipt.** Risk of stale fulfillment (QA check pending, invoices not yet reconciled with project).
  - 🟠 **PROJECT FIELD TRUNCATION PERSISTS:**
    - McMaster Carr: Project shows "[043-3] Mustan" (truncated from "Mustang Pt. 2")
    - jawstec for s3 SALES: Project shows "[451-1] I" (truncated from "INSTAAR S3 x2")
    - mks tasks: Project shows "[451-1] INSTA" / "[451-1] INSTAA" (truncated)
    - **Risk of incorrect billing if truncation causes project lookup failures during invoicing.**
  - 🟠 **TAX-EXEMPT CONSISTENCY:** 3/7 tasks are tax-exempt (YES — all S3 sales orders), 4/7 are taxable (NO). Correct categorization, but requires vigilance for new orders.
  - 🟠 **PRIOR OPEN ISSUES UNRESOLVED:**
    - **Cancelled Digikey task (#100801135)** — flagged in previous snapshot as still OPEN despite being marked "CANCELLED." Not visible in current data; unclear if closed or still lingering.
    - **Multi-project allocation gaps** — jawstec multi-project (#70415) and pololu shop supplies (#1J593583) from prior snapshot not visible here; confirm if closed or reassigned.

## Key Deliverables & Milestones

### **FINAL DEADLINE WINDOW: Aug 27–28, 2026 (7 TASKS)**

| Task | Vendor | Project | Requester | Assignee | Status | Due | Tax Exempt |
|------|--------|---------|-----------|----------|--------|-----|-----------|
| GetFPV (#1001507386) | GetFPV | [550-1] Navy SBIR: Magnetometer | Alex | Meredith | Order Placed | Aug 27 | NO |
| Dronetag Mini 4G (#CLYVSOCSY) | Dronetag | [001-12] Customer Support | Dan Prendergast | Meredith | Order Placed | Aug 27 | NO |
| McMaster Carr (#0825JELSTON) | McMaster Carr | [043-3] Mustang Pt. 2 | Ethan Domagala | Meredith | Order Shipped | Aug 27 | NO |
| 3dr (#5804) | 3dr | [001-16] IRAD Swiftstation | Alex | Meredith | Order Shipped | Aug 27 | NO |
| jawstec for s3 SALES (#70664) | jawstec | [451-1] INSTAAR S3 x2 | Joshua Fromm | Nate | Order Received | Aug 28 | YES |
| mks for s3 sales (#23022) | mks | [451-1] INSTAAR S3 x2 | Joshua Fromm | Nate | Order Received | Aug 28 | YES |
| mks for s3 sales (#22962) | mks | [451-1] INSTAAR S3 x2 | Joshua Fromm | Nate | Order Received | Aug 28 | YES |

## Task Summary

- **Total tasks:** 7 open, 0 completed (in current snapshot)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 5/7 (71%) — GetFPV, Dronetag Mini 4G, McMaster Carr, 3dr + 1 implied prior task
  - **Nate Straus:** 2/7 (29%) — jawstec s3 SALES, mks s3 sales ×2
- **Task status breakdown:**
  - Order Placed: 2 (GetFPV, Dronetag Mini 4G)
  - Order Shipped: 2 (McMaster Carr, 3dr)
  - Order Received: 3 (jawstec, mks ×2) — **all assigned to Nate; fulfillment (QA, invoicing) pending**
- **Notable patterns:**
  - **Meredith handling 4 orders in final 48 hours with "Order Placed" or "Order Shipped" status** — suggests either orders placed very recently or shipment tracking is current; low risk of logistics delay if already shipped.
  - **Nate's S3 queue clustered:** 3 orders for [451-1] INSTAAR S3 x2 from Joshua Fromm; all tax-exempt (institutional purchase); all in "Order Received" state due same day (Aug 28). **Suggests batch order for same project; should be processed together for billing efficiency.**
  - **No unassigned tasks** — improved from prior state; full assignment coverage.

## Recent Activity

- **85% task reduction (45 → 7 open tasks):** Prior snapshot showed critical surge to 45 concurrent orders; current snapshot shows only 7 remain. **Action required:** Confirm with Meredith/Nate whether 38 tasks were genuinely completed or if data was cleaned/archived.
- **Meredith's workload stabilized but still compressed:** Now managing 5/7 final tasks vs. 26/45 in prior snapshot (71% vs. 58% of remaining work). Suggests targeted workload balance