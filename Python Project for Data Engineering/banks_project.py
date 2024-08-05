import pandas as pd
from datetime import datetime
import sqlite3
import requests
import glob
from bs4 import BeautifulSoup

def log_progress(message: str) -> None:
    """
    logs the progress of the ETL
    """

    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(timestamp + ',' + message + '\n')

def extract(target_url: str, table_attr: list[str]) -> pd.DataFrame:
    '''
    extracts top 10 largest banks in the world ranked by market capitalization in billion USD
    '''
    r = requests.get(target_url)
    bs = BeautifulSoup(r.content, 'html.parser')

    dataframe = pd.DataFrame(columns=table_attr)

    tables = bs.find_all('table')
    target_table = tables[0]

    tr = target_table.find_all('tr')
    tr = tr[1:]
    for row in tr:
        row_data = row.find_all('td')
        name = row_data[1].text.replace('\n', '')
        usd_billion = float("".join(row_data[2].text.replace('\n', '').replace(',', '')))
        dataframe = pd.concat([dataframe, pd.DataFrame([{'Name': name, 'MC_USD_Billion': usd_billion}])], ignore_index=True)

    return dataframe

def transform(extracted_data: pd.DataFrame, exchange_csv: str) -> pd.DataFrame:
    '''
    transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places
    '''

    MC_list = extracted_data['MC_USD_Billion'].tolist()
    exchange_df = pd.read_csv(exchange_csv)
    for row in exchange_df.itertuples(index=True, name='Pandas'):
        extracted_data[f'MC_{row.Currency}_Billion'] = [round(x * row.Rate, 2) for x in MC_list]

    return extracted_data

def load_to_csv(data: pd.DataFrame, target_csv: str) -> None:
    '''
    load data to csv
    '''

    data.to_csv(target_csv)

def load_to_db(sql_connection: sqlite3.Connection, data: pd.DataFrame, database: str, table: str) -> None:
    '''
    load data to sqlite database
    '''

    data.to_sql(table, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection: sqlite3.Connection) -> None:
    '''
    run queries on sqlite database
    '''
    
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


target_url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attr = ['Name', 'MC_USD_Billion']
exchange_csv = 'exchange_rate.csv'
target_csv = './Largest_banks_data.csv'
log_file = 'log_code.txt'
target_database = 'Banks.db'
table_name = 'Largest_banks'

log_progress('Preliminaries complete. Initiating ETL process')


log_progress(f"Extracting data from {target_url}")
extracted_data = extract(target_url, table_attr)
log_progress(f"Extracton Done")

log_progress("Transforming data started")
transformed_data = transform(extracted_data, exchange_csv)
print(transformed_data)
log_progress("Transforming data Done")

log_progress("Loading data to CSV")
load_to_csv(transformed_data, target_csv)
log_progress("Loading data to CSV DONE")

conn = sqlite3.connect('Banks.db')
log_progress("Connection to database initiated")

load_to_db(conn, transformed_data, target_database, table_name)
log_progress("Data Loaded to Database as table running queries")

select_all = f'SELECT * FROM {table_name}'
run_query(select_all, conn)

select_avg = f'SELECT AVG(MC_GBP_Billion) FROM {table_name}'
run_query(select_avg, conn)

select_name = f'SELECT Name FROM {table_name}'
run_query(select_name, conn)

select_name_5 = f'SELECT Name FROM {table_name} LIMIT 5'
run_query(select_name_5, conn)

log_progress("Process Completed!!!")

conn.close()