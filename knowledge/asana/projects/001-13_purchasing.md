# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **All 5 open tasks due Jul 18, 2026 (4 days).**
- **Status:** 🔴 **CRITICAL OPERATIONAL ISSUES PERSIST.** Backlog reduced from 9 to 5 open tasks (4 closed between snapshots), but **closure automation failure continues:** 3/5 tasks show "Order Received" status (fulfillment complete) yet remain open. **All remaining tasks converge on single deadline (Jul 18).** Form data truncation persists across all 5 tasks, creating billing/coding risk.
- **Team members involved:**
  - **Meredith O'hara Needham** (2/5 open tasks = 40%, Project Owner) — Microhard, FTDI
  - **Nate Straus** (3/5 open tasks = 60%) — Mouser, jawstec S3, SendCutSend
  - **Requesters:** Alex (3/5 = 60%), Joshua Fromm (1/5 = 20%)
- **Risk signals:**
  - 🔴 **CLOSURE AUTOMATION FAILURE:** 3/5 tasks have "Order Received" status yet remain open (Mouser, jawstec S3, SendCutSend). jawstec S3 and SendCutSend have been in "Order Received" for 19 and 17 days respectively without closure.
  - 🔴 **IMMINENT SINGLE DEADLINE:** All 5 tasks due Jul 18, 2026 (4 days). Two tasks ("Order Placed") may still be in transit; three tasks ("Order Received") should be resolved.
  - 🟠 **FORM DATA TRUNCATION (all 5 tasks affected):** Project billing codes truncated ("General S" instead of full project name; "General Sales (No Specific" incomplete). **Billing/cost allocation risk.**
  - 🟠 **ASSIGNMENT CONCENTRATION:** Nate Straus handles 60% (3/5) of remaining work.

## Key Deliverables & Milestones

### **OPEN TASKS — ALL DUE JUL 18, 2026**

| Task | Vendor | Assigned | Project | Requester | Status | Order Date | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|------------|------------|-------|
| Microhard (BFDD29D8-0008) | Microhard | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 14, 2026 | NO | Approval not required. |
| FTDI (#17721) | FTDI | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 15, 2026 | NO | Approval not required. Placement due date was Jul 15 (likely on-time or 1 day late). |
| Mouser (#39830975) | Mouser | Nate | [001-4] IRAD S0 VTOL | Alex | Order Received | Jul 15, 2026 | NO | **Fulfillment complete; should be closed.** Closure automation failure. |
| jawstec for S3 sales (#69630) | jawstec | Nate | General Sales (No Specific Project) | Joshua Fromm | Order Received | Jun 29, 2026 | YES | **Fulfillment complete; placed 19 days ago.** Should be closed. Closure automation failure. Project field truncated ("General S"). |
| SendCutSend (#SQ29Q224) | SendCutSend | Nate | General Sales (No Specific Project) | Alex | Order Received | Jul 1, 2026 | YES | **Fulfillment complete; placed 17 days ago.** Should be closed. Closure automation failure. Project field truncated ("General Sales (No Specific"). |

## Task Summary
- **Total open tasks:** 5 (down from 9 in prior snapshot; 4 tasks closed/removed between updates)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 2/5 (40%) — both IRAD Swiftstation orders in "Order Placed" status
  - **Nate Straus:** 3/5 (60%) — all three "Order Received" tasks (highest risk group)
- **Completion rates:** 0/5 tasks completed in this snapshot; 4 previously open tasks successfully closed/removed.
- **Notable patterns:**
  - **All 5 tasks consolidated to single deadline (Jul 18).** Represents 100% task concentration on one date—high operational risk if any fail.
  - **3/5 tasks in "Order Received" state but still open:** Systemic workflow failure. jawstec S3 and SendCutSend have exceeded normal fulfillment-to-closure window by 2+ weeks.
  - **Form data truncation on all 5 tasks:** Project billing codes incomplete, affecting cost allocation accuracy.
  - **2/5 tasks (40%) are tax-exempt; 3/5 (60%) taxable.** Split across both vendors and requesters.

## Recent Activity
- **Tasks closed since prior snapshot:** At least 4 previously overdue tasks removed/completed (sendcutsend S2 NASA, jawstec S0, Amazon, DigiKey, and others). Backlog improved 44% (9→5 tasks).
- **Current state (no change from prior snapshot):** All 5 tasks remain at same status and due date. No new closures or status updates observed.
- **jawstec S3 and SendCutSend:** Both have been in "Order Received" status for extended periods (17–19 days) without closure, indicating persistent workflow automation failure.

## Notes & Context

### **CRITICAL UNRESOLVED ISSUES**

1. **Closure Automation Failure (Tier-1 Risk):**
   - 3/5 open tasks (Mouser, jawstec S3, SendCutSend) show "Order Received" status yet remain open in Asana.
   - jawstec S3 placed Jun 29 (19 days ago); SendCutSend placed Jul 1 (17 days ago)—both well past normal fulfillment cycle.
   - **Action required:** Manual closure or workflow fix to auto-close tasks on "Order Received" status. These may represent completed work that is simply not being marked done.

2. **Form Data Truncation (Billing Risk):**
   - All 5 remaining tasks have incomplete project billing codes in custom fields:
     - jawstec S3: "General S" (truncated)
     - SendCutSend: "General Sales (No Specific" (incomplete)
   - **Impact:** Potential mis-billing or cost allocation errors if these codes are used for accounting.
   - **Root cause:** Form field or Asana custom field character limit.

3. **Single Deadline Concentration:**
   - All 5 tasks due Jul 18, 2026 (4 days away). No staggered delivery or fallback timeline.
   - Two tasks ("Order Placed" status) may still be in transit; three tasks should already be resolved.

4. **Operational Improvement:** Backlog reduction from 9→5 tasks suggests manual intervention or project completion activity between snapshots. Recommend process review to understand how 4 tasks were successfully closed and replicate for remaining 3.

---

**Last Updated:** Per new raw data snapshot; prior snapshot date unknown.