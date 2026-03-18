import pandas as pd
data = {
    "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012],
    "CustomerID": ["C001","C002","C003","C001","C004","C002","C005","C003","C006","C007","C001","C008"],
    "Product": ["Laptop","Phone","Shoes","Tablet","T-shirt","Watch","Laptop","Shoes","Headphones","Backpack","Phone","Watch"],
    "Category": ["Electronics","Electronics","Fashion","Electronics","Fashion","Accessories","Electronics","Fashion","Electronics","Accessories","Electronics","Accessories"],
    "Price": [60000,30000,2000,25000,800,5000,60000,2000,4000,1500,30000,5000],
    "Quantity": [1,2,3,1,5,3,1,4,5,6,1,4],
    "OrderDate": ["2024-01-10","2024-01-15","2024-02-05","2024-02-18","2024-03-01","2024-03-10",
                  "2024-04-04","2024-04-12","2024-05-06","2024-05-15","2024-06-02","2024-06-20"],
    "City": ["Delhi","Mumbai","Bangalore","Delhi","Chennai","Mumbai","Bangalore","Delhi","Hyderabad","Delhi","Mumbai","Chennai"]
}

df = pd.DataFrame(data)

print("\nDataset")
print(df)


df["Revenue"] = df["Price"] * df["Quantity"]

print("\nRevenue per Order")
print(df[["OrderID","Revenue"]])

top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Selling Products")
print(top_products)


city_revenue = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)

print("\nCity with Highest Revenue")
print(city_revenue.head(1))


df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Sales Trend")
print(monthly_sales)


customer_spending = df.groupby("CustomerID")["Revenue"].sum()

high_spenders = customer_spending[customer_spending > 50000]

print("\nCustomers spending more than ₹50,000")
print(high_spenders)


category_profit = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\nMost Profitable Category")
print(category_profit.head(1))


pivot = pd.pivot_table(df, values="Revenue", index="Category", columns="City", aggfunc="sum", fill_value=0)

print("\nPivot Table: Revenue by Category and City")
print(pivot)