import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")

# Total Sales Calculation
total_revenue = df["Total Sales"].sum()
print(f"Total Revenue: ${total_revenue}")

# Top-Selling Product
top_product = df.groupby("Product")["Total Sales"].sum().idxmax()
top_product_sales = df.groupby("Product")["Total Sales"].sum().max()
print(f"Best-Selling Product: {top_product} (${top_product_sales})")

# Sales by Category
category_sales = df.groupby("Category")["Total Sales"].sum()
print("
Total Sales by Category:")
print(category_sales)

# Save category sales to CSV
category_sales.to_csv("sales_by_category.csv")

print("Data analysis completed. Insights saved to 'sales_by_category.csv'.")
