import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

# Database connection parameters - modify these
db_params = {
    'dbname': 'courses',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

# Path to the CSV file
csv_file = '/Users/antonbarslund/Documents/GitHub/DISGroup/df_cleaned.csv'

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create the table if it doesn't exist
create_table_query = '''
DROP TABLE IF EXISTS kucourses1;
CREATE TABLE IF NOT EXISTS kucourses1 (
    course_id TEXT,
    title TEXT,
    level TEXT,
    length NUMERIC,
    timeslot TEXT,
    group_name TEXT, 
    description TEXT,
    exam_type TEXT,
    pass_pct TEXT,
    median TEXT,
    mean TEXT,
    fail_pct NUMERIC
);
'''
cursor.execute(create_table_query)
conn.commit()

# Read the CSV file
df = pd.read_csv(csv_file)

# Rename the 'group' column to 'group_name' (since 'group' is a reserved SQL keyword)
if 'group' in df.columns:
    df = df.rename(columns={'group': 'group_name'})

# Insert data row by row
for _, row in df.iterrows():
    # Create the INSERT statement
    insert_query = '''
    INSERT INTO kucourses1 (course_id, title, level, length, timeslot, group_name, 
                            description, exam_type, pass_pct, median, mean, fail_pct)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    
    # Prepare the data as a tuple
    data = (
        row['course_id'],
        row['title'],
        row['level'],
        row['length'],
        row['timeslot'],
        row['group_name'],
        row['description'],
        row['exam_type'],
        row['pass_pct'],
        row['median'],
        row['mean'],
        row['fail_pct']
    )
    
    # Execute the INSERT statement
    cursor.execute(insert_query, data)

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")