# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **19 open tasks with immediate & near-term deadlines: Jul 31, 2026 (TODAY) through Aug 2, 2026.**
- **Status:** 🔴 **OPERATIONAL — CRITICAL DEADLINE CRUNCH ESCALATING.** Task count **surged from 8 to 19 open tasks** (137% increase). **Major shift in composition:** Prior snapshot dominated by fulfillment-stage tasks (Shipped/Received); new batch is predominantly **Order Placed (13/19 = 68%)**, with **only 1 task due TODAY (Jul 31: amazon for SALES)**. **Influx suggests new procurement cycle for [001-4] IRAD S0 VTOL project (11/19 = 58% of all tasks).** Status distribution: **Order Placed 13/19 (68%), Order Shipped 4/19 (21%), Order Received 2/19 (11%).**
- **Team members involved:**
  - **Meredith O'hara Needham** (16/19 = 84%)
  - **Nate Straus** (3/19 = 16%)
- **Requesters:** Alex (11/19 = 58%), Joshua Fromm (8/19 = 42%)
- **Risk signals:**
  - 🔴 **MAJOR PROCUREMENT BATCH — [001-4] IRAD S0 VTOL DOMINANCE:** 11/19 tasks (58%) are for [001-4] IRAD S0 VTOL, all with due date **Aug 2, 2026**, all requested by **Alex**, all **Order Placed** status. This represents a significant project allocation spike. Suggests coordinated component sourcing for S0 VTOL build-out.
  - 🔴 **IMMEDIATE DEADLINE TODAY (JUL 31):** Only 3 tasks due Jul 31:
    - **amazon for SALES** (General Sales, Order Placed, due TODAY) — requires closure verification
    - **Amazon Shop supplies** (Shop Supplies, Order Shipped, due TODAY) — **project field still truncated "[001-"**
    - **FTDI** (#17721, Order Received, [001-16] IRAD Swiftstation) — order received but task open; fulfillment lag or pending QA/invoice
  - 🔴 **OVERDUE TASK PERSISTS:** **protolabs for s0 idiq** (#6794-871) — **due Jul 25 (6 DAYS OVERDUE)**, status "Order Shipped", project [300-3] 2026 IDIQ (Hurricane). **Requires immediate closure or escalation.**
  - 🟠 **RECEIVED-BUT-OPEN PATTERN CONTINUES:** 2/19 tasks (11%) are stuck in "Order Received" state:
    - mouser order for s0 hurricane — due Aug 2, received but open (fulfillment lag or pending invoice/QA)
    - FTDI — due TODAY (Jul 31), received but open
  - 🟠 **FORM FIELD TRUNCATION PERSISTS (WORSENING):** At least 2 tasks with incomplete/truncated project codes:
    - **Amazon Shop supplies:** "[001-" (5 chars, still incomplete; due TODAY)
    - **mouser order for s0 hurricane:** Project field **BLANK** in custom field (no project code assigned despite being [300-3] Hurricane work per task title). **Risk: billing misroute or project code loss.**
  - 🟠 **MEREDITH CONCENTRATION INTENSIFIES:** 16/19 tasks (84%) assigned to Meredith — up from 63%. Nate reduced to 3/19 (16%). **Workload imbalance and bottleneck risk if Meredith is unavailable.**
  - 🟠 **MULTI-PROJECT PORTFOLIO SUSTAINED:** [001-4] IRAD S0 VTOL dominates (58%), but 3 other active projects represented: [001-16] IRAD Swiftstation (1 task), [212-2] NASA S2 & Parts (2 tasks), [300-3] 2026 IDIQ/Hurricane (3 tasks), General Sales (1 task).
  - 🟠 **NEW REQUESTER PATTERN — ALEX SURGE:** Alex now requested 11/19 tasks (58%, all [001-4] VTOL), up from 1 prior task. Joshua Fromm holds 8/19. **Alex may be new PM or project lead for S0 VTOL; requires contact/relationship clarity.**

## Key Deliverables & Milestones

### **OPEN TASKS — CURRENT BATCH**

| Task | Vendor | Assigned | Project (Form) | Requester | Status | Due | Tax Exempt? | Notes |
|------|--------|----------|----------------|-----------|--------|-----|------------|-------|
| **amazon for SALES** | Amazon | Meredith | General Sales | Joshua Fromm | Order Placed | **Jul 31 🔴 TODAY** | YES | ✓ Project field complete. Due TODAY. |
| **Amazon Shop supplies** | Amazon | Meredith | Shop Supplies **(TRUNCATED)** | Nathaniel Straus | Order Shipped | **Jul 31 🔴 TODAY** | NO | Project field truncated: "[001-". Due TODAY. |
| **FTDI (#17721)** | FTDI | Nate Straus | [001-16] IRAD Swiftstation | Alex | Order Received | **Jul 31 🔴 TODAY** | NO | ✓ Project field complete in custom field. Status "Order Received" but task open — fulfillment lag or pending invoice/QA. Due TODAY. |
| **protolabs for s0 idiq (#6794-871)** | Protolabs | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Shipped | **Jul 25 🔴 OVERDUE (6 DAYS)** | YES | **CRITICAL: 6 days overdue. Status "Order Shipped" (placed Jul 23) but task remains open. Requires immediate closure or escalation.** |
| **amazon for s2 nasa** | Amazon | Meredith | [212-2] NASA S2 & Parts | Joshua Fromm | Order Shipped | Aug 1 | YES | ✓ Project field complete. Status "Order Shipped" (placed Jul 30). |
| **mouser order for s0 hurricane (#39954753)** | Mouser | Nate Straus | [300-3] 2026 IDIQ (Hurricane) **(PROJECT FIELD BLANK)** | Joshua Fromm | Order Received | Aug 2 | YES | 🟠 **Project field MISSING in custom field** (task title indicates Hurricane/S0 work, but no project code recorded). Order received but task open. Risk: billing misroute. |
| **ebay for s2 nasa** | eBay | Meredith | [212-2] NASA S2 & Parts | Joshua Fromm | Order Placed | Aug 2 | YES | ✓ Project field complete. Due Aug 2. |
| **Amazon (#65720628)** [S0 VTOL] | Amazon | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | ✓ Project field complete. S0 VTOL build-out batch. Due Aug 2. |
| **Digikey (#100742193)** [S0 VTOL] | Digikey | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | ✓ Project field complete. S0 VTOL build-out batch. Due Aug 2. |
| **Dronetag (882026/005977)** [S0 VTOL] | Dronetag |