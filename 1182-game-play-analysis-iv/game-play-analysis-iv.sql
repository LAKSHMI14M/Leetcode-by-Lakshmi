SELECT 
    ROUND(COUNT(DISTINCT a.player_id) * 1.0 / COUNT(DISTINCT first_logins.player_id), 2) AS fraction
FROM 
    (SELECT player_id, MIN(event_date) AS first_login
     FROM Activity
     GROUP BY player_id) AS first_logins
LEFT JOIN 
    Activity AS a
ON 
    first_logins.player_id = a.player_id 
    AND a.event_date = DATE_ADD(first_logins.first_login, INTERVAL 1 DAY);
