import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url_link = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/project/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
# count the needed
count = 0

html_page = requests.get(url_link).text
data = BeautifulSoup(html_page, 'html.parser')

# Here, the variable tables gets the body of all the tables in the web page
# and the variable rows gets all the rows of the first table.
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count < 50:
        # Extract all the td data objects in the row and save them to col.
        col = row.find_all('td')
        # Check if the length of col is 0, that is, if there is no data in a current row.
        # This is important since, many times there are merged rows that are not apparent in the web page appearance.
        if len(col) != 0:
            # Create a dictionary data_dict with the keys same as the columns of the dataframe
            # created for recording the output earlier and corresponding values from the first three headers of data.
            # If the <td> tag contains text, contents[0] will return that text as a string.
            # If the <td> tag contains other tags or elements, contents[0] will return the first of those elements.
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            # Convert the dictionary to a dataframe and concatenate it with the existing one.
            # This way, the data keeps getting appended to the dataframe with every iteration of the loop.
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

# saving to csv file
# df.to_csv("C:/Users/Toshiba/Documents/top_50_films.csv")

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Load the table into a pandas DataFrame
query = f"SELECT * FROM {table_name}"
df_loaded = pd.read_sql_query(query, conn)

# Print the loaded DataFrame
print(df_loaded)
conn.close()
