SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary
FROM 
    Employee e
JOIN 
    Department d ON e.departmentId = d.id
WHERE 
    e.salary IN (
        SELECT salary
        FROM (
            SELECT DISTINCT salary
            FROM Employee
            WHERE departmentId = e.departmentId
            ORDER BY salary DESC
            LIMIT 3
        ) AS top_salaries
    )
ORDER BY 
    d.name, e.salary DESC;
