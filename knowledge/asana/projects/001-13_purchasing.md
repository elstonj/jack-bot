# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **7 open tasks with deadlines Jul 23–25, 2026.** 🟠 **ELEVATED:** All 7 tasks due within 3 days (Jul 23–25); 4 Swiftstation tasks now consolidated to single due date (Jul 25); 2 tasks already in "Order Received" fulfillment state.
- **Status:** 🟠 **OPERATIONAL — DEADLINE CRUNCH & CLOSURE PATTERN.** Task count **down to 7** (from 10 in prior snapshot). **MAJOR SHIFT:** Amazon Shop overdue task **closed/removed**; SendCutSend S2 NASA & jawstec S0 #69825 **closed/removed**; jawstec sales #69738 **now due Jul 24** (1-day extension from Jul 23?). **NEW:** protolabs S0 IDIQ task added (due Jul 25). **Status pattern:** 2 tasks "Order Received" (Sparkfun, Amazon, Digikey — suggests bulk fulfillment arrived); 4 tasks "Order Placed" (protolabs, JawsTec GCS, S3 power board, jawstec sales). **Closure automation continues to fail:** 3 "Order Received" tasks remain open (likely awaiting manual closure or downstream action). **Form data truncation persists** on S3 ("[001"), jawstec sales (project field empty). **Reassignment pattern:** Nate now owns 3/7 open tasks (Sparkfun, Amazon, Digikey — all Swiftstation batch, due Jul 25); Meredith owns 4/7.
- **Team members involved:**
  - **Meredith O'hara Needham** (4/7 open tasks = 57%, Project Owner) — protolabs S0 (Jul 25), JawsTec GCS (Jul 23), S3 power board (Jul 25)
  - **Nate Straus** (3/7 open tasks = 43%) — Sparkfun (Jul 25), Amazon (Jul 25), Digikey (Jul 25) **[all Swiftstation batch, newly reassigned]**
  - **Requesters:** Alex (4/7 = Swiftstation), Joshua Fromm (2/7 = protolabs S0 + jawstec sales), Sam (1/7 = S3)
- **Risk signals:**
  - 🟠 **IMMINENT DEADLINE CRUNCH:** All 7 tasks due Jul 23–25 (0–3 days from Jul 22). 4 are Swiftstation (Alex, due Jul 25 via Nate); 1 is JawsTec GCS (Alex, due Jul 23 via Meredith — **1 day away**); protolabs & S3 (both due Jul 25); jawstec sales (due Jul 24, 2-day window).
  - 🟠 **CLOSURE AUTOMATION FAILURE PATTERN:** 3 tasks in "Order Received" state remain open (Sparkfun, Amazon, Digikey — all Swiftstation batch, placed Jul 21, due Jul 25). These should auto-close on receipt but persist, suggesting downstream fulfillment dependency or manual closure requirement.
  - 🟠 **REASSIGNMENT TO NATE (SWIFTSTATION BATCH):** Sparkfun, Amazon, Digikey now assigned to Nate (from Meredith in prior snapshot). This suggests Meredith may be managing placement decisions (due dates), while Nate handles receipt/fulfillment closure. **Risk:** If Nate is unavailable, all 3 "Order Received" items stall.
  - 🟠 **PLACEMENT DEADLINE ALREADY PAST:** JawsTec GCS placed Jul 21, due Jul 23 (2-day fulfillment window — tight). Sparkfun, Amazon, Digikey all placed Jul 21, due Jul 25 (4-day window — standard).
  - 🟠 **FORM DATA TRUNCATION UNRESOLVED:** S3 power board project code still "[001" (missing suffix); jawstec sales project field entirely **empty** ("MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" — flagged in task title, no breakdown provided).
  - 🟠 **PRIOR CLOSURES UNEXPLAINED:** Amazon Shop supplies (overdue), SendCutSend S2 NASA (20+ days in "Order Received"), jawstec S0 #69825 (14+ days in "Order Received") all **removed from task list**. No notes on closure reason. Possible bulk archival or external fulfillment.

## Key Deliverables & Milestones

### **OPEN TASKS (sorted by due date)**

| Task | Vendor | Assigned | Project | Requester | Status | Placement Date | Due Date | Tax Exempt? | Notes |
|------|--------|----------|---------|-----------|--------|----------------|----------|------------|-------|
| **JawsTec for GCS (#7004)** | JawsTec | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | 🟠 **2-day fulfillment window.** Due in 1 day (Jul 23). Swiftstation batch. Tight deadline. |
| **jawstec for sales - see details (#69738)** | jawstec | Nate | MULTIPLE PROJECT (unspecified) | Joshua Fromm | Order Received | Jul 6, 2026 | **Jul 24, 2026** | YES | 🟠 **Fulfillment complete (Order Received, 16+ days in state);** should be closed. **Project field empty** — task title flags "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" but no breakdown provided. High ambiguity. |
| **protolabs for s0 idiq (6794-871)** | protolabs | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 23, 2026 | **Jul 25, 2026** | YES | **NEW TASK.** Placement deadline is Jul 23 (today or tomorrow, depending on timezone). Due Jul 25 (2-day window). |
| **JawsTec for GCS (#7004)** | JawsTec | Meredith | [001-16] IRAD Swiftstation | Alex | Order Placed | Jul 21, 2026 | **Jul 23, 2026** | NO | See row 1 above. |
| **S3 extra parts for power board fix (#100576268)** | S3 | Meredith | [001-7] IRAD S3 | Sam | Order Shipped | Jul 22, 2026 | **Jul 25, 2026** | NO | 🟠 Status already "Order Shipped" (fulfillment in transit or complete). Due Jul 25. Project code truncated ("[001"). |
| **Sparkfun (000419974)** | Sparkfun | Nate | [001-16] IRAD Swiftstation | Alex | Order Received | Jul 21, 2026 | **Jul 25, 2026** | NO | 🟠 **Fulfillment complete (Order Received).** Should be closed but remains open. 4-day fulfillment window (Jul 21–25). Swiftstation batch — **reassigned to Nate**. |
| **Amazon** | Amazon | Nate | [001-16] IRAD Swiftstation | Alex | Order Received | Jul 21, 2026 | **Jul 25, 2026** | NO | 🟠 **Fulfillment complete (Order Received).** Should be closed but remains open. 4-day fulfillment window (Jul 21–25). Swiftstation batch — **reassigned to Nate**. |
| **Digikey for G