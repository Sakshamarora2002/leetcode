# Write your MySQL query statement below
with cte_difference as (
    select *, id- (row_number() over()) as diff_ids
    from Stadium
    where people>99
)
select id,visit_date,people from cte_difference
where diff_ids in (select diff_ids from cte_difference group by diff_ids having count(*)>2)
order by visit_date asc;