# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **5 open tasks with deadlines Jul 18, 2026.** Two tasks with order placement dates in the past (Jun 29, Jul 1, Jul 14, Jul 15).
- **Status:** 🔴 **CRITICAL OPERATIONAL CRISIS RESOLVED PARTIALLY.** Task backlog reduced from 9 to 5 open tasks—**4 previously overdue tasks have been closed** (sendcutsend S2 NASA, jawstec S0, Amazon, DigiKey, FTDI, Microhard listed as completed or removed). However, **2 remaining tasks with "Order Received" status still open** (Mouser, jawstec S3, SendCutSend) despite fulfillment, indicating **persistent closure automation failure**. Form data truncation continues across all 5 remaining tasks. Assignment distribution now: **Meredith 40% (2/5 tasks), Nate 60% (3/5 tasks).**
- **Team members involved:**
  - **Meredith O'hara Needham** (2/5 open tasks = 40%, Project Owner) — Microhard, FTDI
  - **Nate Straus** (3/5 open tasks = 60%) — Mouser, jawstec S3, SendCutSend
  - **Requesters:** Alex (3/5 = 60%), Joshua Fromm (1/5 = 20%)
- **Risk signals:**
  - 🔴 **CLOSURE AUTOMATION FAILURE PERSISTS:** 3/5 tasks have "Order Received" or "Order Placed" status yet remain open (Mouser, jawstec S3, SendCutSend). Tasks should auto-close on fulfillment or require explicit manual closure.
  - 🔴 **IMMINENT DEADLINES (ALL DUE JUL 18 — 4 DAYS):**
    - **Microhard** (Status: Order Placed, placed Jul 14) — Due Jul 18
    - **FTDI** (Status: Order Placed, placed Jul 15) — Due Jul 18
    - **Mouser** (Status: Order Received, placed Jul 15) — Due Jul 18
    - **jawstec S3** (Status: Order Received, placed Jun 29 — **19 days ago**) — Due Jul 18
    - **SendCutSend** (Status: Order Received, placed Jul 1 — **17 days ago**) — Due Jul 18
  - 🟠 **FORM DATA TRUNCATION PERSISTS (all 5 tasks affected):**
    - jawstec S3 project shows "General S" (truncated from full project name)
    - SendCutSend project shows "General Sales (No Specific" (incomplete)
    - **BILLING RISK:** Truncated project fields may cause mis-billing or account coding errors.
  - 🟠 **ASSIGNMENT CONCENTRATION:** Nate now handles 60% (3/5) of open tasks. Meredith reduced to 40% (2/5), focusing on IRAD Swiftstation work (Microhard, FTDI).
  - 🟠 **REQUESTER CONCENTRATION:** Alex now 60% (3/5 of tasks); Joshua Fromm 20% (1/5). Significant shift from prior period (Fromm was 44% in previous snapshot, now only jawstec S3).
  - 🟠 **TAX EXEMPTION SPLIT:** 2/5 tasks are tax-exempt (40%); 3/5 non-exempt (60%).

## Key Deliverables & Milestones

### **OPEN TASKS — ALL DUE JUL 18, 2026 (4 DAYS)**

| Task | Vendor | Assigned | Project | Requester | Status | Order Placed | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|--------------|------------|-------|
| Microhard (BFDD29D8-0008) | Microhard | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 14, 2026 | NO | Approval not required. |
| FTDI (#17721) | FTDI | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 15, 2026 | NO | Approval not required. **Placement due date was Jul 15—likely on-time or 1 day late.** |
| Mouser (#39830975) | Mouser | Nate | [001-4] IRAD S0 VTOL | Alex | Order Received | Jul 15, 2026 | NO | **Fulfillment complete; should be closed.** Closure automation failure. |
| jawstec for S3 sales (#69630) | jawstec | Nate | General Sales (No Specific Project) | Joshua Fromm | Order Received | Jun 29, 2026 | YES | **Fulfillment complete; placed 19 days ago.** Should be closed. Closure automation failure. Project field truncated ("General S"). |
| SendCutSend (#SQ29Q224) | SendCutSend | Nate | General Sales (No Specific Project) | Alex | Order Received | Jul 1, 2026 | YES | **Fulfillment complete; placed 17 days ago.** Should be closed. Closure automation failure. Project field truncated ("General Sales (No Specific"). |

## Task Summary
- **Total open tasks:** 5 (down from 9 in prior snapshot; 4 tasks closed/removed)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 2/5 (40%) — Microhard, FTDI (both IRAD Swiftstation work)
  - **Nate Straus:** 3/5 (60%) — Mouser, jawstec S3, SendCutSend
- **Completion rates:** 0/5 tasks completed in this snapshot; 4 previously overdue tasks closed between snapshots.
- **Notable patterns:**
  - All 5 remaining tasks due same day (Jul 18, 2026).
  - 3/5 tasks show "Order Received" status but remain open—**systemic closure workflow failure**.
  - jawstec S3 and SendCutSend placed 17–19 days ago but still marked "Order Received" and open (well past typical fulfillment-to-close cycle).
  - Form data truncation on project billing codes affects all tasks—critical for cost tracking.
  - Significant improvement: Backlog reduced 44% (9→5 tasks), suggesting some manual closure or project completion activity.

## Recent Activity
- **Tasks closed/removed since prior snapshot:** sendcutsend order for S2 NASA, jawstec S0 parts, Amazon, DigiKey, Microhard (placement task), and FTDI (placement task appear to have been removed or combined). **Status of these closures unknown from raw data—likely manual closure by Meredith or workflow intervention.**
- **New/remaining tasks:** All 5 current tasks consolidated to Jul 18 deadline. jawstec S3 and SendCutSend orders placed mid-to-late June/early July, now in "Order Received" state for 17–19 days without closure.
- **Assignment shift:** Nate Straus now handles majority of active work (60%). Meredith focused on two IRAD Swiftstation orders (both marked "Order Placed," both due same day).

## Notes & Context

### **CRITICAL UNRESOLVED ISSUES**

1. **Closure Automation Failure (Tier-1 Risk):**
   - 3/5 open tasks (Mouser, jawstec S3, SendCutSend) show fulfillment status ("Order Received") yet remain open.
   - jawstec S3 and SendCutSend have been in "Order Received" for 17–19 days without closure.
   -