-- E-commerce Sales Analysis (SQLite)

-- 1. Monthly revenue and profit
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(sales), 2) AS revenue,
       ROUND(SUM(profit), 2) AS profit
FROM sales
GROUP BY month
ORDER BY month;

-- 2. Category performance
SELECT category,
       COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(sales), 2) AS revenue,
       ROUND(SUM(profit), 2) AS profit,
       ROUND(100.0 * SUM(profit) / SUM(sales), 2) AS profit_margin_pct
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 3. Regional performance
SELECT region,
       COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(sales), 2) AS revenue,
       ROUND(SUM(profit), 2) AS profit
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- 4. Top products by revenue
SELECT product,
       category,
       ROUND(SUM(sales), 2) AS revenue
FROM sales
GROUP BY product, category
ORDER BY revenue DESC
LIMIT 10;

-- 5. Repeat customers
SELECT customer_id,
       COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(sales), 2) AS revenue
FROM sales
GROUP BY customer_id
HAVING COUNT(DISTINCT order_id) > 1
ORDER BY revenue DESC;
