import json 
import os
from pathlib import Path

# We get the path of this file.
# .parent gives us task_cli/
# .parent.parent is the root fo the project TASK-CLI/
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Definimos la ruta del JSON absoluta
DB_PATH = BASE_DIR / "tasks.json"

def load_tasks():
    """ 
    Returns the data inside of the tasks JSON file
     - If the file doesn't exist or its empty returns a default dict 
    """
    if not DB_PATH.exists():
        return {"tasks": []}
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError: # JSON file exist but its empty
        return {"tasks": []}
    
def save_tasks(data):
    """ 
    Saves the data obtained frome the load_task func 
    """
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)