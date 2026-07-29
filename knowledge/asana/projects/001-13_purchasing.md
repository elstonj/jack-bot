# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **8 open tasks with mixed deadlines: Jul 16 (OVERDUE), Jul 26, Jul 29–30, 2026.**
- **Status:** 🟠 **OPERATIONAL — DEADLINE CRUNCH & OVERDUE TASK PRESENT.** Task count **increased from 6 to 8** (from prior snapshot). Current distribution: **Order Placed 5/8 (63%), Order Shipped 2/8 (25%), Order Received 1/8 (13%).** Notable change: **Amazon task (Jul 16) is OVERDUE by 10 days** (today ~Jul 26). Midwest control products (Jul 26) also overdue or due today. Prior truncation failures (digikey, icare) have been **cleared from task list** — suggests cleanup/closure occurred. New tasks added: mouser for shop equipment ([001-1] IRAD General context implied), powerwerx (MULTIPLE PROJECT flagged). This indicates active procurement rotation with stale tasks persisting.
- **Team members involved:**
  - **Meredith O'hara Needham** (7/8 open tasks = 88%)
  - **Nate Straus** (1/8 = 13% — springstore task only)
- **Requesters:** Joshua Fromm (7/8 = 88%), Nate (1/8 = 13%)
- **Risk signals:**
  - 🔴 **OVERDUE TASK:** Amazon Shop supplies (Jul 16, Order Shipped) is **10 days overdue.** Requested by Nate; assigned to Meredith. Status "Order Shipped" but due date passed. Requires immediate follow-up.
  - 🔴 **IMMINENT/OVERDUE (TODAY or PASSED):** Midwest control products due Jul 26 (Order Shipped). Placed Jul 24; 48-hour window.
  - 🟠 **CRITICAL FORM DATA TRUNCATION PERSISTS:** 2 of 8 tasks still have severely truncated project codes in form capture:
    - **craftcloud:** "Select project to bill purcha" (cut off mid-word)
    - **Midwest control products:** "Select project to bill pur" (truncated)
    - **springstore:** "[300-3" (6 chars, incomplete)
    - **mouser for shop equipment:** "Shop" (ambiguous; likely internal code missing)
    - **mouser order for s0 hurricane:** PROJECT FIELD EMPTY in form notes
    - **Amazon:** "[001-1] IRAD Gene" (truncated from "[001-1] IRAD General")
    - **jawstec:** "[001-7] IR" (truncated from "[001-7] IRAD S3" in task name, but project field shows correct full text in custom field)
    - **Indicates systematic form character-limit truncation (~30–50 chars in notes section).** Risk: Billing misroute, project code ambiguity.
  - 🟠 **HURRICANE BATCH DOMINANCE PERSISTING:** 5/8 tasks (63%) are [300-3] 2026 IDIQ (Hurricane S0). Single-point-of-failure risk remains high.
  - 🟠 **NEW REQUESTERS & ASSIGNEE VARIANCE:** Nate (requester on Amazon, assigned to springstore) adds complexity; prior snapshots showed Joshua Fromm + Meredith only. Nate's springstore task has inconsistent data (due Jul 30, order status "Order Received" — suggests fulfillment lag, but task remains open).
  - 🟠 **MULTI-PROJECT FLAGGED, NO BREAKDOWN:** powerwerx task explicitly notes "[Project: MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION]" but notes section is empty of breakdown. Risk: Incorrect/split billing.
  - 🟠 **SHOP SUPPLIES PROJECT AMBIGUITY:** mouser for shop equipment references "Shop Supplies" in custom field but notes say "Shop" only. Possible alias or incomplete form capture.

## Key Deliverables & Milestones

### **OPEN TASKS — MIXED BATCH (Hurricane S0 IDIQ + S3 IRAD + Shop Supplies + Multi-Project)**

| Task | Vendor | Assigned | Project (Form) | Requester | Status | Placement | Due | Tax Exempt? | Notes |
|------|--------|----------|----------------|-----------|--------|-----------|-----|------------|-------|
| **Amazon Shop supplies** | Amazon | Meredith | [001-1] IRAD Gene **(TRUNCATED)** | Nate | Order Shipped | Jul 14 | **Jul 16 🔴 OVERDUE** | NO | 🔴 **10 DAYS OVERDUE.** Status "Order Shipped" but due date has passed. Requires escalation. Project field truncated from "[001-1] IRAD General." |
| **Midwest control products for s0 idiq** | Midwest Control | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Shipped | Jul 24 | **Jul 26 🔴 TODAY/OVERDUE** | YES | Status "Order Shipped" but task due today or overdue. Notes truncated: "Select project to bill pur..." |
| **icare order for s0 idiq** | iCare | *(Cleared)* | *(Cleared)* | *(Cleared)* | *(Cleared)* | *(Cleared)* | **Jul 26** | *(Cleared)* | 🟢 **REMOVED from task list** since prior snapshot. Truncation error resolved via closure. |
| **digikey for S0 hurricane** | Digikey | *(Cleared)* | *(Cleared)* | *(Cleared)* | *(Cleared)* | *(Cleared)* | **Jul 26** | *(Cleared)* | 🟢 **REMOVED from task list** since prior snapshot. Truncation error ([300-) resolved via closure. |
| **mouser order for s0 hurricane** | Mouser | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 24 | Jul 29 | YES | Project field EMPTY in form. Assumed [300-3] per vendor/context. |
| **craftcloud for s0 hurricane parts** | Craftcloud | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 24 | Jul 29 | YES | Notes truncated: "Select project to bill purcha..." |
| **jawstec for s3 IRAD** | Jawstec | Meredith | [001-7] IRAD S3 | Joshua Fromm | Order Placed | Jul 27 | Jul 29 | NO | ✓ Project field complete. S3 IRAD (first non-Hurricane). Tax exempt = NO (outlier). |
| **mouser for shop equipment** | Mouser | Meredith | Shop Supplies | Joshua Fromm | Order Placed | Jul 28 | Jul 30 | NO | Custom field says "Shop Supplies"; notes say "Shop" only. Possible [001-1] or internal supply project. Verify project code. |
| **powerwerx for multiple projects** | Powerwerx | Meredith | **MULTIPLE PROJECT** *(No breakdown)* | Joshua Fromm | Order Placed | Jul 24 | Jul 30 | YES | 🟠 **CRITICAL:** Task explicitly flagged "PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" but notes section empty. Requires immediate clarification before order ships. Billing split unknown. |
| **springstore for s0 idiq** | Springstore | Nate Straus | [300-3 **(TRUNCATED)** | Joshua Fromm | Order Received | Jul 24 | Jul 30 | YES | Project field truncated from "[300-3] 