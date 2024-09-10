show integrations;
desc storage integration S3_INT;
show stages on emp;
desc stage emp.external_stages.AWS_S3_CSV ;
list @emp.external_stages.aws_s3_csv;
select $1,$2,$3,$4 from @emp.external_stages.aws_s3_csv/customer_data_2020.csv;
show file formats in database  emp;
select * from information_schema.FILE_FORMATS;
select get_ddl('FILE_FORMAT','CSV_FILEFORMAT');
select get_ddl('INTEGRATION','S3_INT');
desc  stage emp.external_stages.AWS_S3_CSV;
copy into @emp.external_stages.AWS_S3_CSV/mallik.csv
from emp.hrdata.countries
file_format=EMP.FILE_FORMATS.CSV_FILEFORMAT;
select $1,$2 from @emp.external_stages.AWS_S3_CSV/mallik.csv;
desc storage INTEGRATION S3_INT;
CREATE OR REPLACE STORAGE INTEGRATION S3_INT
	TYPE=EXTERNAL_STAGE
	STORAGE_PROVIDER='S3'
	STORAGE_AWS_ROLE_ARN='arn:aws:iam::637423531964:role/aws_s3_snoflake_intg'
	STORAGE_AWS_EXTERNAL_ID='VJ94291_SFCRole=2_7AYospMCx5q9A/JK+u0RZu7r7jQ='
	ENABLED=true
	STORAGE_ALLOWED_LOCATIONS=('s3://awss3mallik/csv/', 's3://awss3mallik/json/', 's3://awss3mallik/xml/', 's3://awss3mallik/pipes/', 's3://awss3mallik/output/')
	COMMENT='Integration with aws s3 buckets';

show file formats from  emp;
use database emp;
SHOW FILE FORMATS;

create or replace FILE FORMAT emp.file_formats.json_fileformat
type=json;
create or replace  stage emp.external_stages.AWS_S3_json
url='s3://awss3mallik/json/'
STORAGE_INTEGRATION=s3_int;
list @emp.external_stages.AWS_S3_json;
select get_ddl('STAGE','external_stages.AWS_S3_CSV');
desc stage EMP.EXTERNAL_STAGES.AWS_S3_CSV;
-- Get the DDL for a specific external stage
SELECT GET_DDL('STAGE', 'EMP.EXTERNAL_STAGES.AWS_S3_CSV');

create or replace table EMP.STAGING.PETS_STG
(json_val variant);
copy into EMP.STAGING.PETS_STG
from @emp.external_stages.AWS_S3_json
FILES=('pets_data.json')
file_format=emp.file_formats.json_fileformat
FORCE=TRUE;
list @emp.external_stages.AWS_S3_json.pet_data.json;

copy into EMP.STAGING.PETS_STG
from @~
FILES=('pets_data.json.gz')
file_format=emp.file_formats.json_fileformat
FORCE=TRUE;

create or replace table emp.public.pets_data (column1 variant);
drop table emp.public.pets_data;

list @%pets_data;

copy into EMP.PUBLIC.PETS_data
from @mallik
FILES=('pets_data.json.gz')
file_format=emp.file_formats.json_fileformat
FORCE=TRUE;

select * from EMP.PUBLIC.PETS_data;

create or replace stage emp.public.mallik;



select JSON_VAL:Address.City::string city,
JSON_VAL:Address."House Number"::string "House Number",
JSON_VAL:Address."State"::string State,
JSON_VAL:DOB::DATE DOB,
JSON_VAL:Gender::string Gender,
JSON_VAL:Pets[0]::string pets,
JSON_VAL:Pets[1]::string pets,
JSON_VAL:Phone."Mobile"::string Mobile,
JSON_VAL:Phone."Work"::string Work,
a.* from EMP.STAGING.PETS_STG a;
select JSON_VAL:Address.City::string city,
JSON_VAL:Address."House Number"::string "House Number",
JSON_VAL:Address."State"::string State,
JSON_VAL:DOB::DATE DOB,
JSON_VAL:Gender::string Gender,
f.value::string pets,
JSON_VAL:Phone."Mobile"::string Mobile,
JSON_VAL:Phone."Work"::string Work from EMP.STAGING.PETS_STG a,
--LATERAL FLATTEN(input => JSON_VAL:Pets) f;
TABLE(FLATTEN(JSON_VAL:Pets)) f;
DELETE from EMP.STAGING.PETS_STG;

select 1||null;

select * from CUSTOMER fetch 10 rows only;
select distinct C_NATIONKEY  from CUSTOMER;
select count(1),C_NATIONKEY  from CUSTOMER
group by C_NATIONKEY;
select min(C_NATIONKEY),MAX(C_NATIONKEY)  from CUSTOMER;
select min(C_CUSTKEY),MAX(C_CUSTKEY)  from CUSTOMER;

list @~;

create warehouse transforming

https://iz19678.ap-southeast-1.snowflakecomputing.com

STAGING
create database raw;
create database analytics;
create schema raw.mallik;
create schema analytics.mallik;

select * from information_schema.views;
use database analytics;
create schema if not exists dbt_myarra;

use schema mallik;dbt_myarra;




create table raw.mallik.customers
(
id number,
first_name varchar,
last_name varchar
);

select * from information_schema.views;
show storage integrations  database emp;
show  integrations;
show stages in database emp;
list @emp.EXTERNAL_STAGES.AWS_S3_CSV;
select $1,$2,$3,$4
from @emp.EXTERNAL_STAGES.AWS_S3_CSV/customer_data_2020.csv;


CREATE OR REPLACE EXTERNAL TABLE EMP.PUBLIC.ET_S3_CUSTOMER(
 CUST_ID NUMBER AS (value:c1::NUMBER),
 CUSTNAME VARCHAR AS (value:c2::VARCHAR),
 EMAIL VARCHAR AS (value:c3::VARCHAR),
 CITY VARCHAR AS (value:c4::VARCHAR),
 STATE VARCHAR AS (value:c5::VARCHAR),
 DOB DATE AS TO_DATE(value:c6::VARCHAR,'YYYY-MM-DD')
)
WITH 
LOCATION = @emp.EXTERNAL_STAGES.AWS_S3_CSV
PATTERN = '.*customer.*'
FILE_FORMAT = EMP.FILE_FORMATS.CSV_FILEFORMAT;

show file formats  in database emp;

select metadata$filename,a.* from EMP.PUBLIC.ET_S3_CUSTOMER a;

select to_date('09-20-2024','MM-DD-YYYY');

select EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPT_ID from employees;

