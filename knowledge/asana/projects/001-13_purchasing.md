# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **9 open tasks with deadlines spanning Jul 9–Jul 18, 2026.** **Multiple tasks severely overdue** (sendcutsend S2 NASA due Jul 9, jawstec S0 due Jul 11; both now 5+ days past). Multiple tasks due imminently (Jul 16–18).
- **Status:** 🔴 **CRITICAL OPERATIONAL CRISIS.** Task backlog has nearly **doubled from 5 to 9 open tasks** in single update. **Multiple severely overdue tasks with "Order Shipped" or "Order Received" status remain unclosed,** indicating severe closure automation/workflow failure. Assignment has shifted dramatically: Meredith reduced from 80% to 44% (4/9 tasks); Nate now handles 44% (4/9 tasks). **MAJOR UNRESOLVED ISSUES:** (1) **2 severely overdue tasks** (sendcutsend S2 NASA 5+ days, jawstec S0 5+ days) with fulfilled status but not closed, (2) Assignment concentration now split Meredith/Nate equally, (3) Form data truncation persists across all 9 tasks (jawstec S0 project shows "[300-3] 20", SendCutSend shows "General Sales (No Specific"), (4) Task lifecycle breakdown worsening—5/9 tasks with "Order Received" or "Order Shipped" status yet remain open, (5) Multiple tasks due within 48 hours with unclear fulfillment status.
- **Team members involved:**
  - **Meredith O'hara Needham** (4/9 open tasks = 44%, Project Owner) — Microhard, FTDI, Amazon, jawstec S2 NASA
  - **Nate Straus** (4/9 open tasks = 44%) — Mouser, jawstec S3, SendCutSend, DigiKey
  - **Requesters:** Alex (3), Joshua Fromm (4), Nate (1), Kareem (1)
- **Risk signals:**
  - 🔴 **SEVERELY OVERDUE TASKS (5+ days):**
    - **sendcutsend order for S2 NASA (#S439K456)** due Jul 9, 2026 — **5 days overdue as of Jul 14.** Status "Order Shipped" (fulfillment complete) but task remains open. **Assigned to Meredith.**
    - **jawstec for S0 parts (#69825)** due Jul 11, 2026 — **3+ days overdue as of Jul 14.** Status "Order Shipped" but task remains open. **Assigned to Meredith.**
  - 🔴 **IMMINENT DEADLINES (48 hrs or PAST DUE):**
    - **Amazon (Jul 16, 2 days)** — Status "Order Placed"; due date Jul 16.
    - **DigiKey (Jul 16, 2 days)** — Status "Order Received"; due date Jul 16.
    - **Microhard (Jul 18, 4 days)** — Status "Order Placed"; due date Jul 18.
    - **FTDI (Jul 18, 4 days)** — Status "Order Placed"; due date Jul 18 (placement was due Jul 15—3 days ago).
    - **Mouser (Jul 18, 4 days)** — Status "Order Received"; due date Jul 18.
    - **jawstec S3 (Jul 18, 4 days)** — Status "Order Received"; due date Jul 18 (placed Jun 29, 15+ days ago).
    - **SendCutSend (Jul 18, 4 days)** — Status "Order Received"; due date Jul 18 (placed Jul 1, 13+ days ago).
  - 🔴 **FORM DATA TRUNCATION PERSISTS (all 9 tasks affected):**
    - jawstec S0 project field shows "[300-3] 20" (truncated from "[300-3] 2026 IDIQ (Hurricane)")
    - sendcutsend S2 NASA project shows "[" (severely truncated; should be "[212-2] NASA S2 & Parts")
    - SendCutSend (Nate) project shows "General Sales (No Specific" (incomplete)
    - jawstec S3 project shows "General S" (truncated)
    - DigiKey project shows "[30" (severely truncated from "[300-3] 2026 IDIQ (Hurricane)")
    - Amazon project shows "[001-1] IRAD Gene" (truncated from "[001-1] IRAD General")
    - **CRITICAL RISK:** Orders may be billed to wrong projects if form data not manually corrected.
  - 🔴 **TASK LIFECYCLE BREAKDOWN WORSENING:** 5/9 tasks with "Order Received" or "Order Shipped" status (sendcutsend S2, jawstec S0, Mouser, jawstec S3, SendCutSend) remain open. Suggests complete failure of closure automation after fulfillment.
  - 🟠 **ASSIGNMENT SHIFT & CONCENTRATION:** Meredith dropped from 80% (4/5) to 44% (4/9); Nate rose from 20% (1/5) to 44% (4/9). Workload distribution now roughly equal but with critical overdue items still on Meredith's plate.
  - 🟠 **REQUESTER CONCENTRATION:** Joshua Fromm now owns 4/9 tasks (44%)—new dominant requester (was absent from prior snapshot). Alex still significant at 3/9 (33%). Suggests new project intake (likely NASA S2 & S3 work).
  - 🟠 **TAX EXEMPTION SPLIT:** 4/9 tasks are tax-exempt (44%); 5/9 non-exempt (56%).
  - 🟠 **VENDOR DIVERSITY:** Now includes jawstec (2 tasks), SendCutSend variants (2 tasks), plus FTDI, Mouser, Amazon, DigiKey, Microhard—suggests supply chain broadened.

## Key Deliverables & Milestones

### **SEVERELY OVERDUE & OPEN TASKS**

| Task | Due | Days Overdue | Status | Vendor | Assigned | Project | Requester | Tax Exempt? | Notes |
|------|-----|--------------|--------|--------|----------|---------|-----------|------------|-------|
| sendcutsend order for S2 NASA (#S439K456) | **Jul 9, 2026** | **5 days** | Order Shipped | SendCutSend | Meredith | [212-2] NASA S2 & Parts (form: "[" — **SEVERELY TRUNCATED**) | Joshua Fromm | YES | Fulfillment complete; task should close. **CRITICAL:** Closure automation failure. |
| jawstec for S0 parts (#69825) | **Jul 11, 2026** | **3 days** | Order Shipped | jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) (form: "[300-3] 20" — **TRUNCATED**) | Joshua Fromm | YES | Fulfillment complete; task should close. **CRITICAL:** Closure automation failure. |

### **IMMINENT DEADLINES (DUE WITHIN 4 DAYS)**

| Task | Due | Days | Status | Vendor | Assigned | Project | Requester | Tax Exempt? | Notes |
|------|-----|------|--------|--------|----------|---------|-----------|------------|-------|
| digikey - antennas for hurricane (#100363511) | **Jul 16, 2026** | **2** | Order Received | DigiKey | Nate | [300-3] 2026 IDIQ (Hurricane) (form: "[30" — **SEVERELY TRUNCATED**) | Kareem | NO |