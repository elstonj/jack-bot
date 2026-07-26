# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **14 open tasks with deadlines Jul 25–26, 2026.** 🟠 **CRITICAL DEADLINE CRUNCH:** All 14 tasks due within 1–2 days. Heavy S0 Hurricane procurement (Joshua Fromm, 10 tasks) all placed Jul 23–24, all due Jul 25–26. Two Swiftstation tasks (Sparkfun, Amazon, Digikey GCS) and one S3 task all due Jul 25.
- **Status:** 🟠 **OPERATIONAL — DEADLINE CRUNCH ACTIVE.** Task count **decreased from 19 to 14** (5 tasks resolved or auto-closed). **Status distribution:** 3 "Order Received" (Sparkfun, Amazon, Digikey GCS = 21%); 10 "Order Placed" (Hurricane batch = 71%); 2 "Order Shipped" (springstore, S3 = 14%). **FTDI task no longer in list** — likely closed after Jul 18 overdue date or auto-deleted. **powerwerx, craftcloud, mouser tasks also removed** — status unclear (completed, auto-deleted per form rules, or moved). **Closure automation failure persists:** Sparkfun, Amazon, Digikey GCS all "Order Received" (placed Jul 21, now due Jul 25) remain open; springstore and S3 "Order Shipped" remain open.
- **Team members involved:**
  - **Meredith O'hara Needham** (10/14 open tasks = 71%) — All 10 Hurricane S0 orders (digikey, rocketman, jawstec, Midwest, tattu, rfmall, icare, amazon, protolabs, springstore) + S3 power board parts
  - **Nate Straus** (3/14 open tasks = 21%) — Sparkfun, Amazon, Digikey GCS (Swiftstation, all "Order Received")
- **Requesters:** Joshua Fromm (10/14 = 71%, Hurricane S0); Joshua fromm (1/14 = 7%, springstore, likely typo); Sam (1/14 = 7%, S3); Alex (3/14 = 21%, Swiftstation)
- **Risk signals:**
  - 🔴 **IMMINENT DEADLINE CRUNCH (48 HOURS):** All 14 tasks due Jul 25–26. Protolabs due Jul 25 (1 day); Sparkfun, Amazon, Digikey GCS, S3 due Jul 25 (1 day); 9 Hurricane tasks due Jul 26 (2 days). All Hurricane orders placed Jul 23–24; most 1–2 day fulfillment windows.
  - 🟠 **CLOSURE AUTOMATION STILL FAILING:** Sparkfun, Amazon, Digikey GCS all "Order Received" (placed Jul 21, 4 days ago, now due) remain open — should auto-close per form rules. Springstore and S3 "Order Shipped" remain open. **Pattern suggests either form auto-delete/close mechanism not working or tasks manually kept open.**
  - 🟠 **FORM DATA TRUNCATION UNRESOLVED:** Multiple Hurricane tasks still have truncated project codes: digikey "[300-", rocketman "[30", jawstec "[300-3] 2", icare "[300-3", springstore "[300-3". **High risk of incorrect billing.** (Note: jawstec, Midwest, tattu, rfmall show more complete codes; icare, digikey, rocketman, springstore truncated.)
  - 🟠 **TASK REMOVAL WITHOUT CLOSURE DOCUMENTATION:** 5 tasks from prior snapshot (FTDI, powerwerx, craftcloud, mouser, jawstec sales) no longer in current list. **No closure notes, no completion records.** FTDI was 3 days overdue; powerwerx/craftcloud/mouser had placement ambiguity. **Unclear if orders completed, cancelled, auto-deleted, or escalated.** Risk: no audit trail.
  - 🟠 **HURRICANE BATCH CONCENTRATION:** 10 of 14 tasks (71%) are Hurricane S0 parts from Joshua Fromm, all due Jul 25–26, most placed same day (Jul 24). **Single-point-of-failure risk:** If any critical vendor delays, entire Hurricane timeline at risk. Multiple vendors (protolabs, digikey, rocketman, jawstec, etc.) all with 1–2 day delivery windows.
  - 🟠 **PLACEMENT DATE DISCREPANCIES:** Protolabs form says "When should this order be placed?: Jul 23" but task due date is Jul 25 (2-day window, already placed). Springstore form says "Jul 24" but due Jul 26 (2-day window). **Unclear if form dates are *planned* or *actual* — likely actual placement dates, suggesting orders are submitted and tracking is accurate, but form not consistently updated.**

## Key Deliverables & Milestones

### **OPEN TASKS (sorted by due date, status snapshot as of Jul 24, 2026)**

| Task | Vendor | Assigned | Project | Requester | Status | Placement Date (Form) | Due Date | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|----------------------|----------|------------|-------|
| **protolabs for s0 idiq (6794-871)** | protolabs | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 23, 2026 | **Jul 25, 2026** | YES | 🟠 **DUE IN 1 DAY.** Placed Jul 23, due Jul 25 (2-day window). S0 Hurricane. |
| **S3 extra parts for power board fix (#100576268)** | S3 | Meredith | [001-7] IRAD S3 | Sam | Order Shipped | Jul 22, 2026 | **Jul 25, 2026** | NO | 🟠 **DUE IN 1 DAY.** Status "Order Shipped" (in transit) but task remains open. Power board fix. |
| **Sparkfun (000419974)** | Sparkfun | Nate | [001-16] IRAD Swiftstation | Alex | Order Received | Jul 21, 2026 | **Jul 25, 2026** | NO | 🟠 **DUE IN 1 DAY.** Status "Order Received" (4 days ago, placed Jul 21) but remains open — should have auto-closed per form rules. Swiftstation. |
| **Amazon** | Amazon | Nate | [001-16] IRAD Swiftstation | Alex | Order Received | Jul 21, 2026 | **Jul 25, 2026** | NO | 🟠 **DUE IN 1 DAY.** Status "Order Received" (4 days ago) but remains open. Swiftstation. |
| **Digikey for GCS (#100525116)** | Digikey | Nate | [001-16] IRAD Swiftstation | Alex | Order Received | Jul 21, 2026 | **Jul 25, 2026** | NO | 🟠 **DUE IN 1 DAY.** Status "Order Received" (4 days ago) but remains open. Swiftstation GCS. |
| **digikey for S0 hurricane (#100607181)** | Digikey | Meredith | [300-**3] (truncated) | Joshua Fromm | Order Placed | Jul 24, 2026 | **Jul 26, 2026** | YES | 🟠 **DUE IN 2 DAYS.** Project field truncated "[300-". Placed Jul 24, due Jul 26 (2-day window).