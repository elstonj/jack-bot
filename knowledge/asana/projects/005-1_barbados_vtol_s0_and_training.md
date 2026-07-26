# [005-1] BARBADOS VTOL S0 and Training

## Overview
- **Client/Customer:** Barbados Meteorological Services
- **Contact:** Sabu Best (1-246-535-0016, Sabu.Best@barbados.gov.bb)
- **Dollar Value:** 
  - $22,337 (S0 VTOL + Training; Invoice 1634 paid Feb. 2024)
  - $21,181.81 (ISARRA Flight Week campaign—two S0 VTOL units + ground station + tablet; Invoice 1667 paid May 21, 2026)
- **Timeline:**
  - Original project due: 2024-10-01 (passed)
  - **S0 VTOL delivery due: May 22, 2026 (CRITICALLY OVERDUE)**
  - S0 VTOL handoff meeting: June 23, 2026
  - Operator training delivery: July 1–4, 2026 (Barbados; 6 trainees including Junior Brathwaite)
  - ISARRA Flight Week campaign: August/September 2026
- **Status:** **CRITICAL DELAY — ACTIVE CRISIS**
  - **S0 VTOL crash/tracking bug under active investigation and repair** (flight test restart in progress; Beck Cotter, March 17, 2026)
  - **Bench test work overdue** (Visual Observation Bench Test overdue as of April 30, 2026; Instrumented Bench Test due by May 1, 2026)
  - May 22 delivery deadline substantially missed; threatens June 23 handoff and July 1–4 training
  - **Per Maciej Stachura (April 30, May 4, 2026):** S0 VTOL ranked #2 company priority (after S3 IRAD, tied with ERAU S0 VTOL); Asana due dates require realistic update post-ByLight meeting
  - Operator training unassigned with no due date despite July 1–4 travel commitment and 6 trainees
  - **902–928 MHz ISM band interference risk flagged by Barbados Prime Minister's Office** — requires verification before operational deployment
  - **ISARRA campaign (two units) in QC phase; August delivery target confirmed** (per team correction, Jack Bot, July 6, 2026; QC ongoing as of July 3, 2026; Kevin Adkins approved)
- **Team Members:**
  - Alex Lomis (project owner)
  - Beck Cotter (S0 VTOL delivery lead; flight-testing ongoing)
  - Jack Elston (handoff/training lead; training documentation ownership reassigned per June 1, 2026)
  - Maciej Stachura (technical troubleshooting/priority management)
  - Daniel Prendergast (support)
  - Kevin Adkins (ISARRA logistics approval)
- **Risk Signals:**
  - **S0 VTOL crash/tracking bug—active repair in progress; flight test restart blocking delivery**
  - **Bench test work overdue (Visual Observation) as of late April 2026; Instrumented Bench Test due early May 2026**
  - May 22 handoff due date critically missed; current delivery timeline unknown
  - Ground station asset scarcity (Jack Elston, April 20, 2026): potential hardware reprioritization if timeline slips
  - **Operator training unassigned and without formal due date** despite imminent July 1–4 travel and 6-person commitment
  - NDAA compliance not finalized (Alex Lomis, April 17, 2026)
  - **Radio interference risk in 902–928 MHz ISM band (Microhard P900) not yet verified**
  - ISARRA campaign: QC ongoing; must complete before August delivery

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Status | Notes |
|---|---|---|---|---|
| **Visual Observation Bench Test** | Beck Cotter or support | 2026-04-24 | ⚠️ **OVERDUE** | Per Maciej Stachura (April 30, 2026): overdue as of that date. Must complete before Instrumented Bench Test. |
| **Instrumented Bench Test** | Beck Cotter or support | ~2026-05-01 | ⚠️ **OVERDUE** | Per Maciej Stachura (April 24 & 30, 2026): due by mid-week following April 24. Blocks S0 VTOL delivery. |
| **Deliver S0 VTOL to Barbados** | Beck Cotter | 2026-05-22 | ⚠️ **CRITICALLY OVERDUE** | Crash/tracking bug under active investigation; flight test restart in progress. Bench tests must complete first. **Per Maciej Stachura (May 4, 2026):** "after your meeting with ByLight let's update the due dates in Asana to realistic numbers." Current May 22 date substantially missed; realistic delivery timeline unknown pending crash bug resolution. Platform: S0 VTOL; Order Qty: 1. Training/travel needed July 1–4. Also: **ISARRA campaign includes two additional S0 VTOL units with ground station and tablet for August/September 2026 delivery; both units in QC as of July 3, 2026 per team correction, Jack Bot, July 6, 2026.** |
| **S0 VTOL Handoff Meeting** | Jack Elston | 2026-06-23 | ⚠️ **At Risk** | In-person handoff with Sabu Best and Barbados Meteorological Services. Dependent on Beck Cotter delivery completion; original May 22 deadline missed. |
| **Operator Training Materials & Supplies** | Jack Elston (reassigned per June 1, 2026 team correction) | *No due date set* | ⚠️ **AT RISK** | Training curriculum and materials for 6 trainees (including Junior Brathwaite). Sabu Best available week of May 5, 2025 for preliminary review. **TEAM CORRECTION (Jack Elston, June 1, 2026):** Documentation and training ownership reassigned to Jack Elston (better suited as default owner). Must finalize by June 2026. |
| **Operator Training Delivery** | Unassigned | 2026-07-01–04 | ⚠️ **CRITICALLY AT RISK** | In-person training in Barbados; 6 trainees. Mission: operate S0 VTOL east of Barbados to intercept developing storms; launch site tentatively Bushy Park. Dependent on S0 VTOL delivery and June 23 handoff. Travel scheduled. **No assignee or due date in Asana despite imminent July 1–4 dates.** |
| **Generate NetCDF on UA or Tablet** | Maciej Stachura | *No due date* | ⚠️ **OPEN** | Technical requirement for meteorological data collection and analysis; supports mission objective to intercept developing storms. |
| **ISM Band Interference Verification** | *Not assigned* | *Not scheduled* | ⚠️ **CRITICAL** | **ACTION REQUIRED:** Verify Microhard P900 (FCC ID: NS913P900; IC ID: 3143A-13P900; PN: MHS185000; 902–928 MHz frequency-hopping, 200 kHz channels) mitigation against interference risk in unregulated ISM band. **Barbados Prime Minister's Office flagged concern:** "the frequency range 902 MHz to 928 MHz is the unregulated ISM band and your drone may be prone to interference when it operates in this band." Brochure: https://www.microhardcorp.com/brochures/P900.Brochure.Rev.1.4.4.pdf. Must complete before operational deployment. |
| **NDAA Compliance Finalization** | *Not assigned* | *Not scheduled* | ⚠️ **OPEN** | Per Alex Lomis (April 17, 2026): S0 VTOL "can be" compliant but not finalized. Status