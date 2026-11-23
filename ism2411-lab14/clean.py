#Reflection #1: I think when filling in the missing values is the most ambigous since replacing missing info with a average could make the data less accurate.
#Reflection #2: Yes they would since my comments are super simple sentences.
#Reflection #3: 







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


#Shows the shape before cleaning 
print("Before cleaning:", sales.shape)

#Mean is used to replace missing quantities while keeping the rows
sales["quantity_sold"] = sales["quantity_sold"].fillna(sales["quantity_sold"].mean())

#Order id and Order date are essnetial for identifying and tracking orders
sales = sales.dropna(subset=["order_id", "order_date"])

#shape after cleaning
print("After cleaning: ", sales.shape)

#remaining missing values
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

print("---Exercise 6---")

print(sales.describe())
#the unit_price being -1774.99 is very low
#in quantity_sold max being 9999 is very high

#Removing the rows where quantity_sold is 9,999 because the invalid placeholder values. 
#Keep negative revenue becuas it represents legitimate refunds and return
sales = sales[sales["quantity_sold"] != 9999]

print("Shape after removing placeholder rows:, sales.shape")

print("---Exercise 7---")

sales.to_csv("data/clean_sales.csv", index = False)
sales_check = pd.read_csv("data/clean_sales.csv")

print(sales_check.info())

sales_check = pd.read_csv("data/clean_sales.csv", parse_dates = ["order_date"])

print(sales_check.info())