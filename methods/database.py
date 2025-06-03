import psycopg2
import pandas as pd
from psycopg2.extras import execute_values
import os
from methods.scraper import scrape_courses

# This script initializes a PostgreSQL database and inserts data from a CSV file into it.

#TODO: Sraper as the first to run, then this file, at last app.py


# Try to get from system enviroment variable
# Set your Postgres user and password as second arguments of these two next function calls
user = os.environ.get('PGUSER', 'postgres')
password = os.environ.get('PGPASSWORD', 'admin')
host = os.environ.get('HOST', '127.0.0.1')

csv_file = 'df_cleaned.csv' 


def db_connection():
    """
    This function establishes a connection to the PostgreSQL database using the provided user, host, and password.
    Returns:
        conn: A connection object to the PostgreSQL database.
    """
    db = "dbname='courses' user=" + user + " host=" + host + " password =" + password
    conn = psycopg2.connect(db)
    return conn


def init_db():
    """
    This function initializes the PostgreSQL database by creating necessary tables and inserting data from a CSV file.
    """
    if not os.path.exists(csv_file):
        print("CSV file not found. Running scraper...")
        try:
            scrape_courses()
            print("Scraping completed.")
        except Exception as e:
            print(f"Error running scraper: {e}")
            return
    else:
        print("CSV file already exists, skipping scraper...")
    conn = db_connection()
    cur = conn.cursor()
    """    cur.execute('''DROP TABLE IF EXISTS scores;''')
    cur.execute('''DROP TABLE IF EXISTS users;''')
    cur.execute('''DROP TABLE IF EXISTS kucourses1;''')"""
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL
                );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS scores (
                    score_id SERIAL PRIMARY KEY,
                    user_id INT NOT NULL,
                    score_value INT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );''')
    cur.execute('''CREATE TABLE IF NOT EXISTS kucourses1 (
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
                );''')

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
        cur.execute(insert_query, data)
    conn.commit()
    cur.close()
    conn.close()

init_db()