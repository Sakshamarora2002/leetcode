SELECT d.Name AS "department", e.name AS "Employee" ,e.salary 
FROM (
    SELECT departmentid, Name, Salary, DENSE_RANK() OVER(PARTITION BY departmentid ORDER BY salary DESC) AS r
    FROM employee
) e
JOIN department d ON e.departmentid = d.id
WHERE e.r <= 3;
