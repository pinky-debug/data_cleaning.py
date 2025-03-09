import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicates if any
df = df.drop_duplicates()

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Save the cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)
print("Data cleaning completed. File saved as 'cleaned_sales_data.csv'.")
