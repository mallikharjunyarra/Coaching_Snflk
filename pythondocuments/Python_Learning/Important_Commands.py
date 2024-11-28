python -m venv myenv
myenv/Scripts/activate

pip freeze--To know what are the packages are installed
dbt init--> Initialize the configuration details
dbt debug--> To check the connection is working as expected 

dbr run -module module_name

import snowflake.connector
import pandas as pd

# Establish a connection to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account_identifier',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema',
    role='your_role'  # Optional, based on your permissions
)

# Create a cursor object to interact with Snowflake
cur = conn.cursor()

# Run a query (for example, show all tables)
try:
    cur.execute("SELECT CURRENT_VERSION()")  # Example query
    result = cur.fetchone()
    print(f"Snowflake version: {result[0]}")
finally:
    cur.close()

# Close the connection
conn.close()


