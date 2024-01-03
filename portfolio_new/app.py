# Author: Aghara Christiana O., ALX_Africa_Webstack_Portfolio_project
# Description: This is a Flask App that uses SQLite3 to
# execute (C)reate, (R)ead, (U)pdate, (D)elete operations

from flask import Flask
from flask_cors import CORS
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)
CORS(app)

# Home Page route
@app.route("/")
def home():
    """renders landing page"""
    return render_template("home.html")

# Route to form used to add a new student to the database
@app.route("/enternew")
def enternew():
    return render_template("Todo.html")

#Route to add a new record (INSERT) student data to the database
@app.route("/addrec", methods = ['POST', 'GET'])
def addrec():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            new_task_name = request.form["task_name"]
            new_description = request.form["description"]
            new_due_date = request.form["due_date"]
            new_priority = request.form["priority"]
            new_status = request.form["status"]
            new_category = request.form["category"]
            new_creation_date = request.form["creation_date"]
            new_completion_date = request.form["completion_date"]
            new_assigned_to = request.form["assigned_to"]
    
            # Connect to SQLite3 database and execute the INSERT
            with sqlite3.connect('database.sqlite') as conn:
                cursor = conn.cursor()
    
                sql = """INSERT INTO todos
                (task_name, description, due_date, priority, status, category, creation_date, completion_date, assigned_to)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

                cursor.execute(sql, ( new_task_name, new_description, new_due_date, new_priority, new_status, new_category, new_creation_date, new_completion_date, new_assigned_to))
                conn.commit()  
                msg = "Record successfully added to database"    
        except:
            conn.rollback()
            msg = "Error in the INSERT"

        finally:
            conn.close()
            # Send the transaction message to result.html
            return render_template('result.html', msg=msg)

# Route to SELECT all data from the database
@app.route('/list')
def list():
    # Use the provided database connection
    # SELECT rowid and all Rows from the students table.
    conn = sqlite3.connect("database.sqlite")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM todos")

    rows = cursor.fetchall()
    conn.close()
    # Send the results of the SELECT to the list.html page
    return render_template("list.html",rows=rows)

# Route that will SELECT a specific row in the database then load an Edit form 
@app.route("/edit", methods=['POST', 'GET'])
def edit():
    conn = None
    rows = None

    if request.method == 'POST':
        try:
            id = request.form['rowid']
            conn = sqlite3.connect("database.sqlite")
            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()
            cursor.execute("SELECT rowid, * FROM todos WHERE rowid = " + id)
            
            rows = cursor.fetchall()
        except sqlite3.Error as err:
            conn.rollback()
            msg = f"Error in the Edit: {str(err)}"
        finally:
            if conn is not None:
                conn.close()

    if rows is not None and len(rows) > 0:
        return render_template('edit.html', rows=rows)
    else:
        return render_template('no_data.html')  # Replace 'no_data.html' with the template you want to render when no data is available


# Route used to execute the UPDATE statement on a specific record in the database
@app.route("/editrec", methods=['POST', 'GET'])
def editrec():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the taskid
            rowid = request.form['rowid']
            new_task_name = request.form["new_task_name"]
            new_description = request.form["new_description"]
            new_due_date = request.form["new_due_date"]
            new_priority = request.form["new_priority"]
            new_status = request.form["new_status"]
            new_category = request.form["new_category"]
            new_creation_date = request.form["new_creation_date"]
            new_completion_date = request.form["new_completion_date"]
            new_assigned_to = request.form["new_assigned_to"]

            # UPDATE a specific record in the database based on the rowid
            with sqlite3.connect('database.sqlite') as conn:
                cursor = conn.cursor()

                # Use parameterized query to avoid SQL injection
                cursor.execute("""
                    UPDATE todos
                    SET
                        task_name=?,
                        description=?,
                        due_date=?,
                        priority=?,
                        status=?,
                        category=?,
                        creation_date=?,
                        completion_date=?,
                        assigned_to=?
                    WHERE rowid=?
                """, (new_task_name, new_description, new_due_date, new_priority, new_status, new_category, new_creation_date, new_completion_date, new_assigned_to, rowid))

                conn.commit()
                msg = "Record successfully edited in the database"
        except sqlite3.Error as e:
            conn.rollback()
            msg = f"Error in the Edit: {str(e)}"
        finally:
            conn.close()
            # Send the transaction message to result.html
            return render_template('result.html', msg=msg)
     
        
#Route used to DELETE a specific record in the database    
@app.route("/delete", methods=['POST', 'GET'])
def delete():
    conn = None  # Initialize conn to None
    msg = None  # Initialize msg to None

    if request.method == 'POST':
        try:
            # Use the hidden input value of id from the form to get the rowid
            id = request.form['rowid']
            # Connect to the database and DELETE a specific record based on rowid
            conn = sqlite3.connect('database.sqlite') # Using your existing database connection function
           
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos WHERE rowid=" + id)

            conn.commit()
            msg = "Record successfully deleted from the database"
        except sqlite3.Error as e:
            msg = f"Error in the DELETE: {str(e)}"
        finally:
            if conn is not None:
                conn.close()  # Check if conn is not None before closing
            # Send the transaction message to result.html
            return render_template('result.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
