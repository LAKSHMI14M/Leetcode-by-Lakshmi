/* Write your T-SQL query statement below */
select e.name as Employee
from Employee e
join Employee ee on ee.id=e.managerId
where e.salary>ee.salary