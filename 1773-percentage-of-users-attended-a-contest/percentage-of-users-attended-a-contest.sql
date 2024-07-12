SELECT 
    r.contest_id,
    ROUND(CAST(COUNT(r.user_id) as float ) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM 
    Register r
GROUP BY 
    r.contest_id
ORDER BY 
    percentage DESC,
    r.contest_id ASC;
