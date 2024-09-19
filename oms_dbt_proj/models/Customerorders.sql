WITH CUSTOMERORDERS AS (
SELECT
c.CustomerID,
CONCAT(c.firstName, ' ', c.lastName) AS CustomerName,
COUNT(o.OrderID) AS No_Of_Orders
FROM L1_LANDING.CUSTOMERS c
INNER JOIN L1_LANDING.ORDERS o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, CustomerName
ORDER BY No_Of_Orders DESC
)
SELECT CustomerID, CustomerName, No_Of_Orders
FROM CUSTOMERORDERS