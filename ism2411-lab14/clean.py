import pandas as pd

print("---Exercise 1---")

sales = pd.read_csv("data/messy_sales.csv")
sales.info()

print(sales.isnull().sum())
#Order ID has 31 missing values.
#Order date has 25 missing values.
#Unit price is stored at a str instead of a float.

print("---Exercise 2---")

sales.columns = sales.columns.str.lower().str.replace(" ", "_")

print(sales.columns.tolist())
