# [005-1] BARBADOS VTOL S0 and Training

## Overview
- **Client/Customer:** Barbados Meteorological Services
- **Contact:** Sabu Best (1-246-535-0016, Sabu.Best@barbados.gov.bb)
- **Dollar Value:** $22,337 (fully funded to BST)
- **Timeline:** 
  - Original project due: 2024-10-01 (**PASSED**)
  - S0 VTOL handoff due: May 1, 2026
  - Handoff meeting: June 23, 2026
  - Training window: May 5, 2025 week (Sabu Best availability)
  - Travel/training delivery: July 1-4, 2026
- **Status:** **CRITICAL DELAY** — Original due date (Oct 2024) passed. As of April 2026, **S0-VTOL has an active crash bug under investigation** (Maciej Stachura, 2026-04-20); restart and flight tests planned for week of April 20. S0 VTOL delivery blocker threatens May 1 handoff date. Operator training unassigned with no due date. Major deliverables remain open.
  - **Per Maciej Stachura (2026-04-24):** S0-VTOL is a top priority project with two deliveries (ERAU and Barbados). One bench test task is overdue; instrumented bench test needs completion by mid-week following 2026-04-24.
- **Team Members:** Alex Lomis (owner/delivery lead), Jack Elston (handoff/training lead), Maciej Stachura (technical troubleshooting), Daniel Prendergast (support)
- **Risk Signals:** 
  - **S0 VTOL crash bug—active repair in progress** (week of 2026-04-20); flight test restart on critical path
  - May 1, 2026 handoff due date at risk if crash bug repair extends
  - **Overdue bench test task** and instrumented bench test due mid-week after 2026-04-24 (Maciej Stachura, 2026-04-24)
  - Ground station asset scarcity flagged by Jack Elston (2026-04-20): "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits" — signal that hardware may be reprioritized if timeline slips further
  - Operator training unassigned and without due date despite July 1-4, 2026 travel commitment
  - NDAA compliance pending; S0 VTOL, S0 AD, and E2 "can be" compliant but not "fully" compliant yet (Alex Lomis, 2026-04-17)
  - 902-928 MHz ISM band interference risk flagged by Barbados Prime Minister's Office

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Status | Notes |
|---|---|---|---|---|
| **Deliver S0 VTOL** | Alex Lomis | *No due date set* | ⚠️ **CRITICAL BLOCKER** | Crash bug under active investigation and repair (week of 2026-04-20); flight test restart in progress. Bench test work overdue as of 2026-04-24; instrumented bench test due mid-week after. Must complete before handoff. |
| **S0 VTOL Handoff to Jack Elston** | Jack Elston | 2026-05-01 | Open | Handoff meeting scheduled June 23, 2026. Dependent on S0 VTOL delivery completion. |
| **Conduct Operator Training** | *Unassigned* | *No due date* | Open | 6 trainees including Junior Brathwaite. Sabu Best available week of May 5, 2025. Delivery planned July 1-4, 2026. Training materials and supplies in scope. |
| **Generate NetCDF on UA or Tablet** | Maciej Stachura | *No due date* | Open | Technical requirement for meteorological data collection capability. |

## Task Summary

**Total Tasks:** 4 open; 0 completed

### By Assignee
- **Alex Lomis (Project Owner):** 
  - Deliver S0 VTOL (open, no due date)
  - **Primary blocker:** S0-VTOL crash bug repair and flight test restart (week of 2026-04-20)
  - **Bench test status (as of 2026-04-24):** One overdue "Visual Observation Bench Test" task; "Instrumented Bench Test" needs completion by mid-week after 2026-04-24 (Maciej Stachura, 2026-04-24)
  - NDAA compliance note: "not sure any are _fully_ NDAA compliant yet but the S0 VTOL, S0 AD, and E2 all can be [compliant]" (Alex Lomis, 2026-04-17)

- **Jack Elston:** 
  - S0 VTOL Handoff (open, due 2026-05-01)
  - Training/travel scheduled for July 1-4, 2026
  - Flagged ground station asset constraints: "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)." (Jack Elston, 2026-04-20) — indicates potential resource reallocation if timeline slips

- **Maciej Stachura:** 
  - Generate NetCDF (open, no due date)
  - **Active work:** S0-VTOL crash bug diagnosis and flight test restart; bench test status tracking (week of 2026-04-20 and 2026-04-24)
  - Outlined 4 main technical milestones for week of April 20 (Maciej Stachura, 2026-04-19/20):
    1. EMASS flight tests
    2. **S0-VTOL restart to find and fix crash bug** ← *Critical path for Barbados*
    3. S3 crash bug investigation and flight tests
    4. Mustang progress
  - **Project priority note (2026-04-24):** S0-VTOL ranked #2 among top 5 company priorities (after S3 IRAD, before EMASS closeout, By-Lite Mustang, and SBIR Magnetometer)

- **Daniel Prendergast:** 
  - Supporting role; confirmed task summary feedback (2026-04-17)
  - Noted light workload: "Hopefully with some more training, Jack Bot can make me entirely obsolete by the end of the month" (2026-04-17)

- **Unassigned:** 
  - Conduct operator training (open, no due date)
  - **Must assign and schedule** — needs coordination with Sabu Best's May 5, 2025 availability and July 1-4, 2026 travel dates

### Notable Patterns
- Core hardware delivery (S0 VTOL) is the critical path blocker with no delivery due date set, but bench test overdue as of late April 2026
- Training and data generation tasks lack due dates and ownership clarity
- Active technical troubleshooting on crash bug dominates current work (week of 2026-04-20 onward)
- Regulatory/compliance tasks completed 2023-2024 but full NDAA compliance still pending
- Project elevated to top-5 priority at BST company level (Maciej Stachura, 2026-04-24)

## Recent Activity

**2026-04-24** — Maciej Stachura escalated S0-VTOL workload status:
- One bench test task ("Visual Observation Bench Test") is **overdue**
- "Instrumented Bench Test" must be completed by mid-week following 2026-04-24
- Asked Alex Lomis about roadblocks and dependencies (Maciej Stachura, 2026-04-24)
- Ranked S0-VTOL as #2 priority among 5 top projects: "(1) S3 IRAD with a targeted delivery of end of