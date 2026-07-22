# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **7 open tasks with deadlines Jul 22–23, 2026 (1–2 days out).** Prior overdue task (#69738, due Jul 8) has been removed/closed.
- **Status:** 🟠 **OPERATIONAL — CRITICAL ISSUES PERSIST.** Task count **up to 7** (from 4). New batch of 4 Swiftstation orders assigned to Meredith (all due Jul 23); prior jawstec sales overdue task removed. **Closure automation failure continues:** 2/4 legacy tasks remain in fulfillment states ("Order Received"). **Form data truncation unresolved on all 7 tasks.**
- **Team members involved:**
  - **Meredith O'hara Needham** (6/7 open tasks = 86%, Project Owner) — 4 Swiftstation orders (Sparkfun, Amazon, Digikey, JawsTec; all Jul 23), jawstec S0 parts (Jul 22)
  - **Nate Straus** (1/7 open tasks = 14%) — SendCutSend S2 NASA (Jul 22), jawstec S0 parts (Jul 22)
  - **Requesters:** Alex (4/7 tasks = Swiftstation batch), Joshua Fromm (3/7 tasks = Hurricane/NASA legacy)
- **Risk signals:**
  - 🔴 **IMMEDIATE DEADLINE RISK:** 4 Swiftstation tasks due Jul 23 (1 day away); all status "Order Placed" — placement deadline was Jul 21 (2 days past, now at fulfillment stage).
  - 🔴 **CLOSURE AUTOMATION FAILURE CONTINUES:** 2/7 tasks in fulfillment states ("Order Received") yet remain open (SendCutSend S2 NASA, jawstec S0 parts #69825). Prior snapshot showed identical pattern; issue unresolved.
  - 🟠 **FORM DATA TRUNCATION ON ALL 7 TASKS:** Digikey, JawsTec, jawstec S0 parts, SendCutSend all have truncated project codes ("Swiftsta", "20", missing brackets).
  - 🟠 **MASSIVE ASSIGNEE CONCENTRATION:** Meredith 86%; prior snapshot 50%. New Swiftstation workload concentrated on single owner.
  - 🟠 **DUAL REQUESTER MODEL:** Mix of Alex (new Swiftstation work) and Joshua Fromm (legacy tasks). Risk if either becomes unavailable.

## Key Deliverables & Milestones

### **OPEN TASKS**

| Task | Vendor | Assigned | Project | Requester | Status | Placement Date | Due Date | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|----------------|----------|------------|-------|
| Sparkfun (000419974) | Sparkfun | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | 🔴 Placement deadline Jul 21 now past; due Jul 23 (1 day). |
| Amazon | Amazon | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | 🔴 Placement deadline Jul 21 now past; due Jul 23 (1 day). |
| Digikey for GCS (#100525116) | Digikey | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | 🔴 Placement deadline Jul 21 now past; due Jul 23 (1 day). Project code truncated ("Swiftsta"). |
| JawsTec for GCS (#7004) | JawsTec | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | 🔴 Placement deadline Jul 21 now past; due Jul 23 (1 day). Project code truncated ("Swiftst"). |
| jawstec for s0 parts (#JT70002) | jawstec | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 20, 2026 | Jul 22, 2026 | YES | 2-day window (placement Jul 20, due Jul 22). Project code truncated ("2"). |
| sendcutsend order for s2 nasa (S439K456) | SendCutSend | Nate | [212-2] NASA S2 & Parts | Joshua Fromm | Order Received | Jul 7, 2026 | Jul 22, 2026 | YES | 🔴 Fulfillment complete (Order Received); should be closed. Persists from prior snapshot (17+ days in fulfillment state). |
| jawstec for s0 parts (#69825) | jawstec | Nate | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Received | Jul 9, 2026 | Jul 22, 2026 | YES | 🔴 Fulfillment complete (Order Received); should be closed. Persists from prior snapshot (13+ days in fulfillment state). Project code truncated ("20"). |

## Task Summary
- **Total open tasks:** 7 (up from 4 in prior snapshot)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 6/7 (86%, up from 50%) — 4 Swiftstation orders (Sparkfun, Amazon, Digikey, JawsTec; all new), jawstec S0 parts
  - **Nate Straus:** 1/7 (14%, down from 50%) — SendCutSend S2 NASA, jawstec S0 parts
- **Completion rates:** 0/7 tasks completed this snapshot; prior overdue jawstec sales task (#69738) removed (likely closed externally or merged).
- **Notable patterns:**
  - **NEW SWIFTSTATION BATCH:** 4 tasks all due Jul 23, assigned to Meredith, requested by Alex. All status "Order Placed" with Jul 21 placement deadline now past.
  - **jawstec S0 parts appears twice** (#JT70002 assigned to Meredith, #69825 assigned to Nate) — workflow split persists.
  - **2/7 tasks in fulfillment states ("Order Received") persist open:** SendCutSend S2 NASA (17+ days), jawstec S0 parts #69825 (13+ days). Closure automation failure unresolved.
  - **Form data truncation on all 7 tasks:** Swiftstation project codes truncated; jawstec S0 codes show incomplete ("2", "20").
  - **5/7 tasks are tax-exempt** (legacy Hurricane/NASA work); 2/7 non-exempt (Swiftstation).
  - **Requester split:** Alex (Swiftstation), Joshua Fromm (legacy). 100% concentration risk on each requester within their respective workstreams.

## Recent Activity
- **Major change: Swiftstation batch intake (4 new tasks):**
  - 4 new orders (Sparkfun, Amazon, Digikey, JawsTec) assigned to Meredith, requested by Alex for [001-16] IRAD Swiftstation project.
  - All due Jul 23, 2026 (1 day out). Placement deadline was Jul 21 (now past).
  - All status "Order Placed" — orders appear already submitted; tasks now in tracking phase.