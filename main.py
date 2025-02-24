import inquirer
import os
import json

from create import create

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
