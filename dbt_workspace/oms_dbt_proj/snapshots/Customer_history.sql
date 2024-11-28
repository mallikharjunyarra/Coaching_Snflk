{% snapshot Customer_history %}
{{
    config(
        target_schema='L3_CONSUMPTION',
        unique_key='CustomerID',
        strategy='timestamp',
        updated_at='updated_at'
        )
}}
select * from {{ source('landing','cust') }}
{% endsnapshot %}