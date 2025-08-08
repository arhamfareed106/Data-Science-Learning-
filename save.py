import pandas as pd

data= {
    "Name": ["arham", "azhan", "talha",],
    "Age": [20, 30, 22, ],
    "City": ["Lahore", "paras", "karachi"]
}


df = pd.DataFrame(data)
print(df)


df.to_csv("output.csv", index=False)