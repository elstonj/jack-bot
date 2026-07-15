# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **CRITICAL CHANGE: Task count surged from 1 open task to 5 open tasks.** Deadlines now span Jul 14–Jul 16, 2026; 2 tasks are OVERDUE (Jul 1 deadline passed).
- **Status:** 🔴 **OPERATIONAL STRESS ESCALATING SIGNIFICANTLY.** Task backlog has grown 5x from prior week (1 → 5 open). 2 jawstec orders overdue by 13 days (due Jul 1, now Jul 14+). Ownership split between Meredith and Nate. **CRITICAL UNRESOLVED ISSUES:** (1) Multi-project billing exposure remains (jawstec tasks with truncated project codes), (2) digikey task reassigned from Meredith to Nate with truncated project field, (3) order placement dates have drifted beyond requested dates.
- **Team members involved:**
  - **Meredith O'hara Needham** (4/5 open tasks = 80%, Project Owner) — "Order Placed" & "Order Shipped" pipeline
  - **Nate Straus** (1/5 open tasks = 20%) — DigiKey antenna task, "Order Received" status
  - **Requesters:** Alex (1), Nate (1), Joshua Fromm (2), Kareem (1)
- **Risk signals:**
  - 🔴 **TASK BACKLOG EXPLOSION:** 1 → 5 open tasks in 1 cycle. Intake velocity has jumped dramatically or prior tasks not being closed properly.
  - 🔴 **OVERDUE TASKS (2):** jawstec orders (#69630, #69631) due Jul 1, 2026 — **13 days overdue.** Both "Order Shipped" status suggests fulfillment completed, but tasks remain open. Likely closure automation failure.
  - 🔴 **OWNERSHIP WHIPSAW:** DigiKey antenna task reassigned from Meredith (Project Owner) to Nate Straus without clear handoff note. Suggests approval gate or approval conflict.
  - 🔴 **FORM DATA TRUNCATION PERSISTS & WORSENED:** 
    - DigiKey project field now shows only "[30" (was "[300-3]" in notes — confirms form submission error)
    - jawstec S0 IDIQ project field shows "[300-3] 20" (truncated from "[300-3] 2026 IDIQ (Hurricane)")
    - jawstec S3 Sales project field shows "General S" (truncated from "General Sales")
    - **HIGH RISK:** Orders may be billed to wrong projects if form data not manually corrected.
  - 🟠 **TAX EXEMPTION SPLIT:** 3/5 tasks are tax-exempt (60%); 2 are non-exempt. Verify tax handling on Microhard and Amazon orders.
  - 🟠 **REQUESTER CONCENTRATION:** Joshua Fromm now owns 2/5 tasks (40%); new requester pressure from Alex and continued Nate/Kareem intake.

## Key Deliverables & Milestones

### **OVERDUE & OPEN TASKS**

| Task | Due | Status | Vendor | Assigned | Project | Requester | Tax Exempt? | Notes |
|------|-----|--------|--------|----------|---------|-----------|------------|-------|
| jawstec for s3 sales (#69630) | **Jul 1, 2026 (OVERDUE 13 days)** | Order Shipped | jawstec | Meredith | General Sales (form: "General S" — **TRUNCATED**) | Joshua Fromm | YES | Fulfillment complete; task should close. Form project code incomplete. |
| jawstec for s0 idiq (#69631) | **Jul 1, 2026 (OVERDUE 13 days)** | Order Shipped | jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) (form: "[300-3] 20" — **TRUNCATED**) | Joshua Fromm | YES | Fulfillment complete; task should close. Form project code incomplete. |
| Microhard | Jul 14, 2026 | (not started) | Microhard | Meredith | [001-16] IRAD Swiftstation | Alex | NO | Placement due TODAY or TOMORROW. No status update yet. |
| Amazon Shop supplies | Jul 16, 2026 | Order Placed | Amazon | Meredith | [001-1] IRAD General (form: "[001-1] IRAD Gene" — **TRUNCATED**) | Nate | NO | Order placed; task due Jul 16. Project code incomplete in form. |
| digikey - antennas for hurricane (#100363511) | Jul 16, 2026 | Order Received | DigiKey | Nate | [300-3] 2026 IDIQ (Hurricane) (form: "[30" — **SEVERELY TRUNCATED**) | Kareem | NO | **REASSIGNED TO NATE** from Meredith. Placement was due Jul 13 (3 days ago); order already received. Project code severely incomplete in form. |

### **UPCOMING DEADLINES**
- **Jul 14, 2026:** Microhard order (Meredith) — **DUE IMMINENTLY**
- **Jul 16, 2026:** Amazon and DigiKey tasks (Meredith & Nate) — both in progress or received

## Task Summary
- **Total tasks:** 5 open, 0 completed in this dataset
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 4/5 (80%) — jawstec S3, jawstec S0, Microhard, Amazon
  - **Nate Straus:** 1/5 (20%) — DigiKey antenna
- **Tasks by requester:**
  - **Joshua Fromm:** 2/5 (40%) — both jawstec orders
  - **Alex:** 1/5 (20%) — Microhard
  - **Nate:** 1/5 (20%) — Amazon supplies
  - **Kareem:** 1/5 (20%) — DigiKey
- **Notable patterns:**
  - **BACKLOG SURGE:** 5x increase from prior snapshot (1 → 5 open). Indicates either high intake velocity or failure to close completed orders (jawstec tasks "Order Shipped" but still open).
  - **FORM SUBMISSION QUALITY DEGRADATION:** 4/5 tasks have truncated project codes in form data. Suggests form field character limits, clipboard truncation, or data entry errors.
  - **TASK LIFECYCLE BREAKDOWN:** jawstec tasks are "Order Shipped" (fulfillment complete) but remain open — automation/closure workflow not triggering.
  - **OWNERSHIP INSTABILITY:** DigiKey task bounced from Meredith to Nate; reason unclear.

## Recent Activity
- **Jul 14, 2026 (NOW):** 2 jawstec orders overdue by 13 days (due Jul 1); status "Order Shipped" suggests fulfillment complete but tasks not closed.
- **Jul 14, 2026 (NOW):** Microhard order due today with no status update — placement may not have occurred.
- **Jul 13, 2026 (3 days ago):** DigiKey antenna order was requested for placement; now showing "Order Received" — order has already been processed, but task remains in pipeline.
- **Task reassignment noted:** DigiKey antenna reassigned from Meredith (Project Owner) to Nate Straus — reason not documented.
- **Amazon order:** Status "Order Placed" suggests placement occurred (due date was Jul 14, now listed as due Jul 16 — possible date drift).

## Notes & Context

### **🔴 CRITICAL: FORM DATA TRUNCATION EPIDEMIC**
**ALL 5 TASKS** have truncated or incomplete project codes in the form submission