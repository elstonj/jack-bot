# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across 10+ active projects
- **Timeline:** Ongoing operational project. **Critical compressed deadlines Jul 26 – Aug 27, 2026.** Immediate delivery window: Jul 26–Aug 9 (15 tasks), secondary wave: Aug 11–27 (27 tasks).
- **Status:** 🔴 **CRITICAL OPERATIONAL CRISIS.** Task count **exploded from 8 to 45 open tasks (463% increase overnight).** This represents either:
  - (a) **Massive data sync event** — prior snapshot captured only a filtered subset; full queue is now visible, OR
  - (b) **Legitimate surge in purchase requests** across expanding portfolio.
  - **URGENT:** Verify if this reflects real new demand or data reconciliation. If real, **purchasing pipeline is severely overloaded; Meredith + Nate cannot handle 45 concurrent orders with current capacity.**
  - **Prior batch closure unresolved:** Previous snapshot flagged 8 vendors (Dronetag, APC, Protolabs, Sendcutsend, Jawstec Pt1 & Pt2, Servocity, IRLock) as removed/vanished. **NEW DATA SHOWS THESE TASKS ARE BACK IN QUEUE** — APC, Jawstec Pt1 & Pt2, Protolabs, Dronetag, IRLock, Sendcutsend, craftcloud all present as "Order Received" or "Order Shipped," assigned to Nate. **This confirms data was NOT lost; prior snapshot was incomplete or filtered. However, status values have CHANGED** — e.g., APC now "Order Shipped" (due Aug 2), Jawstec Pt1 now "Order Shipped" (due Aug 2), Jawstec Pt2 now "Order Received" (due Aug 22). **Suggests orders have progressed through pipeline since last update. No evidence of cancellation or duplicate billing yet, but reconciliation required.**
- **Team members involved:**
  - **Meredith O'hara Needham** (26/45 = 58%, decreased from 75% due to redistribution) — still primary bottleneck
  - **Nate Straus** (17/45 = 38%, elevated from 25%) — **significantly expanded role; now handling half of remaining workload**
  - **Unassigned** (2/45 = 4%) — low-priority inventory tasks ("Order Placed in Inventory" status)
- **Requesters:** Joshua Fromm (17/45 = 38%, massive increase from 38%), Alex (7/45 = 16%, down from 38%), Ethan (4/45 = 9%), Nate (3/45 = 7%), Dan Prendergast (1), Sam (1), Spencer (1)
- **Risk signals:**
  - 🔴 **CAPACITY CRISIS:** 45 open tasks, 2 staff (Meredith 26, Nate 17). **Average 22.5 tasks per person.** Assuming 30-min processing per task (form submission, vendor contact, payment processing, receipt confirmation), **each staffer has ~11.25 hours of work.** With compressed deadlines (Jul 26–Aug 27 = 32 days), **feasible but razor-thin margin for QA, invoice disputes, or sick leave.** Any delay compounds.
  - 🔴 **PORTFOLIO EXPLOSION:** Now spans **10+ projects:** [001-4] S0 VTOL, [451-1] INSTAAR S3, [300-3] Hurricane IDIQ, [043-3] Mustang Pt. 2, [550-1] Navy SBIR Magnetometer, [001-16] Swiftstation, [001-7] S3 IRAD, [001-3] S0, [212-2] NASA S2, [001-1] IRAD General, Shop Supplies, General Sales. **Cross-project invoice reconciliation and billing code truncation risk has multiplied.** Field truncation persists (e.g., "[043-3] Mustan," "[001-4] IRAD S0 VT," "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN").
  - 🟠 **NATE'S "ORDER RECEIVED" BACKLOG:** 14/17 Nate-assigned tasks are "Order Received" (status), implying goods have arrived but fulfillment (QA check, invoice verification, project billing closure) is pending. Oldest: **protospace (May 18 — 70 days old), rocketman (Jul 24 — 12 days old), JawsTec for GCS (Jul 21), craftcloud (Jul 24).** **These should have been closed weeks ago.** High risk of:
    - Forgotten invoices (vendor payment pending)
    - Duplicate billing (item received twice, charged twice)
    - Project cost reconciliation errors (item marked as "received" but not yet debited from project budget)
  - 🟠 **UNASSIGNED INVENTORY TASKS:** 2 tasks flagged "Order Placed in Inventory" (Amazon Shop Supplies, Chamba Chai Kettle) and **1 task explicitly marked "CANCELLED"** (Digikey #100801135, S0 VTOL, due Oct 16). **Cancelled task is still OPEN in system.** Suggests task closure workflow is broken; cancelled orders not being marked complete/removed.
  - 🟠 **DEADLINE CLUSTERING:** 
    - Jul 26–29: 4 tasks (jawstec S3 IRAD, jawstec S0 parts, rockwest S3) — **ALREADY PAST DUE if today is Aug 6 or later**
    - Aug 2–9: 11 tasks (APC, Jawstec Pt1, Amazon labels, IRLock, Dronetag, Protolabs, Sendcutsend, Mouser ByLight, McMaster Carr ByLight, Bartington)
    - Aug 11–22: 16 tasks (Amazon Hurricane, mks S3×2, jawstec S3 SALES, home depot, pcbway, Digikey GCS, tomas liu×2, horizon hobby, protospace, rocketman)
    - Aug 23–27: 12 tasks (3dr, GetFPV, Dronetag Mini 4G, McMaster Carr)
  - 🟠 **MULTIPLE-PROJECT ALLOCATION GAPS:** Two tasks require multi-project breakdown but field is truncated/incomplete:
    - **jawstec for multiple projects (#70415):** Due Aug 21, "Order Received," Nate assigned. Project field shows "M" (truncated). **Josh Fromm requested; critical missing data on which projects to bill.**
    - **pololu for shop supplies (#1J593583):** Due Aug 13, "Order Received," Nate assigned. Project field shows "MULTIP" (truncated). **Missing project breakdown.**
  - 🟠 **STALE PLACEMENT DATES (NATE-ASSIGNED):**
    - protospace (May 18 — **70 days old**)
    - rocketman (Jul 24 — 12 days old)
    - JawsTec for GCS (Jul 21 — 16 days old)
    - Sendcutsend S0 VTOL (Jul 31 — 6 days old, but due Aug 8)
    - ebay for S2 NASA (Jul 31 — 6 days old, due Aug 8)
    - craftcloud (Jul 24 — 12 days old, due Aug 8)
  - 🟠 **MIXED TAX-EXEMPT STATUS:** 21/45 tasks are tax-exempt (YES), 24/45 are taxable (NO). **No systematic pattern by project or vendor; requires vigilance per order.** Risk of incorrect tax treatment if form is auto-processed.

## Key Deliverables & Milestones

### **IMMEDIATE DEADLINE WINDOW: Jul 26 – Aug 9, 2026 (15 TASKS)**
*(These are past-