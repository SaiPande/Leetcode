# Write your MySQL query statement below
Select t1.name as Customers from Customers t1
where not exists (
    Select t2.customerId
    from Orders t2
    Where t2.customerId = t1.id)
