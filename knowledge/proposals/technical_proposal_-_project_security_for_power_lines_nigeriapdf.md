# TECHNICAL PROPOSAL - PROJECT SECURITY FOR POWER LINES, NIGERIA

## Document Metadata
- Type: Technical Proposal
- Client/Agency: Nigerian Power Utility (implied from title)
- Program/Solicitation: Project Security for Power Lines - Nigeria
- Date: 2015-04-17
- BST Products/Systems Referenced: None. This proposal is from Consilium (a third-party security vendor), not Black Swift Technologies.
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This document is a technical proposal from Consilium (not BST) offering integrated security solutions to protect Nigerian power line infrastructure from vandalism, theft, and security threats. The proposal presents a comprehensive suite of physical security, surveillance, access control, and monitoring systems designed for utility facilities ranging from headquarters to substations and transmission infrastructure.

## Technical Approach
Consilium proposes a multi-layered security approach combining:
- **Intrusion Detection**: FiberLR fiber-optic perimeter sensors for fence and buried pipeline protection
- **Access Control**: BTX-series turnstiles, swing gates, and biometric fingerprint readers
- **Video Surveillance**: CCTV systems with PTZ cameras, digital video recording, and video analytics
- **Monitoring**: 24/7 digital surveillance, gate access control with video verification, remote monitoring
- **Management Systems**: StarNeT 1000 security management system (SMS) and Network Manager software

## Products & Capabilities Described

### FiberLR - Fiber Optic Intrusion Detection System
- **What it is**: Long-range fiber-optic perimeter intrusion detection sensor
- **Specifications**:
  - Perimeter protection: up to 16 km (10 mi.) of coverage
  - Pipeline protection: up to 48 km (30 mi.) coverage
  - Detection accuracy: 8 m (25 ft.) for perimeter; 30 m (100 ft.) for buried pipelines
  - Detection resolution: 45 m (150 ft.) for perimeter; 100 m (330 ft.) for pipelines
  - Probability of Detection (Pd): 95%
  - False Alarm Rate (FAR): <1/km/month typical
  - Can detect and locate multiple simultaneous intrusions
  - Cut-immune in redundant-loop configuration
- **Proposed Use**: Perimeter security for power line substations, fence-mounted or buried alongside pipelines to detect third-party interference (TPI), digging, tampering
- **Integration**: Compatible with SMS and PSIM platforms via Network Manager

### StarNeT 1000 - Security Management System
- **What it is**: Windows-based multi-functional SMS platform for centralized security control
- **Capabilities**:
  - Multi-workstation, multi-site scalability
  - Real-time alarm viewing and acknowledgment
  - Site-specific mapping with sensor zones
  - Point-and-click hardware control
  - Automated reporting and audit trails
  - Integration with video matrix switches (American Dynamics, Bosch, Pelco)
  - Support for multiple Senstar networks (Silver, Crossfire, Sennet, CCC, MX)
- **Proposed Use**: Central command and control hub for all dispersed power facility security systems
- **Key Feature**: Designed for non-technical operators; intuitive GUI minimizes training costs

### Network Manager Suite
- **What it is**: IP-based alarm reporting and sensor networking platform
- **Capabilities**:
  - Common software interface for all Senstar networked sensors
  - Silver Network uses loop topology with redundant data paths
  - Supports alarm status, operational diagnostics, firmware updates, event logging
  - API interface for third-party SMS integration
  - Redundant configuration option for critical applications
- **Proposed Use**: Real-time sensor data aggregation and management across geographically distributed power facilities

### BTX 300 - Full Height Turnstile Access Control
- **What it is**: Mechanical access control turnstile (manual or motorized options)
- **Specifications**:
  - Single-sided: 1490 x 1240 x 2215 mm, ~300 kg
  - Double-sided: 2220 x 1240 x 2215 mm, ~585 kg
  - Power: 110/220V AC, 50/60Hz; 24V DC standby
  - Passage capacity: ~60 passages/minute mechanical; ~10-25 people/minute nominal
  - Passage authorization time: <0.3 seconds
  - Operating temperature: -20°C to +68°C (optional -50°C with heater)
  - IP rating: IP 54 outdoor (optional IP 56)
  - MTBF: 1M cycles
  - Arm options: Ø42mm steel or Ø40mm 304/316 stainless steel
  - Control: Dry contact, grounding input, optional RS232/RS485/TCP IP modules
  - Emergency mode: Fail-safe (default) or fail-secure options
- **Proposed Use**: Controlled access to substations, facilities, and sensitive areas; prevents unauthorized personnel entry

### 602 Swing Gate - Waist-Height Access Control
- **What it is**: Bi-directional swing gate for high-traffic access control
- **Specifications**:
  - Dimensions: 450 x 1000 x 300 mm + 470 mm arm
  - Power: 110/220V AC, 24V DC standby ~11W typical, ~60W max
  - Passage capacity: ~90 passages/minute mechanical; ~25-46 per minute nominal
  - Operating temperature: -20°C to +68°C (optional -50°C with heater)
  - IP rating: IP 54 outdoor (optional IP 56)
  - Control: Dry contact, grounding input, optional RS232/RS485/TCP IP
  - Emergency mode: Fail-safe or fail-secure
  - Double-sided version: 450 x 1000 x 600 mm, ~22W standby, ~120W max
- **Proposed Use**: Access control at facility entrances and checkpoints with higher throughput than turnstiles

### EVA.5 - Road Barriers
- **What it is**: Motorized vehicle barrier for access control at gates and entry points
- **Specifications**:
  - 24 Vdc intensive-use barrier
  - Arm length: up to 5 m
  - Opening time: 3-5 seconds
  - Torque: 205 Nm
  - Power: 230 Vac (50-60Hz) input; 24 Vdc motor supply
  - Max absorbed current: 1.6 A
  - Operating temperature: -20°C to +50°C
  - IP rating: IP 44
  - Weight: 55 kg
  - Features: Integrated control box, amperometric anti-crushing control, optional photocells, battery backup option
- **Proposed Use**: Vehicle access control at power facility entry gates

### WAB BEM FCKS - Biometric Fingerprint Reader
- **What it is**: Compact standalone/networked biometric access controller with fingerprint sensor
- **Specifications**:
  - Fingerprint capacity: 3,000 PCS (expandable to 8,000)
  - Sensor: 500 dpi optical fingerprint sensor
  - CPU: 400 MHz DSP
  - Memory: 4 MB Flash + 8 MB RAM
  - Card support: EM4100 proximity, Mifare, compatible cards
  - Authentication modes: Fingerprint alone, card alone, card + fingerprint, ID + fingerprint
  - Communication: Wiegand output, TCP/IP
  - Power: 12 VDC, 200 mA typical, 150 mA standby
  - Operating temperature: -20°C to +65°C
  - Humidity: 0-95%
  - Anti-spoofing: Advanced fake fingerprint detection
- **Proposed Use**: High-security access to critical control rooms and sensitive equipment; integrates with WatchNET access control system

## Use Cases & Applications

1. **Perimeter Protection**: FiberLR sensors on substation perimeter fences and around buried power transmission cables to detect intrusion attempts
2. **Facility Access Control**: BTX turnstiles and swing gates controlling personnel access to substations, transformer stations, and maintenance facilities
3. **Vehicle Access**: EVA.5 barriers at main facility gates controlling truck/vehicle entry
4. **Critical Area Security**: Biometric fingerprint readers protecting control rooms, switching stations, and equipment vaults
5. **Centralized Monitoring**: StarNeT 1000 and Network Manager providing 24/7 remote surveillance and alarm response coordination
6. **Compliance Reporting**: Automated audit trails and reporting to meet NERC (North American Electric Reliability Corporation) and Sarbanes-Oxley regulatory requirements
7. **Third-Party Interference Detection**: Pipeline and buried cable protection against unauthorized digging, tapping, and sabotage

## Key Results
No results section; this is a proposal document presenting capabilities, not a performance report. No testing data or implementation outcomes are provided.

## Notable Details

**Regulatory Compliance Emphasis**:
- Document stresses compliance with NERC regulations and Sarbanes-Oxley requirements
- Automated reporting features support audit and regulatory requirements
- Systems designed for critical infrastructure protection under heightened security mandates

**Vendor: Consilium, Not BST**:
- **Critical Note**: This entire proposal is from Consilium, a third-party security systems integrator, not Black Swift Technologies
- Uses Senstar Corporation products (FiberLR, StarNeT, Network Manager) as core components
- Uses Hikvision/third-party PTZ cameras and CCTV systems
- Uses access control equipment from multiple manufacturers (BTX turnstiles, EVA barriers, WAB BEM biometric readers)
- Consilium appears to be a systems integrator/reseller, not equipment manufacturer

**Cost Savings & Value Propositions**:
- Video analytics reduce false alarms compared to conventional motion detection
- Low-bandwidth digital transmission for remote monitoring
- Automation of manual processes and audit report generation
- Enterprise-wide management from central location with local autonomy options

**Competitive Claims**:
- Consilium positioned as "one of the world's leading manufacturers of security products" with 100+ years history (likely referring to parent company)
- Integration capabilities with multiple leading SMS/PSIM platforms
- Scalability from simple standalone systems to complex multi-site operations

**Geographic Context**:
- Proposal specifically tailored for Nigeria power sector
- Addresses region-specific security threats (theft, vandalism, civil unrest)
- Equipment specified with outdoor durability for tropical/harsh environments