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


def update_task(task_id: int, description: str):
    data = load_tasks()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["description"] = description
    save_tasks(data)
    