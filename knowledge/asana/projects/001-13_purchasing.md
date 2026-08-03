# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **13 open tasks with imminent deadline: Aug 2, 2026 (within 24 hours).**
- **Status:** 🔴 **OPERATIONAL — CRITICAL DEADLINE CRUNCH.** Task count **decreased from 14 to 13 open tasks** (7% reduction). **Composition remains dominated by [001-4] IRAD S0 VTOL:** 11/13 tasks (85%) are S0 VTOL components, all due Aug 2. **Status distribution: Order Placed 11/13 (85%), Order Shipped 2/13 (15%), Order Received 1/13 (8%).**
  - **CHANGE FROM PRIOR SNAPSHOT:** Task **"amazon for s2 nasa"** (previously Order Shipped, due Aug 1) **has been removed/closed.** Only "ebay for s2 nasa" remains for NASA S2. **Unknown if closure was legitimate fulfillment or manual cleanup.**
- **Team members involved:**
  - **Meredith O'hara Needham** (12/13 = 92%)
  - **Nate Straus** (1/13 = 8%)
- **Requesters:** Alex (10/13 = 77%), Joshua Fromm (3/13 = 23%)
- **Risk signals:**
  - 🔴 **EXTREME MEREDITH CONCENTRATION PERSISTS:** 12/13 tasks (92%) assigned to Meredith — **down slightly from 93%, but still critical bottleneck.** Only 1 task (mouser for S0 hurricane) assigned to Nate. **Meredith availability is single point of failure for Aug 2 delivery.**
  - 🔴 **S0 VTOL BUILD-OUT BATCH — IMMINENT DEADLINE (AUG 2 — NOW WITHIN 24 HRS):** 11/13 tasks (85%) for [001-4] IRAD S0 VTOL, all due Aug 2, all requested by Alex. Composition:
    - 9 Order Placed: Amazon, Digikey, Dronetag, APC, Hitec, Protolabs, Sendcutsend, Jawstec (Pt 1 & 2)
    - 2 Order Shipped: Servocity, IRLock
  - **⏰ DELIVERY COUNTDOWN:** With Aug 2 due date **24 hours away**, all 11 S0 VTOL tasks in "Order Placed" or "Order Shipped" state must be received/confirmed by end of Aug 2 or project will be delayed.
  - 🟠 **REMOVED TASK — "AMAZON FOR S2 NASA":** Previous snapshot listed this as Order Shipped, due Aug 1. **Not present in current data.** Either task was completed and closed, or removed from list. **Verify closure documentation; if legitimately received, should move to completed tracking.**
  - 🟠 **BLANK PROJECT FIELD — MOUSER ORDER PERSISTS:** **mouser order for s0 hurricane (#39954753)** — project field **completely blank** in custom field despite task title clearly indicating [300-3] 2026 IDIQ (Hurricane). **Critical risk: invoice/billing misroute. This task now past 9 days from original "Jul 24" placement date; status is "Order Received" but project code still blank.** **Immediate correction required before invoice processing.**
  - 🟠 **PROJECT FIELD TRUNCATION PERSISTS:** 3 tasks still have truncated project fields in custom data:
    - Sendcutsend: "[001-4] IRAD S0 VT" (cut off)
    - Jawstec Pt1: "[001-4] IRAD S0 V" (cut off)
    - Jawstec Pt2: "[001-4] IRAD S0 VT" (cut off)
    - **Note:** Raw task data shows full "[001-4] IRAD S0 VTOL" in field headers, but custom form capture appears truncated. Monitor for billing issues.
  - 🟠 **RECEIVED-BUT-OPEN PATTERN:** 1/13 tasks (8%) stuck in "Order Received" state (mouser). **Over 9 days old (placed Jul 24, now Aug 2). Fulfillment lag, missing invoice, or pending QA closure.** **Likely blocking billing workflow.**
  - 🟠 **MULTI-PROJECT PORTFOLIO IMBALANCE:** [001-4] IRAD S0 VTOL overwhelmingly dominates (85%). Only 2 other projects: [212-2] NASA S2 & Parts (1 task: ebay), [300-3] 2026 IDIQ/Hurricane (1 task: mouser). **Confirms S0 VTOL is primary procurement focus.**

## Key Deliverables & Milestones

### **OPEN TASKS — CURRENT BATCH (13 TOTAL, DUE AUG 2, 2026)**

| Task | Vendor | Assigned | Project | Requester | Status | Notes |
|------|--------|----------|---------|-----------|--------|-------|
| **Amazon** | Amazon | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. |
| **Digikey (#100742193)** | Digikey | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. |
| **Dronetag (882026/005977)** | Dronetag | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. |
| **APC (#55956)** | APC | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. |
| **Hitec (5791)** | Hitec | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. |
| **protolabs (#5184-903)** | Protolabs | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. |
| **Sendcutsend S0 VTOL (S242P458)** | Sendcutsend | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. Custom field truncated ("[001-4] IRAD S0 VT"). |
| **Jawstec S0 VTOL Pt1 (#70260)** | Jawstec | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. Custom field truncated ("[001-4] IRAD S0 V"). |
| **Jawstec S0 VTOL Pt2 (#70261)** | Jawstec | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Placed | S0 VTOL batch. Placed Jul 31. Custom field truncated ("[001-4] IRAD S0 VT"). |
| **servocity (#300046306)** | Servocity | Meredith | [001-4] IRAD S0 VTOL | Alex | Order Shipped | S0 VTOL batch. Placed Jul 31. |
| **IRLock (#28043)** | IRLock | Meredith | [001-4] IRAD