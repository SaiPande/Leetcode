# Write your MySQL query statement below
SELECT t1.name as Employee
FROM employee t1, employee t2
WHERE t1.managerId = t2.id
AND t1.salary > t2.salary 