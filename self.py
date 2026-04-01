import pandas as pd


xx=pd.read_csv("orders.csv")
print(xx)
xx["order_date"] = pd.to_datetime(xx["order_date"])

countbyitem=xx.groupby("order_item")["total_amount"].sum()
print(countbyitem)

countbycustomer=xx.groupby("customer_id")["total_amount"].sum()
print(countbycustomer)

bestsoldproduct=xx.groupby("order_item")["total_amount"].sum().sort_values(ascending=False)
print(bestsoldproduct)


dailysales=xx.groupby("order_date")["total_amount"].sum()
print(dailysales)


# Row with highest sales
print(xx.loc[xx["total_amount"].idxmax()])

# Row with lowest sales
print(xx.loc[xx["total_amount"].idxmin()])

# Average
print(xx["total_amount"].mean())

# Which item has maximum sales

print(xx["order_item"].value_counts())


# Extracting month
xx["month"] = xx["order_date"].dt.month
print(xx[["order_date", "month"]].head())

# Extracting month name
xx["month_name"] = xx["order_date"].dt.month_name()
print(xx["month_name"].head())

# Extracting day
xx["Day"]=xx["order_date"].dt.day
print(xx[["order_date","Day"]].head())


# 📊 Monthly sales
monthly_sales = xx.groupby("month")["total_amount"].sum().sort_values()
print(monthly_sales)


# Top customer of the business
top_customer = xx.groupby("customer_id")["total_amount"].sum().sort_values(ascending=False)
print(top_customer.head(1))


# 📆 2. Day Name Analysis (VERY IMPORTANT 🔥)
xx["day_name"] = xx["order_date"].dt.day_name()

day_sales = xx.groupby("day_name")["total_amount"].sum()
print(day_sales)


# Insights---->>>>>>>>

# 1.Top-selling product based on total revenue = Mutton Biryani.
# 2.Customer ID 8 is the highest spending customer.
# 3.March recorded the highest total sales among all months.
# 4.Best days for Busines:-Friday,Saturday,Sunday
# Tuesday and Wednesday are the lowest selling days
# October and December recorded the lowest sales among all months.
