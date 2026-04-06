# Autonomous Quad-Biplane Flight Controller Interim Report

## Document Metadata
- Type: Monthly progress report (Month 2)
- Client/Agency: Creare
- Program/Solicitation: Contract Number S649
- Date: 2019-07-20
- BST Products/Systems Referenced: SwiftPilot (flight controller), SwiftTab (user interface)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This interim report documents Month 2 progress on an autonomous quad-biplane flight control system for Creare. The primary work involved integrating the Double Eagle aircraft dynamics model into the Gazebo simulator and conducting software-in-the-loop (SIL) testing of the SwiftPilot autopilot. Simulations demonstrated successful hover and forward flight control of the 12kg light version of the aircraft.

## Technical Approach
BST's approach focused on simulation-driven development:

1. **Motor/Propeller Modeling**: Created empirical models from KDE motor/propeller specifications using thrust vs. RPM² curve fitting to validate linear thrust characteristics.
   - Selected hardware: KDE7215XF-135 motor, KDE-CF275-DP propellers
   - Battery: 8S LiPo (33.6V, two 4S packs in parallel)
   - Empirical data from KDE website fitted to controller and Gazebo models

2. **Aerodynamic Modeling**: Incorporated XFLR5 aerodynamic model from Creare to define wing and fuselage behavior in Gazebo

3. **Aircraft Dynamics Integration**: Imported STL model with accurate mass, inertia, and rotor locations into simulation environment

4. **Flight Controller Tuning**: Tuned SwiftPilot autopilot in software-in-the-loop simulation, including roll and pitch control loops

5. **Simulated Flight Testing**: Performed test flights of the 8S 12kg light configuration in hover and forward flight regimes

## Products & Capabilities Described

### SwiftPilot
- BST's autonomous flight controller
- Designed to manage transitions between hover and forward flight modes
- Successfully tuned in software-in-the-loop simulation
- Demonstrated stable control in hover and forward flight
- Transition controller noted as still in development

### SwiftTab
- User interface for flight controller
- Displays real-time control loop data (roll, pitch)
- Used for flight tuning and monitoring during simulations

## Use Cases & Applications
- VTOL (Vertical Takeoff and Landing) aircraft operations
- Quad-biplane configuration for extended flight endurance
- Autonomous flight with automatic hover-to-forward flight transitions

## Technical Results
- **Hover Test**: Software-in-the-loop simulation demonstrated stable hover behavior for the Double Eagle aircraft
- **Forward Flight Test**: Successful simulated forward flight with good aircraft behavior in tested regimes
- **Motor Model Validation**: Thrust vs. RPM² relationship confirmed as linear through zero, validating empirical model
- **Control Tuning**: Roll and pitch control loops successfully tuned in simulation environment

## Notable Details
- Aircraft configuration: 8S 12kg light version of Double Eagle
- Transition controller between hover and forward flight still in development at time of report
- Motor/propeller models incorporated slightly different assumptions between Gazebo simulator and flight controller model
- Work was structured in monthly milestones with forward flight analysis planned for subsequent reporting period
- Direct references to external component specifications (KDE motor/prop datasheets) provided for traceability