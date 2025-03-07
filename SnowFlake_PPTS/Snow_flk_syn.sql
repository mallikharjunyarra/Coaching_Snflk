Why Snowflake :-
	Pay for what you use model.
	It is a cloud platform, no Infrastructure cost.
	Snowflake is more than a Datawarehouse.
	It also helps in some transformations, create data pipes, create visual dashboard etc.
	High scalability.
	Data recovery, backup, sharing, masking.
	Can analyze the data present in external files.
	Easy integration with Data Visualization/Reporting tolls.

Data Back Up (Cloning), Data Sharing (Data Sharing feature ), Data Recovery(Time Travel) , Change data capture(Streams) , scheduling (Tasks) 

Storage layer:-
		Data will be stored in columnar format
		Data will be stored in micro partitions
		Micro-partitions are small in size (50 to 500 MB).
Query processing layer :- Muscle of the snowflake it contains Warehouse . Entire query processing will be done .	On AWS they are a group of EC2 instances. Compute cost will be calculated on the basis of query execution time on virtual warehouses
		Auto resume  and autosuspend  
		Scale Up (or)Vertical Scaling
		(Increasing or decreasing the size of virtual warehouse)
		Scale Out (or)Horizontal Scaling
		(Increasing or decreasing the number of clusters
cloud service layer:-Brain of the system ..Infrastructure manager , Authentication & access control ,  metadata manager and security.
				Manages all Serverless tasks like Snowpipe, Tasks, Materialized view maintenance etc.

 ‘Virtual Warehouse’ is a cluster of one or more compute resources used to process queries and other DML operations
The size of warehouse determines the number of servers in each cluster in the warehouse.
In Snowflake, a warehouse is essentially a virtual compute resource that provides the processing power for executing SQL queries and other tasks like data loading, transformation, and unloading.  Warehouses in Snowflake are not physical servers but rather virtual clusters that dynamically allocate computing resources as needed. 

Key Concepts of Snowflake Warehouses
Compute-Only: Warehouses in Snowflake do not store data themselves; they purely provide compute resources. Data is stored in Snowflakes centralized storage layer and accessed through the warehouse.

Scalability: Warehouses can scale up (increasing their size for more compute resources) or scale out (adding more clusters of the same size) to handle varying workloads.

Multi-Cluster Support: Warehouses can be configured with multiple clusters that automatically scale based on the workload, helping manage concurrent user requests efficiently.

On-Demand Activation: Warehouses in Snowflake can be started, suspended, or resized on demand, allowing you to manage costs by only paying for compute resources when in use.

Here’s a breakdown of common sizes:

X-Small: Suitable for light workloads and development or testing.
Small: Often used for small teams or moderate workloads.
Medium: Good for regular workloads that need more consistent performance.
Large: Suitable for heavy workloads or larger data transformations.
X-Large and Above: Ideal for complex, resource-intensive workloads.

Snowflake offers two scalability options that determine how warehouses adapt to workload fluctuations:

Single-Cluster Warehouse: This is a fixed-size warehouse with a single cluster of compute resources. It processes queries sequentially and cannot handle sudden spikes in concurrent user requests as efficiently as a multi-cluster warehouse.

Multi-Cluster Warehouse: This type automatically scales out by adding clusters based on query demand, providing high concurrency. Multi-cluster warehouses are ideal for handling variable workloads with high user concurrency, as Snowflake dynamically adds or removes clusters to meet the demand.

Multi-cluster warehouses have three key configurations:

Max Clusters: Specifies the maximum number of clusters that can be started.
Min Clusters: Specifies the minimum number of clusters to keep active.
Auto-Suspend/Auto-Resume: Allows warehouses to automatically suspend when idle and resume when activity resumes.

Summary:-In Snowflake, warehouses provide the compute power for processing queries and can be tailored to suit specific workloads by adjusting size and scalability mode. They provide flexibility and cost management by allowing on-demand activation, automatic suspension, and scaling options.

XS-1, Small--> 2, medium-->4  L-> 8 X-->16 2X-->32 3X-->64  4x-->128 5X 6X
Scalling polocy (Standard and Economy)
	In Snowflake, scaling policies determine how virtual warehouses (compute resources) handle changes in workloads. Snowflake offers two primary scaling policies: Standard and Economy. These policies control how quickly the virtual warehouse will scale up to accommodate more queries and how it scales down when demand decreases.

XS  to 6xl 
Multi cluster --> Minimum cluser(1) and maximum clusters(10)

CREATE TABLE MY_TABLE (type number, name string,country string,date date) CLUSTER BY (name);

Modifying Cluster keys on existing table: ALTER   TABLE MY_TABLE   CLUSTER BY (name, date);

Snowflake supports and combines both of below access control models.
Discretionary Access Control (DAC): Each object has an owner, who can in turn grant access to that object.
Role-based Access Control (RBAC): Access privileges are assigned to roles, which are in turn assigned to users.

Accountadmin
ORGADMIN
Securityadmin
useradmin
sysadmin
public 

Standard Edition
Enterprise Edition
Business Critical Edition
Virtual Private Snowflake(VPS)

Create the S3 bucket folders in AWS and create the Role from the intergrated account management(Create Role) for the created bucket and note down the ARN of IAM.

CREATE STORAGE INTEGRATION my_s3_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'S3'
STORAGE_AWS_ROLE_ARN = '<aws_role_arn>'--Amazon Resouce Name
ENABLED = TRUE
STORAGE_ALLOWED_LOCATIONS = ('s3://bucket_name/folder/');

// Get external_id(AWS_IAM_USER_ARN) and update it in S3
DESC integration s3_int;

CREATE OR REPLACE STORAGE INTEGRATION S3_INT
	TYPE=EXTERNAL_STAGE
	STORAGE_PROVIDER='S3'
	STORAGE_AWS_ROLE_ARN='arn:aws:iam::253490765544:role/awss3mallik'
	--STORAGE_AWS_EXTERNAL_ID='YA20331_SFCRole=3_W/U6AxdV2RQ7K6MdrK1+nakEnTI='
	ENABLED=true
	STORAGE_ALLOWED_LOCATIONS=('s3://awss3mallik/csv/', 's3://awss3mallik/json/', 's3://awss3mallik/xml/', 's3://awss3mallik/pipes/', 's3://awss3mallik/output/','s3://awss3mallik/parquet/')
	COMMENT='Integration with aws s3 buckets';


CREATE [ OR REPLACE ] STAGE stage_name
  URL = 's3://bucket_name/path/'
  STORAGE_INTEGRATION = storage_integration_name
  [ CREDENTIALS = (AWS_KEY_ID = 'aws_key' AWS_SECRET_KEY = 'aws_secret') ]
  [ FILE_FORMAT = ( { FORMAT_NAME = 'format_name' | TYPE = format_type } ) ]
  [ COPY_OPTIONS = ( ON_ERROR = 'error_behavior' ) ]
  [ COMMENT = 'stage_comment' ];

CREATE OR REPLACE STAGE my_parquet_stage
  URL = 's3://awss3mallik/parquet/'
  STORAGE_INTEGRATION = 'S3_INT'
  FILE_FORMAT = (TYPE = 'PARQUET');

 
CREATE OR REPLACE file format mydb.file_formats.csv_fileformat
    type = csv
    field_delimiter = ','
    skip_header = 1
    empty_field_as_null = TRUE;
  
CREATE OR REPLACE STAGE MYDB.EXT_STAGES.MYS3_STAGE
    URL = 's3://awss3bucketjana/csv/'
    STORAGE_INTEGRATION = s3_int
    FILE_FORMAT = MYDB.FILE_FORMATS.CSV_FILEFORMAT ;


Copy Command :-
COPY INTO TABLENAME
	FROM @STAGE
	file_format= (…)--CSV,JSON,XML,parquet,avro,ORC
	files = (filename1, filename2 …)
	(or)
	pattern = ‘.*filepattern.*’ 
	other_optional_props ;
VALIDATION_MODE  RETURN_n_ROWS|RETURN_ERRORS|RETURN_ALL_ERRORS
	RETURN_ALL_ERRORS:
		This mode scans all specified data files and returns a detailed list of all errors found.
		It doesn't load any data into the table, so it's purely for validation purposes.
	RETURN_ERRORS_LIMIT:
		This mode scans the data files and returns a list of errors up to a specified limit. It allows you to see the first set of issues without scanning the entire dataset.You specify the limit using a number.
	RETURN_SAMPLE_ERRORS:
		This mode scans the data files and returns a sample of errors without going through all the files. It's a faster way to identify issues because it doesn't check everything.
	
RETURN_FAILED_ONLY (TRUE | FALSE ) 
ON_ERROR (CONTINUE | SKIP_FILE | SKIP_FILE_num |SKIP_FILE_num% | ABORT_STATEMENT) 
            CONTINUE: Continue loading and skip error records.
			SKIP_FILE: Skip the entire file if errors are found.
			ABORT_STATEMENT: Stop the load if errors are found
	
FORCE = ( TRUE | FALSE ) Force: Reload files that have already been loaded.
SIZE_LIMIT    TRUNCATECOLUMNS (TRUE | FALSE ) ENFORCE_LENGTH  PURGE (TRUE | FALSE) LOAD_UNCERTAIN_FILES

Cache:-
	Cache is a temporary storage location that stores copies of files or data, so that they can be accessed faster in near future.
	Cache plays vital role in saving costs and speeding up results.Improves query performance.
	
	Query Result CACHE(Cloud service layer)--> 24 hours  This query can be used by any other user from other ware houses also .But query should be same.
	Local disk Cache(VM Layer) --> Until VW is UP and running.Can change the query 


SnowPipe:-
	Snowpipe is a continuous data ingestion service in Snowflake that allows you to automatically load data from files as soon as they arrive in a specified stage (like AWS S3, Azure Blob Storage, or Google Cloud Storage). Unlike the COPY INTO command, which is typically run manually or on a schedule, Snowpipe listens for new files and loads them in near real-time, making it ideal for continuous or streaming data ingestion.
	Create Storage Integration object
	Create a Stage object using storage integration object.
	Create and test Copy command to load the data.
	Create a Pipe by using the Copy command.
	Setup event notifications at Cloud storage provider’s end.
	Desc Pipe pipe_name ; notification channel  column
	
	SELECT * FROM TABLE( INFORMATION_SCHEMA.COPY_HISTORY
		(table_name  =>  'table_name',		 START_TIME =>  'timestamp or expression')	);
SELECT * FROM TABLE(INFORMATION_SCHEMA.COPY_HISTORY(table_name  => 'emp.stagging.json_stag',start_time  => dateadd(hour, -24, current_timestamp)));

	SELECT * FROM TABLE(INFORMATION_SCHEMA.VALIDATE_PIPE_LOAD
	(PIPE_NAME => ‘pipe_name’,     START_TIME => ‘timestamp or expression’);

	lastReceivedMessageTimestamp:
	 Specifies the timestamp of the last event message received from the message queue.
	 If the timestamp is earlier than expected, this indicates an issue with the service configuration (i.e. Amazon SQS) .
	Verify whether any settings were changed in your service configuration.

	lastForwardedMessageTimestamp:
	 Specifies the timestamp of the last “create object” event message that was forwarded to the pipe.
	 If this value is not similar to above timestamp, then there is a mismatch between the cloud storage path where the new data files are created and the path specified in the Snowflake stage object.
	 Verify the paths and correct them.
	
// Create a pipe
CREATE OR REPLACE pipe mydb.pipes.employee_pipe
AUTO_INGEST = TRUE
AS
COPY INTO mydb.public.emp_data
FROM @mydb.external_stages.stage_aws_pipes
pattern = '.*employee.*';	
	
//Listing files under my s3 bucket
LIST @MYDB.EXT_STAGES.MYS3_STAGE;

--------------------------
Zero copy cloning :-
In Snowflake, zero-copy cloning allows users to create a copy of a database, schema, or table without duplicating the underlying data. Instead of physically copying the data, Snowflake creates a metadata clone that points to the same data files, making the process efficient and fast. The main benefits and uses of zero-copy cloning in Snowflake are:
1. Environment Duplication 2. Backup and Recovery  3. Data Sharing and Experimentation  4. Cost Efficiency  5. Testing Schema Changes 6. Historical Analysis.
Here Clone object type can be
(Data storage Objects) Database Schema Table  Stream 
(Data Configuration objects)Stage File Format Task 

CREATE OR REPLACE TABLE mydb.PUBLIC.customer_tt_clone
CLONE mydb.public.customer at (OFFSET => -60*5);

//Dynamic Tables 
create dynamic table dyn_tab_emp
 TARGET_LAG =  '1 minutes' 
  WAREHOUSE = COMPUTE_WH
AS select e.ename,d.dname from emp e inner join dept d on e.deptno=d.deptno;

//Create External Tables
	Snowflake External 	tables allow you to query the files stored in external stage like a regular table, that means without moving that data from files to Snowflake tables.External tables access the files stored in external stage area such as Amazon S3, GCP bucket, or Azure blob storage.
	External tables store metadata about these data files, such as value(complete record), the filename and file row number.
	External tables are read-only, therefore no DML operations can be performed on them.
	But we can use external tables for query and join operations.
	Views and Materialized views can be created against external tables.
	Querying data from external tables is likely slower than querying database tables.
	Advantage of external table is you can analyze the data with out storing it in Snowflake.
	
	External tables store below metadata information.
	VALUE: A VARIANT type column that represents a single row in the external file.
	METADATA$FILENAME: A pseudocolumn that identifies the name of each staged data file included in the external table, including its path in the stage.
	METADATA$FILE_ROW_NUMBER: A pseudocolumn that shows the row number for each record in a staged data file.
	
	For creating External tables,
		Create file format object
		Create stage object referring to cloud storage location.
		Create the External table.

CREATE OR REPLACE EXTERNAL TABLE EXT_TABLES.ET_S3_CUSTOMER(
 CUST_ID NUMBER AS (value:c1::NUMBER),
 CUSTNAME VARCHAR AS (value:c2::VARCHAR),
 EMAIL VARCHAR AS (value:c3::VARCHAR),
 CITY VARCHAR AS (value:c4::VARCHAR),
 STATE VARCHAR AS (value:c5::VARCHAR),
 DOB DATE AS TO_DATE(value:c6::VARCHAR,'YYYY-MM-DD')
)
WITH 
LOCATION = @MYDB.EXT_STAGES.MYS3_STAGE
PATTERN = '.*customer.*'
FILE_FORMAT = MYDB.FILE_FORMATS.CSV_FILEFORMAT;

// Create a stream 

	A stream object records DML changes made to tables including inserts, updates, and deletes.
	Also Stream stores metadata about each change, so that actions can be taken using this metadata.
	We call this process as change data capture (CDC). 
	Streams tracks all row level changes to a source table using offset but doesnt store the changed data.
	Once these changes are consumed by the Target table, this offset moves to the next point.
	Streams can be combined with tasks to set continuous data pipelines.
	Snowpipe + Stream + Task Continuous Data Load.
	
	Along with the changes made to the source table, Streams maintain 3 metadata fields.
		1. METADATA$ACTION: Indicates the DML operation (INSERT, DELETE) recorded.
		2. METADATA$ISUPDATE: Indicates whether the operation was part of an UPDATE statement. Updates to rows in the source object are represented as a pair of DELETE and INSERT records in the stream with a metadata column METADATA$ISUPDATE values set to TRUE.
		3. METADATA$ROW_ID: Specifies the unique and immutable ID for the row, which can be used to track changes to specific rows over time.
	We use merge statement for consuming the changes from stream and applying the same on Target tables.
		// To identify Insert records
		WHERE metadata$action = 'INSERT' AND metadata$isupdate = 'FALSE';
		// To identify Update records
		WHERE metadata$action = 'INSERT' AND metadata$isupdate = 'TRUE';
		To identify Delete records
		WHERE metadata$action = 'DELETE' AND metadata$isupdate = 'FALSE';

		Note: If we want to consume these changes to multiple tables then we have to create multiple streams.

CREATE STREAM MYSTREAMS.STREAM_EMPL ON TABLE STAGE_TBLS.STG_EMPL;

1. Standard Streams: A Standard stream tracks all DML changes to the source object, including inserts, updates, and deletes (including table truncates).
	CREATE OR REPLACE STREAM my_stream ON TABLE my_table;
2. Append-only Streams: An Append-only stream tracks row inserts only. Update and delete operations (including table truncates) are not recorded.
	CREATE OR REPLACE STREAM my_stream ON TABLE my_table	APPEND_ONLY = TRUE; 
3. Insert-only Streams: Supported for External tables only. An insert-only stream tracks row inserts only. They do not record delete operations.
	CREATE OR REPLACE STREAM my_stream ON EXTERNAL TABLE my_table INSERT_ONLY = TRUE;

MERGE INTO INTG_TBLS.EMPL T
USING MYSTREAMS.STREAM_EMPL S
	ON T.EMPID = S.EMPID
WHEN MATCHED                        -- DELETE condition
    AND S.METADATA$ACTION ='DELETE' 
    AND S.METADATA$ISUPDATE = 'FALSE'
    THEN DELETE                   
WHEN MATCHED                        -- UPDATE condition
    AND S.METADATA$ACTION ='INSERT' 
    AND S.METADATA$ISUPDATE  = 'TRUE'       
    THEN UPDATE 
    SET T.EMPNAME = S.EMPNAME,
		T.SALARY = S.SALARY,
		T.AGE = S.AGE,
		T.DEPT = S.DEPT,
		T.LOCATION = S.LOCATION,
		T.LST_UPDT_DT = CURRENT_DATE
WHEN NOT MATCHED 					-- INSERT records
    AND S.METADATA$ACTION ='INSERT'
	AND S.METADATA$ISUPDATE  = 'FALSE'
    THEN INSERT( EMPID, EMPNAME, SALARY, AGE, DEPT, LOCATION, INSRT_DT, LST_UPDT_DT)
	VALUES(S.EMPID, S.EMPNAME, S.SALARY, S.AGE, S.DEPT, S.LOCATION, CURRENT_DATE, NULL);
	
{% macro to_uppercase(string) %}
    upper('{{ string }}')
{% endmacro %}

SELECT {{ to_uppercase('hello world') }} AS upper_text;


	
CDC Type 1 ,2 and 3 :-
CDC Type	Historical Tracking| Storage|Use Case
Type 1	No history, overwrites data|Low|Current state is all that matters (e.g., contact info)
Type 2	Full history with multiple rows	|High|Full historical tracking (e.g., price changes over time)
Type 3	Limited history with previous/current	|Medium|Track recent changes, but no need for full history


Task:-
	We use tasks for scheduling in Snowflake.
	We can schedule 1.	SQL queries 2.	Stored procedures
	Tasks can be combined with streams for implementing the continuous change data captures(CDC).
	We can maintain a DAG of tasks to keep the dependencies between tasks.
	Tasks require compute resources to execute SQL code, we can choose either of snowflake managed compute resources(Serverless)
	User managed (Virtual warehouses)
	By using CREATE TASK Command we can create tasks.

	CREATE OR REPLACE TASK task_name
		WAREHOUSE = ‘warehouse name’
		SCHEDULE = ‘Time or Cron’
		AFTER dep_task_name
	AS 	SQL Statement;
	SQL Statement can be a query or a call to stored procedure.

	CREATE OR REPLACE TASK MYTASKS.TASK_TRACK_TIME
		WAREHOUSE = MYOWN_WH
		SCHEDULE = '1 MINUTE'
	AS  INSERT INTO MYDB.PUBLIC.TRACK_LOAD_TIME(LOAD_TIME) 
		VALUES(CURRENT_TIMESTAMP);
		
	ALTER TASK MYTASKS.TASK_TRACK_TIME RESUME;

	// Using Cron to load the data for every minute
	CREATE OR REPLACE TASK MYTASKS.TASK_TRACK_TIME2
		WAREHOUSE = COMPUTE_WH
		SCHEDULE = 'USING CRON * * * * * UTC'  --minute  hour day  month  Day of the week Time Zone 
	AS INSERT INTO MYDB.PUBLIC.TRACK_LOAD_TIME(NAME,LOAD_TIME) 
		VALUES('DONALD', CURRENT_TIMESTAMP);
		
	ALTER TASK MYTASKS.TASK_TRACK_TIME2 RESUME;
	DAG(Directed Acyclic Grap) of Tasks

	We can check task history from information schema table TASK_HISTORY.
	// To see all tasks history with last executed task first
	select  *   from table(information_schema.task_history()) order by scheduled_time desc;  
	  
	If your task is not running as per schedule, check below things..
	Step 1: Verify the Task status, it should be like ‘started’, if it is in ‘suspended’ state, resume it by using alter command.
	Step 2: Check the Task history and check execution state, if it is in ‘failed’ state, take the query id and check the failure reason.
	Step 3: Verify the Permissions Granted to the Task Owner, Owner should have access to database, schema, tables and warehouses.
	Step 4: Verify the Condition (Only for Streams): check SYSTEM$STREAM_HAS_DATA  , stream may not have data changes to process.

Stages:-
	A stage specifies where data files are stored (i.e. “staged”) so that the data in the files can be loaded into a table.
	Stage is a location of files, that can be internal or external to snowflake
	External Stages:-
		An external stage is the external cloud storage location where data files are stored.Loading data from any of the following cloud storage services is supported regardless of the cloud platform that hosts your Snowflake account:
		Amazon S3 |	Google Cloud Storage|Microsoft Azure
	Internal Stages
		User Internal Stage (@~):- A user stage is allocated to each user for storing files. To store files that are staged and managed by a single     user but can be loaded into multiple tables. User stages cannot be altered or dropped.This option is not appropriate if multiple users     require access to the files.
		Table Internal Stage (@%):- A table stage is available for each table created in Snowflake. Table stages have the same name as the table. 
		   e.g. a table named mytable has a stage referenced as @%mytable ,To store files that are staged and managed by one or more users but only loaded into a single table. Table stages cannot be altered or dropped.Note that a table stage is not a separate database object, rather it is an implicit stage tied to the table itself.
		Named Internal Stage(@):-
		    A named internal stage is a database object created in a schema.To store files that are staged and managed by one or more users and loaded into one or more tables. Create stages using the CREATE STAGE command (similar to external stages)
		   CREATE OR REPLACE STAGE MYDB.internal_stages.sample_stage

	CREATE OR REPLACE STAGE mydb.internal_stages.named_customer_stage;
	list @~/staged;
	list @%customer_data_table;
	list @mydb.internal_stages.named_customer_stage;

	put file://C:\Users\janar\OneDrive\Documents\Files\pets_data.json @~/staged;
	put file://C:\Users\janar\OneDrive\Documents\Files\pets_data.json @%pets_data;
	put file://C:\Users\janar\OneDrive\Documents\Files\customer_data_table.csv @%customer_data_table;
	put file://C:\Users\ymallikharjun\Desktop\Mallik_docs\SnowFlake\Practice\Semi_structured_data\pets_data.json @mallik
	
	put file://C:\Users\ymallikharjun\Downloads\01_customer_data_10k.csv @~/ch09

GET Command:-Purpose: Downloads files from a stage to a local directory. 
This command is useful for retrieving data staged in Snowflake to use on a local system. Syntax: GET @stage_name/path/to/file 'file://local/directory/';

REMOVE Command:-Purpose: Deletes files from a Snowflake stage (both internal and external).
Syntax:  REMOVE @stage_name/path/to/file;   REMOVE @my_stage/data/myfile.csv;

Masking Policy:-
	Column-level Security in Snowflake allows the application of a masking policy to a column within a table or view.
	To protect sensitive data like customers PHI, bank balance info etc.
	Column-level Security includes two features:
	Dynamic Data Masking
	External Tokenization
	Dynamic Data Masking  is the process of hiding data by masking with other characters. We can create masking policies to hide the data present in columns.
	Tokenization is the process of hiding sensitive data by replacing it with cypher text. External Tokenization makes use of masking policies with external functions created at external cloud provider side.
	
	Snowflake supports masking policies to protect sensitive data from unauthorized access while allowing authorized users to access at query runtime. 	Masking policies are schema level objects.	Masking policies can include conditions and functions to transform the data when those conditions are met.	Same masking policy can be applied on multiple columns.


	CREATE OR REPLACE MASKING POLICY customer_phone 
		as (val string) returns string->
	CASE WHEN CURRENT_ROLE() in ('SALES_ADMIN', 'MARKET_ADMIN') THEN val
		ELSE '##-###-###-'||SUBSTRING(val,12,4) 
		END;
		
	// Apply masking policies on columns of CUSTOMER table
	ALTER TABLE PUBLIC.CUSTOMER MODIFY COLUMN C_PHONE
		SET MASKING POLICY customer_phone;
		
	// Unsetting or removing Masking Policy
	ALTER TABLE public.employee 
		MODIFY COLUMN ssn UNSET MASKING POLICY;
		
tags will be used to do the dynamic masking.
		
Cost:-
1.Storage cost   On demand(40$/TB one month) and fixed cost (29$ /1 TB for month)
2.Compute cost 
3.Cloud service Cost  SnowPipe , Meteraialized views  and Tasks 


Time Travel:-
	Snowflake Time Travel enables accessing historical data (i.e. data that has been changed or deleted) at any point within a defined period.
	Restoring data-related objects (tables, schemas, and databases) that might have been accidentally or intentionally deleted.
	Query data in the past that has since been updated or deleted. Duplicating and backing up data from key points in the past.
	Analyzing data usage/manipulation over specified periods of time.No need to enable Time Travel, it is automatically enabled.
	
	Retention is the key component of Time Travel.
	It specifies the number of days for which this historical data is preserved.
	For Standard Edition, the retention period is 1 day, can set it to 0.
	For Enterprise and higher editions it is 90 days, can set it any thing between 0-90 days.
	Default is 1, we can set this period at the time of creation of object or can alter later.
	A retention period of 0 days for any object means disabling Time Travel for the object.
	We can change the retention period by using ALTER command.	Higher retention period, the higher storage cost.
	
	3 Ways to query historical data
		At specified timestamp
		At some time ago
		Before executing any statement/query
		
	1. Below query selects historical data from a table at the specified timestamp:
	select * from my_table at(timestamp => 'Fri, 01 May 2015 16:20:00 -0700'::timestamp_tz);
	2. Below query selects historical data from a table as of 5 minutes ago:
	select * from my_table at(offset => -60*5);
	3. Below query selects historical data that present in the table before executing the query specified by query id
	select * from my_table before(statement => '8e5d0ca9-005e-44e6-b858-a8f5b37c5726');
	
	When a table, schema, or database is dropped, it is not immediately removed from the system. Instead, it is retained for the data retention period for the object, during which time the object can be restored. After retention period is completed, we can’t restore the objects.

	UNDROP TABLE 'TABLE_NAME'
	UNDROP SCHEMA 'SCHEMA_NAME'
	UNDROP DATABASE 'DATABASE_NAME'
	Fail Safe:-
		Fail-safe provides a 7-day period during which historical data may be recoverable by Snowflake.
		This period starts immediately after the Time Travel retention period ends. 
		We cant query or restore the Fail-safe data.We need to contact Snowflake Support to restore the data during Fail-safe period.
		Data recovery through Fail-safe may take several hours to several days to complete.After Fail-safe period is over, there is no other way to recover the data.

	Time Travel:-(0-90 days ), Fail safe 7 days
	CREATE OR REPLACE TABLE mydb.abcxyz.timetravel_ex2(id number, name string) DATA_RETENTION_TIME_IN_DAYS = 20;
	SHOW TABLES like 'timetravel_ex2%';

	ALTER TABLE mydb.public.timetravel_ex 
	SET DATA_RETENTION_TIME_IN_DAYS = 15;

	COPY INTO @MYDB.EXT_STAGES.MYS3_OUTPUT
	FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER;

	create or replace resource monitor MONITOR1 with credit_quota=500
	  triggers on 100 percent do suspend;

	alter warehouse SAMPLE_WH set resource_monitor = MONITOR1;
	----------------------------------------------------

	Example2: To create a monitor that is similar to the above example, but suspends at 90% and suspends immediately at 100% to prevent all warehouses in the account from consuming credits after the quota has been reached:

	create or replace resource monitor MONITOR2 with credit_quota=1000
	  triggers on 90 percent do suspend
			   on 100 percent do suspend_immediate;
		   
// Bernoulli or Row
CREATE TABLE CUST_SAMPLE_1 AS
SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.CUSTOMER
    SAMPLE (10);
	
// System or Block    
CREATE TABLE CUST_SAMPLE_3 AS
SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF10.CUSTOMER
    SAMPLE BLOCK (5);


-- switch back to admin role and grant access
USE ROLE sales_admin;
GRANT USAGE ON DATABASE sales_db TO ROLE sales_users;
GRANT USAGE ON SCHEMA sales_db.public TO ROLE sales_users;
GRANT SELECT ON TABLE sales_db.public.CUSTOMERS TO ROLE sales_users;

Important Queries and functions in snowflake 

EXECUTE AS CALLER
Definition: When a procedure is defined with EXECUTE AS CALLER, it means that the procedure will run with the privileges of the role that is invoking the procedure, rather than the privileges of the role that owns or created the procedure.

   INSERT INTO MYOWN_DB.INTG_TBLS.PETS_DATA
select  
       raw_file:Name::string as Name,
       raw_file:Gender::string as Gender,
       raw_file:DOB::date as DOB,
       f1.value::string as Pet,
       raw_file:Address."House Number"::string as House_No,
	   raw_file:Address.City::string as City,
	   raw_file:Address.State::string as State,
	   raw_file:Phone.Work::number as Work_Phone,
	   raw_file:Phone.Mobile::number as Mobile_Phone
FROM MYOWN_DB.STAGE_TBLS.PETS_DATA_JSON_RAW, 
table(flatten(raw_file:Pets)) f1;

In Snowflake, the FLATTEN function is used to work with semi-structured data stored in JSON, XML, or ARRAY formats. It takes a nested structure and returns a table-like result by expanding (or "flattening") the elements of an array or object. This is particularly useful for querying nested data.

select * from @AWS_S3_PARQUET/cities.parquet;

SELECT
    EMPNO,
    DEPTNO,
    SAL,
    RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) AS salary_rank
FROM emp.stagging.emp QUALIFY salary_rank=1;