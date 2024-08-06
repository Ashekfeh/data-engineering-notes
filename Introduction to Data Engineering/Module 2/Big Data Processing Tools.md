# Apache Hadoop
---
A collection of tools that provide distributes storage and processing of big data.
Distributed storage and processing of large datasets across clusters of computers.

**Node**: A single computer.
Cluster: A collection of nodes.

>[!note] #NOTE Hadoop provides a **reliable**, **scalable**, and cost-effective solution for storing data with no format requirements.

## Benefits include:
- **Better real-time driven decisions**: Incorporate emerging data formants not traditionally used in data warehouses
- **Improved data access and analysis**: Provides real-time, self-service access to stakeholders
- **Data offload and consolidation**: Optimizes and streamlines costs by consolidating data, including cold data across organization.

## Hadoop Distributed File System (HDFS)
HDFS is a storage system for big data that runs on multiple commodity hardware connected through a network.

**HDFS**:
- Provides a scalable and reliable big data storage by partitioning files over multiple nodes.
- Splits large files across multiple computers, allowing parallel access to them.
- Replicates file blocks on different nodes to prevent data loss.

**Advantages:**
- **Scalability**: HDFS can scale to accommodate large data sets by distributing the data across multiple nodes in a cluster. This allows for efficient storage and processing of big data.
- **Fault-tolerance**: HDFS replicates data blocks on different nodes, ensuring data availability even if a server fails. This fault-tolerance feature helps in maintaining data integrity and reliability.
- **Data locality**: HDFS follows the principle of data locality, which means that computations are performed on the nodes where the data is stored. This minimizes network congestion and increases throughput, especially when working with large data sets.
- **Fast recovery**: HDFS is designed to detect faults and automatically recover from hardware failures. This ensures fast recovery and reduces downtime.
- **Streaming data access**: HDFS supports high data throughput rates, making it suitable for accessing and processing streaming data.
- **Portability**: HDFS is portable across multiple hardware platforms and compatible with various underlying operating systems. This allows for flexibility in deploying HDFS in different environments.
# Apache Hive
---
An open-source data warehouse for reading, writing and managing large data set files that are stored directly in either HDFS or other data storage systems such as Apache HBase.

**Hive is suited for** -> Data warehousing tasks such as <ins>ETL, reporting and data analysis</ins>. Hive enables easy access to data via SQL

> [!note] #NOTE: ==Hadoop== is intended for long sequential scans, because <ins>Hive is based on Hadoop</ins>, queries have high latency - Which means **Hive** is <ins><em>less appropriate for applications that need very fast response time.</em></ins>

> [!note] #NOTE : Hive is read-based which is <ins>NOT suitable</ins> for *transaction processing* that involves a high percentage of write operations.
# Apache Spark
---
A general-purpose data processing engine designed to extract and process large volumes of data for a wide range of applications. **which includes**:
- Interactive Analytics
- Streams Processing
- Machine Learning
- Data Integration
- ETL

Key attributes:
- Has in-memory processing which significantly increases speed of computations
- Provides interfaces for major programming languages such as Java, Scala, Python, R & SQL
- Can run using its standalone clustering technology
- Can also run on top of other infrastructures, such as Hadoop
- Can access data in a large variety of data sources, including HDFS and Hive.
- Processes streaming to data fast
- Performs complex analytics in real-time