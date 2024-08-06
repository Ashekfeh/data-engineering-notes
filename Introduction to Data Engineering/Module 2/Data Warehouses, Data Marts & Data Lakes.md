# Data Warehouse
---
Data warehouses are central repositories of data that are integrated from multiple sources. They serve as the single source of truth, storing current and historical data that has been cleansed, conformed, and categorized. They are designed to be <ins>analysis-ready</ins>

## Three-tier architecture
- Database Server
- an OLAP server for processing and analyzing information
- client front-end layer for querying reporting

# Data Marts
---
Data marts are sub-sections of data warehouses that are ==built specifically for a particular business function, purpose, or community of users.== They provide analytical capabilities for a restricted area of the data warehouse and <ins>offer isolated security and performance.</ins>

## Basic types of data marts
- Dependent data marts are a subset of an enterprise data warehouse and pull data from it
- Independent data marts are created from sources other than enterprise data warehouse such as internal operational system or external data.
- Hybrid data marts combine inputs from data warehouses, operational systems and external systems.

> [!note] #NOTE: The purpose of a data mart is t o provide users with relevant data when they need it, accelerate business processes, enable data-driven decision-making, improve end-user response time, and provide secure access and control.

## Data Lakes
---
Data lakes are data repositories that can store ==large amounts of structured, semi-structured, and unstructured data in their native format.== Unlike data warehouses, data lakes do <ins>not require predefined structures or schemas before loading the data.</ins> They serve as a repository of raw data, straight from the source, to be transformed based on the specific use case for analysis.


## DATA LAKEHOUSE
It combines the flexibility and cost of a data lake, and performance & structure governance of a data warehouse.
## Benefits of Data Lakes
1. the ability to store all types of data.
2. scalability based on storage capacity.
3. time-saving in defining structures and schemas, and the ability to repurpose data for various use cases.

# Factors to keep in mind when considering a data repository
---
- Type of data <span style="color:lightgreen"> (structured, semi-structured or unstructured) </span>
- Schema of the data
- performance requirements
- Whether you're working data at rest or streaming data (data in motion)
- Data encryption needs
- Volume of data and whether you need Big Data system
- Storage requirements
- Frequency of data access
	- Frequent updates
	- Keep in vault for a long time
- Standards set by your organization
- Purpose of data repository
	- transactional
	- Analytical
	- Archival
	- Data warehousing
- Compatibility of the data repository with the existing ecosystem of programming languages, tools and processes
- Security features
- Scalability
- ==Very few organizations use one data repository==
- Cost
- Hosting platform is an important consideration - AWS RDS, Amazon's Aurora, Google's relational offering
- How data needs to be stored?
- How data needs to be retrieved?
- Where the data should be stored?
- Structure of the data
- Nature of application
- Volume of data being ingested