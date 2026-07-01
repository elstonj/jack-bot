# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; critical deadlines **JUL 1–2, 2026** (10 open tasks due within 48 hours)
- **Status:** 🔴 **CRITICAL OPERATIONAL STRESS.** Task list stabilized at **10 open tasks** (vs. prior cycle's rebound to 17). **PRIOR UNEXPLAINED REAPPEARANCE CYCLE RESOLVED** — the 11 "Order Placed in Inventory" tasks with Aug 28 due date are NO LONGER VISIBLE in current data pull. Current workload is **form-driven and assignment-focused:** 6 tasks assigned to Meredith O'hara Needham, 4 to Nate Straus, 0 unassigned. **However, immediate execution risk is ACUTE: 8 of 10 tasks due JUL 1–2 with status "Order Placed" or "Order Received"—no evidence of invoicing, receipt verification, or project reconciliation.**

- **Team members involved:**
  - **Meredith O'hara Needham** (project owner; 6/10 open tasks = 60%)
  - **Nate Straus** (4/10 open tasks = 40%)
  - **Requesters:** Joshua Fromm (5 tasks), Ethan (2 tasks), Nate (1 task), Sam (1 task), Alex (1 task)

- **Risk signals:**
  - 🔴 **IMMINENT DUE DATES — NO SLACK:** 8 of 10 tasks due JUL 1–2, 2026 (within 48 hours of data pull). All assigned, but **no downstream visibility into receipt confirmation, invoice matching, or project cost reconciliation.** Tasks show "Order Placed" or "Order Shipped"/"Order Received" status but do **not** close upon completion—suggesting either manual archival required or workflow gap.
  - 🔴 **PRIOR CYCLE ANOMALY UNRESOLVED:** Previous knowledge file reported catastrophic task collapse (67% reduction) + unexplained reappearance of 11 tasks with reclassified due dates and status. **Current pull does NOT include those 11 tasks**, suggesting either deletion, archival, or reclassification to hidden view. **No audit trail, no correction note from team.** Risk of silent data loss or external workflow bypass.
  - 🟡 **TAX EXEMPTION & APPROVAL GAPS:** Multiple tasks show "Tax Exempt?: YES/NO" and "Requires Approval?: No" — no evidence of threshold-based approval enforcement. Jawstec orders (Tax Exempt: YES) are marked "Requires Approval?: No", but no PO trail visible in task notes.
  - 🟡 **NO POST-ORDER WORKFLOW:** All tasks remain open after "Order Placed"/"Order Received"—no subtasks for invoice verification, three-way match, or project billing confirmation. Single point of failure if orders require follow-up.

## Key Deliverables & Milestones

### **DUE JUL 1–2, 2026 — 10 TASKS (IMMEDIATE ACTION WINDOW, 48–72 HOURS)**

| Task | Due | Vendor | Assigned | Project | Requester | Status | Notes |
|------|-----|--------|----------|---------|-----------|--------|-------|
| jawstec for s0 idiq (#69631) | Jul 1, 2026 | Jawstec | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Tax Exempt; Requested Jun 29 |
| jawstec for s3 sales (#69630) | Jul 1, 2026 | Jawstec | Meredith O'hara Needham | General Sales | Joshua Fromm | Order Placed | Tax Exempt; Requested Jun 29 |
| amazon for s0 hurricane idiq | Jul 1, 2026 | Amazon | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Tax Exempt; Requested Jun 29 |
| digikey for idiq (#009799) | Jul 1, 2026 | Digikey | Nate Straus | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Received | Tax Exempt; Requested Jun 24 |
| HiTec- ByLight (#5526) | Jul 1, 2026 | HiTec/ByLight | Nate Straus | [043-3] Mustang Pt. 2 | Ethan | Order Received | Requested Jun 23 |
| GetFPV (#1001480217) | Jul 1, 2026 | GetFPV | Nate Straus | Shop Supplies | Alex | Order Received | Requested Jun 22 |
| Digikey- Bylight Order (#100124240) | Jul 2, 2026 | Digikey/ByLight | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | Requested Jun 30 |
| Digikey / Protektive Pak (#100117933) | Jul 2, 2026 | Digikey/Protektive Pak | Meredith O'hara Needham | [001-1] IRAD General | Nate | Order Shipped | Requested Jun 30 |
| Extra FTDI USB boards (#100117560) | Jul 2, 2026 | [Unknown] | Meredith O'hara Needham | Shop Supplies | Sam | Order Shipped | Requested Jun 30 |
| compositeenvisions for s3 sales | Jul 2, 2026 | Composite Envisions | Nate Straus | General Sales | Joshua Fromm | Order Received | Requested Jun 16 (oldest request in current batch) |

---

## Task Summary

- **Total tasks:** 10 open, 0 completed
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 6/10 (60%) — 3 "Order Placed", 3 "Order Shipped"
  - **Nate Straus:** 4/10 (40%) — 3 "Order Received", 1 "Order Received"
  - **Unassigned:** 0/10 (0%) — **IMPROVEMENT vs. prior cycle (65% dark)**

- **Status distribution:**
  - **Order Placed:** 4 tasks (Meredith: 3, Nate: 0, Meredith: 1 via Digikey-Bylight)
  - **Order Received:** 4 tasks (Nate: 4)
  - **Order Shipped:** 2 tasks (Meredith: 2)

- **Notable patterns:**
  - **Heavy concentration on two requesters:** Joshua Fromm (5 tasks), Ethan (2 tasks) account for 7/10 tasks.
  - **Project concentration:** [300-3] 2026 IDIQ (Hurricane) appears in 3 tasks (digikey, jawstec s0, amazon); General Sales in 2; [043-3] Mustang Pt. 2 in 2; [001-1] IRAD in 1; Shop Supplies in 2.
  - **Vendor concentration:** Digikey (3 tasks), Amazon (1), Jawstec (2), HiTec/ByLight (2), GetFPV, Composite Envisions, Protektive Pak (1 each).
  - **All form-driven:** Custom fields (Tax Exempt, Requires Approval, Requester name) fully populated—suggests form submission discipline is working. **However, form-based auto-delete mechanism referenced in project notes remains undocumented and unexplained.**

---