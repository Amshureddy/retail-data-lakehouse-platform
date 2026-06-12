import pandas as pd

file_path = "data/raw/Brazilian E-Commerce Public Dataset by Olist.csv"

df = pd.read_csv(file_path)

print("Original shape:", df.shape)

df = df.drop_duplicates()

df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
df["order_delivered_customer_date"] = pd.to_datetime(df["order_delivered_customer_date"])

df["delivery_days"] = (
    df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
).dt.days

cleaned_df = df[
    [
        "order_id",
        "customer_id",
        "customer_city",
        "customer_state",
        "product_category_name",
        "payment_type",
        "price",
        "freight_value",
        "payment_value",
        "order_purchase_timestamp",
        "order_status",
        "delivery_days",
    ]
]

cleaned_df.to_csv("data/processed/cleaned_retail_sales.csv", index=False)

print("Cleaned shape:", cleaned_df.shape)
print("Cleaned file saved successfully.")