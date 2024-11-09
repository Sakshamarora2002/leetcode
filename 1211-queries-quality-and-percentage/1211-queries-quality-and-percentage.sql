# Write your MySQL query statement below
SELECT 
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(CASE WHEN COALESCE(rating, 0)< 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM 
    Queries where query_name is not null
GROUP BY 
    query_name;