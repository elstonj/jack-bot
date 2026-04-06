# HACKthePILOT - Track 1 Detailed Report

## Document Metadata
- **Type:** Competition Results Report / Bug Bounty Analysis
- **Client/Agency:** U.S. Navy (via HACKtheMACHINE-UNMANNED 2021 program)
- **Program/Solicitation:** HACKtheMACHINE-UNMANNED 2021, Track 1
- **Date:** December 14, 2021
- **BST Products/Systems Referenced:** 
  - Autopilot & Ground Control Software
  - SwiftCore UAV platform
  - gcsDaemon (Ground Control Station Daemon)
  - pro_core_swil_MULTIROTOR (drone control process)
  - SWIL (SWIFT Integrated Libraries/software)
- **Key Personnel:** 
  - Dr. Dave Burke (Fathom5 Chief Engineer)
  - Anthony Connor (Fathom5 Cybersecurity Engineer)
  - Jack Elston (BST CEO, referenced in OSINT findings)

## Executive Summary

HACKthePILOT was a bug bounty competition held November 16-18, 2021, where cybersecurity teams competed to identify vulnerabilities in Black Swift Technologies' Autopilot and Ground Control Station software. 98 vulnerability reports were submitted; 57 were validated and awarded points/bounties, representing 30 unique vulnerabilities (21 Critical, 16 High, 11 Medium, 12 Low). Total prize distribution was $30,000 across 40 individuals on 9 eligible teams. The competition revealed significant security gaps in authentication, encryption, input validation, and memory safety that could enable drone hijacking, crashes, surveillance, and denial of service attacks.

## Technical Approach

### Competition Structure
- **Duration:** 56 hours (2:00 PM EST Nov 16 – 11:59 PM EST Nov 18, 2021)
- **Format:** Team-based bug bounty with point scoring and monetary rewards
- **Prize Distribution:**
  - Top 3 teams: $15,000 split ($7,500 / $5,000 / $2,500)
  - Per-vulnerability bounties: $15,000 divided by severity (Critical/High/Medium/Low)
  - First-finder received full bounty; duplicate finders received ~10% of primary
- **Participants:** Teams of 3-10 members (solo participation allowed); 40 individuals across 9 eligible teams

### Gamification vs. Production Deployment
The competition exposed a critical issue: vulnerabilities valid in the game environment may not exist in production due to architectural modifications:

**Gamified Deployment (HACKthePILOT):**
- Ground Control Station containerized via Docker (exposed to participants)
- Autopilot code run on hardware abstraction layer instead of embedded device
- Direct simulation/autopilot connection bypassing standard network and RF security layers
- Internal sensor/controller interfaces exposed

**Production Deployment (Black Swift Technologies):**
- GCS runs on secured network appliance
- Autopilot on actual embedded devices
- Standard network and RF systems with additional security components
- Internal interfaces protected

**Impact:** Multiple reported vulnerabilities are not applicable to production systems, requiring BST assessment of actual criticality.

## Products & Capabilities Described

### Black Swift Technologies Systems

**Autopilot System**
- Core flight control software
- Vulnerable to remote command injection, buffer overflows, DoS attacks
- Lacks authentication mechanisms
- No state validation before executing commands
- Uses unencrypted telemetry broadcasts

**Ground Control Station (GCS) / gcsDaemon**
- Port 55555 service for drone command and control
- Critical vulnerabilities:
  - No authentication between clients and GCS
  - No authentication between GCS and drone
  - Buffer overflow vulnerabilities (strcpy, sprintf with no bounds checking)
  - Memory corruption in client socket handling
  - SIGPIPE exceptions on certain commands (mission plan delete)
  - Crashes on rapid connections or large packet fuzzing
  - Out-of-bounds array access in Socket::checkFD function

**SWIL (Swift Integrated Libraries) / pro_core_swil_MULTIROTOR**
- Drone-embedded control process
- Vulnerabilities:
  - CLI argument buffer overflows
  - Improper input handling for radio port numbers
  - Global memory overflow via HOME environment variable
  - Relative path execution (mkdir, rm commands)
  - No encryption on telemetry broadcasts
  - Unencrypted command traffic
  - Buffer overflows on connection handling
  - Can be crashed via altitude-triggered memory corruption
  - XBee/ZigBee mode with shared, unencrypted encryption keys (dev mode)

**Communications Protocol**
- PKT_ACTION_COMMAND and PKT_ACTION_ACK packet types
- Unencrypted telecommands and telemetry
- No source authentication for messages
- Acknowledgments broadcast to all clients (information leak)

### Use Cases & Applications

**Intended Deployment Context:** U.S. Navy drone swarm operations
- Safety-critical autonomous flight systems
- Multi-drone coordination
- Remote piloting via ground control stations
- Mission planning with waypoints
- Real-time telemetry and flight control

## Key Results / Validated Vulnerabilities

### Critical Severity Vulnerabilities (21 total)

**Authentication & Access Control (7 vulnerabilities)**
- **1402234:** Remote unauthenticated drone engine kill via GCS (mid-flight shutdown)
- **1402271:** Missing authentication on gcsDaemon port 55555 (arbitrary drone control via Python script)
- **1403287:** Remote unauthenticated flight control and crash (reconfigure to manual mode, send out-of-envelope commands, destroy via altitude loss)
- **1404410:** Lack of message source authentication (message capture and replay)
- **1404435:** Unauthenticated full joystick control (PoC draws square pattern demonstrating control)
- **1404651:** Hijack control via IP address spoofing (terminate legitimate controller, assume control)
- **1404791:** Lack of client-side authentication (man-in-the-middle potential)

**Denial of Service - Memory Corruption (6 vulnerabilities)**
- **1402283:** CLI argument buffer overflow in gcsDaemon launcher (-J joystick option)
- **1402289:** Rapid connections from same IP cause segmentation fault (Out-of-bounds read, Socket::checkFD, numClients unbounded increment)
- **1403145:** Large packet fuzzing causes segmentation fault (buffer overflow in GCS daemon, loss of C2)
- **1403175:** Remote checkFD memory corruption DoS (~21 simultaneous connections crash gcsDaemon via dereference of fds_bits[16] out of bounds)
- **1403649:** Remote buffer overflow in both drone and GCS (incorrect connection/data handling)
- **1404664:** Multiple connections to gcsDaemon cause segmentation fault

**Safety-of-Flight (3 vulnerabilities)**
- **1404787:** Remote altitude-triggered checkFD DoS in SWIL (drone crashes at ~1600m altitude when receiving repeated connections; FORTIFY_SOURCE causes process exit)
- **1404626:** Joystick input causes erratic flight and loss of control
- **1404838/1404841:** X/Y velocity underflow via crafted packets (in-flight parameter modification causing potential damage/destruction)

**Command Injection & Crash (5 vulnerabilities)**
- **1403619:** SIGPIPE error on GCS (attacker can terminate GCS, disconnect other users, intercept messages)
- **1403625:** Session disruption via drone control to GCS (freeze previous sessions without alerting user)
- **1403644:** Remote unauthenticated firmware update crash
- **1404594:** Denial of service via firmware update trigger (unauth user halts pro_core_swil_MULTIROTOR)
- **1404833:** GCS denial of service via mission plan delete command (SIGPIPE exception)

---

### High Severity Vulnerabilities (16 total)

**Information Disclosure (4 vulnerabilities)**
- **1404301:** Remote unauthenticated information leak via PKT_ACTION_ACK (GCS broadcasts ACKs to all clients, revealing operator commands, launch/land times, waypoints; actionable for physical operations)
- **1404629:** SWIL broadcasts unencrypted telemetry exposing position (attacker can intercept, reconstruct flight path)
- **1404663:** Telecommands from GCS to SWIL unencrypted (reveal flight plan and waypoints via sniffing)
- **1404858:** Unauthorized UAV telemetry reading (unprivileged network user can listen to drone telemetry: GPS position, system info, sensor data)

**Buffer Overflow & Code Execution (5 vulnerabilities)**
- **1404431:** Buffer overflow when connecting to host (IP spoofing enables remote code execution)
- **1404624:** Buffer overflow in gcsDaemon CLI parsing (strcpy on command line arguments, overwrites token and n_number secrets)
- **1404821:** Global memory overflow from HOME environment variable (sprintf into 32-byte buffer, allows DoS, parameter modification, potential RCE)
- **1404828:** Relative path for 'mkdir' command (privilege escalation/lateral movement potential)
- **1404830:** Relative path for 'rm' command (privilege escalation/lateral movement potential)

**Input Validation (3 vulnerabilities)**
- **1404576:** Lack of command line argument validation (atoi/atof without error checking, CWE-758)
- **1404771:** SWIL improper input handling for radio port number (non-numeric input, unsafe dereference, unpredictable behavior)
- **1404785:** Input validation missing in control system (no state checks before command execution; shutdown while airborne possible)

**Miscellaneous (4 vulnerabilities)**
- **1403644:** Remote unauthenticated firmware update crash
- **1404486:** File permission misconfiguration (unprivileged user can read /var/log/apt/ logs with sensitive info)
- **1404735:** 3-packet sequence causes GCS crash
- **1404857:** In dev mode, XBee/ZigBee protocol uses shared, unencrypted encryption key

---

### Medium Severity Vulnerabilities (11 total)
- **1404842:** Sensitive data exposure (hashes exposed to non-privileged users)
- **1404847:** Poor operational security (developer names in files, large OSINT haul from WordPress directory listing and Jack Elston's public GitHub; 1,177 content files scraped)
- **1404852:** Public posting of source code (172 files marked "BST Proprietary" on public repo)

### Low Severity Vulnerabilities (12 total)
- Various input handling and privilege escalation edge cases

## Notable Details

### Competition Execution Challenges
- **Slow start:** Initial submissions only in last hours of Day 1; participants unfamiliar with VM setup
- **Scope confusion:** Teams initially submitted Gazebo simulation vulnerabilities; had to redirect to autopilot/GCS focus
- **High submission volume:** Once scope clarified, Day 2 saw surge in submissions
- **Duplicate findings:** 16 of 57 validated vulnerabilities were duplicates (41 unique total)

### Vulnerability Distribution by Severity
- Critical: 21 (37%)
- High: 16 (28%)
- Medium: 11 (19%)
- Low: 12 (21%)

### Root Cause Analysis Themes
1. **No authentication:** Complete absence of client-GCS and GCS-drone authentication
2. **Memory safety:** Unsafe string functions (strcpy, sprintf), unbounded arrays, out-of-bounds access
3. **Input validation:** No bounds checking, missing error handling on type conversions
4. **Encryption:** Unencrypted telemetry and command traffic
5. **State management:** No command sequencing, missing state validation before execution
6. **Operational security:** Public source code, developer identifiable info, exposed OSINT vectors

### Impact on U.S. Navy Mission
- **Safety of flight:** Multiple ways to crash drones mid-mission
- **Loss of command and control:** DoS attacks disable GCS, preventing operator intervention
- **Drone hijacking:** Full remote control possible without authentication
- **Mission compromise:** Flight plans and telemetry exposed; operator actions monitored in real-time
- **Physical consequences:** Drones can be destroyed or used against intended targets

### OSINT Vulnerability (1404847)
The report documents significant intelligence gathering by competitors:
- WordPress upload directory listing enabled (scraped 1,177 files)
-