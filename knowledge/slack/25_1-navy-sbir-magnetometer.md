# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin magnetometers with BST's aircraft platforms for magnetic signature detection applications (MAD - Magnetic Anomaly Detection). Key participants include Beck Cotter, Maciej, Tyler, Sam Hild, Alex Lomis, Joshua Fromm, Jack Elston, and Ethan Domagala from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), Navy DEVCOM (Morris "DeSi"), Navy TPOC (Angel Ruiz-Reyes), Royal Navy contact Simon, Lockheed Martin UK (LMUK), and external consultant Eric Correa. Additional BST staff include Meredith Needham (administrative/coordination) and Dan Prendergast. Activity spans from October 2025 through July 2026, covering Phase I completion, Phase II proposal submission, kickoff, and ongoing Option period development with flight testing preparation and sensor optimization work.

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
- TCE participation: Decided NOT to participate in April TCE due to early development status; planning for August TCE when system is more mature
- Technical approach: Task O.2 will use simulated classified model to avoid SCIF/clearance requirements

**April 2026:**
- Cetacean budget reallocation: Reduce Cetacean's subcontract in Option period and reallocate ~$10K for other uses, since Cetacean not continuing in Phase II (April 20, 2026)
- Acoustic component approach: Continuing with separate aircraft for acoustic sensors; Navy requires drone-based solution for Phase II
- CRT subcontract closure: CRT has invoiced only ~$2K of their Base Period allocation; remaining $8.5K plus all option funds available for reallocation (April 20, 2026)
- August Camp Pendleton demo: Confirmed as primary Option focus; will reallocate CRT funds for travel and demo costs (April 20-21, 2026)
- Reusable MAD S0 design: Decided to use stock S0 with smaller commercial LiPo battery, new antenna, and launch rail rather than hand-launch variant (April 22, 2026)
- Landing gear: Fixed spline (vs wing swivel), small wing tip skids to keep wings level on landing (April 22, 2026)
- Launcher development: Deferred CAD/explosive launch development to Phase II; focus Option period on manual hand-throw launch from UH-60 (April 21, 2026)
- Future launcher approach: Estes rocket assist identified as solution for boat/vehicle-based launches; tube-launched system for non-recoverable boat-based deployment (April 23, 2026)

**May 2026:**
- S0-MAD Reusable flight article: Reuse as many parts as possible from the ADONIS S0 rather than building a new aircraft (May 6, 2026)
- Ground test rig: Bartington sensor successfully integrated mechanically (May 6, 2026)
- Bartington logging approach: CSV format output selected for sensor data logging (May 27, 2026)
- Flight test methodology: 1-hour test of each logger deemed sufficient to satisfy Navy TPOC Angel Ruiz-Reyes requirements (May 27, 2026)
- Bartington sensor test configuration: Sequential 1-hour test runs for each sensor (Bartington and QuSpin) with aircraft off, planned as initial baseline validation (May 28, 2026)
- QuSpin filter configuration: Decision pending on 10Hz low-pass filter enablement for next test week; need to verify custom filter options available in QuSpin profile loading feature per Jeff (May 29, 2026)

**June 2026:**
- Electrical integration investigation: Potential source of increased magnetic noise identified—magnetometer now electrically connected to aircraft powered by aircraft regulator (vs. previous independent USB battery) and integration of carbon boom (June 1, 2026)
- Bartington sensor power isolation strategy: Decision to use isolated supply/comms for Bartington sensor due to extreme susceptibility to electronic noise (requires <1mV ripple on power supply) (June 2, 2026)
- ADC selection: Decided to pursue 24-bit ADC (or dual 24-bit ADCs interfaced via I2C) to achieve 1μV resolution required for Bartington sensor logging (June 2, 2026)
- Custom PCB approach: Agreed to design quick-turn PCB for isolated power supply and high-resolution ADC integration rather than using breakout boards (June 2, 2026)
- Eric Correa follow-up coordination: Maciej flagged need for team to reach out to Eric Correa with any remaining questions before his leave (June 3, 2026) - he is off duty after June 4th for a couple of weeks
- ADONIS S0 radio specification: Clarified that the S0 aircraft being used from ADONIS for flight testing uses a 430 radio (Microhard type to be confirmed) (June 4, 2026)
- Deployment tube checklist: Sam Hild to update and send deployment tube checklist for approval; Jack Elston requesting schematic review from Sam Hild (June 5, 2026)
- Custom PCB design fixes: Sam Hild fixed ADC 3.3V supply connection issue (U1 pin 26, C2+C4 isolation in inner copper) and JP1 jumper wiring; updates pushed and board ordered (June 9, 2026)
- QuSpin power isolation approach: Maciej requesting similar isolated power setup for QuSpin sensor as developed for Bartington to restore sensor accuracy from earlier performance (June 10, 2026)
- QuSpin power supply testing: Maciej to take over testing of QuSpin power supply while Sam Hild focuses on S3 development; testing focused on verifying noise reduction effectiveness (June 12, 2026)
- Bartington sensor model confirmation: Identified as UAS Mag PC298 with 105 µT range (June 16, 2026)
- Launcher parts procurement: Approved ordering launcher design parts totaling $1.3K from McMaster (June 22, 2026)
- Magnetometer power supply: Sam Hild identified that magnetometer draws ~1A at 5V (higher than expected); current LDO is 500mA max and causing under-voltage/current condition preventing output. Maciej requested quick-turn procurement of higher-capacity LDO; Sam Hild to check existing inventory first (June 23, 2026)
- TCE event dates: Originally planned for August 17-28, rescheduled to September 14-24 at Camp Pendleton (June 29, 2026)

**July 2026:**
- QuSpin firmware update approach: Decided to send QuSpin sensor back to manufacturer for firmware update and QC check rather than conducting testing in current "noisy mode" (July 7-8, 2026). Rationale: Quick turnaround expected from vendor for firmware update and configuration optimization, preferable to testing with known suboptimal settings.
- Royal Navy Q2 2027 helicopter drop specs: Open to all S0 options (S0-weather, S0-MAD, or S0 with onboard camera); would be dropped over ocean near airbase, ground-controlled initially (similar to C-130 setup), and recovered at airfield. Onboard video recording requested as marketing tool for project expansion (July 8, 2026)
- Royal Navy long-term pricing target: $10K per unit for quantity 100+ orders
- GPS jamming contingency: Decided to add RC receiver capability