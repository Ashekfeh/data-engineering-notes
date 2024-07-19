# Extract, Transform & Load Process (ETL)
---
Extract, Transform and load process is an automated process which includes:
- **Gathering** raw data
- **Extracting** information need for reporting and analysis
- **Cleaning, Standardizing & Transforming** data into useable format
- **Loading** data into a data repository

## Extract
Extract is the step where data from source locations is collected for collection.
Extraction can be through:
- **Batch processing** — large chunks of data moved from source to destination at scheduled intervals. <span style="color:lightgreen"> TOOLS:</span> [Stitch]([Stitch: Simple, extensible cloud ETL built for data teams | Stitch (stitchdata.com)](https://www.stitchdata.com/)), [Blendo]([Blendo: #1 ETL Tool | Data Integration & Pipeline Tool](https://www.blendo.co/))
- **Stream processing** — data pulled in real-time from source, transformed in transit, and loaded into data repository. <span style="color:lightgreen"> TOOLS:</span> [Apache Samza]([[Samza (apache.org)](https://samza.apache.org/)), [Apache Storm]([Apache Storm](https://storm.apache.org/)), [Apache Kafka]([Apache Kafka](https://kafka.apache.org/))

## Transform
Transform involves the execution of rules and functions that convert raw data into data that can be used for analysis. For example:
- Standardizing date formats and units of measurement
- Removing duplicate data
- Filtering out data that is not required
- Enriching data (i.e. splitting name into first and last name)
- Establishing key relationships across tables
- Applying business rules and validations
## Loading
Loading is the transportation of processed data in to a repository. It can be:
- **Initial loading** - populating all of the data in the repository
- **Incremental loading** - applying updates and modifications periodically
- **Full refresh** - erasing a data table and reloading fresh data

### Load verification
load verification include:
- Missing or null values
- Server performance
- Load failures

# Extract, Load & Transform Process (ELT)
---

![[Pasted image 20240716025247.png]]
## Advantages:
1. Shortens the cycle between extraction and delivery
2. Allows you to ingest volumes of raw data as immediately as the data becomes available
3. Affords greater flexibility to analyst and data scientists for exploratory data analytics
4. Transforms only that data which is required for a particular analysis so it can be leveraged for multiple use cases
5. ==More Suited to work with BIG DATA ==

# Data Pipelines
---
A data pipeline
- Encompasses the entire journey of moving data from one system to another, including the ETL process
- Can be used for both batch and streaming data
- Supports both long-running batch queries and smaller interactive queries
- Typically loads data into a data lake but can also load data into a variety of target destinations - including other applications or visualizations

| Tool           | website                                                       |
| -------------- | ------------------------------------------------------------- |
| Apache Beam    | [Apache Beam®](https://beam.apache.org/)                      |
| Apache Airflow | [Apache Airflow](https://airflow.apache.org/)                 |
| Data Flow      | [Dataflow \| Google Cloud](https://cloud.google.com/dataflow) |
