SELECT
o.CustomerID,
c.CustomerName AS CustomerName,
o.ordercount AS No_Of_Orders,
o.revenue as revenue
FROM {{ref('Orders_fact')}} o
INNER JOIN {{ref('Customer_stg')}} c 
ON c.CustomerID = o.CustomerID
ORDER BY No_Of_Orders DESC
