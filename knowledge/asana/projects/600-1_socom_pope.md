# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Project Owner:** Dan Prendergast
- **Timeline:** Multi-phase delivery spanning October 2026 – April 2027
  - CLIN 1 (PCLT baseline): Due Nov 20, 2026
  - CLIN 2 (METAR): Due Jan 31, 2027
  - CLIN 4 (EO/IR R&R): Due Mar 26, 2027
  - CLIN 5 (EO/IR Real-time ATR): Due Apr 30, 2027
- **Status:** Active – prototype build and requirements phase underway. **Schedule has shifted:** per Dan Prendergast (2026-10-08), prototype completion and site visit now expected week of Oct 19 (not Oct 8–9).
- **Team Members:** Dan Prendergast (lead), Josh Fromm, Ethan Domagala, Alex Lomis, Ben Busby; one mechanical/electrical task unassigned
- **Risk Signals:** 
  - Three duplicate "Write requirements and top-level design" tasks for Dan (due 2026-10-19, 2026-10-28, 2027-01-04) — likely represents a single rolling requirements activity across CLINs, needs consolidation
  - One unassigned mechanical/electrical integration task (Due 2027-01-26)
  - Tight sequencing: prototype build → site visit → design refinements

## Key Deliverables & Milestones

### CLIN 1: PCLT Baseline Prototype
1. **Build prototype PCLT S0 with accelerometer** — Ethan Domagala — Due 2026-10-20
   - Accelerometer ordered (per 2026-10-08 feedback); expected delivery late Oct or week of Oct 19
2. **SOCOM site visit and instrumented S0 launch** — Josh Fromm — Due 2026-10-27
3. **Design refinement for launch survival (limited scope)** — Josh Fromm — Due 2026-11-03
4. **CLIN 1 closeout slides/report** — Dan Prendergast — Due 2026-11-20

### CLIN 2: METAR Variant
1. **Build prototype S0 METAR** — Ethan Domagala — Due 2026-12-22
2. **Bench, ground, and local flight testing** — Ethan Domagala — Due 2027-01-09
3. **Operational flight evaluation** — Dan Prendergast — Due 2027-01-26
4. **CLIN 2 closeout slides/report** — Dan Prendergast — Due 2027-01-31

### CLIN 4: EO/IR Reconnaissance & Reporting
1. **EO/IR camera selection and purchase** — Dan Prendergast — Due 2026-10-28
2. **Build prototype S0 EO/IR R&R** — Ethan Domagala — Due 2027-01-28
3. **Bench, ground, and local flight test** — Ethan Domagala — Due 2027-02-19
4. **Operational flight evaluation** — Dan Prendergast — Due 2027-03-22
5. **CLIN 4 closeout slides/report** — Dan Prendergast — Due 2027-03-26

### CLIN 5: EO/IR Real-time ATR
1. **ATR selection and integration** — Dan Prendergast — Due 2027-01-19
   - Notes: Model classification status, training datasets, validation, labels to be determined
2. **Build prototype S0 EO/IR Real-time ATR variant** — Ethan Domagala — Due 2027-04-02
3. **Bench, ground, and local flight test** — Ethan Domagala — Due 2027-04-19
4. **Operational flight evaluation** — Dan Prendergast — Due 2027-04-24
5. **CLIN 5 closeout slides/report** — Dan Prendergast — Due 2027-04-30

### Cross-Cutting Work
- **Datalink and comm protocol modifications** (CLIN 1) — Alex Lomis — Due 2026-11-24
- **Datalink and comm protocol development** (CLIN 2) — Alex Lomis — Due 2026-12-17
- **Datalink radio selection and comm protocol development** (CLIN 5) — Alex Lomis — Due 2027-01-20
- **Software and UI updates for image capture button and display** (CLIN 1) — Ben Busby — Due 2026-12-03
- **Software and UI updates** (CLIN 2) — Ben Busby — Due 2027-01-22

## Task Summary
- **Total tasks:** 34 open, 1 completed
- **Completion rate:** ~3% (1 of 35)
- **Recently completed:** Design and order prototype PCLT end cap (Josh Fromm, due 2026-10-02, completed 2026-10-15) — end cap CAD completed and sent out for quote

### By Assignee (Open Tasks)
| Assignee | Count | Key Responsibilities |
|----------|-------|---------------------|
| Dan Prendergast | 11 | Requirements, design, camera/ATR selection, operational evaluation, closeout reports |
| Josh Fromm | 5 | Mechanical design, refinement, site visit, integration |
| Ethan Domagala | 6 | Prototype builds (PCLT, METAR, EO/IR variants) and flight testing across all CLINs |
| Alex Lomis | 3 | Datalink and comm protocol work across CLINs 1, 2, 5 |
| Ben Busby | 2 | Software and UI updates (CLINs 1, 2) |
| Unassigned | 1 | Mechanical and electrical integration design (Due 2027-01-26) |

## Recent Activity
**2026-10-08** – Dan Prendergast status update (correcting earlier Oct 8–9 timeline):
- Top-level requirements being derived from five CONOPS described in ROMs; **completion expected early next week** (i.e., week of Oct 14)
- Josh Fromm completing end cap CAD **today** and sending for quote
- Accelerometer ordered (to measure ejection force profile)
- **End cap and accelerometer expected late next week or week of Oct 19**
- First test fire to be arranged after parts arrive

**2026-10-15** – End cap design task marked complete; Josh Fromm sent quote request

## Notes & Context
- **Schedule Shift (AUTHORITATIVE):** The original knowledge file indicated Oct 8–9 for prototype build and site visit. Per Dan Prendergast's 2026-10-08 feedback, these milestones have shifted to the week of Oct 19 and beyond. Asana due dates (2026-10-20 for build, 2026-10-27 for site visit) now reflect this revised timeline.
- **Duplicate Requirements Tasks:** Three tasks all titled "Write requirements and top-level design" (or similar) appear for Dan Prendergast with different due dates (2026-10-19, 2026-10-28, 2027-01-04). These likely represent requirements-writing activities for CLINs 1, 4, and 5 respectively, but should be clarified or renamed for clarity.
- **Unassigned Work:** Mechanical and electrical integration design (Due 2027-01-26) is not yet assigned; may block downstream integration work.
- **Site Visit Open Questions:** Josh Fromm's task notes flag:
  - Can PCLT tube be loaded inflight, or must loading occur on ground?
  - Is power switch accessible when inside aircraft?
  - These will be addressed during the SOCOM site visit (due 2026-10-27).
- **Component Delivery Critical Path:** Prototype builds depend on end cap and accelerometer arrival (expected week of Oct 19). This drives the CLIN 1 timeline and cascades to subsequent CL