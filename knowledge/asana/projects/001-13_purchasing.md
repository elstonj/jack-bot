# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due June 19–21, 2026
- **Status:** **ACTIVE — CRITICAL IMPROVEMENT OBSERVED.** Assignment concentration has normalized: Meredith O'hara Needham down to 3/7 (43%), Nate Straus up to 4/7 (57%). **Delegation strategy is working.** 4/7 tasks marked "Order Received" or "Order Shipped" but remain open — form-based auto-closure still not functioning. Manual closure required immediately for completed orders. Task volume reduced from 11 to 7 (5 tasks successfully closed/removed since last cycle).
- **Team members involved:**
  - **Nate Straus** (4/7 assigned tasks; jawstec #69219, Microhard, sendcutsend #SC51C906, Mouser #39526033; **delegation momentum restored**)
  - **Meredith O'hara Needham** (3/7 assigned tasks; compositeenvisions, Sendcutsend #S1841769, Digikey GCS WiFi boards; project owner; **concentration reduced from 82% to 43%**)
  - **Joshua Fromm** (3/7 as requester; compositeenvisions, sendcutsend #SC51C906, jawstec focus)
  - **Nate** (2/7 as requester; Microhard, Digikey GCS WiFi boards, Mouser)
  - **Alex** (2/7 as requester; Sendcutsend #S1841769, Mouser)

- **Risk signals:**
  - 🟢 **CRITICAL REGRESSION RESOLVED — DELEGATION RESTORED:**
    - Meredith O'hara Needham: 3/7 (43%, **down from 82%**). 
    - Nate Straus: 4/7 (57%, **up from 18%**). **Delegation strategy is working; single-point-of-failure risk substantially reduced.**
    - 5 tasks successfully closed/removed from open list (likely auto-closed via form or manually resolved).
  
  - 🟡 **TASK STATUS MISMATCH PERSISTS — 4/7 TASKS "COMPLETED" BUT OPEN:**
    - "Order Shipped": Digikey GCS WiFi boards (#99879354)
    - "Order Received": sendcutsend for s3 sales (#SC51C906), Microhard / Hurricane GCS, jawstec (#69219), Mouser (#39526033)
    - **Form-based auto-closure is not functioning.** Manual closure required for all 4 completed orders immediately.
  
  - 🟡 **POSITIVE: OVERALL TASK HYGIENE IMPROVED** — 5/12 tasks from prior cycle successfully closed. Indicates process compliance improving despite form-closure lag.
  
  - 🟡 **SENDCUTSEND REAPPEARED AS OPEN TASK:**
    - sendcutsend for s3 sales (#SC51C906) due Jun 21, 2026 (Nate Straus assigned; status "Order Received").
    - Previously marked as "Order Shipped" with due date Jun 5 and noted as manually closed. **Task has been reopened or recreated with extended due date.** Clarify with Nate whether this is a second order or a task lifecycle error.
  
  - 🟡 **BILLING AMBIGUITY — 2 TASKS ASSIGNED TO "General Sales":**
    - compositeenvisions (due Jun 20) — assigned to "General Sales (No Specific Project)" but requester is Joshua Fromm (S3 focus); expect [001-7] IRAD S3 billing.
    - jawstec (due Jun 19) — assigned to "General Sales (No Specific Project)" but requester is Joshua Fromm (S3 focus); expect [001-7] IRAD S3 billing.
    - **Both likely belong to [001-7] IRAD S3; update project field in Asana before final billing.**

## Key Deliverables & Milestones

### **DUE JUNE 19, 2026 — 3 Tasks (Status: Mostly Completed)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| Sendcutsend (#S1841769) | Jun 19, 2026 | Order Placed | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | NO | Metal/composite cutting for Navy magnetometer SBIR. Status "Order Placed"; expected ship Jun 17, 2026. **CLOSE IMMEDIATELY when shipped.** |
| Digikey GCS WiFi boards (#99879354) | Jun 19, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | GCS WiFi-capable boards via Digikey. Status "Order Shipped" — **CLOSE IMMEDIATELY.** |
| jawstec for s3 parts - SALES (#69219) | Jun 19, 2026 | Order Received | **Nate Straus** | General Sales (No Specific Project) | Joshua Fromm | YES | Status "Order Received" — **CLOSE IMMEDIATELY.** Update project field to [001-7] IRAD S3 before billing. |
| Mouser (#39526033) | Jun 19, 2026 | Order Received | **Nate Straus** | [001-7] IRAD S3 | Alex | NO | Status "Order Received" — **CLOSE IMMEDIATELY.** |

### **DUE JUNE 20–21, 2026 — 3 Tasks (Status: Mixed)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| compositeenvisions for s3 sales | Jun 20, 2026 | Order Placed | Meredith O'hara Needham | General Sales (No Specific Project) | Joshua Fromm | YES | Order placement date Jun 16, 2026 (completed). Status "Order Placed" — track for shipment. **Update project field to [001-7] IRAD S3 before billing; reassign to Nate Straus.** |
| Microhard / Hurricane GCS | Jun 20, 2026 | Order Received | **Nate Straus** | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | Status "Order Received" (order placed May 11, 2026 — 40+ days ago). **CLOSE IMMEDIATELY.** Long delay indicates process breakdown; implement daily audit of "Order Received" tasks. |
| sendcutsend for s3 sales (#SC51C906) | Jun 21, 2026 | Order Received | **Nate Straus** | General Sales (No Specific Project) | Joshua Fromm | YES | Order placement date Jun 3, 2026 (completed 2+ weeks ago). Status "Order Received" — **CLOSE IMMEDIATELY.** **Clarify with Nate: is this a second order or task lifecycle error?** Update project field to [001-7] IRAD S3 before billing. |

## Task Summary

- **Total tasks:** 7 open, 0 completed (down from 11 open in prior cycle)
- **Tasks by assignee:**
  - **Nate Straus:** 4/7 (57%) — jawstec #69219, Microhard, sendcutsend #SC51C906, Mouser #39526033. All "Order Received" status — all **ready for immediate closure.**
  - **Meredith O'hara Needham:** 3/7 (43%) — composite