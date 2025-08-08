from numpy import shape
import pandas as pd

data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}

df = pd.DataFrame(data)
print(df)
print(f"Shape: {df,shape}")

print(f"colum_name: {df.columns}")