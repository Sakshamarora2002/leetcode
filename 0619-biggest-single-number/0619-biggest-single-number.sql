# Write your MySQL query statement below
WITH RankedNumbers AS (
    SELECT num, 
           RANK() OVER (ORDER BY num) AS rk,
           COUNT(*) OVER (PARTITION BY num) AS cnt
    FROM MyNumbers
)
SELECT MAX(num) as num
FROM RankedNumbers
WHERE cnt = 1;  -- Ensures only distinct numbers are considered

