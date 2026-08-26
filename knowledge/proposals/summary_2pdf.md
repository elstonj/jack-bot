# AI-Enabled Mobile Autonomous Laboratories for Real-Time Adaptive Experimentation in Dynamic Environmental Systems (Genesis Mission Phase I)

## Document Metadata
- **Type:** SBIR Phase I Proposal
- **Client/Agency:** U.S. Department of Energy (DOE), Office of Science (ASCR)
- **Program/Solicitation:** RFA Number DE-FOA-0003612; Challenge Focus Area 11 - "Achieving AI-Driven Autonomous Laboratories"; Topic A - "Advanced Robotics for Dynamic Laboratory Environments"
- **Date:** 2026 (submission date August 21, 2026)
- **BST Products/Systems Referenced:** AI-guided autonomous uncrewed aerial systems (UAS)
- **Key Personnel:** 
  - Principal Investigator: Dr. Jack Elston (Black Swift Technologies)
  - Co-Investigator: Dr. Gijs DeBoer (Brookhaven National Laboratory)
  - Last Editor: Beck Cotter

## Executive Summary
This proposal presents a framework for scientific discovery that tightly couples artificial intelligence, autonomous sensing, and physics-based modeling in a closed-loop system. Rather than treating data collection and analysis separately, the approach enables adaptive, decision-driven observing where sensing strategies are continuously optimized based on evolving system knowledge and quantified uncertainty. The Phase I demonstration targets atmospheric boundary layer characterization using AI-guided UAS platforms that implement closed-loop sampling strategies and adapt measurement locations in real time.

## Technical Approach

### Core Framework
- **Closed-Loop Architecture:** Integrates machine learning, uncertainty quantification, and model-informed inference to create robotic platforms that efficiently interrogate complex, multiscale phenomena
- **Three-Layer System Architecture:**
  1. **Inference Layer:** Updates calibrated posterior belief over local atmospheric profiles and hidden planetary boundary-layer height (PBLH) interface using physics-constrained probabilistic digital twin
  2. **Decision Layer:** Scores feasible waypoint or short-trajectory primitives by predicted uncertainty reduction
  3. **Search-to-Track Layer:** Switches from exploration to MPC-style (model predictive control) interface-following once posterior indicates sufficient localization

### Three Key Development Efforts
1. **Physics-Constrained Probabilistic Digital Twin:** 
   - Uses interpretable profile variables augmented with learned residual/context states
   - Employs lightweight set/attention encoders for assimilating sparse, irregular observations
   - Infers PBLH from UAS path measurements

2. **Uncertainty-Aware Adaptive Sensing Module:**
   - Performs greedy receding-horizon scoring of feasible trajectory primitives
   - Operates under flight-time, energy, and safety constraints
   - Prioritizes information-rich regions

3. **Search-to-Track Integration:**
   - Integration in simulation/replay
   - Hardware-in-the-loop testing as stretch activity
   - Performance evaluation against fixed, human-designed, and ablated adaptive baselines

### Operational Loop
Streaming observations update belief state → belief state defines uncertainty in hidden interface → uncertainty determines next measurement

## Products & Capabilities Described

### AI-Guided Autonomous UAS
- **What it is:** Uncrewed aerial systems equipped with closed-loop sampling capability and real-time adaptive measurement location selection
- **How used:** Implements adaptive decision-driven observing to characterize atmospheric processes with transient, spatially heterogeneous features
- **Key capability:** Converts sparse, irregular path measurements into calibrated online belief state over hidden atmospheric interface and uses that uncertainty to guide robotic action

### Physics-Constrained Probabilistic Digital Twin
- **What it is:** A model combining interpretable atmospheric profile variables with learned residual states and attention mechanisms
- **How used:** Performs real-time inference and localization of PBLH interface from sparse UAS measurements
- **Key benefit:** Enables uncertainty quantification and Bayesian updating as new observations arrive

## Use Cases & Applications

### Primary Application: Planetary Boundary Layer Height (PBLH) Characterization
- **Challenge Addressed:** Fixed or pre-programmed observations fail to resolve sharp gradients in thermodynamic variables that govern transport, mixing, and dispersion
- **Solution:** AI-guided UAS maps spatiotemporal structure of PBLH interface by:
  - Identifying and localizing PBLH interface in real time
  - Tracking interface as environmental conditions evolve
  - Prioritizing information-rich regions and responding to environmental variability

### Broader DOE-Relevant Domains
The framework is positioned as generalizable to observe other dynamic atmospheric processes and complex, data-limited systems

## Success Metrics (Phase I Targets)
- **Resource Efficiency:** At least 20% reduction in sensing resources compared to baseline
- **Accuracy Improvement:** At least 10% improvement at equal sensing budget
- **Inference Latency:** Inference-plus-scoring cycles below 5 seconds in reduced benchmark
- **Calibration:** Uncertainty calibration validation
- **Ablation Studies:** Quantitative assessment of component contributions
- **Metric Categories:** Resource-to-localization, accuracy-at-budget, uncertainty calibration, real-time latency

## Deliverables
- Benchmark datasets
- Trained models
- Evaluation scripts
- Reusable workflow artifacts
- Preparation for alignment with Genesis Mission evaluation practices and AmSC/ModCon-compatible infrastructure hosting

## Notable Details
- **Partnership:** Collaboration with Brookhaven National Laboratory (Dr. Gijs DeBoer, Co-I)
- **Distinction:** Positions closed-loop adaptive sensing as novel paradigm shift from traditional fixed observation strategies
- **Hardware-in-Loop:** Full hardware integration planned as stretch activity, indicating feasibility demonstration is secondary to algorithm development in Phase I
- **Reusability:** Emphasis on creating general-purpose tools and datasets for broader AI-driven laboratory automation community
- **Evaluation Framework:** Explicit alignment with DOE's Genesis Mission evaluation standards suggests awareness of broader program context and commitment to compatibility with federal research infrastructure