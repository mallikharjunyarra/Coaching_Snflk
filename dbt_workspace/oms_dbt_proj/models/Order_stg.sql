{{ config(materialized='incremental' ,unique_key='ORDERID') }}
select ORDERID, ORDERDATE, CUSTOMERID, EMPLOYEEID, STOREID, STATUS, UPDATED_AT,
current_timestamp dbt_updated_at
from {{source('landing','order')}} 
{% if is_incremental() %}
where UPDATED_AT>=(select max(dbt_updated_at) from {{ this }})
{% endif %}
