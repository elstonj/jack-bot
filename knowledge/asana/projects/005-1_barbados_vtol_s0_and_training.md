# [005-1] BARBADOS VTOL S0 and Training

## Overview
- **Client/Customer:** Barbados Meteorological Services
- **Contact:** Sabu Best (1-246-535-0016, Sabu.Best@barbados.gov.bb)
- **Dollar Value:** $22,337 (fully funded to BST; Invoice 1634 paid Feb. 2024) + **$21,181.81 for ISARRA Flight Week campaign** (Invoice 1667, paid May 21, 2026)
- **Timeline:** 
  - Original project due: 2024-10-01 (**PASSED**)
  - S0 VTOL delivery due: May 22, 2026 (**AT CRITICAL RISK**)
  - S0 VTOL handoff meeting: June 23, 2026
  - Operator training delivery: July 1–4, 2026
  - Sabu Best availability for preliminary materials review: week of May 5, 2025
  - **ISARRA Flight Week campaign: August/September 2026** (two S0 VTOL units + ground station + tablet; delivery target aligned with August 2026)
- **Status:** **CRITICAL DELAY — ACTIVE CRISIS (as of April 30, 2026); secondary ISARRA campaign in build/QC phase (July 2026)**
  - **S0-VTOL crash/tracking bug under active investigation and repair** (week of April 20, 2026); flight test restart in progress (Beck reported ongoing as of March 17, 2026)
  - **Bench test work overdue as of April 24, 2026:** "Visual Observation Bench Test" overdue; "Instrumented Bench Test" due by Thursday following April 24 (Maciej Stachura, April 24 & 30, 2026)
  - May 22, 2026 delivery deadline at imminent risk; threatens June 23 handoff and July 1–4 training dates
  - **Per Maciej Stachura (April 30, May 4, 2026):** S0-VTOL ranked #2 company priority (after S3 IRAD, tied with ERAU S0-VTOL delivery); requires realistic Asana due date update post-ByLight meeting
  - Operator training unassigned with no due date despite July 1–4 travel commitment and 6 trainees
  - **902–928 MHz ISM band interference risk flagged by Barbados Prime Minister's Office** — requires verification before operational deployment
  - **ISARRA campaign (two units) in QC phase; August delivery target confirmed with Kevin Adkins** (Slack, May 21, 2026)
- **Team Members:** Alex Lomis (owner), Beck Cotter (delivery lead), Jack Elston (handoff/training lead), Maciej Stachura (technical troubleshooting/priority management), Daniel Prendergast (support), Kevin Adkins (ISARRA logistics approval)
- **Risk Signals:** 
  - **S0 VTOL crash/tracking bug—active repair in progress; flight test restart on critical path**
  - **Bench test work overdue (Visual Observation); Instrumented Bench Test due mid-week of May 5, 2026**
  - May 22 handoff due date at critical risk if crash bug repair extends beyond next 1–2 weeks
  - Ground station asset scarcity flagged by Jack Elston (April 20, 2026): potential hardware reprioritization if timeline slips
  - **Operator training unassigned and without formal due date** despite imminent July travel and 6-person commitment
  - NDAA compliance not finalized; per Alex Lomis (April 17, 2026), S0 VTOL "can be" compliant but not "fully" compliant yet
  - **Radio interference risk in 902–928 MHz ISM band (Microhard P900, FCC ID NS913P900, frequency-hopping 200 kHz channels) not yet verified**
  - ISARRA campaign: QC in progress; must complete before August delivery

## Key Deliverables & Milestones

| Deliverable | Assignee | Due Date | Status | Notes |
|---|---|---|---|---|
| **Visual Observation Bench Test** | Beck Cotter (or support team) | 2026-04-24 | ⚠️ **OVERDUE** | Per Maciej (April 30, 2026): "one overdue task 'Visual Observation Bench Test'"; must catch up before next deliverable. |
| **Instrumented Bench Test** | Beck Cotter (or support team) | ~2026-05-01 (mid-week following 2026-04-24) | ⚠️ **IN PROGRESS** | Per Maciej (April 24 & 30, 2026): due "by next Thursday" following April 24; blocking S0 VTOL delivery. |
| **Deliver S0 VTOL to Barbados** | Beck Cotter | 2026-05-22 | ⚠️ **CRITICAL BLOCKER** | Crash/tracking bug under active investigation and repair (week of April 20, 2026); flight test restart in progress. Bench tests must complete first. **Per Maciej (May 4, 2026): "after your meeting with ByLight let's update the due dates in Asana to realistic numbers"** — current May 22 date likely unrealistic pending crash bug resolution. Platform: S0 VTOL; Order Qty: 1. Training/travel needed July 1–4. |
| **S0 VTOL Handoff Meeting** | Jack Elston | 2026-06-23 | ⚠️ **At Risk** | In-person handoff with Sabu Best and Barbados Meteorological Services. Dependent on Beck Cotter delivery (May 22) completion. |
| **Operator Training Materials & Supplies** | <@U04CZK4K7P0> | *No due date* | ⚠️ **OPEN** | Training curriculum and materials required for 6 trainees (including Junior Brathwaite). Sabu Best available week of May 5, 2025 (for preliminary materials review). **TEAM CORRECTION (Jack Elston, June 1, 2026):** Documentation and training ownership reassigned from <@U014ZL9FLE9> to <@U04CZK4K7P0> (better suited as default owner for this type of deliverable). Must finalize by June 2026. |
| **Operator Training Delivery** | Jack Elston | 2026-07-01–04 | ⚠️ **At Risk** | In-person training in Barbados; 6 trainees (including Junior Brathwaite). Travel scheduled. Mission: operate S0 VTOL east of Barbados to intercept developing storms; launch site tentatively Bushy Park. Dependent on S0 VTOL delivery and June 23 handoff. |
| **Generate NetCDF on UA or Tablet** | Maciej Stachura | *No due date* | ⚠️ **OPEN** | Technical requirement for meteorological data collection and analysis; supports mission objective to intercept developing storms. |
| **ISM Band Interference Verification** | *Not assigned* | *Not scheduled* | ⚠️ **CRITICAL** | **ACTION REQUIRED:** Verify Microhard P900 (FCC ID: NS913P900; IC ID: 3143A-13P900; PN: MHS185000; 902–928 MHz frequency-hopping, 200 kHz channels) mitigation against interference risk in unregulated ISM band. **Barbados Prime Minister's Office flagged concern:** "the frequency range 902 MHz to 928 MHz is the unregulated ISM band and your drone may be prone to interference when it operates in this band." Brochure reference: https://www.microhardcorp.com/brochures/P900.Brochure.Rev.1.4.4.pdf. Must complete before operational deployment. |
| **NDAA Compliance Finalization** | *Not assigned* | *Not scheduled* | ⚠️ **OPEN** | Per Alex Lomis (