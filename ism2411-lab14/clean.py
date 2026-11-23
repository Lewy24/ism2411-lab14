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

print("---Exercise 3 ---")

print("Before cleaning:", sales.shape)

sales["quantity_sold"] = sales["quantity_sold"].fillna(sales["quantity_sold"].mean())
sales = sales.dropna(subset=["order_id", "order_date"])

print("After cleaning: ", sales.shape)
print(sales.isnull().sum())

print("---Exercise 4 ---")

sales["order_date"] = pd.to_datetime(sales["order_date"], errors = "coerce")

print("Missing dates after conversion:", sales["order_date"].isna().sum())

sales["unit_price"] = sales["unit_price"].str.replace("$", "", regex = False).str.replace(",", "", regex=False).astype(float)
sales["revenue"] = (sales["unit_price"] * sales["quantity_sold"]).round(2)

print(sales.dtypes)

print("---Exercise 5---")

print("Duplicate rows:", sales.duplicated().sum())
sales =  sales.drop_duplicates()

print("Shape after removing duplicates:", sales.shape)