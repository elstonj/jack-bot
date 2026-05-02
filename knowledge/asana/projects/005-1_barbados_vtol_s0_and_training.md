# [005-1] BARBADOS VTOL S0 and Training

## Overview
- **Client/Customer:** Barbados Meteorological Services
- **Contact:** Sabu Best (1-246-535-0016, Sabu.Best@barbados.gov.bb)
- **Dollar Value:** $22,337 (fully funded to BST; Invoice 1634 paid Feb. 2024)
- **Timeline:** 
  - Original project due: 2024-10-01 (**PASSED**)
  - S0 VTOL delivery/handoff due: May 1, 2026
  - Handoff meeting: June 23, 2026
  - Training window: May 5, 2025 week (Sabu Best availability for preliminary materials review)
  - Travel/training delivery: July 1–4, 2026
- **Status:** **CRITICAL DELAY** — Original due date (Oct 2024) passed. As of late April 2026, **S0-VTOL has an active crash bug under investigation** (week of April 20, 2026); restart and flight tests in progress. **Bench test work overdue as of 2026-04-24** ("Visual Observation Bench Test"); "Instrumented Bench Test" due mid-week after 2026-04-24 (Maciej Stachura, 2026-04-24). S0 VTOL delivery blocker threatens May 1 handoff date. Operator training unassigned with no due date. Major deliverables remain open.
  - **Per Maciej Stachura (2026-04-24):** S0-VTOL is ranked #2 among top 5 BST company priorities: (1) S3 IRAD with end-of-May delivery target; (2) **S0-VTOL (two deliveries: ERAU and Barbados)**; (3) EMASS closeout; (4) By-Lite Mustang; (5) SBIR Magnetometer.
- **Team Members:** Alex Lomis (owner/delivery lead), Jack Elston (handoff/training lead), Maciej Stachura (technical troubleshooting), Daniel Prendergast (support)
- **Risk Signals:** 
  - **S0 VTOL crash bug—active repair in progress** (week of 2026-04-20); flight test restart on critical path
  - **Bench test work overdue as of 2026-04-24** ("Visual Observation Bench Test"); "Instrumented Bench Test" due mid-week after 2026-04-24 (Maciej Stachura, 2026-04-24)
  - May 1, 2026 handoff due date at imminent risk if crash bug repair extends
  - Ground station asset scarcity flagged by Jack Elston (2026-04-20): "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)." — signal that hardware may be reprioritized if timeline slips further
  - Operator training unassigned and without due date despite July 1–4, 2026 travel commitment
  - NDAA compliance not finalized; S0 VTOL, S0 AD, and E2 "can be" compliant but not "fully" compliant yet (Alex Lomis, 2026-04-17)
  - **902–928 MHz ISM band interference risk flagged by Barbados Prime Minister's Office** — S0 VTOL uses Microhard P900 radio (FCC ID: NS913P900, IC ID: 3143A-13P900, PN: MHS185000) operating in unregulated ISM band; frequency-hopping (200 kHz channels) may mitigate but **requires verification before operational deployment**

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Status | Notes |
|---|---|---|---|---|
| **Deliver S0 VTOL** | Alex Lomis | 2026-05-01 | ⚠️ **CRITICAL BLOCKER** | Crash bug under active investigation and repair (week of 2026-04-20); flight test restart in progress. **Bench test work overdue as of 2026-04-24** ("Visual Observation Bench Test"); "Instrumented Bench Test" due mid-week after 2026-04-24 (Maciej Stachura, 2026-04-24). Must complete before handoff. |
| **S0 VTOL Handoff & Training** | Jack Elston | 2026-05-01 (delivery); 2026-07-01–04 (training) | Open | Handoff meeting scheduled June 23, 2026. Training delivery July 1–4, 2026. 6 trainees including Junior Brathwaite. Launch site: tentatively Bushy Park, east into Atlantic (for storm intercept). Dependent on S0 VTOL delivery completion. Platform: S0 VTOL; Order Qty: 1. Travel scheduled: Yes. |
| **Operator Training Materials & Supplies** | *Unassigned* | 2026-07-01 | Open | Training materials and supplies required for operator instruction. Sabu Best available week of May 5, 2025 (for preliminary materials review). **Must assign and finalize curriculum.** |
| **Generate NetCDF on UA or Tablet** | Maciej Stachura | *No due date* | Open | Technical requirement for meteorological data collection capability; supports mission objective to intercept developing storms east of Barbados. |

## Task Summary

**Total Tasks:** 1 open formal task in Asana (Barbados S0 VTOL handoff); 3+ subtasks/dependencies tracked in notes and team communications

### By Assignee
- **Alex Lomis (Project Owner):** 
  - Deliver S0 VTOL (open, due 2026-05-01) — **PRIMARY BLOCKER**
  - **Crash bug & flight test restart** (week of 2026-04-20) — active investigation in progress
  - **Bench test status (as of 2026-04-24):** One overdue "Visual Observation Bench Test" task; "Instrumented Bench Test" needs completion by mid-week after 2026-04-24 (Maciej Stachura, 2026-04-24)
  - NDAA compliance status: "not sure any are _fully_ NDAA compliant yet but the S0 VTOL, S0 AD, and E2 all can be [compliant]" (Alex Lomis, 2026-04-17)

- **Jack Elston:** 
  - Barbados S0 VTOL (open, due 2026-05-01) — formal handoff task in Asana
  - S0 VTOL Handoff meeting: June 23, 2026
  - Training/travel scheduled: July 1–4, 2026
  - Flagged ground station asset constraints (2026-04-20): "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)." — indicates potential resource reallocation if timeline slips

- **Maciej Stachura:** 
  - Generate NetCDF (open, no due date)
  - **Active work:** S0-VTOL crash bug diagnosis and flight test restart; bench test status tracking (weeks of 2026-04-20 and 2026-04-24)
  - Outlined 4 main technical milestones for week of April 20 (Maciej Stachura, 2026-04-19/20):
    1. EMASS flight tests
    2. **S0-VTOL restart to find and fix crash bug** ← *Critical path for Barbados*
    3. S3 crash bug investigation and flight tests
    4. Mustang progress
  - **Project priority confirmation (2026-04-24):** S0-VTOL ranked #2 among top 5 company priorities

- **Daniel Prendergast:** 
  - Support role (not yet formally assigned to specific Barbados tasks)

## Recent Activity

- **2