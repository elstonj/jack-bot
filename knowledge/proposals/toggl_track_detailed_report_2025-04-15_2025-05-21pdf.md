# Toggl Track Detailed Report: S0 Hurricane Phase II (04/15/2025 – 05/21/2025)

## Document Metadata
- Type: Time tracking report
- Client/Agency: NOAA
- Program/Solicitation: [301-3] S0 Hurricane Phase II - 2025 / Joe Cione (NOAA contact)
- Date: Report period 04/15/2025 – 05/21/2025 (generated 05/22/2025)
- BST Products/Systems Referenced: S0 (UAS platform)
- Key Personnel: Josh Fromm, Sam Hild, Jack Elston, Ethan Domagala, Nate, Stachura, Alex, Austin Vera

## Executive Summary
This is a detailed time-tracking report for the S0 Hurricane Phase II project under NOAA contract with researcher Joe Cione. The report documents 416 hours 24 minutes 36 seconds of labor across a 37-day period (mid-April through mid-May 2025), spanning hardware construction, avionics integration, sensor testing, and software development.

## Project Activities & Technical Work

### Hardware Construction & Assembly
- **Parachute Tube Construction**: Ethan Domagala led assembly of deliverable components (04/16-04/17)
- **Latch System Work**: Countersinking, beveling, drilling, and grinding of latch components (04/28, 05/07)
- **MHP (likely sensor/payload housing) Assembly**: Potting, sticker cover installation (05/07, 05/20-05/21)
- **Arming System**: Arming switch and arming lock bar work (04/18)
- **Deployment Battery Integration**: Assembly and integration (04/18)

### Avionics & Sensor Testing
- **VLD1 Driver/Radar Altimeter Testing**: Extensive setup and testing led by Sam Hild (04/15, 04/17-04/18, 04/22, 04/28, 05/01-05/02, 05/06, 05/08, 05/12)
  - New VLD1 board testing initiated (05/08)
- **Autopilot Setup**: Jack Elston configured autopilot systems (05/10-05/11)
- **Avionics Testing**: General avionics bench testing (05/13)

### Real-Time Kinematic (RTK) Positioning System Development
- **Moving Base RTK**: Extensive development and debugging (04/30, 05/02, 05/05-05/08, 05/12, 05/19-05/21)
  - Fixed lost RTCM packets in base station buffering (05/06)
  - Testing rover RTCM forwarding (05/07-05/08)
  - Fixed UBX send frequency problem (05/12)
  - UBX zero relpos bug debugging and feature development (05/12)
  - RTCM verification tools development (05/08)
  - S0 wiring diagrams for RTK system (05/19-05/21)

### Integration & Documentation
- **Wiring Diagrams**: Detailed S0 wiring diagrams created by Sam Hild (05/19-05/21)
- **Presentation Preparation**: Jack Elston worked on presentation materials (04/28-04/29, overnight)

### Team Meetings & Industry Engagement
- **Bi-weekly Prep Meetings**: ET (Extended Target?) pre-season testing planning meetings (04/16, 05/13) for 8-30 June timeline
- **UAS Hurricane Symposium Attendance**: Jack Elston and team attended (05/01-05/02)
- **ET Industry Needs Discussion**: Jack Elston (05/05)
- **UK ET Summit Preliminary Discussions**: Jack Elston (05/06)
- **S0 Project Meeting**: Team coordination (05/07)

## Technical Systems & Components

### Primary Systems
1. **S0 Platform**: UAS designed for hurricane operations
2. **VLD1 Radar Altimeter**: Primary sensor undergoing integration and testing
3. **Moving Base RTK Navigation**: Custom real-time kinematic positioning system with base station and rover components
4. **Autopilot**: Flight control system being configured
5. **Parachute Deployment System**: Recovery mechanism with deployment battery and arming switch

### Software/Firmware Work
- RTCM (Radio Technical Commission for Maritime Services) packet handling and forwarding
- UBX (u-blox) protocol implementation and debugging
- Base station buffering and data forwarding logic
- RTCM verification tools

## Notable Details

### Team Structure
- **Leadership/Engineering**: Josh Fromm (full-time presence on project), Jack Elston (meetings, autopilot, presentations)
- **Avionics/Sensor Lead**: Sam Hild (VLD1 testing, RTK development, wiring)
- **Hardware/Mechanical**: Ethan Domagala (primary fabrication), Austin Vera (support)
- **Avionics Support**: Nate (assembly, testing, avionics)
- **Software/Integration**: Alex (appears mid-May, avionics work)

### Workload Patterns
- Significant evening/weekend work by Josh Fromm (multiple 06:00 PM - 09:00/10:00 PM sessions)
- Intensive RTK software development by Sam Hild in final week
- Heavy mechanical construction in late April, shifting to electrical/wiring integration in May

### Key Milestones/Deadlines
- Pre-season testing scheduled for June 8-30 (biweekly prep meetings through May)
- Presentation completed/updated end of April
- UAS Hurricane Symposium engagement (05/01-05/02)
- International outreach (UK ET Summit preliminary discussions)

### Deliverable Status (as of 05/21)
Construction of all components appears substantially complete by end of period, with focus shifting to final assembly, wiring integration, and functional testing in preparation for June field operations.