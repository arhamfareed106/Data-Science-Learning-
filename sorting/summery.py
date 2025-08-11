import pandas as pd

data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}

df=pd.DataFrame(data)


avg_salary= df['age'].mean()

print(avg_salary)