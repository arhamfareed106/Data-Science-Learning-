import pandas as pd

data= {
    "name": ["arham", "azhan", "ali", "ahmad", "usama"],
    "age": [22, 23, 34, 25, 45],
    "salary":[2200,3000,5000,6000, 11000]
        
}

df=pd.DataFrame(data)

grouped= df.groupby("age")['salary'].sum()

print(grouped)