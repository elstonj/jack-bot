# S2 UAS Launcher Usage Guide

## Document Metadata
- Type: Operating/maintenance manual
- Product: S2 UAS Launcher Assembly
- Date: Created/Modified 2019-01-17
- BST Products/Systems Referenced: S2 (Small Swift Two - UAS), Launcher system
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This is an operational manual for the S2 UAS pneumatic launcher system, providing step-by-step instructions for assembly, aircraft installation, charging/pressurization, firing, and troubleshooting. The launcher uses a compressed air/gas system with a main tank, hoses, and control pad to catapult-launch the S2 aircraft.

## Technical Approach
The launcher operates via:
- Pneumatic pressure system with main tank requiring 4/5+ battery charge to operate
- Two hoses (black and red) connecting case to main tank with different installation methods
- Power connector with twist-locking mechanism
- Wireless launch control pad with fire buttons (requires 3-4 second press-and-hold)
- Integrated pump system that shuts off automatically when tank reaches proper pressure (indicated by strobe light)
- Manual relief valve and vent button for system depressurization
- Rails with folding legs for stability; aircraft mounted via fuselage-side holes

## Products & Capabilities Described

### S2 UAS Launcher
- **What it is:** Pneumatic catapult launcher system for the S2 small unmanned aircraft system
- **Key components:** 
  - Launcher rail cart with folding legs (front and back)
  - Main pressurized tank
  - Pump system with integrated pressure monitoring (LED strobe indicator)
  - Launch control pad with wireless/corded operation
  - Manual vent and relief valve systems
- **Operation mode:** Aircraft must be in autonomous mode with preflight validation completed before charging
- **Fire mechanism:** Dual fire buttons requiring simultaneous 3-4 second press-and-hold

## Use Cases & Applications
- Field deployment of S2 aircraft in autonomous missions
- Rapid launch capability for time-sensitive operations
- Environments where conventional runway/hand launch is impractical

## Notable Details

**Safety-Critical Features:**
- Multiple warnings about staying clear of launcher/aircraft line-of-fire while system is pressurized
- Mandatory venting procedure if launch is aborted
- Requirement to approach system from sides only, never in front
- Propeller orientation requirement (vertical) to prevent damage during arm folding

**Power Management:**
- Battery-dependent pump operation (primary 12V system)
- Secondary power option via jumper cables to external 12V lead-acid battery
- Low battery fallback: cannot pressurize tank if primary battery insufficient

**Troubleshooting Indicators:**
- LED illumination = proper tank pressurization
- Pump shutdown + LED on = ready to fire
- Pump shutdown but no LED = battery failure (requires venting and recharge)
- System design includes manual relief valve backup if electronic vent button fails

**Integration with S2 Aircraft:**
- Aircraft mounting via holes in fuselage sides onto launcher rails
- Requires aircraft to be in autonomous mode before launch sequence
- Preflight validation mandatory via S2 control system before pressurization begins