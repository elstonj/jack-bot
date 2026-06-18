# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due June 5–19, 2026
- **Status:** **ACTIVE — ESCALATING WITH DELEGATION SHIFT.** 10 open tasks (up from 9). 6 tasks marked "Order Shipped" or "Order Received" but remain open in task list — form-based tasks are not auto-closing on status update. **1 OVERDUE TASK:** sendcutsend for s3 sales (due Jun 5, 2026 — 14+ days overdue). **CRITICAL CHANGE:** Assignment concentration reduced to 80% (8/10 on Meredith O'hara Needham; 2/10 newly assigned to Nate Straus) — first meaningful delegation observed. However, single-point-of-failure risk persists.
- **Team members involved:**
  - **Meredith O'hara Needham** (8/10 assigned tasks; project owner; primary order placement role)
  - **Nate Straus** (2/10 assigned tasks; NEW — jawstec #69219, Mouser #39526033; emerging co-lead)
  - **Joshua Fromm** (4/10 as requester; S3 sales, S0 IDIQ, compositeenvisions focus)
  - **Nate** (3/10 as requester; GCS parts, WiFi boards focus)
  - **Alex** (2/10 as requester; Mouser, Sendcutsend; magnetometer SBIR)
  - **Sam** (1/10 as requester; Hurricane GCS parts)

- **Risk signals:**
  - 🔴 **OVERDUE TASK — REQUIRES IMMEDIATE CLOSURE:**
    - **sendcutsend for s3 sales (#SC51C906)** — due Jun 5, 2026 (14+ days overdue; status "Order Shipped" confirms fulfillment). **Task must be closed immediately to reduce clutter.**
  - 🟡 **ASSIGNMENT CONCENTRATION IMPROVING BUT REMAINS HIGH:** Meredith O'hara Needham assigned to 8/10 (80%, down from 100%). Nate Straus now assigned to 2/10 (jawstec, Mouser). **Positive trend, but single-point-of-failure risk on Meredith persists.** Further delegation encouraged.
  - 🟡 **TASK STATUS MISMATCH PERSISTS:** 6/10 tasks have "Order Shipped" or "Order Received" status but remain open in task list (sendcutsend, hurricane GCS Parts, Digikey GCS parts, Amazon/GCS, servocity, jawstec, Mouser). **Form-based task auto-closure is not functioning correctly.** **Action needed:** Close completed orders manually to improve tracking accuracy.
  - 🟡 **DUE DATE DRIFT:** New tasks (Sendcutsend WiFi boards, Digikey GCS WiFi boards) due Jun 19, 2026; older tasks due Jun 5–18, 2026. Suggests mixed order windows or task aging without closure.
  - 🟡 **BILLING AMBIGUITY PERSISTS:** jawstec (#69219) and sendcutsend for s3 sales (#SC51C906) assigned to "General Sales (No Specific Project)" — unclear whether these are [001-7] IRAD S3 or external sales revenue. **Requires clarification before final billing.**

## Key Deliverables & Milestones

### **OVERDUE — REQUIRES IMMEDIATE CLOSURE**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| sendcutsend for s3 sales (#SC51C906) | Jun 5, 2026 | Order Shipped | Meredith O'hara Needham | General Sales (No Specific Project) | Joshua Fromm | YES | 🔴 **14+ days overdue.** Status "Order Shipped" confirms fulfillment complete. **Close task immediately; clarify billing allocation ([001-7] IRAD S3 vs. external sales).** |

### **DUE JUNE 18, 2026 — 5 Tasks (Status: Mixed)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| hurricane GCS Parts (#99854859) | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Sam | NO | GCS procurement for Hurricane IDIQ. Status "Order Shipped" — task should be closed pending final receipt. |
| servocity for s3 canada demo (#300044802) | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [001-7] IRAD S3 | Joshua Fromm | NO | S3 Canada demo components. Status "Order Shipped" — task eligible for closure. |
| batteries for s0 idiq (#500103) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | YES | Battery procurement for S0 IDIQ (Hurricane component). Status "Order Placed" — track for shipment. |
| Digikey (GCS parts) (#99853994) | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | GCS components via Digikey. Status "Order Shipped" — task eligible for closure. |
| Amazon / GCS | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | GCS procurement via Amazon. Status "Order Shipped" — task eligible for closure. |

### **DUE JUNE 19, 2026 — 2 Tasks (NEW + REASSIGNED)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| Sendcutsend (#S1841769) | Jun 19, 2026 | Order Placed | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | NO | 🆕 **NEW TASK.** Metal/composite cutting for Navy magnetometer SBIR. Status "Order Placed." Expected ship Jun 17, 2026. New project assignment: [550-1]. |
| Digikey GCS WiFi boards (#99879354) | Jun 19, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | 🆕 **NEW TASK.** GCS WiFi-capable boards via Digikey. Status "Order Placed." Expected ship Jun 17, 2026. |

### **DUE JUNE 19, 2026 — 2 Tasks (REASSIGNED TO NATE)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| jawstec for s3 parts - SALES (#69219) | Jun 19, 2026 | Order Received | **Nate Straus** | General Sales (No Specific Project) | Joshua Fromm | YES | 🔄 **REASSIGNED TO NATE STRAUS** (previously Meredith). Status "Order Received" — task eligible for closure. **Clarify billing allocation.** |
| Mouser (#39526033) | Jun