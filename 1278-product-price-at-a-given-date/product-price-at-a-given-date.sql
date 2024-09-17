SELECT p.product_id,
       COALESCE(pr.new_price, 10) AS price
FROM (SELECT DISTINCT product_id
      FROM Products) AS p
LEFT JOIN (SELECT product_id,
                   new_price,
                   change_date
            FROM Products
            WHERE change_date <= '2019-08-16') AS pr
ON p.product_id = pr.product_id
AND pr.change_date = (
    SELECT MAX(change_date)
    FROM Products
    WHERE product_id = pr.product_id
    AND change_date <= '2019-08-16'
)
ORDER BY p.product_id;
