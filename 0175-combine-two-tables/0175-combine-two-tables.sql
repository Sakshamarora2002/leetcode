# Write your MySQL query statement below
select FirstName, lastName, city, state
from Person Left join Address 
on Person.personId= Address.personId;