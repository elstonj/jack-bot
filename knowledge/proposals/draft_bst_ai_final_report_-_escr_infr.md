# Draft BST AI Final Report - ESCR & INFR

## Document Metadata
- **Type:** Final Report (Grant Performance Report)
- **Client/Agency:** Colorado Advanced Industries Accelerator Grant Program
- **Program/Solicitation:** Advanced Industries Accelerator Grant Program
- **Grant Award No.:** CTGG1-2023-3372
- **Grant Award Amount:** $250,000.00
- **Grant Period:** 2/22/23 – 2/29/24
- **Date Submitted:** 2024-02-16 (last edit; document marked as draft)
- **BST Products/Systems Referenced:** S2 (aircraft platform), Q3 sensor (methane detection), MLD (Methane Leak Detection payload)
- **Key Personnel:** Advisory board includes three senior O&G industry execs; Danny Jimenez (advisory board member, involved in business development); no other BST staff named

## Executive Summary
Black Swift Technologies received a $250,000 Colorado Advanced Industries grant to develop and pilot a methane leak detection (MLD) capability on its S2 UAS platform for oil & gas applications. The program successfully completed initial demonstrations with anchor customer PDCE (now Chevron) in Q3 2023, revealing an unexpectedly powerful capability to map methane flux across multi-km areas using eddy covariance analysis. However, deployment timelines were extended by 9 months due to technical challenges (sensor thermal drift, sophisticated data analysis development) and resource constraints, pushing MVP completion and customer deployment into Q2 2024.

## Technical Approach

### Core Technology
- **Platform:** S2 unmanned aircraft system (UAS)
- **Sensor:** Q3 methane detection sensor (second article built under grant)
- **Novel Analysis Method:** Flux mapping via eddy covariance technique that uses "wind memory" to identify methane leak sources
  - Enables survey of 4km × 4km areas with only 5-10 downwind passes
  - Produces visual "flux maps" showing leak distribution and magnitude

### Development Strategy
1. **Integration:** Q3 sensor integrated to S2 platform
2. **Field Testing:** Iterative testing at BST facility (Longmont area) and customer sites
3. **Analytics Development:** Custom backend analysis tools for flux mapping (committed internal IR&D of $70K beyond grant funding)
4. **UI/UX:** Development of graphical flux map visualization for stakeholder communication

### Key Technical Challenges Encountered
1. **Sensor thermal drift:** Heat dissipation issue from disconnected heatsink inside aircraft
2. **Data analysis complexity:** Discovered more sophisticated eddy covariance technique than initially planned, requiring extended development
3. **Autonomous flight autonomy validation:** Confirmed ability to autonomously execute survey patterns at required methane sensitivity
4. **Logistics optimization:** Determining flight patterns, geographic landing requirements, and operational constraints

## Products & Capabilities Described

### S2 Aircraft
- Multi-rotor UAS platform capable of autonomous survey operations
- Integrated methane detection payload
- Autonomous navigation for systematic survey patterns
- Used for methane leak detection in oil & gas wellsites and surrounding areas

### Q3 Methane Sensor
- Methane-specific detection sensor
- Integrated to S2 for airborne measurement
- Sensitivity sufficient for regional (multi-km scale) leak detection
- Second article built under grant; first successful demonstration January 2023 at BST facility

### MLD (Methane Leak Detection) Capability
- Complete system for detecting and mapping methane emissions
- Can measure leakage rates from individual wellsites
- Can map methane sources across multi-km areas (40+ wells in single flight)
- Generates flux maps showing leak distribution and magnitude
- Also demonstrated on S2 MLD payload for high-altitude coal mine applications

### Analytics Backend (In Development)
- Eddy covariance-based flux mapping algorithm
- Wind memory analysis to isolate leak sources
- MVP expected Q2 2024
- BST invested additional $70K in development beyond grant

## Use Cases & Applications

### Oil & Gas Wellsite Monitoring (Primary)
- **Anchor Customer:** PDCE/Chevron
  - Initial test Q3 2023 on single wellsite
  - Demonstrated ability to identify whether emissions originated from wellsite or surrounding area
  - PDCE case: determined wellsite was minimal contributor; surrounding wetlands primary source
  - Result: powerful regulatory/public communication tool
  - C-level interest at Chevron Ventures for further testing and potential investment
  
- **Early Adopter:** Crowheart Energy (Wyoming)
  - Manufacturing Service Agreement (MSA) executed December 2023
  - MOU in place with expectation to begin pilot Q2 2024
  - Intended use: survey production wellsites for methane leaks

### Abandoned Coal Mine Methane Detection
- $60K contract with Delta Climate (introduced through AIA pitch bootcamp)
- Objective: evaluate S2 MLD capability to sense methane release from abandoned coal mines
- High-altitude mountain testing near Carbondale, CO
- Timing: pushed from mid-2023 to later in year due to platform availability

### Regulatory Validation
- Scheduled first flights with METEC (CSU-sponsored, government-certified Methane Leak Detection certification site) for Q2 2024
- Objective: establish validation pathway for platform certification
- Target: Colorado DNR well remediation programs

### Emerging Opportunities (Identified but Not Yet Pursued)
- Landfill methane leak management
- Carbon capture from methane leak detection (coal mines)

## Key Results

### Successful Milestones
1. **System Integration:** Q3 sensor successfully integrated to S2
2. **Initial Flight Demonstration:** January 2023 at BST Longmont facility
3. **Customer Pilot Testing:** PDCE wellsite survey Q3 2023 qualitatively successful
4. **Flux Mapping Capability:** Discovered ability to map methane across 4km × 4km areas with 5-10 passes (unexpected advantage from delayed testing)
5. **Analytics Development:** Eddy covariance analysis tool development progressing; BST committed $70K internal funding due to capability exceeding expectations
6. **Advisory Board:** Established with three senior O&G industry executives, generating business development leads
7. **Business Development:** Partnership with Crowheart Energy (MSA + MOU executed)
8. **Contract Revenue:** $60K contract with Delta Climate for coal mine testing

### Delayed Milestones
- **MVP Configuration:** Originally expected sooner; now projected Q2 2024
- **Initial Trial Deployments:** Pushed 9 months out; now expected after MVP validation
- **Full Deployment:** 9-month delay from original schedule
- **Subsequent Customer Deployment:** Delayed correlatively

### Investment & Capital
- **IR&D Investment:** $70K (BST internal funding, beyond grant)
- **Capital Equipment:** $30K methane detection sensor acquisition
- **Total Company Investment:** $100K ($70K development + $30K equipment)
- **Follow-On Funding:** None closed yet; investors (including Chevron Ventures) positioned to commit upon successful MVP demonstration
- **Contingency:** Full-time O&G BD/Sales hire pending $1M–$2M pre-seed raise, itself contingent on MVP success

### Jobs
- **FTEs Created:** 0
- **FTEs Retained:** All existing FTEs retained
- **Consultants Added:** 3 part-time consultants hired for project support

### Intellectual Property
- Provisional patent in development for Methane Leak Detection UAS

## Notable Details

### Customer Evolution & Market Reception
- **PDCE (now Chevron):** Initial skepticism around wellsite responsibility; flux mapping results provided unexpected value proposition for demonstrating low-impact wellsites to regulators and public. Escalated interest to Chevron Ventures C-level.
- **Crowheart Energy:** Strong commitment signaled through executed MSA and MOU; positioned as first paying customer pending MVP validation.
- **Delta Climate:** Unsolicited interest from new customer class (coal mine methane) discovered through grant bootcamp introduction.

### Technical Insight
The delay in MVP delivery inadvertently created a competitive advantage: extended field testing and analysis development resulted in discovery of more sophisticated eddy covariance flux mapping technique than originally envisioned, transforming product from simple leak detection to regional flux mapping covering 4km × 4km areas in single flight.

### Business Strategy
- **Near-term:** Complete MVP → deploy with Chevron and Crowheart → catalyze investment
- **Medium-term:** Secure $1M–$2M pre-seed to fund full-time sales/marketing and scale-up
- **Longer-term:** Expand to coal mining, landfill, and other methane-detection verticals
- **Timeline:** Revenue expected summer 2024; investment closure expected within 3 months of MVP demonstration

### Grant Impact Assessment
- Grant funding catalyzed Q3 sensor expedited delivery (January 2023 demo)
- Enabled customer pilot with PDCE, generating industry traction
- Funded stand-up of advisory board (industry connections)
- Enabled partnership with Crowheart (MSA/MOU)
- Generated contract opportunity with Delta Climate

### Regulatory & Certification Path
- CSU/METEC validation flights scheduled Q2 2024
- Colorado DNR conversations ongoing
- Certification strategy aligned with state/federal regulatory requirements (details not specified in report)

---

## Document Quality Notes
- **Status:** Marked as draft; appears substantially complete but may have incomplete sections (Project Budget/Expenditures section 12 is blank; section 11 "Other Commercial Progress" is brief)
- **Tone:** Professional; candid about delays and reasons; emphasizes unexpected positive outcomes
- **Data Gaps:** Specific sensor specifications not provided; exact MVP feature list not detailed; names of most BST staff members withheld