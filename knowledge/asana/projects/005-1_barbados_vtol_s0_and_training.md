# [005-1] BARBADOS VTOL S0 and Training

## Overview
- **Client/Customer:** Barbados Meteorological Services
- **Contact:** Sabu Best (1-246-535-0016, Sabu.Best@barbados.gov.bb)
- **Dollar Value:** $22,337 (fully funded to BST; Invoice 1634 paid Feb. 2024)
- **Timeline:** 
  - Original project due: 2024-10-01 (**PASSED**)
  - S0 VTOL delivery due: May 22, 2026
  - S0 VTOL handoff meeting: June 23, 2026
  - Operator training delivery: July 1–4, 2026
  - Sabu Best availability for preliminary materials review: week of May 5, 2025
- **Status:** **CRITICAL DELAY** — Original due date (Oct 2024) passed. As of late April 2026, **S0-VTOL has an active crash bug under investigation** (week of April 20, 2026); restart and flight tests in progress. **Bench test work overdue as of 2026-04-24** ("Visual Observation Bench Test"); "Instrumented Bench Test" due by Thursday following 2026-04-24 (Maciej Stachura, 2026-04-24 & 2026-04-30). S0 VTOL delivery blocker threatens May 22 handoff date. Operator training unassigned with no due date. Major deliverables remain open.
  - **Per Maciej Stachura (2026-04-30 & 2026-05-04):** S0-VTOL is ranked #2 among top 5 BST company priorities: (1) S3 IRAD with end-of-May delivery target; (2) **S0-VTOL (two deliveries: ERAU and Barbados)**; (3) EMASS closeout; (4) By-Lite Mustang; (5) SBIR Magnetometer.
- **Team Members:** Alex Lomis (owner), Beck Cotter (delivery lead), Jack Elston (handoff/training lead), Maciej Stachura (technical troubleshooting), Daniel Prendergast (support)
- **Risk Signals:** 
  - **S0 VTOL crash bug—active repair in progress** (week of 2026-04-20); flight test restart on critical path
  - **Bench test work overdue as of 2026-04-24** ("Visual Observation Bench Test"); "Instrumented Bench Test" due by Thursday following 2026-04-24 (Maciej Stachura, 2026-04-24 & 2026-04-30)
  - May 22, 2026 handoff due date at imminent risk if crash bug repair extends
  - Ground station asset scarcity flagged by Jack Elston (2026-04-20): "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)." — signal that hardware may be reprioritized if timeline slips further
  - Operator training unassigned and without due date despite July 1–4, 2026 travel commitment
  - NDAA compliance not finalized; per Alex Lomis (2026-04-17), S0 VTOL, S0 AD, and E2 "can be" compliant but not "fully" compliant yet
  - **902–928 MHz ISM band interference risk flagged by Barbados Prime Minister's Office** — S0 VTOL uses Microhard P900 radio (FCC ID: NS913P900, IC ID: 3143A-13P900, PN: MHS185000) operating in unregulated ISM band with frequency-hopping (200 kHz channels); **requires verification before operational deployment** to confirm mitigation of interference risk

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Status | Notes |
|---|---|---|---|---|
| **Deliver S0 VTOL to Barbados** | Beck Cotter | 2026-05-22 | ⚠️ **CRITICAL BLOCKER** | Crash bug under active investigation and repair (week of 2026-04-20); flight test restart in progress. **Bench test work overdue as of 2026-04-24** ("Visual Observation Bench Test"); "Instrumented Bench Test" due by Thursday following 2026-04-24 (Maciej Stachura, 2026-04-24 & 2026-04-30). Must complete before handoff. Platform: S0 VTOL; Order Qty: 1. Training/travel needed July 1–4. |
| **S0 VTOL Handoff Meeting** | Jack Elston | 2026-06-23 | Open | In-person handoff meeting with Sabu Best and Barbados Meteorological Services. Dependent on Beck Cotter delivery completion. |
| **Operator Training Materials & Supplies** | *Unassigned* | *No due date* | Open | Training materials and supplies required for operator instruction. Sabu Best available week of May 5, 2025 (for preliminary materials review). Training delivery scheduled July 1–4, 2026. 6 trainees including Junior Brathwaite. **Must assign and finalize curriculum.** Intent: drone to fly east of Barbados into developing storms from tentative launch site Bushy Park. |
| **Operator Training Delivery** | Jack Elston | 2026-07-01–04 | Open | Training delivery in Barbados. Travel scheduled. 6 trainees. Dependent on S0 VTOL delivery and June 23 handoff. |
| **Generate NetCDF on UA or Tablet** | Maciej Stachura | *No due date* | Open | Technical requirement for meteorological data collection capability; supports mission objective to intercept developing storms east of Barbados. |
| **ISM Band Interference Verification** | *Not assigned* | *Not scheduled* | Open | **ACTION REQUIRED:** Verify Microhard P900 frequency-hopping mitigation (200 kHz channels) against interference risk in 902–928 MHz ISM band. Barbados Prime Minister's Office flagged concern. Must complete before operational deployment. |

## Task Summary

**Total Tasks:** 4 open in Asana; 0 completed

### By Assignee
- **Beck Cotter:**
  - **Barbados S0 VTOL** (open, due 2026-05-22) — **PRIMARY DELIVERY TASK**
  - Crash bug & flight test restart (week of 2026-04-20) blocking completion
  - Bench test work overdue as of 2026-04-24; instrumented bench test due by Thursday following 2026-04-24 (Maciej Stachura, 2026-04-24 & 2026-04-30)
  - Training/travel needed: Yes (July 1–4, 2026)

- **Jack Elston:** 
  - S0 VTOL handoff meeting: June 23, 2026
  - Operator training/travel scheduled: July 1–4, 2026
  - Flagged ground station asset constraints (2026-04-20): "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)."

- **Maciej Stachura:** 
  - **Generate NetCDF** (open, no due date)
  - **Active work:** S0-VTOL crash bug diagnosis and flight test restart; bench test status tracking (weeks of 2026-04-20 and 2026-04-24)
  - **Priority confirmation (2026-04-30 & 2026-05-04):** S0-VTOL ranked #2 among top 5 company priorities
  - Requesting updates on bench test roadblocks and support needs from Beck Cotter and team (2026-04-24 & 2026-04-30)

- **Alex Lomis:** 
  - Project owner; secondary "Deliver S0 VTOL" task open with no due