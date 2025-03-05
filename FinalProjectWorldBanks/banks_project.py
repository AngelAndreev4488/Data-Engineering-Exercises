from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime


url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
exchange_rate_csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
table_attribs = ["Name", "MC_USD_Billion"]
table_attribs_final = ["Name", "MC_USD_Billion", "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
output_csv_path = './Largest_banks_data.csv'


def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt", "a") as f:
        f.write(timestamp + ' : ' + message + '\n')


def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')

    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) >= 3:  # Check if the row has enough columns
            try:
                country_with_flag = col[0].get_text(strip=True)
                name = col[1].get_text(strip=True)  # Bank name
                mc_usd_billion = float(col[2].get_text(strip=True).replace(',', ''))

                row_data = {"Name": name, "MC_USD_Billion": mc_usd_billion}  # Example row
                df.loc[len(df)] = row_data
            except Exception as e:
                print(f"Error processing row: {e}")

    log_progress('Data extraction complete. Initiating Transformation process')
    return df


def transform(df, csv_path):

    exchange_rates = pd.read_csv(csv_path)

    exchange_rate_dict = {}
    for index, row in exchange_rates.iterrows():
        exchange_rate_dict[row['Currency']] = row['Rate']

    # Add new columns for market capitalization in other currencies
    df['MC_GBP_Billion'] = df['MC_USD_Billion'] * exchange_rate_dict['GBP']
    df['MC_EUR_Billion'] = df['MC_USD_Billion'] * exchange_rate_dict['EUR']
    df['MC_INR_Billion'] = df['MC_USD_Billion'] * exchange_rate_dict['INR']

    df['MC_GBP_Billion'] = df['MC_GBP_Billion'].round(2)
    df['MC_EUR_Billion'] = df['MC_EUR_Billion'].round(2)
    df['MC_INR_Billion'] = df['MC_INR_Billion'].round(2)

    log_progress('Data transformation complete. Initiating Loading process')
    return df


def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)
    log_progress('Data saved to CSV file')


def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    log_progress('Data loaded to Database as a table, Executing queries')


def run_query(query_statement, sql_connection):
    print(pd.read_sql(query_statement, sql_connection))
    log_progress('Process Complete')


log_progress('Preliminaries complete. Initiating ETL process')

df_extracted = extract(url, table_attribs)
print(df_extracted)

df_transformed = transform(df_extracted, exchange_rate_csv_path)
print(df_transformed)

load_to_csv(df_transformed, output_csv_path)

sql_connection = sqlite3.connect('Banks.db')
log_progress('SQL Connection initiated')

load_to_db(df_transformed, sql_connection, table_name)

query_statements = ['SELECT * FROM Largest_banks', 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks',
                    'SELECT Name from Largest_banks LIMIT 5']
for query in query_statements:
    run_query(query, sql_connection)

sql_connection.close()
log_progress('Server Connection closed')
