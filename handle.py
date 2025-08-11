import pandas as pd


data= {
    "name": ["arham", "None", "ali", "ahmad"],
    "age": [22, None, 34, 25],
    "salary":[2200,None,5000,6000]
        
}

df= pd.DataFrame(data)

print(df)

# df.fillna(0, inplace=True)

df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)

print(df)