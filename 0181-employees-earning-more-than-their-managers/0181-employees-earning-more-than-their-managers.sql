# Write your MySQL query statement below
select ed.name as Employee from Employee as ed ,Employee as em
where ed.managerId= em.id and ed.salary>em.salary; 