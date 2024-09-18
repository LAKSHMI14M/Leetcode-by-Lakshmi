select c.name as Customers
from Customers c
full outer join Orders o on c.id=o.customerId
where customerId is null;