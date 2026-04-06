# Hummingbird SwiftCore FMS Project Overview

## Document Metadata
- Type: Development and Integration Project Plan (DRAFT)
- Client/Agency: Reference Technologies (ReferenceTEK)
- Program/Solicitation: Custom development contract for Hummingbird II UAV
- Date: September 22, 2015
- BST Products/Systems Referenced: SwiftCore FMS, SwiftPilot, SwiftStation, SwiftTab
- Key Personnel: Not named in document

## Executive Summary
Black Swift Technologies proposed a custom development and integration effort to adapt its SwiftCore Flight Management System for the Hummingbird II, a unique ducted-fan multi-rotor UAV made by Reference Technologies. The project involved developing a flight dynamics model, simulation environment with HIL testing, novel multi-rotor control algorithms, and modified interfaces, with a 23-week timeline and $175k development budget plus $20k for two prototype systems.

## Technical Approach

**Vehicle Architecture:**
- Hummingbird II features a central ducted fan with counter-rotating blades
- 6 external rotors (expandable to 8) called Dynamic Propulsion Units (DPUs)
- Hybrid power system: on-board combustion engine with generator + battery system for load balancing
- Central duct and external DPUs use angled configuration for yaw stabilization

**Development Strategy:**
- Customize existing SwiftCore FMS base architecture for Hummingbird-specific requirements
- Create functional simulation environment with Hardware-in-Loop (HIL) testing and real-time visualization
- Develop flight dynamics model (FDM) specific to Hummingbird II
- Design control system utilizing central duct for altitude/speed control and external DPUs for attitude control
- Modify SwiftTab interface for improved vehicle control and situational awareness
- Incremental development and testing approach across 9 milestone blocks to reduce schedule and cost risks

**Project Structure:**
- 15 weeks software development
- 4 weeks system checkout (verification & validation testing)
- 4 weeks field testing support
- Completion targeted for end of Q1 2016

## Products & Capabilities Described

**SwiftCore FMS:**
- Flight management system customized for multi-rotor VTOL applications
- Designed to control unique Hummingbird II propulsion architecture
- Consists of three integrated components:

**SwiftPilot:**
- Flight control hardware component
- Includes Microhard 900 MHz radio modem (standard equipment)
- Cost: $5,125-$7,250 per unit depending on order quantity (Tables 3-4)

**SwiftStation:**
- Ground station component
- Includes Microhard 900 MHz radio modem (standard equipment)

**SwiftTab:**
- User interface tablet (standard Samsung Galaxy Tab 10.1)
- Modified for Hummingbird II-specific control and situational awareness
- Custom development required for this application

## Deliverables

1. Functional simulation environment with HIL testing and real-time visualization
2. Flight dynamics model (FDM) of Hummingbird II for simulator
3. Custom SwiftCore FMS control system designed specifically for Hummingbird II
4. Modified SwiftTab interface for Hummingbird II operations
5. Summary report detailing flight testing results and performance metrics
6. Two (2) prototype SwiftCore FMS units for integration and testing

## Use Cases & Applications

- Hummingbird II multi-rotor UAV operations in unspecified mission profiles
- VTOL (vertical takeoff and landing) autonomous flight operations
- Extended endurance missions (hybrid combustion-electric power system enables longer flight times than battery-only systems)

## Key Results

This is a project plan document (draft), not a completion report. No test results or performance data are included. The document was created in September 2015 with a proposed start date of October 5, 2015.

## Notable Details

**Intellectual Property:**
- ReferenceTEK retains ownership of the Hummingbird FDM simulation model
- ReferenceTEK retains all flight test reports and data specific to Hummingbird
- SwiftCore FMS technology and general multi-rotor capabilities remain BST property

**Budget Structure ($195k total):**
- $175k development effort
- $20k for two prototype units
- Development payments ($75k) tied to milestone completion with ReferenceTEK approval
- Post-sales payments ($100k) spread across production unit sales (5-unit increments at $25k per 5 units)
- Prototype units cost significantly higher ($10k per unit) due to customization and 3-week delivery timeline
- Production units: $5,125-$7,250 per unit (5-50 unit orders)

**Risk Management:**
- Fixed-price contract with milestone-based payments
- Cost/payment sharing between parties: upfront development ($75k), post-sales recovery ($100k)
- Engineering Change Orders (ECOs) process for requirements changes after Week 3
- Approval feedback loop required from ReferenceTEK before task completion
- Minimum 5-unit order requirement for production systems; 5-week lead time for first article

**Responsibilities:**
- BST: Software development, simulation, integration support, on-site engineering, field testing support
- ReferenceTEK: Electrical and mechanical integration, regulatory/FAA approvals, field testing leadership, production system shipment

**Requirements Document:**
- Detailed specifications in separate "Hummingbird II SwiftCore FMS Requirements" document (revision 1.0, dated June 8, 2015)