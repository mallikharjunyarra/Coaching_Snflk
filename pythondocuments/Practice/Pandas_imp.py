 
Pandas is a powerful and popular Python library used for data manipulation and analysis. Here are some of the most commonly used functions and methods in Pandas:

1. Creating Data Structures
    pd.DataFrame(): Create a DataFrame (2D labeled data structure) from dictionaries, lists, or other collections.
    pd.Series(): Create a Series (1D labeled array) from a list, NumPy array, or dictionary.
    pd.read_csv(): Read data from a CSV file into a DataFrame.
    pd.read_excel(): Read data from an Excel file into a DataFrame.
    pd.read_sql(): Read data from a SQL database into a DataFrame.
    pd.read_json(): Read data from a JSON file into a DataFrame.
2. Viewing and Inspecting Data
    df.head(): Show the first few rows of the DataFrame.
    df.tail(): Show the last few rows of the DataFrame.
    df.info(): Get a summary of the DataFrame, including data types and non-null values.
    df.describe(): Get statistical summaries of numerical columns (mean, min, max, etc.).
    df.shape: Get the dimensions of the DataFrame (rows, columns).
    df.columns: List the column names.
    df.index: Get the row indices.
3. Selecting and Filtering Data
    df['column_name']: Select a single column as a Series.
    df[['col1', 'col2']]: Select multiple columns.
    df.iloc[]: Select rows and columns by index-based integer location.
    df.loc[]: Select rows and columns by label.
    df[df['column'] > value]: Filter rows based on condition.
    df.query('column > value'): Query data using SQL-like syntax.
4. Data Cleaning and Manipulation
    df.dropna(): Remove rows or columns with missing values.
    df.fillna(value): Fill missing values with a specified value.
    df.drop(columns=['col1', 'col2']): Drop specified columns.
    df.rename(columns={'old_name': 'new_name'}): Rename columns.
    df.astype(): Change the data type of a column.
    df.sort_values(by='column', ascending=False): Sort the DataFrame by a column.
    df.apply(function): Apply a function to each element, row, or column.
5. Aggregating and Grouping Data
    df.groupby('column'): Group data by a specific column.
    df.agg({'col1': 'mean', 'col2': 'sum'}): Perform aggregate operations on columns.
    df.mean(), df.sum(), df.count(), df.min(), df.max(): Compute aggregate functions.
    df.value_counts(): Count occurrences of unique values.
6. Merging and Joining Data
    pd.concat([df1, df2]): Concatenate DataFrames along a particular axis.
    pd.merge(df1, df2, on='key'): Merge two DataFrames on a key column(s).
    df.join(df2): Join DataFrames based on their index.
    
    df1 = pd.DataFrame({'emp_id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'score': [90, 85, 78]})

merged_df = pd.merge(df1, df2, left_on='emp_id', right_on='id', how='inner')
print(merged_df)

merged_df = pd.merge(df1, df2, on='id', how='left')
print(merged_df)

7. Exporting Data
    df.to_csv('filename.csv'): Save the DataFrame to a CSV file.
    df.to_excel('filename.xlsx'): Save the DataFrame to an Excel file.
    df.to_sql('table_name', connection): Save the DataFrame to a SQL database.
    df.to_json('filename.json'): Save the DataFrame to a JSON file.
8. Advanced Operations
    df.pivot_table(): Create a pivot table.
    df.crosstab(): Compute a cross-tabulation of two or more factors.
    df.melt(): Unpivot a DataFrame from wide format to long format.
    df.resample('M').sum(): Resample time series data (e.g., monthly).
These functions and methods cover a wide range of tasks from reading data, inspecting it, cleaning it, and analyzing it to exporting results. Familiarity with these will help you handle most data manipulation tasks using Pandas

import pandas as pd

# Example DataFrame
data = {'A': [1, 2, 2, 3, 4, 4], 'B': [5, 6, 6, 7, 8, 8]}
df = pd.DataFrame(data)

# Remove duplicates
df = df.drop_duplicates()

print(df)



import pandas as pd
merged_df = pd.merge(e, d, on='DEPARTMENT_ID', how='inner')
# Group by 'DEPTNO' and count the number of occurrences
result = merged_df.groupby('DEPARTMENT_ID').size().reset_index(name='count')
# Filter groups with count > 4 (equivalent to HAVING count(1) > 4)
result = result[result['count'] > 2]
# Display the result
print(result)

import boto3
import pandas as pd
from io import StringIO

# AWS S3 bucket and file details
bucket_name = 'your-bucket-name'
source_key = 'path/to/large-file.csv'
destination_prefix = 'path/to/split-files/'

# S3 Client
s3 = boto3.client('s3')

# Step 1: Download the large file
response = s3.get_object(Bucket=bucket_name, Key=source_key)
data = response['Body'].read().decode('utf-8')

# Step 2: Read the data into a Pandas DataFrame (use chunks if necessary)
df = pd.read_csv(StringIO(data))

# Step 3: Split into smaller files (e.g., 1000 rows per file)
chunk_size = 1000
for i, chunk in enumerate(range(0, df.shape[0], chunk_size)):
    chunk_df = df.iloc[chunk:chunk + chunk_size]
    
    # Convert chunk DataFrame to CSV
    chunk_data = chunk_df.to_csv(index=False)
    
    # Upload each chunk back to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=f"{destination_prefix}chunk_{i+1}.csv",
        Body=chunk_data
    )
    print(f"Uploaded chunk_{i+1}.csv")


import requests
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Define the API endpoint and parameters
API_URL = "https://api.example.com/data"  # Replace with the actual API URL
API_HEADERS = {
    "Authorization": "Bearer YOUR_API_TOKEN",  # Replace with your API token
}

# Snowflake connection details
SNOWFLAKE_CONFIG = {
    "user": "YOUR_SNOWFLAKE_USERNAME",
    "password": "YOUR_SNOWFLAKE_PASSWORD",
    "account": "YOUR_SNOWFLAKE_ACCOUNT",  # e.g., "abc123.east-us-2.azure"
    "warehouse": "YOUR_WAREHOUSE",
    "database": "YOUR_DATABASE",
    "schema": "YOUR_SCHEMA",
    "role": "YOUR_ROLE",  # Optional: specify if needed
}

# Target table in Snowflake
TARGET_TABLE = "YOUR_TABLE_NAME"

def fetch_api_data():
    """Fetch data from the API."""
    try:
        response = requests.get(API_URL, headers=API_HEADERS)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        data = response.json()  # Assume the API returns JSON
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def transform_data(data):
    """Transform the raw API data into a DataFrame."""
    try:
        # Convert data to a DataFrame (modify as needed based on your API structure)
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

def load_data_to_snowflake(df):
    """Load the DataFrame into the Snowflake table."""
    try:
        # Establish a connection to Snowflake
        conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
        
        # Use the write_pandas function for efficient loading
        success, num_rows, _ = write_pandas(conn, df, TARGET_TABLE)
        
        if success:
            print(f"Successfully loaded {num_rows} rows into {TARGET_TABLE}")
        else:
            print("Failed to load data into Snowflake.")
        
        # Close the connection
        conn.close()
    except Exception as e:
        print(f"Error loading data into Snowflake: {e}")

def main():
    """Main function to orchestrate the data pipeline."""
    # Step 1: Fetch data from API
    api_data = fetch_api_data()
    if api_data is None:
        return
    
    # Step 2: Transform data into a DataFrame
    data_df = transform_data(api_data)
    if data_df is None or data_df.empty:
        print("No data to load into Snowflake.")
        return

    # Step 3: Load the data into Snowflake
    load_data_to_snowflake(data_df)

if __name__ == "__main__":
    main()
    
import cx_Oracle 
try: 
    con=cx_Oracle.connect('scott/tiger@localhost') 
    cursor=con.cursor() 
    cursor.execute("select * from employees") 
    n=int(input("Enter the number of required rows:")) 
    data=cursor.fetchmany(n) 
    for row in data: 
        print(row) 
 except cx_Oracle.DatabaseError as e: 
     if con: 
        con.rollback() 
        print("There is a problem with sql :",e) 
finally: 
     if cursor: 
     cursor.close() 
     if con: 
     con.close()
