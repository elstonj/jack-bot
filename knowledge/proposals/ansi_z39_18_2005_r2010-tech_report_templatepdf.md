# ANSI/NISO Z39.18-2005 (R2010) - Scientific and Technical Reports

## Document Metadata
- **Type**: American National Standard (ANSI/NISO standard specification)
- **Standard Designation**: ANSI/NISO Z39.18-2005 (R2010)
- **Issued**: July 27, 2005; Reaffirmed May 13, 2010
- **ISSN**: 1041-5653
- **ISBN**: 978-1-937522-21-6
- **Subject**: Guidelines for preparation, presentation, and preservation of scientific and technical reports
- **Published by**: National Information Standards Organization (NISO), Baltimore, MD
- **Date Found in BST Records**: Created/Modified 2025-05-28
- **Last Editor**: Daniel Prendergast
- **BST Project Context**: Located in AFWERX SBIR Phase II - Soil Moisture Mapping project deliverables

## Executive Summary
This ANSI/NISO standard provides comprehensive guidelines for preparing, presenting, and preserving scientific and technical reports in both print and digital formats. The 2005 revision (reaffirmed 2010) modernizes the previous standard to address the shift from paper-only publications to digital and multimedia formats, emphasizing metadata management, digital preservation, and interoperability across multiple publication media.

## Purpose & Scope
The standard establishes uniform practices for:
- Creating reports with appropriate metadata capture
- Organizing report components (front matter, body, back matter)
- Presenting information in print and digital formats
- Discovering and accessing reports through effective metadata
- Preserving digital documents for long-term access
- Supporting multimedia and "born digital" report formats

The standard is intentionally flexible, accommodating diverse report purposes and presentation methods rather than prescribing a single format.

## Key Technical Concepts

### Digital Format Representation
The standard recommends structured approaches using:
- **Document Type Definition (DTD)**: Defines building blocks and rules for XML documents
- **XML (eXtensible Markup Language)**: Maintains report contents and structure
- **XSL (eXtensible Style Sheet)**: Provides presentation formatting and alternative display options

These components work together to enable automatic validation, flexibility of representation, and format migration.

### Metadata Framework
Three types of metadata required:

**Descriptive Metadata**
- Title, creator (author), keywords, subject references
- Enables discovery and resource identification
- Based on standards like Dublin Core or MARC 21

**Structural Metadata**
- Table of contents, list of figures/tables
- Explains relationships between multipart objects
- Enhances internal navigation

**Administrative Metadata**
- Software type/version, file formats, rights information
- Supports maintenance and long-term archiving
- Required for format migration and access control

## Report Components Framework

### Front Matter (Descriptive & Descriptive Metadata)
- **Cover** (optional)
- **Title Section** (required) - includes report number, title, authors, organizations
- **Notice Section** (conditional) - copyright, distribution restrictions
- **Format Information** (conditional) - for digital originals
- **Report Documentation Page** (conditional) - for federal agency reports; uses Standard Form (SF) 298
- **Abstract** (required)
- **Contents/Table of Contents** (required)
- **List of Figures and Tables** (conditional - when >5 items)
- **Foreword, Preface, Acknowledgments** (conditional)

### Body Matter (Content)
- **Summary** (required)
- **Introduction** (required)
- **Methods, Assumptions, and Procedures** (required)
- **Results and Discussion** (required)
- **Conclusions** (required)
- **Recommendations** (conditional - when report proposes action)
- **References** (required)

### Back Matter
- **Appendices** (optional)
- **Bibliography** (optional)
- **Symbols, Abbreviations, and Acronyms** (optional)
- **Glossary** (optional)
- **Index** (optional)
- **Distribution List** (optional)

## Presentation Guidelines

### Design Principles
- **Line Length**: Specified for readability
- **Font Choice**: Clarity and legibility standards
- **Print Specifications**: Margins, paper quality (acid-free recommended), ink durability
- **Digital Presentation**: Multiple rendering options via XSL for different display media

### Visual and Tabular Matter
- Figures and tables properly labeled and integrated
- Consistent nomenclature and formatting
- Print and non-print-specific guidelines provided
- Alternative representations for accessibility

### Numbers, Units, and Equations
- Standard SI units recommended (IEEE/ASTM SI-10-2002)
- Formulas and equations clearly presented with spacing
- Chemical and multi-line equations handled with specific formatting conventions

### Designation Elements
- Consistent hierarchical designation of sections
- Print-specific guidance for chapter/section numbering

## Key Concepts for Digital Documents

### Persistence
- Addresses limitation of URLs ("404" errors when resources move)
- Recommends persistent identifiers: Uniform Resource Names (URNs), Digital Object Identifiers (DOIs)
- Essential for long-term preservation and archiving

### Interoperability
Achievable at three levels:
- **Technical**: Consistent protocols and formats for message exchange
- **Content**: Data, metadata, and semantic agreements
- **Organizational**: Access rules, authentication, payment, collection management

### Discovery
- Reports must be discoverable by target audiences
- Metadata capture during production workflow is critical
- Use published controlled vocabularies, not ad hoc terminology
- Accessibility required for compliance with Section 508 (Rehabilitation Act)
- Avoid proprietary software not common to target audience

### Creation Phase Priorities
- Intellectual property rights review
- Security and classification assessment
- Structured coding for repurposing into multiple formats
- Copyright establishment and permissions
- Metadata capture: platform, OS, software version, file naming conventions
- Consistency standards for collaborative documents

### Maintenance and Preservation
- Choose time-tested publishing media (acid-free paper, polyester-based film for digital)
- Use XML DTD encoding for electronic reports
- Maintain internal and external links
- For multimedia reports: preserve both presentation media and content
- Enable migration across platforms, applications, and organizations
- Implement version control mechanisms

### Dissemination Strategy
- Plan distribution channels at project outset
- Utilize libraries, wholesalers, jobbers, online retailers
- Archive on web with unique identifiers via supporting agencies
- Support both print and digital publication paths

### Access and Distribution Control
- Classification/distribution information via electronic labeling or print
- Visible marking on cover/title page for print; opening screen for digital
- Example notations: "Approved for public release; distribution unlimited" or "Distribution authorized to DoD components only"
- Use metadata schema when physical marking impossible

## Standards Referenced

### American National Standards Referenced
- ANSI/NISO Z39.9-1992 (R2001) - International Standard Serial Numbering (ISSN)
- ANSI/NISO Z39.14-1997 (R2002) - Guidelines for Abstracts
- ANSI/NISO Z39.23-1997 (R2002) - Standard Technical Report Number (STRN) Format
- ANSI/NISO Z39.84-2000 - Syntax for Digital Object Identifier
- ANSI/NISO Z39.85-2001 - Dublin Core Metadata Element Set

### Other Standards
- IEEE/ASTM SI-10-2002 - International System of Units (SI)
- ISO 2108 - International Standard Book Numbering (ISBN)

### Regulatory Requirements
- Americans with Disabilities Act (ADA) of 1990
- Section 508 of Rehabilitation Act (1973) - Electronic information accessibility
- Privacy Act of 1974

## Standards Development Process
- Developed by NISO Committee AW with rigorous peer review
- Approved by American National Standards Institute (ANSI)
- Input from diverse voting members across libraries, publishers, government agencies, standards organizations
- Periodic review and reaffirmation process (most recent 2010)

## Notable Organizational Perspectives
Standard reflects practices from:
- Federal agencies (Defense Technical Information Center, National Archives)
- Academic institutions (Carnegie Mellon, Old Dominion University)
- Research organizations (RAND Corporation, National Agricultural Library)
- Library systems (Library of Congress, various specialized library associations)
- Publishing industry
- Information management professionals

## Flexibility & Best Practices Approach
- Standard explicitly allows multiple organizational patterns based on report purpose
- References Appendix D for model formats
- Advocates examining best practices within user's organization and discipline
- Emphasizes that no single format requirement applies universally
- Supports diversity in presentation while maintaining uniform metadata capture

## Digital/Multimedia Considerations
- Recognizes "born digital" reports with embedded links
- Accommodates multimedia presentations (video, audio without written accompaniment)
- PowerPoint and similar multimedia formats considered valid report formats
- Addresses versioning and integrity issues in digital environments
- Different design constraints for print vs. electronic documents noted
- Recommends production methods enabling conversion between media and formats

## Notable Document Governance
- NISO oversight by elected Board of Directors
- Represents organizations including OCLC, Library of Congress, major publishers, federal agencies
- Reaffirmed periodically to maintain relevance
- Open to suggestions for improvement

---

## Notes on BST Context
This document appears in BST's AFWERX SBIR Phase II project deliverables (Soil Moisture Mapping) as a **template or reference standard**, not as BST's own technical report. The document itself is a standards specification rather than a BST proposal, capability brief, or project report. It likely served as the formatting/organizational guide for BST's actual project deliverables or technical reports submitted under that SBIR contract.