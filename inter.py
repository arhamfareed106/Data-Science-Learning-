import pandas as pd


data= {
    "name": ["arham", "None", "ali", "ahmad"],
    "age": [22, None, 34, 25],
    "salary":[2200,None,5000,6000]
        
}

df = pd.DataFrame(data)

print(df)

df.interpolate(method="linear", axis=0, inplace=True )

