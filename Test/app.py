from flask import Flask, jsonify, request

app = Flask(__name__)

todo_list = [
    {
        "id": 0,
        "Task_description": "Home chores",
        "Task_status": "Still in progress,",
    }
    {
        "id": 1,
        "Task_description": "Office project",
        "Task_status": "Complete,"
    }
    {
        "id": 1,
        "Task_description": "Market errands",
        "Task_status": "not started"
    }
    
]

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'GET':
        if len(todo_list) > 0:
            return jsonify(todo_list)
        else:
            'Nothing Found',404

    if request.method == 'POST':
        new_Task_description = request.form['Task_description']
        new_Task_status = request.form['Task_status']
        iD = todo_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'Task_description': new_Task_description,
            'Task_status': new_Task_status
        }
        todo_list.append(new_obj)
        return jsonify(todo_list), 201
if __name__ == '__main__':
    app.run()
