# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders due June 18–20, 2026
- **Status:** **ACTIVE — ESCALATING WITH PERSISTENT SINGLE-POINT-OF-FAILURE RISK.** 11 open tasks (up from 10). **CRITICAL REGRESSION: Assignment concentration has REBOUNDED to 85% (9/11 on Meredith O'hara Needham); delegation to Nate Straus reduced to 2/11 (jawstec, Mouser).** New task (compositeenvisions) assigned to Meredith despite earlier delegation attempt. **6/11 tasks marked "Order Shipped" or "Order Received" but remain open** — form-based auto-closure still not functioning. **1 PREVIOUSLY OVERDUE TASK (sendcutsend for s3 sales, due Jun 5) appears to have been MANUALLY CLOSED or removed from task list** — good hygiene signal. New task (Microhard / Hurricane GCS) added as "Order Received" status but remains open (due Jun 20).
- **Team members involved:**
  - **Meredith O'hara Needham** (9/11 assigned tasks; project owner; primary order placement role; **concentration increased from 8/10**)
  - **Nate Straus** (2/11 assigned tasks; jawstec #69219, Mouser #39526033; co-lead role **shrinking relative to total tasks**)
  - **Joshua Fromm** (4/11 as requester; S3 sales, S0 IDIQ, compositeenvisions focus)
  - **Nate** (4/11 as requester; GCS parts, WiFi boards, Microhard focus)
  - **Alex** (2/11 as requester; Sendcutsend, Mouser; magnetometer SBIR focus)
  - **Sam** (1/11 as requester; Hurricane GCS parts)

- **Risk signals:**
  - 🔴 **ASSIGNMENT CONCENTRATION REBOUNDED — REGRESSION OBSERVED:**
    - Meredith O'hara Needham: 9/11 (82%, **up from 80%**). New task (compositeenvisions) assigned to Meredith despite prior delegation to Nate. **Single-point-of-failure risk has WORSENED.**
    - Nate Straus: 2/11 (18%, **down from 20%**). Delegation attempt appears to have stalled; no new tasks assigned to Nate since previous cycle.
    - **Recommendation:** Reassign new tasks (compositeenvisions, Microhard, Sendcutsend, Digikey WiFi boards) to Nate to restore delegation momentum and reduce Meredith bottleneck.
  
  - 🟡 **TASK STATUS MISMATCH PERSISTS — 6/11 TASKS "COMPLETED" BUT OPEN:**
    - "Order Shipped": Digikey GCS WiFi boards, hurricane GCS Parts, Digikey (GCS parts), Amazon / GCS, servocity
    - "Order Received": Microhard / Hurricane GCS, jawstec, Mouser
    - **Form-based auto-closure is not functioning.** Manual closure required for completed orders.
  
  - 🟡 **POSITIVE: OVERDUE TASK CLOSURE** — sendcutsend for s3 sales (#SC51C906, due Jun 5) no longer appears in open task list. Status "Order Shipped" has been resolved via manual closure or task removal. **Good hygiene; repeat for remaining completed orders.**
  
  - 🟡 **NEW TASK (Microhard / Hurricane GCS) ADDED WITH EARLY ORDER DATE:**
    - Order placed May 11, 2026 (1+ month ago); due Jun 20; status "Order Received" (fulfilled).
    - **Task should have been closed immediately upon receipt; 5+ weeks delayed closure indicates process breakdown.**
  
  - 🟡 **BILLING AMBIGUITY — 2 TASKS ASSIGNED TO "General Sales":**
    - compositeenvisions (NEW, due Jun 20) — assigned to "General Sales (No Specific Project)" but requester is Joshua Fromm (S3 focus).
    - jawstec (ongoing, due Jun 19) — assigned to "General Sales (No Specific Project)"; unclear whether [001-7] IRAD S3 or external revenue.
    - **Clarify project allocation before final billing.**

## Key Deliverables & Milestones

### **DUE JUNE 18, 2026 — 5 Tasks (Status: Mixed)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| hurricane GCS Parts (#99854859) | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Sam | NO | GCS procurement for Hurricane IDIQ. Status "Order Shipped" — **CLOSE IMMEDIATELY.** |
| batteries for s0 idiq (#500103) | Jun 18, 2026 | Order Placed | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | YES | Battery procurement for S0 IDIQ (Hurricane component). Status "Order Placed" — track for shipment. |
| Digikey (GCS parts) (#99853994) | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | GCS components via Digikey. Status "Order Shipped" — **CLOSE IMMEDIATELY.** |
| Amazon / GCS | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | GCS procurement via Amazon. Status "Order Shipped" — **CLOSE IMMEDIATELY.** |
| servocity for s3 canada demo (#300044802) | Jun 18, 2026 | Order Shipped | Meredith O'hara Needham | [001-7] IRAD S3 | Joshua Fromm | NO | S3 Canada demo components. Status "Order Shipped" — **CLOSE IMMEDIATELY.** |

### **DUE JUNE 19, 2026 — 3 Tasks (Status: Mixed)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| Sendcutsend (#S1841769) | Jun 19, 2026 | Order Placed | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | NO | Metal/composite cutting for Navy magnetometer SBIR. Status "Order Placed"; expected ship Jun 17, 2026. **REASSIGN TO NATE STRAUS.** |
| Digikey GCS WiFi boards (#99879354) | Jun 19, 2026 | Order Shipped | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | NO | GCS WiFi-capable boards via Digikey. Status "Order Shipped" — **CLOSE IMMEDIATELY.** |
| jawstec for s3 parts - SALES (#69219) | Jun 19, 2026 | Order Received | **Nate Straus** | General Sales (No Specific Project) | Joshua Fromm | YES | Status "Order Received" — **CLOSE IMMEDIATELY.** Clarify billing allocation ([001-7] IRAD S3 vs. external sales). |
| Mouser (#39526033) | Jun 19, 2026 | Order Received | **Nate Str