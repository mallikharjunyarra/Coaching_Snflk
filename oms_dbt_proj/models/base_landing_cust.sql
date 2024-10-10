with source as (
      select * from {{ source('landing', 'cust') }}
),
renamed as (
    select
        {{ adapter.quote("CUSTOMERID") }},
        {{ adapter.quote("FIRSTNAME") }},
        {{ adapter.quote("LASTNAME") }},
        {{ adapter.quote("EMAIL") }},
        {{ adapter.quote("PHONE") }},
        {{ adapter.quote("ADDRESS") }},
        {{ adapter.quote("CITY") }},
        {{ adapter.quote("STATE") }},
        {{ adapter.quote("ZIPCODE") }},
        {{ adapter.quote("UPDATED_AT") }}

    from source
)
select * from renamed
  