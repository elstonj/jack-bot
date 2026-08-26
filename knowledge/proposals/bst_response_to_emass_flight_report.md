# BST Response to EMASS Flight Report

## Document Metadata
- Type: Technical assessment and business analysis (email response with detailed report)
- Client/Agency: EMASS (external partner/collaborator)
- Program/Solicitation: Not specified; appears to be a collaborative flight control evaluation
- Date: 2026-08-20
- BST Products/Systems Referenced: BST AP (Autopilot), ECS-DOT (external flight controller under evaluation)
- Key Personnel: Daniel Prendergast (author/BST), Mark, Scott, Tom, Moe (recipients/EMASS team)

## Executive Summary
BST conducted a technical assessment of EMASS's ECS-DOT flight controller against BST's own autopilot system. While the ECS-DOT demonstrated marginal single-digit efficiency improvements during turns, these gains were solely attributable to higher airspeed—a capability easily replicated in modern flight controllers with minimal code changes. BST concluded that integrating ECS-DOT would impose unreasonable costs, time, and operational risk relative to its marginal technical benefits.

## Technical Approach
BST evaluated ECS-DOT through comparative flight testing, analyzing:
- Flight efficiency metrics across multiple flight patterns and loops
- Altitude hold quality and flight path repeatability
- Airspeed consistency and control performance
- Straight-line vs. turning flight segments

The assessment identified two key experimental flaws:
1. Controllers were not "speed-matched" during testing (0.5 m/s average difference)
2. Altitude waypoint definitions differed (ECS-DOT used constant MSL; BST AP used constant AGL)

## Products & Capabilities Described

### BST AP (Autopilot)
- Modern flight controller with terrain-following capability
- Can achieve equivalent or superior flight performance to ECS-DOT with proper airspeed management
- Requires only ~20 hours of engineering work to replicate ECS-DOT's efficiency gains
- Demonstrated superior path repeatability and control stability

### ECS-DOT (EMASS system under evaluation)
- Machine learning-based neural network flight controller
- Claims: Higher efficiency (+7.6%, +8.1% in testing), more consistent altitude hold, repeatable flight paths
- Actual performance: Single-digit improvements in turns only, achieved solely through higher airspeed during turns
- Reliability concerns: Majority of controllers failed to complete multiple pattern loops without failure
- Additional complexity: Added neural network SoC increases size, weight, power consumption

## Technical Findings

### Claims Analysis
**Claim #1: ECS-DOT achieves 7.6%-8.1% higher efficiency than speed-matched BST pair**
- **Response:** Controllers were not speed-matched; efficiency differences entirely attributable to 0.5 m/s airspeed variance
- **Evidence:** Figure 9 shows efficiency curves overlay when airspeed is matched
- **Corrected prediction:** If speed-matched on straight-line segments (mission-critical portions), overall improvements would be "significantly less than 7.6% and 8.1%"

**Claim #2: ECS-DOT more efficient at every corner on nearly every loop**
- **Response:** Turn efficiency improvements would be "significantly less than the 10.9% and 12.4%" shown in Figure 13 if straight-line speeds were matched
- **Bottom line:** Turns show single-digit improvements only due to higher airspeed

**Claim #3: ECS-DOT flies markedly more repeatable path**
- **Response:** Altitude consistency claim results from experimental flaw #2 (different waypoint altitude definitions)
- **Correction:** ECS-DOT actually demonstrates greater flight path variability in lateral and airspeed dimensions
- **Observation:** Visual trajectory analysis shows ECS-DOT "wavy portions" indicating less stable flight characteristics

## Cost-Benefit Analysis

### Costs of ECS-DOT Integration
- **Engineering effort:** ~200 hours (rough order of magnitude)
  - Collecting training data for ECS-DOT tuning
  - Hardware/software interface development
  - Integration and testing
- **Operational risk:** Significant—drone company must surrender flight control authority to ML-based system
  - Requires comprehensive safety architecture (flight control override and monitoring)
  - Few companies have existing safety infrastructure; BST benefited from prior NASA project work
- **Complexity penalty:** Neural network-based SoC adds complexity, size, weight, power with marginal benefit
- **Reliability risk:** ML controller failure rate (majority unable to complete test patterns) unacceptable for production systems

### Costs of Replicating ECS-DOT Behavior
- **Engineering effort:** ~20 hours
  - Implementing variable airspeed profiles for mission vs. non-mission segments
  - Simulation and flight testing
  - "Trivial software change" to existing BST AP
- **Risk profile:** Minimal—works within well-understood flight control domain
- **Safety:** No new safety architecture required

## Assessment of Machine Learning Approach

BST raised fundamental concerns about neural network suitability for low-level flight control:

**Why NNs are mismatched to this problem:**
- Flight control operates in well-understood physics domain with low variable count
- Classical control algorithms (PID controllers, etc.) are highly effective and efficient for this domain
- NNs provide value only in domains with unclear scientific principles and high variable complexity
- Document indicates this assessment was held from project inception

**Specific NN limitations in flight control:**
- Difficulty achieving reliable, safe training behavior
- Excessive complexity for simple airspeed variation task
- No inherent advantage over deterministic algorithms for trajectory control or stability

## Key Conclusions

### Technical Assessment
- With further refinement, ECS-DOT could match BST AP performance in airspeed, altitude, lateral path, orientation, and reliability
- No efficiency improvements beyond single-digit gains in turns
- All measured improvements solely from higher turn airspeeds
- ECS-DOT demonstrates greater flight path variability in practice

### Business Assessment
BST explicitly recommends **against** ECS-DOT integration:
> "Any modern flight controller allows easy speed control for efficient flight (either manually or with very minor code changes), replicating the airspeed profile and efficiency gains demonstrated by the ECS-DOT. As a potential client, I would not spend the time, money, and risk integrating ECS-DOT into my flight control system when I can achieve the same results with my existing controller at a very small fraction of the time, cost, and risk."

## Notable Details

- **Experimental rigor issues acknowledged:** Author notes flaws equally attributable to both organizations
- **Candid delivery:** Despite acknowledging EMASS investment in development, author provides direct negative assessment
- **Competitive positioning:** Document implicitly establishes BST's flight control capabilities as equivalent or superior to ML-based alternatives
- **Risk awareness:** Emphasis on operational safety and integration risk reflects production-oriented perspective
- **Technical maturity gap:** Reliability issues (controller failures) suggest ECS-DOT not ready for operational deployment
- **Domain expertise:** BST's prior NASA safety architecture work positioned them to evaluate integration risks better than typical drone manufacturers