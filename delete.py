import os
import json
import inquirer

def delete():
    TODO_FILE = "todo_list.json"

    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []  # Handle empty or corrupted files
    else:
        tasks = []

    if not tasks:
        print("No tasks to delete")
        return

    print("Delete a Todo")
    print("Select the Todo to delete")

    choices = []
    for task in tasks:
        choices.append(f"{task['id']}: {task['title']}")

    questions = [
        inquirer.List('task',
                        message="Select the Todo to delete",
                        choices=choices,
                    ),
    ]

    answers = inquirer.prompt(questions)

    task_id = int(answers['task'].split(":")[0])

    tasks = [task for task in tasks if task['id'] != task_id]

    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

    print("Todo deleted successfully")