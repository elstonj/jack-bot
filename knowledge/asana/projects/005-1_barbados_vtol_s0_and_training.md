# [005-1] BARBADOS VTOL S0 and Training

## Overview
- **Client/Customer:** Barbados Meteorological Services
- **Contact:** Sabu Best (1-246-535-0016, Sabu.Best@barbados.gov.bb)
- **Dollar Value:** $22,337 (fully funded to BST)
- **Timeline:** Project due 2024-10-01 (passed); training window May 5, 2025 week; travel dates July 1-4, 2026; handoff June 23, 2026
- **Status:** **CRITICAL DELAY** — Project due date passed October 2024. As of April 2026, team feedback indicates **S0-VTOL has a crash bug under active investigation** (Maciej Stachura, 2026-04-20); restart and flight tests planned for the week of April 20. Handoff and training still pending. Major deliverables remain open with no completion dates set.
- **Team Members:** Alex Lomis (owner), Jack Elston, Maciej Stachura, Daniel Prendergast
- **Risk Signals:** 
  - **S0 VTOL delivery blocker:** crash bug found; flight test restart in progress (as of 2026-04-20)
  - S0 VTOL handoff due May 1, 2026; June 23 handoff meeting scheduled (possible timeline compression)
  - Operator training unassigned with no due date
  - Ground station asset scarcity flagged by Jack Elston (2026-04-20): may need to reallocate older ground stations from S0-VTOL kits if timeline slips further

## Key Deliverables & Milestones
- **Deliver S0 VTOL** (Alex Lomis) — No due date set; **CRITICAL BLOCKER** with active crash bug repair underway
  - Crash bug investigation and flight test restart: week of 2026-04-20 (Maciej Stachura, et al.)
- **S0 VTOL Handoff to Jack Elston** — Due May 1, 2026; handoff meeting scheduled June 23, 2026
- **Conduct Operator Training** (Unassigned) — No due date; planned for May 5, 2025 week (6 participants including Junior Brathwaite); travel July 1-4, 2026
- **Generate NetCDF on UA or Tablet** (Maciej Stachura) — No due date; technical requirement for data collection

## Task Summary
- **Total Tasks:** 4 open (as of latest data); previous knowledge showed 12 total with 8 completed — **current data shows Asana task count reduced**
- **By Assignee:**
  - **Maciej Stachura:** Generate NetCDF (open, no due date) — actively engaged in S0-VTOL crash bug diagnosis
  - **Alex Lomis:** Deliver S0 VTOL (open, no due date) — owner; noted S0 VTOL _can be_ NDAA compliant (with S0 AD and E2 variants) pending full compliance work
  - **Jack Elston:** S0 VTOL Handoff (open, due May 1, 2026); flagged ground station asset constraints
  - **Daniel Prendergast:** Recently provided task summary feedback (2026-04-17); appears to have supporting role
  - **Unassigned:** Operator training (open, no due date)
- **Notable Patterns:** Regulatory/administrative tasks completed 2023-2024; core hardware delivery and training stalled; active technical troubleshooting on critical path

## Recent Activity
- **2026-04-20:** Maciej Stachura outlined 4 main technical milestones for the week:
  1. EMASS flight tests
  2. **S0-VTOL restart to find and fix the crash bug** (Maciej Stachura, Alex Lomis team)
  3. S3 work to find crash bug and flight test on S1-22, hover test S3
  4. Mustang Progress
- **2026-04-20:** Jack Elston flagged potential asset reallocation: older ground stations from S0-VTOL kits may need to shift to other projects if timeline continues to slip
- **2026-04-17:** Daniel Prendergast provided positive feedback on task summaries; Alex Lomis clarified NDAA compliance status (not yet fully compliant, but S0 VTOL, S0 AD, E2 variants can be)
- **2026-01-19:** Drone flight application completed (previous cycle)
- **2024:** Export licensing chain completed; payment received (Invoice 1634, Feb 2024)

## Notes & Context

### Mission Profile
- **Purpose:** Fly east of Barbados into developing storms for meteorological data collection
- **Launch Site:** Bushy Park, flying east into the Atlantic
- **Training Intent:** 6 trainees including Junior Brathwaite

### Radio System (Microhard P900)
- **Frequency:** 902-928 MHz (unregulated ISM band)
- **Mode:** Frequency hopping; 200 kHz bandwidth per channel
- **Certifications:** FCC ID NS913P900, IC ID 3143A-13P900
- **Part Number:** MHS185000
- **Brochure:** https://www.microhardcorp.com/brochures/P900.Brochure.Rev.1.4.4.pdf
- **⚠️ Interference Risk:** Barbados PM's Office flagged potential interference in unregulated ISM band (902-928 MHz range)

### Training & Support
- **Trainees:** 6 people (including Junior Brathwaite)
- **Trainer Availability:** Sabu Best available week of May 5, 2025
- **Deliverables:** Training materials and supplies included in $22,337 scope
- **Travel:** July 1-4, 2026 (scheduled for handoff/training delivery)

### Regulatory & Compliance
- ✅ Export license obtained (Aug 21, 2024)
- ✅ S0 classified for export (May 22, 2024)
- ✅ Drone flight application completed and submitted (Jan 19, 2026)
- ✅ Payment received (Invoice 1634, Feb 2024)
- 🔄 **NDAA Compliance:** S0 VTOL, S0 AD, and E2 variants _can be_ NDAA compliant pending completion of compliance work (Alex Lomis, 2026-04-20)

### Technical Requirements
- NetCDF data generation capability needed on unmanned aircraft or tablet
- **Active Issue:** S0-VTOL crash bug under investigation and repair (week of 2026-04-20)
- Pre-flight checklist created and completed (Mar 2024)
- Seamless Docs portal: https://barbados.seamlessdocs.com/sc/uasapplication
- Drive folder: https://drive.google.com/drive/folders/13bU4xXnxT5qWnw9XbtGFCABcVPVhcvRb

### Priority
- Medium (per custom field)

---

## ⚠️ URGENT ACTION ITEMS
1. **S0-VTOL crash bug resolution** — Active investigation underway (week of 2026-04-20); prioritize flight test restart and completion before May 1 handoff date
2. **Confirm S0 VTOL delivery due date** — Set formal completion target aligned with May 1, 2026 handoff task
3. **Assign and schedule operator training** — Coordinate with Sabu Best's May 5, 2025 availability; reconcile with July 1-4, 2026 travel dates
4. **Ground station asset review** — Jack Elston flagged potential shortage; assess availability and reallocation plan if timeline extends
5. **Mitigate radio interference risk** — Validate Microhard P900 operation in Barbados ISM band regulatory environment with PM's Office concern noted