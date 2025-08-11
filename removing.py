import pandas as pd
from sqlalchemy import true

data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}

df = pd.DataFrame(data)
print(df)
df.drop(columns=['age'], inplace=True)

print(df)