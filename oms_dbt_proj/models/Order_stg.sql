{{ config(materialized='table') }}
select ORDERID, ORDERDATE, CUSTOMERID, EMPLOYEEID, STOREID, STATUS, UPDATED_AT
from {{source('landing','order')}} 