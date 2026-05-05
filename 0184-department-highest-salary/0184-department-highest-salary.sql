# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e, Department d
WHERE e.departmentId = d.id 
AND e.salary = (
    SELECT MAX(salary) 
    FROM employee
    WHERE departmentId = d.id 
)
