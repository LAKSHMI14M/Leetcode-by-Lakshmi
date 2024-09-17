# Write your MySQL query statement below
WITH UniqueCities AS (
    SELECT 
        lat, lon
    FROM 
        Insurance
    GROUP BY 
        lat, lon
    HAVING 
        COUNT(*) = 1
),
MatchingTiv AS (
    SELECT 
        tiv_2015
    FROM 
        Insurance
    GROUP BY 
        tiv_2015
    HAVING 
        COUNT(*) > 1
)
SELECT 
    ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM 
    Insurance i
JOIN 
    UniqueCities uc ON i.lat = uc.lat AND i.lon = uc.lon
JOIN 
    MatchingTiv mt ON i.tiv_2015 = mt.tiv_2015;
