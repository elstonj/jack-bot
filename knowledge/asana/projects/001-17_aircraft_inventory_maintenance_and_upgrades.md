# [001-17] Aircraft Inventory Maintenance and Upgrades

## Overview
- **Client/customer:** Internal BST development project
- **Dollar value:** Not specified
- **Timeline:** Multi-year project spanning 2018–2025, with final activity in December 2025
- **Status:** **ARCHIVED** – Project concluded with all deliverables completed as of December 2025. Future aircraft and equipment maintenance now tracked through the **Fleet Maintenance Asana Project** (established May 2026 per Daniel Prendergast)
- **Team members involved:** Nate Straus, Ben Busby, Maciej Stachura, Josh Fromm, Jack Elston; majority of historical tasks unassigned
- **Risk signals:** None (project complete and maintenance workflow formalized)

## Key Deliverables & Milestones
- **QC Flight Test Cards** – Created for E2 and Flamewheel platforms (Nov 2023)
- **S2 Platform Development** – Multiple S-series aircraft (S20001–S20018) built and tested throughout project lifecycle
- **E2 Platform Development** – E-series aircraft (E20001–E20014) completed through 2024
- **Flamewheel (FW) Platform** – FW0001, FW0002, FW 450 variants completed (2018–2025)
- **EGO-I Specialized Aircraft** – Magnetometer calibration and hardware upgrades (2019)
- **Hardware Infrastructure** – Battery packs, rail launcher systems, GCS boards, servo orders completed
- **Gazebo Simulation** – Alerion Turbine Inspection simulation framework completed (Oct 2025)
- **Multi-rotor Estimator Code** – Software development with simulation and flight test validation (concluded Jan 2021)
- **S3 Platform Planning** – Three distinct upgrade tracks identified (Jul 2026):
  - **S3 Whitehorse Upgrades** – Separate work stream; candidate for standalone project once approved and funded
  - **S3 General Upgrades** – Part of Industrial Plan
  - **S3 Military Upgrades** – Part of Industrial Plan

## Task Summary
- **Total tasks:** 0 open, 0 completed in current Asana view (historical 180 completed tasks archived)
- **Historical tasks by assignee (from archive):**
  - Unassigned: ~165 tasks (bulk of hardware and platform work)
  - Nate Straus: S20009 platform (Dec 2025)
  - Maciej Stachura: QC test cards, E2 thrust diagnostics, Gazebo simulation work
  - Ben Busby: Gazebo simulation (Alerion Turbine Inspection)
  - Josh Fromm: E2 battery stoppers (Sep 2021)
  - Jack Elston: FW 450 hardware, EGO-I magnetometer calibration (2019)
- **Notable patterns:** Heavy use of unassigned tasks suggests batch/team-wide work; platform naming convention (S2X, E2X, FWX) tracks distinct aircraft families; extensive parts ordering and assembly work indicates inventory management focus

## Recent Activity

**S3 Industrial Plan Timeline Adjustments (Jul 2026):**
Per Maciej Stachura (Jul 27–28, 2026), the following modifications to the Industrial Plan starting September 2026 are proposed for KS Tech Sync:
1. **Cancel** S3 Europe wing reduction
2. **Move S3 Hybrid right** and **S0/S0-VTOL ISR left** (with goal of S0-ISR demo for UK)
3. **Move S3 de-ice and S3 Salt Spray right** and **S3 severe cold left** (to align with Whitehorse demo timeline)
4. **Status uncertain** on S3 Methane, S3 Visual, and S3 comms in Q4 2026 (awaiting decision)

**S3 Platform Planning (Jul 2026):**
Per Maciej Stachura (Jul 24, 2026), three distinct S3 upgrade initiatives are now formally separated:
1. **S3 Whitehorse Upgrades** – Separate from Industrial Plan; pending approval and funding; will be spun into standalone **S3 Whitehorse** project once approved
2. **S3 General Upgrades** – Part of Industrial Plan
3. **S3 Military Upgrades** – Part of Industrial Plan

**Workflow Evolution & Post-Flight Issue Management (May 2026):**
Daniel Prendergast established a standardized post-flight issue reporting form (May 11, 2026) that automatically routes aircraft and equipment issues to the **"Fleet Maintenance" Asana Project** for hardware issues, or other relevant projects. This form is now part of standard BST post-flight procedures and supersedes task tracking within this archived project.

**Final project completion (2025):**
- S20009 platform completed by Nate Straus (Dec 17, 2025)
- FW0001 and FW0002 platform work finalized (Oct 21, 2025)
- Major October 2025 batch completion (Oct 15):
  - S2 battery pack builds (qty 2–3 units)
  - Rail launcher components (dummy weight, control box parts)
  - GCS board testing and validation
  - Balance lead assembly (qty 6)
  - S-series platform work (S20012–S20018)
  - Servo orders (30x Hacker DITEX-0606 micro servos)
  - Gazebo simulation work for Alerion Turbine Inspection (Ben Busby, Pablo, Maciej collaboration)
  - E2 platform thrust diagnostics (Maciej Stachura)

## Notes & Context

**Project scope:** Comprehensive multi-rotor aircraft development and maintenance spanning 7+ years, covering:
- **Software development:** Multi-rotor estimator code with simulation and flight test validation (concluded Jan 2021)
- **Hardware platforms:** Four distinct aircraft families (S2, E2, Flamewheel, EGO-I) with iterative builds and upgrades
- **Inventory management:** Extensive parts procurement (batteries, servos, propellers, hardware), assembly (battery packs, lead balancing), and maintenance (case repairs, replacement latches)
- **Quality assurance:** QC flight test cards, thrust diagnostics, board testing
- **Simulation integration:** Gazebo-based simulation framework for Alerion Turbine Inspection

**Key technical notes:**
- E20006 preflight incident (2024) documented propeller idling issue related to tablet code synchronization
- Blade torque specifications determined through hardware testing with loctite (2021)
- Extensive supplier relationships (Hacker Motors, SKB cases, Lee for cost updates)

**Post-project maintenance framework:** All future aircraft and equipment issues are captured via Daniel Prendergast's post-flight form (May 2026) and automatically routed to the Fleet Maintenance project or other relevant project spaces. This archived project serves as historical reference only.

**Future roadmap:** S3 platform development underway with three separate upgrade tracks; S3 Whitehorse upgrades to be spun into standalone project once funding/approval secured. Industrial Plan modifications under discussion for September 2026 execution (per Maciej Stachura, Jul 24–28, 2026).