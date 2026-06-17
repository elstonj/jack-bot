# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due June 12–18, 2026
- **Status:** **ACTIVE — ESCALATING.** 9 open tasks (up from 5). 4 tasks already marked "Order Placed" or "Order Shipped" but remain open in task list — suggests form-based tasks are not auto-closing on status update. **2 overdue tasks:** Microhard (due May 11, 2026 — 36+ days overdue) and jawstec #69219 (due Jun 12, 2026 — likely overdue as of current snapshot date). All tasks assigned to Meredith O'hara Needham; single-point-of-failure concentration persists at 100%.
- **Team members involved:**
  - **Meredith O'hara Needham** (9/9 assigned tasks; project owner; order placement role)
  - **Nate Straus** (3/9 as requester; GCS parts focus)
  - **Joshua Fromm** (4/9 as requester; S3 sales, S0 IDIQ, compositeenvisions)
  - **Alex** (1/9 as requester; S3 procurement)
  - **Sam** (1/9 as requester; Hurricane GCS parts — new requester)

- **Risk signals:**
  - 🔴 **ASSIGNMENT CONCENTRATION CRITICAL:** All 9/9 tasks assigned to Meredith O'hara Needham (100%). Single-point-of-failure risk unchanged from prior snapshot; no delegation improvement made.
  - 🔴 **OVERDUE TASKS:** 
    - **Microhard / Hurricane GCS** — due May 11, 2026 (36+ days overdue; status "Order Shipped" suggests fulfillment complete, but task remains open).
    - **jawstec for s3 parts - SALES** — due Jun 12, 2026 (status "Order Shipped" suggests fulfillment; task should be closed).
  - 🟡 **TASK STATUS MISMATCH:** 4/9 tasks have "Order Placed" or "Order Shipped" status but remain open in task list. Form-based task auto-closure may not be triggering correctly. **Action needed:** Close or archive completed orders to reduce clutter and improve tracking accuracy.
  - 🟡 **BILLING AMBIGUITY PERSISTS:** "compositeenvisions for s3 sales" assigned to "General Sales (No Specific Project)" — flagged in prior snapshot as unresolved. **Still requires clarification before placement.**
  - 🟡 **DUE DATE INFLATION:** Original snapshot showed tasks due Jun 15–16, 2026; new data shows most now due Jun 18, 2026 (3-day slip). Microhard shows May 11 (placed in past). Suggests task due dates may not reflect actual procurement windows.

## Key Deliverables & Milestones

### **OVERDUE — REQUIRES CLOSURE**

| Task | Due | Status | Assigned | Project | Requester | Notes |
|------|-----|--------|----------|---------|-----------|-------|
| Microhard / Hurricane GCS (#TBD) | May 11, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate Straus | 🔴 **36+ days overdue.** Status "Order Shipped" suggests fulfillment complete. **Close task immediately.** |
| jawstec for s3 parts - SALES (#69219) | Jun 12, 2026 | Order Shipped | Meredith O'hara Needham | General Sales (No Specific Project) | Joshua Fromm | 🟡 **Likely overdue.** Status "Order Shipped" confirms fulfillment. **Close task; clarify whether this is [001-7] IRAD S3 or external sales revenue.** |

### **DUE JUNE 18, 2026 — 6 Tasks (Status: Mixed)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| hurricane GCS Parts (#99854859) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Sam | NO | GCS procurement for Hurricane IDIQ. Status "Order Placed" — task should be progressed or archived. |
| servocity for s3 canada demo (#300044802) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [001-7] IRAD S3 | Joshua Fromm | NO | S3 Canada demo components. Status "Order Placed" — task eligible for closure pending fulfillment. |
| batteries for s0 idiq (#500103) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | YES | Battery procurement for S0 IDIQ (Hurricane component). Status "Order Placed." |
| Digikey (GCS parts) (#99853994) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate Straus | NO | GCS components via Digikey. Status "Order Placed." Originally due Jun 15; 3-day slip. |
| Amazon / GCS | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate Straus | NO | GCS procurement via Amazon. Status "Order Placed." Originally due Jun 15; 3-day slip. |
| Mouser (#39526033) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [001-7] IRAD S3 | Alex | NO | Electronic components for S3 IRAD. Status "Order Placed." Originally due Jun 15; 3-day slip. |

### **DUE JUNE 16, 2026 — 1 Task**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| compositeenvisions for s3 sales | Jun 16, 2026 | Open | Meredith O'hara Needham | General Sales (No Specific Project) | Joshua Fromm | YES | ⚠️ **BILLING CLARIFICATION NEEDED:** Assigned to "General Sales" but references "s3 sales." Likely [001-7] IRAD S3 or external sales fulfillment. **Confirm project allocation before placement.** |

## Task Summary
- **Total tasks:** 9 open, 0 completed (up from 5 in prior snapshot)
- **Task status breakdown:**
  - Open (not yet placed): 1 task (11%) — compositeenvisions
  - Order Placed: 6 tasks (67%) — hurricane GCS, servocity, batteries, Digikey, Amazon, Mouser
  - Order Shipped: 2 tasks (22%) — jawstec #69219, Microhard
- **Assignee breakdown:**
  - Meredith O'hara Needham: 9/9 (100%) — **CONCENTRATION UNCHANGED; critical single-point-of-failure**
- **Requester breakdown:**
  - Joshua Fromm: 4/9 (44%) — compositeenvisions, servocity, batteries, jawstec
  - Nate Straus: 3/9 (33%) — Digikey, Amazon, Microhard
  - Alex: 1/9 (11%) — Mouser
  -