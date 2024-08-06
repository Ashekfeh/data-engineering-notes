# Introduction
---
## Layers of a Data Platform Architecture:
1. Data Ingestions or Data Collection Layer
2. Data Storage and Integration Layer
3. Data Processing Layer
4. Analysis and User Interface Layer
5.  Data Pipeline Layer ==(Overlays multiple layers)==

# Data Collection/Ingestion Layer
---
The Data Collection Layer is responsible for connecting to the source systems and bringing the data from these systems into the data platform. 
This layer perform some of following key tasks:
- Transfer data from data sources to the data platform in streaming and batch modes
- Maintain information about the data collected in the metadata repository (i.e. how much data was was ingested in a batch/data source, etc.)

## Tools for Data Ingestion
- [Dataflow | Google Cloud](https://cloud.google.com/dataflow)
- [IBM Streams](https://www.ibm.com/docs/en/streams/4.3.0?topic=welcome-introduction-streams)
- [Streaming Analytics - IBM Cloud](https://cloud.ibm.com/catalog/services/streaming-analytics)
- [Amazon Kinesis](https://aws.amazon.com/pm/kinesis/?trk=dc8c58e6-010d-4e9f-ac23-9b42ecc0c545&sc_channel=ps&ef_id=CjwKCAjwtNi0BhA1EiwAWZaANKmkWG0QvodDJ5jmzgI8KGYW9kTyz2GgxHmIwuXZsQec0O_eVP9kcBoC_akQAvD_BwE:G:s&s_kwcid=AL!4422!3!651510223194!e!!g!!amazon%20kinesis!19828206918!146491677985&gclid=CjwKCAjwtNi0BhA1EiwAWZaANKmkWG0QvodDJ5jmzgI8KGYW9kTyz2GgxHmIwuXZsQec0O_eVP9kcBoC_akQAvD_BwE)
- [Apache Kafka](https://kafka.apache.org/)

# Data Storage and Integration Layer
---
After data is ingested, it needs to be stored and integrated. 
The Storage and Integration Layer in data platforms needs to:
- Store data for processing and long term use.
- Transform and merge extracted data, either logically or physically.
- Make data available for processing in both streaming and batch modes

> [!note] #NOTE The storage layer needs to be **reliable**, **scalable**, **high-performing** & **cost-efficient**.

## Tools For Data Storage
### Relational Databases:
- [IBM Db2](https://www.ibm.com/db2)
- [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- [MySQL](https://www.mysql.com/)
- [Oracle Database](https://www.oracle.com/database/)
- [PostgreSQL](https://www.postgresql.org/)

### Database-as-a-service:
- [IBM Db2 on Cloud](https://www.ibm.com/db2)
- [Amazon RDS](https://aws.amazon.com/free/database/?trk=f82aa888-030f-435f-a5c0-d0513a6b7aa8&sc_channel=ps&ef_id=CjwKCAjwtNi0BhA1EiwAWZaANC4r5v78jzv1HjIlk0Rrvbbtaxv7KI2eSzfgANxfekAKtW5WSlxJzBoClR8QAvD_BwE:G:s&s_kwcid=AL!4422!3!645155970885!e!!g!!amazon%20rds!19572078717!144705012425&gclid=CjwKCAjwtNi0BhA1EiwAWZaANC4r5v78jzv1HjIlk0Rrvbbtaxv7KI2eSzfgANxfekAKtW5WSlxJzBoClR8QAvD_BwE)
- [Google SQL](https://cloud.google.com/sql)
- [Azure SQL](https://azure.microsoft.com/en-us/products/azure-sql/database)

### Non-Relational Database (NoSQL):
- [IBM Cloudant](https://www.ibm.com/products/cloudant)
- [Redis](https://redis.io/)
- [MongoDB](https://www.mongodb.com/)
- [Apache Cassandra](https://cassandra.apache.org/_/index.html)
- [Neo4j](https://neo4j.com/)
## Tools for Data Integration
- [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data)
- [IBM Cloud Pak for Integration](https://www.ibm.com/products/cloud-pak-for-integration)
- [Talend](https://www.talend.com/)
- [OpenStudio](https://openstudio.net/)
### Open Source Tools:
- [Boomi](https://boomi.com/)
- [SnapLogic](https://www.snaplogic.com/)

### Platform as a service (iPaaS):
- [Adeptia Integration Suite](https://support.adeptia.com/hc/en-us/articles/207881013-Overview-of-Adeptia-Integration-Suite)
- [Google Cloud's Integration](https://cloud.google.com/application-integration/docs/overview)
- [IBM Application Integration Suite on Cloud](https://www.ibm.com/docs/en/ais/1.0.0?topic=overview-application-integration-suite)
- [Informatica's Integration Cloud](https://www.informatica.com/products/cloud-integration.html)

# Data Processing Layer
---
Once the data has been *ingested*, *stored* and *integrated*, it need to be processed. **Data validation**, **transformation** and **applying business logic** to the data are some of the things that need to happen in this layer.
The processing layer should be able to:
- Read data in batch or streaming modes from storage and apply transformations
- Support popular querying tools and programming languages.
- Scale to meet the processing demands of a growing dataset.
- Provide a way for analysts to work with data in the data platform.

Some of the Transformation tasks that can occur in this layer:
- **Structuring** - Actions that change the form and schema of the data (which can be as simple as changing the order of fields within a record or as complex as combining fields into complex structures using joints and unions).
- **Normalization** - Cleaning the database of of unused data and reducing redundancy and inconsistency.
- **Denormalization** - Combining data from multiple tables into a single table so that it can be queried more efficiently.
- **Data Cleaning** - Fixing irregularities in data to provide credible data for downstream applications an uses.

## Tools
There are a host of tools available for performing these transformations on data. selected based on the ==data size==, ==structure== and ==specific capabilities of this tool==:
- Spreadsheets
- OpenRefine
- Google DataPrep
- Watson Studio Refinery
- Trifacta
- Python (Libraries such as Pandas)
- R ( #TODO ADD LIBRARIES HERE )

> [!note] #NOTE: **Storage** and **Processing** can ==occur in the same layer==.

> [!note] #NOTE: Data can first be stored in [[Big Data Processing Tools#Apache Hadoop |Hadoop HDFS]] and then processed in a data processing engine like [[Big Data Processing Tools#Apache Spark|Apache Spark]].

>[!note] #NOTE: Data Processing layer can also precede the Data Storage Layer, where transformations are applied before data is loaded, or stored in the database.


# Analysis and user Interface Layer
---
The Analysis and User Interface Layer in data engineering is responsible for delivering processed data to data consumers. It involves the following:

- **Data consumers**: Business Intelligence Analysts, Data Scientists, and other applications/services that need the data.
- **Interactive visual representations**: Dashboards and analytical reports for business stakeholders.
- **Querying tools and programming languages**: SQL for relational databases, SQL-like querying tools for non-relational databases, and programming languages like Python, R, and Java.
- **APIs**: Used for running reports on data, consuming data in real-time, and integrating with other applications/services.
- **Dashboarding and Business Intelligence applications**: Examples include IBM Cognos Analytics, Tableau, Jupyter Notebooks, Python and R libraries, and Microsoft Power BI.

# Data Pipeline
---
Overlaying the [[Architecting The Data Platform#Data Collection/Ingestion Layer|Data Ingestion]], [[Architecting The Data Platform#Data Storage and Integration Layer|Data Storage and Integration]] and [[Architecting The Data Platform#Data Processing Layer|Data Processing]] layers is the **Data Pipeline layer** with <ins>extract, transform and load tools</ins>. This layer is **responsible** for ==implementing and maintaining a continouosly flowing data pipelines==

## Tools
- [Apache Airflow](https://airflow.apache.org/)
- [Dataflow | Google Cloud](https://cloud.google.com/dataflow)