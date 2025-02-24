import pandas as pd
import requests
import json

data = requests.get("https://official-joke-api.appspot.com/jokes/ten")

results = json.loads(data.text)

df = pd.json_normalize(results)


df.drop(columns=["type", "id"], inplace=True)

# When inplace=True, the changes are applied directly to the original DataFrame df,
# and no new DataFrame is returned.
#
# If inplace=False (or omitted), the method would return a new DataFrame
# with the specified columns dropped, and the original DataFrame df would remain unchanged.

print(df)
