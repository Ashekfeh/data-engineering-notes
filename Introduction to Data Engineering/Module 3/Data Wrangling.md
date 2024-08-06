#  Introduction
---
**Data wrangling/munging** is an iterative process that involves:
- Data Exploration
- Transformation
- Validation
- Making data available for credible and meaningful analysis

# Transformation
---
## Structuring Dat
---
this task includes action that change the form and schema of your data. Data will come from multiple sources (i.e. relational data base, web API, etc.) and In order to merge them, you will need to change the form or schema of your data.

**Joins**: Combines columns. When two tables are joined together, columns from the first source table are combined with columns from the second source table—in the same row. So, each row in the resultant table contains columns from both tables.

**Unions**:Unions combine rows. Rows of data from the first source table are combined with rows of data from the second source table into a single table. Each row in the resultant table is from one source table or another.

## Normalization and Denormalization
---
**Normalizing** data includes:
- Cleaning unused data.
- Reducing redundancy.
- Reducing inconsistency.

> [!note] #NOTE: Data coming from [[Factors for Selecting and Designing Data Stores#Intended use of data|Transactional Systems]] is <ins>highly normalized</ins>

**Denormalizing** data includes:
- Denormalizing data includes combining data from multiple tables into a single table for faster querying of data for reports and analysis.

## Cleaning Data
---
Cleaning tasks are actions that fix irregularities in data in order to produce a credible and accurate analysis.

### Inspection
- Detecting errors and issues
- Validating against rules and constraints
- Profiling data to inspect source data.
- Visualizing data using statistical methods

> [!note] #NOTE: Data profiling helps you to inspect the **source data** to understand the *structure*, *content*, and *interrelationships* in your data. it uncovers ==anomalies== and ==data quality issues== (i.e. missing values, duplicate data, inconsistent data formats, and outliers.)

> [!note] #NOTE: Visualizing the data helps you spot outliers[^1]

### Cleaning
The technique you apply for cleaning your dataset will depend on your <ins>use case</ins> and the <ins>type of issues you encounter</ins>.

Some common issues with data:

**Missing Values** can cause unexpected or biased results, you can:
- Filter out records with missing values.
- Source missing information (in case it is intrinsic to your use case For example, missing age data from a demographics study)
- Imputation, that is, calculate the missing values based on statistical values.

**Duplicate Data** ==needs to be removed==

**Irrelevant Data** is data that is not contextual to your use case.

**Data type conversion** is needed to <ins>ensure that values in a field are stored as the data type of THAT field</ins>

**Standardizing data** is needed to ensure date-time formats and units of measurement are standard across the dataset.

**Syntax Error** such as white space, extra spaces, typos and formats ==need to be fixed==

**Outliers**[^1] need to be examined for accuracy and inclusion of dataset.



---
[^1]: An _outlier_ is an observation that lies an abnormal distance from other values in a random sample from a population. In a sense, this definition leaves it up to the analyst (or a consensus process) to decide what will be considered abnormal. Before abnormal observations can be singled out, it is necessary to characterize normal observations.