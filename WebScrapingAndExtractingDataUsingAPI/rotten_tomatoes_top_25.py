import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url_link = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
db_name = 'MoviesRottenTomatoes.db'
table_name = 'Top_25'
csv_path = '/home/project/top_50_films.csv'
df = pd.DataFrame(columns=["Film", "Year", "Rotten Tomatoes"])
count = 0

html_page = requests.get(url_link).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count < 25:

        col = row.find_all('td')

        if len(col) != 0:
            data_dict = {"Film": col[1].contents[0],
                         "Year": col[2].contents[0],
                         "Rotten Tomatoes": col[3].contents[0]
                         }

            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

df['Year'] = df['Year'].astype(int)

# saving to csv file
# df.to_csv("C:/Users/Toshiba/Documents/top_50_films.csv")

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)

query = f"SELECT * FROM {table_name}"
df_loaded = pd.read_sql_query(query, conn)
print(df_loaded)

filtered_df = df_loaded[(df_loaded['Year'] >= 2000)]

print(filtered_df)
conn.close()
