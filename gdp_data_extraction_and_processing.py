import pandas as pd
import numpy as np

# Specify the URL of the webpage
url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

# Read all tables from the webpage
tables = pd.read_html(url)

# Retain table number 3
df = tables[3]

# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0, 2]]

# Retain the rows with index 1 to 10, indicating the top 10 economies of the world
df = df.iloc[1:11]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ["Country", "GDP (Million USD)"]

# Convert GDP values from millions to billions and format to two decimal points
df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(float) / 1000
df["GDP (Million USD)"] = df["GDP (Million USD)"].round(2)

# Change the column name to reflect the new unit (Billion USD)
df.columns = ["Country", "GDP (Billion USD)"]

# Display the modified DataFrame
print("\nModified DataFrame with GDP in Billions:")
print(df)
