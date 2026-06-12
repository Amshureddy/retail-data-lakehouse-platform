import pandas as pd

file_path = "data/raw/Brazilian E-Commerce Public Dataset by Olist.csv"

df = pd.read_csv(file_path)

print("Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())