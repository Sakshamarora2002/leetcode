# Write your MySQL query statement below
select u.name , sum(t.amount) as Balance from Users as u
join Transactions as t
on u.account=t.account
group by u.account
having Balance>10000;