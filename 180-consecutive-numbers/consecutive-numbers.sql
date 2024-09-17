# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num, 
        id,
        ROW_NUMBER() OVER (ORDER BY id) AS rn,
        ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
    FROM Logs
) AS numbered
GROUP BY num, (rn - grp)
HAVING COUNT(*) >= 3;
