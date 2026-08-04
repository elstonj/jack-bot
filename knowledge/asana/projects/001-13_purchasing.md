# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **8 open tasks; critical deadlines Aug 2–5, 2026.**
- **Status:** 🟡 **OPERATIONAL — URGENT DEADLINE COMPRESSION.** Task count **decreased dramatically from 13 to 8 open tasks** (38% reduction). **Portfolio composition has shifted significantly:** [001-4] IRAD S0 VTOL now **only 3/8 tasks (38%)** — down from 85%. **New projects entered queue:** [043-3] Mustang Pt. 2, [001-1] IRAD General, [300-3] 2026 IDIQ (Hurricane) expanded. **Status distribution has improved:** Order Shipped now 3/8 (38%, up from 15%), Order Received 2/8 (25%, up from 8%), Order Placed 3/8 (38%, down from 85%).
  - **CRITICAL CHANGE:** Prior snapshot listed 11/13 S0 VTOL tasks due Aug 2 in "Order Placed" state. **Current data shows only 3 S0 VTOL tasks remaining, all now "Order Shipped" (Amazon, Digikey, Hitec), due Aug 2.** **8 vendors from prior batch have been removed/closed (Dronetag, APC, Protolabs, Sendcutsend, Jawstec Pt1 & Pt2, Servocity, IRLock).** This suggests **massive fulfillment activity overnight — orders either arrived, were consolidated, or workflow was restructured.** **Verify closure documentation; if legitimately completed, indicates successful Aug 1–2 delivery push.**
  - **NEW TASKS ENTERED QUEUE:** 5 new tasks added (shop supplies, Mouser ByLight, Amazon launch switch, rocketman, protospace). Requesters expanded to include Joshua Fromm, Ethan, Nate.
- **Team members involved:**
  - **Meredith O'hara Needham** (6/8 = 75%, down from 92%)
  - **Nate Straus** (2/8 = 25%, up from 8%) — **elevated role**
- **Requesters:** Alex (3/8 = 38%, down from 77%), Joshua Fromm (3/8 = 38%, up from 23%), Ethan (1/8 = 13%), Nate (1/8 = 13%)
- **Risk signals:**
  - 🔴 **MEREDITH STILL CRITICAL BOTTLENECK:** 6/8 tasks (75%) assigned to Meredith — **slight improvement, but still dominant.** Nate has expanded to 2 tasks (rocketman, protospace), suggesting workload rebalancing.
  - 🔴 **MASSIVE S0 VTOL BATCH CLOSURE — UNVERIFIED:** 8 vendors from prior "Order Placed" batch have vanished from task list. **Either:** (a) successfully received Aug 1–2 and moved to completed tracking, (b) consolidated into remaining 3 "Order Shipped" tasks, or (c) **removed without closure documentation.** **Immediate action required: audit completed task history and vendor invoices to confirm fulfillment status.** If orders were cancelled or consolidated, risk of project delay or duplicate billing.
  - 🟠 **COMPRESSED DEADLINE WINDOW:** 3 tasks due Aug 2 (Amazon, Digikey, Hitec — all S0 VTOL, all "Order Shipped"), 5 tasks due Aug 5 (shop supplies, Mouser ByLight, Amazon launch switch, rocketman, protospace). **No buffer between delivery windows; any delay in Aug 2 shipments cascades to Aug 5 workflow.**
  - 🟠 **NATE-ASSIGNED TASKS WITH STALE PLACEMENT DATES:** 
    - **rocketman (#1817):** Due Aug 5, status "Order Received," but "placed" Jul 24 — **12 days old.** Order may have arrived but fulfillment confirmation (invoice, QA check) is pending.
    - **protospace:** Due Aug 5, status "Order Received," "placed" May 18 — **over 2.5 months old.** **Extreme lag; possible legacy task or missing closure. High risk of invoice disputes or forgotten follow-up.**
  - 🟠 **PROJECT FIELD TRUNCATION PERSISTS:** Shop supplies custom field shows "Shop S" (truncated). Mouser ByLight shows "[043-3] Mustang" (appears complete, but monitor). Ensure billing codes are fully captured in backend.
  - 🟠 **PORTFOLIO DIVERSIFICATION — NEW RISK SURFACE:** Purchasing now spans 5+ projects (S0 VTOL, Shop Supplies, Mustang Pt. 2, IRAD General, Hurricane IDIQ). **Increased complexity; easier to miss cross-project invoice reconciliation or duplicate orders.**

## Key Deliverables & Milestones

### **OPEN TASKS — CURRENT BATCH (8 TOTAL)**

| Task | Vendor | Assigned | Project | Requester | Status | Due | Notes |
|------|--------|----------|---------|-----------|--------|-----|-------|
| **Amazon** | Amazon | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | Aug 2 | S0 VTOL batch. Tax exempt. Placed Jul 31. **Delivery imminent.** |
| **Digikey (#100742193)** | Digikey | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | Aug 2 | S0 VTOL batch. Tax exempt. Placed Jul 31. **Delivery imminent.** |
| **Hitec (5791)** | Hitec | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | Aug 2 | S0 VTOL batch. Tax exempt. Placed Jul 31. **Delivery imminent.** |
| **amazon for shop supplies** | Amazon | Meredith | Shop Supplies | Joshua Fromm | Order Placed | Aug 3 | **Truncated project field ("Shop S").** Placed Aug 3. |
| **Mouser- ByLight Laser (#40026106)** | Mouser | Meredith | [043-3] Mustang Pt. 2 | Ethan | Order Placed | Aug 5 | New project (Mustang). Tax exempt. Placed Aug 3. |
| **Amazon / launch switch** | Amazon | Meredith | [001-1] IRAD General | Nate | Order Placed | Aug 5 | IRAD General. Placed Aug 3. |
| **rocketman for s0 hurricane (#1817)** | Rocketman | Nate | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Received | Aug 5 | **Stale placement date (Jul 24 — 12 days old).** Status "Order Received" suggests arrived but fulfillment pending. Tax exempt. |
| **protospace for s0 idiq** | Protospace | Nate | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Received | Aug 5 | **EXTREME LAG: Placed May 18 (over 2.5 months ago).** Status "Order Received." **High risk of missing invoice or forgotten closure. Immediate investigation required.** Tax exempt. |

## Task Summary
- **Total tasks:** 8 open, 0 completed (in this query; prior snapshot shows 0 completed as well — no closed task data provided)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 6/8 (75%) — amazon (shop supplies, S0 VTOL×2), Mouser ByLight, Amazon launch switch
  - **Nate Straus:** 2/8 