# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **10 open tasks with deadlines Jul 16–24, 2026.** 🔴 **CRITICAL:** 6 tasks due Jul 22–23 (today or tomorrow); 1 task already overdue (Amazon Shop supplies, due Jul 16).
- **Status:** 🔴 **OPERATIONAL — CRITICAL DEADLINE & CLOSURE ISSUES.** Task count **up to 10** (from 7). **NEW:** 1 S3 power board task (due Jul 22, requester Sam); prior 4-task Swiftstation batch now shows **2 status changes** (Sparkfun remains "Order Placed"; Amazon & Digikey now "Order Shipped"). **Closure automation failure persists:** 3/10 tasks in "Order Received" fulfillment state remain open (SendCutSend S2 NASA, jawstec S0 #69825, jawstec sales #69738). **Form data truncation unresolved on all 10 tasks.** **1 task OVERDUE:** Amazon Shop supplies (due Jul 16, placement Jul 14; status "Order Shipped" — should be closed).
- **Team members involved:**
  - **Meredith O'hara Needham** (7/10 open tasks = 70%, Project Owner) — 4 Swiftstation orders (Sparkfun, Amazon, Digikey, JawsTec; Jul 22–23), jawstec S0 parts (Jul 22), S3 power board (Jul 22)
  - **Nate Straus** (3/10 open tasks = 30%) — SendCutSend S2 NASA (Jul 22), jawstec S0 #69825 (Jul 22), jawstec sales #69738 (Jul 24)
  - **Requesters:** Alex (4/10 = Swiftstation), Joshua Fromm (5/10 = legacy Hurricane/NASA/sales), Sam (1/10 = S3)
- **Risk signals:**
  - 🔴 **OVERDUE TASK:** Amazon Shop supplies (Meredith, due Jul 16; status "Order Shipped"). Placement was Jul 14 — fulfillment complete 6+ days ago; should be closed.
  - 🔴 **IMMINENT DEADLINE CRUNCH:** 6/10 tasks due Jul 22–23 (1–2 days); 4 are Swiftstation (Alex), 1 S3 power board (Sam), 1 jawstec S0 (Joshua). Meredith carries 5/6 of these.
  - 🔴 **CLOSURE AUTOMATION FAILURE PERSISTS:** 3/10 tasks in "Order Received" state remain open:
    - SendCutSend S2 NASA (20+ days in fulfillment, due Jul 22)
    - jawstec S0 #69825 (14+ days in fulfillment, due Jul 22)
    - jawstec sales #69738 (18+ days in fulfillment, due Jul 24) — new appearance with no project breakdown despite "MULTIPLE PROJECT" tag
  - 🟠 **STATUS INCONSISTENCIES ON SWIFTSTATION BATCH:**
    - Sparkfun: "Order Placed" (on track)
    - Amazon & Digikey: "Order Shipped" (accelerated fulfillment?) — now shows 2 status updates within batch
    - JawsTec: "Order Placed" (matches Sparkfun)
    - **Risk:** Mix of statuses suggests asynchronous vendor fulfillment; shipments may arrive out-of-sequence.
  - 🟠 **FORM DATA TRUNCATION ON ALL 10 TASKS:** Project codes truncated on S3 ("[001"), JawsTec ("[001-16] IRAD Swiftst"), jawstec S0 ("[300-3] 2"), Amazon Shop ("[001-1] IRAD Gene"), SendCutSend ("[").
  - 🟠 **WORKLOAD CONCENTRATION:** Meredith 70% (up from 86% in prior snapshot due to Nate reassignments); 5/6 imminent deadline tasks assigned to her.
  - 🟠 **3-REQUESTER MODEL WITH CONCENTRATION RISK:** Alex (Swiftstation, 4 tasks), Joshua Fromm (legacy, 5 tasks), Sam (new S3, 1 task). Loss of Alex or Joshua impacts 40% or 50% of workload respectively.

## Key Deliverables & Milestones

### **OPEN TASKS (sorted by due date)**

| Task | Vendor | Assigned | Project | Requester | Status | Placement Date | Due Date | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|----------------|----------|------------|-------|
| **Amazon Shop supplies** | Amazon | Meredith | [001-1] IRAD General | Nate | Order Shipped | Jul 14, 2026 | **Jul 16, 2026** | NO | 🔴 **OVERDUE (6+ days past due).** Status "Order Shipped" — fulfillment complete. Should be closed. Project code truncated ("[001-1] IRAD Gene"). |
| **S3 extra parts for power board fix** | (S3) | Meredith | [001-7] IRAD S3 | Sam | (no status) | Jul 22, 2026 | **Jul 22, 2026** | NO | **NEW TASK.** Due today (Jul 22). Placement deadline same as due date. Requester: Sam (new voice). Project code truncated ("[001"). |
| **jawstec for s0 parts (#JT70002)** | jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 20, 2026 | **Jul 22, 2026** | YES | 2-day window (placement Jul 20, due Jul 22). Project code truncated ("[300-3] 2"). |
| **sendcutsend order for s2 nasa (S439K456)** | SendCutSend | Nate | [212-2] NASA S2 & Parts | Joshua Fromm | Order Received | Jul 7, 2026 | **Jul 22, 2026** | YES | 🔴 Fulfillment complete (Order Received, 20+ days in state); should be closed. Persists from prior snapshots. Project code truncated ("["). |
| **jawstec for s0 parts (#69825)** | jawstec | Nate | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Received | Jul 9, 2026 | **Jul 22, 2026** | YES | 🔴 Fulfillment complete (Order Received, 14+ days in state); should be closed. Persists from prior snapshots. Project code truncated ("[300-3] 20"). |
| **Sparkfun (000419974)** | Sparkfun | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | Placement deadline Jul 21 now past; due Jul 23 (1 day). Swiftstation batch. |
| **Amazon** | Amazon | Meredith | [001-16] IRAD Swiftstation | Alex | Order Shipped | Jul 21, 2026 | **Jul 23, 2026** | NO | 🟠 Status changed to "Order Shipped" (accelerated vs. Sparkfun/JawsTec "Order Placed"). Due Jul 23 (1 day). Swiftstation batch. |
| **Digikey for GCS (#100525116)** | Digikey | Meredith | [001-16] IRAD Swiftstation | Alex | Order