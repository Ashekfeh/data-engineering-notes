# Counting
---
counting the number of rows of data, or records in datasets.

**Examples:**
```sql
-- counts the number of rows in the dataset
SELECT COUNT(*) FROM CarSaleDetails;

-- Displays the unique car dealers in the dataset
SELECT DISTINCT Dealer from CaresSaleDetails;

-- Counting the number of unique/distinct car dealers in dataset
SELECT COUNT(DISTINCT Dealer) FROM CarSaleDetails; 
```

# Aggregation
---
**Aggregation functions** help provide an overview of the dataset from different perspectives.

```sql
-- Calculating the sum of a numeric column
SELECT SUM(Sale_Amount) AS sum_all FROM CarSaleDetails;

-- Calculating the average value of a numeric column
SELECT AVG(Sale_Amount) AS avg_all FROM CarSaleDetails;

-- Calculating the stanadard deviation to see HOW SPREAD THE NUMBERS ARE
SELECT STDDEV(Sale_Amount) AS std_all FROM CarSaleDetails;
```

# Extreme Value Identification
---
Identifying extreme values in a dataset.

```sql
-- Calculating the maximum value in a column
SELECT MAX(Sale_Count) AS max_all FROM CarSaleDetails;

-- Calculating the minimum value in a column
SELECT MIN(Sale_Count) AS max_all FROM CarSaleDetails;
```

# Slicing Data
---
Finding customers based on specific conditions or set of conditions

```sql
-- Finds dealers in Albuquerque and Texline
SELECT Dealer FROM CarSaleDetails WHERE Dealer City IN ("Albuquerque", "Texline")
```

# Sorting Data
---
**Sorting Data** helps to arrange data in a meaningful order, making it easier to understand and analyze data.

```sql
SELECT * FROM CarSaleDetails ORDER BY Date_of_Purchase;
```

# Filtering Patterns
---
Filter patterns to <ins>perform partial matches of data values</ins>

```sql
SELECT * FROM CarSaleDetails WHERE Pin LIKE "871%"
```

> [!note] #NOTE: `EQUAL TO` Operator returns records in which a data value matches a certain value

> [!note] #NOTE: `LIKE` Operator helps you to specify a pattern to return records that match a data value partially.

# Grouping Data
---
Grouping data based on ==commonality==

```sql
SELECT SUM(Sale_Amount) as area_sum, Pin FROM CarSaleDetails GROUP BY Pin
```