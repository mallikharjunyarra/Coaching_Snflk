select o.ORDERID, o.ORDERDATE, o.CUSTOMERID, o.EMPLOYEEID, o.STOREID, o.STATUS, o.UPDATED_AT,
count(DISTINCT o.ORDERID) as ordercount,
SUM(oi.quantity*oi.unitprice) as revenue
FROM  {{ ref('Order_stg') }} o
INNER JOIN {{ ref('OrderItems_stg') }} oi on o.orderid=oi.orderid
GROUP BY o.ORDERID, o.ORDERDATE, o.CUSTOMERID, o.EMPLOYEEID, o.STOREID, o.STATUS, o.UPDATED_AT