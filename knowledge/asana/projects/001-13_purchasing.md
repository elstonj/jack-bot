# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current order due June 21, 2026
- **Status:** **ACTIVE — CRITICAL REGRESSION.** Task count collapsed from 3 to 1 open task. **⚠️ CRITICAL: Remaining task ("sendcutsend #SC51C906") shows status "Order Received" but remains open — 18+ days past order placement (Jun 3, 2026). Form-based auto-closure still non-functional. Manual closure required immediately.**
- **Team members involved:**
  - **Nate Straus** (1/1 assigned; sendcutsend #SC51C906; maintains 100% of open workload)
  - **Joshua Fromm** (1/1 as requester; sendcutsend #SC51C906)
  - **Meredith O'hara Needham** (project owner; no open assignments)

- **Risk signals:**
  - 🔴 **CRITICAL CLOSURE FAILURE — 1 REMAINING TASK "COMPLETED" BUT OPEN:**
    - "Order Received": sendcutsend #SC51C906 (due Jun 21, placed Jun 3 — **18+ days stale**)
    - Form-based auto-closure is NOT functioning. Manual closure required **immediately**.
    - Task will auto-delete per project notes if not closed/submitted.
  
  - 🔴 **SINGLE-POINT-OF-FAILURE RISK: NATE STRAUS 100% OF OPEN TASKS** — Concentration spiked from 67% to 100% after mysterious closure/removal of Meredith's compositeenvisions task and Nate's Microhard task. Requires urgent investigation: Were these tasks legitimately closed, or did they auto-delete due to form-based mechanism failure?
  
  - 🟡 **BILLING AMBIGUITY PERSISTS:**
    - sendcutsend #SC51C906 assigned to "General Sales (No Specific Project)" (partial entry: "Genera") but requester is Joshua Fromm (S3 focus); likely [001-7] IRAD S3.
    - Must be reassigned to [001-7] IRAD S3 in project field before final billing.

## Key Deliverables & Milestones

### **DUE JUNE 21, 2026 — 1 Task (Status: "Order Received" but Open)**

| Task | Due | Status | Assigned | Project | Requester | Tax Exempt | Notes |
|------|-----|--------|----------|---------|-----------|-----------|-------|
| sendcutsend for s3 sales (#SC51C906) | Jun 21, 2026 | Order Received | **Nate Straus** | General Sales (No Specific Project) | Joshua Fromm | YES | Order placement date Jun 3, 2026 (completed 18+ days ago). Status "Order Received" — **CLOSE IMMEDIATELY.** Update project field to [001-7] IRAD S3 before billing. Task will auto-delete per project form policy if not actioned. |

## Task Summary

- **Total tasks:** 1 open, 0 completed (down from 3 in prior cycle; **67% reduction in open tasks**)
- **Tasks by assignee:**
  - **Nate Straus:** 1/1 (100%) — sendcutsend #SC51C906. Status "Order Received" — **ready for immediate closure.**
- **Requester distribution:**
  - **Joshua Fromm:** 1/1 (sendcutsend #SC51C906) — needs [001-7] IRAD S3 project reassignment

## Recent Activity

- **Dramatic task collapse:** Only 1 open task remains (down from 3). Two tasks have disappeared from the system:
  - **compositeenvisions** (was: Meredith O'hara Needham, "Order Placed" status, due Jun 20) — **no longer in Asana task list**
  - **Microhard / Hurricane GCS** (was: Nate Straus, "Order Received" status, due Jun 20) — **no longer in Asana task list**
  - **Possible explanations:** (1) Legitimate closure before last cycle, (2) auto-deletion by form-based mechanism, (3) manual removal. **Requires urgent clarification.**

- **Remaining task shows "completed" status (Order Received) but remains open.**
  - Order placed Jun 3, 2026 — now 18+ days past completion date.
  - Form-based auto-closure mechanism is **still not triggering closure** in Asana.
  - Task at imminent risk of auto-deletion per project notes.

- **Concentration risk spiked:** Nate Straus now holds 100% of open tasks (up from 67% in prior cycle). This is unsustainable and suggests either:
  - Legitimate closure of other tasks coinciding with process improvements, OR
  - Process failure (auto-deletion) affecting visibility.

## Notes & Context

- **URGENT ACTION REQUIRED:**
  1. **Close sendcutsend #SC51C906 task manually immediately** — do not rely on form-based auto-closure (clearly non-functional).
  2. **Investigate disappearance of compositeenvisions and Microhard tasks** — determine if they were legitimately closed, auto-deleted, or removed manually. If auto-deleted, this indicates the project form policy ("USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE") is triggering unintended deletions and must be disabled or redesigned.
  3. **Reassign sendcutsend #SC51C906 to [001-7] IRAD S3 project** in Asana before billing cycle (project field shows incomplete entry "Genera").
  4. **Contact Asana/IT re: form-based auto-closure and auto-deletion failures** — investigate why completed orders are not auto-closing and whether tasks are being auto-deleted per project policy.
  5. **Restore workload balance to Nate Straus and Meredith O'hara Needham** — if compositeenvisions and Microhard were legitimately closed, confirm closure mechanism and restart delegation pattern (67/33 split).

- **Form-based closure mechanism:** Project notes reference a form (https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594) with an auto-delete policy. Current data suggests:
  - Auto-closure for "Order Received"/"Order Placed" tasks is **non-functional**.
  - Auto-deletion for tasks not submitted via form **may be active** (explains disappearance of 2 tasks), but process is opaque.
  - **Recommend disabling auto-delete and implementing manual closure workflow** until form mechanism is debugged.

- **Billing ambiguity:** sendcutsend #SC51C906 shows incomplete project assignment ("Genera" — likely truncated "General Sales"). Must be corrected to [001-7] IRAD S3 before final billing.