# Introduction
---
Enterprise-level data platforms and data repositories need to tackle security at multiple levels:
- Physical Infrastructure Security
- Network Security
- Application Security
- Data Security
# The CIA Triad
---
Key component to creating an effective strategy for information security include:
- **Confidentiality** through controlling unauthorized access
- **Integrity** through validating that your resources are trustworthy and have not been tampered with.
- **Availability** by ensuring authorized users have access to resources when they need it.

# Physical Layer Infrastructure
---
A key component of IT security.

Measures to insure physical structure security:
- access to the perimeter of the facility based on authentication and round-the-clock surveillance for entry and exit points of the facility.
- multiple power feeds from independent utility providers with dedicated generators and UPS battery backup 
- heating and cooling mechanisms for managing the temperature and humidity levels in the facility.
- by factoring in environmental threats before considering the location of the facility (for example: infrastructure facilities are never housed in flood plains, in areas prone to earthquakes, the infrastructure is housed in an earthquake-resistant structure, multi-level lightning protection and earthing systems are also installed in such facilities)

# Network Security:
---
Network security is <ins>vital</ins> to keep interconnected systems and data safe:
- **Firewalls** to prevent unauthorized access to private networks
- **Network Access Control** to ensure endpoint security by allowing only authorized devices to connect to network.
- **Network Segmentation** to create silos[^1], or virtual local area networks within a network.
- **Security Protocols** to ensure attackers cannot tap into data while it is in transit.
- **Intrusion Detection** and **Intrusion Prevention** systems to inspect incoming traffic for intrusion attempts and vulnerabilities.

# Application Security
---
Application Security is critical for keeping customer data private and ensuring applications are fast and responsive.

> [!note] #NOTE: security needs to be built into the foundation of an application in order to prevent other applications and services from introducing vulnerabilities

you can make your application safe by following security engineering practices such as:
- **Threat Modeling** to identify relative weaknesses and attack patterns relate to the application
- **Secure Design** that mitigates risks
- **Secure Coding guides and practices** that prevent vulnerabilities
- **Security Testing** to fix problems before the application is deployed and to validate that it is free of known issues.
# Data Security
---
Data is either at rest in storage, or in transit, between systems, applications, services and workloads

**Authentication Systems** verify you are who you say you are, it is accomplished by <ins>Password, Tokens, Biometrics</ins> or a combination of these.

**Authorization** ensures users access information based on their roles and privileges' assigned to their roles.

## Data at rest:
-  Includes files, object and storage.
- Stored physically in a database, data warehouse, tapes, offsite backups, and mobile devices.
- Can be protected by encryption.

## Data in transit:
- Moving from one location to another over the internet.
- Can be protected using encryption methods such as HTTPS, SSL, and TLS.

# Monitoring and Intelligence
---
Security Monitoring and Intelligence Systems:
- Create and audit of history for triage compliance purpose.
- Provides reports and alerts that help enterprises react to security violations in time.

---
[^1]: #TODO Lookup a definition or a source about it