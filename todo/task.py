from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

with open('bd.json') as f:
    tasks = json.load(f)

if len(tasks)<0:
    with open("bd.json", "w", encoding="utf-8") as f:
        json.dump([], f)

def WriteTask():
    with open("bd.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file)

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add-task', methods=['POST'])
def addTask():
    taskName = request.form.get('new-task')
    if len(taskName)==0:
        return redirect('/')
    else:
        ids = []
        for task in tasks:
            ids.append(task.get('id'))
        if len(ids) == 0:
            m = 0
        else:
            m = max(ids)

        task = {
            'id': m + 1,
            "name": taskName

        }
        tasks.append(task)
        with open("bd.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file)
        return redirect('/')

@app.route('/remove-task', methods=['GET'])
def removeTask():
    taskId = int(request.args.get('id'))

    for task in tasks:
        if task.get('id') == taskId:
            tasks.remove(task)
    WriteTask()
    return redirect('/')


@app.route('/edit-task', methods=['GET'])
def editTask():
    taskId = int(request.args.get('id'))
    name = ''
    for task in tasks:
        if task.get('id') == taskId:
            name = task.get('name')
            WriteTask()
    return render_template('item-edit.html', taskValue=name, id=taskId)


@app.route('/save-task', methods=['POST'])
def saveTask():
    taskName = request.form.get('edit-task')
    taskId = int(request.form.get('id'))

    for task in tasks:
        if task.get('id') == taskId:
            task['name'] = taskName
        WriteTask()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
