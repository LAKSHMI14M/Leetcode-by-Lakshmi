# Write your MySQL query statement below
WITH FriendCounts AS (
    SELECT
        requester_id AS id,
        COUNT(DISTINCT accepter_id) AS num
    FROM
        RequestAccepted
    GROUP BY
        requester_id

    UNION ALL

    SELECT
        accepter_id AS id,
        COUNT(DISTINCT requester_id) AS num
    FROM
        RequestAccepted
    GROUP BY
        accepter_id
)

SELECT
    id,
    SUM(num) AS num
FROM
    FriendCounts
GROUP BY
    id
ORDER BY
    num DESC
LIMIT 1;
