import pandas as pd


data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}


df = pd.DataFrame(data)

#display the dataframe

print("sample data frame")

print(df)
print("single colum")
print(df["name"])


subset = df[["name", "age"]]

print(subset)