# Navy STTR Phase I Kickoff: Hazardous Weather Operations

## Document Metadata
- Type: Kickoff presentation
- Client/Agency: Office of Naval Research (ONR)
- Program/Solicitation: Navy STTR Phase I; Contract N68335-25-C-0270
- Date: July 16, 2025 (presentation); Phase I base period July 2025 - January 2026
- BST Products/Systems Referenced: S0 UAS, S0-VTOL
- Key Personnel: Jack Elston (Principal Investigator), Maciej Stachura (BST); Josh Wadler (ERAU), Jun Zhang (University of Miami), John Park (Old Dominion University)

## Executive Summary
Black Swift Technologies is executing a Navy STTR Phase I contract to enhance the S0 UAS platform for naval atmospheric profiling in hazardous weather conditions. The project focuses on quantifying S0's superiority over radiosondes for air-sea interaction observations, improving wind and turbulence measurement accuracy, developing new sensor capabilities (turbulence, wave height), and creating autonomous adaptive sampling strategies for hurricane and maritime operations.

## Technical Approach

**S0 System Enhancement Strategy:**
1. Comparative analysis of existing platforms (NCAR dropsondes, radiosondes, Raytheon Coyote, Anduril Altius-600, Dragoon Coreolis) to establish S0's performance advantages
2. Detailed error analysis identifying sources of uncertainty in wind measurements, turbulence estimation, and height calculations
3. Integration pathway development for Navy launch platforms (sonobuoy systems, P-8A Poseidon external pods, CH-53E helicopters)
4. Icing mitigation strategies evaluation (heating elements, de-icing coatings)
5. Onboard turbulence computation algorithms leveraging 100Hz multi-hole probe wind sensor data
6. Radar-based wave height measurement system development (to replace laser altimeter limited by precipitation)
7. Two-tiered autonomous sampling strategy:
   - Open-loop: Preprogrammed rules from tropical cyclone forecast models
   - Closed-loop: Machine learning surrogate models with real-time adaptive updating using hurricane forecast data

## Products & Capabilities Described

**S0 UAS:**
- Primary platform for hurricane and hazardous weather atmospheric profiling
- Long-range communications enabling 191-mile range to P-3 aircraft
- Flush-air sensing nose cone for wind measurement
- Onboard 100Hz wind data acquisition and calculation capability
- Integrated sensors: pressure, temperature, humidity, 3D winds, sea surface temperature
- Automated sensor-directed flight in hurricanes with minimal operator overhead

**2024 Performance:**
- 19 missions flown (4 Ernesto, 4 Francine, 7 Helene, 4 Milton); 17 successful
- Wind accuracy: 1-2 m/s
- Data rate: ~3 Hz
- Endurance: 105 minutes
- Reliability: 85-90%
- Laser wave height sensor (clear air only)

**2025 Target Improvements:**
- Wind accuracy: 0.2 m/s (10x improvement)
- Data rate: 10 Hz (3x improvement)
- Endurance: 120 minutes
- Reliability: >90%
- Radar wave height measurement (all-weather)
- Manufacturing scaling: 50 aircraft with "light" effort (vs. 19 with "tremendous effort" in 2024)
- Turbulence measurements onboard
- Automated data processing onboard P-3

**S0-VTOL:**
- Land-launch variant of S0 sensing core
- 200+ km/h dash speed
- Same sensors and avionics as S0
- Currently in use by Barbados and Embry-Riddle Aeronautical University

## Use Cases & Applications

**Primary (Established):**
- Hurricane atmospheric profiling and reconnaissance
- Air-sea interaction region high-resolution observations
- Replacement for radiosondes in hazardous conditions

**Secondary (Proposed/Future):**
- World Meteorological Organization vertical wind profiling (1000' elevation near Tulsa)
- Integration with 53rd Weather Reconnaissance Squadron for P-8 magnetic anomaly detection
- C-130 drop site condition assessment
- KC-135 magnetic mapping operations
- Stratospheric balloon deployments via NASA (wildfire monitoring, disaster response, storm tracking)

## Technical Details & Specifications

**Wind Measurement:**
- Multi-hole flush-air probe with 100Hz onboard calculation
- Current accuracy: 1-2 m/s; target: 0.2 m/s
- Turbulence computation: leveraging 100Hz data for fine-scale turbulence and vertical velocity

**Wave Height:**
- Current: Laser altimeter (limited to clear air)
- 2025: Small radar sensor (all-weather capability)
- Task B3 focus: Quantify exact measurement/accuracy requirements

**Communications:**
- Long-range link; demonstrated 191-mile range to host P-3
- Data rate currently ~3 Hz; target 10 Hz

**Endurance & Propulsion:**
- 2024: 105 minutes
- 2025: 120 minutes (improved propulsion and batteries)
- Significantly improved ease of assembly and scalability

## Project Organization & Timeline

**Base Period: July 2025 - January 2026**

| Task | Dates | Focus | Lead |
|------|-------|-------|------|
| B1 (Kickoff) | 7/7-9/6 | Comparative platform analysis; S0 strengths/weaknesses | ERAU, UM, BST |
| B2 | 8/7-10/6 | Navy platform integration plan; error analysis; icing mitigation | BST, ERAU, UM, ODU |
| Progress Report | 10/6/25 | Interim deliverable | — |
| B3 | 10/7-12/6 | Turbulence algorithms (100Hz onboard); radar wave height measurement | BST, ERAU, UM |
| B4 | 11/7-1/6 | Autonomous adaptive sampling (open-loop and closed-loop AI models) | ODU, BST |
| Final Report | 1/6/26 | Deliverable | — |

**Option Period:** Kickoff date to be determined

## Project Team Structure
- **Black Swift Technologies:** Jack Elston (PI), Maciej Stachura
- **Embry-Riddle Aeronautical University:** Josh Wadler
- **University of Miami:** Jun Zhang
- **Old Dominion University:** John Park

## Notable Details

**Competitive Advantages Highlighted:**
- Demonstrated reliability in actual hurricane operations (19 successful missions in 2024)
- Adaptive sampling capability unique to UAS vs. expendable platforms (radiosondes, dropsondes)
- Highest wind measurement by UAS achieved to date
- Longest air-deployed UAS flight into storm
- Onboard 100Hz wind data enabling turbulence measurement not possible with radiosondes

**Navy-Specific Requirements Being Addressed:**
- Integration with sonobuoy launch systems and military aircraft external mounts (P-8A, CH-53E)
- Magnetic anomaly and mapping detection integration
- Icing capability in harsh maritime environments
- Automated data processing and reduced crew overhead for P-3 operations

**Partnerships & Stakeholder Buy-In:**
- NOAA operational hurricane missions (2024 baseline)
- 53rd Weather Reconnaissance Squadron for future operational integration
- NASA stratospheric balloon programs (cost-sharing model)
- International operators (Barbados, ERAU using S0-VTOL)

**Technology Transfer/Scaling Success:**
- 2024: 19 aircraft built with "tremendous effort"
- 2025 goal: 50 aircraft with "light" effort (manufacturing process maturation)