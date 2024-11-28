{{ dbt_utils.deduplicate(
    relation=source('landing', 'orderitem'),
    partition_by=['ORDERID'],
    order_by=["UPDATED_AT desc"],
   )
}}