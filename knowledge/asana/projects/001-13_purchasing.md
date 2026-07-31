# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **8 open tasks with immediate & near-term deadlines: Jul 30–31, 2026 (TODAY/TOMORROW), Aug 1.**
- **Status:** 🔴 **OPERATIONAL — CRITICAL DEADLINE CRUNCH.** Task count **decreased from 11 to 8** (prior snapshot included expired/closed tasks). Current distribution: **Order Placed 2/8 (25%), Order Shipped 3/8 (38%), Order Received 3/8 (38%).** **Shift from "Order Placed" dominance to balanced Shipped/Received suggests fulfillment acceleration.** Notable change: **jawstec overdue task and IRAD S3/S7 batch have been resolved/closed.** New entrant: **amazon for s2 nasa** ([212-2] NASA S2, Order Shipped, due Aug 1).
- **Team members involved:**
  - **Meredith O'hara Needham** (5/8 open tasks = 63%)
  - **Nate Straus** (3/8 = 38% — FTDI, digikey, springstore)
- **Requesters:** Joshua Fromm (6/8 = 75%), Nathaniel Straus (1/8 = 13%), Alex (1/8 = 13%)
- **Risk signals:**
  - 🔴 **IMMEDIATE DEADLINE CRUNCH:** 4 tasks due TODAY (Jul 31): amazon for SALES, Amazon Shop supplies, FTDI, digikey. 2 tasks due YESTERDAY (Jul 30): powerwerx, mouser for shop equipment — **both status "Order Shipped" but open; require closure verification.**
  - 🔴 **RECEIVED-BUT-OPEN PATTERN INTENSIFIES:** FTDI, digikey, springstore all "Order Received" but remain open. **3/8 tasks (38%) are stuck in fulfillment limbo.** Suggests missing closure workflow, pending invoice verification, or quality inspection holdups.
  - 🟠 **FORM FIELD TRUNCATION PERSISTS (UNCHANGED):** 4 of 8 tasks have incomplete project codes:
    - **Amazon Shop supplies:** "[001-" (5 chars, incomplete)
    - **digikey for S0 hurricane:** "[300-" (5 chars, incomplete)
    - **springstore for s0 idiq:** "[300-3" (6 chars, incomplete, missing closing bracket)
    - **FTDI notes section:** "Requi" (truncated from form capture, but task title & custom field are correct)
    - Risk: Billing misroute, project code ambiguity.
  - 🟠 **MULTI-PROJECT TASK UNRESOLVED:** powerwerx for multiple projects — status "Order Shipped" (placed Jul 24) but custom field explicitly states "[Project: MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION]" with **no breakdown in notes.** Due yesterday (Jul 30). **Order may have shipped without billing clarity.** Requires immediate project allocation & potential split invoice reconciliation.
  - 🟠 **HURRICANE BATCH PERSISTENT:** 2/8 tasks (25%) are [300-3] 2026 IDIQ (digikey, springstore), plus powerwerx "multiple projects" may include Hurricane work. Reduced from prior 45% but still significant.
  - 🟠 **NATE STRAUS EXPANSION & NEW REQUESTER (ALEX):** Nate now owns 3/8 tasks (38%, up from 27%). Alex appears as requester for FTDI — new or misspelled requester, unclear context.
  - 🟠 **PROJECT DIVERSITY INCREASING:** New project entered: [212-2] NASA S2 & Parts (amazon for s2 nasa). Suggests portfolio expansion beyond IRAD/Hurricane/Shop. Tax exempt = YES (consistent with government contracts).

## Key Deliverables & Milestones

### **OPEN TASKS — CURRENT BATCH (Jul 30–Aug 1 DEADLINES)**

| Task | Vendor | Assigned | Project (Form) | Requester | Status | Placement | Due | Tax Exempt? | Notes |
|------|--------|----------|----------------|-----------|--------|-----------|-----|------------|-------|
| **amazon for SALES** | Amazon | Meredith | General Sales (No Specific Project) | Joshua Fromm | Order Placed | Jul 29 | **Jul 31 🔴 TODAY** | YES | ✓ Project field complete. General sales (non-project-specific). Due today. |
| **Amazon Shop supplies** | Amazon | Meredith | Shop Supplies **(TRUNCATED)** | Nathaniel Straus | Order Shipped | Jul 29 | **Jul 31 🔴 TODAY** | NO | Project field truncated: "[001-" (5 chars). Status "Order Shipped" but task remains open. Due today. |
| **FTDI** | FTDI | Nate Straus | [001-16] IRAD Swiftstation ✓ | Alex | Order Received | Jul 15 | **Jul 31 🔴 TODAY** | NO | ✓ Project field complete in custom field. Notes section truncated: "Requi" (form capture artifact). Status "Order Received" but task open — fulfillment lag or pending invoice/QA. Due today. Nate owns; Alex (new requester?) requested. |
| **digikey for S0 hurricane** | Digikey | Nate Straus | [300-3] 2026 IDIQ (Hurricane) **(TRUNCATED)** | Joshua Fromm | Order Received | Jul 24 | **Jul 31 🔴 TODAY** | YES | Project field truncated: "[300-" (5 chars). Status "Order Received" but task open. Due today. Nate owns; placed Jul 24. |
| **powerwerx for multiple projects** | Powerwerx | Meredith | MULTIPLE PROJECT (BREAKDOWN MISSING) ⚠️ | Joshua Fromm | Order Shipped | Jul 24 | **Jul 30 🔴 YESTERDAY** | YES | 🔴 **CRITICAL: Status "Order Shipped" (placed Jul 24) but task due yesterday (Jul 30). Order may have already shipped WITHOUT project breakdown or billing allocation.** Custom field explicitly requests breakdown in description; notes are empty. **Requires immediate escalation: which projects does this order service? Invoice reconciliation needed.** Tax exempt = YES (suggests government/IRAD work, but unclear allocation). |
| **mouser for shop equipment** | Mouser | Meredith | Shop Supplies | Joshua Fromm | Order Shipped | Jul 28 | **Jul 30 🔴 YESTERDAY** | NO | Status "Order Shipped" but due yesterday. Task remains open. Verify closure. |
| **springstore for s0 idiq** | Springstore | Nate Straus | [300-3] 2026 IDIQ (Hurricane) **(TRUNCATED)** | Joshua Fromm | Order Received | Jul 24 | **Jul 30 🔴 YESTERDAY** | YES | Project field truncated: "[300-3" (6 chars, missing closing bracket). Status "Order Received" but task open (fulfillment lag). Nate owns. Due yesterday. |
| **amazon for s2 nasa** | Amazon | Meredith | [212-2] NASA S2 & Parts ✓ | Joshua Fromm | Order Shipped | Jul 30 | **Aug 1** | YES | **NEW PROJECT ENTRY:** [212-2] NASA S2 & Parts (government contract, tax exempt). ✓ Project field complete. Status "Order Shipped" (placed Jul 30). Due Aug 1. Suggests portfolio expansion. |

## Task Summary

**Total:** 8 open tasks, 0 completed (snapshot baseline).

**By Assignee:**
- **Meredith O'hara Needham:** 5/8 (63%) — amazon SALES, Amazon Shop, power