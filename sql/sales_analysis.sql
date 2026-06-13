-- Total Revenue

SELECT
    SUM(payment_value) AS total_revenue
FROM cleaned_retail_sales;


-- Revenue by State

SELECT
    customer_state,
    SUM(payment_value) AS revenue
FROM cleaned_retail_sales
GROUP BY customer_state
ORDER BY revenue DESC;


-- Average Delivery Days

SELECT
    AVG(delivery_days) AS avg_delivery_days
FROM cleaned_retail_sales;


-- Top Payment Methods

SELECT
    payment_type,
    COUNT(*) AS total_orders
FROM cleaned_retail_sales
GROUP BY payment_type
ORDER BY total_orders DESC;