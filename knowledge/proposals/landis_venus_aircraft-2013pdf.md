# Venus Aircraft

## Document Metadata
- Type: Technical presentation/white paper
- Author: Geoffrey A. Landis, NASA John Glenn Research Center
- Date: 2013 (based on file creation date 2018-03-06 and reference as background material)
- Context: Referenced in Black Swift Technologies' 2018 SBIR Phase I Venus proposal
- Key Personnel: Geoffrey A. Landis (NASA); Chris LaMarre; A. Colozza; Les Bossinas (artist)

## Executive Summary
This document presents a comprehensive technical analysis of solar-powered aircraft design for Venus atmospheric exploration, comparing aircraft to balloons and airships as exploration platforms. It details the aerodynamic principles, design evolution, and feasibility of sustained powered flight in Venus's dense atmosphere above the cloud layers, supported by concept designs and mass budgets from multiple design iterations (2000-2008).

## Technical Approach

### Atmospheric Flight Dynamics on Venus
- **Optimal flight altitude:** 50-60 km above Venus surface
  - Atmospheric density profile similar to Earth's
  - Gravity is 90% of Earth's (easier powered flight)
  - Above clouds with higher solar intensity than Earth
  - Acid droplets require corrosion-resistant materials
  
- **Aerodynamic principles:**
  - Lift equation: F = ½ ρ CL A V² = mg
  - Flight velocity: V = SQRT[(mg/A)/(2ρCL)]
  - Power required: P = mg/(L/D) × V = (mg)^3/2 / [(L/D)(2ρA)^½]
  - Optimal L/D ratio needed to balance parasitic drag

### Solar Airplane Figure of Merit
- Calculated comparative advantage: Venus has figure of merit of **2.2** compared to Earth (1.0)
  - Factors: solar intensity inversely proportional to distance squared (Venus at 0.723 AU)
  - Power required proportional to square root of atmospheric density
  - Venus: 1 bar pressure, 0.91 gravity
  - Result: **solar flight easier on Venus than Earth**

### Solar Energy Availability
- Surface: 10% of exoatmospheric power at 1000 nm; <1% at 450 nm
- **Above 50 km:** Venus has more sunlight than Earth
- **Above 65 km:** Venus atmosphere essentially clear

## Products & Capabilities Described
Not applicable. This is a NASA reference document, not a Black Swift Technologies document.

## Use Cases & Applications

### Venus Atmospheric Exploration
- **Platform advantages over alternatives:**
  - **Balloon:** Simple, demonstrated on Venus, but fixed location and difficult altitude changes
  - **Airship:** Slow speed (cannot stationkeep or stay in sun), difficult stow/deploy
  - **Airplane:** Easy altitude changes, speed allows stationkeeping and continuous sun exposure, easy latitude maintenance

### Mission Capabilities
- Continuous operation in sunlight (unlike airships and balloons)
- Ability to maintain station and follow variable wind patterns
- Flexible altitude control within design limits
- Latitude maintenance capability

## Design Evolution & Specifications

### Initial Concepts (2000-2001)
- Simple flying-wing design with small tail
- Aeroshell diameter: 1.2 meters

### 2001 OAI Proposal (Chris LaMarre design)
- Wing area (S): 1.6 m²
- Wingspan (b): 4.38 m
- Aspect ratio (AR): 12
- Mass: 15 kg
- Airfoils: DF 101 and SG8000 investigated

### RASC Design (Final, 2003)
- **Aeroshell diameter:** 3.7 meters (size of Viking lander entry system)
- Aeroshell shape based on Mars Pathfinder
- Aircraft folded into aeroshell for entry and deployment

### RASC Venus Airplane Mass Budget
| System | Mass (kg) | Mass Fraction |
|--------|-----------|---------------|
| Airplane | 103 | 20% |
| Heatshield Structure | 36.05 | 7% |
| Heatshield TPS | 66.95 | 13% |
| Backshell Structure | 61.80 | 12% |
| Backshell TPS | 41.20 | 8% |
| Parachute System | 51.50 | 10% |
| Deployment Mechanism | 77.25 | 15% |
| Misc (COMM, Power, Ballast) | 77.25 | 15% |
| **Total Entry Payload** | **515** | **100%** |
| With 30% Contingency | **670** | — |

### RCS (Reaction Control System) for Entry
- Two thruster options: Marquardt 100 lbf (28.0 kg) or Rockwell 25 lbf (25.0 kg)
- Total RCS dry mass: 51.9 kg
- Propellant/Pressurant: 103.9 kg (N₂O₄/Hydrazine bipropellant or Hydrazine monopropellant)
- **Total entry system dry mass:** 721 kg
- **Total entry system wet mass:** 825 kg
- **ΔV capability:** 350 m/s

### Power Analysis
- Design point: 9m wing with 18% solar cell efficiency and 80% packing
- Alternative configurations analyzed:
  - 9m wing with 32% efficiency: reduced power requirement
  - 6m wing with 32% efficiency and double-sided arrays: assumes 77% albedo reflection
- Optimal altitude: where power required equals power available (~55-60 km)

### 2008 Boston University Design
- Student design XQ-V1 (Greg Thanavaro)

## Comparison: Mars Airplane (ARES) Reference Point
- 6.25 m span
- Aspect ratio: 5.6
- Mass including margin: 101 kg
- Used as baseline for folding/deployment technology transfer

## Key Technical Findings

### Altitude Selection Critical
- **Lower altitudes (40-50 km):** Easier to fly but requires excessive power to maintain airspeed against wind
- **Higher altitudes (65+ km):** Low atmospheric density requires prohibitively high airspeed
- **Optimal band (55-60 km):** Balances power availability with aerodynamic requirements

### Material Requirements
- All exposed surfaces must be corrosion-resistant to sulfuric acid
- Metal surfaces need passivation coating
- Acid-resistant materials are well-developed technology

### Power Budget Challenge
- Calculation must account for wind speed
- Trade-off between wing area (increased mass) and solar cell efficiency
- Higher efficiency cells reduce required wing area but increase cost
- Double-sided solar arrays promising but limited by albedo assumptions

## Notable Details

### Planetary Comparison
| Planet | Distance (AU) | Gravity (g) | Pressure (bar) | Figure of Merit | Notes |
|--------|---|---|---|---|---|
| Earth | 1 | 1 | 1 | 1 | Baseline |
| **Venus** | **0.723** | **0.91** | **1** | **2.2** | **Best for solar aircraft** |
| Mars | 1.524 | 0.38 | 0.0064 | 0.15 | Thin atmosphere problematic |
| Jupiter | 5.203 | 2.36 | 1 | 0.01 | High gravity, distance |
| Saturn | 9.572 | 0.92 | 1 | 0.01 | Distance, opacity |
| Titan | 9.572 | 0.14 | 1.5 | 0.27 | Low gravity advantage offset by distance |

### Deployment Technology Transfer
- Stow and deploy concepts demonstrated by ARES Mars airplane
- Folding mechanisms detailed but noted as "needs work" in 2003
- Aeroshell-based deployment concept validated through Mars Pathfinder heritage

### Design References
- Aerovironment Pathfinder, Sky Sailor, Sunseeker
- NASA Glenn solar airplane team expertise
- Solar Impulse program reference

## Publications by Landis et al. (2001-2006)
Comprehensive peer-reviewed publications documenting development from 2001 "Exploring Venus by Solar Airplane" through 2006 "Robotic Exploration of the Surface and Atmosphere of Venus" in *Acta Astronautica*, *Journal of Spacecraft and Rockets*, and AIAA conferences.

---

## Significance for Black Swift Technologies Context
This document provides the foundational atmospheric flight physics and conceptual design heritage for Venus airplane missions. BST's 2018 SBIR Venus proposal likely built upon or referenced these established principles and design approaches for atmospheric exploration platforms on Venus.