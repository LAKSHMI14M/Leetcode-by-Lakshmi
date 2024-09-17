WITH FirstOrders AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),
ImmediateOrders AS (
    SELECT f.customer_id, d.order_date, d.customer_pref_delivery_date
    FROM FirstOrders f
    JOIN Delivery d
    ON f.customer_id = d.customer_id AND f.first_order_date = d.order_date
)
SELECT 
    ROUND(100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS immediate_percentage
FROM ImmediateOrders;
/* Write your T-SQL query statement below */
