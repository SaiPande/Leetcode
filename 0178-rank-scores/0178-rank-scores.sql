# Write your MySQL query statement below
Select score, dense_rank() OVER (ORDER BY score DESC) AS 'rank'
from scores
