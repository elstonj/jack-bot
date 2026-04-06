# BlkSwft_Dynexus iRIS JDA DRAFT

## Document Metadata
- Type: Presentation (Joint Development & Testing proposal)
- Client/Agency: Internal presentation (potential NASA collaboration implied by folder location)
- Program/Solicitation: NASA 2017 SBIR Phase II+
- Date: October 15, 2018 (presentation date); created/modified October 23, 2018
- BST Products/Systems Referenced: None directly (this is a Dynexus Technology presentation to BST)
- Key Personnel: David Sorum (Dynexus CEO), Dave Lung (Dynexus CPO), Dr. Jon Christophersen (Dynexus Chief Scientist); Jack Elston (BST—last editor)

## Executive Summary
Dynexus Technology presents iRIS (Rapid Wideband Electrical Impedance Spectroscopy), a patented battery monitoring technology that enables State of Stability (SOS) diagnostics and prognostics for lithium-ion batteries in near real-time. BST is being approached for a potential joint development and testing agreement to integrate iRIS technology onto small drone platforms, with a phased approach beginning with a 6-month technology assessment.

## Technical Approach

**iRIS Core Technology:**
- Patented field-deployable implementation of Electrical Impedance Spectroscopy (EIS)
- Active wideband AC signal excitation (0.1 Hz – 2 kHz frequency range)
- Rapid continuous monitoring capability at 10-second intervals
- Effective for online (under-load) and offline battery monitoring
- Produces 2 kB of data per scan; ~5 MB per day operation

**Measurement Capabilities:**
The technology measures:
- State of Charge (SOC)
- State of Health (SOH) with enhanced degradation tracking
- **State of Stability (SOS)** — battery health, aging, and safety characteristics (key differentiator)
- Remaining Useful Life (RUL) prediction
- End of Life (EOL) prediction
- Catastrophic event prediction (short-circuit, thermal runaway)

**Competitive Advantages over Existing Methods:**
- OCV (Open Circuit Voltage): Accumulates errors with capacity fade
- Coulomb Counting: Accumulates errors with capacity fade
- Single-frequency AC impedance: Requires periodic offline recalibration
- TI Impedance Track: Uses DC resistance (IR drop) but limited to SOC/capacity
- **iRIS:** Active, rapid, under-load capable; enables predictive safety assessment

**National Lab Validation:**
- Idaho National Laboratory (INL): State of Health, degradation, RUL prediction
- Sandia National Laboratory: State of Stability, battery abuse characterization, short-circuit/thermal runaway prediction

## Products & Capabilities Described

**iRIS System (Current & Roadmap)**

*Today – "Black Box" Configuration:*
- Sales price: $5k–$25k + tech support
- Target market: Stationary/UPS/Grid applications
- Full external monitoring system

*1 Year – Single Board Device:*
- Sales price: $100–$500 + software license
- Target market: e-Mobility (electric vehicles, presumably small drones)
- Reduced form factor

*2–3 Years – Integrated Circuit:*
- Sales price: TBD
- Target market: Consumer electronics
- Fully integrated chip-level implementation

**Proposed Demo Systems for Phase I:**
- iRIS-G2 system: Baseline EIS assessment and battery health signature mapping
- iRIS-G3 Ultra High-Res system: Advanced battery analytics (aging, safety/abuse, reuse signatures)

**Software/Platform Architecture:**
- iRIS-OS: Embedded software layer
- EIS via HCSD (High-Current Source Driver)
- Cloud analytics platform with AI/machine learning
- Service health management and security management modules
- Reporting and data science capabilities

## Use Cases & Applications

**Primary Proposed Application (for this JDA):**
- Small drone platform integration
- Battery safety requirements assessment for drone battery modules and packs
- Onboard vs. offboard battery monitoring exploration

**Other Potential Use Cases (mentioned):**
- Internal defect detection/characterization
- Fast charging safety and optimization
- Counterfeit battery detection
- Battery reuse assessment
- Battery cybersecurity intrusion detection

## Key Results
Not applicable—this is a proposal presentation, not a report with results. However, it references:
- Sandia National Laboratory 2017 e-Vehicle Battery Safety Study for US DOT NHTSA endorsement of rapid impedance spectrum sensors for Li-ion safety
- Dr. Christophersen received R&D 100 Award (2011) for Impedance Measurement Box innovation
- Multiple patents and peer-reviewed publications cited (not detailed)

## Joint Development & Testing Agreement Framework

**Phase I (6 months: November 2018 – April 2019)**
- iRIS Rapid Impedance Technology Assessment
- iRIS Concept Study for Small Drone Platforms
- EIS-based Battery Safety Requirements & Assessment for drone battery modules/packs
- Initial iRIS Evaluation & Characterization Testing
- Recommend procurement of 2 iRIS Demo Systems (@$25k each)
- EIS-based battery analytics with AI/machine learning development
- Explore box/board-level applications (onboard vs. offboard)
- Tech support: TBD engineering hours and travel from Dynexus

**Proposed Dynexus Participants:**
- Dr. Jon Christophersen (Chief Scientist)
- Paul Boerger / Dan Haas (iRIS System Development Engineering)
- David Lung (Chief Product Officer)
- Supporting resources: University of Montana, Idaho National Laboratory, Sandia National Laboratory, University of Maryland

## Notable Details

1. **Dynexus–BST Relationship:** This presentation is being made TO Black Swift (implied by Jack Elston's editorial involvement and folder location in BST's NASA SBIR project archive). Dynexus is seeking a joint development partnership with BST, likely to apply iRIS to BST's drone platforms.

2. **Technology Maturity:** iRIS has been validated by two national laboratories (INL, Sandia), providing significant credibility. The presentation explicitly references positive assessment from Sandia's DOT/NHTSA battery safety work.

3. **Commercialization Strategy:** Clear roadmap from lab/specialized equipment ($5k–$25k) → mobile/e-mobility form factor ($100–$500) → mass-market IC integration.

4. **Dr. Christophersen's Pedigree:** Former INL senior research engineer (2000–2015), technical lead for INL Battery Test Center (world leader in advanced energy storage testing). R&D 100 Award winner. Primary inventor of iRIS technology. High credibility for battery diagnostics.

5. **Cost & Data Profile:** Modest data footprint (~5 MB/day) makes it feasible for drone transmission; rapid 10-second scan intervals enable real-time operational safety monitoring.

6. **Potential BST Application:** Given BST's focus on small UAS platforms, iRIS integration would enable autonomous battery health/safety monitoring for extended operations (arctic, volcanic, hurricane sampling)—addressing a critical operational constraint of battery-powered drones.