import argparse
import json

def add_task(description: str):
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file) # Python dictionary?
            data_tasks = data["tasks"]
            max_id = 0

            for task in data_tasks: # Finds the maximum current id to store the new task
                max_id = max(max_id, int(task["id"]))
        
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
            print(json.dumps(data, indent=2))
    except FileNotFoundError:
        print("There is no JSON file to read from")



def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # List command
    parrser_add = subparsers.add_parser("list", help="Lists the current tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)

    elif args.command == "list":
        list_tasks()


if __name__ == "__main__":
    main()