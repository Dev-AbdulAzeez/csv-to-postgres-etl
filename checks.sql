-- 1. Total rows loaded (must match the "Loaded" count from etl.py)
SELECT COUNT(*) FROM sales_clean;

-- 2. Nulls left in key columns (expect 0)
SELECT COUNT(*) FROM sales_clean
WHERE order_date IS NULL OR sales IS NULL;

-- 3. Duplicate order lines (expect no rows)
SELECT order_id, product_id, COUNT(*)
FROM sales_clean
GROUP BY order_id, product_id
HAVING COUNT(*) > 1;

-- 4. Total sales (compare with pandas)
SELECT ROUND(SUM(sales)::numeric, 2) FROM sales_clean;

-- 5. Date range of the data
SELECT MIN(order_date), MAX(order_date) FROM sales_clean;