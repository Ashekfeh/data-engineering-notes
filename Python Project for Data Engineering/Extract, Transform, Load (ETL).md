# Introduction
---
[[ETL, ELT & Data Pipelines#Extract, Transform & Load Process (ETL)|ETL]]  is a type of batch processing. It is a process of extracting large amounts of data from multiple sources and formats and transforming it into one specific data format before loading it onto a database or target.


# Extract
---
## Composite Functions

```python
import glob

# considering we have a bunch of files:
# source1.json
# source2.json
# source3.json
# source1.csv
# source2.csv
# source3.csv

list_csv = glob.glob('*.csv') # ['source1.csv', 'source2.csv', 'source3.csv']

list_json = glob.glob('*.json') # ['source1.json', 'source2.json', 'source3.json']
```

## Extract CSV

```python
def extract_from_csv(file_to_process):
	dataframe = pd.read_csv(file_to_process)
	return dataframe

df = extract_from_csv('source1.csv')
```

## Extract JSON

```python
def extract_from_json(file_to_process):
	dataframe = pd.read_json(file_to_process, lines=True)
	return dataframe

df = extract_from_json('source1.json')
```

## Function Extract CSV

```python
def extract():
	# create an empty dataframe to hold extraced data
	extracted_data = pd.Dataframe(columns=['name', 'height', 'weight'])

	# process all csv files
	for csvfile in glob.glob('*.csv'):
		extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)

	# process all json files
	for jsonfile in glob.glob("*.json"):
		extracted_data = extracted.append(extract_from_json(jsonfile), ignore_index=True)

	return extracted_data
```

#NOTE: If we did not set the parameter `ignore_index` to true, then the ==index of the data frame `extracted_data` would be the same as the row Number of the original file.== If we set the `ignore index` to true, then the ==order of each row would be the same as the order the row was appended to the data frame.==.

# Transform
---
## Conversion function

```python
def transform(data):
	# convert height which is in inches to millimeters
	# Convert inches to meters and round off to two decimals (one inch is 0.0254)
	data['height'] = round(data.height * 0.0254, 2)

	# convert pound to kgs and round off two decimals (one pound is 0.45359237)
	data['weight'] = round(data.weight * 0.45359237, 2)
```

# Loading and Logging
---

## Loading
```python
def load(targetfile, data_to_load):
	data_to_load.to_csv(targetfile)

targetfile = 'transformed_data.csv'
load(targetfile, transformed_data)
```

## Logging Entries

```python
from datetime import datetime

def log(message):
	timestamp_format = '%Y-%h-%d-%H:%M:%S'
	now = datetime.now()
	timestamp = now.strftime(timestamp_format)
	with open( "logfile.txt". "a" ) as f:
		f.write( timestamp + ',' + message + '\n' )
```

# Final Call
---
```python
log("ETL Job Started")

log("Extract phase started")
extracted_data = extract()
log("Extract Job Ended")

log("Transform Job Started")
transformed_data = transform(extracted_data)
log("Transform Job Ended")

log("Load Job Started")
load(targetfile, transformed_data)
log("Load Job Ended")
```
