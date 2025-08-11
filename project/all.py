import pandas as pd


df= pd.read_csv("F:\coding\company project\data science learn\project\sales_data_sample.csv", encoding="latin1")

df.sort_values( by="QUANTITYORDERED", ascending=True, inplace=True)

print(df)