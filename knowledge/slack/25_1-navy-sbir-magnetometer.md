# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin magnetometers with BST's aircraft platforms for magnetic signature detection applications. Key participants include Jack, Beck, Maciej, Tyler, and Sam from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), and Navy contacts. Activity spans from October 2025 through April 2026, covering Phase I completion and Phase II proposal submission and kickoff preparation.

## Key Decisions

**October 2025:**
- Magnetometer positioning: Decided to position sensor 2.5-5ft from motor with MuMetal shielding
- Shielding approach: MuMetal encasing around motor with short shaft design
- S0 aircraft modifications: 3x wing area increase to handle 1.3kg payload

**January 2026:**
- Partner selection: Chose Ultra Maritime over CRT as Phase 2 subcontractor
- Sensor approach: Decided on separate aircraft for magnetometer and acoustic sensors (not combined)
- Battery selection: Switch to pouch battery cells to reduce magnetic interference
- Computing: Add Google Coral TPU for compute needs (~2W power vs higher GPU power)

**March 2026:**
- TCE participation: Decided NOT to participate in April TCE due to early development status
- Will plan for August TCE when system is more mature
- Technical approach: Task O.2 will use simulated classified model to avoid SCIF/clearance requirements

## Projects & Initiatives

**Phase I (Completed January 2026):**
- Status: Final Report and TABA successfully submitted January 11-12, 2026
- Payments: Final $20k payment received
- Technical achievements: Magnetic noise target of ~30 pT RMS (half Navy requirement of 3 pT/sqrt(Hz))

**Phase II (April 2026 - ongoing):**
- Budget: $1.4M over 30 months
- Proposal submitted March 27, 2026 (one day extension)
- Contract signed March 25th, option start date April 12, 2026
- Planned: 4 experimentation events, 6 S0-AD aircraft (4 base + 2 option)
- Phase II kickoff meeting scheduled with Navy TPOC Angel Ruiz-Reyes for April 21, 2026
- Kickoff brief due April 14, 2026

## Action Items & Commitments

**Immediate (April 2026):**
- Beck: Prepare and distribute Phase II kickoff brief using template (due April 14, 2026)
- Team: Update kickoff brief template to include Option Period tasks
- Beck: Schedule kickoff meeting with Angel for April 21, 2026 (confirmed)

**Ongoing:**
- Maciej: Review University of Michigan SOW for potential task cuts
- Purchase QuSpin Gen-2.0 OTFM sensor ($11,775 budgeted)
- Complete quad chart update for Angel to share with Navy contacts

**Technical:**
- Sam offered to add magnetometer support to dronecan logging program
- Need to clarify flight certification requirements and Bartington sensor availability
- Update RPi data logger: add clock, increase baud rate, add WiFi controls

## Client & External References

**Navy Contacts:**
- Angel Ruiz-Reyes (TPOC) - primary Navy contact
- Tony, Marc (London TechBridge), Ed
- Morris "DeSi" at DEVCOM
- Megan (Navy contact for submission coordination)
- Navy STP office (navystp.com)

**External Partners:**
- **QuSpin:** Jeff providing magnetometer expertise, loaning equipment, sharing Python calibration code
- **Ultra Maritime:** Paul - Phase 2 subcontractor ($300K base, $120K option)
- **University of Michigan:** Paul - subcontractor with budget negotiations
- **Bartington:** Sensor supplier for ground testing reference
- **Cetacean:** Alex coordinating on sensor array design
- **Royal Navy:** Expressed interest in magnetometer technology

## Recurring Topics & Themes

**Technical Challenges:**
- Magnetic interference management from aircraft motors and electronics
- Aircraft weight/size constraints for payload integration
- Balancing magnetic shielding vs. calibration approaches
- Remote data logging and WiFi control capabilities

**Regular Activities:**
- Bi-weekly internal meetings, monthly meetings with subcontractors
- Progress reports and deliverable submissions
- Sensor testing at various distances and configurations
- CAD design iterations for different aircraft configurations
- Phase II kickoff planning and milestone tracking

## Important Resources

**Code & Documentation:**
- Code location: payload/quspin directory
- QuSpin Python calibration code shared by Jeff
- TCE planning brief (CUI - Controlled Unclassified Information)
- Phase II Kickoff Brief template: https://docs.google.com/presentation/d/1OU8JXlp_XGyqt6y0LFuRqlQAQD6UGa9f3xG3R9C-dJs/edit?usp=sharing

**Testing Facilities:**
- Fredericksburg Geo Facility (recommended by TPOC)
- Table Mountain, Boulder (recommended calibrated test site)
- Magnetic test chamber consideration ($70K for 2m version)

**Technical Specifications:**
- Navy magnetic noise requirement: 3 pT/sqrt(Hz)
- Current performance: ~30 pT RMS
- Motor specs: ~10k RPM (167 Hz revolution, 2338 Hz magnetic pole swapping)
- Sensor positioning: 35" from motor in S0 aircraft design

## Recent Activity

**April 2026:**
- Beck distributed Phase II kickoff brief template on April 6th
- Kickoff brief due April 14, 2026 (8 days prior to Navy meeting)
- Navy kickoff meeting scheduled for April 21, 2026 with Angel Ruiz-Reyes
- Brief template requires update to include Option Period tasks
- Transition to Phase II active planning and formal coordination with Navy leadership

The project has successfully transitioned from Phase I completion to Phase II execution, with formal kickoff preparations underway. Strong Navy support continues with scheduled leadership meetings to align on Phase II execution strategy.