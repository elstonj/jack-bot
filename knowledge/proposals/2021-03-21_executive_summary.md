# A Novel Aerial Drone Platform for Exploration of Titan - Interim Report Executive Summary

## Document Metadata
- Type: Interim Report / Executive Summary
- Client/Agency: NASA
- Program/Solicitation: SBIR (Contract Number: 80NSSC19C0332)
- Date: March 21, 2021
- BST Products/Systems Referenced: S2 (aircraft), SwiftPilot (avionics), MiniSwarm (prototype platform)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing a novel aerial drone platform for exploration of Titan under NASA contract. The project involves creating simulation environment models, flight dynamics models, and an Earth-based analog prototype to demonstrate technology readiness for a Titan atmospheric exploration mission. As of March 2021, simulation models were complete, flight dynamics modeling was underway, and initial prototype integration and testing had begun.

## Technical Approach

### Simulation Environment
- **Titan-GRAM 2005 Integration**: Converted the Titan-GRAM atmospheric model into a web API to enable networked queries
  - Input conversion from hardcoded files to template-based system
  - Consolidated fragmented output files to stdout
  - Updated to support concurrent requests
  - Query interface via URL parameters (e.g., `/titan_gram/<latitude>/<longitude>/<altitude>`)
  - JSON response includes: Temperature (K), Density (kg/m³), Pressure (N/m²), East Wind (m/s), North Wind (m/s)

### Flight Dynamics Modeling
- **JSBSim Integration**: Connected Titan-GRAM 2005 to JSBSim (flight dynamics simulator) via configurable UDP socket
- **Autopilot Interface**: Socket-based data parsing between autopilot and JSBSim
  - Uses existing Autopilot TCP socket and JSBSim UDP socket
  - BST forked JSBSim to internal version for model/script additions and core modifications
  - Created translation layers to abstract JSBSim interface and simplify connections to wind data and autopilot
- **Cross-planetary Simulation**: Demonstrated end-to-end simulation capability with BST S2 aircraft model flown on both Earth and Titan

### Earth Prototype Development
- **Platform**: MiniSwarm aircraft modified as Earth analog
- **Avionics**: SwiftPilot avionics integrated with pitot/static tubes
- **System Mass**: 1.4 kg total

## Products & Capabilities Described

### SwiftPilot Avionics
- BST's autopilot/avionics system
- Successfully integrated into MiniSwarm prototype
- Demonstrated TCP socket communication interface for flight control
- Provided responsive aircraft control during transition testing

### S2 Aircraft
- BST's baseline aircraft design
- Used as flight dynamics model for Titan simulation studies
- Demonstrated glide characteristics (18 m/s commanded speed on Titan with motor disabled)

### MiniSwarm Prototype Platform
- Small quadrotor/VTOL aircraft used as Earth analog for Titan missions
- **Initial Flight Test Specifications:**
  - Gross Takeoff Weight: 1.42 kg
  - Hover power: 192 W (13.2 A)
  - Maximum forward flight speed: 13 m/s
  - Number of test flights: 4
  - Performed transition from hover to 60-degree forward flight angle (30 degrees off-horizontal)
  - Airspeed achieved during forward flight: 13 m/s (measured by pitot tube)
  - Propulsion system: Modified from original MiniSwarm configuration for Colorado high-elevation testing

## Use Cases & Applications
- **Titan Atmospheric Exploration**: Primary application is an aerial drone capable of operating in Titan's dense atmosphere
- **Transition Flight Testing**: Demonstrated VTOL-to-forward-flight transition capability relevant to Titan operations
- **Long-duration Flight**: Implied capability for sustained atmospheric sampling missions

## Project Timeline Status (as of March 21, 2021)
| Task | Target Month | Status |
|------|--------------|--------|
| Simulation environment models | 5 | ✓ Complete |
| Drone flight dynamics models | 11 | Underway |
| Avionics integration with terrestrial prototype | 13 | First prototype complete |
| Flight permission | 13 | Not Started |
| Terrestrial flight testing | 16 | Not Started |

## Key Results (Prototype Testing)

**Hover Testing:**
- Successfully achieved hover with 192 W power requirement
- Responsive control characteristics noted

**Transition Testing:**
- Successfully transitioned from hover to 60-degree forward flight angle
- Maintained pitch angle of 60 degrees throughout forward flight phase
- Achieved 13 m/s airspeed during forward flight
- Excellent heading control maintained during forward flight
- Pilot feedback: aircraft was responsive and controllable

**Simulation Results:**
- 1-minute glide test of S2 on Titan with motor disabled at 18 m/s demonstrated end-to-end simulation capability
- Cross-planetary simulation (Earth vs. Titan models) validated modeling approach

## Notable Details

### Hardware Modifications
- **Propulsion System Swap**: Original propulsion replaced with higher-thrust system due to weight and Colorado high-elevation testing requirements
- **ESC Upgrade**: Replaced original DYS 4-in-1 ESC with system allowing simplified parameter changes and consistent motor RPM control

### Software Architecture
- Created custom translation layers to abstract JSBSim complexity
- Built configurable socket-based interfaces for flexible integration
- Enabled remote execution capability through web server design

### Testing Approach
- Controls tested without flaps, using only rotor control
- Demonstrated good heading control authority during forward flight
- Integration of pitot/static measurements for validation

### Competitive Advantages Demonstrated
- Web API approach to Titan-GRAM enables scalable atmospheric modeling
- Internal JSBSim fork allows modification without upstream dependencies
- End-to-end simulation pipeline from atmospheric model through flight dynamics to autopilot control
- Prototype validation of VTOL transition concept at altitude with custom avionics