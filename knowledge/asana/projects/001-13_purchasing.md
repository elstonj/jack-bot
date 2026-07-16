# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **CRITICAL CHANGE: Task composition has shifted.** 5 open tasks with deadlines spanning Jul 4–Jul 17, 2026. **1 task is SEVERELY OVERDUE** (SendCutSend, due Jul 4, now Jul 14+). 3 tasks due within 48 hours (Jul 15–16).
- **Status:** 🔴 **OPERATIONAL STRESS PERSISTS & EVOLVES.** Task backlog remains at 5 open tasks but composition has changed—jawstec orders have been replaced/closed, but new vendors (FTDI, Mouser, SendCutSend) have entered the pipeline. **CRITICAL UNRESOLVED ISSUES:** (1) **1 severely overdue task (SendCutSend, 10 days past due date)** with "Order Shipped" status but not closed, (2) Form data truncation continues across all 5 tasks (DigiKey project still "[30"), (3) 3 tasks due imminently (Jul 15–16) with unclear placement status, (4) Ownership remains concentrated on Meredith (80%), (5) Task lifecycle breakdown—multiple "Order Shipped" tasks remaining open.
- **Team members involved:**
  - **Meredith O'hara Needham** (4/5 open tasks = 80%, Project Owner) — primary purchasing executor
  - **Nate Straus** (1/5 open tasks = 20%) — DigiKey antenna, "Order Received" status
  - **Requesters:** Alex (3), Nate (1), Kareem (1)
- **Risk signals:**
  - 🔴 **SEVERELY OVERDUE TASK:** SendCutSend (#SQ29Q224) due Jul 4, 2026 — **10 days overdue as of Jul 14.** Status is "Order Shipped" (fulfillment complete) but task remains open. Closure automation failure.
  - 🔴 **IMMINENT DEADLINES (48 hrs):** FTDI (Jul 15), Amazon (Jul 16), DigiKey (Jul 16), Mouser (Jul 17). Multiple tasks approaching or at due date with unclear placement status.
  - 🔴 **FORM DATA TRUNCATION PERSISTS:** 
    - DigiKey project field still shows only "[30" (severely truncated from "[300-3] 2026 IDIQ (Hurricane)")
    - Amazon project field shows "[001-1] IRAD Gene" (truncated from full "[001-1] IRAD General")
    - SendCutSend project field shows "General Sales (No Specific" (truncated)
    - **HIGH RISK:** Orders may be billed to wrong projects if form data not manually corrected.
  - 🟠 **TASK LIFECYCLE BREAKDOWN:** 2/5 tasks with "Order Shipped" status (SendCutSend, Mouser) remain open. Suggests closure automation or manual task completion is not being triggered after fulfillment.
  - 🟠 **REQUESTER CONCENTRATION SHIFT:** Alex now owns 3/5 tasks (60%) — significant increase from prior snapshot (was 1/5). Nate and Kareem each own 1 task.
  - 🟠 **TAX EXEMPTION SPLIT:** 1/5 task is tax-exempt (20%, SendCutSend); 4/5 are non-exempt.

## Key Deliverables & Milestones

### **OVERDUE & OPEN TASKS**

| Task | Due | Status | Vendor | Assigned | Project | Requester | Tax Exempt? | Notes |
|------|-----|--------|--------|----------|---------|-----------|------------|-------|
| SendCutSend (#SQ29Q224) | **Jul 4, 2026 (OVERDUE 10 days)** | Order Shipped | SendCutSend | Meredith | General Sales (No Specific Project) (form: "General Sales (No Specific" — **TRUNCATED**) | Alex | YES | Fulfillment complete; task should close. Closure automation failure. |
| FTDI | **Jul 15, 2026 (DUE TODAY or TOMORROW)** | (not started) | FTDI | Meredith | [001-16] IRAD Swiftstation | Alex | NO | Placement due Jul 15. No status update yet. |
| Amazon Shop supplies | **Jul 16, 2026 (DUE in 2 days)** | Order Placed | Amazon | Meredith | [001-1] IRAD General (form: "[001-1] IRAD Gene" — **TRUNCATED**) | Nate | NO | Order placed; task due Jul 16. Project code incomplete in form. |
| Mouser (#39830975) | **Jul 17, 2026 (DUE in 3 days)** | Order Shipped | Mouser | Meredith | [001-4] IRAD S0 VTOL | Alex | NO | Order shipped; task due Jul 17. Fulfillment complete but task not closed. |
| digikey - antennas for hurricane (#100363511) | **Jul 16, 2026 (DUE in 2 days)** | Order Received | DigiKey | Nate | [300-3] 2026 IDIQ (Hurricane) (form: "[30" — **SEVERELY TRUNCATED**) | Kareem | NO | Placement was due Jul 13 (1 day ago); order already received. Project code severely incomplete in form. |

### **UPCOMING DEADLINES**
- **Jul 15, 2026:** FTDI order (Meredith) — **DUE IMMINENTLY**
- **Jul 16, 2026:** Amazon and DigiKey tasks (Meredith & Nate) — both due within 48 hours

## Task Summary
- **Total tasks:** 5 open, 0 completed in this dataset
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 4/5 (80%) — FTDI, Amazon, Mouser, SendCutSend
  - **Nate Straus:** 1/5 (20%) — DigiKey antenna
- **Tasks by requester:**
  - **Alex:** 3/5 (60%) — FTDI, Mouser, SendCutSend (significant increase from prior snapshot: 1 → 3)
  - **Nate:** 1/5 (20%) — Amazon supplies
  - **Kareem:** 1/5 (20%) — DigiKey
- **Notable patterns:**
  - **TASK COMPOSITION SHIFT:** jawstec orders have been removed/closed; new vendors (FTDI, Mouser, SendCutSend) have entered. Backlog remains at 5 tasks but focus has changed.
  - **FORM SUBMISSION QUALITY DEGRADATION PERSISTS:** All 5 tasks have truncated or incomplete project codes in form data. DigiKey remains severely truncated ("[30"). Suggests ongoing form field character limits or data entry errors.
  - **TASK LIFECYCLE BREAKDOWN:** 2/5 tasks with "Order Shipped" status (SendCutSend, Mouser) remain open—automation/closure workflow not triggering.
  - **REQUESTER PRESSURE SHIFT:** Alex now owns 60% of intake (3/5 tasks), up from 1 prior snapshot.

## Recent Activity
- **Jul 14, 2026 (NOW):** SendCutSend order **10 days overdue** (due Jul 4); status "Order Shipped" suggests fulfillment complete but task not closed. Severe closure automation failure.
- **Jul 14, 2026 (NOW):** FTDI order due **tomorrow (Jul 15)** with no status update — placement may not have occurred.
- **Jul 16, 2026 (2 days):** Amazon and DigiKey both due within 48 hours.
- **Jul 17, 2026 (3 days):**