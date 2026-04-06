# Nighttime Fire Observations eXperiment (NightFOX) - UAS Wildfire Measurements in Support of FIREX and Fire Weather Forecasting

## Document Metadata
- **Type:** NOAA UAS RFP Proposal (draft)
- **Client/Agency:** NOAA Earth System Research Laboratory (ESRL), Chemical Sciences Division
- **Program/Solicitation:** FY17 NOAA UAS RFP; addresses RFP Objectives #3 (long-endurance fixed-wing UAS observing strategies) and #5 (UAS payload evaluation, testing, calibration, validation)
- **Date:** March 15, 2017 (draft); modified August 31, 2017
- **BST Products/Systems Referenced:** SuperSwift UAS
- **Key Personnel:** 
  - Ru-Shan Gao (PI, ESRL/CSD) – Team lead, instrument development
  - Karen H. Rosenlof (CoI, ESRL/CSD) – Flight planning, modeling
  - Troy Thornberry (CoI, ESRL/CSD affiliate via CIRES) – Instrument development, field deployment coordination
  - Brian Argrow (CoI, University of Colorado, Dept. Aerospace Engineering Sciences) – UAS operations, flight permits, airspace access
  - Sher Schranz (CoI, ESRL/GSD affiliate via CIRA) – Fire weather modeling

## Executive Summary
NightFOX proposes to design, integrate, and validate two lightweight instrument packages (one for in situ fire plume sampling, one for remote fire observations) on a Black Swift Technologies SuperSwift UAS to enable nighttime wildfire emissions and perimeter measurements—a critical data gap left unfilled by manned aircraft due to safety constraints. The system will be field-deployed during NOAA's planned FIREX field mission (July-September 2019) to improve fire weather forecasting and support air quality and climate research on wildfire impacts.

## Technical Approach

### Overall Strategy
- **Platform:** SuperSwift UAS (5 lb payload capacity) operated by University of Colorado Research and Engineering Center for Unmanned Vehicles (CU RECUV)
- **Two integrated instrument packages:**
  1. **In situ package:** CO₂, CO, aerosol (fine and coarse modes), relative humidity (RH), temperature (T), pressure (p); winds derived from UAS avionics
  2. **Remote-sensing package:** Visible and infrared imagers, thermal imager, single-element mid-infrared (MIR, ~4 µm) fire radiative power (FRP) sensor(s), ambient RH/T/p sensors

### In Situ Payload Development
- Target 1-second response time (critical for spatial resolution; at 20 m/s cruise speed, 25-s response time = 0.5 km spatial resolution)
- Candidate CO₂/CO sensors to be identified and tested; modifications planned to improve response time
- Fine-mode aerosol sensor already developed by team; iMet sensors for RH/T/p
- If commercial sensors prove inadequate, custom solutions will be developed

### Remote-Sensing Payload Development
- **Challenge identified:** Long-wavelength IR (LWIR, 7-14 µm) thermal imagers saturate at fire temperatures; mid-infrared (MIR, 4 µm) imagers ideal for FRP but costly and bulky
- **Solution:** Single-element 4 µm MIR sensors (small, low-cost) for FRP determination with cross-track scanning; lightweight visible camera and thermal imager for spatial context
- Target package cost: $15-20K
- Laboratory calibration of remote-sensing sensors; validation through satellite data comparison

### Integration & Testing
- Data recorded onboard; small subset transmitted real-time for monitoring and decision-making
- Multiple test flights planned in Year 2; field deployment to prescribed burn opportunities
- FIREX mission deployment: UAS based next to Aerodyne mobile lab; 2-4 sorties per night; target 30-60 flight hours over ~15 nights; minimum 20 hours needed to meet objectives

### Flight Operations
- Hand-launched, lands on paved road
- Two pilots per deployment
- Extended FAA Certificates of Authorization (COA) sought for nighttime BLOS (beyond line-of-sight) operations
- Coordination with FAA, Department of Interior, USFS for airspace access

## Products & Capabilities Described

### SuperSwift UAS
- **Specifications:**
  - 5 lb payload capacity
  - ~20 m/s cruise speed
  - Operational radius: 30-60 km (depending on flight strategy)
  - Capable of >2 hour endurance
  - Hand-launched; lands on paved road
  
- **Key advantages for this application:**
  - Spacious, forward-located, modular nose-cone payload bay enabling atmospheric sampling and rapid payload exchange
  - Inexpensive nose cones allow easy instrument integration
  - Electric motor (not air-breathing), eliminates concerns about engine damage from dense fire plumes
  - Inherently suited to nighttime/BLOS operations (beyond line-of-sight)
  
- **Selection rationale:** Compared to alternatives (Tempest/UASUSA, Penguin BE/UAV Factory, Puma AE/AeroVironment), SuperSwift offers:
  - Lower cost
  - Modular payload bay (competitors lack this)
  - Rear-mounted propeller (cleaner for ambient sampling than nose-propeller designs)
  - Minimal launch/recovery overhead
  
- **Current readiness level:** RL 4 (test flown); target RL 8 (operational) by project end

### In Situ Instrument Package
- **Measurements:** CO₂, CO, aerosol (fine & coarse), RH, T, p, winds (from avionics)
- **Readiness level:** RL 3 (feasible; ~30% of sensors identified) → RL 8
- **Technical innovations:** 
  - 1-second response time (vs. standard 10-60 s for commercial sensors)
  - Modification of commercial solid-state sensors as alternative to custom builds
- **Status:** Candidate CO₂/CO/coarse aerosol sensors already identified; fine-mode aerosol sensor developed; iMet sensors for RH/T/p identified

### Remote-Sensing Instrument Package
- **Measurements:** Fire radiative power (FRP), fire perimeter, ambient RH/T/p
- **Readiness level:** RL 3 (feasible) → RL 8
- **Technical approach:**
  - Single-element 4 µm MIR sensors for FRP (small, low-cost, avoids saturation issues of LWIR thermal imagers)
  - Cross-track scanning to improve spatial resolution
  - Visible and thermal imagers for contextual mapping
- **Target cost:** $15-20K per package
- **Status:** Candidate visible, IR, thermal imagers and MIR FRP sensors identified

### UAS Observation System (UASOS)
- Integration of SuperSwift + dual instrument packages + flight planning + data assimilation into fire weather models
- **Readiness level:** RL 2 (concept formed) → RL 8
- **Deliverables:** 
  - Proven nighttime observation system with ambient wind data capability
  - Sampling strategies for in situ and remote-sensing flights (Figure 1 shows basic flight patterns)
  - Data ingestion protocols for WRF-Sfire fire weather model

### Observation Strategies
- **Readiness level:** RL 3 (feasible) → RL 8
- Two distinct flight patterns: in situ (plunge through/sampling) vs. remote-sensing (hovering/scanning over fire)
- Development led by Karen Rosenlof and Brian Argrow, beginning Year 1
- Coordination with FAA, DoI, USFS on flight permission requirements

## Use Cases & Applications

### Primary Mission: FIREX Field Campaign (2019)
- **Context:** NOAA's Fire Influence on Regional and Global Environments (FIREX) mission planned July-September 2019; coordinates with NASA FIREChem and USDA/DoI FASMEE
- **Critical gap filled by NightFOX:** Nighttime fire measurements impossible with manned aircraft due to safety concerns; fire plumes more concentrated at night (lower boundary layer), worse air quality, but no current observing capability
- **Scientific objectives:**
  - Study wildfire emissions and chemical transformations
  - Measure fire plume distributions and perimeter
  - Characterize nighttime fire emissions and plume characteristics
  - Provide data for air quality and fire weather forecasting
  - Support land management decisions

### Secondary Applications (Mentioned)
- **Oil and gas field flares:** SuperSwift proposed for calibration/validation of satellite measurements of flare FRP
- **Future capability:** Swarming (coordinated multi-UAS network) for continuous high-resolution spatial information

### Fire Weather Modeling Integration
- Data assimilation into WRF-Sfire model
- Incorporation of high-resolution nighttime fire perimeter, spatially resolved FRP, and ambient RH/p/T/wind measurements
- Expected outcome: Improved fire weather forecasts and air quality predictions

## Key Results (if applicable)
This is a proposal document, not a final report. No results are presented. However, explicit success criteria are established:

### Final Acceptance Criteria:
1. **Two robust UAS instrument packages** demonstrating usefulness through favorable inter-comparison with established instruments
2. **Successful data-collection flights** >2 hours duration with UAS recovery and useful data return
3. **Successful incorporation of data** for improvement of fire weather forecasting

### Readiness Level Targets
All four elements (Platform, Payload, Observing System, Observation Strategy) expected to advance from RL 2-4 to **RL 8 (operational)** by project end.

### Year-Specific Milestones:
- **Year 1:** Sensor identification/acquisition; establish inter-agency relationships; begin observation strategy planning; begin data assimilation protocol development
- **Year 2:** Sensor testing/selection; payload design/construction; integration to SuperSwift; test flights; field deployment to prescribed burn; test model ingestion
- **Year 3:** Finalize payloads; FIREX field mission participation; incorporate data into forecast models; satellite data comparison; refine strategies

## Notable Details

### Project Scope & Alignment
- Addresses two RFP objectives: #3 (long-endurance fixed-wing UAS observing strategies) and #5 (payload evaluation/testing/calibration/validation)
- Supports NOAA Long-Term Goals:
  1. Improved understanding of changing climate and its impact
  2. Reduced loss of life/property from high-impact events
- Contributes to NOAA OAR mission: "advance understanding and prediction of the Earth System to enhance society's ability to make effective decisions"

### Budget & Resources
- **Total requested funding:** $447.1K over 3 years
  - Year 1: $94.3K
  - Year 2: $194.2K
  - Year 3: $158.6K
- **In-kind contributions:** $559.3K total (NOAA staff, CU expertise, existing assets)
- **Personnel effort:** PI and CoIs provide significant in-kind labor; Troy Thornberry (4 months/year) to be funded by grant

### Risk Mitigation Strategy
- **UAS purchase delays:** CU has backup platforms (Tempest, custom Mistral) available
- **UAS crash:** Two redundant instrument sets planned; backup UAS platforms available
- **Inadequate sensors:** Primary and secondary sensor options identified from project start
- **Instrument cost overrun:** CSD internal funds identified as backup source
- **Flight permits (HIGH RISK):** Early engagement with FAA, DoI; leverage Dr. Argrow's existing FAA relationships and COA experience
- **Key personnel loss (MODERATE-HIGH RISK):** All key personnel committed; replacements to be identified at project start

### Competitive Positioning
- **Unique capability gap:** "To our knowledge there is no such a system available, either inside NOAA or outside" for nighttime wildfire plume observations
- **SuperSwift advantages:** 
  - Modular nose-cone payload bay (competitors lack this)
  - Lower cost than Tempest, Penguin BE, Puma AE
  - Electric motor design (safer around dense fire plumes)
  - Suitable for future swarming applications
- **Instrument innovation:** Focus on reducing size/weight/power/cost while maintaining research