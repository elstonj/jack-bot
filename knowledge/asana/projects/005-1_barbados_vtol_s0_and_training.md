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
- **Team Members:** Alex Lomis (owner), Jack Elston, Maciej Stachura, Daniel Prendergast
- **Risk Signals:** 
  - **S0 VTOL crash bug—active repair in progress** (week of 2026-04-20); flight test restart critical path
  - May 1, 2026 handoff due date at risk if crash bug repair extends
  - Ground station asset scarcity flagged by Jack Elston (2026-04-20): "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits" — signal that hardware may be reprioritized if timeline slips further
  - Operator training unassigned and without due date despite July 1-4, 2026 travel commitment
  - NDAA compliance pending; S0 VTOL, S0 AD, and E2 "can be" compliant but not "fully" compliant yet (Alex Lomis, 2026-04-17)

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Status | Notes |
|---|---|---|---|---|
| **Deliver S0 VTOL** | Alex Lomis | *No due date set* | ⚠️ **CRITICAL BLOCKER** | Crash bug under active investigation and repair (week of 2026-04-20); flight test restart in progress. Must complete before handoff. |
| **S0 VTOL Handoff to Jack Elston** | Jack Elston | 2026-05-01 | Open | Handoff meeting scheduled June 23, 2026. Dependent on S0 VTOL delivery completion. |
| **Conduct Operator Training** | *Unassigned* | *No due date* | Open | 6 trainees including Junior Brathwaite. Sabu Best available week of May 5, 2025. Delivery planned July 1-4, 2026. Training materials and supplies in scope. |
| **Generate NetCDF on UA or Tablet** | Maciej Stachura | *No due date* | Open | Technical requirement for meteorological data collection capability. |

## Task Summary

**Total Tasks:** 4 open; 0 completed

### By Assignee
- **Alex Lomis (Project Owner):** 
  - Deliver S0 VTOL (open, no due date)
  - **Primary blocker:** S0-VTOL crash bug repair and flight test restart (week of 2026-04-20)
  - NDAA compliance note: "not sure any are _fully_ NDAA compliant yet but the S0 VTOL, S0 AD, and E2 all can be [compliant]" (Alex Lomis, 2026-04-17)

- **Jack Elston:** 
  - S0 VTOL Handoff (open, due 2026-05-01)
  - Training/travel scheduled for July 1-4, 2026
  - Flagged ground station asset constraints: "depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)." (Jack Elston, 2026-04-20) — indicates potential resource reallocation if timeline slips

- **Maciej Stachura:** 
  - Generate NetCDF (open, no due date)
  - **Active work:** S0-VTOL crash bug diagnosis and flight test restart (week of 2026-04-20, Maciej Stachura, 2026-04-20)
  - Outlined 4 main technical milestones for week of April 20:
    1. EMASS flight tests
    2. **S0-VTOL restart to find and fix crash bug** ← *Critical path for Barbados*
    3. S3 crash bug investigation and flight tests
    4. Mustang progress

- **Daniel Prendergast:** 
  - Supporting role; confirmed task summary feedback (2026-04-17)
  - Noted light workload: "Hopefully with some more training, Jack Bot can make me entirely obsolete by the end of the month" (2026-04-17)

- **Unassigned:** 
  - Conduct operator training (open, no due date)
  - **Must assign and schedule** — needs coordination with Sabu Best's May 5, 2025 availability and July 1-4, 2026 travel dates

### Notable Patterns
- Core hardware delivery (S0 VTOL) is the critical path blocker; no delivery due date has been set
- Training and data generation tasks lack due dates and ownership clarity
- Active technical troubleshooting on crash bug dominates current work (week of 2026-04-20)
- Regulatory/compliance tasks completed 2023-2024 but full NDAA compliance still pending

## Recent Activity

**2026-04-20** — Maciej Stachura outlined 4 main technical goals/milestones for the week:
1. EMASS flight tests
2. **S0-VTOL restart to find and fix the crash bug** (Alex Lomis and Maciej Stachura)
3. S3 crash bug investigation and flight test on S1-22, hover test S3
4. Mustang progress

**2026-04-20** — Jack Elston flagged potential asset reallocation: "seems reasonable. depending on timeline we might be able to shift some older ground stations from the S0-VTOL kits. (I hate to do that, but might be best)." 
- **Context:** If handoff date (May 1, 2026) is missed, ground station hardware from Barbados kits may be reprioritized to other projects.

**2026-04-17** — 
- Daniel Prendergast approved task summary: "That's a decent summary for my tasks. Curious what everyone else thinks."
- Alex Lomis clarified NDAA compliance status: "I'm not sure any are _fully_ NDAA compliant yet but the S0 VTOL, S0 AD, and E2 all can be I believe."

## Notes & Context

### Mission Profile
- **Purpose:** Fly east of Barbados into developing storms for meteorological data collection
- **Launch Site:** Bushy Park, flying east into the Atlantic
- **Training Scope:** 6 trainees (including Junior Brathwaite); Sabu Best to lead training
- **Data Collection:** NetCDF generation required on unmanned aircraft or tablet

### Radio System (Microhard P900)
- **Frequency:** 902-928 MHz (unregulated ISM band)
- **Mode:** Frequency hopping; 200 kHz bandwidth per channel
- **Certifications:** FCC ID NS913P900, IC ID 3143A-13P900
- **Part Number:** MHS185000
- **Brochure:** https://www.microhardcorp.com/brochures/P900.Brochure.Rev.1.4.4.pdf
- **⚠️ Interference Risk:**