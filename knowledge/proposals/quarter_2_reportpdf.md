# Quarter 2 Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- Type: Phase II Interim Report (Quarterly Progress Report)
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II, Contract NNX14CG09C
- Date: October 2014
- BST Products/Systems Referenced: SuperSwift (new airframe in development), S2/Tempest (existing platform), SwiftCore/SwiftPilot Pro (autopilot)
- Key Personnel: Jack Elston, Maciej (last name not provided), Cory (last name not provided), CET team members (Colorado Engineering and Technical Services)

## Executive Summary
This Q2 Phase II report documents BST's progress on developing an airborne soil moisture mapping system using a small unmanned aircraft (sUAS). Key accomplishments include detailed analysis and optimization of a 2x2 microstrip colinear antenna array for the Lobe Differencing Correlation Radiometer (LDCR), ground testing of the LDCR Build01 prototype, preliminary aerodynamic and mechanical design of the new SuperSwift airframe purpose-built for this mission, and design of a high-rate data logger system. Flight permission authorization is pending from NASA Ames and the FAA.

## Technical Approach

### Antenna Array Development (Section 2.0)
- **System**: 2x2 rectangular L-band microstrip collinear ("MiCo") antenna array operating at 1.4135 GHz (SMAP frequency band 1400-1427 MHz)
- **Architecture**: Four elements, each consisting of 5-segment microstrip colinear patch antennas with omnidirectional patterns; arranged at half-wavelength horizontal and quarter-wavelength vertical separations to cancel radiation at horizon while creating end-fire beams in nadir and zenith directions
- **Substrate**: Rogers 4003C duroid, fabricated in three sections
- **Key Design Achievements**:
  - Measured return loss of 2x1 subarray validated HFSS simulation accuracy
  - Identified 20 MHz frequency shift due to proximity effects and styrofoam spacer blocks
  - Optimized vertical separation distance at 55.5 mm (2.5 mm larger than quarter wavelength) for maximum main-to-back lobe ratio of 19.6 dB (band-averaged)
  - Developed frequency tuning methods using dielectric loading (silicon RTV strips with εr=3.6)
  - Integrated complete 2x2 array into Tempest fuselage mockup

### LDCR Build01 Ground Testing (Section 3.0)
- **Unit**: Human-portable soil moisture sensor using lobe-differencing correlation radiometer technique
- **Configuration**: Two L-band microstrip patch antennas (up-looking and down-looking), LDCR receiver with ZFL-1000LN+ amplifiers, AD5391 correlator board, NDVI sensor boards, GPS and navigation subsystem
- **Test Results**:
  - Measured LDCR sensitivity: 4.5×10⁻⁴ V/K
  - Measured voltage differential accuracy: Within 3% agreement with theoretical calculations (measured 0.17 V vs. calculated 0.1755 V)
  - Achieved temperature sensitivity (ΔT_RMS): 3.7 K (measured) vs. 2.57 K (theoretical); 44% higher than predicted
  - Identified noise sources and planned refinements including sample rate increase to 32 kS/s, LN2 calibration target, and crosstalk investigation

## Products & Capabilities Described

### Tempest UAS (Existing Platform)
- **Role**: Initial carrier platform for antenna array integration; later superseded by new SuperSwift design
- **Application**: Soil moisture mapping using integrated 2x2 antenna array on fuselage
- **Status in Q2**: Fuselage mockup completed with integrated antenna array for RF testing

### SuperSwift (New Development)
- **Overview**: Purpose-built electric powered pusher sUAS with V-tail configuration, designed specifically for soil moisture mapping mission with removable nose cone payload integration
- **Airframe Specifications**:
  - Empty weight: 7.5 lbs
  - Gross takeoff weight (with 3 lb payload): 10.5 lbs
  - Maximum payload capacity: 5 lbs
  - Wing area: 1100 in² (aspect ratio 13.09)
  - Wing span: 120 in, root chord 10 in, tip chord 7.5 in
  - Mean aerodynamic chord: 9.24 in
  - Taper ratio: 0.84
  - Wing loading: 22 oz/ft²
  - Forward sweep: 0.6°
  - Airfoil: MH 70 (11.08% thickness-to-chord ratio, low pitching moment)
  
- **Performance Predictions**:
  - Stall speed at 6,000 ft: 33.5 ft/s
  - Max coefficient of lift (wing): 1.23
  - Flight time: 90 minutes (87 minutes at cruise, 6,000 ft altitude)
  - Cruise power consumption: 71.5 W at 83.4% efficiency
  
- **Propulsion**:
  - Motor: Scorpion SII-4025-440KV (440 RPM/V, 0.025Ω internal resistance, 1.1A zero-torque current)
  - Propeller: APC Thin Electric 12x12 inch
  - Battery: 5-cell LiPo, 11000 mAh capacity
  
- **Tail Design**: V-tail with NACA 0009 airfoils (7 in root chord, 5.75 in tip chord, 40 in from wing leading edge)
  - Horizontal tail volume: 0.48
  - Vertical tail volume: 0.015
  - Incidence angle: 1° positive
  - Predicted downwash angle at tail: 1.3°
  
- **Stability**:
  - Neutral point: 4.25 in from wing leading edge
  - Center of gravity: 2.0 in from wing leading edge
  - Static margin: 21% (0.5 in forward of wing root ¼-chord)
  
- **Launch Characteristics**: Hand-launchable from unimproved surfaces; pusher configuration provides operator safety, low tail boom clearance
- **Construction**: Initial prototype in foam (for aerodynamic and mechanical verification), subsequent versions in composites
- **Status**: Design 90% complete, construction scheduled to begin November 1, 2014

### Removable Nose Cone
- **Design**: Fiberglass construction housing entire soil moisture mapping payload
- **Integration**: Mechanical and electrical interfaces under development; weight/balance chart provided to users for payload integration
- **Status**: Design 60% complete, payload interfaces pending

### LDCR (Lobe Differencing Correlation Radiometer)
- **Configuration**: Build01 = portable ground test unit; Version 2 carrier being developed
- **Carrier**: New machined aluminum case design reduces weight by factor of 3 while maintaining component shielding
- **Production Plan**: 4 additional complete LDCR units planned (one per SuperSwift, one ground test unit, one spare); completion targeted for Q3
- **Specifications**:
  - Operating frequency: 1.4135 GHz (L-band)
  - Bandwidth: 27 MHz
  - RC integration time constant: 1.5 ms
  - Sensitivity: 4.5×10⁻⁴ V/K

### High-Rate Data Logger (Section 5.0)
- **Architecture**: Multi-board system integrating analog/RF conditioning, FPGA processing, and solid-state storage
- **Components**:
  - Analog/RF Board: Signal conditioning, gain addition, balun circuits, analog correlation (32 kS/s→1 kS/s)
  - FPGA Module: Spartan-6 based EFM-02 (USB3.0 output)
  - ADC: LTC2143-14 (14-bit, 80 MS/s dual converter)
  - Host: VIA EPIA-P910-10Q Pico ITX board
  - Storage: SSD2GO Pocket (tested to 394 MB/s write speed)
  
- **Data Requirements**:
  - Sample rate: 60 MS/s at 14-bit (third Nyquist zone sampling)
  - Total disk write speed: 210 MB/s
  - Storage capacity: 756 GB per 1-hour sortie
  - Input sources: 2 LDCR analog channels, 8 thermistor inputs, 50 Hz telemetry (autopilot, NDVI/thermal, laser altimeter)
  - Output formats: 
    - Processed LDCR analog data at 60 MS/s
    - Telemetry at 50 Hz
    - Analog correlated data at 1 kS/s
    - Single binary file with common timestamp
  
- **Design Changes from Original**:
  - Reduced from 180 MS/s 16-bit to 60 MS/s 14-bit (due to third Nyquist zone approach)
  - Simplified from 36-card microSD array (original) → 11-card array (intermediate) → single SSD (final)
  - Eliminated complex parallel write logic
  - Reduced power requirements
  - Improved post-flight data access
  
- **Status**: Prototype design completed Q2, build and test scheduled for Q3

### SwiftCore/SwiftPilot Pro
- **Application**: Flight control and autonomous operations
- **Usage**: Simulated SuperSwift flights in X-Plane for aerodynamic and control algorithm verification; software-in-the-loop testing completed successfully

## Use Cases & Applications

### Primary Mission: Soil Moisture Mapping
- **Application**: Airborne measurement of soil moisture content using passive radiometric sensing
- **Measurement Approach**: Lobe-differencing correlation radiometry at L-band (1.4 GHz), sensing soil moisture to ~5-10 cm depth under most conditions
- **Deployment Plan**: Winter 2014/2015 deployment in Oklahoma to verify system operation and validate design (despite non-optimal seasonal conditions)
- **Scientific Value**: Contributes to SMAP (Soil Moisture Active Passive) mission algorithms and validation; supports agricultural and hydrological monitoring

### Secondary/Derivative Missions
- **Removable Nose Cone Concept**: Designed to enable rapid payload swaps for other scientific missions where quick changeout capability is valuable

## Key Results

### Antenna Array Performance
- **2x1 Subarray**: Return loss <-18 dB across 27 MHz working band (1400-1427 MHz); omnidirectional radiation pattern with null at horizon
- **2x2 Array**: Main-to-back lobe ratio of 19.6 dB (band-averaged); optimized vertical separation reduces mutual coupling
- **Frequency Tuning**: Achieved 5 MHz frequency reduction using dielectric loading; method validated for manufacturing error compensation

### LDCR Ground Testing
- **Instrument Validation**: Output voltage measurements in excellent agreement with theoretical calculations (0.17 V measured vs. 0.1755 V predicted)
- **Sensitivity Achievement**: 3.7 K ΔT_RMS (44% higher than 2.57 K theoretical); origin of discrepancy attributed to correlator circuitry noise (under investigation)
- **Operational Modes Verified**: Reference-only, mixed antenna/reference, and full antenna differential modes all functional
- **Next Steps**: Improved experimental fixture, LN2 calibration target, sample rate increase to 32 kS/s with 32x averaging, crosstalk analysis

### SuperSwift Aerodynamic Design
- **Simulation Validation**: Aircraft handled well in X-Plane flight simulation; autopilot control algorithms verified through software-in-the-loop testing
- **Design Efficiency**: High aspect ratio wing (13.09) optimized for low-speed hand-launch requirement; V-tail reduces structural weight vs. conventional tail; static margin of 21% ensures stability
- **Manufacturing Readiness**: CAD design complete, aerodynamic analysis 90% complete; foam prototype construction ready to begin

### Data Logger Development
- **Simplified Architecture**: Transition from complex multi-card approach to single SSD eliminates significant risk while improving operational efficiency