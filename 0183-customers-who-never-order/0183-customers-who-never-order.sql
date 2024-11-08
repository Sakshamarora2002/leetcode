# Write your MySQL query statement below
select e.name as Customers from Customers as e left join Orders o
on e.id=o.customerId
where customerId is null;



