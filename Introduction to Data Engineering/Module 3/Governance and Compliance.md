#  Introduction
---
Data Governance is a collection of principles, practices, and processes to maintain the **Security, Privacy and Integrity**.

# Data that needs Governance
---
**Personal**: Personal Information (PI) and Sensitive Personal Information (SPI)
- Can be traced back to an individual
- Can be used to identify an individual
- Can be used to cause harm to the individual

> [!note] #NOTE: The **General Data Protection Regulation (GDPR)** is a regulation that was implemented by the European Union (EU) in 2018 to protect the personal data and privacy of EU citizens. for transactions that occur in EU states

> [!note] #NOTE: In the united states, different states has made their own regualtions.

**Industry-specific regulations**:
- Health Insurance Portability and Accountability Act (HIPAA) for Healthcare.
- Payment Card Industry Data Security Standard (PCI DSS) for Retail.
- Sarbanes Oxley (SOX) for Finance.

# Compliance
---
Compliance covers the process and procedure through which an organization adheres to regulations and conducts its operations in a **legal and ethical manners**.

Organizations need to:
- Establish controls and checks in order to comply with regulations.
- Maintain a verifiable audit trail to establish adherence to regulations.

# Data Lifecycle
---
Governance regulations require enterprises to **know their purpose** and **be clear and transparent in their actions** at every step of the data lifecycle.

- In the **Data Acquisition Stage**, you need to:
	- Identify data that needs to be collected and the legal basis for procuring the data.
	- Establish the intended use of data, published as a privacy policy.
	- Identify the amount of data you need to meet your defined purposes.
- In the **Data Processing Stage**, you need to:
	- Flesh out details of how exactly you are going to process personal data.
	- Establish your legal basis for the processing of personal data.
- In the **Data Storage Stage**, you need to:
	- Define where you will store the data.
	- Establish specific measures you will take to prevent internal and external security breaches.
- In the **Data Sharing Stage**, you need to:
	- Identify third-party vendors in your supply chain that will have access to the collected data.
	- Establish how you will hold third-party vendors contractually accountable to regulations.
- In the **Data Retention and Disposal Stages**, you need to:
	- Define policies and processes you will follow for the retention and deletion of personal data after a designated time.
	- Define how you will ensure deleted data is removed from all locations, including third-party systems.

> [!note] #NOTE:In the data lifecycle, it is important to <ins>maintain an auditable personal data trail at each stage</ins>.
# Technology as an Enabler
---
Today's tools and technologies provide several controls for ensuring organizations comply to governance regulations.

**Authentication and Access Control**:
- Layered authentication processes
- Combination of passwords, tokens, biometrics to prevent unauthorized access.
- Authentication systems verify that you are who you are
- Access Control systems ensure only authorized users have access to resources, both systems and data, based on their user group and role.

**Encryption and Data Masking**:
- Encryption converts to an encoded format that can only be legible once it is decrypted via a secure key.
- Encryption of data is available for:
	- Data at rest.
	- Data in transit.
- Data Masking provides anonymization of data for downstream processing and pseudonymization of data.
- Anonymization abstracts the presentation layer without changing the data in the database itself.
- Pseudonymization of data replaces personally identifiable so that it cannot be traced back to an individual's identity.

**Hosting**
On-premise and cloud-based systems provide hosting options that comply with the requirements and restrictions for international data transfers.

**Monitoring and Alerting**
- Security monitoring proactively monitors, tracks and reacts to security violations across infrastructure, applications and platforms.
- Monitoring systems provide detailed audit reports that track access and other operations on the data.
- Alerting functionalities flag security breaches so immediate remedial actions can be triggered.
- Alerts are based on the severity and urgency level of a breach.

**Data Erasure**:
A software-based method for permanently clearing data from a system by overwriting. Data erasure prevents deleted data from being retrieved.