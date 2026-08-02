# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **14 open tasks with immediate & near-term deadlines: Aug 1–2, 2026 (within 24–48 hours).**
- **Status:** 🔴 **OPERATIONAL — CRITICAL DEADLINE CRUNCH.** Task count **decreased from 19 to 14 open tasks** (26% reduction). **Composition shift toward [001-4] IRAD S0 VTOL dominance:** 11/14 tasks (79%) are S0 VTOL components, all due Aug 2. **Status distribution: Order Placed 12/14 (86%), Order Shipped 2/14 (14%), Order Received 1/14 (7%).**
- **Team members involved:**
  - **Meredith O'hara Needham** (13/14 = 93%)
  - **Nate Straus** (1/14 = 7%)
- **Requesters:** Alex (11/14 = 79%), Joshua Fromm (3/14 = 21%)
- **Risk signals:**
  - 🔴 **EXTREME MEREDITH CONCENTRATION:** 13/14 tasks (93%) assigned to Meredith — **up from 84%**. Only 1 task (mouser) assigned to Nate. **Critical bottleneck and availability risk.**
  - 🔴 **S0 VTOL BUILD-OUT BATCH — IMMINENT DEADLINE (AUG 2):** 11/14 tasks (79%) for [001-4] IRAD S0 VTOL, all due Aug 2, all requested by Alex, all "Order Placed" or "Order Shipped". **Represents major component procurement cycle.** Includes:
    - 10 Order Placed: Amazon, Digikey, Dronetag, APC, Hitec, Protolabs, Sendcutsend, Jawstec (Pt 1 & 2), servocity
    - 1 Order Shipped: IRLock
  - 🟠 **OVERDUE TASK STATUS UNCLEAR:** Prior snapshot flagged **protolabs for s0 idiq (#6794-871)** as **6 days overdue (due Jul 25)**. **This task is NOT in current open list.** Either task was closed/completed, or data refresh cleared historical overdue. **Verify closure or escalation status.**
  - 🟠 **PROJECT FIELD TRUNCATION PERSISTS:** **ebay for s2 nasa** project field truncated in raw data ("Select project to bill purchase: [212-2] NAS" — incomplete). **Risk: billing misroute if not corrected.**
  - 🟠 **BLANK PROJECT FIELD — MOUSER ORDER:** **mouser order for s0 hurricane (#39954753)** — project field **completely blank** in custom field ("Select project to bill purchase: [blank]"). **Task title indicates [300-3] 2026 IDIQ (Hurricane) work, but project code not recorded in form.** **Critical risk: invoice/billing misroute. Immediate correction required.**
  - 🟠 **RECEIVED-BUT-OPEN PATTERN:** 1/14 tasks (7%) stuck in "Order Received" state (mouser). **Fulfillment lag or pending invoice/QA closure.**
  - 🟠 **MULTI-PROJECT PORTFOLIO IMBALANCE:** [001-4] IRAD S0 VTOL overwhelmingly dominates (79%). Only 3 other projects represented: [212-2] NASA S2 & Parts (2 tasks), [300-3] 2026 IDIQ/Hurricane (1 task). **Suggests S0 VTOL is primary focus; other projects quieter or stalled.**

## Key Deliverables & Milestones

### **OPEN TASKS — CURRENT BATCH (14 TOTAL)**

| Task | Vendor | Assigned | Project | Requester | Status | Due | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|-----|------------|-------|
| **amazon for s2 nasa** | Amazon | Meredith | [212-2] NASA S2 & Parts **(TRUNCATED)** | Joshua Fromm | Order Shipped | Aug 1 🟠 | YES | Project field truncated in custom field. Placed Jul 30. |
| **Amazon** | Amazon | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **Digikey (#100742193)** | Digikey | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **Dronetag (882026/005977)** | Dronetag | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **APC (#55956)** | APC | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **Hitec (5791)** | Hitec | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **protolabs (#5184-903)** | Protolabs | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **Sendcutsend S0 VTOL (S242P458)** | Sendcutsend | Meredith | [001-4] IRAD S0 VTOL **(TRUNCATED)** | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Project field truncated ("[001-4] IRAD S0 VT"). Placed Jul 31. |
| **Jawstec S0 VTOL Pt1 (#70260)** | Jawstec | Meredith | [001-4] IRAD S0 VTOL **(TRUNCATED)** | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Project field truncated ("[001-4] IRAD S0 V"). Placed Jul 31. |
| **Jawstec S0 VTOL Pt2 (#70261)** | Jawstec | Meredith | [001-4] IRAD S0 VTOL **(TRUNCATED)** | Alex | Order Placed | Aug 2 | YES | S0 VTOL build-out batch. Project field truncated ("[001-4] IRAD S0 VT"). Placed Jul 31. |
| **ebay for s2 nasa** | eBay | Meredith | [212-2] NASA S2 & Parts | Joshua Fromm | Order Placed | Aug 2 | YES | Placed Jul 31. |
| **servocity (#300046306)** | Servocity | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | Aug 2 | YES | S0 VTOL build-out batch. Placed Jul 31. |
| **IRLock (#28043)** | IRLock | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | Aug 2 | YES | S0 