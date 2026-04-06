# Hummingbird SwiftCore FMS Project Overview

## Document Metadata
- Type: Project plan / development proposal
- Client/Agency: Reference Technologies (ReferenceTEK)
- Program/Solicitation: Custom development contract
- Date: June 11, 2015 (draft)
- BST Products/Systems Referenced: SwiftCore FMS, SwiftTab, SwiftPilot, SwiftStation
- Key Personnel: Not named in document
- Status: Sales completed / inactive project

## Executive Summary
Black Swift Technologies proposed a custom development and integration effort to adapt its SwiftCore Flight Management System for Reference Technologies' Hummingbird II multi-rotor UAV. The project involved designing flight control systems tailored to the vehicle's unique hybrid power architecture (central ducted fan with 6-8 external Dynamic Propulsion Units), with a 15-week development timeline and total cost of $210,000 including first article production.

## Technical Approach

**Vehicle Configuration:**
- Hummingbird II multi-rotor with single main ducted fan surrounded by 6 or 8 external rotors (Dynamic Propulsion Units/DPS)
- Hybrid power system: on-board combustion engine + generator + battery system + electric motors
- Center duct uses counter-rotating blades for yaw stabilization; external DPS angled for yaw control

**Development Strategy:**
- Custom SwiftCore FMS adaptation for Hummingbird II's unique propulsion architecture
- Incremental development and testing organized in 7 milestone blocks
- Main duct assigned to altitude and speed control; external DPS for attitude control
- Simulator-first approach with hardware-in-loop (HIL) testing before flight testing

**Development Milestones (15 weeks, July 1 - October 4, 2015):**
1. Simulator Development and Hummingbird II Flight Dynamics Model (FDM)
2. Vehicle Integration
3. Manual Control Development
4. Multi-rotor Control Development
5. Main-duct Altitude/Energy Control
6. ECU and Payload Control
7. Testing and Verification & Validation (V&V)

## Products & Capabilities Described

**SwiftCore FMS**
- Flight management system adapted for multi-rotor VTOL vehicles
- Custom control system designed specifically for Hummingbird II's hybrid propulsion
- Delivered as 5 first-article production units

**SwiftTab**
- Interface system; modified version provided improved health & status (H&S) display for Hummingbird II

**SwiftPilot & SwiftStation**
- Components of production SwiftCore FMS bundle
- Integrated with customer-selected radios

**Flight Dynamics Model (FDM)**
- Realistic simulation model of Hummingbird II
- Developed for simulator environment with HIL capabilities
- IP ownership transferred to ReferenceTEK

## Use Cases & Applications
- Multi-rotor UAV platform with hybrid combustion/electric power system
- Autonomous and manual flight operations
- Altitude/speed control via main duct
- Attitude control via external DPS

## Deliverables
- Functional simulation environment with HIL testing and real-time visualization
- Realistic flight dynamics model of Hummingbird II
- Custom flight control system for Hummingbird II
- Modified SwiftTab interface for improved H&S
- Summary report detailing flight test results and performance metrics
- Five (5x) full SwiftCore FMS first-article production units

## Budget & Payment Structure

**Development Cost: $175,000**
- Development milestones (paid during project): $75,000
  - Project kickoff: $25,000
  - Hummingbird FDM completion: $15,000
  - Manual control demonstration: $10,000
  - Full system control demonstration: $10,000
  - Autonomous flight control demonstration: $10,000
  - Testing and final V&V: $5,000
- Post-sales payments (paid as units sold): $100,000
  - Units 1-5: $25,000
  - Units 6-10: $25,000
  - Units 11-15: $25,000
  - Units 16-20: $25,000

**First Article Hardware: $35,000**
- 5 production-ready systems: $17,500 at order + $17,500 at delivery

**Production Unit Pricing (minimum 5-unit order):**
- 5 units: $7,250/unit
- 10 units: $6,550/unit
- 20 units: $5,975/unit
- 50 units: $5,125/unit

**Total Project Cost: $210,000**

## Notable Details

**Intellectual Property:**
- ReferenceTEK retains IP ownership of Hummingbird FDM model and all flight test reports and data
- BST retains IP of SwiftCore FMS core technology (generic multi-rotor features are separate from Hummingbird-specific customizations)

**Requirements Management:**
- Project specification defined in separate "Hummingbird II SwiftCore FMS Requirements" document (Rev 1.0, dated June 8, 2015)
- Changes after project kickoff treated as engineering change orders with potential price adjustments requiring mutual agreement

**Risk Mitigation:**
- Incremental payment schedule tied to milestone completion and ReferenceTEK approval reduces cost and schedule risk
- On-site personnel at ReferenceTEK facilities for integration and testing
- Simulator-first development approach to identify issues before flight testing

**Market Positioning:**
- Pricing reflects costs of: rapid development timeline, new simulation environment with HIL, novel flight dynamics model, innovative multi-rotor control system, SwiftTab customization, and on-site personnel