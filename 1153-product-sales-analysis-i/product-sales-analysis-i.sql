/* Write your T-SQL query statement below */
select p.product_name,S.year,S.price
from Sales S
join  Product p on S.product_id=p.product_id;