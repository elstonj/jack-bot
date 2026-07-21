# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **4 open tasks with mixed deadlines: Jul 8 (overdue), Jul 22 (14 days).**
- **Status:** 🔴 **CRITICAL OPERATIONAL ISSUES PERSIST.** Task count down to 4 (from 5), but **one task is overdue (Jul 8), closure automation failure continues, and form data remains truncated.** New tasks assigned to Meredith (2 tasks, up from 1). jawstec S0 parts reappear as separate task.
- **Team members involved:**
  - **Meredith O'hara Needham** (2/4 open tasks = 50%, Project Owner) — jawstec S0 parts (IDIQ), jawstec sales
  - **Nate Straus** (2/4 open tasks = 50%) — SendCutSend S2 NASA, jawstec S0 parts
  - **Requester:** Joshua Fromm (all 4 tasks = 100%)
- **Risk signals:**
  - 🔴 **OVERDUE TASK:** jawstec for sales (#69738) due Jul 8, 2026 — **14 days overdue.** Status "Order Shipped" but remains open.
  - 🔴 **CLOSURE AUTOMATION FAILURE CONTINUES:** 2/4 tasks in fulfillment states ("Order Shipped", "Order Received") yet remain open.
  - 🟠 **FORM DATA TRUNCATION (all 4 tasks affected):** Project billing codes incomplete or marked "MULTIPLE PROJECT" without breakdown. jawstec S0 tasks truncated ("2" instead of full project code).
  - 🟠 **REASSIGNMENT TO MEREDITH:** jawstec S0 parts (#JT70002) now assigned to Meredith (previously Nate). Potential workflow shift or load rebalancing.
  - 🟠 **ALL 4 TASKS SINGLE REQUESTER:** Joshua Fromm 100% — concentration risk if requester becomes unavailable.

## Key Deliverables & Milestones

### **OPEN TASKS**

| Task | Vendor | Assigned | Project | Requester | Status | Order Placement Date | Due Date | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|----------------------|----------|------------|-------|
| jawstec for s0 parts (#JT70002) | jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 20, 2026 | Jul 22, 2026 | YES | Placement due Jul 20; task due Jul 22 (2-day window). Project code truncated ("2"). |
| jawstec for sales - see details (#69738) | jawstec | Meredith | MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN | Joshua Fromm | Order Shipped | Jul 6, 2026 | **Jul 8, 2026** | YES | **🔴 OVERDUE by 14 days.** Status "Order Shipped" but remains open. No project breakdown provided. |
| sendcutsend order for s2 nasa (S439K456) | SendCutSend | Nate | [212-2] NASA S2 & Parts | Joshua Fromm | Order Received | Jul 7, 2026 | Jul 22, 2026 | YES | Fulfillment complete (Order Received); should be closed. |
| jawstec for s0 parts (#69825) | jawstec | Nate | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Received | Jul 9, 2026 | Jul 22, 2026 | YES | Fulfillment complete (Order Received); should be closed. Project code truncated ("20"). |

## Task Summary
- **Total open tasks:** 4 (down from 5 in prior snapshot)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 2/4 (50%, up from 40%) — jawstec S0 parts (Order Placed), jawstec sales (Order Shipped, **overdue**)
  - **Nate Straus:** 2/4 (50%, down from 60%) — SendCutSend S2 NASA, jawstec S0 parts
- **Completion rates:** 0/4 tasks completed in this snapshot; 1 task removed from prior update (Microhard, FTDI, Mouser tasks gone; prior knowledge file showed 5 tasks).
- **Notable patterns:**
  - **jawstec S0 parts appears twice** (#JT70002 assigned to Meredith, #69825 assigned to Nate) — potential duplicate or workflow split across projects/requesters.
  - **100% requester concentration:** All 4 tasks requested by Joshua Fromm.
  - **2/4 tasks in fulfillment states ("Order Shipped", "Order Received") yet remain open:** Closure automation failure persists.
  - **Form data truncation on all 4 tasks:** jawstec sales missing project breakdown; jawstec S0 codes show "2" and "20" (incomplete).
  - **All 4 tasks are tax-exempt.**

## Recent Activity
- **Major change:** Prior snapshot showed 5 tasks with Jul 18 deadline (Microhard, FTDI, Mouser, jawstec S3, SendCutSend). This snapshot shows **completely different 4 tasks** with Jul 8 (overdue) and Jul 22 (new) deadlines.
  - **jawstec S3 sales (from prior snapshot) likely merged into jawstec for sales (#69738, now assigned to Meredith)** — prior task was "Order Received" status; current task shows "Order Shipped" status. **Task is now 14 days overdue.**
  - Mouser, FTDI, Microhard, prior SendCutSend task: **removed/completed between snapshots** (4 tasks closed).
  - New tasks: jawstec S0 parts (#JT70002), jawstec S0 parts (#69825), sendcutsend S2 NASA replacement.
- **Nate Straus losing tasks to Meredith:** Nate assignment concentration decreased from 60% to 50%. Meredith now managing both S0 orders and overdue sales task.

## Notes & Context

### **CRITICAL UNRESOLVED ISSUES**

1. **🔴 OVERDUE TASK — IMMEDIATE ACTION REQUIRED:**
   - **jawstec for sales (#69738):** Due Jul 8, 2026. **Status "Order Shipped" — task should be closed and resolved.** Remaining open for 14+ days indicates either:
     - Shipping delay or delivery issue.
     - Task closure workflow failure (not auto-closing on "Order Shipped" status).
   - **Action:** Verify delivery status; if received, close task immediately. If delayed, escalate to vendor.

2. **Closure Automation Failure (Tier-1 Risk) — UNRESOLVED:**
   - 2/4 tasks in fulfillment states ("Order Shipped", "Order Received") remain open.
   - SendCutSend S2 NASA (#S439K456): "Order Received" status yet task remains open.
   - jawstec S0 parts (#69825): "Order Received" status yet task remains open.
   - **Root cause:** Workflow automation not triggering on "Order Shipped" or "Order Received" status transitions. Prior snapshot noted jawstec S3 and SendCutSend tasks persisted in "Order Received" for 17–19 days without closure—**same pattern repeats here.**
   - **Action required:** Manual closure protocol or workflow fix. Consider batch-closing all "Order Received"/"Order Shipped" tasks weekly.

3. **Form Data Truncation & Incomplete Billing Codes (Tier-2 Risk) — UNRESOLVED:**
   - **jawstec for sales (#69738)