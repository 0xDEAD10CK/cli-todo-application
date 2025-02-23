import inquirer
import os
import json


TODO_FILE = "todo_list.json"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create():
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



# Create a menu using inquirer
questions = [
    inquirer.List('action',
                    message="What do you want to do?",
                    choices=['Create a new Todo', 'Delete a Todo', 'Update a Todo', 'List all Todos'],
                ),
]

answers = inquirer.prompt(questions)

if answers['action'] == 'Create a new Todo':
    clear()
    create()
elif answers['action'] == 'Delete a Todo':
    clear()
    print('Deleting a Todo')
elif answers['action'] == 'Update a Todo':
    clear()
    print('Updating a Todo')
elif answers['action'] == 'List all Todos':
    clear()
    print('Listing all Todos')
else:
    clear()
    print('Invalid option')
