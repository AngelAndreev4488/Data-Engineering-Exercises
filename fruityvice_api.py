import pandas as pd
import requests
import json


data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

print(pd.DataFrame(results))

#  data needs to be 'flattened' or normalized
df2 = pd.json_normalize(results)

print(df2)

# Filter the DataFrame to get rows where the "name" column is 'Cherry'
cherry = df2.loc[df2["name"] == 'Cherry']

# Access the 'family' and 'genus' columns from the first row of the filtered DataFrame
family = cherry.iloc[0]['family']
genus = cherry.iloc[0]['genus']

# Print the results
print(family, genus)


# how many calories are contained in a banana
banana = df2.loc[df2['name'] == 'Banana']

calories = banana.iloc[0]['nutritions.calories']

print(f"Banana calories: {calories}")

