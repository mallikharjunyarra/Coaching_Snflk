-- Create a work table in all environments
CREATE TABLE DEV_EMP.WORK.MIGRATE_VIEWS(VIEW_NAME VARCHAR(50));
CREATE TABLE TEST_EMP.WORK.MIGRATE_VIEWS(VIEW_NAME VARCHAR(50));
CREATE TABLE PROD_EMP.WORK.MIGRATE_VIEWS(VIEW_NAME VARCHAR(50));

-- Create a XW table among environments 
CREATE OR REPLACE TABLE DEV_EMP.WORK.XW_ENV_DATABASES(SRC_ENV_DB VARCHAR(50), TGT_ENV_DB VARCHAR(50));
INSERT INTO DEV_EMP.WORK.XW_ENV_DATABASES VALUES ('TEST_EMP', 'DEV_EMP');

CREATE OR REPLACE TABLE TEST_EMP.WORK.XW_ENV_DATABASES(SRC_ENV_DB VARCHAR(50), TGT_ENV_DB VARCHAR(50));
INSERT INTO TEST_EMP.WORK.XW_ENV_DATABASES VALUES ('DEV_EMP', 'TEST_EMP');

CREATE OR REPLACE TABLE PROD_EMP.WORK.XW_ENV_DATABASES(SRC_ENV_DB VARCHAR(50), TGT_ENV_DB VARCHAR(50));
INSERT INTO PROD_EMP.WORK.XW_ENV_DATABASES VALUES ('TEST_EMP', 'PROD_EMP');

/*
CREATE OR REPLACE VIEW DEV_EMP.HRDATA.VIEW_NAME
AS 
SELECT t1.col1, t1.col2, t2.col1, t3.col3
FROM DEV_DB1.HRDATA.EMPL t1 
JOIN DEV_DB2.HRDATA.DEPT t2
on t1.col1=t2.col1
JOIN DEV_DB3.HRADATA.LOC t3
ON t1.col2=t3.col2;
*/

/* 
INSERT INTO TEST_EMP.WORK.XW_ENV_DATABASES VALUES ('DEV_DB1', 'TEST_DB1');
INSERT INTO TEST_EMP.WORK.XW_ENV_DATABASES VALUES ('DEV_DB2', 'TEST_DB2');
INSERT INTO TEST_EMP.WORK.XW_ENV_DATABASES VALUES ('DEV_DB3', 'TEST_DB3');
INSERT INTO TEST_EMP.WORK.XW_ENV_DATABASES VALUES ('DEV_EMP', 'TEST_EMP');
*/

/* 
INSERT INTO PROD_EMP.WORK.XW_ENV_DATABASES VALUES ('TEST_DB1', 'PROD_DB1');
INSERT INTO PROD_EMP.WORK.XW_ENV_DATABASES VALUES ('TEST_DB2', 'PROD_DB2');
INSERT INTO PROD_EMP.WORK.XW_ENV_DATABASES VALUES ('TEST_DB3', 'PROD_DB3');
INSERT INTO PROD_EMP.WORK.XW_ENV_DATABASES VALUES ('TEST_EMP', 'PROD_EMP');
*/

---------------------

-- Creating some views
-- 1. Create a view with details of employees working in 'IT' department
CREATE OR REPLACE VIEW dev_emp.hrdata.v_employees_it_dept
AS 
SELECT emp.*, dept.department_name
FROM dev_emp.hrdata.employees emp 
JOIN dev_emp.hrdata.departments dept
ON emp.dept_id = dept.dept_id
WHERE dept.department_name LIKE 'IT'
;

-- 2. Create a view with the details of employees working in 'Europe' region
CREATE OR REPLACE VIEW dev_emp.hrdata.v_employees_europe
AS
SELECT emp.employee_id, emp.first_name, emp.salary, emp.hire_date, 
dept.department_name, cnt.country_name, reg.region_name
FROM dev_emp.hrdata.employees emp 
JOIN dev_emp.hrdata.departments dept
ON emp.dept_id = dept.dept_id
JOIN dev_emp.hrdata.locations loc
ON dept.location_id = loc.location_id
JOIN dev_emp.hrdata.countries cnt
ON loc.country_id = cnt.country_id
JOIN dev_emp.hrdata.regions reg
ON cnt.region_id = reg.region_id
WHERE reg.region_name = 'Europe'
;

-- 3. Create a view for top 3 salaried employees and their salaries
CREATE OR REPLACE VIEW dev_emp.hrdata.v_top3_salaried_employees
AS
SELECT employee_id, first_name, last_name, salary FROM 
( SELECT *, DENSE_RANK() OVER(ORDER BY salary DESC) as rank
  FROM dev_emp.hrdata.employees
) WHERE rank <= 3
;

-- 4. Create a view with dept wise number of employees hired in the year 1997
CREATE OR REPLACE VIEW dev_emp.hrdata.v_dept_wise_emp_hired
AS
SELECT dept.department_name, count(*) as no_emp_hired
FROM dev_emp.hrdata.employees emp 
JOIN dev_emp.hrdata.departments dept
ON emp.dept_id = dept.dept_id
WHERE YEAR(hire_date) = 1997
--WHERE YEAR(hire_date) = YEAR(CURRENT_DATE)
GROUP BY dept.department_name
;

-- 5. Create a view with the number of direct employees working under all managers
CREATE OR REPLACE VIEW dev_emp.hrdata.v_direct_reportees_count
AS
SELECT emp.manager_id, mgr.first_name||' '||mgr.last_name as mgr_name, COUNT(*) as reportees_count
FROM dev_emp.hrdata.employees emp
JOIN dev_emp.hrdata.employees mgr
ON emp.manager_id = mgr.employee_id
GROUP BY emp.manager_id, mgr_name
;

-- 6. Create a view with complete employee details.
CREATE OR REPLACE VIEW dev_emp.hrdata.v_employee_details
AS
SELECT
emp.employee_id, emp.first_name||' '||emp.last_name as emp_name, emp.salary, 
emp.hire_date, emp.email, emp.phone_number, mgr.first_name||' '||mgr.last_name as mgr_name,
dept.department_name, loc.street_address, loc.postal_code, loc.city, loc.state_province as state,
cnt.country_name as country, reg.region_name as region, job.job_title

FROM dev_emp.hrdata.employees emp

LEFT OUTER JOIN dev_emp.hrdata.employees mgr
ON emp.manager_id = mgr.employee_id

LEFT OUTER JOIN dev_emp.hrdata.departments dept
ON emp.dept_id = dept.dept_id

LEFT OUTER JOIN dev_emp.hrdata.locations loc
ON dept.location_id = loc.location_id

LEFT OUTER JOIN dev_emp.hrdata.countries cnt
ON loc.country_id = cnt.country_id

LEFT OUTER JOIN dev_emp.hrdata.regions reg
ON cnt.region_id = reg.region_id

LEFT OUTER JOIN dev_emp.hrdata.jobs job
ON emp.job_id = job.job_id
;