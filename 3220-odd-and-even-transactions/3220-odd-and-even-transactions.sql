# Write your MySQL query statement below
# we will be creating two dummy results and join them further
with cte1 as(
    select sum(case when amount%2=0 then amount else 0 end) as even_sum, transaction_date 
    from transactions group by transaction_date
    ),
cte2 as(
    select sum(case when amount%2!=0 then amount else 0 end) as odd_sum, transaction_date 
    from  transactions group by transaction_date
    )
select cte1.transaction_date , cte2.odd_sum , cte1.even_sum from
cte1 join cte2
on 
cte1.transaction_date=cte2.transaction_date
order by cte1.transaction_date asc;
    


