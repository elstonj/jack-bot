# BST Milestone Plan

## Document Metadata
- Type: Phase II SBIR milestone and budget plan
- Client/Agency: NASA
- Program/Solicitation: SBIR Phase II (NASA Autonomy program, reference [200-14])
- Date: 2026-05-12
- BST Products/Systems Referenced: SwiftCore RTA Kit, SwiftSim, SwiftDeploy, S2, EMASS, custom-board hardware, ADONIS
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This document outlines BST's two-year Phase II SBIR project plan to advance autonomous flight capabilities to TRL 7. The program structures development across 8 quarters with progressive milestones in simulation (SwiftSim), real-time autonomy infrastructure (SwiftCore RTA Kit), deployment tools (SwiftDeploy), and flight validation, culminating in Part 108 safety-case documentation and commercial handoff.

## Technical Approach

**Year One (59% of budget)** focuses on development and hardware maturation:
- Build out simulation infrastructure (SwiftSim alpha → v1.0 with SWIL, Monte Carlo, HWIL capability)
- Develop real-time autonomy kit specification and reference implementation (SwiftCore RTA Kit v0.1 → v1.0)
- Design and prototype custom autopilot board (requirements → schematic → 2 prototype boards)
- Conduct controller validation via simulation (EMASS sim-validated controller revision)
- Accumulate supervised autonomy flight hours (target: ≥10 hours by end Y1Q4)
- Build adversarial test corpus (1000+ test cases v1.0)

**Year Two (41% of budget)** transitions to validation and productization:
- Operationalize flight testing (20+ flight hours Y2Q2, 30+ by Y2Q3 to meet Objective 4)
- Integrate with customer systems (Genesis/BNL or substitute)
- Finalize deployment tools and security (SwiftDeploy v0.5 → v1.0 with signed binary CI/CD chain)
- Develop Part 108 safety case (outline → draft → final)
- Conduct adversarial override event validation (≥3 documented events)
- Document commercialization handoff to internal product line and Phase III customers

## Products & Capabilities Described

### SwiftSim
- **What it is:** Simulation and validation framework
- **Evolution:** Alpha (SWIL only) → v0.5 (SWIL + Monte Carlo) → v1.0 (SWIL + HWIL + Monte Carlo)
- **Use:** Primary development and validation vehicle; supports software-in-the-loop testing and Monte Carlo analysis

### SwiftCore RTA Kit
- **What it is:** Real-time autonomy development kit
- **Evolution:** Specification draft → v0.1 (header library + reference implementation) → v1.0
- **Use:** Standard interface for autonomous flight control; enables multi-airframe, multi-layer autonomy

### SwiftDeploy
- **What it is:** Deployment and productization tool
- **Evolution:** v0.5 (signed binary CI/CD chain) → v1.0
- **Use:** Secure binary delivery and integration for commercial customers; includes CI/CD automation

### Custom Autopilot Board
- **Specification:** Requirements spec, schematic design, prototype fabrication (2 boards)
- **Use:** Hardware-in-the-loop integration and validation; enables embedded deployment

### EMASS Controller
- **What it is:** Simulation-validated flight controller
- **Milestones:** Sim-validated revision (Y1Q2), HWIL integration (Y1Q3), Phase II flights (extended hover Y2Q1, dynamic pattern Y2Q2)

### S2
- **Use:** Multi-layer multi-airframe flight testing platform; PID auto-tuning demonstration in Y1Q3

## Use Cases & Applications

- **Multi-airframe autonomy:** Supervised autonomy demonstrations across different platforms
- **Terrain-following missions:** Q5 campaign mentioned in budget guidance
- **PID auto-tuning:** S2 platform demonstration (Y1Q3), cross-airframe scaling (Y2Q2)
- **Customer integration:** Genesis or BNL collaboration (Y2Q1 onwards)
- **ADONIS case study:** Finalized in Y2Q2
- **Adversarial testing:** Validation of autonomous override events; ≥3 documented events by Y2Q3

## Key Milestones & Results

### Year One
| Quarter | Key Achievements |
|---------|-----------------|
| Y1Q1 | SwiftCore RTA Kit spec draft; SwiftSim alpha; custom-board requirements; first SBC selection |
| Y1Q2 | SwiftCore RTA Kit v0.1; SwiftSim v0.5 with Monte Carlo; custom-board schematic; EMASS controller revision |
| Y1Q3 | 2 custom-board prototypes fabricated; S2 PID auto-tuning flight; EMASS HWIL milestone; adversarial corpus v1.0 (1000+ cases) |
| Y1Q4 | SwiftSim v1.0; ≥10 supervised autonomy flight hours; first EMASS Phase II flight (extended hover); mid-program NASA review |

### Year Two
| Quarter | Key Achievements |
|---------|-----------------|
| Y2Q1 | SwiftDeploy v0.5; Genesis/BNL integration begins; Part 108 safety-case outline; second EMASS flight series (dynamic pattern) |
| Y2Q2 | Custom-board HWIL integration complete; ≥20 total flight hours; ADONIS case study finalized; SwiftCore RTA Kit v1.0 |
| Y2Q3 | ≥30 total flight hours (Objective 4 met); SwiftDeploy v1.0; ≥3 adversarial override events documented; Part 108 draft for internal review |
| Y2Q4 | Final Phase II report; Part 108 safety case finalized (Objective 6 met); SwiftDeploy security review; Phase III commercialization roadmap; TABA final deliverable |

## Budget Summary

| Period | Amount | Profile |
|--------|--------|---------|
| Year 1 | $687,838 | 59% (development-heavy) |
| Year 2 | $479,851 | 41% (operations-heavy) |
| **Total Phase II** | **~$1.168M** | |

**Quarterly Breakdown:**
- Y1Q1: $165,000K (foundation, labor-dominant)
- Y1Q2: $205,000K (highest engineering intensity; concurrent Tasks 1, 2, 4)
- Y1Q3: $185,000K (most hardware-intensive; PCB/fabrication peak)
- Y1Q4: $132,838K (transition to flight operations)
- Y2Q1: $135,000K (operational demonstration ramp)
- Y2Q2: $140,000K (peak flight-test validation tempo)
- Y2Q3: $110,000K (documentation and safety-case intensive)
- Y2Q4: $94,851K (commercialization focus)

## Notable Details

- **TRL Target:** Program concludes at TRL 7
- **Flight Hour Thresholds:** 10+ (Y1Q4) → 20+ (Y2Q2) → 30+ (Y2Q3, objective-tied)
- **Regulatory Alignment:** FAA Part 108 safety case generation and finalization with documented commercialization handoff
- **Hardware Development:** SBC down-selection in Y1Q1; custom-board fabrication peak in Y1Q3; HWIL integration by Y2Q2
- **Adversarial Validation:** 1000+ test corpus cases built in Y1Q3; ≥3 override events documented by Y2Q3
- **Customer Transition:** Genesis/BNL integration begins Y2Q1; Phase III customer handoff in Y2Q4
- **Spend Profile Rationale:** Year 1 weighted toward R&D and prototyping; Year 2 weighted toward operations, validation, and productization
- **Concurrent Development:** Multiple tasks (Tasks 1, 2, 4) run in parallel during Y1Q2, the highest engineering intensity period