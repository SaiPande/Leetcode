# Write your MySQL query statement below
Select distinct t1.email as Email
from person t1, person t2
where t1.id <> t2.id
and t1.email = t2.email