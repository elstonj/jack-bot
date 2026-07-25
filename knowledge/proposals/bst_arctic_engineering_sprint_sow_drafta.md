# Arctic UAS Engineering Sprint — Black Swift S3 Cold-Weather Configuration

## Document Metadata
- **Type:** Statement of Work (SOW) — Draft A for internal review
- **Client/Agency:** NexTech Solutions LLC (NTS) on behalf of Canadian Joint Forces Command (CJFC)
- **Program/Solicitation:** Arctic UAS Phase II — Engineering Sprint and Whitehorse Test Event
- **Date:** 24 July 2026
- **BST Products/Systems Referenced:** Black Swift S3 (tube-launched VTOL fixed-wing UAS), SwiftCore FMS, SwiftTab ground station, REX110-class EO/IR gimbal, long-range encrypted datalink
- **Key Personnel:** Jack Elston, Ph.D., Founder and CEO (BST point of contact)

---

## Executive Summary

Black Swift Technologies proposes to advance the S3 UAS from its current demonstrated operational floor of –30 °C to a cold-soak-qualified configuration suitable for sustained arctic operations, with demonstrated capability at –30 to –40 °C and a documented engineering path to –55 °C. The effort encompasses airframe and electronics requalification, battery thermal management, heated staging cases, integration of EO/IR and long-range datalink payloads, and demonstration at the Whitehorse test event (planned November 2026). The scope spans approximately six months (26 weeks) or a compressed 14–16 week sprint if aligned to a November event date.

---

## Technical Approach

### Core Cold-Weather Modifications (Tasks 2–5: ~1,100 hours)

**Task 2 — Airframe Cold-Weather Modification (~250 hours)**
- Change epoxy laminating resin system to extended-temperature-compatible formulation; qualify on structural coupons before flight articles.
- Characterize temperature-sensitive COTS components (servos, motors, actuators, bearings) and add localized heating where required.
- Specify and apply cold-rated lubricants and greases on all actuators and joints.
- Implement drained pitot-static installation with heated pitot and static ports to prevent moisture accumulation and freezing.
- Optional: increase propeller-to-ground clearance to ~8 inches for operation on unprepared snow surfaces.
- **Exit Criteria:** Coupon and surface test data showing structural integrity at temperature; documented lubricant and component selections; pitot-static installation verified free of moisture retention after cold-soak and thaw.

**Task 3 — BST-Produced Electronics Cold-Weather Modification (~750 hours — largest single element and principal schedule driver)**
- **Manufacturing Process Updates:**
  - Low-temperature-capable solder alloy, mechanical staking of large components, conformal coating of assembled boards.
  - PCB substrate change from FR4 to material with better low-temperature performance; requalify stack-up for impedance-controlled and high-current traces.
  - Requalify assembly and rework procedures under new process.

- **Component-Level Thermal Provisions:**
  - Add heating elements with thermostatic control to temperature-sensitive sensors: inertial measurement unit (IMU), differential pressure sensors, magnetometers.
  - Investigate supply board operating temperature; add heating or relocate assembly if margin inadequate.
  - Insulate avionics enclosure and provide conditioned volume so FMS boots from warm state.
  - Characterize total power consumption for active heating and confirm energy budget against mission endurance.
  - Review antenna placement for heated enclosures and revised case layout.
  - [Confirm scope] Convert aileron actuation to DroneCAN to reduce discrete wiring and improve cold-weather connector reliability.

- **Exit Criteria:** Boards built to updated process pass power-on, boot, and functional test at target temperature following four-hour soak; heating power draw characterized and within mission energy budget.

**Task 4 — Battery Thermal Management**
- Instrument battery packs; characterize cell temperature over representative mission profile starting from warm pack in ambient conditions at target floor.
- Validate hypothesis that self-heating under load maintains pack within limits once mission begins warm.
- If insufficient, add insulation first, then active thermostatically-controlled heating as secondary remedy.
- Define and document battery preconditioning and handling procedure for arctic crews, including maximum permissible cold exposure between case removal and launch.
- [Confirm scope] Modify airframe to permit battery swap without payload removal for gloved-hand operation.
- **Exit Criteria:** Instrumented mission-profile data showing cell temperature within limits from conditioned start; documented crew procedure with defined cold-exposure limit.

**Task 5 — Arctic Transit and Staging Case (~100 hours)**
- Add heating elements to both transport cases with external power input suitable for vehicle or snowmobile electrical system.
- Design and integrate temperature controller with setpoint control and over-temperature protection.
- Replace foam and padding with materials rated for extended temperature range, retaining current case external dimensions.
- Verify warm-up time from arctic ambient to staging temperature and corresponding power draw.
- **Exit Criteria:** Both cases hold staging temperature at target ambient on vehicle power; warm-up time and current draw documented.

### Integration and Qualification Tasks (Tasks 1, 6–10)

**Task 1 — Program Management, Systems Engineering and Test Planning**
- Maintain integrated sprint schedule with milestone gates aligned to Whitehorse event.
- Conduct kickoff technical interchange meeting to confirm requirements, operational vignettes, and success criteria.
- Produce Cold Weather Qualification Test Plan defining chamber protocol: complete air vehicle and ground station cold-soak to target temperature, minimum four-hour soak to thermal equilibrium, power-on, full avionics and FMS boot, motor spin-up, and datalink verification at temperature, with data logging and BST engineering witness.
- Perform thermal survey to identify temperature-sensitive components and instrument them for chamber campaign.
- Maintain requirements verification matrix traceable to questionnaire and SOW.

**Task 6 — Ingress Protection and Anti-Icing**
- Reseal enclosures; revise gasket and fastener details; add drainage paths at low points.
- Improve moisture management for melt-refreeze cycles (dominant ingress risk in arctic operation).
- Provide heated pitot and static provisions and evaluate leading-edge ice mitigation.
- Conduct IP testing to IP54 target rating.
- Note: Formal IP54 certification testing currently excluded from sprint estimate; CJFC to confirm whether certified rating or demonstrated performance required.

**Task 7 — EO/IR and BLOS Datalink Integration**
- Mechanical and electrical integration of REX110-class EO/IR gimbal into payload bay with power and thermal interface.
- Integrate long-range encrypted datalink and payload antenna; coordinate placement with antenna work.
- Verify video stabilization, image roll compensation, H.264/H.265 compression through integrated chain.
- Verify gimbal modes — object tracking, geolocation stare, manual slew — against FMS.
- Flight-test to confirm modeled range and endurance figures with payload installed.
- **Note:** Full BLOS range qualification is follow-on work; sprint deliverable is demonstrated integration, not fielded production configuration.

**Task 8 — Integrated Air Vehicle and Payload Control Station (BST internal funding)**
- Extend existing SwiftCore ground station to host payload control and video display.
- Design interface for gloved operation and legibility in high-glare snow conditions.

**Task 9 — Environmental Chamber Cold-Soak Qualification**
- Secure chamber access (Boulder-area facility to ~–20 °C; commercial facility budgeted for colder soak).
- Cold-soak complete air vehicle and ground station to target temperature for minimum four hours to thermal equilibrium.
- At temperature, perform power-on, full avionics and FMS boot, motor spin-up, datalink verification with data logging.
- Repeat over thermal cycles to expose intermittent failures and fatigue.
- **Exit Criteria:** Qualification report establishing demonstrated cold floor, with residual engineering path to –55 °C stated explicitly.

**Task 10 — Field Validation and Whitehorse Demonstration Support**
- Conduct cold-weather field flights at Colorado high-altitude winter site prior to deployment.
- Update crew procedures, checklists, operator handbook for arctic configuration.
- Ship system and batteries to Whitehorse with hazmat documentation.
- Provide two BST personnel on site for [8] days (setup, demonstration, teardown).
- Produce post-event report capturing performance against objectives and lessons learned.

---

## Products & Capabilities Described

### Black Swift S3 — Baseline and Modified Configuration

**Current Baseline (Pre-Modification)**
- **Type:** U.S.-manufactured, EAR99-controlled, tube-launched VTOL fixed-wing UAS.
- **Operational Temperature Floor:** –30 °C (established operationally, not by chamber qualification).
- **Operational Temperature Ceiling:** +46 °C.
- **Maximum Sustained Wind:** 30 kt.
- **Ingress Protection:** IP42/43, sealed avionics bay.
- **Airframe:** Carbon-fiber/polyamide, low thermal sensitivity.
- **Avionics:** SwiftCore FMS with temperature-tolerant COTS electronics.
- **Battery Provision:** Pre-flight preconditioning practice; no active heating.
- **Stored Footprint:** Two hard cases — airframe 62 × 27 × 13 in / 85 lb; payload and GCS 42 × 25 × 12 in / 75 lb.
- **Endurance and Range:** 160 km / 120 min with REX110 (modeled); 200 km / 150 min clean configuration.

**Arctic-Modified Configuration (Post-Sprint Deliverable)**
- **Target Cold Floor:** –30 to –40 °C demonstrated in environmental chamber; documented engineering path to –55 °C.
- **Ingress Protection:** IP54 target (up from IP42/43 baseline).
- **Airframe Resin:** Extended-temperature-compatible epoxy laminating resin.
- **Thermal Management:**
  - Heated, insulated avionics enclosure (conditioned volume for FMS warm boot).
  - Thermostatic heating of IMU, differential pressure sensors, magnetometers.
  - Drained, heated pitot-static installation.
  - Active battery thermal management (insulation + conditional heating as needed).
- **Cold-Weather Crew Burden:** Reduced to allow assembly, battery handling, and launch by two operators wearing arctic gloves, staging from heated case.
- **Heated Staging Cases:** External power input from vehicle/snowmobile electrical system; temperature control with setpoint and over-temperature protection.
- **EO/IR and BLOS Datalink Integration:** REX110-class gimbal with stabilized full-motion video and onboard recording; long-range encrypted datalink for BLOS command and video.

### SwiftCore FMS
- **Role:** Flight management system requalified for cold-start and sustained operation at target temperature.
- **Cold-Capability Provisions:** Insulated enclosure with conditioning; heating of sensitive sensors; requalified electronics manufacturing process.
- **Integration:** Unified control with SwiftTab ground station for air vehicle and payload.

### SwiftTab Ground Control Station
- **Enhancement:** Extended to host payload control and video display.
- **Arctic Ergonomics:** Interface designed for gloved operation and legibility in high-glare snow conditions.
- **Integration:** Single unified interface controlling both air vehicle and REX110 payload.

### REX110-Class EO/IR Gimbal
- **Capability:** Stabilized full-motion video and onboard recording.
- **Integration Status:** Demonstrated integration (sprint goal); full BLOS range qualification is follow-on work.
- **Integration Details:** Mechanical and electrical integration into S3 payload bay with power and thermal interface; video stabilization and H.264/H.265 compression; gimbal modes including object tracking, geolocation stare, manual slew.

### Long-Range Encrypted Datalink
- **Purpose:** Beyond-line-of-sight command and video transmission.
- **Integration:** Payload antenna placement coordinated with revised thermal and case configurations.
- **Sprint Goal:** Demonstrated integration supporting modeled 160 km / 120 min range with REX110 payload (subject to flight test validation).

### Arctic Transit and Staging Cases
- **Configuration:** Heated hard cases for airframe and payload/GCS.
- **Power Source:** External input from vehicle or snowmobile electrical system.
- **Thermal Management:** Heating elements with temperature controller (setpoint and over-temperature protection).
- **Materials:** Cold-rated foam and padding, extended temperature range.
- **Dimensions:** Retain current external dimensions (62 × 27 × 13 