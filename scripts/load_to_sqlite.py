import pandas as pd
import sqlite3

# Read cleaned data
df = pd.read_csv("data/processed/cleaned_retail_sales.csv")

# Create SQLite database
conn = sqlite3.connect("retail.db")

# Load dataframe into database
df.to_sql(
    "cleaned_retail_sales",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into SQLite database.")

conn.close()