select ORDERID
from {{ ref('Orders_fact') }}
where revenue<0