import pandas as pd


data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}

df = pd.DataFrame(data)
# print(df)

df["advance"]= df["salary"]*0.8

print(df)


df.insert(0, "Employee_id", ([1,24,45,55,]))

print(df)