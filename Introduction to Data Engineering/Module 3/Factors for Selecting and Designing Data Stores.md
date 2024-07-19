# Primary Considerations for designing a Data Store
---
## Type of Data
---
**RDBMS** is best used for structured data, which has a well-defined schema and can be organized into a tabular format

**NoSQL** is best used for semi-structured and unstructured data, data that is <ins>schema-less</ins> and <ins>free-form</ins>

**Four types of NoSQL Databases:**
- Key-value
- **Document-based**: <ins>NOT the best option</ins> for complex search queries and multi-operation transactions
- Column-Based
- Graph-Based
## Volume of data
---
Volume/Scale of data:
- **Data Lake**: Store large volumes of raw data in its native format, straight from its source. It stores both relational and non-relational data at scale without defining the data's structure and schema.
- **Big Data Store**: Store data that is high-volume, high-velocity, of diverse types, needs distributed processing for fast analytics.

## Intended use of data
---
How you intend to use the data you are collecting:
- Number of Transactions
- Frequency of Updates
- Type of Operations
- Response Time
- Backup & Recovery

**Transactional Systems**: used for capturing high-volume transactions, need to be designed for high-speed read, write, and update operations.

**Analytical Systems**: need complex queries to be applied to large amounts of historical data aggregated from transactional systems. They need faster response times to complex queries.

**Schema design, indexing, and partitioning**: strategies have abig role to play in performance of systems based on how data is getting used.

#NOTE: The intended use of data also derives **scalability** as a design consideration.

#NOTE: **Normalization** is another important consideration at the design stage.
		it allows:
		- Optimal use of storage space.
		- Makes database maintenance easier.
		- Provides faster access to data.
#NOTE: <span style="color:red"> IMPORTANT </span> Normalization is important for systems that handle ==Transactional Data==. But for systems designed for handling ==analytical queries==, normalization can lead to <ins>performance issues.</ins>
## Storage considerations
---
Design considerations from the perspective of storage:
- **Performance** - Throughput[^1] and Latency[^2]
- **Availability** - Storage solution must enable you to access your data when you need it, without exception. <ins>There should be no <i>downtime</i></ins>.
- **Integrity** - Data MUST be save from corruption, loss and outside attacks.
- **Recoverability of Data** - Storage solution should ensure you can recover your data in the event of failures and natural disasters.
## Privacy, Security and Governance needs
---
#NOTE: A secure data strategy is a <ins>layered approached</ins>, it includes:
		- Access Control
		- Multizone encryption
		- Data management
		- Monitoring Systems
	
#NOTE: Regulations such as [GDPR](https://gdpr-info.eu/), [CCPA](https://oag.ca.gov/privacy/ccpa), and [HIPAA](https://www.hhs.gov/hipaa/index.html) restrict the ownership, use, and management of personal and sensitive data.

#NOTE: Dat needs to be made available through controlled data flow and data management by using multiple data protection techniques.

---
[^1]: Rate at which information can be read from and written to the storage.
[^2]: Time it takes to access a specific location in storage.