# Retail Data Lakehouse Platform

## Project Overview

This project was created to practice data engineering and analytics concepts using a real-world retail sales dataset.

The project reads raw retail sales data, cleans and transforms it using Python and Pandas, loads the processed data into a SQLite database, and performs SQL analysis to generate business insights.

Through this project, I gained hands-on experience working with Python, SQL, data cleaning, database loading, and basic analytics.

---

## Technologies Used

- Python
- Pandas
- SQL
- SQLite
- Git
- GitHub
- Power BI

---

## Project Workflow

1. Read raw retail sales data from CSV files.
2. Clean and transform the data using Python and Pandas.
3. Load the cleaned data into a SQLite database.
4. Run SQL queries to analyze business performance.
5. Generate insights from sales and customer data.

---

## Project Structure

```text
retail-data-lakehouse-platform/

├── airflow/
│   └── dags/

├── dashboard/
│   └── powerbi_screenshots/

├── data/
│   ├── raw/
│   └── processed/
│       └── cleaned_retail_sales.csv

├── scripts/
│   ├── read_data.py
│   ├── clean_data.py
│   └── load_to_sqlite.py

├── sql/
│   └── sales_analysis.sql

├── .gitignore
└── README.md
```

## Analysis Performed

### Revenue Analysis

Calculated total revenue generated from retail sales data.

### Revenue by State

Analyzed revenue across customer states to identify top-performing regions.

### Average Delivery Time

Calculated average delivery days to evaluate delivery performance.

### Payment Method Analysis

Analyzed customer payment preferences and identified the most commonly used payment methods.

---

## Key Findings

- Average delivery time was approximately 12 days.
- Credit card was the most frequently used payment method.
- Revenue varied significantly across different states.
- Certain states contributed a larger share of total sales.

---

## Skills Demonstrated

- Data Cleaning
- Data Transformation
- SQL Querying
- SQLite Database Management
- ETL Concepts
- Data Analysis
- Git Version Control
- Business Insight Generation

---

## Future Improvements

- Automate the pipeline using Apache Airflow.
- Integrate Snowflake as a cloud data warehouse.
- Build an interactive Power BI dashboard.
- Deploy the pipeline using AWS services.

---

## Author

Amshu Reddy Cheruku
