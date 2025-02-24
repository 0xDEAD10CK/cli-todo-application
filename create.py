import inquirer
import json
import os

def create():
    TODO_FILE = "todo_list.json"

    print("Create New Todo")

    todo = [
        inquirer.Text('title', message='Todo Name'),
        inquirer.List('priority', message='Priority', choices=["Low", "Medium", "High", "Urgent"]),
        inquirer.Text('due_date', message='Due Date')
    ]

    answers = inquirer.prompt(todo)

    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []  # Handle empty or corrupted files
    else:
        tasks = []


    # Determine the next ID
    next_id = tasks[-1]["id"] + 1 if tasks else 1

    # Create the new task
    new_task = {
        "id": next_id,
        "title": answers['title'],
        "status": "Pending",
        "priority": answers['priority'],
        "due_date": answers['due_date']
    }

    # Append and save
    tasks.append(new_task)
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)