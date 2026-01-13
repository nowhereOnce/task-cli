import argparse
import json
import os
from collections import defaultdict

def add_task(description: str):
    try:
        with open("./tasks.json", "r") as file:

            max_id = 0
            if os.stat("./tasks.json").st_size != 0: # If the file is NOT empty
                data = json.load(file) 
                for task in data["tasks"]: # Finds the maximum current id to store the new task
                    max_id = max(max_id, int(task["id"]))

            else: # Empty file
                data = defaultdict(list)             

        with open("tasks.json", "w") as file:
            new_task = {
                "id": max_id + 1,
                "description": description,
                "status": "todo"
            }
            
            data["tasks"].append(new_task)
            json.dump(data, file) # Saves into the JSON file

    except FileNotFoundError:
        print("There was an error while trying to open the JSON file")


def list_tasks():
    try:
        with open("./tasks.json") as file:
            data = json.load(file) 
            # Print format needs to be changed
            for task in data["tasks"]:
                print(f"{task["id"]}:\t{task["description"]} | {task["status"]}")

    except FileNotFoundError:
        print("There is no JSON file to read from")

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