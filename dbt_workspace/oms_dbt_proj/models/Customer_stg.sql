{{ config(materialized='table') }}
SELECT
CustomerID,
FIrstName,
lastname,
Email,
Phone,
Address,
City,
State,
ZipCode,
Updated_at,
CONCAT(FirstName, ' ', LastName) AS CustomerName
FROM {{ source('landing','cust') }} 