# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin magnetometers with BST's aircraft platforms for magnetic signature detection applications. Key participants include Beck, Maciej, Tyler, Sam, and Alex from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), and Navy contacts. Activity spans from October 2025 through April 2026, covering Phase I completion and Phase II proposal submission and kickoff preparation.

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

**April 2026:**
- Cetacean budget reallocation: Decided to reduce Cetacean's subcontract in the Option period and reallocate ~$10K for other uses, since Cetacean is not continuing in Phase II
- Acoustic component approach: Continuing with separate aircraft for acoustic sensors; Navy requires drone-based solution for Phase II (April 17, 2026)

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
- Kickoff brief due April 14, 2026 - **SUBMITTED April 14, 2026**

## Action Items & Commitments

**Completed (April 2026):**
- Beck: Prepared and distributed Phase II kickoff brief template (April 6, 2026)
- Team: Updated kickoff brief template to include Option Period tasks
- Maciej: Reviewed and approved submission slidedeck (April 10, 2026)
- Alex: Reviewed and approved submission slidedeck (April 10, 2026)
- Meredith Needham: Submitted Kickoff brief, FWA Certification, and invoices to PIEE (April 14, 2026)

**Ongoing:**
- Beck: Researching formal process to modify Cetacean subcontract agreement and reduce their Option period tasks
- Maciej: Continue tracking Cetacean budget reallocation status
- Purchase QuSpin Gen-2.0 OTFM sensor ($11,775 budgeted)
- Complete quad chart update for Angel to share with Navy contacts
- Jack Elston: Evaluating potential acoustic component collaboration partner (April 17, 2026) - shared preliminary information without NDA
- Alex Lomis: Following up on acoustic payload options for Phase II aircraft platform

**Technical:**
- Sam offered to add magnetometer support to dronecan logging program
- Need to clarify flight certification requirements and Bartington sensor availability
- Update RPi data logger: add clock, increase baud rate, add WiFi controls

## Client & External References

**Navy Contacts:**
- Angel Ruiz-Reyes (TPOC) - primary Navy contact; kickoff meeting April 21, 2026
- Tony, Marc (London TechBridge), Ed
- Morris "DeSi" at DEVCOM
- Megan (Navy contact for submission coordination)
- Navy STP office (navystp.com)

**External Partners:**
- **QuSpin:** Jeff providing magnetometer expertise, loaning equipment, sharing Python calibration code
- **Ultra Maritime:** Paul - Phase 2 subcontractor ($300K base, $120K option)
- **University of Michigan:** Paul - subcontractor with budget negotiations
- **Cetacean:** Alex coordinating on sensor array design; reducing Option period involvement, ~$10K budget being reallocated
- **Bartington:** Sensor supplier for ground testing reference
- **Royal Navy:** Expressed interest in magnetometer technology
- **Potential acoustic partner:** Jack Elston evaluating collaboration for acoustic component (April 17, 2026); contact provided acoustic payload information; appears to be vehicle-focused company that integrates third-party sensors rather than developing their own

**Administrative:**
- Meredith Needham (PIEE) - submitted final kickoff and FWA documentation

## Recurring Topics & Themes

**Technical Challenges:**
- Magnetic interference management from aircraft motors and electronics
- Aircraft weight/size constraints for payload integration
- Balancing magnetic shielding vs. calibration approaches
- Remote data logging and WiFi control capabilities
- Acoustic sensor integration and platform compatibility

**Regular Activities:**
- Bi-weekly internal meetings, monthly meetings with subcontractors
- Progress reports and deliverable submissions
- Sensor testing at various distances and configurations
- CAD design iterations for different aircraft configurations
- Phase II kickoff planning and milestone tracking
- Vendor and partnership evaluation for complementary capabilities

**Administrative/Contracting:**
- Formal subcontract modifications for scope changes
- Budget reallocation and task reduction processes

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
- April 9: Beck pinged team regarding kickoff brief progress
- April 10: Maciej and Alex confirmed satisfaction with submission slidedeck; Beck confirmed PDF will be finalized Monday before meeting
- April 10: Maciej raised question about Cetacean budget reallocation (~$10K) since they're not continuing in Phase II; Beck confirmed formal subcontract modification process will be required
- April 14: **Meredith Needham submitted Phase II Kickoff brief, FWA Certification, and invoices to PIEE** - all administrative Phase II startup items complete
- April 17: Jack Elston identified potential acoustic component collaboration partner; shared materials without NDA restriction. Alex Lomis noted promising acoustic payload option from this vendor. Maciej confirmed Navy requirement for drone-based acoustic solution in Phase II, ruled out vehicle-based options.
- Navy kickoff meeting confirmed for April 21, 2026 with Angel Ruiz-Reyes

**Project Status:** Phase II is now officially launched with all required submissions completed. Team is prepared for Navy leadership kickoff meeting on April 21. Budget