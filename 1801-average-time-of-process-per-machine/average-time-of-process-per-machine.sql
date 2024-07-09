/* Write your T-SQL query statement below */
SELECT
    machine_id,
    ROUND(AVG(process_time), 3) AS processing_time
FROM (
    SELECT
        A.machine_id,
        A.process_id,
        MAX(CASE WHEN A.activity_type = 'end' THEN A.timestamp END) - MAX(CASE WHEN A.activity_type = 'start' THEN A.timestamp END) AS process_time
    FROM Activity A
    GROUP BY A.machine_id, A.process_id
) AS ProcessTimes
GROUP BY machine_id;
