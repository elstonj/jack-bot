# Airworthiness Questions

## Document Metadata
- Type: Q&A / Capability Questionnaire (DoD/USSOCOM compliance)
- Client/Agency: USSOCOM (U.S. Special Operations Command)
- Program/Solicitation: USSOCOM CRADA (Cooperative Research and Development Agreement)
- Date: 2026-06-30
- BST Products/Systems Referenced: S0, S0-AD, SwiftCore Flight Management System
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
This document addresses airworthiness and operational questions from USSOCOM regarding the S0 unmanned aircraft system. It covers safety mechanisms, operator training, security protocols, payload capabilities, and operational limitations for the S0-AD atmospheric sensing variant.

## Technical Approach & Safety Systems

### Flight Control & Containment
- **Vertical Geo-fence**: Operator-set minimum/maximum altitude limits enforced in mission planning and autopilot; prevents waypoint creation outside limits and restricts manual flight control via handset
- **Lost Link Protocol**: Pre-set lost link point; aircraft proceeds directly to waypoint and orbits if communication lost beyond operator-defined timeout; operator can regain control via handset at any time
- **Low Battery Limit**: Operator-configurable battery threshold triggers automatic return to landing orbit point and landing execution
- **Velocity/Rate Limiting**: Pitch, roll, yaw rate, airspeed, and vertical speed limits during manual handset control to prevent stalls, spins, and loss-of-control states

### Navigation & Failure Management
- **GPS Failure Response**: Red (Level 1) alert on control tablet; within visual line-of-sight (LOS), pilot takes manual control; beyond visual line-of-sight (BVLOS), aircraft assumes level attitude and gradual descent to landing
- **Navigation Redundancy**: No autonomous GPS-loss redundancy; relies on manual control within LOS
- **Failure Indication System**: Pop-up alerts on control tablet (Level 1 = red/critical; Level 2 = yellow/less severe) indicating GPS loss, control link loss, low battery, RemoteID failure, etc.

## Products & Capabilities Described

### S0 / S0-AD Aircraft
- **Description**: Small unmanned aircraft system (sUAS) with SwiftCore Flight Management System
- **Atmospheric Sensing Payload**: Measures atmospheric pressure, ambient temperature, relative humidity, and 3D winds via nose-mounted sensors
- **Control**: Tablet-based mission planning and ground control station; optional handset manual control
- **Current Configuration**: S0-AD configured for atmospheric/meteorological sensing only (no FMV, EW/SI capabilities mentioned)

### SwiftCore Flight Management System
- **Description**: Internally developed flight management and control system
- **Security Testing**: Examined during U.S. Navy HacktheMachine-Unmanned competition (2021); critical and medium vulnerabilities identified and addressed
- **Operator Experience**: BST operators qualified and experienced across multiple deployments; customer initial training achievable in 2-3 days

## Use Cases & Applications
- USSOCOM operational testing (LOS-dependent, ground-based operations)
- Atmospheric sensing and meteorological data collection
- Missions requiring extended operational range

## Notable Details

### Security & Compliance
- **No ATO (Authority to Operate)** currently granted
- **Datalink Encryption**: Optional 256-bit AES encryption available but not currently used in BST operations
- **Software Development**: Entirely internally developed by U.S. citizens/persons; codebase managed in GitLab
- **Cybersecurity Assessment**: No formal assessment conducted; vulnerability testing limited to HacktheMachine competition results

### Operational Limits
- **Maximum LOS Range**: Successfully demonstrated at 215 nautical miles (datalink and GCS aboard high-altitude manned aircraft); for SOCOM ground operations, limited by aircraft altitude and terrain between S0 and operator
- **System Status**: Minor wind-measurement discrepancies resolved; no major system failures reported

### Training & Qualifications
- BST operators: Multi-year, multi-deployment experience with S0 and other BST aircraft
- Customer operators: 2-3 day initial qualification program