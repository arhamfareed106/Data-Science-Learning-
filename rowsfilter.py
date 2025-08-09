import pandas as pd

data= {
    "name": ["arham", "azhan", "ali", "ahmad"],
    "age": [22, 23, 34, 25],
    "salary":[2200,3000,5000,6000]
        
}

df = pd.DataFrame(data)     

high_salary= df[df["salary"]> 2000]

print(high_salary)


filterd= df[(df["salary"]> 3000) & (df["age"]> 23) ]

print(filterd)