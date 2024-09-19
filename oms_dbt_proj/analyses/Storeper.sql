select o.STOREID,
sum(oi.revenue) revenue
FROM  {{ ref('Order_stg') }} o
INNER JOIN {{ ref('Orders_fact') }} oi on o.orderid=oi.orderid
GROUP BY o.STOREID