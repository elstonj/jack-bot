_Asana snapshot as of 2026-11-14: 194 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active (high volume of pending orders)
- **Risk Signal:** **Communication breakdown — Joshua Fromm reports he is not receiving purchasing email forwards as of 2026-11-13** (per team feedback). Many orders assigned to him remain open. Additionally, 194 open tasks with 0 completed suggests tasks are not being marked complete after orders are placed/received.

## Key Issues

### ⚠️ Immediate: Email Forwarding Problem
**[2026-11-13] Joshua Fromm reports:** "i think maybe i got removed from the purchasing email forward… not sure, not getting any emails"

This indicates a **critical communication gap**. Joshua is the primary requester on ~80% of the open orders, but may not be receiving status updates or alerts. This could cause:
- Orders being placed twice
- Delays in order placement
- Lost visibility of delivery dates

**Action Required:** Verify Joshua is on the purchasing email distribution and restore if needed.

---

## Task Summary

### Volume & Completion
- **Total Open:** 194 tasks
- **Completed:** 0 tasks
- **Implied Issue:** Orders marked "Order Received," "Order Shipped," or "Order Placed" are still open in Asana. This suggests the workflow does not include task closure after delivery/receipt, creating stale data.

### Tasks by Assignee
| Assignee | Count | Notes |
|---|---|---|
| **Meredith O'hara Needham** | ~15 | Primary owner; executing purchases |
| **Joshua Fromm** | ~140+ | Primary requester; **not receiving emails per 11/13 feedback** |
| **Unassigned** | ~40 | Old orders (many from June–Sept 2026, already received) |
| Other requesters (Alex, Spencer, Sam, Ali, Dan, etc.) | ~20 | Various one-off purchases |

---

## Recent Activity & Upcoming Deadlines

### **OVERDUE (Due dates in Sept–Oct 2026, still open)**
- Microhard 10x p900 / 100x p400 | [300-3] 2026 IDIQ | Due 2026-11-07 | Status: "Order Placed" | Jack Elston requester
- PSKN3-24/55S antenna / StepGlobal | [001-7] IRAD S3 | Due 2026-10-11 | Status: "Order Placed" | Dan P. requester
- Components for Ground Antenna | [001-7] IRAD S3 | Due 2026-09-27 | Status: "Order Placed" | Dan requester
- icare order for s0 idiq | [300-3] 2026 IDIQ | Due 2026-07-26 | Status: "Order Placed" | Joshua Fromm requester
- Many tasks from June–Aug 2026 marked "Order Received" but never closed

### **APPROACHING (Nov 2026)**
- **Dronetag DRI RID Module** | [001-8] IRAD Flight Testing | Due **2026-11-13** (TODAY) | Jack Elston | Requires Approval: Yes
- **composite envisions for s3 (backorder)** | Future Sales | Due **2026-11-11** (OVERDUE) | Joshua Fromm
- **protolabs for s3 sales** | Future Sales | Due **2026-11-15** | Joshua Fromm | Status: "Order Placed"
- **materials for QC kits** (ESD trays, FTDI boards) | [001-1] IRAD General | Due **2026-11-15** | Ali Sulehria | Requires Approval: Yes | Status: "Order Placed"
- **digikey for s3 parts** | Future Sales | Due **2026-11-15** | Joshua Fromm | Status: "Order Placed"
- **FLIR Hadron 640R Camera** | [001-23] SOCOM S0-AD | Due **2026-11-12** | Dan | Status: "Order Placed"
- **jawstec for s3 parts** | [451-1] INSTAAR S3 x2 | Due **2026-11-13** | Joshua Fromm | Status: "Order Received"

### **Backlog (Due Dec 2026–Jan 2027)**
~120 tasks marked "Order Placed in Inventory" with due dates of 2026-12-29 or 2027-01-04. These include:
- S3 repairs (laser, regulator, backup regulators, RF connectors)
- Shop supplies and equipment
- [300-3] Hurricane IDIQ parts
- [001-7] IRAD S3 parts
- [600-01] SOCOM Pope ii components

---

## Notes & Context

### Workflow Issues
1. **No Task Closure:** Orders with statuses "Order Received," "Order Shipped," and "Order Placed in Inventory" remain open. This creates:
   - False sense of open volume
   - Inability to distinguish active vs. completed work
   - Stale data for planning

2. **Tax Exempt & Approval Tracking:**
   - Custom fields capture tax-exempt status (YES/NO) and approval requirement
   - Only ~5 tasks require approval (>$200); most are pre-approved

3. **Project Billing:**
   - Orders span multiple projects: [001-x] IRAD variants, [300-3] Hurricane IDIQ, [451-1] INSTAAR S3, [550-1] Navy SBIR, [600-01] SOCOM Pope ii, [043-3] Mustang Pt. 2, [039-1] S2 Oklahoma, and "Future Sales" / "General Sales" / "Shop Supplies"
   - Some orders split across "MULTIPLE PROJECT — PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" (tracking gap)

4. **Vendor Frequency:**
   - Repeat vendors: Jawstec, McMaster, Digikey, Amazon, Mouser, SendCutSend, Protolabs, Composite Envisions
   - Suggests established procurement relationships; opportunity for batch discounting or account review

### Communication Gaps
- Joshua Fromm's email forwarding issue (11/13/2026) is **critical**—he is the primary requester but may not be aware of order statuses.
- No evidence of escalation for overdue items (Sept–Oct orders still open).
- Form-based submission (linked in project notes) may not be triggering notifications properly.

### Budget Data
No total budget or milestones provided in Asana. Order amounts are not visible in task titles. Custom fields may store cost data, but it is not exported in the raw data.

---

## Recommendations
1. **Restore Joshua Fromm's email access immediately.**
2. **Implement task closure workflow:** Once an order is received/placed in inventory, close the task to reduce noise.
3. **Review overdue orders from Sept–Oct 2026:** Determine if items have actually been received/used and close out accordingly.
4. **Audit "Order Placed in Inventory" items:** Many have vague request dates (May–Aug 2026). Clarify scope and intended project.
5. **Aggregate project spending:** Cross-check Asana against actual invoices/POs to verify accuracy.