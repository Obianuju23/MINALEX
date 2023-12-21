import sqlite3

def create_todo_table():
    # Connect to a database (this will create a new file if it doesn't exist)
    conn = sqlite3.connect("todo.sqlite")
    cursor = conn.cursor()

    sql_query = """CREATE TABLE IF NOT EXISTS todos (
        task_id INTEGER PRIMARY KEY,
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

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def insert_tasks():
    # Connect to the database
    conn = sqlite3.connect("todo.sqlite")
    cursor = conn.cursor()

    # Insert 5 tasks into the "todos" table
    tasks = [
        ('School preps', 'Get the kids to do their holiday project', '2024-01-05', 'High', 'in progress', 'Family', '2023-12-20', None, 'Muna'),
        ('Slides prep', 'Ensure the slides are ready', '2023-12-22', 'High', 'in progress', 'Skill acquisition', '2023-12-05', None, 'Uju'),
        ('Office schedules', 'Finish the task my boss gave me', '2023-12-17', 'High', 'completed', 'Official duty', '2023-12-10', '2023-12-15', 'Kings' ),
        ('Market errands', 'Get some grocery for the home', '2024-12-31', 'Medium', 'not started', 'Personal', '2023-12-25', None, 'Lota'),
        ('Project', 'Tidy up the project', '2024-01-05', 'High', 'in progress', 'Work', '2023-12-12', '2024-01-02', 'Tobe')
    ]

    # Insert each task
    for task in tasks:
        cursor.execute("""
        INSERT INTO todos 
        (task_name, description, due_date, priority, status, category, creation_date, completion_date, assigned_to)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, task)


    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # Run this script when executed directly
    create_todo_table()
    insert_tasks()