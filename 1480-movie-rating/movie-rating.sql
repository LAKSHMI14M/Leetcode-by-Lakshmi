# Write your MySQL query statement below
WITH UserRatings AS (
    SELECT 
        u.name,
        COUNT(mr.movie_id) AS num_movies
    FROM 
        Users u
    JOIN 
        MovieRating mr ON u.user_id = mr.user_id
    GROUP BY 
        u.user_id, u.name
),

TopUser AS (
    SELECT 
        name
    FROM 
        UserRatings
    ORDER BY 
        num_movies DESC, name ASC
    LIMIT 1
),

MovieRatings AS (
    SELECT 
        m.title,
        AVG(mr.rating) AS avg_rating
    FROM 
        MovieRating mr
    JOIN 
        Movies m ON mr.movie_id = m.movie_id
    WHERE 
        mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
    GROUP BY 
        m.movie_id, m.title
),

TopMovie AS (
    SELECT 
        title
    FROM 
        MovieRatings
    ORDER BY 
        avg_rating DESC, title ASC
    LIMIT 1
)

SELECT 
    (SELECT name FROM TopUser) AS results
UNION ALL
SELECT 
    (SELECT title FROM TopMovie);
