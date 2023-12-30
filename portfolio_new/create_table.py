# Author: Aghara Christiana O, ALX_Africa
# Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called todos 
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this script:
# python create_table.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

cursor = conn.cursor()

sql_query = """CREATE TABLE IF NOT EXISTS todos (
        task_name TEXT NOT NULL,
        description TEXT,
        due_date DATE,
        priority TEXT,
        status TEXT,
        category TEXT,
        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completion_date TIMESTAMP,
        assigned_to TEXT
    )"""

    # Create the "todos" table
cursor.execute(sql_query)
print("Created table successfully!")

    # Commit the changes and close the connection
conn.commit()
conn.close()