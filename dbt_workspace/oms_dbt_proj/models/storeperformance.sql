select o.STOREID,
sum(oi.revenue) revenue,
SUM(st.salestarget) as salestarget
FROM  {{ ref('Order_stg') }} o
INNER JOIN {{ ref('Orders_fact') }} oi on o.orderid=oi.orderid
INNER JOIN {{ ref('salestargets') }} st on st.storeid=o.STOREID
GROUP BY o.STOREID