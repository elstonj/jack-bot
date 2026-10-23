_Asana snapshot as of 2026-10-23: 21 open tasks, 37 completed (last 365 days)._

# S0 Hurricane Phase II - 2025

## Overview
- **Client/Customer:** NOAA / University of Miami (Joe Cione, primary POC)
- **Billing Contact:** Joe Cione & Jun Zhang (jun.zhang@noaa.gov)
- **Total Budget:** $1,700,000 (all to Black Swift Technologies)
- **Contract Number:** 1305M225P0034
- **Timeline:** 
  - Original end date: August 25, 2025
  - **Extended to: August 25, 2026** (6-month extension)
- **Status:** **ARCHIVED** — marked as low priority; however, active work ongoing with contract extension
- **Team:** Whole BST team; key assignees include Jack Elston, Maciej Stachura, Josh Fromm, Ethan Domagala, Dan Prendergast, Alex Lomis
- **Risk Signals:** 
  - Contract extension just granted (Dec 2026 update); many open tasks still lack assignments and due dates
  - 21 open tasks vs. 37 completed; most open work is category-level (Design, Testing, Construction) without specific owners
  - Qualification survey in progress (Oct 2026) — Spencer Hoehl requesting FAA Part 107/61/141, security clearances, NOAA Hurricane training, and COA documentation from team

## Key Deliverables & Milestones

**Extended Contract CLINs (due by August 25, 2026):**
- CLIN 1002 – Operator and Observer course development
- CLIN 1003 – Operator and Observer Training session
- CLIN 1004 – Instructor Training Course development
- CLIN 1005 – Instructor Training

**Completed Milestones:**
- [DONE] Delivery of 34 systems to AOC — due 2025-07-01, completed 2025-12-15
- [DONE] Hardware / software freeze — due 2025-07-01, completed 2025-11-17
- [DONE] Live video — completed 2025-12-10 (Optional MVP)

**Open Milestones (no due date assigned):**
- 10Hz Met Data (Required MVP)
- Increased Endurance (Required MVP)
- Dual GPS (Required MVP)
- GUI / usability improvements (Required MVP)
- Airops updates (Required MVP)
- Skyfora Integration plan (Optional MVP)
- MultiUAS (Optional MVP)
- Deliver additional 13 S0 systems — due 2026-07-01

## Task Summary
- **Total open:** 21 | **Total completed:** 37
- **Open tasks by category:** Most are high-level buckets (Design, Testing, Construction, Deployments, Administrative, Meetings, Travel, Software/Firmware, Data processing, QC) with no assignee
- **Key assignees (completed work):**
  - Jack Elston: 10+ completed tasks (firmware, integration, testing, multi-UAS setup)
  - Maciej Stachura: 4 completed tasks (testing, wind estimator, flight notes)
  - Josh Fromm: 2 completed tasks (battery fix, changelog)
  - Ethan Domagala, Dan Prendergast, Alex Lomis: 1–2 each
- **Completion patterns:** Heavy focus on bug fixes and validation (IAS sensor issues, RH conditioning, battery drain, radar interference) through Feb–April 2026; most recent work is testing and integration

## Recent Activity
- **December 10, 2025:** Status update — contract extension confirmed. NOAA allocated $115K + $54K (total ~$169K additional). Funds earmarked for early parts ordering or 3 UAS builds. Jack Elston working with NOAA to establish IDIQ contract for ongoing build orders. Planning 25–30 UAS for FY25.
- **Nov–Dec 2025:** Completed deployment mission (NOAA, Joe Cione, 2 S0 aircraft, Maciej Stachura as operator); hardware/software freeze; new UI testing; clear-air testing
- **Feb–Mar 2026:** Bug fix cycle — resolved IAS sensor detection failures, RH conditioning, radar interrupt, battery drain; confirmed dual S0 and multi-UAS capability during CAT
- **Apr 2026:** Final QC flights and local testing validation
- **Oct 2026 (Team Corrections):** Spencer Hoehl requesting documentation of team member qualifications (FAA pilot certifications, security clearances, NOAA Hurricane training, COA training) — suggests upcoming operational or regulatory requirements

## Notes & Context
- **Project Type:** Development and deployment of S0 VTOL UAS for hurricane observation; continuation of existing program into FY25 hurricane season
- **Products/Services:** S0, Custom Payload
- **Key Issues Resolved:**
  - Airspeed (IAS) sensor: Frequent failures during high-flight-tempo ops (Oct 2025); now stable after parameter adjustments (FF 3.5, Kh 1.5)
  - Relative Humidity (RH): Initially low reporting; conditioning logic restored; post-processing via datalink temps confirmed
  - Battery management: S0-45 shipped full, arrived at 80%; now flagged for safer transport procedures
  - Multi-UAS capability: Confirmed feasibility of dual ground stations + antenna on P3 for simultaneous operations
- **Contract Acceleration:** Original scope (34 systems delivery, hardware/SW freeze by mid-2025) completed ahead of schedule. Extension allows continued feature development (10Hz met data, increased endurance, GUI/usability, AirOps updates) and additional system builds (13 more units by July 2026)
- **Organizational Context:** Funds being routed for parts ordering or full UAS builds; IDIQ contract in negotiation suggests larger ongoing commitments beyond current contract
- **Qualification Request (Oct 2, 2026):** Spencer Hoehl conducting team-wide survey of pilot certifications, security clearances, and hurricane/COA training — likely in preparation for expanded operations or NOAA compliance review related to CLINs 1002–1005 (training course development and delivery)