import pandas as pd

df= pd.read_json("sample_Data.json")

print('dispaly 10 rows of first ')
print(df.head())

print('dispaly 10 rows of last ')
print(df.tail ())

# df.to_json("newoutput.xlsx", index=False)