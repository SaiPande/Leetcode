# Write your MySQL query statement below
Select t2.id As Id from Weather t1, Weather t2
Where t1.temperature < t2.temperature and datediff(t2.recordDate,t1.recordDate) = 1