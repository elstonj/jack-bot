# RAVEN UAS - Procurement Specification (Draft SOW)

## Document Metadata
- Type: Statement of Work (SOW) and Procurement Specification (Draft)
- Client/Agency: Lockheed Martin UK Ltd (LMUK RMS); Royal Navy (implied end customer)
- Program/Solicitation: RAVEN UAS Programme
- Date: 29 July 2026 (Created/Modified); 16 July 2026 (Draft Issue)
- BST Products/Systems Referenced: None explicitly named; Black Swift Technologies is the subcontractor/supplier
- Key Personnel: 
  - Alasdair Brackenridge (Subcontract Programme Manager, Author)
  - Beck Cotter (Last Editor)
  - Lead Systems Engineer (TBC - approval authority)

## Executive Summary
This is a draft procurement specification and Statement of Work for Lockheed Martin UK to procure 12 RAVEN unmanned air systems (UAS variants TBD) from Black Swift Technologies. The document establishes configuration management, quality assurance, testing, documentation, training, and support requirements aligned with UK defence standards (DEF STAN) and ISO 9001:2015 quality accreditation.

## Statement of Work Overview

### Manufacturing & Delivery (SOW-1)
- Supply and manufacture of **12 UAS** (variants to be defined later)
- Acceptance method: Supplier demonstration of compliance against specification

### Design Changes (SOW-2 to SOW-4)
- Requirement for design modifications including:
  - UAV flight path changes
  - Operation without GPS/rebro capability
- Integration support (radios)
- Design and supply of data pack per SDRL-E007

### Bill of Materials (SOW-5)
- Supply complete BOM for UAS and all items with supplier-defined part numbers
- Acceptance via buyer inspection

## Configuration Management Requirements

**Standard Applied:** DEF STAN 05-057 Issue 8 or equivalent

**Key Requirements:**
- SOW-6: Implement CM programme per defense standard; demonstrated via routine surveillance audits
- SOW-7: Prepare CI (Configured Items) documentation establishing Functional, Design (Allocated), and Product baselines
- SOW-8: Define Configuration Items and baselines within SDRL-CM004

## Quality Assurance Requirements

### Accreditation (SOW-9 to SOW-12)
- Maintain **ISO 9001:2015** third-party accreditation (or equivalent) throughout contract lifecycle with scope appropriate to contract
- Advise buyer of any changes to registration status or scope
- Establish internal audit process to assure compliance
- Prevent counterfeit parts per DEF STAN 05-135
- **Note:** Call required between LM UK QA and BST to establish how intent is met with BST's current QA processes

### First Article Inspection (SOW-13 to SOW-16)
- Designate POC responsible for quality to manage FAI activity
- Notify buyer 10 working days in advance of FAI readiness
- Provide FAI report (SDRL-Q004) in advance of product acceptance
- Retain FAI results throughout contract lifecycle
- **FAI Content Requirements:**
  - Technical examination verifying as-built conforms to technical documentation
  - Completed checklists with objective evidence for each end item part number (LRU)
  - Actual measurement data for interface dimensions
  - Configuration identifiers (part/serial numbers, revision levels)
  - Discrepancy/deficiency/defect data and corrective actions

### Certificate of Conformity (SOW-17)
- Provide per SDRL-Q003 for each product delivered
- Must reference DEFCON 627 Issue 04-24
- Minimum content required by specification includes contractor details, CofC reference number, PO number, approved concessions, acquirer details, item description with part number and specification, serial numbers, quantities, signed attestation of compliance

### End Item Data Package (SOW-18)
- Supply per SDRL-Q008 concurrent with hardware shipment
- Shall include:
  - Reference to As-Built List (SDRL-CM005)
  - Reference to FAI report (SDRL-Q004)
  - Certificate of Conformance (SDRL-Q003)
- Alternative: C of C can fulfill EIDP requirements if subcontractor tailors appropriately

### As-Built List (SOW-19 to SOW-20)
- Create detailed "as-built" configuration listing per SDRL-CM005
- Separate ABL required for each discrete equipment delivery with all embodied CIs listed
- Reference: DEF STAN 05-057 Issue 8
- Content must include: part numbers, serial numbers, non-conformances, drawing/specification/issue numbers, embodiment data, nomenclature, next higher assembly references, quantities per system
- Can be delivered with Certificate of Conformity or as part of EIDP

## Test Process

### Factory Acceptance Test (SOW-21 to SOW-22)
- FAT conducted by supplier at supplier's premises
- Results documented per SDRL-T012
- Upon FAT completion, package and deliver equipment to:
  - **LMUK, Langstone Technology Park, HAVANT, Portsmouth, PO9 1SW**
  - *Note: Address confirmation required for "Unit 1"*

### Site Acceptance Test (SOW-24 to SOW-25)
- Demonstrate system operates correctly post-shipping and assembly
- Supplier provides SAT support and corrects any discrepancies discovered
- Acceptance of SAT reports (SDRL-T012) required
- *Note: SAT necessity flagged as TBC in draft*

**SDRL-T012 Test Report Content:**
- Test Brief for Acceptance Test (Entry/Exit criteria approval sheet)
- Test Debrief for Acceptance (completed exit approval sheet)
- 'As Run' Test Procedures/Schedules with test results
- Configuration Management of test facilities used
- Requirements Summary (Pass/Fail/Blocked outcomes)

## Design Drawing and Data Set (SOW-4, SDRL-E007)

**Purpose:** Contain all design data defining and describing final system design

**Reference:** DEF STAN 05-010 Part 2 Issue 8

**Minimum Content Required:**
1. Product Data Sheets
2. Product User Manuals
3. Connection schemes, ICDs, or drawings for Equipment Rack including:
   - All electrical connections between rack components
   - Electrical safety earths
   - External power supply connection points
   - External data connection points
4. Equipment installation details
5. Master Record Index/As-Built List

*Note: BST to advise what of this SDRL is currently available*

## Training & Support Requirements

### Training Delivery (SOW-26)
- Provide buyer with training and training materials for operation and maintenance of UAS
- Format per SDRL-TBC
- Training conducted at supplier site
- *Specific SDRL reference pending*

### Trials Support
- Provide in-country support to customer trials
- *Duration and quantity TBC*

### Technical Publications
- Provide technical documentation for operation and maintenance of each UAS variant
- Structured format per SDRL-L040
- *Alternative noted: could be fulfilled via access to online manuals/content*

### Sustainment Support
- Potential requirement for spares and repairs pack in-country
- Provide remote technical support during UAS trials

## Configuration Items List (SDRL-CM004)

**Purpose:** List all Configured Items with structure and characteristics; designate configuration levels and support baseline identification

**Reference:** DEF STAN 05-057 Issue 8

**Content for Development Items:**
- CI reference
- Manufacturer name and part number
- Manufacturer nomenclature
- Development/Non-Development item designation
- Next higher CI reference
- Logistic Control Number (LCN)
- Next higher assembly reference
- Quantity within next higher assembly
- Subcontractor/vendor name, part number, nomenclature
- NATO stock number (if codified)

## Key Open Items (Marked "TBC" - To Be Confirmed)

1. **System Specification Section (Section 4):** Entire system specification section incomplete; depends on Customer RFP
2. **UAS Variants:** Specific configurations and quantities to be defined at later stage
3. **Design Changes Detail:** GPS/rebro operation requirements not yet detailed
4. **GCS/Hand Controllers:** Question whether separate quantities need definition
5. **FAT/SAT Product Acceptance:** Exact acceptance criteria for SAT; whether SAT is needed at all
6. **Trials Support Duration & Quantity:** Scope of in-country support pending
7. **Training SDRL:** Specific SDRL number not yet assigned
8. **Technical Publications:** Format TBC; alternative online access being considered
9. **Delivery Address:** Unit 1 address confirmation required
10. **SDRL-E007 Availability:** What design data is currently available from BST
11. **ISO 9001:2015 QA Alignment:** Call required to align BST's current QA processes with intent

## Notable Details

- **Defence Standards Compliance:** Document emphasizes UK Defence Standards (DEF STAN 05-057, DEF STAN 05-010, DEF STAN 05-135, DEFCON 627)
- **Document Classification:** Marked as Lockheed Martin Proprietary Information with strict handling requirements
- **Subcontractor Relationship:** BST is operating as a subcontractor to LMUK; LM is prime contractor to Royal Navy
- **Flexible EIDP Approach:** Certificate of Conformity can substitute for End Item Data Package if properly tailored
- **Counterfeit Prevention:** Explicit requirement to prevent counterfeit parts per defense standard
- **Configuration Control:** Emphasis on FM, baselines, and configuration control throughout product lifecycle and field returns
- **Quality Audit Integration:** Routine surveillance audits anticipated with LM buyer
- **Concurrent Documentation:** EIDP to ship with hardware under separate cover via SDRL requirements
- **Serialization:** Serial number tracking and embodiment data required throughout system hierarchy

---

**Status:** This is Issue 0.1 Draft (dated 16 July 2026). Multiple sections pending finalization pending customer RFP details and BST capability confirmation calls.