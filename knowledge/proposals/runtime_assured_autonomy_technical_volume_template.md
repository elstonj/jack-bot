# Runtime Assured Autonomy Technical Volume Template

## Document Metadata
- Type: SBIR/STTR Phase I Technical Proposal Template
- Client/Agency: Department of Defense (DoD), Department of the Air Force (DAF)
- Program/Solicitation: Runtime Assured Autonomy (RTAA)
- Date: 2026-05-08 (document creation/modification date)
- BST Products/Systems Referenced: None (this is a template, not a completed proposal)
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This is a blank template document for Phase I SBIR/STTR technical proposals submitted to the Department of the Air Force for the Runtime Assured Autonomy (RTAA) program. The template provides structured guidance for small business contractors to propose feasibility studies on autonomous system monitoring and fault mitigation architectures.

## Technical Approach
The template guides proposers to address two main functional elements:

1. **RTAA Fault Determination Function**: Continuous monitoring of autonomous system performance through information acquisition (onboard sensors, fleet communications, tactical/strategic broadcasts), knowledge extraction (fusion and filtering), and fault determination logic. Focus on detecting autonomy failures in course-of-action (COA) generation and execution rather than platform safety alone. Use cases should span various fault types: autonomy design flaws, platform hardware failures, pop-up threats, mission changes, contingency misresponses. Detection strategies may employ fault isolation techniques, heuristics, or formal methods. Critical requirement: minimize false alarms that disable correctly-functioning autonomy handling off-nominal conditions.

2. **RTAA Mitigation Function**: Recovery procedures activated upon fault detection to restore safe operations. Options include simple reversionary functions, failsafe loiter points, or pre-defined sequential COAs. Phase I should assess recovery feasibility under various scenarios and determine conditions triggering mission abandonment versus continued execution.

## Products & Capabilities Described
No specific BST products are mentioned in this template. This is a proposal framework document, not a technical description of existing systems.

## Use Cases & Applications
Template guidance specifies mission scenarios for use case development:
- **Mission Types**: ISR (Intelligence, Surveillance, Reconnaissance), patrol, supply delivery, high-value escort, weapon engagement/deployment, enemy suppression
- **Operating Environments**: High-risk zones, no-fly zones, natural and urban terrain
- **Threat Scenarios**: Red team air and ground assets, contested areas of operation

## Phase I Deliverables & Expectations
- Initial architecture and functional design documentation
- Low-order design and analysis studies using desktop simulation environments
- Phase II technology development plan based on Phase I results
- Proposers may use their own models/simulation environments
- No government-furnished data required for Phase I
- Awardees should expect Air Force engagement during Phase II planning for platform/architecture/mission alignment

## Notable Details

**Compliance & IP Requirements:**
- Proposals may include restricted technical data requiring non-disclosure outside Government (requires specific marking and legends per DFARS 252.227-7018)
- Government retains royalty-free license for Government purposes for 20 years post-completion; unlimited rights thereafter
- Proposers must assert any restrictions on data/software use, release, or disclosure
- ITAR and Export Control restrictions apply; universities cannot publicly release Export Controlled information

**Proposal Structure Requirements:**
- Single column, single-spaced, 10-point minimum font
- Standard 8.5" x 11" paper with 1-inch margins
- Header with company name, topic number, DSIP proposal number on each page
- Specific page limits per Service/Component-specific instructions (not stated in template)
- No locked/encrypted files; no embedded active media (videos, animations)

**Mandatory Proposal Sections:**
1. Problem/opportunity identification and significance
2. Phase I technical objectives
3. Phase I Statement of Work (tasks, methods, schedule, deliverables, subcontractors)
4. Related work and state-of-the-art awareness
5. Relationship with future Phase II research
6. Commercialization strategy (~1 page with market need, size, quantitative results timeline)
7. Key personnel (PI and team qualifications, publications, patents, awards)
8. Foreign nationals disclosure (citizenship, visa status, involvement level)
9. Facilities and equipment justification
10. Subcontractors/consultants (minimum 2/3 work by SBC for SBIR; 40% SBC + 30% Research Institution for STTR)
11. Prior/current/pending similar funding disclosure
12. Data restrictions assertions with DFARS compliance

**SBIR vs. STTR Distinctions:**
- **SBIR**: Minimum 2/3 of research by small business firm (direct+indirect costs); university subcontracts allowed; Federal Lab/FFRDC participation without waiver
- **STTR**: Minimum 40% by small business firm + 30% by single Research Institution; FFRDCs allowed; Federal Laboratories permitted in remaining 30%

**Air Force Expectations:**
Significant Air Force interaction expected during Phase II planning for alignment with specific platforms, architectures, and missions of interest. Proposers should be prepared for government-directed scope refinement post-award.