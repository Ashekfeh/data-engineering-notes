# Gathering Data
## Using Queries to Extract Data from SQL Databases
---
[[Languages for Data Engineering#SQL <span style="color lightgreen">(Most Popular) </span>|SQL]] is a querying language used for extracting information from relational databases.
It offers simple commands to specify:
- What is to be retrieved from the database.
- Table from which it need to be extracted.
- Grouping records with matching values.
- Dictating the sequence in which the query results are displayed.
- Limiting the number of results that can be returned by the query.

> [!note] #NOTE: Non-relational databases can be queried using **SQL** or **SQL-like** query tools. Some non-relational databases come with their own querying tools such as **CQL** for **Cassandra** and **GraphQL** for **Neo4J**.

## Application Programming Interfaces (APIs)
---
Popularly used for extracting data from a variety of data sources.
- APIs are invoked from applications that require the data and access an endpoint containing the data. Endpoints can include databases, web services and data marketplaces.
- APIs are also used for validation.

## Extracting Data from The Web (Web Scraping)
---
**Web Scraping/ Screen Scraping/ Web Harvesting** is used for downloading specific data from web pages based on defined parameters. It is Used for extracting data such as text, contact information, images, videos, podcasts & product items from a web property.

> [!note] #NOTE: **RSS feeds** are used for capturing updated data from online forums and news sites where data is refreshed on an ongoing basis.

## Sensor Data
---
**Data Streams** are a popular source of aggregating constant streams of data flowing from sources such as *Instruments, IoT devices, Applications & GPS data from cars*.

> [!note] #NOTE: Data streams and feed are also used for extracting data from social media sites and interactive platforms.

## Data Exchanges
---
**Data Exchange** allow the exchange of data between data providers and data consumers. They have a set of a well-defined exchange standards, protocols, and formats relevant for exchanging data.

These platforms:
- Facilitate the exchange of data
- Ensure that security and governance are maintained
- Provide data licensing workflows, de-identification and protection of personal information, legal frameworks and quarantined analytics environment.

Examples of popular data exchange platforms include: AWS DataExchange, Crunchbase, lotame & Snowflake.

## Other Sources
---
Numerous other data sources can be tapped into for specific needs.
For example:
- **Forrester** and **Business Insider** for <ins>marketing trends & spending</ins>
- Research and advisory firms such as **Gartner** and **Forrester** for <ins>strategic and operational guidance</ins>.
- Agencies for user behavior data, mobile and web usage, market surveys and demographic studies.

# Importing Data
---
Data that has been identified and gathered from the various data sources now needs to be loaded or imported into a data repository before it can be wrangled, mined, and analyzed. The importing process involves combining data from different sources to provide a combined view and a single interface using which you can query and manipulate the data.

## Data Types and Destination Repositories
---
### Structured Data
- **Relational Databases** store structure data schema.
- Sources include data from OLTP systems[^1], online forms, sensors, network and weblongs 
- Can also be stored in NoSQL databases.

### Semi-structured Data[^2]
- Can be stored in NoSQL clusters.
- XML and JSON are commonly used for storing and exchanging semi-structured data.

> [!note] #NOTE:JSON is the preferred data type for web services

### Unstructured Data[^3]
- Can be stored in NoSQL databases and [[Data Warehouses, Data Marts & Data Lakes#Data Lakes|data lakes]]
> [!note] #NOTE: [[ETL, ELT & Data Pipelines#Extract, Transform & Load Process (ETL)|ETL]] tools and [[ETL, ELT & Data Pipelines#Data Pipelines|pipelines]] provide automated functions that <ins>facilitate the process of importing data</ins>.

---
[^1]: OLTP stands for Online Transaction Processing. It is a type of database system that is designed to support transaction-oriented applications.

[^2]: Semi-structured data refers to data that does not have a rigid, predefined structure like traditional structured data, but still has some organizational properties. (i.e. emails, XML, zipped files, binary executables and TCP/IP protcols)

[^3]: Sources include web pages, social media feeds, images, videos, documents, media logs, and surveys.