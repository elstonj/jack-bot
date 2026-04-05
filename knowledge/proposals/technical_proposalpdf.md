# PrecisionTerra NASA SBIR Phase 1 Technical Proposal

## Document Metadata
- Type: NASA SBIR Phase 1 Technical Proposal
- Client/Agency: NASA Aeronautics Research Mission Directorate (ARMD)
- Program/Solicitation: NASA SBIR Subtopic A3.02 (Positioning, Navigation and Timing for Wildfire Management)
- Proposal Number: A3.02-1042
- Date: 2026-02-12 (submission date)
- Key Personnel: Maithreyi Gopalakrishnan (PI/CEO), Dr. Dmitriy Zusin, Benon Gattis, Dr. Jade Morton (Technical Advisor)

## Executive Summary
PrecisionTerra proposes to develop and validate a software-based positioning, navigation, and timing (PNT) solution for reliable GPS operation in degraded environments, specifically targeting wildfire mitigation operations using small unmanned aircraft systems (sUAS). The solution leverages patented Adaptive Joint Tracking (AJT) IP licensed from University of Colorado-Boulder and aims to improve GPS signal tracking by 6-30x over current methods in GPS-degraded conditions.

## Technical Approach

### Core Innovation: Adaptive Joint Tracking (AJT)
PrecisionTerra's proprietary signal processing technology addresses the fundamental problem that GPS signals degrade differently across multiple frequencies in challenging environments (mountains, canyons, forests, fire/smoke).

**Key Technical Insight:**
- GPS broadcast frequencies (L1, L2, L5) have carrier phase, Doppler frequency, and Doppler rate that are proportional to the fundamental carrier frequency
- Signal strength (dB-Hz) is NOT proportional and degrades differently for each frequency
- Current receivers use "Single-Frequency Tracking" (independent tracking per frequency) or "Joint Tracking" (weighted averaging)

**AJT Method:**
- Adaptively switches between Single-Frequency Tracking and Joint Tracking based on real-time signal strength thresholds for each frequency
- Reduces tracking jitter (tracking error) by using state estimation with state vectors of carrier phase, Doppler frequency, and Doppler rate
- Most effective in frequency-selective degradation environments (wildfire conditions with differential smoke/fire impact on frequencies)

**Performance Claims (Simulation Results):**
- Dual-frequency tracking example: When L1 fixed at 45 dB-Hz and L5 at 15 dB-Hz:
  - Single-Frequency Tracking: ~50° tracking jitter (non-trackable)
  - Joint Tracking: ~10° tracking jitter
  - AJT: ~1.5° tracking jitter (6.6x improvement over Joint Tracking, 33.3x over Single-Frequency)
- Overall range: 6-30x improvement over current methods when one frequency weakens beyond 25 dB-Hz

### Intellectual Property
- **Patent:** US20220276393A1 (granted October 2024), 20 distinct claims
- **Developer:** Dr. Jade Morton (CU-Boulder Aerospace Engineering professor, 40+ years GNSS experience)
- **Status:** PrecisionTerra in late stages of obtaining exclusive license for all fields of use

### Full Product Architecture
PrecisionTerra's software-defined signal processor includes:

1. **Signal Acquisition** - Correlation techniques to acquire L1 and L5 GPS signals (L2 planned for roadmap)
2. **Signal Tracking** - Code phase and carrier phase tracking in feedback loops
   - AJT applied at carrier phase tracking stage (purple blocks in pipeline)
3. **Navigation Solution** - Calculates x, y, z positions from pseudorange, carrier phase, Doppler frequency
   - Currently at TRL 4, targeting TRL 6 with Phase 1 completion

**Current Status:**
- Code developed and tested for all blocks except navigation solution
- Components integrated
- Navigation solution design/implementation to occur during Phase 1

## Products & Capabilities Described

### PrecisionTerra Software-Defined Signal Processor
- **What it is:** Software-based GNSS signal processor implementing AJT carrier phase tracking algorithm
- **Current capabilities:** L1 and L5 GPS signal processing
- **Planned additions:** L2 GPS signal processing
- **Key advantage:** First known software-defined signal processor capable of jointly tracking multiple GPS frequencies in fully software environment
- **Technology readiness:** TRL 4 at proposal time; will reach TRL 6 with Phase 1 completion

### Comparison to State-of-the-Art
- **RTK/PPP methods:** Complementary techniques that improve accuracy AFTER signal acquisition; do not address tracking problem
- **Standard tracking:** Code phase and carrier phase tracked in parallel (industry standard)
- **AJT differentiation:** No known commercial GPS receiver currently uses adaptive joint multi-frequency tracking like AJT
- **Estimated advantage:** 5-10x improvement over state-of-the-art tracking in commercial-grade receivers (requires validation)

## Use Cases & Applications

### Primary Use Case: Wildfire Mitigation
**Application:** sUAS operations in GPS-degraded wildfire environments for:
- Supply delivery
- Water/fire suppressant drops
- Emergency response

**Environment Types:**
- Mountainous areas (Boulder Flatirons, Rocky Mountains, San Juan Mountains, Tenmile Range)
- Canyons (Glenwood, Black, Eldorado, Poudre Canyons)
- Dense forests (Roosevelt, Uncompaghre, San Isabel, Gunnison National Forests)

**Why Relevant:**
- Wildfires occur in GPS-degraded environments
- Fire, smoke, and rapidly changing landscape exacerbate signal interference
- Frequency-selective degradation (fire/smoke impact different frequencies differently) is ideal for AJT
- Minimal payload requirement necessary for sUAS integration
- Time-critical response requires low-latency PNT solution

### Secondary Market Opportunities (from Related Work)
- **LEO satellite navigation:** DoD partnership with NAL Research to track Low-Earth Orbit satellite signals
- **Ionospheric scintillation mitigation:** Dr. Morton's lab research on mitigating LEO carrier frequency effects
- **Multipath interference reduction:** Code phase tracking approaches in development

## Technical Objectives & Validation Plan

### Key Questions to Answer
1. What is absolute and relative performance of AJT in GPS-degraded, wildfire-prone Colorado environments?
2. How does PrecisionTerra's solution compare to commercial-grade receivers (uBlox)?
3. What is the latency of PrecisionTerra's signal processor vs. commercial alternatives?

### Four Technical Objectives with Deliverables

**O1: Data Collection (Weeks 1-4)**
- **Objective:** Collect positioning data from GPS front-end devices, uBlox receivers, and IMU in relevant wildfire environments
- **Deliverables:** 7 datasets per location (3 raw streams from front-end devices, 3 uBlox datasets, 1 IMU reference) × 4 locations
- **Locations:** 12 datasets across Colorado canyons, mountains, forests
- **Technical Risk Mitigation:** 
  - Use 3 identical units of each receiver type to handle equipment malfunction
  - Stack receivers to maintain identical x-y positions; minimize z-height uncertainty
  - Moving vehicle testing (not UAS due to cost; UAS would be $25K+)
- **Personnel:** Maithreyi Gopalakrishnan (60 hrs), TBA Signal Processing Engineer (60 hrs)

**O2: Tracking Performance Comparison (Weeks 5-10)**
- **Objective:** Compare AJT tracking performance vs. uBlox receiver in each GPS-degraded environment
- **Deliverables:** Statistical analysis of tracking jitter (tracking error) for AJT vs. uBlox across all locations
- **Benchmark:** uBlox receivers commonly used in commercial UASs; uBlox is industry standard for comparison
- **Critical Risk:** If AJT underperforms, commercial pathways must be reevaluated; if outperforms significantly, opens DoD/commercial pilot opportunities
- **Personnel:** Maithreyi Gopalakrishnan (90 hrs), TBA Signal Processing Engineer (90 hrs), Dmitriy Zusin (30 hrs)

**O3: Positioning Accuracy Evaluation (Weeks 11-22)**
- **Objective:** Determine if AJT yields better positioning accuracy than uBlox vs. baseline IMU truth data
- **Sub-Tasks:**
  - **T5 (11-15 weeks):** Design/implement navigation solution for AJT software (160 hrs Maithreyi, 120 hrs TBA, 60 hrs Zusin, 120 hrs Gattis)
  - **T6 (16-17 weeks):** Calculate x, y, z positions for all datasets through PrecisionTerra's nav solution (120 hrs total)
  - **T7 (18-22 weeks):** Statistical analysis comparing mean/std dev of PrecisionTerra vs. uBlox vs. IMU ground truth (288 hrs total)
- **Deliverables:** Position accuracy comparison, mean/std dev analysis by location and time-of-day
- **Technical Risk Mitigation:** Collect multiple datasets from same location at different times/days to reduce uncertainty; characterize accuracy by operating environment, not in general
- **Critical Importance:** Positioning accuracy is essential for UAS operations (water drops, supply delivery precision)

**O4: Latency Analysis (Weeks 23-26)**
- **Objective:** Compare latency of AJT software processor vs. uBlox hardware receiver
- **Sub-Tasks:**
  - **T8 (23-24 weeks):** Optimize PrecisionTerra software for latency (150 hrs)
  - **T9 (25-26 weeks):** Measure execution time per processing block vs. uBlox (120 hrs)
- **Deliverables:** Latency comparison analysis with bottleneck identification
- **Expected Outcome:** Unlikely to beat hardware speed, but quantify overhead for viability assessment
- **Technical Risk:** May reveal unacceptable latency; mitigation involves step-by-step bottleneck analysis and alternate solution exploration
- **Importance for UAS:** Time-critical wildfire response requires acceptable latency

## Key Results (Baseline/Expected)

### Simulation Results (Already Demonstrated)
- **L1-L2-L5 triple-frequency tracking:** AJT shows significant improvements in tracking jitter across signal strength variations
- **Dual-frequency example:** 33.3x improvement over Single-Frequency Tracking, 6.6x over Joint Tracking when signal severely degraded
- **Performance envelope:** 6-30x improvement dependent on frequency combinations and relative signal strengths

### Validation Gap
- Simulation results promising but must be validated in:
  - Real GPS-degraded environments (fire, smoke, terrain)
  - Comparison against commercial receivers in field conditions
  - Actual UAS integration scenarios
- Phase 1 project designed to close this gap

## Notable Details

### Intellectual Property Strategy
- **Exclusive license:** In late stages; 20 distinct patent claims provide strong differentiation
- **Developer affiliation:** Dr. Jade Morton frequently collaborates with leading receiver manufacturers, suggesting AJT approach is likely novel in commercial space

### Team Composition
- **Principal Investigator:** Maithreyi Gopalakrishnan (CEO/Founder)
  - B.S./M.S. Engineering Physics (CU-Boulder 2016), M.S. Management Science (Stanford 2020)
  - Background: Intel process engineer, consulting, research experience at SLAC and MIT Lincoln Lab
  - 30-35 hours/week commitment (760 hours total)
  - Optics/signal processing background with electrical engineering minor
  
- **Signal Processing Research Scientist:** Dr. Dmitriy Zusin
  - PhD Physics (CU-Boulder 2018), developed PrecisionTerra's software-defined signal processor
  - Prior: Data scientist at HD mapping company, computational electromagnetics at KLA
  - Part-time role (contractual commitment elsewhere)

- **Signal Processing Engineer:** Benon Gattis
  - PhD Candidate, Aerospace Engineering (expected graduation May 2027)
  - GPS data processing expertise, RFI detection research, multi-sensor solutions
  - Publications at ION GNSS+ 2024 and 2022
  - Part-time role (doctoral commitments)

- **To Be Announced (TBA):** Full-time Signal Processing Engineer (hiring underway)
  - Desired qualifications: PhD in GNSS or RF signal processing
  - Required: High-performance, low-latency signal processing code (Python/C++)