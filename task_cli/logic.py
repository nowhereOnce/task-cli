import readline
from task_cli.database import load_tasks, save_tasks

def add_task(description: str):
    data = load_tasks()
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
    data = load_tasks()
    for task in data["tasks"]:
        print(f"{task["id"]}:\t| {task["description"]} | {task["status"]}")


def delete_task(task_id: int):
    data = load_tasks()
    data["tasks"] = [t for t in data["tasks"] if t["id"] != task_id]
    save_tasks(data)


def update_task(task_id: int, description = None):
    data = load_tasks()
    
    task = next((t for t in data["tasks"] if t["id"] == task_id), None)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if description is None:
        
        def prefill_input(prompt, prefill=''):
            readline.set_startup_hook(lambda: readline.insert_text(prefill))
            try:
                return input(prompt)
            finally:
                readline.set_startup_hook()

        print(f"Updating task {task_id}...")
        description = prefill_input("Description: ", task["description"])

    # Update data 
    task["description"] = description
    save_tasks(data)
    print(f"Task {task_id} updated successfully.")
    

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