# What is a Relational Database?
---
A relation  database is a collection of data organized into a table structure, where tables can be linked or related based on data common to each.

Relational databases use structured query language or SQL, for querying data.


# Critical Points about RDBMS
---
- Ideal for the optimized storage, retrieval and processing of data for large volumes of data.
- Each table has a unique set of rows and columns.
- Relationships can be defined between tables. ( Which can minimize redundancy ).
- Fields can be restricted to specific data types and values. ( Which minimizes irregularities and leads to greater consistency and data integrity)
- Can retrieve millions of record in seconds using SQL for querying data.
- Security architecture of relational databases provides greater access control and governance.

# Advantages of Relational Databases
---
- **Create meaningful information** by joining tables.
- **Flexibility** to make changes while the database is in use
- **Minimize data redundancy** by allowing relationships to be defined between tables.
- Offer export and import options that provide **Ease of backup and disaster recovery**.
- Are **ACID compliant**, ensuring accuracy and reliability in database transactions.

# Use Cases of RDBMS
---
**Online Transaction Processing (OLTP) Applications** Can support transaction-oriented tasks that run at high rates and:
- Accommodate large number of users
- Manage small amounts of data.
- Support frequent queries and fast response times.

**Data Warehouses** Can be optimized for Online Analytical processing (OLAP)

**IoT Solutions** Provide the speed and ability to collect and process data from edge devices.

# Limitations of RDBMS:
---
- Does not work well with **Semi-Structured and Unstructured Data**
- Migrations between two RDBMS's is possible only when the source and destination tables have identical schemas and data types.
- Entering a value greater than the defined length of a data field results in loss of information.