# NIST SP 800-171 DoD Assessment Methodology, Version 1.2.1

## Document Metadata
- Type: Compliance guidance / assessment methodology document
- Client/Agency: U.S. Department of Defense (DoD)
- Program/Solicitation: DFARS clause 252.204-7012 (Safeguarding Covered Defense Information and Cyber Incident Reporting)
- Date: June 24, 2020 (Version 1.2.1; updates to Version 1.1 shown in blue)
- BST Products/Systems Referenced: None
- Key Personnel: Not applicable (this is a DoD guidance document, not a BST proposal/report)

## Executive Summary
This is a DoD assessment methodology document establishing a standardized approach for evaluating contractor implementation of NIST SP 800-171 security requirements. It defines three levels of assessment (Basic/self-assessment, Medium, and High), provides a weighted scoring system with a baseline of 110 points, and describes how assessment results will be documented and posted to the Supplier Performance Risk System (SPRS) to provide DoD visibility and reduce contract-by-contract compliance verification.

## Document Classification
**NOTE:** This document is not a Black Swift Technologies proposal, report, or capability document. It is a DoD compliance guidance document (NIST SP 800-171 DoD Assessment Methodology, Version 1.2.1) that was stored in BST's project files, likely because BST is subject to these DFARS cybersecurity requirements as a DoD contractor.

## Regulatory Background
- **DFARS Clause 252.204-7012** requires DoD contractors and subcontractors to provide adequate security for Defense Controlled Unclassified Information (CUI) and implement minimum security requirements from NIST SP 800-171
- **DFARS Provision 252.204-7008** requires offerors to represent they will implement NIST SP 800-171 security requirements
- **USD(A&S) Memorandum (February 5, 2019)** directed DCMA to apply a standard, strategic (corporate-wide) assessment methodology as an alternative to contract-by-contract compliance documentation

## Assessment Levels

### Basic (Contractor Self-Assessment)
- Contractor self-scores based on review of system security plan(s)
- Confidence level: **Low**
- Results posted to SPRS by contractor via PIEE

### Medium Assessment
- Conducted by trained DoD personnel
- Review of system security plan descriptions to identify inadequate coverage of requirements
- Typically conducted during scheduled visits (e.g., Critical Design Review)
- Confidence level: **Medium**

### High Assessment (On-Site or Virtual)
- Conducted by trained DoD personnel
- Thorough verification/examination/demonstration of system security plan and implementation
- Uses NIST SP 800-171A methodology
- Reviews evidence (scanning results, system inventories, configuration baselines, MFA demonstrations)
- **On-site** High Assessments preferred for full risk evaluation; **virtual** assessments permitted with data protection measures (DoD SAFE transmission, local-only review, NSA-guided data destruction)
- Confidence level: **High**
- Contractors have 14 business days post-assessment to provide additional information or rebut findings

## Scoring Methodology

### Baseline Score
- Maximum score: **110 points** (equals total number of NIST SP 800-171 security requirements)
- Points subtracted for each requirement not implemented
- Negative scores are possible

### Weighting System
Requirements are weighted based on impact to information system security and DoD CUI when not implemented:

**5-point requirements (23 basic + 19 derived):** Fundamental requirements or those allowing significant exploitation/exfiltration
- Examples: 3.1.1 (limit system access), 3.8.7 (control removable media use), 3.13.11 (FIPS-validated cryptography), 3.14.2 (malicious code protection)

**3-point requirements (7 basic + 7 derived):** Specific/confined effect on network/data security
- Examples: 3.8.2 (limit CUI access on media), 3.1.19 (encrypt CUI on mobile devices)

**1-point requirements:** Limited or indirect effect on security
- Examples: 3.5.5 (prevent identifier reuse), 3.14.7 (identify unauthorized system use)

### Special Scoring Cases

**Multi-Factor Authentication (3.5.3):**
- 5 points subtracted if not implemented for any users
- 3 points subtracted if implemented only for remote and privileged users (not general users)

**FIPS-Validated Encryption (3.13.11):**
- 5 points subtracted if no encryption employed
- 3 points subtracted if encryption employed but not FIPS-validated

**Remote/Wireless/Mobile Access (3.1.12, 3.1.16, 3.1.18):**
- No points deducted if company disallows these capabilities (with policy/procedures to prevent inadvertent enablement)

### Partial Implementation & Plans of Action

**Temporary Deficiencies:**
- Remediation feasible; fix in process; requires plan of action
- Should be scored as "implemented" if appropriately addressed in plan of action with deficiency reviews, milestones, and progress toward correction
- No standard duration; must be reasonable given solution availability, cost, time to implement, risk, and interim mitigations
- Applies to initial rollout issues (e.g., specific equipment compatibility) and post-implementation issues (e.g., patch invalidating FIPS validation)

**Isolated Enduring Exceptions:**
- Remediation not feasible (e.g., unique equipment, specialized lab environments)
- Documented in system security plan with mitigations
- Should be scored as "implemented"
- Not suitable for plans of action

**Plans of Action Are Not Substitutes:**
- Unimplemented requirements scored as "not implemented" even with plan of action
- Example: 75% rollout of MFA with active plan of action = requirement scored as "not implemented"
- Lack of plan of action for unimplemented requirement results in 3.12.2 assessment as "not implemented"

### DoD CIO Adjudications
- If contractor received favorable DoD CIO adjudication that requirement is not applicable or alternative security measure equally effective, include in system security plan
- Such measures assessed as "implemented"
- Documentation need not be resubmitted for each contract (unless requested by contracting officer)

## System Security Plan Requirements

**Mandatory for Assessment:**
- System security plan (3.12.4) describing each covered contractor information system
- Plan of action (3.12.2) for each unimplemented security requirement describing how and when it will be met
- Absence of system security plan results in finding: "assessment could not be completed due to incomplete information and noncompliance with DFARS clause 252.204-7012"

## Assessment Frequency
- Anticipated once every three years
- May be more frequent based on program criticality/risk or security-relevant changes

## Documentation & SPRS Posting

### Information Posted to SPRS
- Standard assessed (e.g., NIST SP 800-171 Rev 1)
- Organization conducting assessment (DCMA or other, identified by DoDAAC or CAGE code)
- Each system security plan assessed, mapped to specific industry CAGE code(s)
- Date and level of assessment (basic, medium, or high)
- **Summary level score only** (e.g., 105 of 110), NOT individual requirement values
- Projected date for achieving score of 110 based on plans of action

### Access & Protection
- SPRS is authoritative source for contractor/supplier performance information
- Available to DoD personnel; contractors may view their own results via SPRS per Software User's Guide
- Detailed assessment documentation from High Assessments retained as **For Official Use Only (FOUO)** for internal DoD use
- Protected against unauthorized release under FOIA Exemption 4 (trade secrets, confidential commercial/financial information)

### Strategic Assessment Alternative
- Results posted in SPRS provide alternative to contract-by-contract assessment requirements
- DoD Components directed to rely on SPRS assessment results in lieu of including contract-level NIST SP 800-171 implementation assessment requirements

## Notable Compliance Details

**Scoring Template Note:** Assessment focuses on extent of implementation, not value judgment of specific approach. All solutions meeting requirements are acceptable.

**Cyber Incident Reporting:** DFARS 252.204-7012 also requires reporting of cyber incidents affecting contractor information systems/networks to DoD.

**Flow-Down to Subcontractors:** DFARS 252.204-7012 must be flowed down to all subcontracts for operationally critical support or where subcontract performance involves DoD CUI.

**Marking/Identification:** Contractors required to mark/identify DoD CUI per contract direction.

**Virtual Assessment Protocols (Added in Version 1.2.1 response to COVID-19):**
- Data transmitted via DoD Secure Access File Exchange (SAFE)
- Local review only on assessor computers
- Screen sharing via DoD-approved CUI collaboration mediums
- Contractor data destroyed per NSA guidance post-assessment
- Does not fully cover all NIST SP 800-171 requirements; may require follow-up on-site assessment

## Applicability to Black Swift Technologies
This document was likely retained by BST as a reference for its own DFARS compliance obligations as a DoD contractor. It establishes the framework under which BST's cybersecurity posture and NIST SP 800-171 implementation may be assessed.