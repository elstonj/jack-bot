_Asana snapshot as of 2026-11-17: 63 open tasks, 17 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview

- **Client/Customer:** SOCOM
- **Priority:** High
- **Status:** Active — in full execution across 6 CLINs (Contract Line Items). Early-phase tasks (camera selection, PCLT testing) recently completed; design and prototyping work underway through mid-2027.
- **Project Owner:** Dan Prendergast
- **Timeline:** 
  - Started: ~October 2026 (early prototyping/trade studies)
  - Major milestone: PCLT Test Launch at SOCOM Facility due 2026-11-13
  - Final delivery: Multiple CLIN closeouts through May 2027
  - Key gate: Customer airworthiness process begins 2027-01-25
- **Team Members:** Dan Prendergast (PM/lead), Jack Elston (electrical/firmware), Josh Fromm (mechanical design), Sam Hild (carrier board), Ethan Domagala (prototyping/test), Ben Busby (software), Maciej Stachura (sensors/software), Alex Lomis (test), others
- **Task Volume:** 63 open, 17 completed (77% open rate)

## Risk Signals

- **PCLT Test Launch due 2026-11-13** (imminently due) — assigned to Dan Prendergast; associated report and customer photos due same week. Status unclear.
- **GFI: Answers re PCLT due 2026-11-20** — 3 critical open questions on safe separation weight, mount angle, and gap tolerances. No assignee; blocks downstream design.
- **Hardware selection dependencies (Nov 18–Dec 14):** Camera, processing hardware, carrier board, radio selection staggered; many tasks unassigned or dependent on prior work.
- **High burndown ahead:** 60–70 Mechanical Engineer hours per task across Dec–Feb; Electrical/Firmware 25–40 hours per task; Systems Engineer hours fragmented across variants (3–31 hours).
- **Multiple unassigned critical tasks:** VOXL2 lead time & ordering, RB5 hardware validation, autopilot-to-SBC spec, EMI testing, all due 2026-11-20 with no owner.

## Key Deliverables & Milestones

| Milestone/Deliverable | Due Date | Owner | Scope/Notes |
|---|---|---|---|
| **PCLT Test Launch at SOCOM Facility** | 2026-11-13 | Dan Prendergast | 50 ME hrs, 12 SE hrs; test of prototype |
| **GFI: Answers re PCLT** | 2026-11-20 | Unassigned | Safe separation, mount angle, aircraft gap; critical blocker |
| **All-variants Common Camera Selection** | 2026-11-11 | Dan Prendergast | 10 ME, 60 Test hrs; likely complete (selected cameras task done) |
| **All-variants Common Processing Hardware Selection** | 2026-11-18 | Jack Elston | 30 Elec/FW hrs |
| **All-variants Common Radio Selection** | 2026-12-11 | Jack Elston | 25 Elec/FW hrs |
| **All-variants Carrier Board Design & Fab** | 2026-12-14 | Sam Hild | 40 Elec/FW hrs |
| **GFI: Customer begins airworthiness process** | 2027-01-25 | Unassigned | Program gate |
| **CLIN 1 Closeout** | 2027-03-12 | Dan Prendergast | METAR variant |
| **CLIN 2 Closeout** | 2027-03-12 | Unassigned | EO/IR R&R variant |
| **CLIN 3 Closeout** | 2027-05-31 | Unassigned | Auto-METAR variant |
| **CLIN 4 Closeout** | 2027-03-12 | Dan Prendergast | EO/IR ATR variant |
| **CLIN 5 Closeout** | 2027-05-31 | Dan Prendergast | EO/IR FMV variant |
| **CLIN 6 Closeout** | 2027-05-31 | Unassigned | Gimballed camera variant |

**Operational Flight Evaluations (OFEs):** Scheduled across CLINs:
- CLIN 1, 2, 4 combined OFE: 2027-03-05 (52 Test hrs, 31 SE hrs)
- CLIN 3: 2027-03-05
- CLIN 4: 2027-04-24
- CLIN 5: 2027-03-22

## Task Summary

- **Total:** 80 tasks (63 open, 17 completed)
- **Completion rate:** 21% complete
- **Assigned vs. Unassigned:** ~40 tasks unassigned (many critical path)

### Tasks by Assignee (open only)

| Assignee | Count | Key Tasks | Completion Pattern |
|---|---|---|---|
| Dan Prendergast | 11 | PCLT test, camera selection, system reqs, CLIN closeouts, OFE, gimbal trade study, ATR selection | Very active; heavily loaded across all phases |
| Ethan Domagala | 7 | Prototype builds (METAR, EO/IR R&R, Auto-METAR, ATR, FMV), bench/flight testing | Builds and test focus; starts mid-Feb |
| Josh Fromm | 5 | PCLT design changes, mechanical/electrical updates (multiple CLIN variants) | Mechanical design; Dec–Feb window |
| Jack Elston | 4 | Processing hardware, radio selection, comm protocol (CLINs 1, 2, 4), datalink (CLIN 6) | Electrical/firmware lead; Nov–Jan |
| Ben Busby | 3 | Software for payload integration (CLINs 1, 4, 6) | Software integration; Jan–April |
| Maciej Stachura | 3 | Precipitation/cloud/visibility sensor trade studies (CLIN 3), software (Auto-METAR, CLIN 3) | Sensor selection & automation; Jan–March |
| Sam Hild | 1 | Carrier board design & fab | Single critical deliverable; due Dec 14 |
| Unassigned | 29 | VOXL2 environment, RB5 validation, EMI testing, GFI PCLT answers, all CLIN closeouts (2, 3, 6), comm protocol (CLIN 3), mechanical updates (CLIN 4) | Many critical-path items without owners |

### Notable Patterns

- **Hardware selection bottleneck (Nov–Dec):** Camera, processing, radio, carrier board decisions cascade; many prerequisite tasks unassigned.
- **Prototype builds compressed into Feb–April:** Ethan Domagala is sole builder across 5 variants (METAR, EO/IR R&R, Auto-METAR, ATR, FMV); tight scheduling.
- **Four distinct CLIN variants** (1=METAR, 2=EO/IR R&R, 3=Auto-METAR, 4=EO/IR ATR, 5=EO/IR FMV, 6=Gimballed FMV), each requiring parallel Comm Protocol, Mechanical Updates, and Software tasks — high replication and coordination overhead.
- **Systems Engineer hours fragmented:** 3–31 hrs per task, sprayed across design reviews, comm, component integration, and OFE; suggests tight SE staffing or unclear allocation.
- **Custom fields track effort:** Most design/build tasks include Mechanical Engineer, Electrical/Firmware, Software, Test Engineer, Technician, and Systems Engineer hour budgets — good visibility but cumulative load not summarized at project level.

## Recent Activity

**Completed (last ~2 weeks, inferred):**
- Camera selection finalized (STARVIS + Sony IMX585 tested; lenses and filters assessed)
- Hadron cameras ordered
- Night and day camera test plans executed; post-processing complete
- Requirements and design docs finalized for initial phases
- SOCOM site visit completed; prototype PCLT S0 with accelerometer built and launched

**Imminent (next 2 weeks):**
- **2026-11-13:** PCLT Test Launch at SOCOM Facility and report due (Dan Prendergast)
- **2026-11-13:** Document report for test PCLT launch results (Dan Prendergast)
- **2026-11-18:** Processing hardware selection (Jack Elston)
- **2026-11-20:** GFI: Answers re PCLT (critical blocker — no owner assigned); VOXL2 lead time & ordering, RB5 validation, EMI testing, autopilot-to-SBC spec, carrier board layout, demo approach docs all due (all unassigned)

**Upcoming design & build phase (Dec 2026–Feb 2027):**
- Carrier board fab (Sam Hild, due Dec 14)
- PCLT design changes (Josh Fromm, due Dec 11)
- Mechanical/electrical updates for component integration (Josh Fromm, multiple variants, due Dec 21–Feb 17)
- Comm protocol design (Jack Elston, multiple variants, due Dec 11–Jan 20)
- Prototype orders and builds (Ethan Domagala, Feb 1–April 2)
- Bench, ground, and local flight testing (Ethan Domagala, Feb 23–April 19)

## Notes & Context

### Critical Open Questions & Dependencies

From task notes:
- **PCLT mount & separation (GFI due 2026-11-20):**
  - Is 16 lb safe separation weight adequate?
  - What is PCLT mount angle in aircraft?
  - Gap between aircraft skin and PCLT tube rim?
  - *Blocks design changes and certification pathway.*

- **VOXL2 & RB5 processor selection:**
  - CoVar runtime and 64MP frame handling on RB5 hardware not yet confirmed (due 2026-11-20).
  - RB5-class SOMs being compared for RevB carrier board.
  - VOXL2 build environment and bridge port needed (due 2026-11-20).
  - *Blocks carrier board layout and mechanical design.*

- **ATR (Automatic Target Recognition) model status (CLIN 4, due 2027-01-19):**
  - Datasets used: all open source; validation results & classification status TBD.
  - Plans to develop with unclassified model; label list needed.
  - *Affects CLIN 4 (EO/IR ATR) build schedule.*

- **Payload automation patterns:**
  - Multiple tasks reference autonomous collection patterns (circle flight + cardinal heading imagery, image compression, triggers, calibration).
  - Details evolving; affects software design for CLINs 1, 2, 3, 4, 6.

### Staffing & Load

- **Dan Prendergast** carrying PM, design lead, and test leadership; heavy overlap suggests bottleneck risk.
- **Ethan Domagala** sole prototype builder across 5 variants; Feb–April timeline is aggressive.
- **Josh Fromm** (mechanical) and **Jack Elston** (electrical) are dual-variant leads; coordination overhead.
- **29 unassigned critical tasks** — assignment needed immediately for Nov 20–Dec dates.

### Dollar Value

No explicit budget line items in task data; custom fields track effort hours only. Project is SOCOM contract with 6 CLINs (likely cost-plus or FFP by CLIN); no summary P&L visible.

### Airworthiness & Certification

Program gated on customer airworthiness review (Jan 25, 2027). OFEs scheduled March–April 2027 (post-gate). Suggests FAA or SOCOM certification pathway; PCLT test at SOCOM facility is early validation.

### External Coordination

- Monthly update meetings with SOCOM PM established.
- Site visit to SOCOM facility completed; questions about in-flight loading and S0 accessibility resolved.
- L3 Harris consultation on image intensifiers completed.
- CoVar (image processing) SOW/requirements drafted; sponsorship/FCL/DD254 tracking underway.