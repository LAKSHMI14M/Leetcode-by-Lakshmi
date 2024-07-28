select 'Low Salary' as category ,count(*) as accounts_count
from  Accounts
where income <20000
union All
select 'Average Salary' as category ,count(*) as accounts_counts
from Accounts
where income  between 20000 and 50000
union all 
select 'High Salary' as category ,count(*) as accounts_counts
from  Accounts
where income >50000
order by accounts_count desc;
