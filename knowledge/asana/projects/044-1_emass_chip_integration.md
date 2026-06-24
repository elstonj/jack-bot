# [044-1] EMASS Chip Integration

## Overview
- **Client/Customer**: EMASS (Commercial customer)
- **Dollar Value**: $90,000 total funding to Black Swift Technologies
  - **Revised billing structure** (June 2026): Split final milestone into **Milestone 4a: Engineering support + flights ($25k)** and **Milestone 4b: Final reports ($10k)**; transitioning to **per-flight-day billing** going forward
  - **Payment friction**: EMASS declined to pay final milestone ($35k) due to incomplete final report; restructured agreement reflects customer pushback
- **Timeline**: Original November 10, 2025 to January 31, 2026; extended through May 2026 for validation and reporting. **No firm end date currently set.**
- **Status**: **🔴 INDEFINITELY POSTPONED — External blocker on EMASS controller delivery.** Per Daniel Prendergast (May 13–14, 2026): "EMASS Validation Flight #2 is postponed indefinitely until they get us a functioning controller." Per Jack Elston (May 12, 2026): "de-prioritize it, but we don't want to drag this out more than a month." **All remaining validation flights and final reporting blocked.**
- **Team Members**: Dan Prendergast (Owner/Lead), Jack Elston, Maciej Stachura, Nate Straus, Ethan Domagala, Meredith O'hara Needham; Alex and Sam (magnetometer integration critical engineering, per Maciej Stachura June 8, 2026)
- **Risk Signals**: 
  - **🔴 CRITICAL: Project indefinitely postponed on external EMASS controller delivery** — Validation Flights #2 and #3 cannot proceed until EMASS delivers functioning controller binary. This is outside BST control.
  - **🔴 CRITICAL: Customer payment friction** — EMASS refused to pay final milestone ($35k) because Validation Flights #2–#3 and final report remain incomplete. New per-flight-day billing model signals reduced confidence in fixed-price delivery.
  - **⚠️ Escalation boundary approaching** (set ~June 12, 2026): Jack Elston (May 12, 2026) imposed informal 1-month hold limit before escalation/re-evaluation.
  - **⚠️ Priority downrank**: Maciej Stachura (April 30, 2026) ranked EMASS as Priority #3 for closure (after S3 IRAD and S0-VTOL), indicating BST focus is shifting elsewhere while awaiting customer action.
  - **⚠️ Navy meeting no-show** (June 8, 2026): Scheduled Navy meeting at 9:30 AM did not occur per Maciej Stachura — possible coordination issue or schedule slippage.

## Key Deliverables & Milestones
- **Phase 1: Design & Alignment** (Due: Jan 28, 2026) - ✅ Completed
- **Phase 1b: Interface Design Freeze** (Due: Feb 6, 2026) - ✅ Completed
- **Phase 2: Integration & Firmware** (Due: Feb 13, 2026) - ✅ Completed
- **Phase 4: Validation & Reporting** (Due: Mar 11, 2026) - ✅ Completed
- **Milestone 4a: Engineering support + flights** ($25k) — **IN PROGRESS / BLOCKED**
  - Validation Flight #1 (April 27, 2026) — ✅ **Completed April 25, 2026** (2 days early)
  - Validation Flight #2 — **🔴 INDEFINITELY POSTPONED** *(awaiting functioning controller binary from EMASS)*
  - Validation Flight #3 — **🔴 INDEFINITELY POSTPONED** *(awaiting functioning controller binary from EMASS)*
- **Milestone 4b: Final reports** ($10k) — **🔴 BLOCKED** *(cannot start until validation flights #2–#3 complete)*

## Task Summary
- **Total Open Tasks**: 5 tasks; **0 completed in this reporting cycle**
  - Validation Flight #2 (Dan Prendergast, no due date) — **INDEFINITELY POSTPONED on EMASS controller delivery**
  - Validation Flight #3 (Dan Prendergast, no due date) — **INDEFINITELY POSTPONED on EMASS controller delivery**
  - Final Report (Dan Prendergast, no due date) — **BLOCKED** (cannot complete until validation flights complete)
  - Data analysis × 2 (Maciej Stachura, no due dates) — **BLOCKED** (cannot analyze until validation flights complete)
- **Tasks by Assignee**:
  - **Dan Prendergast**: 3 open tasks (2 validation flights, 1 final report) — **ALL INDEFINITELY POSTPONED on external EMASS controller delivery**
  - **Maciej Stachura**: 2 open tasks (data analysis × 2) — **BLOCKED** (awaiting validation flight completion)
  - **Jack Elston & Nate Straus**: Actively coordinated field execution in April–May but not formally assigned in Asana
  - **Meredith O'hara Needham**: Invoicing/admin (submitted initial invoice March 24, 2026)
  - **Alex & Sam**: Critical magnetometer integration engineering tasks (per Maciej Stachura, June 8, 2026)

## Recent Activity

**June 8, 2026 (Maciej Stachura — Team Correction)**:
- **Navy meeting at 9:30 AM did not occur** — flagged as no-show or scheduling issue.
- **Magnetometer integration assigned to Alex and Sam** — critical engineering tasks; external team members or sub-team support structure.

**June 2026 (Daniel Prendergast — Authoritative Billing Restructure)**:
- **BILLING MODEL REVISED due to customer payment friction**
- Quote: "they did not want to pay for our last milestone on the original agreement ($35k) since we never completed a final report. So I told them we're going to split that milestone into 'Milestone 4a: Engineering support + flights' for $25k, and 'Milestone 4b: final reports' for $10k. Moving forward we're just going to charge them on a per-flight-day basis."
- **Interpretation**: EMASS pushed back on fixed-price model; BST accepted reduced Milestone 4 payment ($35k → $25k upfront) and transitioned to time-and-materials (per-flight-day) billing to reduce customer friction and maintain relationship. Signals customer dissatisfaction with incomplete deliverables.

**May 14, 2026 (Daniel Prendergast — Authoritative)**:
- **PROJECT INDEFINITELY POSTPONED ON EMASS CONTROLLER DELIVERY**
- Quote: "CU IRISS training is complete. EMASS Validation Flight #2 is postponed indefinitely until they get us a functioning controller."
- Both Validation Flights #2 and #3 cannot proceed.

**May 12, 2026 (Jack Elston — Authoritative Escalation Boundary)**:
- **De-prioritize EMASS; impose informal 1-month hold boundary**
- Quote: "emass is likely delayed, we're waiting on them to get a working system to test, so de-prioritize it, but we don't want to drag this out more than a month"
- **Interpretation**: Accept external delay is expected; enforce escalation/re-evaluation by ~June 12, 2026 if situation unresolved.

**May 7–8, 2026 (Daniel Prendergast)**:
- **Financial flag**: "did EMASS ever pay the second invoice?" — Indicates invoice/payment gap or customer relationship friction alongside technical delays.

**May 4, 2026 (Daniel Prendergast)**:
- Confirmed external blocker: "We cannot perform those flights until they send us a new controller binary in the emass-bst slack channel."
- Shifted own priority to 53rd Weather Squadron and SOCOM visit slides.

**April 30, 2026 (Maciej Stachura