import argparse
import json
import os

def load_task():
    """ 
    Returns the data inside of the tasks JSON file
     - If the file doesn't exist or its empty returns a default dict 
    """
    if not os.path.exists("tasks.json"):
        return {"tasks": []}
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except json.JSONDecodeError: # JSON file exist but its empty
        return {"tasks": []}
    
def save_tasks(data):
    """ 
    Saves the data obtained frome the load_task func 
    """
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)


def add_task(description: str):
    data = load_task()
    max_id = 0
    for task in data["tasks"]:
        max_id = max(max_id, int(task["id"]))
    
    new_task = {
        "id": max_id + 1,
        "description": description,
        "status": "todo"
    }
    data["tasks"].append(new_task)

    save_tasks(data)


def list_tasks():
    data = load_task()
    for task in data["tasks"]:
        print(f"{task["id"]}:\t| {task["description"]} | {task["status"]}")

def delete_task(id: int):
    try:
        with open("./tasks.json") as file:
            data = json.load(file)
        
        with open("./tasks.json", "w") as file:
            for task in data["tasks"]:
                if int(task["id"]) == id:
                    data["tasks"].remove(task)
            json.dump(data, file)

    except FileNotFoundError:
        print("There was an error while trying to open the JSON file")


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # List command
    parser_list = subparsers.add_parser("list", help="Lists the current tasks")

    # Delete command 
    parser_add = subparsers.add_parser("delete", help="Deletes a task given its id.")
    parser_add.add_argument("id", type=int, help="Integer ID of the task to delete.")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)

    elif args.command == "list":
        list_tasks()

    elif args.command == "delete":
        delete_task(args.id)

if __name__ == "__main__":
    main()