from task_cli.database import load_tasks, save_tasks
from task_cli.utils import get_prefilled_input
from rich.console import Console
from rich.table import Table
import datetime

def add_task(description: str):
    if not description:
        print("Please enter a valid description.")
        return

    data = load_tasks()
    max_id = 0
    for task in data["tasks"]:
        max_id = max(max_id, int(task["id"]))
    
    new_task = {
        "id": max_id + 1,
        "description": description.strip(),
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S.%f'),
        "updatedAt": None
    }
    data["tasks"].append(new_task)

    save_tasks(data)
    print(f"Task {new_task["id"]} created successfully.")


def list_tasks(status: str):
    data = load_tasks()
    tasks = data["tasks"]
    if status:
        tasks = [t for t in tasks if t["status"] == status]

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Description", min_width=20, max_width=35)
    table.add_column("Status", justify="right")
    table.add_column("Created at", width=10)
    table.add_column("Updated at", width=10)

    for t in tasks:
        # Convert from string to datetime obj
        t_createdAt_date_obj = datetime.datetime.strptime(t["createdAt"], '%d-%m-%y %H:%M:%S.%f')
        t_createdAt_date = t_createdAt_date_obj.date()

        if t["updatedAt"] is not None:
            t_updatedAt_date_obj = datetime.datetime.strptime(t["updatedAt"], '%d-%m-%y %H:%M:%S.%f')
            t_updatedAt_date = t_updatedAt_date_obj.date()

        color = "green" if t["status"] == "done" else "yellow"
        table.add_row(str(t["id"]), 
                      t["description"], 
                      f"[{color}]{t['status']}[/]",
                      t_createdAt_date.strftime('%d-%m-%y'),
                      t_updatedAt_date.strftime('%d-%m-%y') if t["updatedAt"] is not None else "",
                      )
    
    console.print(table)


def delete_task(task_id: int):
    data = load_tasks()

    #Validate if the task exists
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id]
    save_tasks(data)
    print(f"Task {task["id"]} deleted successfully.")



def update_task(task_id: int, description = None):
    if description != None and len(description.strip()) == 0:
        print("Please enter a valid description.")
        return
    
    data = load_tasks()
    
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if description is None:
        print(f"\nUpdating task {task_id}... Press [ctrl + c] to cancel.\n")
        try:
            description = get_prefilled_input("Description: ", task["description"])
        except KeyboardInterrupt:
            print("\nOperation canceled by user.\n")
            return

    if description != task["description"]: # if changes were made    
        # Update data 
        task["description"] = description
        task["updatedAt"] = datetime.datetime.now().strftime('%d-%m-%y %H:%M:%S.%f') # update time
        save_tasks(data)
        print(f"Task {task_id} updated successfully.")
    else:
        print("No changes made.")

def mark_in_progress(task_id: int):
    data = load_tasks()
    
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    print(f"Updating task {task_id}...")
    task["status"] = "in progress"
    save_tasks(data)
    print(f"Task {task_id} updated successfully.")


def mark_done(task_id: int):
    data = load_tasks()
    
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    print(f"Updating task {task_id}...")
    task["status"] = "done"
    save_tasks(data)
    print(f"Task {task_id} updated successfully.")


def mark_todo(task_id: int):
    data = load_tasks()
    
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    print(f"Updating task {task_id}...")
    task["status"] = "todo"
    save_tasks(data)
    print(f"Task {task_id} updated successfully.")
    