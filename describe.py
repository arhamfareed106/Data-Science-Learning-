import pandas as pd
data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}

df=pd.DataFrame(data)

print("sample dataframe")
print(df)

print("descriptive stattic")
print(df.describe())