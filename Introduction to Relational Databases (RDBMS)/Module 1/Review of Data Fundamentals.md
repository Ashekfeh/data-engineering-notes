# Data Structures
---
We can categorize data into three main types: __Structured, Unstructured and semi-structured__.

## Structured Data
---
Structured data refers to data that is highly organized and follows a predefined format. It is typically arranged in tables with rows and columns, similar to a spreadsheet. Structured data adheres to a strict schema and has a rigid structure, ensuring consistency and easy retrieval.

Examples of structured data include:
- Excel Spreadsheets
- SQL Databases
- Online forms

## Unstructured Data
---
Unstructured data refers to data that lacks a specific format or organization. It does not conform to any predefined rules or sequences, making it challenging to process and analyze using traditional methods.

Unstructured data can include:
- Text files
- Media Files
- Web pages
- Social media content (i.e. Posts, tweets, etc.)

## Semi-structured Data
---
Semi-structured data refers to data that possesses some organizational properties but does not adhere to a strict tabular structure like structured data. It often employs a hierarchical structure or tags to organize information, providing a balance between flexibility and structure.

Examples of Semi-structured data:
- JSON files
- XML documents
- Emails

# Data Sources
---
Data sources refer to the various places or origins from which data is collected or obtained. In the context of data analysis and management, data sources can include:
1. Traditional Databases: These include structured databases like SQL databases, where dat ais stored in predefined tables and columns
2. Flat files: These are simple text files that contain data in a plain, unstructured format (i.e. CSV files or TSV files)
3. XML datatsets: __Extensible Markup Language__ files define data structure using tags, attributes, and schema.
4. Web scraping: Data can be collected from websites by extracting information from HTML pages or using web scraping tools.
5. Data streams and feeds: Real-time data can be obtained from sources like IoT devices with sensors, social media platforms, or other streaming data sources. 
6. Social media platforms: Data can be collected from social media platforms such as Facebook, Twitter, or Instagram, including posts, tweets, and other updates.
7. Data warehouses: These are centralized repositories that store large amounts of structured and historical data from various sources.
8. Data lakes: Data lakes are storage repositories that store large volumes of raw and unprocessed data in its native format.
9. APIs (Application Programming Interfaces): APIs allow access to data from external systems or services, enabling data retrieval and integration.
10. External data providers: Organizations can obtain data from external sources such as market research firms, government databases, or public datasets.

# Data Repositories
---
__Data repositories__ are centralized storage systems that actively store, manage, and organize data in a structured manner. They provide a framework for efficient data retrieval, administration, and analysis. There are two major categories of data repositories:
1. **[[RDBMS|Relation Databases]]**: Relational databases consist of structured data stored in related tables. The links between the tables minimize data duplication while preserving intricate relationships.
2.  __Non-Relational databases__: Non-relational databases, also known as NoSQL databases, offer flexibility in handling diverse and unstructured data. They are suitable for scenarios where data structures may vary or evolve over time. Non-relational databases can handle semi-structured and unstructured data more effectively than relational databases. Examples of non-relational databases include MongoDB, Cassandra, and Redis

> [!note] #NOTE: Relational databases are commonly used for Online Transaction Processing (OLTP) systems, which support day-to-day business activities such as customer transactions, human resource activities, and workflows.

# Scope of Relational Database
---
__OLAP__[^1] Systems include various storage solutions, like relational and non-relational databases, [[Data Warehouses, Data Marts & Data Lakes#Data Warehouse|Data Warehouses]], [[Data Warehouses, Data Marts & Data Lakes#Data Lakes|Data lakes]] and big data stores. it focuses on querying and analyzing large data sets to extract meaningful insights.

# Non-Relational Databases
---
NoSQL or Non-Relational Databases offer flexibility in handling diverse and unstructured data

---
[^1]: Online Analytical Processing
